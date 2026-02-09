---
layout: page
title: Biography
permalink: /bio/
description: Learn about Nicolas Leins' academic background, research at ZIB, and experience in VR, AR, and Industrial Software.
---
<style>.post-header { display: none; }</style>

<div class="card">
  <h1 style="margin-top: 0;">Biography</h1>
  <p style="font-size: 1.1em; color: #4b5563;">
    {{ site.data.person.bio_long }}
  </p>
</div>

<div class="bio-grid">

  <!-- Left Column -->
  <div>
    <h2 style="margin-top: 0;">Education</h2>
    <div class="card">
      {% for edu in site.data.person.education %}
      <h3 style="font-size: 1.1em; margin-bottom: 5px;">{{ edu.degree }}</h3>
      <div style="color: #446b59; font-weight: 600;">{{ edu.institution }}</div>
      <div style="color: #6b7280; font-size: 0.9em; margin-bottom: 10px;">{{ edu.status }}</div>
      {% if forloop.last == false %}
      <hr style="border-top: 1px solid #f3f4f6; margin: 15px 0;">
      {% endif %}
      {% endfor %}
    </div>

    <h2 style="margin-top: 20px;">Research Interests</h2>
    <div class="card">
      <ul style="margin-bottom: 0; padding-left: 20px;">
        {% for interest in site.data.person.research_interests %}
        <li style="margin-bottom: 10px;"><strong>{{ interest.name }}:</strong><br><span style="color: #4b5563;">{{ interest.description }}</span></li>
        {% endfor %}
      </ul>
    </div>
  </div>

  <!-- Right Column -->
  <div>
    <h2 style="margin-top: 0;">Professional Experience</h2>
    <div class="card">
      {% for pos in site.data.person.positions %}
      <div style="margin-bottom: 20px;">
        <h3 style="font-size: 1.1em; margin-bottom: 5px;">{{ pos.title }}</h3>
        <div style="color: #446b59; font-weight: 600;">{{ pos.institution }}</div>
        <div style="color: #6b7280; font-size: 0.9em; margin-bottom: 5px;">
          {% if pos.current %}Since {{ pos.start_date }}{% else %}{{ pos.start_date }} – {{ pos.end_date }}{% endif %}
        </div>
        {% if pos.description %}
        <p style="font-size: 0.95em; color: #4b5563; margin-bottom: 0;">{{ pos.description }}</p>
        {% endif %}
      </div>
      {% if forloop.last == false %}
      <hr style="border-top: 1px solid #f3f4f6; margin: 15px 0;">
      {% endif %}
      {% endfor %}
    </div>

    <h2 style="margin-top: 20px;">Contact</h2>
    <div class="card">
      <ul style="list-style: none; padding-left: 0; margin-bottom: 0;">
        <li style="margin-bottom: 10px;">
          <strong>Address:</strong><br>
          {{ site.data.person.address.street }}<br>
          {{ site.data.person.address.postal_code }} {{ site.data.person.address.city }}, {{ site.data.person.address.country }}<br>
          {{ site.data.person.address.room }}
        </li>
        <li style="margin-bottom: 10px;">
          <strong>Email:</strong> <a href="mailto:{{ site.data.person.email }}">{{ site.data.person.email }}</a>
        </li>
        <li style="margin-bottom: 10px;">
          <strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/{{ site.data.person.credentials.linkedin }}">{{ site.data.person.full_name }}</a>
        </li>
        <li style="margin-bottom: 10px;">
          <strong>GitHub:</strong> <a href="https://github.com/{{ site.data.person.credentials.github }}">@{{ site.data.person.credentials.github }}</a>
        </li>
        <li style="margin-bottom: 10px;">
          <strong>ResearchGate:</strong> <a href="{{ site.data.person.credentials.researchgate }}">Nicolas Leins</a>
        </li>
        <li>
          <strong>ZIB Profile:</strong> <a href="{{ site.data.person.credentials.zib }}">Interactive Optimization and Learning</a>
        </li>
      </ul>
    </div>
  </div>

</div>
