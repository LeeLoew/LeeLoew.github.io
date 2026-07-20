#!/bin/bash
# SessionStart hook: install Ruby/Jekyll dependencies so Claude Code on the web
# can build the site and run checks. Mirrors .github/workflows/ci.yml.
set -euo pipefail

# Only needed in the remote (web) environment; skip locally.
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "$CLAUDE_PROJECT_DIR"

bundle install

echo "Dependencies installed. Build with: bundle exec jekyll build"
