---
title: "Retrieving Climate Change Disinformation by Narrative"
subtitle: 'Max Upravitelev, Veronika Solopova, Charlott Jakob, Premtim Sahitaj, Vera Schmitt - arXiv preprint'
authors:
  - Max Upravitelev
  - Veronika Solopova
  - Charlott Jakob
  - Premtim Sahitaj
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

abstract: Detecting climate disinformation narratives typically relies on fixed taxonomies, which do not accommodate emerging narratives. Thus, we re-frame narrative detection as a retrieval task given a narrative’s core message as a query, rank texts from a corpus by alignment with that narrative. This formulation requires no predefined label set and can accommodate emerging narratives. We repurpose three climate disinformation datasets (CARDS, Climate Obstruction, climate change subset of PolyNarrative) for retrieval evaluation and propose SpecFi, a framework that generates hypothetical documents to bridge the gap between abstract narrative descriptions and their concrete textual instantiations. SpecFi uses community summaries from graph-based community detection as few-shot examples for generation, achieving a MAP of 0.494 on CARDS without access to narrative labels. We further introduce narrative variance, an embedding-based difficulty metric, and show via partial correlation analysis that standard retrieval degrades on high-variance narratives (BM25 loses 63.4% of MAP), while SpecFi-CS remains robust (32.7% loss). Our analysis also reveals that unsupervised community summaries converge on descriptions close to expert-crafted taxonomies, suggesting that graph-based methods can surface narrative structure from unlabeled text.

# Summary. An optional shortened abstract.
summary: 
tags:
featured: true

url_pdf: https://arxiv.org/abs/2603.22015
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
