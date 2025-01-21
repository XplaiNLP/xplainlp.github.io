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
          <span style="color: #DCDCDC; font-size: 1rem;">
          Advancing Natural Language Processing at the Quality and Usability Lab, Technische Universität Berlin.
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
      subtitle: Our mission is to advance the field of Natural Language Processing through explainable and user-centric approaches. We focus on developing transparent, efficient, and practical NLP solutions that bridge the gap between complex language models and human understanding.

      filters:
        # Folders to display content from
        folders:
          - research
        # Only show content with these tags
        tags: []
  
  - block: collection
    content:
      title: Latest News
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
        ### [NEWS-POLYGRAPH](https://news-polygraph.com/)
        Verification and Extraction of Disinformation Narratives with Individualized Explanations
        ### [VERANDA](https://www.tu.berlin/qu/forschung/laufende-vergangene-projekte/laufende-projekte/veranda)
        Trustworthy Anonymization of Sensitive Patient Records for Remote Consultation (VERANDA)
        ### [VeraXtract](https://www.tu.berlin/en/qu/research/current-past-projects/laufende-projekte/veraxtract)
        Verification and Extraction of Disinformation Narratives with Individualized Explanations


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
