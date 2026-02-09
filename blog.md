---
layout: page
title: Blog
permalink: /blog/
description: Research updates, thoughts, and latest news from Nicolas Leins on AI, Robotics, and Human-Computer Interaction.
---

<ul>
  {% for post in site.posts %}
    <li>
      <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>
      <h3>
        <a class="post-link" href="{{ post.url | relative_url }}">
          {{ post.title | escape }}
        </a>
      </h3>
      {%- if site.show_excerpts -%}
        {{ post.excerpt }}
      {%- endif -%}
    </li>
  {% endfor %}
</ul>
