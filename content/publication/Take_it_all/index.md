---
title: "Take It All: Ensemble Retrieval for Multimodal Evidence Aggregation"
subtitle: 'Max Upravitelev, Veronika Solopova, Premtim Sahitaj, Ariana Sahitaj, Charlott Jakob, Sebastian Möller, Vera Schmitt - In Proceedings of the Ninth Fact Extraction and VERification Workshop (FEVER)'
authors:
  - Max Upravitelev
  - Veronika Solopova
  - Premtim Sahitaj
  - Ariana Sahitaj
  - Charlott Jakob
  - Sebastian Möller 
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

abstract: Multimodal fact checking has become increasingly important due to the predominance of visual content on social media platforms, where images are frequently used to enhance the credibility and spread of misleading claims, while generated images become more prevalent and realistic as generative models advance. Incorporating visual information, however, substantially increases computational costs, raising critical efficiency concerns for practical deployment. In this study, we propose and evaluate the ADA-AGGR (ensemble retrievAl for multimoDAl evidence AGGRegation) pipeline, which achieved the second place on both the dev and test leaderboards of the FEVER 9/AVerImaTeC shared task. However, long runtimes per claim highlight challenges regarding efficiency concerns when designing multimodal claim verification pipelines. We therefore run extensive ablation studies and configuration analyses to identify possible performance–runtime improvements. Our experiments show that substantial efficiency gains are possible without significant loss in verification quality. For instance, we reduced the average runtime by up to 6.28× while maintaining comparable performance across evaluation metrics by aggressively downsampling input images processed by visual language models. Overall, our results highlight that careful design choices are crucial for building scalable and resource-efficient multimodal fact-checking systems suitable for real-world deployment.

# Summary. An optional shortened abstract.
summary: 
tags:
featured: true

url_pdf: https://aclanthology.org/2026.fever-1.7/
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
