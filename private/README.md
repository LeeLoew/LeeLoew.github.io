# Private (password-gated) pages

This folder holds **soft password-protected** pages, served at `/private/` on
the live site. They use [StatiCrypt](https://github.com/robinmoisson/staticrypt):
each page is AES-256 **encrypted** and only decrypted in the visitor's browser
after they type the correct password.

## ⚠️ What this is (and isn't)

- ✅ Fine for **low-sensitivity, "just-not-public" convenience** sharing.
- ❌ **Not** real security. It's one shared password, the encrypted blob is
  public, and a weak password can be brute-forced offline. Don't put anything
  confidential, proprietary, or under NDA here. For that, use real access
  control (e.g. Cloudflare Access) or keep it off the public site entirely.

## How it works

```
private/
  index.html             # ENCRYPTED page that gets published  (commit this)
  .staticrypt.json       # the salt — not secret               (commit this)
  encrypt.sh             # helper script
  _src/
    index.html.template  # starter template (no secrets)       (committed)
    index.html           # YOUR plaintext content — LOCAL ONLY, gitignored
```

The plaintext in `_src/*.html` is **gitignored** so it never reaches the public
GitHub repo. Only the encrypted output (`private/*.html`) is committed.

## Editing / adding a private page

1. Create your working copy from the template (first time only):
   ```bash
   cp _src/index.html.template _src/index.html
   ```
2. Edit `_src/index.html` with the content you want to share.
   (Add more pages as `_src/anything.html` — each becomes `/private/anything`.)
3. Encrypt:
   ```bash
   ./encrypt.sh        # prompts for the password
   ```
4. Commit & push the encrypted output:
   ```bash
   git add private/*.html private/.staticrypt.json
   git commit -m "Update private page"
   git push
   ```
5. Share the link + password, e.g. `https://<your-username>.github.io/private/`.

## Changing the password

Just re-run `./encrypt.sh` with the new password and push. Anyone with the old
password keeps no access once the new encrypted file is live.

## The demo page

The `index.html` currently committed is a demo encrypted with the password
**`changeme`**. Replace it with your own content + password before sharing.
