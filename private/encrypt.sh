#!/usr/bin/env bash
#
# Encrypt the plaintext pages in _src/ into password-gated pages served
# from /private/ on the live site, using StatiCrypt (AES-256, in-browser).
#
# Prereqs: Node.js installed (https://nodejs.org). No global install needed --
#          npx fetches StatiCrypt on demand.
#
# Usage:   ./encrypt.sh        (you'll be prompted for the password)
#
# Notes:
#   * Plaintext sources in _src/*.html are gitignored and must stay local.
#   * Only the encrypted .html output and .staticrypt.json (the salt -- not
#     secret) get committed and published.
#   * .staticrypt.json keeps the salt stable so re-encrypting is consistent.
#
set -euo pipefail
cd "$(dirname "$0")"

shopt -s nullglob
sources=(_src/*.html)
if [ ${#sources[@]} -eq 0 ]; then
  echo "No plaintext pages found in _src/."
  echo "Copy the starter first:  cp _src/index.html.template _src/index.html"
  echo "then edit _src/index.html and re-run ./encrypt.sh"
  exit 1
fi

# -d .       write encrypted output into this private/ directory
# --short    suppress the short-password warning
# (password omitted -> StatiCrypt prompts, so it never hits shell history)
npx --yes staticrypt "${sources[@]}" -d . --short

echo
echo "Done. Encrypted page(s) written to private/."
echo "Commit & push the .html file(s), then share the URL + password:"
echo "  https://<your-username>.github.io/private/"
