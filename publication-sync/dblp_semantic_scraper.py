#!/usr/bin/env python3
"""
Publication fetcher + missing-paper detector for lab website updates.

Pulls publication metadata from DBLP (primary source, curated) and
optionally Semantic Scholar (to catch very recent items DBLP hasn't
indexed yet), then:

  1. Scans the EXISTING website's publication folders (EXISTING_SITE_DIR),
     reads each index.md's `title:` field, and diffs it against the
     fetched papers (fetched in full from DBLP/S2 -- neither has a "what's
     new" query, so the full list has to be pulled every run to compute
     this diff) to find which ones are NOT yet on the site.
  2. Writes a Markdown report of just the missing papers (MISSING_REPORT_PATH)
     and, if GENERATE_MISSING_FOLDERS is True, generates ready-to-use
     folder+index.md entries for ONLY the missing papers (MISSING_PAPERS_DIR)
     so you can review and drop them straight into the site repo.

Configure the CONFIG block below and run:
    pip install requests pyyaml
    python scholar_scraper.py

Notes:
    - DBLP: any profile URL works; the script reads the PID from it and
      queries DBLP's public SPARQL endpoint. The per-person XML export
      is behind a bot check and no longer returns XML to plain HTTP clients.
    - Semantic Scholar author ID: the numeric ID at the end of the
      profile URL, e.g. https://www.semanticscholar.org/author/Vera-Schmitt/1234567
      -> id is "1234567". Set to None to skip it.
    - This script does NOT touch Google Scholar. Scholar has no public
      API, disallows scraping in its ToS, and aggressively rate-limits/
      CAPTCHAs automated requests. DBLP + Semantic Scholar cover the same
      metadata without those problems.
    - Year filter: set YEAR for a single year, or MIN_YEAR/MAX_YEAR for
      a range. Leave all three as None for no filtering.
    - Matching for the "missing" diff is done on a normalized title
      (lowercased, alphanumeric-only), so minor punctuation/spacing
      differences between DBLP/S2 and the site won't cause false positives.
      Still, always eyeball the missing-report before bulk-adding folders --
      title drift (e.g. a preprint title vs. camera-ready title) can cause
      a paper to look "missing" when it's actually already there.
"""

import difflib
import os
import re
import sys
import unicodedata
from pathlib import Path
from os import PathLike
import requests
import yaml
from config import cfg

# ----------------------------- CONFIG -----------------------------
DBLP_URL = cfg.dblp_url #"https://dblp.org/pid/295/6533.html"
SEMANTIC_SCHOLAR_ID = cfg.semantic_scholar_id #"2114572998"

# Path to the website repo's existing publications folder
# (one subfolder per paper, each containing an index.md).
EXISTING_SITE_DIR = cfg.existing_site_dir #"/Users/swarnadeep/Riju/Code/academic/XplaiNLP/xplainlp.github.io/content/publication"

MISSING_REPORT_PATH = cfg.missing_report_path #"/Users/swarnadeep/Riju/Code/academic/XplaiNLP/scrapper/data/output/missing_publications.md"
MISSING_PAPERS_DIR = cfg.missing_papers_dir #"/Users/swarnadeep/Riju/Code/academic/XplaiNLP/scrapper/data/output/missing_papers"
GENERATE_MISSING_FOLDERS = cfg.generate_missing_folders #True  # if True, also write ready-to-use folders for missing papers only

YEAR = cfg.year             # e.g. 2025 -> only that year (overrides MIN_YEAR/MAX_YEAR)
MIN_YEAR = cfg.min_year          # e.g. 2023 -> 2023 onward
MAX_YEAR = cfg.max_year          # e.g. 2024 -> up to and including 2024

# Minimum title-similarity ratio (0-1) for treating an arXiv/preprint entry
# and a real-venue entry as the SAME paper. Only applies when one side is a
# preprint venue and the other isn't -- two real, distinct papers are never
# merged by this, no matter how similar their titles look.
ARXIV_TITLE_SIMILARITY_THRESHOLD = cfg.arxiv_similarity_threshold #0.7
# --------------------------------------------------------------------

DBLP_HEADERS = cfg.http_headers#{"User-Agent": "lab-website-publication-sync/1.0"}

