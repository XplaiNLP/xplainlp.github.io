---
title: "Persona Prompting as a Lens on LLM Social Reasoning"
subtitle: 'Jing Yang, Moritz Hechtbauer, Elisabeth Khalilov, Evelyn Luise Brinkmann, Vera Schmitt, Nils Feldhus - arXiv preprint'
authors:
  - Jing Yang
  - Moritz Hechtbauer
  - Elisabeth Khalilov
  - Evelyn Luise Brinkmann
  - Dr. Vera Schmitt
  - Nils Feldhus
date: "2026-01-28T00:00:00Z"
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

abstract: For socially sensitive tasks like hate speech detection, the quality of explanations from Large Language Models (LLMs) is crucial for factors like user trust and model alignment. While Persona prompting (PP) is increasingly used as a way to steer model towards user-specific generation, its effect on model rationales remains underexplored. We investigate how LLM-generated rationales vary when conditioned on different simulated demographic personas. Using datasets annotated with word-level rationales, we measure agreement with human annotations from different demographic groups, and assess the impact of PP on model bias and human alignment. Our evaluation across three LLMs results reveals three key findings (1) PP improving classification on the most subjective task (hate speech) but degrading rationale quality. (2) Simulated personas fail to align with their real-world demographic counterparts, and high inter-persona agreement shows models are resistant to significant steering. (3) Models exhibit consistent demographic biases and a strong tendency to over-flag content as harmful, regardless of PP. Our findings reveal a critical trade-off while PP can improve classification in socially-sensitive tasks, it often comes at the cost of rationale quality and fails to mitigate underlying biases, urging caution in its application. 

# Summary. An optional shortened abstract.
summary: 
tags:
featured: true

url_pdf: https://arxiv.org/abs/2601.20757
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
