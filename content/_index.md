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
          NLP and XAI Research Group at the <a href="https://www.tu.berlin/en/qu" target="_blank">Quality and Usability Lab TU Berlin</a>
          </span>
        </div>
      text: |
        At the **XplaiNLP research group**, we are shaping the future of **Intelligent Decision Support Systems (IDSS)** by developing AI that is **explainable, trustworthy, and human-centered**. Our research spans the entire **IDSS pipeline**, integrating advances in **natural language processing (NLP), large language models (LLM), explainability (XAI), evaluation, legal frameworks, and human-computer interaction (HCI)** to ensure AI-driven decision-making aligns with ethical and societal values.

        We focus on **high-risk AI applications** where **human oversight is critical**, including **disinformation detection, social media analysis, medical data processing, and legal AI systems**. Our interdisciplinary research tackles key challenges to set new standards for AI-driven decision support, ensuring that these technologies serve society **responsibly and effectively**.
    design:
      background:
        image:
          filename: welcome.jpg
          filters:
            brightness: 0.3
        text_color_light: true

  - block: markdown
    content:
      title: Our Methods
      subtitle: Advancing AI for Responsible Decision Support
      text: |
        We develop and refine AI methodologies that improve decision-making under uncertainty, including:

        - **Retrieval-Augmented Generation (RAG) & Knowledge Retrieval**: Enhancing the factual accuracy and reliability of AI-generated content by integrating structured and unstructured knowledge sources.
        - **Natural Language Processing (NLP) & Large Language Models (LLM)**: Developing specialized **language models for domain-specific tasks**, with a focus on robustness, fairness, and generalization.
        - **Explainable AI (XAI) for NLP**: Creating methods that **enhance model interpretability and user trust**, ensuring that AI explanations are meaningful, especially in high-stakes environments.
        - **Human-Computer Interaction (HCI) & Legal-AI Alignment**: Designing AI systems that are **usable, legally compliant, and human-centered**, optimizing decision workflows for expert and non-expert users.
        - **Evaluation & Safety of AI Models**: Establishing rigorous **performance assessment frameworks** to measure **bias, reliability, and long-term impact** of AI systems in real-world applications.
    design:
      columns: '1'

  - block: markdown
    content:
      title: Our Applications
      subtitle: Tackling High-Risk AI Challenges
      text: |
        We apply our AI advancements to critical, real-world decision-making scenarios, including:

        - **Disinformation Detection & Social Media Analysis**: Investigating **misinformation, hate speech, and propaganda** using advanced **NLP and XAI** methods. We analyze how AI-driven detection changes over time and how **human perception of AI explanations evolves**.
        - **Medical Data Processing & Trustworthy AI in Healthcare**: Developing AI tools that **simplify access to medical information**, improve **faithfulness and factual consistency** in medical text generation, and support clinicians in **interpreting AI-generated recommendations**.
        - **Legal & Ethical AI for High-Stakes Domains**: Ensuring AI decision support complies with **regulatory standards**, enhances **explainability in legal contexts**, and aligns with **ethical AI principles**.
    design:
      columns: '1'

  - block: portfolio
    content:
      title: Research
      subtitle: "Advancing Transparent and Trustworthy AI for Decision Support in High-Stakes Domains"
      text: |
        In the XplaiNLP Group, we create intelligent decision support systems (IDSS), by researching the whole cycle from developing and implementing large language models, and designing user interfaces with human-meaningful representations of model outputs and metadata, by implementing eXplanations and transparency features from NLP-based predictions.
      filters:
        folders:
          - research
        tags: []

  - block: collection
    content:
      title: News
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
      columns: '2'

  - block: markdown
    content:
      title: Projects
      text: |
        # Running
        ### [NEWS-POLYGRAPH](/projects/past_projects/news_polygraph/)
        Verification and Extraction of Disinformation Narr