# DBLP appends a 4-digit disambiguation suffix to author names that collide
# with another researcher of the same name, e.g. "Sebastian Möller 0001".
# This is meant to stay internal to DBLP and should be stripped for display.
_DBLP_AUTHOR_SUFFIX_RE = re.compile(r"\s+\d{4}$")


def clean_author_name(name: str) -> str:
    return _DBLP_AUTHOR_SUFFIX_RE.sub("", name.strip())

# DBLP entry tag -> CSL publication_types value used by Hugo Academic
PUBLICATION_TYPE_MAP = {
    "article": "article-journal",
    "inproceedings": "paper-conference",
    "incollection": "chapter",
    "book": "book",
    "phdthesis": "thesis",
    "mastersthesis": "thesis",
}
DEFAULT_PUBLICATION_TYPE = "manuscript"


# Public SPARQL endpoint. The per-person XML export
# (https://dblp.org/pid/<id>.xml) is fronted by a bot check and answers
# plain HTTP clients with an HTML interstitial, which is what used to
# blow up ElementTree with "syntax error: line 1, column 0".
DBLP_SPARQL_ENDPOINT = "https://sparql.dblp.org/sparql"
_DBLP_SPARQL_PAGE = 500
_BIBTEX_NS = "http://purl.org/net/nknouf/ns/bibtex#"
_DOI_PREFIXES = (
    "https://doi.org/",
    "http://doi.org/",
    "https://dx.doi.org/",
    "http://dx.doi.org/",
)

# DBLP indexes more than just papers under a person's profile -- datasets,
# software, homepages, and edited-volume records show up as different
# bibtex types too. Only these types represent an actual authored publication;
# anything else (e.g. "misc"/"data" for datasets and software, edited
# volumes, proceedings) is excluded so it never enters the pipeline as if
# it were a paper.
_DBLP_PAPER_TAGS = {
    "article", "inproceedings", "incollection", "book",
    "phdthesis", "mastersthesis",
}


def dblp_person_uri(profile_url: str) -> str:
    """Return the DBLP person IRI for a profile URL (.html, .xml, or bare)."""
    cleaned = profile_url.strip().split("?", 1)[0].split("#", 1)[0]
    for suffix in (".html", ".xml", ".json"):
        if cleaned.endswith(suffix):
            cleaned = cleaned[: -len(suffix)]
    cleaned = cleaned.rstrip("/")
    marker = "/pid/"
    idx = cleaned.find(marker)
    if idx == -1:
        raise ValueError(f"Not a DBLP person profile URL: {profile_url}")
    pid = cleaned[idx + len(marker):]
    if not re.fullmatch(r"[A-Za-z0-9._-]+/[A-Za-z0-9._-]+", pid):
        raise ValueError(f"Unexpected DBLP PID in URL: {profile_url}")
    return f"https://dblp.org/pid/{pid}"


def _dblp_sparql(query: str) -> list[dict]:
    headers = dict(DBLP_HEADERS or {})
    headers["Accept"] = "application/sparql-results+json"
    resp = requests.post(
        DBLP_SPARQL_ENDPOINT,
        data={"query": query},
        headers=headers,
        timeout=60,
    )
    resp.raise_for_status()
    content_type = resp.headers.get("Content-Type", "")
    if "json" not in content_type.lower():
        raise RuntimeError(
            "DBLP SPARQL endpoint did not return JSON "
            f"({resp.status_code} {content_type}): {resp.text[:160]!r}"
        )
    payload = resp.json()
    if payload.get("status") == "ERROR":
        raise RuntimeError(payload.get("exception") or "DBLP SPARQL query failed")
    return payload.get("results", {}).get("bindings", [])


def _sparql_pages(make_query) -> list[dict]:
    rows = []
    offset = 0
    while True:
        page = _dblp_sparql(make_query(offset, _DBLP_SPARQL_PAGE))
        rows.extend(page)
        if len(page) < _DBLP_SPARQL_PAGE:
            return rows
        offset += _DBLP_SPARQL_PAGE


def _binding(row: dict, key: str) -> str | None:
    cell = row.get(key)
    if not cell:
        return None
    value = cell.get("value")
    return value or None


