---
title: People
date: 2025-01-09
type: landing
sections:
  - block: slider
    content: {}
    design:
      columns: '1'
  - block: people
    content:
      title: Meet the Team
      user_groups:
        - Group Lead
        - Honorary Professorship
        - Administration
        - Senior Researchers
        - Researchers
        - Guest-researchers & Partners
        - Research Assistants
      sort_by: weight
      sort_ascending: true
    design:
      show_interests: false
      show_role: true
      show_social: false
      show_organizations: false

  - block: slider
    content:
      slides:
      - title: 👋 Welcome to the group
        content: Take a look at what we're working on...
        align: center
        background:
          image:
            filename: coders.jpg
            filters:
              brightness: 0.7
          position: right
          color: '#666'
      - title: Lunch & Learn ☕️
        content: 'Share your knowledge with the group and explore exciting new topics together!'
        align: left
        background:
          image:
            filename: contact.jpg
            filters:
              brightness: 0.7
          position: center
          color: '#555'
      - title: World-Class Semiconductor Lab
        content: 'Just opened last month!'
        align: right
        background:
          image:
            filename: welcome.jpg
            filters:
              brightness: 0.5
          position: center
          color: '#333'
        link:
          icon: graduation-cap
          icon_pack: fas
          text: Join Us
          url: ../contact/
    design:
      # Slide height is automatic unless you force a specific height (e.g. '400px')
      slide_height: ''
      is_fullscreen: true
      # Automatically transition through slides?
      loop: true
      # Duration of transition between slides (in ms)
      interval: 1500
---
