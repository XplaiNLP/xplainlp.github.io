---
title: "Cross-Refine: Improving Natural Language Explanation Generation by Learning in Tandem"
subtitle: 'Qianli Wang, Tatiana Anikina, Nils Feldhus, Simon Ostermann, Sebastian Möller, Vera Schmitt'
authors:
  - Qianli Wang
  - Tatiana Anikina
  - Nils Feldhus
  - Simon Ostermann
  - Sebastian Möller
  - Vera Schmitt
date: "2024-09-11T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date). 2024/9/11
publishDate: "2024-09-11T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["paper-conference"]

# Publication name and optional abbreviated publication name.
publication: "COLING 2025"
publication_short: "COLING 2025"

abstract: Natural language explanations (NLEs) are vital for elucidating the reasoning behind large language model (LLM) decisions. Many techniques have been developed to generate NLEs using LLMs. However, like humans, LLMs might not always produce optimal NLEs on first attempt. Inspired by human learning processes, we introduce Cross-Refine, which employs role modeling by deploying two LLMs as generator and critic, respectively. The generator outputs a first NLE and then refines this initial explanation using feedback and suggestions provided by the critic. Cross-Refine does not require any supervised training data or additional training. We validate Cross-Refine across three NLP tasks using three state-of-the-art open-source LLMs through automatic and human evaluation. We select Self-Refine (Madaan et al., 2023) as the baseline, which only utilizes self-feedback to refine the explanations. Our findings from automatic evaluation and a user study indicate that Cross-Refine outperforms Self-Refine. Meanwhile, Cross-Refine can perform effectively with less powerful LLMs, whereas Self-Refine only yields strong results with ChatGPT. Additionally, we conduct an ablation study to assess the importance of feedback and suggestions. Both of them play an important role in refining explanations. We further evaluate Cross-Refine on a bilingual dataset in English and German.

# Summary. An optional shortened abstract.
summary: 
tags:
featured: false

url_pdf: https://aclanthology.org/2025.coling-main.77.pdf
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
