---
layout: page
title: Writing
kicker: Essays
subtitle: On applied AI and the people who have to live with it
description: >-
  Essays by Lee Rogers on applied AI: what real deployments returned, why
  people trust or ignore new tools, and governance that helps organizations
  say yes.
---

I write about getting value from AI inside a real organization, with the
numbers attached. That means behavioral science, honest accounting of what
worked and what didn't, and the unglamorous 80% of the job that never makes
it into a demo.

{% if site.posts.size > 0 %}
## Latest essays

<ul class="post-list">
  {% for post in site.posts %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    {% if post.subtitle %}<p class="post-blurb">{{ post.subtitle }}</p>{% endif %}
    {% assign pw = post.content | strip_html | number_of_words %}
    <span class="post-date">{{ post.date | date: "%B %-d, %Y" }} · {% include reading-time.html words=pw %}</span>
  </li>
  {% endfor %}
</ul>
{% else %}
> **Coming soon.** Essays and original research are on the way.
{% endif %}

## What to expect

The topics repeat because the work repeats: concrete deployments and what
they returned, why skilled people trust or ignore new tools, where expert
judgment belongs in the loop, and governance that makes yes possible. When I
publish original research, it shows up here first.

<div class="page-cta">
  <div>
    <h2>Follow along</h2>
    <p>New essays land in the RSS feed the moment they publish. No newsletter yet; when there is one, it will be announced here.</p>
  </div>
  <a class="btn btn-primary" href="{{ '/feed.xml' | relative_url }}">Subscribe via RSS</a>
</div>
