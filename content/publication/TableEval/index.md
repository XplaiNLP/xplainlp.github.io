---
title: 'Table Understanding and (Multimodal) LLMs: A Cross-Domain Case Study on Scientific vs. Non-Scientific Data'
subtitle: 'Ekaterina Borisova, Fabio Barth, Nils Feldhus, Raia Abu Ahmad, Malte Ostendorff, Pedro Ortiz Suarez, Georg Rehm, and Sebastian Möller'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
    - Ekaterina Borisova
    - Fabio Barth
    - Nils Feldhus
    - Raia Abu Ahmad
    - Malte Ostendorff
    - Pedro Ortiz Suarez
    - Georg Rehm
    - Sebastian Möller
# Author notes (optional)
author_notes: 

date: '2025-06-05T12:00:00Z'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2025-06-21T07:02:00Z'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['workshop-paper']

# Publication name and optional abbreviated publication name.
publication: The 4th Table Representation Learning Workshop at ACL 2025
publication_short: TRL @ ACL 2025

abstract: "Tables are among the most widely used tools for representing structured data in research, business, medicine, and education. Although LLMs demonstrate strong performance in downstream tasks, their efficiency in processing tabular data remains underexplored. In this paper, we investigate the effectiveness of both text-based and multimodal LLMs on table understanding tasks through a cross-domain and cross-modality evaluation. Specifically, we compare their performance on tables from scientific vs. non-scientific contexts and examine their robustness on tables represented as images vs. text. Additionally, we conduct an interpretability analysis to measure context usage and input relevance. We also introduce the TableEval benchmark, comprising 3017 tables from scholarly publications, Wikipedia, and financial reports, where each table is provided in five different formats: Image, Dictionary, HTML, XML, and LaTeX. Our findings indicate that while LLMs maintain robustness across table modalities, they face significant challenges when processing scientific tables."
# Summary. An optional shortened abstract.
summary: This paper focuses on cross-domain and cross-modality evaluation, comparing the performance of (M)LLMs on both scientific and non-scientific tables, covering image and four text representations of tables.

tags: []

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://openreview.net/pdf?id=umbMEwiTtq'
url_code: 'https://github.com/esborisova/TableEval-Study'
url_dataset: 'https://huggingface.co/datasets/katebor/TableEval'
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Schematic representation of the main phases in our experiments: 1. Develop TableEval dataset, 2. Evaluate each (M)LLM on individual data subsets from TableEval using various table representations (Image, LaTeX, XML, HTML, Dict), 3. Apply interpretability tools to the output yielding post-hoc feature attributions (e.g., using gradient-based saliency) which signify the importance of each token with respect to the model’s output.'
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

