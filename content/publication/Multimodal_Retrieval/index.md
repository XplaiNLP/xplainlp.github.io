---
title: "Selective Multimodal Retrieval for Automated Verification of Image–Text Claims"
subtitle: 'Yoana Tsoneva, Paul-Conrad Feig, Jiaao Li, Veronika Solopova, Neda Foroutan, Arthur Hilbert, Vera Schmitt - In Proceedings of the Ninth Fact Extraction and VERification Workshop (FEVER)'
authors:
  - Yoana Tsoneva
  - Paul-Conrad Feig
  - Jiaao Li
  - Veronika Solopova
  - Neda Foroutan
  - Arthur Hilbert 
  - Dr. Vera Schmitt
date: "2026-03-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date). 2024/9/11
publishDate: "2024-09-11T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["workshop-paper"]

# Publication name and optional abbreviated publication name.
publication: The Ninth Fact Extraction and VERification Workshop
publication_short: FEVER

abstract: This paper presents an efficiency-aware pipeline for automated fact-checking of real-world image–text claims that treats multimodality as a controllable design variable rather than a property that must be uniformly propagated through every stage of the system. The approach decomposes claims into verification questions, assigns each to text- or image-related types, and applies modality-aware retrieval strategies, while ultimately relying on text-only evidence for verdict prediction and justification generation. Evaluated on the AVerImaTeC dataset within the FEVER-9 shared task, the system achieves competitive question, evidence, verdict, and justification scores and ranks fourth overall, outperforming the official baseline on evidence recall, verdict accuracy, and justification quality despite not using visual evidence during retrieval. These results demonstrate that strong performance on multimodal fact-checking can be achieved by selectively controlling where visual information influences retrieval and reasoning, rather than performing full multimodal fusion at every stage of the pipeline.

# Summary. An optional shortened abstract.
summary: 
tags:
featured: true

url_pdf: https://aclanthology.org/2026.fever-1.10/
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
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/s9CC2SKySJM)'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects:
- internal-project

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---
