---
title: "The Missing 62%"
tagline: "Member research at a scale no team could do by hand, verified by a zero-error audit"
client: "PICPA"
role: "Designed & built solo"
tags: [Applied AI, Data Enrichment]
depth: full
featured: true
order: 2
updated: "July 2026"
metrics:
  - value: "0"
    label: "wrong entries in the accuracy audit"
  - value: "≈16,000"
    label: "people to research"
  - value: "3–4"
    label: "person-years of manual work, estimated"
  - value: "~$200/mo"
    label: "flat AI subscription, no vendor contract"
related_posts: [the-missing-62]
description: >-
  A four-stage multi-agent AI pipeline (anchor, corroborate, weigh, verify)
  that enriched thousands of records, passed an accuracy audit with zero
  wrong entries, beat a commercial data tool head to head, and surfaced a
  seven-figure membership opportunity. Built solo on a flat monthly AI
  subscription.
---

## The challenge

A majority of Pennsylvania's licensed CPAs, roughly 16,000 people or about
62%, weren't PICPA members. The opportunity was obvious. The prospect list
wasn't much help: names and license numbers only, without the firm, role, or
seniority you'd need to reach anyone thoughtfully. Researching one person
properly takes 20 to 30 minutes across multiple sources, which works out to
an estimated three to four person-years of manual work. Commercial data
vendors tested poorly, and they raised the kind of compliance and brand
questions a professional association is obligated to ask.

## The approach

I built a four-stage multi-agent AI pipeline:

1. **Anchor** each person's identity, rejecting the look-alikes
2. **Corroborate** facts across five independent public sources
3. **Weigh** the evidence by source reliability
4. **Verify** every value against the page it was cited from

Two design choices mattered more than any model choice. The pipeline runs
locally, so sensitive member data never leaves the building. And it declines
rather than guesses: every field carries a source and a confidence level,
and when the evidence isn't there, the field stays empty.

{% include stat-callout.html value="7/10" title="Head-to-head, zero errors" text="In a bake-off against a commercial data tool, the pipeline scored 7 out of 10 with zero errors. The vendor managed 2–3 out of 10 and was confidently wrong." %}

## The results

Thousands of records enriched, and an accuracy audit that found zero wrong
entries. The output is a segmented, source-cited dataset behind a
seven-figure membership opportunity, built solo on a flat ~$200/month AI
subscription, without per-record metering or a data-vendor contract.

## What I learned

The speed matters less than the trust. A pipeline that guesses confidently
poisons its own results: the first wrong answer someone acts on discredits
every row that was right. Provenance, confidence levels, and the discipline
to leave a field blank are what make AI output something a team will build
a campaign on.
