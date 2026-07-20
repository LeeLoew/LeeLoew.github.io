# CLAUDE.md — leeloew.github.io

Lee Rogers' professional site: research strategist, human-centered AI in
professional services. Live at https://leeloew.github.io, deployed by GitHub
Pages' classic branch build of `master`.

## Hard constraints

- **GitHub Pages safe mode.** The site is built by the `github-pages` gem
  (Jekyll 3.10). Only [whitelisted plugins](https://pages.github.com/versions/)
  work — currently `jekyll-sitemap` and `jekyll-feed` are used. No custom
  Ruby plugins, and keep Liquid compatible with Jekyll 3.x.
- **URL stability.** Root pages deliberately keep their filenames; they
  publish as pretty URLs (`/aboutme/`, `/research/` — titled "Experience",
  `/portfolio/`, `/insights/`, `/work-with-me/`), and GitHub Pages 301s the
  old extensionless links. Don't rename these files. (The trailing-slash
  style comes from the `permalink:` setting in `_config.yml`.)
- The `github-pages` gem injects the default Primer theme; our local
  `_layouts/` override it entirely, but it emits a harmless unused
  `assets/css/style.css` in the build output. Ignore it.
- **`master` is production.** Every push to `master` deploys. Do feature work
  on a branch and let CI (`.github/workflows/ci.yml`) validate the build
  before merging.
- **Never read `private/_src/`.** It holds the *plaintext* of password-gated
  pages and is gitignored. Treat its contents as private user data. See
  "Private pages" below.

## Repo map

```
_config.yml          site metadata, nav links (`nav:` + `cta:`), plugins
_layouts/
  default.html       full HTML shell: head/SEO, header nav, footer, mobile-nav JS
  page.html          interior pages: page-hero (title/subtitle) + prose body
  post.html          insight essays: hero with date + prose + back link
_includes/
  structured-data.html  JSON-LD (WebSite + Person), home page only
assets/css/site.css  the entire design system (no frameworks)
assets/img/          monogram.svg (nav/footer mark), favicon.svg
index.html           home: hero, stats, service cards, 91% callout, CTA band
aboutme.md           about page
research.md          experience page (timeline, education, skills)
portfolio.md         selected work
insights.md          essay index — auto-lists _posts/, "coming soon" otherwise
work-with-me.md      services page
404.html             not-found page
private/             StatiCrypt password-gated area (see below)
robots.txt           blocks /private/, points at sitemap.xml
```

## Design system (assets/css/site.css)

- **Fonts:** Fraunces (display/headings) + Inter (text), loaded from Google
  Fonts in `_layouts/default.html`.
- **Tokens:** all colors/spacing live in `:root` custom properties at the top
  of `site.css`; dark theme overrides them in a `prefers-color-scheme: dark`
  block. Change tokens, not scattered values.
- **Brand:** ink `#15212B`, teal accent `#0E7C86`, gradient
  `--hero-grad` (ink → deep teal). The monogram/favicon SVGs use the same
  palette — keep them in sync if the brand shifts.
- **Reusable classes:** `.shell` (container), `.btn-primary/.btn-ghost`,
  `.card-grid`/`.card`, `.callout`, `.cta-band`, `.page-cta`,
  `.feature-item`, `.timeline`/`.timeline-item`, `.edu-grid`,
  `.skill-badges`, `.post-list`. Reuse these before inventing new patterns.

## Common tasks

**Add an insight essay** — create `_posts/YYYY-MM-DD-slug.md`:

```markdown
---
layout: post
title: "Essay title"
subtitle: Optional one-line dek
description: One-sentence summary for SEO/social.
---

Body in Markdown.
```

It publishes at `/insights/<slug>/` (set by `permalink:` in `_config.yml`),
appears automatically on `/insights`, and lands in the RSS feed (`/feed.xml`).

**Add a nav link** — edit `nav:` in `_config.yml` (order = display order).
`cta:` is the highlighted button.

**Add a social profile** — uncomment/set `author.linkedin` or `author.github`
in `_config.yml`; the footer link and JSON-LD `sameAs` pick them up.

**Change SEO/positioning copy** — `description:` in `_config.yml` (site-wide
+ Person JSON-LD) and per-page `description:` front matter.

## Private pages (`private/`)

Soft password protection via StatiCrypt — encrypted HTML is committed and
served at `/private/`; plaintext sources live in `private/_src/` and are
gitignored. To update: edit `private/_src/*.html`, run `private/encrypt.sh`
(prompts for the password), commit only the encrypted output. Full details in
`private/README.md`. Not real security — nothing confidential goes there.

## Build & preview

```bash
bundle install               # once; uses the github-pages gem
bundle exec jekyll serve     # preview at http://localhost:4000
bundle exec jekyll build --strict_front_matter   # what CI runs
```

The `.claude/hooks/session-start.sh` hook auto-installs deps in Claude Code
web sessions (no-op locally).
