#!/usr/bin/env python3
"""
Cross-check Vera's DBLP+Semantic Scholar publication list AND the existing
website against her Google Scholar profile, and flag any papers Scholar
has that neither source caught.

DBLP + Semantic Scholar remain the source of truth for the website.
Google Scholar is used here ONLY as an occasional audit pass -- to catch
coverage gaps (e.g. a thesis, a non-CS venue, a very fresh preprint) that
DBLP/S2 might have missed. This script does not modify anything in
EXISTING_SITE_DIR; it only writes a report + optional ready-to-review
folders for the flagged (Scholar-only, not-yet-on-site) papers.

A paper is only flagged if it is on Scholar AND:
  - NOT found via DBLP/Semantic Scholar, AND
  - NOT already present on the site

This means the output of this script and the output of
dblp_semantic_scraper.py are disjoint (one requires being known via
DBLP/S2, the other requires NOT being known via DBLP/S2) -- so both can
safely write into the SAME final output directory (FINAL_PAPERS_DIR)
without overwriting or duplicating each other's folders.

Requires both sibling scripts to be in the SAME directory as this one:
    dblp_semantic_scraper.py     (DBLP + Semantic Scholar fetch/merge/site-diff logic)
    google_scholar_citations.py  (Google Scholar profile scraping logic)

Requires: pip install requests pyyaml undetected-chromedriver selenium

Usage:
    python cross_check_scholar.py

Reminder: Google Scholar has no public API and disallows scraping in
its ToS. Run this occasionally / by hand when you actually want an
audit, not on a schedule or repeatedly in a short window.
"""

import sys
import time
from config import cfg

import dblp_semantic_scraper as sync           # DBLP + Semantic Scholar + site-diff logic
import google_scholar_citations as gs           # Google Scholar profile scraping logic

# ----------------------------- CONFIG -----------------------------
DBLP_URL = cfg.dblp_url #"https://dblp.org/pid/295/6533.html"
SEMANTIC_SCHOLAR_ID = cfg.semantic_scholar_id #"2114572998"
SCHOLAR_PROFILE_URL = cfg.google_scholar_profile_url#"https://scholar.google.com/citations?user=pKbJC10AAAAJ&hl=en"

# Same site path used by dblp_semantic_scraper.py -- needed here too so we
# don't flag papers that are already on the site.
EXISTING_SITE_DIR = cfg.existing_site_dir #"/Users/swarnadeep/Riju/Code/academic/XplaiNLP/xplainlp.github.io/content/publication"

FLAGGED_REPORT_PATH = cfg.scholar_flagged_report_path #"/Users/swarnadeep/Riju/Code/academic/XplaiNLP/scrapper/data/output/scholar_only_flagged.md"

# Same directory dblp_semantic_scraper.py writes its missing-paper folders
# to. Since the two scripts' outputs are disjoint (see module docstring),
# writing to the same directory gives you ONE final folder to review and
# copy into content/publication/, combining both loops' findings.
FINAL_PAPERS_DIR = cfg.missing_papers_dir #"/Users/swarnadeep/Riju/Code/academic/XplaiNLP/scrapper/data/output/missing_papers"
GENERATE_FLAGGED_FOLDERS = cfg.generate_missing_folders #True
# --------------------------------------------------------------------


def scholar_pub_to_core_format(scholar_pub: dict) -> dict:
    """Convert a Google-Scholar-scraped publication into the same dict
    shape used by dblp_semantic_scraper.py, so it can go through the same
    build_index_md() / write_paper_folders() logic.

    NOTE: Scholar author names are often abbreviated (e.g. "V Schmitt"
    instead of "Vera Schmitt") -- worth fixing up by hand if you use
    the generated folder, since DBLP/S2 entries use full names.
    """
    authors = [a.strip() for a in (scholar_pub.get("authors_raw") or "").split(",") if a.strip()]
    return {
        "title": scholar_pub.get("title") or "Untitled",
        "authors": authors,
        "year": scholar_pub.get("year") or None,
        "venue": scholar_pub.get("venue_raw") or None,
        "link": None,   # Scholar's profile table doesn't expose a direct paper link
        "doi": None,
        "abstract": None,
        "type": None,   # unknown -> falls back to DEFAULT_PUBLICATION_TYPE in build_index_md
        "source": "google_scholar",
        "citations": scholar_pub.get("citations", 0),
    }


def main():
    # 1. Source of truth: DBLP + Semantic Scholar
    print(f"Fetching DBLP publications from {DBLP_URL} ...", file=sys.stderr)
    dblp_pubs = sync.fetch_dblp(DBLP_URL)
    print(f"  -> {len(dblp_pubs)} entries from DBLP", file=sys.stderr)

    s2_pubs = []
    if SEMANTIC_SCHOLAR_ID:
        print(f"Fetching Semantic Scholar publications for author {SEMANTIC_SCHOLAR_ID} ...", file=sys.stderr)
        s2_pubs = sync.fetch_semantic_scholar(SEMANTIC_SCHOLAR_ID)
        print(f"  -> {len(s2_pubs)} entries from Semantic Scholar", file=sys.stderr)

    merged = sync.merge_publications(dblp_pubs, s2_pubs)
    known_titles = {sync.normalize_title(p["title"]) for p in merged}
    print(f"DBLP+S2 combined: {len(merged)} unique publications known", file=sys.stderr)

    # 2. What's already on the site (so we don't re-flag it)
    print(f"Scanning existing site publications in {EXISTING_SITE_DIR} ...", file=sys.stderr)
    existing_titles = sync.parse_existing_titles(EXISTING_SITE_DIR)
    print(f"  -> {len(existing_titles)} existing papers found on site", file=sys.stderr)

    # 3. Audit pass: Google Scholar profile
    print(f"Launching browser to fetch {SCHOLAR_PROFILE_URL} ...", file=sys.stderr)
    browser = gs.get_browser()
    try:
        browser.get(SCHOLAR_PROFILE_URL)
        time.sleep(3)
        gs.expand_all_publications(browser)
        scholar_pubs = gs.parse_publications(browser)
    finally:
        browser.quit()
    print(f"  -> {len(scholar_pubs)} entries from Google Scholar", file=sys.stderr)

    # 4. Flag anything on Scholar that's neither known via DBLP/S2 NOR
    # already on the site.
    flagged_raw = [
        p
        for p in scholar_pubs
        if p["normalized_title"] not in known_titles
        and p["normalized_title"] not in existing_titles
    ]
    flagged = [scholar_pub_to_core_format(p) for p in flagged_raw]
    print(
        f"Flagged (on Scholar, not found via DBLP/S2, not already on site): {len(flagged)}",
        file=sys.stderr,
    )

    # 5. Write report
    report = sync.to_markdown(
        flagged, header="# On Google Scholar but NOT found via DBLP/S2 or the site"
    )
    FLAGGED_REPORT_PATH.write_text(report,encoding="utf-8")
    print(f"Wrote flagged report to {FLAGGED_REPORT_PATH}", file=sys.stderr)

    # 6. Optionally generate index.md-ready folders for just the flagged
    # papers, into the SAME final directory dblp_semantic_scraper.py uses.
    if GENERATE_FLAGGED_FOLDERS and flagged:
        sync.write_paper_folders(flagged, FINAL_PAPERS_DIR)
        print(
            "NOTE: flagged folders have limited metadata (no link/doi/abstract, "
            "and author names may be abbreviated as Scholar shows them). "
            "Review and fill these in by hand before adding to the site.",
            file=sys.stderr,
        )


if __name__ == "__main__":
    main()