def _bibtex_tag(iri: str | None) -> str | None:
    if iri and iri.startswith(_BIBTEX_NS):
        return iri[len(_BIBTEX_NS):].lower()
    return None


def _bare_doi(value: str | None) -> str | None:
    if not value:
        return None
    lowered = value.lower()
    for prefix in _DOI_PREFIXES:
        if lowered.startswith(prefix):
            return value[len(prefix):]
    return value


def _fetch_dblp_publications(person_uri: str) -> dict[str, dict]:
    def make_query(offset: int, limit: int) -> str:
        return f"""
PREFIX dblp: <https://dblp.org/rdf/schema#>
SELECT ?publ ?title ?year ?venue ?page ?doi ?bibtype WHERE {{
  ?publ dblp:authoredBy <{person_uri}> .
  ?publ dblp:title ?title .
  OPTIONAL {{ ?publ dblp:yearOfPublication ?year . }}
  OPTIONAL {{ ?publ dblp:publishedIn ?venue . }}
  OPTIONAL {{ ?publ dblp:primaryDocumentPage ?page . }}
  OPTIONAL {{ ?publ dblp:doi ?doi . }}
  OPTIONAL {{ ?publ dblp:bibtexType ?bibtype . }}
}}
ORDER BY ?publ
LIMIT {limit}
OFFSET {offset}
"""

    records: dict[str, dict] = {}
    for row in _sparql_pages(make_query):
        publ = _binding(row, "publ")
        title = _binding(row, "title")
        if not publ or not title:
            continue
        rec = records.get(publ)
        if rec is None:
            rec = {
                "title": title.strip().rstrip("."),
                "year": _binding(row, "year"),
                "venue": _binding(row, "venue"),
                "link": _binding(row, "page") or publ,
                "doi": _bare_doi(_binding(row, "doi")),
                "type": _bibtex_tag(_binding(row, "bibtype")),
            }
            records[publ] = rec
            continue
        rec["venue"] = rec["venue"] or _binding(row, "venue")
        rec["link"] = rec["link"] or _binding(row, "page") or publ
        rec["doi"] = rec["doi"] or _bare_doi(_binding(row, "doi"))
        rec["type"] = rec["type"] or _bibtex_tag(_binding(row, "bibtype"))
    return records


def _fetch_dblp_authors(person_uri: str) -> dict[str, list[str]]:
    def make_query(offset: int, limit: int) -> str:
        return f"""
PREFIX dblp: <https://dblp.org/rdf/schema#>
SELECT ?publ ?ordinal ?name WHERE {{
  ?publ dblp:authoredBy <{person_uri}> .
  ?publ dblp:hasSignature ?sig .
  ?sig a dblp:AuthorSignature .
  ?sig dblp:signatureOrdinal ?ordinal .
  ?sig dblp:signatureDblpName ?name .
}}
ORDER BY ?publ ?ordinal
LIMIT {limit}
OFFSET {offset}
"""

    by_publ: dict[str, dict[int, str]] = {}
    for row in _sparql_pages(make_query):
        publ = _binding(row, "publ")
        name = _binding(row, "name")
        ordinal = _binding(row, "ordinal")
        if not publ or not name or ordinal is None:
            continue
        try:
            position = int(ordinal)
        except ValueError:
            continue
        by_publ.setdefault(publ, {})[position] = clean_author_name(name)
    return {
        publ: [names[pos] for pos in sorted(names)]
        for publ, names in by_publ.items()
    }


def fetch_dblp(profile_url: str) -> list[dict]:
    person_uri = dblp_person_uri(profile_url)
    records = _fetch_dblp_publications(person_uri)
    authors = _fetch_dblp_authors(person_uri)

    pubs = []
    skipped_non_paper = 0
    for publ, rec in records.items():
        if rec["type"] not in _DBLP_PAPER_TAGS:
            skipped_non_paper += 1
            continue
        pubs.append(
            {
                "title": rec["title"],
                "authors": authors.get(publ, []),
                "year": rec["year"],
                "venue": rec["venue"],
                "link": rec["link"],
                "doi": rec["doi"],
                "abstract": None,
                "type": rec["type"],
                "source": "dblp",
                "dblp_key": publ.removeprefix("https://dblp.org/rec/")
                if publ.startswith("https://dblp.org/rec/") else None,
            }
        )

    if skipped_non_paper:
        print(
            f"  (excluded {skipped_non_paper} non-paper DBLP record(s): "
            f"datasets, software, homepages, edited volumes, etc.)",
            file=sys.stderr,
        )

    return pubs


