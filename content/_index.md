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
      subtitle: "Advancing Transparent and Trustworthy AI for Decision Support in High-Stakes Domains"
      text: |
        At XplaiNLP research group, we are shaping the future of Intelligent Decision Support Systems (IDSS) by developing AI that is explainable, trustworthy, and human-centered. Our research spans the entire IDSS pipeline, integrating advances in natural language processing (NLP), large language models (LLM), explainability (XAI), evaluation, legal frameworks, and human-computer interaction (HCI) to ensure AI-driven decision-making aligns with ethical and societal values. We focus on high-risk AI applications where human oversight is critical, including disinformation detection, social media analysis, medical data processing, and legal AI systems. Our interdisciplinary research tackles the following key challenges.
        Through interdisciplinary collaboration, hands-on research, and mentorship, XplaiNLP is at the forefront of shaping AI that is not only powerful but also transparent, fair, and accountable. Our goal is to set new standards for AI-driven decision support, ensuring that these technologies serve society responsibly and effectively.


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
        <div style="display: flex; gap: 20px;">

        <div style="flex: 1;">

        - [Quality and Usability Lab, TU Berlin](https://www.tu.berlin/qu)
        - [Berlin Institute for the Foundations of Learning and Data (BIFOLD)](https://www.bifold.berlin)
        - [Einstein Center Digital Future (ECDF)](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.digital-future.berlin/&ved=2ahUKEwjXj6b_252LAxXlSvEDHZIUKl4QFnoECBAQAQ&usg=AOvVaw0tcYQGq7jghqPvw4fGUbht)

        </div>

        <div style="flex: 1;">

        - [German Research Center for Artificial Intelligence (DFKI)](https://www.dfki.de/web/dfki/en)
        - Fraunhofer [IDMT](https://www.idmt.fraunhofer.de) / [AISEC](https://www.aisec.fraunhofer.de/)
        - [BIH/IfSS](https://www.bih-ifss.de/)
        - [Charité](https://www.charite.de/)

        </div>
        </div>


        ## Industry Collaborations
        <div style="display: flex; gap: 20px;">

        <div style="flex: 1;">

        - [Deutsche Welle (DW)](https://www.dw.com/en)
        - [Rundfunk Berlin-Brandenburg (RBB)](https://www.rbb-online.de/)
        - [Deutsche Presse-Agentur (dpa)](https://www.dpa.com/)
        - [Ubermetrics Technology GmbH](https://www.ubermetrics.de/)

        </div>

        <div style="flex: 1;">

        - [INTAPP GmbH](https://www.intapp.de/)
        - [Transfermedia GmbH](https://www.transfermedia.de/)
        - [Crowdee GmbH](https://www.crowdee.de/)
        - [AI Berlin](https://www.ai-berlin.de/)

        </div>

        </div>

        ## Research Networks

        <div style="display: flex; gap: 20px;">

        <div style="flex: 1;">

        - [CERTAIN](https://www.certain-trust.eu/)

        </div>

        <div style="flex: 1;">

        - [AI4Media](https://www.ai4media.eu/)

        </div>

        <div style="flex: 1;">

        - [AI-GRID](https://www.ai-grid.eu/)

        </div>

        </div>
  
    design:
      columns: '2'
---
