---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: hero
    content:
      title: |
        <div style="display: flex; justify-content: center; align-items: center; text-align: center; height: 10vh;">
          XplaiNLP Research Group
        </div>
        <div style="display: flex; justify-content: center; align-items: center; text-align: center; height: 10vh;">
          <span style="color:rgba(150, 148, 148, 0.87); font-size: 1rem;">
          NLP Research Group at the Quality and Usability Lab,
          Technische Universität Berlin
          </span>
        </div>
    design:
      background:
        image:
          filename: welcome.jpg
          filters:
            brightness: 0.3
        text_color_light: true

  - block: portfolio
    content:
      title: Research
      subtitle: In the XplaiNLP Group, we create intelligent decision support systems (IDSS), by researching the whole cycle from developing and implementing large lansguage models, and designing user interfaces with human-meaningful representations of model outputs and metadata, by implementing eXplanations and transparency features from NLP-based predictions.

      filters:
        # Folders to display content from
        folders:
          - research
        # Only show content with these tags
        tags: []
  
  - block: collection
    content:
      title: News
      subtitle:
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
    design:
      view: compact
      columns: '2'

  - block: markdown
    content:
      title: Projects
      text: |
        ## Running
        ### [NEWS-POLYGRAPH](https://news-polygraph.com/)
        Verification and Extraction of Disinformation Narratives with Individualized Explanations
        ### [VERANDA](https://www.tu.berlin/qu/forschung/laufende-vergangene-projekte/laufende-projekte/veranda)
        Trustworthy Anonymization of Sensitive Patient Records for Remote Consultation (VERANDA)
        ### [VeraXtract](https://www.tu.berlin/en/qu/research/current-past-projects/laufende-projekte/veraxtract)
        Verification and Extraction of Disinformation Narratives with Individualized Explanations

        ## Past
        ### [ateSDG](https://www.tu.berlin/en/qu/forschung/laufende-vergangene-projekte/laufende-projekte/atesdg)
        ### [DFG-project LocTrace](https://www.tu.berlin/en/qu/research/current-past-projects/past-projects/monetary-valuation-of-location-information)
    design:
      columns: '2'

  - block: markdown
    content:
      title: Teaching
      text: |
        ### [Natural Language Processing (Summer Term)](https://moseskonto.tu-berlin.de/moses/modultransfersystem/bolognamodule/beschreibung/anzeigen.html?nummer=41047&version=1&sprache=2)
        ### Privacy Seminar (Summer Term)
        ### Advanced Study Projects (Summer and Winter Term)

    design:
      columns: '2'


  - block: markdown
    content:
      title: Partnerships
      text: |
        ## Academic Partnerships
        * Quality and Usability Lab, TU Berlin
        * Berlin Institute for the Foundations of Learning and Data (BIFOLD)
        * Einstein Center Digital Future (ECDF)

        ## Industry Collaborations
        * Tech Innovation Hub Berlin
        * Language AI Research Consortium

        ## Research Networks
        * European Association for NLP
        * German Research Network for AI
    design:
      columns: '2'

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
    design:
      columns: '1'
---
