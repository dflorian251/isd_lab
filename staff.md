---
layout: staff
title: Staff
description: ""
navorder: 6
---
<h2>Faculty Members</h2>
<ul>
  {% assign filtred_staff = site.data.staff | where: "member", "faculty" %}
  {% for staff in filtred_staff    %}
    <li>
      <img src="{{ staff.avatar }}" alt="{{ staff.name }}">
      <h3>{{ staff.name }}</h3>
      <p>{{ staff.role }}</p>
      <p>{{ staff.bio }}</p>
    </li>
  {% endfor %}
</ul>

<h2>Researchers</h2>
