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
    - DBLP: any profile URL works; the script converts it to the
      XML export endpoint (append .xml).
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
import xml.etree.ElementTree as ET
from pathlib import Path
from os import PathLike
import requests
import yaml
from config import cfg

# ----------------------------- CONFIG -----------------------------
DBLP_URL = cfg.dblp_url #"https://dblp.org/pid/295/6533.html"
SEMANTIC_SCHOLAR_ID = cfg.dblp_url #"2114572998"

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


def dblp_xml_url(profile_url: str) -> str:
    """Convert a DBLP profile URL (.html or bare) into its .xml export URL."""
    if profile_url.endswith(".xml"):
        return profile_url
    if profile_url.endswith(".html"):
        return profile_url[: -len(".html")] + ".xml"
    return profile_url.rstrip("/") + ".xml"


# DBLP indexes more than just papers under a person's profile -- datasets,
# software, homepages, and edited-volume records show up as different XML
# tags too. Only these tags represent an actual authored publication;
# anything else (e.g. "data" for datasets/software, "www" for homepages,
# "editor" for edited volumes, "proceedings" for a volume itself) is
# excluded so it never enters the pipeline as if it were a paper.
_DBLP_PAPER_TAGS = {
    "article", "inproceedings", "incollection", "book",
    "phdthesis", "mastersthesis",
}


def fetch_dblp(profile_url: str) -> list[dict]:
    url = dblp_xml_url(profile_url)
    resp = requests.get(url, headers=DBLP_HEADERS, timeout=30)
    resp.raise_for_status()
    root = ET.fromstring(resp.content)

    pubs = []
    skipped_non_paper = 0
    for r in root.findall(".//r"):
        for entry in list(r):
            if entry.tag not in _DBLP_PAPER_TAGS:
                skipped_non_paper += 1
                continue

            title_el = entry.find("title")
            if title_el is None or not title_el.text:
                continue
            authors = [clean_author_name(a.text) for a in entry.findall("author") if a.text]
            year_el = entry.find("year")
            venue_el = entry.find("journal")
            if venue_el is None:
                venue_el = entry.find("booktitle")
            ee_el = entry.find("ee")
            url_el = entry.find("url")

            pubs.append(
                {
                    "title": title_el.text.strip().rstrip("."),
                    "authors": authors,
                    "year": year_el.text if year_el is not None else None,
                    "venue": venue_el.text if venue_el is not None else None,
                    "link": ee_el.text if ee_el is not None else (
                        f"https://dblp.org/{url_el.text}" if url_el is not None else None
                    ),
                    "doi": None,
                    "abstract": None,
                    "type": entry.tag,
                    "source": "dblp",
                }
            )

    if skipped_non_paper:
        print(
            f"  (excluded {skipped_non_paper} non-paper DBLP record(s): "
            f"datasets, software, homepages, edited volumes, etc.)",
            file=sys.stderr,
        )

    return pubs


def fetch_semantic_scholar(author_id: str) -> list[dict]:
    url = f"https://api.semanticscholar.org/graph/v1/author/{author_id}/papers"
    params = {
        "fields": "title,authors,venue,year,externalIds,url,abstract",
        "limit": 1000,
    }
    resp = requests.get(url, params=params, timeout=30)
    resp.raise_for_status()
    data = resp.json()

    pubs = []
    for p in data.get("data", []):
        external_ids = p.get("externalIds") or {}
        pubs.append(
            {
                "title": (p.get("title") or "").strip().rstrip("."),
                "authors": [a.get("name") for a in p.get("authors", [])],
                "year": str(p["year"]) if p.get("year") else None,
                "venue": p.get("venue") or None,
                "link": p.get("url"),
                "doi": external_ids.get("DOI"),
                "abstract": p.get("abstract"),
                "type": "unknown",
                "source": "semantic_scholar",
            }
        )
    return pubs


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
                rp["doi"] = rp.get("doi") or pp.get("doi")
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
