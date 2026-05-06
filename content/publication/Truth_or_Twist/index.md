---
title: "Truth or twist? optimal model selection for reliable label flipping evaluation in llm-based counterfactuals"
subtitle: 'Qianli Wang, Nils Feldhus, Luis Felipe Villa-Arenas, Christin Seifert, Sebastian Möller, Vera Schmitt - In Proceedings of the 18th International Natural Language Generation Conference'
authors:
  - Qianli Wang
  - Nils Feldhus
  - Luis Felipe Villa-Arenas
  - Christin Seifert
  - Sebastian Möller
  - Dr. Vera Schmitt
date: "2025-10-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date). 2024/9/11
publishDate: "2024-09-11T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: The 18th International Natural Language Generation Conference
publication_short: INLG 2025

abstract: Counterfactual examples are widely employed to enhance the performance and robustness of large language models (LLMs) through counterfactual data augmentation (CDA). However, the selection of the judge model used to evaluate label flipping, the primary metric for assessing the validity of generated counterfactuals for CDA, yields inconsistent results. To decipher this, we define four types of relationships between the counterfactual generator and judge models being the same model, belonging to the same model family, being independent models, and having an distillation relationship. Through extensive experiments involving two state-of-the-art LLM-based methods, three datasets, four generator models, and 15 judge models, complemented by a user study (n = 90), we demonstrate that judge models with an independent, non-fine-tuned relationship to the generator model provide the most reliable label flipping evaluations. Relationships between the generator and judge models, which are closely aligned with the user study for CDA, result in better model performance and robustness. Nevertheless, we find that the gap between the most effective judge models and the results obtained from the user study remains considerably large. This suggests that a fully automated pipeline for CDA may be inadequate and requires human intervention.

# Summary. An optional shortened abstract.
summary: 
tags:
featured: true

url_pdf: https://aclanthology.org/2025.inlg-main.5/
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
