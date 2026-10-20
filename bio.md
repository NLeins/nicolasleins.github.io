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
      <ol class="bio-records" role="list">
        {% for edu in site.data.person.education %}
        {% assign education_status = edu.status | downcase %}
        <li class="bio-record">
          <div class="bio-record-meta">
            <span class="bio-record-date">{% if education_status == 'currently' and edu.start_year %}Since {{ edu.start_year | escape }}{% else %}{{ edu.status | escape }}{% endif %}</span>
            {% if education_status == 'currently' %}
            <span class="bio-record-current">Current</span>
            {% endif %}
          </div>
          <h3 class="bio-record-title">{{ edu.degree | escape }}</h3>
          <div class="bio-record-institution">{{ edu.institution | escape }}</div>
          {% if edu.degree contains "Ph.D." %}
          <p class="bio-record-description">
            Ph.D. supervisor: <a href="{{ site.data.person.phd_supervisor.url | escape }}">{{ site.data.person.phd_supervisor.name | escape }}</a><br>
            Co-supervisor: <a href="{{ site.data.person.co_supervisor.url | escape }}">{{ site.data.person.co_supervisor.name | escape }}</a>
          </p>
          {% endif %}
        </li>
        {% endfor %}
      </ol>
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
      <ol class="bio-records" role="list">
        {% for pos in site.data.person.positions %}
        <li class="bio-record">
          <div class="bio-record-meta">
            <span class="bio-record-date">{% if pos.current %}Since {{ pos.start_date | escape }}{% else %}{{ pos.start_date | escape }} – {{ pos.end_date | escape }}{% endif %}</span>
            {% if pos.current %}
            <span class="bio-record-current">Current</span>
            {% endif %}
          </div>
          <h3 class="bio-record-title">{{ pos.title | escape }}</h3>
          <div class="bio-record-institution">{{ pos.institution | escape }}</div>
          {% if pos.description %}
          <p class="bio-record-description">{{ pos.description | escape }}</p>
          {% endif %}
        </li>
        {% endfor %}
      </ol>
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
