---
layout: page
title: Insights
subtitle: Writing on human-centered AI, adoption, and the value gap
description: >-
  Essays and original research by Lee Rogers on the human side of AI in
  professional services — adoption, trust, responsible AI, and why so many AI
  investments underdeliver.
---

I write about the human side of AI in professional services and finance — how
people actually adopt these tools, why so many AI investments underdeliver, and
what rigorous research says about closing the gap between adoption and real value.

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
> **Coming soon.** I'm building out a regular set of essays and original research
> here. In the meantime, the latest thinking goes out first to my network on
> LinkedIn.
{% endif %}

## Topics I cover

- **The AI value gap** — why most organizations can't tell whether their AI is working, and how to measure what actually matters.
- **Human-centered adoption** — trust, behavior change, and what makes AI stick (or fail) with real teams.
- **Responsible AI in practice** — governance and ethics translated from policy into everyday decisions.
- **Research that earns the room** — turning evidence into something executives can act on.

<div class="page-cta">
  <h2>Stay in the loop</h2>
  <p>A dedicated newsletter is on the way. Until then, the fastest way to follow along is on LinkedIn — or ask to be notified when it launches.</p>
  <!-- TODO: replace with a newsletter signup once Substack/Beehiiv is set up. -->
  <a class="btn btn-primary" href="mailto:{{ site.author.email }}?subject=Notify%20me%20about%20the%20newsletter">Get notified</a>
</div>
