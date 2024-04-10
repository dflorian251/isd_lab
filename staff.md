---
layout: staff
title: Staff
description: ""
navorder: 6
---

<ul>
  {% for staff in site.authors %}
    <li>
      <img src="{{ staff.avatar }}" alt="{{ staff.name }}">
      <h3>{{ staff.name }}</h3>
      <p>{{ staff.role }}</p>
      <p>{{ staff.bio }}</p>
    </li>
  {% endfor %}
</ul>
