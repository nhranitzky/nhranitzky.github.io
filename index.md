---
title: Welcome
layout: home
---

<p class="intro">
  A small personal space where I collect my writing, notes, and experiments.
</p>

<div class="doc-list">
  {% assign docs = site.pages | where_exp: "p", "p.path contains '.md'" | sort: "date" | reverse %}
  {% for page in docs %}
    {% if page.path != 'index.md' and page.title %}
      <a class="doc-card" href="{{ page.url | relative_url }}">
        <h3 class="doc-title">{{ page.title }}</h3>
        {% if page.date %}
          <time class="doc-date">{{ page.date | date: "%B %-d, %Y" }}</time>
        {% endif %}
        {% if page.summary %}
          <p class="doc-summary">{{ page.summary }}</p>
        {% endif %}
        <span class="doc-arrow">Read &rarr;</span>
      </a>
    {% endif %}
  {% endfor %}
</div>