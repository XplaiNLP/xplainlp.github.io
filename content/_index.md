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

  - block: markdown
    content:
      title: Research
      text: |
        Our mission is to advance the field of Natural Language Processing through explainable and user-centric approaches. We focus on developing transparent, efficient, and practical NLP solutions that bridge the gap between complex language models and human understanding.

        #### Explainable AI in NLP
        Developing transparent models that elucidate decision-making processes in natural language understanding, making AI systems more interpretable and trustworthy.

        #### Human-Computer Interaction
        Enhancing user experience through intuitive language-based interfaces and studying how humans interact with language models.

        #### Machine Learning for NLP
        Advancing algorithms that improve language comprehension and generation while maintaining transparency and efficiency.
    design:
      columns: '2'
      spacing:
        padding: ['20px', '0', '20px', '0']
  
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

  - block: collection
    content:
      title: Publications
      text: ""
      count: 5
      filters:
        folders:
          - publication
        publication_type: 'article'
      offset: 0
      order: desc
      page_type: publication
    design:
      view: citation
      columns: '2'

  - block: markdown
    content:
      title: Broader Impact
      text: |
        ## Educational Initiatives
        The XplaiNLP Lab is committed to democratizing NLP education and research:

        #### NLP4Kids
        An educational initiative bringing natural language processing concepts to primary and secondary school students through interactive workshops and learning materials.

        #### Open Source Contributions
        We actively contribute to the open-source community by releasing research code, datasets, and educational resources.

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
