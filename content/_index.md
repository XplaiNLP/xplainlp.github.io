---
title: ""
date: 2022-10-24
type: landing

sections:
  - block: hero
    content:
      title: |
        <div style="display: flex; justify-content: center; align-items: center; text-align: center; height: 10vh; color: white;">
          XplaiNLP Research Group
        </div>
        <div style="display: flex; justify-content: center; align-items: center; text-align: center; height: 10vh;">
          <span style="color:rgba(150, 148, 148, 0.87); font-size: 1rem;">
          NLP and XAI Research Group at the <a href="https://www.tu.berlin/en/qu" target="_blank">Quality and Usability Lab TU Berlin</a>
          </span>
        </div>
      # The text key is now empty as requested, so no text appears over the image.
      text: |
    design:
      background:
        image:
          filename: welcome.jpg
          filters:
            brightness: 0.3
      text_color_light: true

  - block: markdown
    content:
      title: Welcome to XplaiNLP Research Group
      text: |
        ### **XplaiNLP: Advancing Transparent and Trustworthy AI for Decision Support in High-Stakes Domains**

        At the **XplaiNLP research group**, we are shaping the future of **Intelligent Decision Support Systems (IDSS)** by developing AI that is **explainable, trustworthy, and human-centered**. Our research spans the entire **IDSS pipeline**, integrating advances in **natural language processing (NLP), large language models (LLM), explainability (XAI), evaluation, legal frameworks, and human-computer interaction (HCI)** to ensure AI-driven decision-making aligns with ethical and societal values.

        We focus on **high-risk AI applications** where **human oversight is critical**, including **disinformation detection, social media analysis, medical data processing, and legal AI systems**. Our interdisciplinary research tackles the following key challenges:

        ### **Our Methods: Advancing AI for Responsible Decision Support**

        We develop and refine AI methodologies that improve decision-making under uncertainty, including:

        - **Retrieval-Augmented Generation (RAG) & Knowledge Retrieval**: Enhancing the factual accuracy and reliability of AI-generated content by integrating structured and unstructured knowledge sources.
        - **Natural Language Processing (NLP) & Large Language Models (LLM)**: Developing specialized **language models for domain-specific tasks**, with a focus on robustness, fairness, and generalization.
        - **Explainable AI (XAI) for NLP**: Creating methods that **enhance model interpretability and user trust**, ensuring that AI explanations are meaningful, especially in high-stakes environments.
        - **Human-Computer Interaction (HCI) & Legal-AI Alignment**: Designing AI systems that are **usable, legally compliant, and human-centered**, optimizing decision workflows for expert and non-expert users.
        - **Evaluation & Safety of AI Models**: Establishing rigorous **performance assessment frameworks** to measure **bias, reliability, and long-term impact** of AI systems in real-world applications.

        ### **Our Applications: Tackling High-Risk AI Challenges**
        We apply our AI advancements to critical, real-world decision-making scenarios, including:

        - **Disinformation Detection & Social Media Analysis**: Investigating **misinformation, hate speech, and propaganda** using advanced **NLP and XAI** methods. We analyze how AI-driven detection changes over time and how **human perception of AI explanations evolves**.
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
        ## Academic Partnerships
        <div style="display: flex; gap: 20px;">

        <div style="flex: 1;">

        - [Deutsche Presse-Agentur (dpa)](https://www.dpa.com/)
        - [Deutsche Welle (DW)](https://www.dw.com/en)
        - [Rundfunk Berlin-Brandenburg (rbb)](https://www.rbb-online.de/)
        - [Ubermetrics Technology GmbH/Unicepta](https://www.ubermetrics.de/)

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
