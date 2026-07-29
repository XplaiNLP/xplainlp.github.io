#!/usr/bin/env python3
"""
Pre-upload sanity check for missing_papers/.

Run this after generating missing_papers/ (via dblp_semantic_scraper.py
and/or cross_check_scholar.py) and BEFORE copying anything into
content/publication/. Checks:

  1. No duplicate titles within missing_papers/ itself.
  2. None of the missing_papers/ titles already exist on the live site
     (a fresh re-check, independent of whatever the generating scripts
     computed -- catches drift if the site changed since then).
  3. No empty/placeholder titles.

Exits with a clear PASS/FAIL summary. This does not modify anything --
read-only checks against the two local folders.

Usage:
    python sanity_check.py
"""

import os
import sys
from collections import defaultdict
from config import cfg
from pathlib import Path

import dblp_semantic_scraper as sync  # reuse parse_existing_titles, normalize_title

# ----------------------------- CONFIG -----------------------------
MISSING_PAPERS_DIR = cfg.missing_papers_dir #"/Users/swarnadeep/Riju/Code/academic/XplaiNLP/scrapper/data/output/missing_papers"
EXISTING_SITE_DIR = cfg.existing_site_dir #"/Users/swarnadeep/Riju/Code/academic/XplaiNLP/xplainlp.github.io/content/publication"
# --------------------------------------------------------------------


def load_missing_titles(missing_dir: Path) -> list[tuple[str, str]]:
    """Returns list of (folder_name, title) for every folder with an index.md."""
    if not os.path.isdir(missing_dir):
        print(f"ERROR: missing_papers dir not found: {missing_dir}", file=sys.stderr)
        sys.exit(1)

    entries = []
    for entry in sorted(os.listdir(missing_dir)):
        index_path = os.path.join(missing_dir, entry, "index.md")
        if not os.path.isfile(index_path):
            continue
        with open(index_path, "r", encoding="utf-8") as f:
            content = f.read()
        parts = content.split("---", 2)
        if len(parts) < 3:
            entries.append((entry, None))
            continue
        import yaml
        try:
            front_matter = yaml.safe_load(parts[1]) or {}
        except yaml.YAMLError:
            entries.append((entry, None))
            continue
        title = front_matter.get("title")
        entries.append((entry, title))
    return entries


def main():
    print(f"Loading missing_papers from {MISSING_PAPERS_DIR} ...", file=sys.stderr)
    entries = load_missing_titles(MISSING_PAPERS_DIR)
    print(f"  -> {len(entries)} folders found\n", file=sys.stderr)

    problems = []

    # Check 1: empty/placeholder titles
    empty = [folder for folder, title in entries if not title or title.strip() == "" or title == "Untitled"]
    if empty:
        problems.append(f"{len(empty)} folder(s) with empty/placeholder title:")
        for f in empty:
            problems.append(f"  - {f}")

    # Check 2: duplicate titles WITHIN missing_papers/
    by_normalized = defaultdict(list)
    for folder, title in entries:
        if title:
            by_normalized[sync.normalize_title(title)].append((folder, title))

    duplicates = {k: v for k, v in by_normalized.items() if len(v) > 1}
    if duplicates:
        problems.append(f"\n{len(duplicates)} duplicate title group(s) WITHIN missing_papers/:")
        for norm_title, group in duplicates.items():
            problems.append(f"  Title match: {group[0][1]!r}")
            for folder, title in group:
                problems.append(f"    - {folder}/  (title: {title!r})")

    # Check 3: fresh re-check against the live site
    print(f"Re-scanning live site at {EXISTING_SITE_DIR} ...", file=sys.stderr)
    existing_titles = sync.parse_existing_titles(EXISTING_SITE_DIR)
    print(f"  -> {len(existing_titles)} titles currently on site\n", file=sys.stderr)

    already_on_site = [
        (folder, title) for folder, title in entries
        if title and sync.normalize_title(title) in existing_titles
    ]
    if already_on_site:
        problems.append(f"\n{len(already_on_site)} folder(s) ALREADY on the live site (stale, should be removed):")
        for folder, title in already_on_site:
            problems.append(f"  - {folder}/  (title: {title!r})")

    # Summary
    print("=" * 60)
    if not problems:
        print(f"PASS -- {len(entries)} papers checked, no duplicates, no titles already on site.")
        print("Safe to review individually and copy into content/publication/.")
    else:
        print(f"FAIL -- issues found in {len(entries)} papers checked:\n")
        print("\n".join(problems))
        print("\nFix these before uploading. Duplicates: keep the better-sourced")
        print("folder (has a real link/DOI) and delete the other. Already-on-site")
        print("entries: just delete that folder, it's stale output from an earlier run.")
    print("=" * 60)


if __name__ == "__main__":
    main()
