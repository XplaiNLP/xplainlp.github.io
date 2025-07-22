---
title: People
date: 2025-01-09

type: landing

sections:
  - block: slider 
    content:
    design:
      # Use full-width design so the slider can be centered nicely
      columns: '1'
  - block: people
    content:
      title: Meet the Team
      # Choose which groups/teams of users to display.
      #   Edit `user_groups` in each user's profile to add them to one or more of these groups.
      user_groups:
          - Group Lead
          - Honorary Professorship
          - Administration
          - Senior Researchers
          - Researchers
          - Guest-researchers & Partners
          - Research Assistants
      <!-- sort_by: Params.last_name -->
      sort_by: weight
      sort_ascending: true
      
    design:
      show_interests: false
      show_role: true
      show_social: false
      show_organizations: false
      
      
---
