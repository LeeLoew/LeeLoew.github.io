---
layout: page
title: Insights
subtitle: Writing on applied AI, adoption, and the human side of the rollout
description: >-
  Essays by Lee Rogers on applied AI — real use cases with measurable wins,
  the behavioral science of adoption, augmenting professional judgment, and
  responsible AI as an enabler.
---

I write about what it actually takes to get value from AI inside a real
organization — with the numbers, the behavioral science, and the unglamorous
80% that never makes it into the demos.

{% if site.posts.size > 0 %}
## Latest essays

<ul class="post-list">
  {% for post in site.posts %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <span class="post-date">{{ post.date | date: "%B %-d, %Y" }}</span>
  </li>
  {% endfor %}
</ul>
{% else %}
> **Coming soon.** Essays and original research are on the way.
{% endif %}

## What I cover

- **Real use cases & measurable wins** — concrete AI deployments and the efficiency they produced: before/after, time saved, quality gained, and what broke first.
- **The human side of adoption** — trust, automation bias, resistance, and habit change: what brain science says about why AI rollouts succeed or fail.
- **Augmenting professional judgment** — AI plus experts done right: where to trust the model, and where the human must stay in the loop.
- **Responsible by default** — governance as the thing that lets an organization say *yes* to AI, translated into plain, practical checks.

<div class="page-cta">
  <h2>Stay in the loop</h2>
  <p>New essays land here first. A dedicated newsletter is on the way — ask to be notified when it launches.</p>
  <a class="btn btn-primary" href="mailto:{{ site.author.email }}?subject=Notify%20me%20about%20the%20newsletter">Get notified</a>
</div>
