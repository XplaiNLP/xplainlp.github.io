#!/usr/bin/env python3
"""
Google Scholar author-profile scraper -- citation counts only.

IMPORTANT CONTEXT (read before running):
  - This is NOT part of the main publication-sync pipeline (scholar_scraper.py).
    That script (DBLP + Semantic Scholar) is what generates the actual
    website content and should stay the source of truth for titles,
    authors, venues, links, and abstracts.
  - This script exists ONLY to pull the one thing Scholar has that
    DBLP/S2 don't: citation counts and h-index/i10-index. Treat its
    output as supplementary data (e.g. "N citations" badges), not as
    a replacement pipeline.
  - Google Scholar has no public API, explicitly disallows automated
    scraping in its Terms of Service, and aggressively rate-limits or
    CAPTCHAs repeated automated access. Run this occasionally / by hand
    when you actually need updated citation numbers -- not on a schedule,
    not in CI, not repeatedly in a short window. If you get blocked,
    that's Scholar's anti-bot system working as intended; back off and
    try again later rather than retrying immediately.
  - Requires: pip install undetected-chromedriver selenium

Usage:
    python scholar_citations.py
"""

import json
import re
import sys
import time
from config import cfg

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

# ----------------------------- CONFIG -----------------------------
PROFILE_URL = cfg.google_scholar_profile_url #"https://scholar.google.com/citations?user=pKbJC10AAAAJ&hl=en"
OUTPUT_JSON = cfg.scholar_output_json #"/Users/swarnadeep/Riju/Code/academic/XplaiNLP/scrapper/data/output/scholar_citations.json"
HEADLESS = cfg.headless
# Be polite / avoid tripping rate limits: small delay between "Show more" clicks
CLICK_DELAY_SECONDS = cfg.click_delay_seconds #2
MAX_SHOW_MORE_CLICKS = cfg.max_show_more_clicks  # safety cap
# --------------------------------------------------------------------


def get_browser():
    options = uc.ChromeOptions()
    if HEADLESS:
        options.add_argument("--headless=new")
    return uc.Chrome(options=options,version_main=150)


def expand_all_publications(browser) -> None:
    """Click 'Show more' repeatedly until all publications are loaded
    or the button becomes disabled/disappears."""
    for _ in range(MAX_SHOW_MORE_CLICKS):
        try:
            button = browser.find_element(By.ID, "gsc_bpf_more")
        except Exception:
            break  # button not found, nothing more to expand

        if not button.is_enabled():
            break

        button.click()
        time.sleep(CLICK_DELAY_SECONDS)


def parse_overall_stats(browser) -> dict:
    """Parse the citation/h-index/i10-index summary table (gsc_rsb_st)."""
    stats = {}
    try:
        cells = browser.find_elements(By.CSS_SELECTOR, "table#gsc_rsb_st td.gsc_rsb_std")
        values = [c.text.strip() for c in cells]
        # Order on the page: Citations(All, Since), h-index(All, Since), i10-index(All, Since)
        labels = [
            "citations_all", "citations_since",
            "h_index_all", "h_index_since",
            "i10_index_all", "i10_index_since",
        ]
        for label, value in zip(labels, values):
            stats[label] = int(value) if value.isdigit() else value
    except Exception as e:
        print(f"WARNING: could not parse overall stats: {e}", file=sys.stderr)
    return stats


def normalize_title(title: str) -> str:
    return "".join(ch.lower() for ch in (title or "") if ch.isalnum())


def parse_publications(browser) -> list[dict]:
    pubs = []
    rows = browser.find_elements(By.CSS_SELECTOR, "table#gsc_a_t tr.gsc_a_tr")

    for row in rows:
        try:
            title_el = row.find_element(By.CSS_SELECTOR, "td.gsc_a_t a.gsc_a_at")
            title = title_el.text.strip()

            gray_divs = row.find_elements(By.CSS_SELECTOR, "td.gsc_a_t div.gs_gray")
            authors = gray_divs[0].text.strip() if len(gray_divs) > 0 else ""
            venue = gray_divs[1].text.strip() if len(gray_divs) > 1 else ""

            year_el = row.find_elements(By.CSS_SELECTOR, "td.gsc_a_y span")
            year = year_el[0].text.strip() if year_el else ""

            citation_el = row.find_elements(By.CSS_SELECTOR, "td.gsc_a_c a.gsc_a_ac")
            citation_text = citation_el[0].text.strip() if citation_el else ""
            citations = int(citation_text) if citation_text.isdigit() else 0

            pubs.append(
                {
                    "title": title,
                    "authors_raw": authors,
                    "venue_raw": venue,
                    "year": year,
                    "citations": citations,
                    "normalized_title": normalize_title(title),
                }
            )
        except Exception as e:
            print(f"WARNING: skipped a row due to parse error: {e}", file=sys.stderr)
            continue

    return pubs


def main():
    print(f"Launching browser (headless={HEADLESS}) ...", file=sys.stderr)
    browser = get_browser()

    try:
        print(f"Fetching {PROFILE_URL} ...", file=sys.stderr)
        browser.get(PROFILE_URL)
        time.sleep(3)  # let the page settle before interacting

        print("Expanding full publication list ...", file=sys.stderr)
        expand_all_publications(browser)

        print("Parsing overall stats ...", file=sys.stderr)
        stats = parse_overall_stats(browser)
        print(f"  -> {stats}", file=sys.stderr)

        print("Parsing publications table ...", file=sys.stderr)
        pubs = parse_publications(browser)
        print(f"  -> {len(pubs)} publications found", file=sys.stderr)

    finally:
        browser.quit()

    output = {"profile_url": PROFILE_URL, "overall_stats": stats, "publications": pubs}
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"Wrote {OUTPUT_JSON}", file=sys.stderr)


if __name__ == "__main__":
    main()
