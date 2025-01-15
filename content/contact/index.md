---
title: Contact
date: 2022-10-24

type: landing

sections:
  - block: hero
    content:
      title: |
        <div style="display: flex; justify-content: center; align-items: center; text-align: center; height: 10vh;">
          About Us
        </div>
        <div style="display: flex; justify-content: center; align-items: center; text-align: center; height: 10vh;">
          <span style="color: #DCDCDC; font-size: 1rem;">
          Our mission is to advance the field of Natural Language Processing through explainable and user-centric approaches. We focus on developing transparent, efficient, and practical NLP solutions that bridge the gap between complex language models and human understanding.
          </span>
        </div>
    design:
      background:
        image: 
          filename: contact.jpg
          filters:
            brightness: 0.3
        text_color_light: true

  - block: markdown
    content:
      title: Applications
      text: |
        Although we are always looking for highly motivated and talented researchers, we get far more applications than we have positions available. If you’d like to join our team, please do not send your applications via email but see the following:

        #### Postdocs
        Leading researches that

        #### PhD students
        We are always looking for talented PhD student candidates

        #### Internships, Lab Rotations, Bachelor or Master Thesis
        As we get many requests, we can evaluate only a small fraction carefully. Generally, you should not expect a response. You can increase the chances of your application by carefully answering our ...

        #### Questions
        If you have questions regarding applications, please contact ...
    design:
      columns: '2'
      spacing:
        padding: ['20px', '0', '20px', '0']
  - block: contact
    content:
      title: Contact
      text: |-
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer tempus augue non tempor egestas. Proin nisl nunc, dignissim in accumsan dapibus, auctor ullamcorper neque. Quisque at elit felis. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean eget elementum odio. Cras interdum eget risus sit amet aliquet. In volutpat, nisl ut fringilla dignissim, arcu nisl suscipit ante, at accumsan sapien nisl eu eros.
      email: test@example.org
      phone: 888 888 88 88
      address:
        street: Ernst-Reuter-Platz 7
        city: Berlin
        region: Berlin
        postcode: '10587'
        country: Germany
        country_code: DE
      coordinates:
        latitude: '52.512779'
        longitude: '13.320082'
      office_hours:
        - 'Monday 10:00 to 13:00'
        - 'Wednesday 09:00 to 10:00'
      #contact_links:
      #  - icon: comments
      #    icon_pack: fas
      #    name: Discuss on Forum
      #    link: 'https://discourse.gohugo.io'
    
      # Automatically link email and phone or display as text?
      autolink: false
    
    design:
      columns: '2'
---
