---
title: 'Integrating Video, Text, and Images for Multimodal Disinformation Detection'
subtitle: "Thomas Hetzner, Veronika Solopova, Vera Schmitt, Dorothea Kolossa" 

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
- Thomas Hetzner
- Veronika Solopova
- Vera Schmitt
- Dorothea Kolossa

# Author notes (optional)
author_notes: 

date: '2025-09-18T00:00:00Z'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2025-01-01T00:00:00Z'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['']

# Publication name and optional abbreviated publication name.
publication: Proceedings of the 4th ACM International Workshop on Multimedia AI against Disinformation
publication_short:

abstract: |
Disinformation increasingly spans multiple modalities, includingmanipulated audio, fake videos, and text-image content pairs in thecase of articles. Existing detection models often address the modali-ties separately, limiting their effectiveness in real-world scenarios. This study proposes a unified multimodal disinformation detectionmodel that simultaneously analyzes text, image, and video con-tent. To operationalize this unified approach, we transform videodata into complementary textual and visual representations. Audiotracks are transcribed using Whisper, while keyframes are extractedfrom video using one of three methods: random frame extraction,clustering-based selection, and our novel extraction method. Cap-tions are generated for each keyframe to embed visual semanticsinto the textual stream, enabling integrated cross-modal analysis. This combined representation is evaluated against unimodalbaselines and state-of-the-art Vision-Language Models (VLMs), in-cluding LLaMA and VILA. Results across model architectures anddataset configurations show that our unified multimodal pipelineoutperforms separate modality-specific systems in detecting disin-formation.
# Summary. An optional shortened abstract.
summary: 

tags: []

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://dl.acm.org/doi/full/10.1145/3733567.3735570'
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
