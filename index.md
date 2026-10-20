---
layout: page
title: Home
description: Portfolio and research of Nicolas Leins, Ph.D. student at Zuse Institute Berlin specializing in Human-Computer Interaction and Agentic AI.
---
<style>.post-header { display: none; }</style>

<div class="card card-flat hero">
  <div class="hero-text">
    <p class="hero-eyebrow">Researcher &middot; Zuse Institute Berlin</p>
    <h1 class="hero-title">Hi, I'm {{ site.data.person.first_name }}.</h1>
    <p class="hero-lead">
      {{ site.data.person.bio_short }}
    </p>
    <p class="hero-subtext">
      My Ph.D. supervisor is <a href="{{ site.data.person.phd_supervisor.url }}">Prof. Dr. Sebastian Pokutta</a>, co-supervised by <a href="{{ site.data.person.co_supervisor.url }}">Dr. Jana Gonnermann-Müller</a>.
    </p>
    <p class="hero-subtext">
      {{ site.data.person.goal }}
    </p>
    <div class="hero-actions">
      <a href="{{ '/bio/' | relative_url }}" class="btn">About Me &rarr;</a>
      <a href="{{ '/publications/' | relative_url }}" class="btn btn-secondary">View Publications &rarr;</a>
    </div>
  </div>
  <div class="hero-media">
     <img src="{{ site.data.person.profile_image | relative_url }}" alt="{{ site.data.person.full_name }}">
  </div>
</div>

<section class="home-updates" aria-labelledby="latest-updates-title">
  <h2 id="latest-updates-title">Latest Updates</h2>

  {% include featured_publication.html %}

  <div class="home-updates-more">
    <a href="{{ '/publications/' | relative_url }}">View all publications &rarr;</a>
  </div>
</section>
