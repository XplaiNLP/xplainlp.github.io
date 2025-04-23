---
title: 'Utilising Large Language Models for Adversarial Attacks in Text-to-SQL: A Perpetrator and Victim Approach'
subtitle: "Sahitaj, Ariana; Nilles, Markus; Schenkel, Ralf; Schmitt, Vera (2025). Datenbanksysteme für Business, Technologie und Web (BTW 2025). DOI: 10.18420/BTW2025-59. Gesellschaft für Informatik, Bonn. EISSN: 2944-7682. pp. 919-931. Student Track. Bamberg. 3.-7. März 2025"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
- Ariana Sahitaj
- Markus Nilles
- Ralf Schenkel
- Dr. Vera Schmitt

# Author notes (optional)
author_notes: 

date: '2025-03-03T00:00:00Z'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2017-01-01T00:00:00Z'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: Datenbanksysteme für Business, Technologie und Web (BTW 2025)
publication_short: BTW(2025)

abstract: |
    This paper investigates the use of Large Language Models (LLMs) for the Text-to-SQL task, both as Perpetrator models for generating adversarial attacks and as Victim models for assessing their robustness. In this study, two state-of-the-art LLMs, Llama3 with 70 billion and Mixtral with 47 billion parameters, were employed as Perpetrators to generate adversarial examples at the character-, word-, and sentence-level. A total of 77,292 adversarial examples were generated from 2,147 data points of the Spider test-set using three additional LLMs as Victims and evaluated thoroughly. These Victim models are based on Llama3 with 8 billion parameters and differ only in the extent of fine-tuning for related benchmark tasks. The results show that attacks at the word-level, particularly through synonym replacements, most significantly impair model performance. Additionally, providing database schemas significantly improves execution accuracy, while fine-tuning does not always enhance robustness against adversarial attacks. This work provides important insights into improving the reliability of Text-to-SQL models in future applications and makes a significant contribution to the further development of these models in research.
# Summary. An optional shortened abstract.
summary: 

tags: []

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://dl.gi.de/items/66a63fc0-f9a7-49a0-8ec1-41c00fb7fe65'
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