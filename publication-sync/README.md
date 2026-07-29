# Publication Sync Pipeline — VeraXtract Website

Keeps `content/publication/` on the group website in sync with the latest publications using **DBLP**, **Semantic Scholar**, and **Google Scholar**.

---

# Quick Start

1. Clone this repository.
2. Install the required Python packages.
3. Edit **`config.py`**.
4. Run:

```bash
python dblp_semantic_scraper.py
```

For an occasional audit against Google Scholar:

```bash
python cross_check_scholar.py
```

Finally, before copying anything into the website repository:

```bash
python sanity_check.py
```

---

# Configuration

All user-editable settings are contained in a single file:

```text
config.py
```

The remaining Python scripts automatically import these settings—you should never need to edit the scripts themselves.

The configuration is organised into four sections:

## Publication Sources

- DBLP profile URL
- Semantic Scholar author ID
- Google Scholar profile URL

## Directories

- Website repository root
- Output directory

All reports and generated publication folders are derived automatically from these directories.

## Filters

- `YEAR`
- `MIN_YEAR`
- `MAX_YEAR`

Leave them as `None` to process every publication.

## Runtime Options

- Google Scholar headless mode
- HTTP request headers
- Matching threshold
- Other optional runtime settings

---

# Scripts

## 1. `dblp_semantic_scraper.py`

The primary synchronization script. This is the script you'll run most often.

It:

- downloads publications from DBLP and Semantic Scholar,
- merges metadata,
- compares the results against the website,
- generates publication folders,
- produces missing-paper reports,
- generates per-author review requests.

---

## 2. `google_scholar_citations.py`

Helper module used to retrieve citation statistics from a Google Scholar profile.

Normally this is **not** executed directly. It is imported by `cross_check_scholar.py`.

Because Google Scholar has no public API, this script should only be used occasionally.

---

## 3. `cross_check_scholar.py`

An occasional audit step.

It compares Google Scholar against the DBLP/Semantic Scholar dataset and identifies publications that may be missing from the synchronization pipeline.

Use this periodically—not as part of a scheduled workflow.

---

## 4. `sanity_check.py`

The final verification step.

Run this after generating publication folders and before copying them into the website repository.

The script performs several consistency checks, including:

- duplicate generated papers,
- papers already present in the website,
- malformed or placeholder metadata.

The script is completely **read-only**.

If every check passes, the generated folders are ready for manual review and Git submission.

---

# Recommended Workflow

```text
dblp_semantic_scraper.py
        │
        ▼
Review generated papers
        │
        ▼
cross_check_scholar.py      (optional)
        │
        ▼
Review Scholar-only papers
        │
        ▼
sanity_check.py
        │
        ▼
Copy into content/publication/
        │
        ▼
Git commit → Push → Pull Request
```

## Requirements

- Python 3.11+
- Google Chrome (required only for Google Scholar scraping)

The main synchronization script (`dblp_semantic_scraper.py`) does **not** require Chrome.

Chrome is only needed when running:

- `cross_check_scholar.py`
- `google_scholar_citations.py`

If ChromeDriver reports a version mismatch, update Chrome or set the appropriate `version_main` in `google_scholar_citations.py`.