# Semantic Scholar publicationTypes -> our type (first match in this priority order wins)
_S2_TYPE_PRIORITY = [
    ("Conference", "inproceedings"),
    ("BookSection", "incollection"),
    ("Book", "book"),
    ("JournalArticle", "article"),
]


_VENUE_JOURNAL_WORDS = ("journal", "transactions")
_VENUE_CONFERENCE_WORDS = ("proceedings", "workshop", "conference", "symposium", "findings")


def _s2_year(year: str | None, venue: str | None, title: str) -> str | None:
    """S2 sometimes reports the preprint year for a paper that was published
    later. If the venue name contains exactly one year and it is LATER than
    S2's year (e.g. "... (TrustNLP 2026)" vs 2025), use the venue's year."""
    if not year or not venue or is_preprint_venue(venue):
        return year
    venue_years = set(re.findall(r"\b(20\d{2})\b", venue))
    if len(venue_years) == 1:
        venue_year = venue_years.pop()
        if int(venue_year) > int(year):
            print(f"  (year adjusted {year} -> {venue_year} from venue name: {title[:60]!r})",
                  file=sys.stderr)
            return venue_year
    return year


def _s2_type(paper: dict, venue: str | None, arxiv_id: str | None) -> str:
    """Map Semantic Scholar's publicationTypes to our type.
    Preprints (arXiv.org venue, or an arXiv ID and no venue) stay "unknown",
    because S2 labels them "JournalArticle" even though they aren't."""
    if is_preprint_venue(venue) or (arxiv_id and not venue):
        return "unknown"
    kinds = paper.get("publicationTypes") or []
    for kind, mapped in _S2_TYPE_PRIORITY:
        if kind in kinds:
            return mapped
    # S2 often leaves publicationTypes empty for new papers: guess from the venue name.
    v = (venue or "").lower()
    if any(w in v for w in _VENUE_JOURNAL_WORDS) or "national academy" in v:
        return "article"
    if any(w in v for w in _VENUE_CONFERENCE_WORDS):
        return "inproceedings"
    return "unknown"


def _s2_link(paper: dict, venue: str | None, doi: str | None, arxiv_id: str | None) -> str | None:
    """Prefer a link that goes to the paper itself over the Semantic Scholar page:
    arXiv for preprints, the DOI for published papers, then arXiv, then S2."""
    is_preprint = is_preprint_venue(venue) or (arxiv_id and not venue)
    if arxiv_id and is_preprint:
        return f"https://arxiv.org/abs/{arxiv_id}"
    if doi:
        return f"https://doi.org/{doi}"
    if arxiv_id:
        return f"https://arxiv.org/abs/{arxiv_id}"
    return paper.get("url")


def _s2_paper_to_pub(p: dict) -> dict:
    external_ids = p.get("externalIds") or {}
    venue = p.get("venue") or None
    doi = external_ids.get("DOI")
    arxiv_id = external_ids.get("ArXiv")
    return {
        "title": (p.get("title") or "").strip().rstrip("."),
        "authors": [a.get("name") for a in p.get("authors", [])],
        "year": _s2_year(str(p["year"]) if p.get("year") else None, venue,
                         (p.get("title") or "").strip()),
        "venue": venue,
        "link": _s2_link(p, venue, doi, arxiv_id),
        "doi": doi,
        "arxiv_id": arxiv_id,
        "abstract": p.get("abstract"),
        "type": _s2_type(p, venue, arxiv_id),
        "source": "semantic_scholar",
    }


