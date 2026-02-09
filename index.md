---
layout: page
title: Home
description: Portfolio and research of Nicolas Leins, PhD student at Zuse Institute Berlin specializing in Human-Computer Interaction and Agentic AI.
---
<style>.post-header { display: none; }</style>

<div class="card" style="display: flex; align-items: center; gap: 40px; border: none; background: transparent; box-shadow: none;">
  <div style="flex: 1;">
    <h1 style="margin-top: 0; font-weight: 800; color: #111827;">Hi, I'm {{ site.data.person.first_name }}.</h1>
    <p style="font-size: 1.25em; line-height: 1.6; color: #4b5563;">
      {{ site.data.person.bio_short }}
    </p>
    <p style="color: #4b5563;">
      {{ site.data.person.goal }}
    </p>
    <br>
    <a href="{{ '/bio/' | relative_url }}" class="btn">About Me &rarr;</a>
    <a href="{{ '/publications/' | relative_url }}" class="btn" style="margin-left: 10px; background-color: white; color: #446b59 !important; border: 1px solid #446b59;">View Publications &rarr;</a>
  </div>
  <div style="flex: 0 0 250px;">
     <img src="{{ site.data.person.profile_image | relative_url }}" alt="{{ site.data.person.full_name }}" style="border-radius: 50%; width: 250px; height: 250px; object-fit: cover; box-shadow: 0 10px 25px rgba(0,0,0,0.1); border: 4px solid white;">
  </div>
</div>

<h2 style="margin-top: 40px; margin-bottom: 20px;">Latest Updates</h2>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
  {% for post in site.posts limit:3 %}
  <div class="card">
    <span style="color: #6b7280; font-size: 0.85em; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;">{{ post.date | date: "%B %d, %Y" }}</span>
    <h3 style="margin-top: 10px; margin-bottom: 10px;">
      <a href="{{ post.url | relative_url }}" style="text-decoration: none; color: #111827;">{{ post.title }}</a>
    </h3>
    <p style="color: #4b5563;">{{ post.excerpt | strip_html | truncatewords: 20 }}</p>
    <a href="{{ post.url | relative_url }}" style="font-weight: 600; font-size: 0.9em;">Read more &rarr;</a>
  </div>
  {% endfor %}
</div>

<div style="margin-top: 20px; text-align: center;">
  <a href="{{ '/blog/' | relative_url }}" style="font-weight: 600;">View all posts &rarr;</a>
</div>