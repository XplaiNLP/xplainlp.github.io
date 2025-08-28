---
title: ""
date: 2022-10-24
type: landing

sections:
  - block: hero
    content:
      title: |
        <div style="display: flex; justify-content: center; align-items: center; text-align: center; height: 10vh; color: white;">
          
        </div>
        <div style="display: flex; justify-content: center; align-items: center; text-align: center; height: 120vh;">
          <span style="color:rgba(150, 148, 148, 0.87); font-size: 1rem;">
    
          </span>
        </div>
      # The text key is now empty as requested, so no text appears over the image.
      text: |
    design:
      background:
        image:
          filename: team_park_all.jpg
          filters:
            brightness: 0.99
          height: 120vh
      text_color_light: true
      css_class: wide-hero

  - block: markdown
    content:
      title: XplaiNLP Research Group
      text: |
        ### **XplaiNLP: Explainable and Interpretable NLP for Trustworthy and Meaningful Decision Support in High-Stake Domains**

        At the **XplaiNLP research group** at the <a href="https://www.tu.berlin/en/qu" target="_blank">Quality and Usability Lab TU Berlin</a>, we are researching on the future of **Intelligent Decision Support Systems (IDSS)** by developing AI that is **explainable, trustworthy, and human-centered**. Our research spans the entire **IDSS pipeline**, integrating advances in **NLP/(M)LLMs, XAI/Interpretability, HCI, and legal analysis** to ensure AI-driven decision-making aligns with ethical and societal values.

        We focus on **high-risk AI applications** where **human oversight is critical**, including **disinformation detection, social media analysis, medical data processing, and legal AI systems**. 

        ### **Our Applications: Tackling High-Risk AI Challenges**
        We adeveloping and deploying AI tools for real-world decision-making scenarios, including:

        - **Disinformation Detection & Social Media Analysis**: Investigating **mis- disinformation, hate speech, propaganda and FIMI** using advanced **NLP, XAI and Interpretability** methods. 
        - **Medical Data Processing & Trustworthy AI in Healthcare**: Developing AI tools that **simplify access to medical information**, improve **faithfulness and factual consistency** in medical text generation, and support clinicians in **interpreting AI-generated recommendations**.
        - **Legal & Ethical AI for High-Stakes Domains**: Ensuring AI decision support complies with **regulatory standards**, enhances **explainability in legal contexts**, and aligns with **ethical AI principles**.

        Through **interdisciplinary collaboration, hands-on research, and mentorship**, **XplaiNLP** is at the forefront of shaping AI that is not only powerful but also **transparent, fair, and accountable**. Our goal is to **set new standards for AI-driven decision support**, ensuring that these technologies serve society **responsibly and effectively**.
    design:
      # This block will now have a standard background, not the hero image.
      columns: '1'
    

  - block: portfolio
    content:
      title: Research
      subtitle: "Advancing Transparent and Trustworthy AI for Decision Support in High-Stakes Domains"
      text: |
        In the XplaiNLP Group, we create intelligent decision support systems (IDSS), by researching the whole cycle from developing and implementing large language models, and designing user interfaces with human-meaningful representations of model outputs and metadata, by implementing eXplanations and transparency features from NLP-based predictions.
      filters:
        # Folders to display content from
        folders:
          - research
        # Only show content with these tags
        tags: []

  - block: collection
    content:
      title: News
      subtitle: ""
      text: ""
      count: 3
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: news
    design:
      view: compact
      columns: '1'

  - block: markdown
    content:
      title: Projects
      text: |
        # Running
        ### [NEWS-POLYGRAPH](/projects/past_projects/news_polygraph/)
        Verification and Extraction of Disinformation Narratives with Individualized Explanations
        ### [VERANDA](/projects/past_projects/veranda/)
        Trustworthy Anonymization of Sensitive Patient Records for Remote Consultation (VERANDA)
        ### [VeraXtract](/projects/past_projects/veraXtract/)
        Verification and Extraction of Disinformation Narratives with Individualized Explanations
        ### [fakeXplain](/projects/past_projects/fakeXplain/)
        Transparent and meaningful explanations in the context of disinformation detection
        ### [PSST](/projects/running_projects/psst/)
        Removing identifying features in speech, improving interactions between devices and cloud services, and creating new ways to assess privacy threats
        ### ORCHESTRA
        Orchestrating Reliable, Compliant, and eXplainable Agentic AI Workflows

        # Under Review
        ### Fake-O-Meter
        Multimodaler KI-basierter Desinformations-Assistent für Aufklärung und Resilienz im Umgang mit medialen Desinformationen
        ### Deutsch-Israleische Projektkooperation (DIP)
        Adaptive AI for High-Stakes Decision Processes: Balancing Automation and Human Control

        # Past
        #### [ateSDG](/projects/past_projects/ateSGD/)
        Analyzing Sustainability Reports from companies and classifying them according to their contribution to one or multiple SDGs
        #### [DFG-project LocTrace](/projects/past_projects/DFG/)
        Evaluation of different methods for the monetary evaluation of privacy
    design:
      columns: '1'


  - block: markdown
    content:
      title: Teaching
      text: |
        ### [Natural Language Processing (Summer Term)](https://moseskonto.tu-berlin.de/moses/modultransfersystem/bolognamodule/beschreibung/anzeigen.html?nummer=41047&version=1&sprache=2)
        ### Privacy Seminar (Summer Term)
        ### Advanced Study Projects (Summer and Winter Term)
    design:
      columns: '1'

  - block: markdown
    content:
      title: Partnerships
      text: |
        ## Research Partners
        <div style="display: flex; gap: 20px;">

        <div style="flex: 1;">

        - [DFKI SLT](https://www.dfki.de/web/forschung/forschungsbereiche/speech-and-language-technology)
        - [BIH Charité](https://www.bihealth.org/en/)
        - [IfSS Charité](https://sexualmedizin.charite.de/)
        - [Fraunhofer IDMT](https://www.idmt.fraunhofer.de/)
        - [Fraunhofer AISEC](https://www.aisec.fraunhofer.de/)
         </div>

        <div style="flex: 1;">

        - [CopeNLU University of Copenhagen](https://www.copenlu.com/)
        - [Tel Aviv university](https://english.tau.ac.il/profile/jmeyer)
        - [Oxford University](https://www.cs.ox.ac.uk/people/ani.calinescu/)
        - [IRIT Toulouse](https://www.irit.fr/)

        </div>

        </div>

        ## Media and Industry Partners
        <div style="display: flex; gap: 20px;">

        <div style="flex: 1;">

        - [Deutsche Presse-Agentur (dpa)](https://www.dpa.com/)
        - [Deutsche Welle (DW)](https://www.dw.com/en)
        - [Rundfunk Berlin-Brandenburg (rbb)](https://www.rbb-online.de/)
        - [Ubermetrics Technology GmbH/Unicepta](https://www.ubermetrics.de/)
        - [Exorde Labs France](https://www.exordelabs.com/)
    

        </div>

        <div style="flex: 1;">

        - [delphai/INTAPP GmbH](https://www.delphai.com/)
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
      columns: '1'
---