def fetch_semantic_scholar(author_id: str) -> list[dict]:
    url = f"https://api.semanticscholar.org/graph/v1/author/{author_id}/papers"
    params = {
        "fields": "title,authors,venue,year,externalIds,url,abstract,publicationTypes",
        "limit": 1000,
    }
    resp = requests.get(url, params=params, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    return [_s2_paper_to_pub(p) for p in data.get("data", [])]


# ---------------------------- arXiv ID helper ----------------------------

_ARXIV_ID_PATTERNS = [
    re.compile(r"arxiv\.org/(?:abs|pdf)/([^\s?#]+?)(?:v\d+)?(?:\.pdf)?/?$", re.I),
    re.compile(r"10\.48550/arxiv\.(.+?)(?:v\d+)?$", re.I),
]


def arxiv_id_of(p: dict) -> str | None:
    """arXiv ID from an explicit field, the DOI (10.48550/arXiv.*), or the link."""
    if p.get("arxiv_id"):
        return p["arxiv_id"]
    for text in (p.get("doi"), p.get("link")):
        for rx in _ARXIV_ID_PATTERNS:
            m = rx.search(text or "")
            if m:
                return m.group(1)
    return None


# ---------------------------- author accents ----------------------------

_NAME_TRANSLIT = str.maketrans({
    "ß": "ss", "ø": "o", "Ø": "O", "æ": "ae", "Æ": "AE",
    "đ": "d", "Đ": "D", "ł": "l", "Ł": "L", "ð": "d", "þ": "th",
})


def _fold_name(name: str) -> str:
    """Lowercase, accent-free, letters/digits/spaces only -- for comparing names."""
    t = unicodedata.normalize("NFKD", name.translate(_NAME_TRANSLIT))
    t = t.encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", t)).strip()


def restore_author_accents(pubs: list[dict]) -> int:
    """Semantic Scholar often drops accents ("Moller" for "Möller"). Wherever the
    same name (ignoring accents) appears WITH accents anywhere in our data
    (typically DBLP), use that spelling. Ambiguous names are left alone.
    Names that never appear with accents in the data can't be restored.
    Returns the number of names fixed."""
    known: dict[str, str | None] = {}
    for p in pubs:
        for a in p.get("authors") or []:
            if a and not a.isascii():
                key = _fold_name(a)
                if key in known and known[key] != a:
                    known[key] = None  # two different accented spellings -> ambiguous
                else:
                    known[key] = a

    fixed = 0
    for p in pubs:
        authors = p.get("authors") or []
        updated = []
        for a in authors:
            replacement = known.get(_fold_name(a)) if a and a.isascii() else None
            if replacement and replacement != a:
                updated.append(replacement)
                fixed += 1
            else:
                updated.append(a)
        if updated != authors:
            p["authors"] = updated
    return fixed


def normalize_title(title: str | None) -> str:
    return "".join(ch.lower() for ch in (title or "") if ch.isalnum())


def merge_publications(dblp_pubs: list[dict], s2_pubs: list[dict]) -> list[dict]:
    """DBLP entries take priority; add S2 entries whose title isn't already present.
    Also backfill DBLP entries with abstract/doi from S2 when available, matched by title."""
    s2_by_title = {normalize_title(p["title"]): p for p in s2_pubs if p["title"]}

    merged = []
    seen_titles = set()
    for p in dblp_pubs:
        key = normalize_title(p["title"])
        s2_match = s2_by_title.get(key)
        if s2_match:
            p = dict(p)
            p["abstract"] = p.get("abstract") or s2_match.get("abstract")
            p["doi"] = p.get("doi") or s2_match.get("doi")
            p["arxiv_id"] = p.get("arxiv_id") or s2_match.get("arxiv_id")
        merged.append(p)
        seen_titles.add(key)

    for p in s2_pubs:
        key = normalize_title(p["title"])
        if key and key not in seen_titles:
            merged.append(p)
            seen_titles.add(key)

    return merged


# Venue strings that indicate a preprint/non-peer-reviewed listing, rather
# than the actual published venue. Checked as a substring, case-insensitive.
_PREPRINT_VENUE_MARKERS = ["arxiv", "corr"]


def is_preprint_venue(venue: str | None) -> bool:
    if not venue:
        return False
    v = venue.lower()
    return any(marker in v for marker in _PREPRINT_VENUE_MARKERS)


def title_similarity(a: str | None, b: str | None) -> float:
    """Similarity ratio (0-1) between two normalized titles."""
    return difflib.SequenceMatcher(None, normalize_title(a), normalize_title(b)).ratio()


def dedupe_arxiv_duplicates(
    pubs: list[dict], threshold: float = ARXIV_TITLE_SIMILARITY_THRESHOLD
) -> list[dict]:
    """Collapse cases where the same paper appears twice -- once as an
    arXiv/preprint listing, once under its real venue -- with a slightly
    different title (e.g. workshop-shortened title, added subtitle).

    Only merges when one side is a preprint venue and the other is NOT --
    this is what makes it safe: two genuinely different real papers with
    similar titles are never touched, since neither would be a preprint
    venue and the gate below simply won't fire for that pair.

    When a match is found, the real-venue entry is kept (title/venue/link/
    type come from it), backfilled with abstract/doi from the preprint
    entry if the real-venue entry is missing them.
    """

    preprint_pubs = [p for p in pubs if is_preprint_venue(p.get("venue"))]
    real_pubs = [p for p in pubs if not is_preprint_venue(p.get("venue"))]

    merged_preprint_ids = set()
    for pp in preprint_pubs:
        for rp in real_pubs:
            if title_similarity(pp.get("title"), rp.get("title")) >= threshold:
                rp["abstract"] = rp.get("abstract") or pp.get("abstract")
                # Never give a published paper the preprint's own arXiv DOI.
                pp_doi = pp.get("doi")
                if pp_doi and pp_doi.lower().startswith("10.48550/arxiv."):
                    pp_doi = None
                rp["doi"] = rp.get("doi") or pp_doi
                rp["arxiv_id"] = rp.get("arxiv_id") or arxiv_id_of(pp)
                merged_preprint_ids.add(id(pp))
                break

    return real_pubs + [pp for pp in preprint_pubs if id(pp) not in merged_preprint_ids]


def filter_by_year(pubs: list[dict], min_year: int | None, max_year: int | None) -> list[dict]:
    if min_year is None and max_year is None:
        return pubs

    filtered = []
    for p in pubs:
        year = p.get("year")
        if year is None:
            continue
        try:
            y = int(year)
        except ValueError:
            continue
        if min_year is not None and y < min_year:
            continue
        if max_year is not None and y > max_year:
            continue
        filtered.append(p)
    return filtered


def to_markdown(pubs: list[dict], header: str = "# Publications") -> str:
    def sort_key(p):
        try:
            return -int(p["year"])
        except (TypeError, ValueError):
            return 0

    pubs_sorted = sorted(pubs, key=sort_key)

    lines = [header, ""]
    current_year = None
    for p in pubs_sorted:
        year = p.get("year") or "n.d."
        if year != current_year:
            lines.append(f"## {year}")
            lines.append("")
            current_year = year

        authors = ", ".join(p.get("authors") or []) or "Unknown authors"
        venue = p.get("venue")
        title = p.get("title", "Untitled")
        link = p.get("link")

        entry = f"**{title}**  \n{authors}"
        if venue:
            entry += f"  \n_{venue}_"
        if link:
            entry += f"  \n[Link]({link})"

        lines.append(entry)
        lines.append("")

    return "\n".join(lines)


# ------------------------ Existing-site scanning ------------------------

def parse_existing_titles(existing_dir: Path) -> set[str]:
    """Walk the existing site's publication folders, parse each index.md's
    YAML front matter, and return a set of normalized titles."""
    if not os.path.isdir(existing_dir):
        print(f"WARNING: existing site dir not found: {existing_dir}", file=sys.stderr)
        return set()

    titles = set()
    for entry in sorted(os.listdir(existing_dir)):
        index_path = os.path.join(existing_dir, entry, "index.md")
        if not os.path.isfile(index_path):
            continue

        with open(index_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Front matter is between the first two '---' lines.
        parts = content.split("---", 2)
        if len(parts) < 3:
            print(f"  skip (no front matter): {index_path}", file=sys.stderr)
            continue

        try:
            front_matter = yaml.safe_load(parts[1]) or {}
        except yaml.YAMLError as e:
            print(f"  skip (YAML parse error in {index_path}): {e}", file=sys.stderr)
            continue

        title = front_matter.get("title")
        if title:
            titles.add(normalize_title(title))

    return titles


def find_missing(pubs: list[dict], existing_titles: set[str]) -> list[dict]:
    return [p for p in pubs if normalize_title(p.get("title")) not in existing_titles]


# ------------------------ Hugo Academic index.md ------------------------

def slugify(title: str, max_len: int = 60) -> str:
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug).strip("-")
    return slug[:max_len].rstrip("-") or "untitled"


def yaml_single_quote(text: str) -> str:
    return "'" + (text or "").replace("'", "''") + "'"


def yaml_block_literal(text: str, indent: int = 4) -> str:
    if not text:
        return ""
    pad = " " * indent
    wrapped_lines = text.strip().splitlines() or [text.strip()]
    return "\n".join(pad + line for line in wrapped_lines)


def build_index_md(p: dict) -> str:
    title = p.get("title") or "Untitled"
    authors = p.get("authors") or []
    year = p.get("year")
    venue = p.get("venue") or ""
    link = p.get("link") or ""
    doi = p.get("doi") or ""
    abstract = p.get("abstract") or ""

    subtitle = ", ".join(authors)
    if venue or year:
        subtitle += f" - {venue}{(' ' + year) if year else ''}".rstrip()

    date_str = f"{year}-01-01T00:00:00Z" if year else ""
    pub_type = PUBLICATION_TYPE_MAP.get(p.get("type") or "", DEFAULT_PUBLICATION_TYPE)

    authors_yaml = "\n".join(f"- {a}" for a in authors) if authors else "- "

    abstract_block = (
        f"abstract: |\n{yaml_block_literal(abstract)}" if abstract else "abstract: "
    )

    return f"""---
title: {yaml_single_quote(title)}
subtitle: {yaml_single_quote(subtitle)}
# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
{authors_yaml}
# Author notes (optional)
author_notes:
date: {yaml_single_quote(date_str)}
doi: {yaml_single_quote(doi)}
# Schedule page publish date (NOT publication's date).
publishDate: {yaml_single_quote(date_str)}
# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['{pub_type}']
# Publication name and optional abbreviated publication name.
publication: {yaml_single_quote(venue)}
publication_short:
{abstract_block}
# Summary. An optional shortened abstract.
summary:
tags: []
# Display this page in the Featured widget?
featured: false
# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org
url_pdf: {yaml_single_quote(link)}
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''
# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: ''
  focal_point: ''
  preview_only: false
# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []
# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---
"""


# ----------------------------- BibTeX (cite.bib) -----------------------------
# DBLP's own .bib download sits behind the same bot check as the XML export,
# so the BibTeX is built here from the metadata we already collect. Hugo
# Academic-style themes show a "Cite" button when a page folder has cite.bib.

_BIB_ESCAPES = {"&": r"\&", "%": r"\%", "_": r"\_", "#": r"\#"}

# our publication type -> (BibTeX entry type, field that holds the venue)
_BIB_ENTRY_TYPES = {
    "inproceedings": ("inproceedings", "booktitle"),
    "article": ("article", "journal"),
    "incollection": ("incollection", "booktitle"),
}

_BIB_TITLE_STOPWORDS = {"a", "an", "the", "on", "of", "for", "in", "to", "and", "with"}


def _bib_escape(text: str) -> str:
    return "".join(_BIB_ESCAPES.get(ch, ch) for ch in text)


def _ascii_slug(text: str) -> str:
    folded = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", folded.lower())


def bibtex_key(p: dict) -> str:
    """DBLP-style key when we know the DBLP record, else lastname+year+word."""
    if p.get("dblp_key"):
        return "DBLP:" + p["dblp_key"]
    authors = p.get("authors") or []
    last = _ascii_slug(authors[0].split()[-1]) if authors else "anon"
    words = [w for w in re.findall(r"[A-Za-z0-9]+", p.get("title") or "")
             if w.lower() not in _BIB_TITLE_STOPWORDS]
    first_word = _ascii_slug(words[0]) if words else "paper"
    return f"{last or 'anon'}{p.get('year') or ''}{first_word}"


def build_bibtex(p: dict) -> str:
    entry_type, venue_field = _BIB_ENTRY_TYPES.get(p.get("type") or "", ("misc", None))

    fields: list[tuple[str, str]] = []
    authors = p.get("authors") or []
    if authors:
        fields.append(("author", " and ".join(_bib_escape(a) for a in authors)))
    fields.append(("title", _bib_escape(p.get("title") or "Untitled")))
    aid = arxiv_id_of(p)
    skip_venue = entry_type == "misc" and aid and is_preprint_venue(p.get("venue"))
    if p.get("venue") and not skip_venue:
        fields.append((venue_field or "howpublished", _bib_escape(p["venue"])))
    if p.get("year"):
        fields.append(("year", str(p["year"])))
    if p.get("doi"):
        fields.append(("doi", p["doi"]))
    if p.get("link"):
        fields.append(("url", p["link"]))
    if aid:
        fields.append(("eprinttype", "arXiv"))
        fields.append(("eprint", aid))

    body = ",\n".join(f"  {name} = {{{value}}}" for name, value in fields)
    return f"@{entry_type}{{{bibtex_key(p)},\n{body}\n}}\n"


def write_paper_folders(pubs: list[dict], papers_dir: Path) -> None:
    os.makedirs(papers_dir, exist_ok=True)
    used_slugs = set()

    for p in pubs:
        base_slug = slugify(p.get("title") or "untitled")
        slug = base_slug
        n = 2
        while slug in used_slugs:
            slug = f"{base_slug}-{n}"
            n += 1
        used_slugs.add(slug)

        folder = os.path.join(papers_dir, slug)
        os.makedirs(folder, exist_ok=True)
        with open(os.path.join(folder, "index.md"), "w", encoding="utf-8") as f:
            f.write(build_index_md(p))
        with open(os.path.join(folder, "cite.bib"), "w", encoding="utf-8") as f:
            f.write(build_bibtex(p))

    print(f"Wrote {len(pubs)} paper folders under {papers_dir}", file=sys.stderr)


def main():
    min_year, max_year = MIN_YEAR, MAX_YEAR
    if YEAR is not None:
        min_year = max_year = YEAR

    print(f"Fetching DBLP publications from {DBLP_URL} ...", file=sys.stderr)
    dblp_pubs = fetch_dblp(DBLP_URL)
    print(f"  -> {len(dblp_pubs)} entries from DBLP", file=sys.stderr)

    s2_pubs = []
    if SEMANTIC_SCHOLAR_ID:
        print(f"Fetching Semantic Scholar publications for author {SEMANTIC_SCHOLAR_ID} ...", file=sys.stderr)
        s2_pubs = fetch_semantic_scholar(SEMANTIC_SCHOLAR_ID)
        print(f"  -> {len(s2_pubs)} entries from Semantic Scholar", file=sys.stderr)

    merged = merge_publications(dblp_pubs, s2_pubs)
    print(f"Merged total: {len(merged)} unique publications", file=sys.stderr)

    before_dedup = len(merged)
    merged = dedupe_arxiv_duplicates(merged)
    if len(merged) < before_dedup:
        print(
            f"Collapsed {before_dedup - len(merged)} arXiv/preprint duplicate(s) "
            f"into their real-venue counterpart",
            file=sys.stderr,
        )

    fixed_names = restore_author_accents(merged)
    if fixed_names:
        print(f"Restored accents in {fixed_names} author name(s)", file=sys.stderr)

    if min_year is not None or max_year is not None:
        merged = filter_by_year(merged, min_year, max_year)
        print(f"After year filter: {len(merged)} publications", file=sys.stderr)

    # 1. Diff against the existing site
    print(f"Scanning existing site publications in {EXISTING_SITE_DIR} ...", file=sys.stderr)
    existing_titles = parse_existing_titles(EXISTING_SITE_DIR)
    print(f"  -> {len(existing_titles)} existing papers found on site", file=sys.stderr)

    missing = find_missing(merged, existing_titles)
    print(f"Missing from site: {len(missing)} papers", file=sys.stderr)

    missing_md = to_markdown(missing, header="# Papers Missing From Website")
    with open(MISSING_REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(missing_md)
    print(f"Wrote missing-papers report to {MISSING_REPORT_PATH}", file=sys.stderr)

    # 2. Optionally generate ready-to-use folders for just the missing papers
    if GENERATE_MISSING_FOLDERS and missing:
        write_paper_folders(missing, MISSING_PAPERS_DIR)


if __name__ == "__main__":
    main()