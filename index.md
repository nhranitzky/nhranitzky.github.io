---
title: Welcome
layout: default
---

<p class="intro">
  A small personal space where I collect my writing, notes, and experiments.
</p>

<div class="doc-list">
  {% assign docs = site.pages | where_exp: "p", "p.path contains '.md'" | sort: "date" | reverse %}
  {% for page in docs %}
    {% if page.path != 'index.md' and page.title %}
      <a class="doc-card" href="{{ page.url | relative_url }}">
        <h3>{{ page.title }}</h3>
        {% if page.date %}
          <time>{{ page.date | date: "%B %-d, %Y" }}</time>
        {% endif %}
        {% if page.summary %}
          <p>{{ page.summary }}</p>
        {% endif %}
      </a>
    {% endif %}
  {% endfor %}
</div>