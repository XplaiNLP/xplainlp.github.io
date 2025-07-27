---
title: 'Improving Sentiment Analysis for Ukrainian Social Media Code-Switching Data'
subtitle: "Yurii Shynkarov, Veronika Solopova, Vera Schmitt"
" 

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
- Yurii Shynkarov
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
  This paper addresses the challenges of sentiment analysis in Ukrainian social media, where users frequently engage in code-switching with Russian and other languages. We introduce COSMUS (COde-Switched MUltilingual Sentiment for Ukrainian Social media), a 12,224-texts corpus collected from Telegram channels, product‐review sites and open datasets, annotated into positive, negative, neutral and mixed sentiment classes as well as language labels (Ukrainian, Russian, code-switched). We benchmark three modeling paradigms: (i) few‐shot prompting of GPT‐4o and DeepSeek V2-chat, (ii) multilingual mBERT, and (iii) the Ukrainian‐centric UkrRoberta. We also analyze calibration and LIME scores of the latter two solutions to verify its performance on various language labels. To mitigate data sparsity we test two augmentation strategies: back‐translation consistently hurts performance, whereas a Large Language Model (LLM) word‐substitution scheme yields up to +2.2% accuracy. Our work delivers the first publicly available dataset and comprehensive benchmark for sentiment classification in Ukrainian code‐switching media. Results demonstrate that language‐specific pre‐training combined with targeted augmentation yields the most accurate and trustworthy predictions in this challenging low‐resource setting.
# Summary. An optional shortened abstract.
summary: 

tags: []

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://aclanthology.org/2025.unlp-1.18/'
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


