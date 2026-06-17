---
title: Welcome
layout: home
---

<p class="intro">
  A small personal space where I collect my writing, notes, and experiments.
  <a href="{{ '/feed.xml' | relative_url }}"><img src="{{ '/media/rss.svg' | relative_url }}" alt="RSS" style="height: 1em; width: auto; vertical-align: -0.1em;"></a>
</p>

<div class="doc-list">
  {% assign docs = site.data.toc | sort: "date" | reverse %}
  {% for doc in docs %}
    <a class="doc-card" href="{{ doc.url | relative_url }}">
      <h3 class="doc-title">{{ doc.title }}</h3>
      {% if doc.date %}
        <time class="doc-date">{{ doc.date | date: "%B %-d, %Y" }}</time>
      {% endif %}
      {% if doc.summary %}
        <p class="doc-summary">{{ doc.summary }}</p>
      {% endif %}
      <span class="doc-arrow">Read &rarr;</span>
    </a>
  {% endfor %}
</div>