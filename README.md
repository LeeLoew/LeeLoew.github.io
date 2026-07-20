# leeloew.github.io

Lee Rogers' professional site — research strategist focused on human-centered
AI in professional services. Live at <https://leeloew.github.io>.

A hand-built [Jekyll](https://jekyllrb.com) site (no theme gem, no CSS
framework). GitHub Pages builds and deploys it automatically from `master`.

## Editing

| What | Where |
|---|---|
| Page content | `index.html`, `aboutme.md`, `research.md`, `portfolio.md`, `insights.md`, `work-with-me.md` |
| New insight essay | Add `_posts/YYYY-MM-DD-slug.md` (publishes at `/insights/<slug>/`) |
| Design system | `assets/css/site.css` |
| Layout / nav / footer | `_layouts/`, nav links in `_config.yml` |
| Password-gated pages | `private/` — see `private/README.md` |

## Local preview

```bash
bundle install
bundle exec jekyll serve   # http://localhost:4000
```

## Deploying

Merge (or push) to `master` — GitHub Pages rebuilds the site automatically.
CI (`.github/workflows/ci.yml`) validates that the site builds on every push
and pull request.
