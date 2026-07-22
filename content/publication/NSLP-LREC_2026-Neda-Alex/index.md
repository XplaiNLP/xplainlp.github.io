---
title: "Retrieval-Augmented LLMs and Encoder Models for Multi-Label Climate Disinformation Narrative Classification"
subtitle: 'Foroutan, N., Tsiakalou, A., & Schmitt, V. (2026). Retrieval-Augmented LLMs and Encoder Models for Multi-Label Climate Disinformation Narrative Classification . In Proceedings of Natural Scientific Language Processing (NSLP) @ LREC 2026'
authors:
  - Neda Foroutan 
  - Alexandra Tsiakalou
  - Dr. Vera Schmitt
date: "2026-05-11T00:00:00Z"
doi: "10.63317/2sxk32q2vrqz"


publishDate: "2026-05-16T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["workshop-paper"]

# Publication name and optional abbreviated publication name.
publication: Proceedings of Natural Scientific Language Processing at LREC 2026
publication_short: (NSLP) @ LREC 2026

abstract: The detection of climate misinformation narratives remains challenging due to label imbalance, hierarchical taxonomies, and the multi-label nature of real-world claims. Developing models that can reliably assign fine-grained narrative categories is therefore essential for scalable analysis of climate disinformation. We present our approach to multi-label climate misinformation narrative classification for ClimateCheck@NSLP 2026 Task 2. The task requires assigning one or more narrative categories, defined by the hierarchical CARDS taxonomy, to climate-related claims. We investigate both encoder-based transformers and decoder-only large language models (LLMs), comparing fine-tuning BERT-based models with prompt-based and retrieval-augmented instruction tuning strategies with Qwen3 model. To address data scarcity and label imbalance, we explore targeted augmentation using external CARDS-based resources as well as semantic similarity filtering. Our experiments show that augmentation improves encoder-based models, with ModernBERT achieving competitive performance at low computational cost. However, the strongest results are obtained using retrieval-augmented instruction tuning with Qwen3, which narrows the candidate narrative space prior to prediction. This approach achieves a Macro-F1 score of 59.72% on the official test set, securing second place on the leaderboard. These findings demonstrate the effectiveness of retrieval-guided LLM adaptation for structured multi-label narrative classification while highlighting the continued relevance of efficient encoder-based models.


# Summary. An optional shortened abstract.
summary: 
tags:
featured: true

url_pdf: https://lrec.elra.info/lrec2026-ws-nslp-22
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
