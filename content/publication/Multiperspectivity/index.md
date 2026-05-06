---
title: "Multiperspectivity as a Resource for Narrative Similarity Prediction"
subtitle: 'Max Upravitelev, Veronika Solopova, Jing Yang, Charlott Jakob, Premtim Sahitaj, Ariana Sahitaj, Vera Schmitt - arXiv preprint'
authors:
  - Max Upravitelev
  - Veronika Solopova
  - Jing Yang
  - Charlott Jakob
  - Premtim Sahitaj
  - Ariana Sahitaj
  - Dr. Vera Schmitt
date: "2026-03-23T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date). 2024/9/11
publishDate: "2024-09-11T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["preprint"]

# Publication name and optional abbreviated publication name.
publication: 
publication_short: 

abstract: Predicting narrative similarity can be understood as an inherently interpretive task different, equally valid readings of the same text can produce divergent interpretations and thus different similarity judgments, posing a fundamental challenge for semantic evaluation benchmarks that encode a single ground truth. Rather than treating this multiperspectivity as a challenge to overcome, we propose to incorporate it in the decision making process of predictive systems. To explore this strategy, we created an ensemble of 31 LLM personas. These range from practitioners following interpretive frameworks to more intuitive, lay-style characters. Our experiments were conducted on the SemEval-2026 Task 4 dataset, where the system ranked 13th out of 47 teams and achieved an accuracy score of 0.705. Accuracy improves with ensemble size, consistent with Condorcet Jury Theorem-like dynamics under weakened independence. Practitioner personas perform worse individually but produce less correlated errors, yielding larger ensemble gains under majority voting. Our error analysis reveals a consistent negative association between gender-focused interpretive vocabulary and accuracy across all persona categories, suggesting either attention to dimensions not relevant for the benchmark or valid interpretations absent from the ground truth. This finding underscores the need for evaluation frameworks that account for interpretive plurality.

# Summary. An optional shortened abstract.
summary: 
tags:
featured: true

url_pdf: https://arxiv.org/abs/2603.22103
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
