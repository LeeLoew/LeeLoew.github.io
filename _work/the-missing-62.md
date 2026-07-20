---
title: "The Missing 62%"
tagline: "AI membership intelligence at scale — zero-wrong accuracy, built solo"
client: "PICPA"
role: "Designed & built solo"
tags: [Applied AI, Data Enrichment]
depth: full
featured: true
order: 2
metrics:
  - value: "0"
    label: "wrong entries in the accuracy audit"
  - value: "≈16,000"
    label: "people to research"
  - value: "3–4"
    label: "person-years of manual work, estimated"
  - value: "~$200/mo"
    label: "flat AI subscription — no vendor contract"
related_posts: [the-missing-62]
description: >-
  A four-stage multi-agent AI pipeline (anchor → corroborate → weigh → verify)
  that enriched thousands of records with a zero-wrong accuracy audit, beat a
  commercial data tool head-to-head, and surfaced a seven-figure membership
  opportunity — built solo on a flat monthly AI subscription.
---

## The challenge

A majority of Pennsylvania's licensed CPAs — roughly 16,000 people, the
missing 62% — weren't PICPA members. The opportunity was obvious; the
prospect list wasn't. It held names and license numbers only: no firm, no
role, no seniority, no way to reach anyone thoughtfully. Researching each
person properly takes 20–30 minutes across multiple sources — an estimated
**three to four person-years** of manual work. Commercial data vendors were
inaccurate when tested, and raised exactly the compliance and brand questions
a professional association should be asking.

## The approach

I built a four-stage multi-agent AI pipeline:

1. **Anchor** each person's identity — and reject the look-alikes
2. **Corroborate** facts across five *independent* public sources
3. **Weigh** the evidence by source reliability — not naive voting
4. **Verify** every value against the page it was cited from

Two design choices mattered more than any model choice. It runs **locally**,
so sensitive member data never leaves the building. And it's built to
**decline rather than guess**: every field carries a source and a confidence
level, and when the evidence isn't there, the field stays empty. No false
precision.

{% include stat-callout.html value="7/10" title="Head-to-head, zero errors" text="In a bake-off against a commercial data tool, the pipeline scored 7 out of 10 with zero errors; the vendor managed 2–3 out of 10 — and was confidently wrong." %}

## The results

Thousands of records enriched with a **zero-wrong accuracy audit**. The
output is a segmented, source-cited dataset behind a **seven-figure
membership opportunity** — built solo, on a flat ~$200/month AI subscription,
with no per-record metering, no data-vendor contract, and no added headcount.

## What I learned

The win isn't speed, though the speed is absurd. It's **accuracy you can
trust enough to act on**. A pipeline that guesses confidently is worse than no
pipeline — someone eventually acts on the wrong guess, and then nobody trusts
any of it. Provenance, confidence, and restraint are what turn AI output into
something a team will actually build a campaign on.
