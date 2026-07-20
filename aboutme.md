---
layout: page
title: About me
kicker: About
subtitle: Behavioral scientist (PhD) · Applied-AI specialist · Philadelphia
description: >-
  About Lee Rogers, a behavioral scientist (PhD) and research strategist in
  Philadelphia who builds production AI systems and studies the human side
  of whether people adopt them.
---

{% assign portrait = site.static_files | where: "path", "/assets/img/portrait.jpg" | first %}
<figure class="about-portrait{% unless portrait %} is-placeholder{% endunless %}">
  {% if portrait %}
  <img src="{{ '/assets/img/portrait.jpg' | relative_url }}" alt="Lee Rogers" width="480" height="600">
  {% else %}
  <img src="{{ '/assets/img/monogram.svg' | relative_url }}" alt="" width="120" height="120">
  {% endif %}
</figure>

I'm Lee Rogers, a research strategist in Philadelphia. For fourteen years my
work has had the same shape in every setting: take a question an organization
cares about, design research that answers it honestly, and carry the answer
into the room where the decision gets made.

These days most of those questions involve AI. I lead strategic research in
the accounting profession, where I've moved AI out of the pilot phase and into
production for membership research, benchmarking, and the everyday work in
between. Research I author is licensed by state CPA organizations around the
country.

My PhD is in psychological and brain sciences, and it turned out to be the
useful half of applied AI. Whether a rollout succeeds has less to do with the
model than with trust, habit, and professional judgment: people over-rely on
tools that sound confident, abandon tools that embarrassed them once, and
quietly go back to the old way when the new one asks too much of them.
Designing around those tendencies is most of my job.

Two things shape how I work. I like proof more than theory, so everything I
publish or ship is anchored to a real outcome, including the parts that didn't
work on the first try. And I want this technology handled responsibly: systems
that cite their sources, admit uncertainty, and keep sensitive data where it
belongs. I'm currently pursuing the IAPP AI Governance Professional (AIGP)
credential to put formal structure under that instinct.

## Tools

<ul class="skill-badges">
  <li>Claude Code</li>
  <li>Python</li>
  <li>Qualtrics</li>
  <li>Alchemer</li>
  <li>Tableau</li>
  <li>Figma</li>
  <li>Microsoft 365 &amp; Copilot</li>
</ul>

## Now · July 2026

A running note on what has my attention, updated as it changes. The member
enrichment pipeline is in production and growing. I'm partway through the
IAPP AIGP coursework. And the AI-adoption webinar continues on the national
state-society circuit, which keeps me in front of the audiences this research
is for.

<div class="page-cta">
  <div>
    <h2>Working on something similar?</h2>
    <p>If your organization is somewhere in the middle of an AI rollout, I've probably seen a version of your situation before.</p>
  </div>
  <a class="btn btn-primary" href="{{ '/work-with-me' | relative_url }}">Work with me</a>
</div>
