from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = ROOT.parent.parent


@dataclass(frozen=True)
class Config:
    # ------------------------------------------------------------------
    # Publication Sources
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # Google Scholar
    # ------------------------------------------------------------------
    #
    # Google Scholar scraping requires Google Chrome to be installed.
    #
    # The scraper uses Selenium together with ChromeDriver to automate
    # the browser. If Chrome is not installed, or if the installed
    # Chrome version is incompatible with the downloaded ChromeDriver,
    # the Google Scholar scripts may fail to launch.
    #
    # If you encounter a Chrome/ChromeDriver version mismatch, set
    # `version_main=<your Chrome major version>` in
    # `google_scholar_citations.py`.
    #
    # These settings are only used by:
    #   - google_scholar_citations.py
    #   - cross_check_scholar.py
    #
    google_scholar_profile_url: str


    dblp_url: str
    semantic_scholar_id: str | None



    # ------------------------------------------------------------------
    # Root Directories
    # ------------------------------------------------------------------
    website_root: Path
    output_root: Path

    # ------------------------------------------------------------------
    # Options
    # ------------------------------------------------------------------
    generate_missing_folders: bool = True




    # ------------------------------------------------------------------
    # Filters
    # ------------------------------------------------------------------
    year: int | None = None
    min_year: int | None = None
    max_year: int | None = None

    # ------------------------------------------------------------------
    # Matching
    # ------------------------------------------------------------------
    arxiv_similarity_threshold: float = 0.7

    # ------------------------------------------------------------------
    # Networking
    # ------------------------------------------------------------------
    http_headers: dict[str, str] | None = None


    # ------------------------------------------------------------------
    # Google Scholar Specific Configs
    # ------------------------------------------------------------------

    headless: bool = True
    click_delay_seconds: int = 2
    max_show_more_clicks: int = 20


    # ------------------------------------------------------------------
    # Derived Paths (no need for users to edit these)
    # ------------------------------------------------------------------
    @property
    def existing_site_dir(self) -> Path:
        return self.website_root / "content" / "publication"

    @property
    def missing_report_path(self) -> Path:
        return self.output_root / "missing_publications.md"

    @property
    def missing_papers_dir(self) -> Path:
        return self.output_root / "missing_papers"

    @property
    def scholar_output_json(self) -> Path:
        return self.output_root / "scholar_citations.json"

    @property
    def scholar_flagged_report_path(self) -> Path:
        return self.output_root / "scholar_only_flagged.md"

# ======================================================================
# User Configuration
# Edit only this section.
# ======================================================================

cfg = Config(
    # DBLP profile URL
    dblp_url="https://dblp.org/pid/295/6533.html",

    # Semantic Scholar author ID (set to None to disable)
    semantic_scholar_id="2114572998",

    # Path to the cloned website repository.
    #
    # Example:
    # website_root = Path("/path/to/VeraXtract-Website")
    #
    # The directory must contain:
    #   content/
    #   content/publication/
    #   content/authors/
    website_root = Path("/Users/swarnadeep/Riju/Code/academic/XplaiNLP/xplainlp.github.io"),
    #website_root = ROOT / "website"

    # Directory where generated reports and folders will be written.
    output_root = PROJECT_ROOT / "data" / "output_2",

    # Generate folders for missing publications
    generate_missing_folders=True,

    # Filter publications (leave as None to disable)
    year=None,
    min_year=None,
    max_year=None,

    # Similarity threshold for matching arXiv preprints
    arxiv_similarity_threshold=0.7,

    http_headers={
        "User-Agent": "lab-website-publication-sync/1.0",
    },

    google_scholar_profile_url="https://scholar.google.com/citations?user=pKbJC10AAAAJ&hl=en",

)
