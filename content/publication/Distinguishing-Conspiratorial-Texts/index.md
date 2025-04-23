---
title: 'Towards a Computational Framework for Distinguishing Critical and Conspiratorial Texts by Elaborating on the Context and Argumentation with LLMs'
subtitle: "Ariana Sahitaj, Premtim Sahitaj, Salar Mohtaj, Sebastian Möller, Vera Schmitt - Working Notes of CLEF 2024"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
- Ariana Sahitaj
- Premtim Sahitaj
- Salar Mohtaj
- Sebastian Möller
- Vera Schmitt

# Author notes (optional)
author_notes: 

date: '2024-01-31T00:00:00Z'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2017-01-01T00:00:00Z'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: Working Notes of CLEF 2024
publication_short:

abstract: |
    The shared task of PAN 2024 addresses the need to distinguish between critical and conspiratorial texts in relation to public health measures during the COVID-19 pandemic. In early 2020, the pandemic caused a simultaneous rise in misinformation and conspiracy theories, leading to an ’infodemic’ that increased societal insecurity. This notebook introduces an experimental computational framework leveraging Large Language Models (LLMs) for contextual and argumentative elaborations to enhance the classification accuracy of a reference DeBERTa base classification model. Our approach involves automatic annotations of intent and argumentation style, hypothesizing that these features aid in differentiating between conspiracy and critical texts. Experimental results, however, reveal that DeBERTa performs best without these elaborations, achieving an MCC of 0.838 and F1-macro of 0.917. The inclusion of LLM-generated feature annotations did not surpass the baseline performance. These findings suggest that while theoretically valuable, the practical application of such elaborations requires further refinement. Future work should focus on optimizing LLM outputs and exploring alternative techniques to enhance text classification without overloading models with excessive information.
# Summary. An optional shortened abstract.
summary: 

tags: []

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://ceur-ws.org/Vol-3740/paper-277.pdf'
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