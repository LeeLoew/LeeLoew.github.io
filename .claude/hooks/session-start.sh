#!/bin/bash
# SessionStart hook: install Ruby/Jekyll dependencies so Claude Code on the web
# can build the site and run checks. Mirrors .github/workflows/ci.yml.
set -euo pipefail

# Only needed in the remote (web) environment; skip locally.
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "$CLAUDE_PROJECT_DIR"

# Install the base bundle, then the appraisal-specific gemfiles (jekyll 3 & 4),
# matching what CI does. `bundle install` is used (not `bundle ci`) so the
# cached container state can be reused across sessions.
bundle install

# Appraisal's executable isn't exposed through bundler's binstub path, so
# resolve it explicitly before running `appraisal install`.
appraisal_bin="$(bundle exec ruby -e 'print Gem.bin_path("appraisal", "appraisal")')"
bundle exec ruby "$appraisal_bin" install

echo "Dependencies installed. Build with: bundle exec jekyll build"
