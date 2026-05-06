---
title: "Extending Information Bottleneck Attribution to Video Sequences for Deepfake Detection"
subtitle: 'Veronika Solopova, Lucas Schmidt, Vera Schmitt, Dorothea Kolossa - In International Symposium on Intelligent Data Analysis'
authors:
  - Veronika Solopova
  - Lucas Schmidt
  - Dr. Vera Schmitt
  - Dorothea Kolossa
date: "2026-04-18T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date). 2024/9/11
publishDate: "2024-09-11T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["paper-conference"]

# Publication name and optional abbreviated publication name.
publication: "International Symposium on Intelligent Data Analysis"
publication_short: "IDA 2026"

abstract: As the quality of deepfakes increasingly matches authentic video, reliable detection requires automated video classifiers. Yet these models often operate as black boxes, making it hard to assess their trustworthiness in high-stakes security and forensic settings. We introduce VIBA (Video Information Bottleneck Attribution), an explainable video classification method that extends Information Bottleneck Attribution (IBA) to jointly capture spatial and temporal dependencies. VIBA is post-hoc and model-agnostic, producing relevance and optical flow maps that reveal manipulated regions and motion inconsistencies across frames. We apply VIBA to deepfake detection with three architectures Xception for spatial features, a VGG11-based optical flow model for motion dynamics, and a CViT visual transformer for long-range temporal reasoning. Across models, VIBA yields more temporally stable and spatially precise explanations than Grad-CAM, and aligns more closely with expert human annotations. By making deepfake detector outputs easier to analyse and interpret, VIBA supports secure, transparent deployment of video analysis systems in digital forensics and misinformation monitoring.

# Summary. An optional shortened abstract.
summary: 
tags:
featured: true

url_pdf: https://link.springer.com/chapter/10.1007/978-3-032-23833-7_12
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
