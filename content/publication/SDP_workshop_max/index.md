---
title: 'Comparing LLMs and BERT-based Classifiers for Resource-Sensitive Claim Verification in Social Media'
subtitle: "Max Upravitelev, Nicolau Duran-Silva, Christian Woerle, Giuseppe Guarino, Salar Mohtaj, Jing Yang, Veronika Solopova, Vera Schmitt" 

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
- Max Upravitelev
- Nicolau Duran-Silva
- Christian Woerle
- Giuseppe Guarino
- Salar Mohtaj
- Jing Yang
- Veronika Solopova
- Vera Schmitt

# Author notes (optional)
author_notes: 

date: '2025-07-20T00:00:00Z'
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
  The overwhelming volume of content being published at any given moment poses a significant challenge for the design of automated fact-checking (AFC) systems on social media, requiring an emphasized consideration of efficiency aspects.As in other fields, systems built upon LLMs have achieved good results on different AFC benchmarks. However, the application of LLMs is accompanied by high resource requirements. The energy consumption of LLMs poses a significant challenge from an ecological perspective, while remaining a bottleneck in latency-sensitive scenarios like AFC within social media. Therefore, we propose a system built upon fine-tuned smaller BERT-based models. When evaluated on the ClimateCheck dataset against decoder-only LLMs, our best fine-tuned model outperforms Phi 4 and approaches Qwen3 14B in reasoning mode — while significantly reducing runtime per claim. Our findings demonstrate that small encoder-only models fine-tuned for specific tasks can still provide a substantive alternative to large decoder-only LLMs, especially in efficiency-concerned settings.
# Summary. An optional shortened abstract.
summary: 

tags: []

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://aclanthology.org/2025.sdp-1.26/'
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


