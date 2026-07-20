---
layout: page
title: Case studies
subtitle: Production deployments with the numbers, and the design decisions behind them
kicker: Selected work
permalink: /work/
redirect_from:
  - /portfolio/
  - /portfolio.html
description: >-
  Case studies from Lee Rogers: AI-adoption research licensed by six state
  CPA organizations, a multi-agent enrichment pipeline with a zero-error
  audit, scenario forecasting, and profession-wide benchmarking.
---

{% assign studies = site.work | sort: "order" %}

## Full case studies

<ol class="case-list">
{% for s in studies %}{% if s.depth == "full" %}
  {% assign m = s.metrics | first %}
  <li class="case">
    <a href="{{ s.url | relative_url }}">
      <p class="where">{{ s.client }} · {{ s.tags | first }}</p>
      <h3>{{ s.title }}</h3>
      <p>{{ s.tagline }}</p>
      <span class="case-metric"><strong>{{ m.value }}</strong> {{ m.label }}</span>
    </a>
  </li>
{% endif %}{% endfor %}
</ol>

<h2 class="work-section-label">Method notes</h2>

Shorter write-ups of repeatable methods, shared at the level of approach
rather than client detail.

<ol class="case-list" style="counter-reset: case 2;">
{% for s in studies %}{% if s.depth == "brief" %}
  {% assign m = s.metrics | first %}
  <li class="case">
    <a href="{{ s.url | relative_url }}">
      <p class="where">{{ s.tags | first }}</p>
      <h3>{{ s.title }}</h3>
      <p>{{ s.tagline }}</p>
      <span class="case-metric"><strong>{{ m.value }}</strong> {{ m.label }}</span>
    </a>
  </li>
{% endif %}{% endfor %}
</ol>

## Earlier work

Usability research with 1,000+ participants across medical and consumer
devices (Bresslergroup); seven years of mixed-methods research at the
University of Delaware contributing to 20+ publications and 23+ conference
talks; AI upskilling workshops for faculty and graduate students at Drexel
University.

<div class="page-cta">
  <div>
    <h2>Want the full story on any of these?</h2>
    <p>Happy to walk through the methods on a call, including what I'd do differently now.</p>
  </div>
  <a class="btn btn-primary" href="mailto:{{ site.author.email }}">Contact me</a>
</div>
