---
layout: page
title: Blog
permalink: /blog/
description: Research updates, thoughts, and latest news from Nicolas Leins on AI, Robotics, and Human-Computer Interaction.
---

<div class="blog-index">
  <ul class="blog-list" role="list">
    {% for post in site.posts %}
    <li class="blog-list-item">
      <article class="blog-preview">
        <p class="blog-preview-meta">
          <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %-d, %Y" }}</time>
        </p>
        <h2 class="blog-preview-title">
          <a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>
        </h2>
        {% assign post_excerpt = post.excerpt | strip_html | strip %}
        {% if post_excerpt != '' %}
        <p class="blog-preview-excerpt">{{ post_excerpt | truncatewords: 45 | escape_once }}</p>
        {% endif %}
        <a class="blog-read-more" href="{{ post.url | relative_url }}" aria-label="Read article: {{ post.title | escape }}">Read article &rarr;</a>
      </article>
    </li>
    {% else %}
    <li>No posts yet.</li>
    {% endfor %}
  </ul>
</div>
