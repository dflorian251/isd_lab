---
layout: staff
title: Staff
description: ""
navorder: 1
---
<h2>Faculty Members</h2>
<ul class = "staff-list" id = "faculty-staff">
  {% assign faculty_staff = site.data.staff | where: "member", "faculty" %}
  {% for staff in faculty_staff %}
    <li>
      <div class = "staff-avatar-container">
        <img src="{{ staff.avatar }}" alt="{{ staff.name }}">
      </div>
      <div class = "staff-name-container">
        <h3 class = "staff-name">
          {% assign splited_name = staff.name | split:' ' %}
          <a href = "{{ staff.url }}">
            {% for name in splited_name%}
              {{ name }}<br>
            {% endfor %}
          </a>
        </h3>
      </div>
      <p>{{ staff.rank }}</p>
      <p>{{ staff.bio }}</p>
    </li>
  {% endfor %}
</ul>

<h2>Researchers</h2>
<ul class = "staff-list">
  {% assign researchers_staff = site.data.staff | where: "member", "researcher" %}
  {% for staff in researchers_staff %}
    <li>
      <div class = "staff-avatar-container">
        <img src="{{ staff.avatar }}" alt="{{ staff.name }}">
      </div>
      <div class = "staff-name-container">
        <h3 class = "staff-name">
          <a href = "#">
            {{ staff.name }}
          </a>
        </h3>
      </div>
      <p>{{ staff.rank }}</p>
      <p>{{ staff.bio }}</p>
    </li>
  {% endfor %}
</ul>
