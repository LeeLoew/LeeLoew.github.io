#!/usr/bin/env python3
"""Build the site into the repository root.

Run:  python3 _src/build.py
Writes the three pages, the stylesheet, robots.txt, sitemap.xml, the 404 page,
and redirect stubs for the old /draft/ addresses. Content lives in this file so
the whole site can be regenerated after edits.
"""
from pathlib import Path
from urllib.parse import quote
import json

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "leelandrogers.com"
SITE = "https://" + DOMAIN
EMAIL = "Leeland.Rogers@gmail.com"

CSS = r"""
@font-face{font-family:"Fraunces";src:url("fonts/fraunces-latin.woff2") format("woff2");font-weight:100 900;font-style:normal;font-display:swap}
@font-face{font-family:"Fraunces";src:url("fonts/fraunces-italic-latin.woff2") format("woff2");font-weight:100 900;font-style:italic;font-display:swap}
@font-face{font-family:"Instrument Sans";src:url("fonts/instrument-sans-latin-wght-normal.woff2") format("woff2");font-weight:400 700;font-style:normal;font-display:swap}
@font-face{font-family:"Instrument Sans";src:url("fonts/instrument-sans-latin-wght-italic.woff2") format("woff2");font-weight:400 700;font-style:italic;font-display:swap}
:root{
  --bg:#f4f2ec; --ink:#15181a; --muted:#5c6166; --rule:#dbd8cf;
  --accent:#1f4a40; --accent-ink:#1a3d35; --brass:#a9823f; --brass-lt:#d3b47c;
  --hero-a:#255649; --hero-b:#15362f;
  --display:"Fraunces",Georgia,"Times New Roman",serif;
  --body:"Instrument Sans",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
  --ease:cubic-bezier(.2,.7,.2,1);
  --pad-l:max(22px,env(safe-area-inset-left,0px)); --pad-r:max(22px,env(safe-area-inset-right,0px));
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--body);font-size:17px;line-height:1.6;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;min-height:100vh;min-height:100dvh;display:flex;flex-direction:column}
main{flex:1}
::selection{background:var(--accent);color:#fff}
a{color:var(--accent-ink);text-decoration:none}
:focus-visible{outline:2px solid var(--brass);outline-offset:4px;border-radius:2px}
.wrap{max-width:1120px;margin:0 auto;padding-left:var(--pad-l);padding-right:var(--pad-r)}

/* top bar */
.top{position:sticky;top:0;z-index:10;background:rgba(244,242,236,.82);-webkit-backdrop-filter:saturate(1.4) blur(14px);backdrop-filter:saturate(1.4) blur(14px);border-bottom:1px solid var(--rule)}
.top .wrap{display:flex;align-items:center;justify-content:space-between;gap:16px 28px;padding-block:18px}
.brand{font-family:var(--display);font-weight:500;font-size:21px;letter-spacing:-.015em;color:var(--ink);white-space:nowrap}
.brand span{font-weight:400;color:var(--muted);font-size:.7em;margin-left:.35em;letter-spacing:0}
.top nav{display:flex;gap:28px;font-size:15.5px;font-weight:500}
.top nav a{position:relative;color:inherit;padding:6px 0}
.top nav a::after{content:"";position:absolute;left:0;right:0;bottom:0;height:1px;background:currentColor;transform:scaleX(0);transform-origin:right}
.top nav a:hover::after,.top nav a[aria-current]::after{transform:scaleX(1);transform-origin:left}
.home .top{position:absolute;left:0;right:0;background:none;-webkit-backdrop-filter:none;backdrop-filter:none;border-color:transparent;color:rgba(255,255,255,.92)}
.home .top .brand{visibility:hidden}

/* hero (home) */
.hero{position:relative;isolation:isolate;color:#eef3f0;background:linear-gradient(155deg,var(--hero-a),var(--hero-b) 72%)}
.hero::before{content:"";position:absolute;inset:0;z-index:-1;background:radial-gradient(110% 85% at 8% 0%,rgba(255,255,255,.13),transparent 62%)}
.hero::after{content:"";position:absolute;inset:0;z-index:-1;opacity:.5;mix-blend-mode:soft-light;pointer-events:none;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 .55 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
.hero .wrap{display:grid;gap:40px;padding-block:112px 0}
.hero .text{min-width:0}
.kicker{display:flex;align-items:center;gap:14px;margin:0 0 22px;font-size:12.5px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:rgba(255,255,255,.72)}
.kicker::before{content:"";flex:none;width:40px;height:1px;background:var(--brass-lt);transform-origin:left}
.hero .name{font-family:var(--display);font-weight:400;font-size:clamp(52px,8.2vw,104px);line-height:1;letter-spacing:-.035em;margin:0 0 22px;color:#fff}
.hero .name .mask{display:block;overflow:hidden;padding-bottom:.14em;margin-bottom:-.14em}
.hero .name .in{display:block}
.hero .name small{font-size:.26em;font-weight:400;letter-spacing:.02em;margin-left:.5em;color:rgba(255,255,255,.66);vertical-align:.95em}
.hero .role{margin:0;font-size:clamp(17px,1.55vw,20px);line-height:1.45;color:rgba(255,255,255,.92)}
.hero .role span{display:block;color:rgba(255,255,255,.66)}
.portrait{position:relative;margin:0 0 -44px;width:min(68%,280px);aspect-ratio:4/5;overflow:hidden;box-shadow:0 36px 60px -34px rgba(8,22,18,.7)}
.portrait::after{content:"";position:absolute;inset:0;border:1px solid rgba(255,255,255,.16);pointer-events:none}
.portrait img{width:100%;height:100%;object-fit:cover;object-position:center 18%;display:block}
@media(min-width:820px){
  .hero .wrap{grid-template-columns:minmax(0,1fr) 320px;gap:64px;align-items:end;padding-block:148px 0}
  .hero .text{padding-bottom:72px}
  .portrait{width:100%;margin-bottom:-72px;justify-self:end}
}

/* main */
main{padding-block:64px 96px}
.home main{padding-block:104px 96px}
@media(min-width:820px){.home main{padding-block:128px 112px}}
h1,h2,h3,p{margin:0}
.page-head{margin-bottom:56px}
.page-head h1{font-family:var(--display);font-weight:400;font-size:clamp(44px,6.4vw,76px);line-height:1;letter-spacing:-.03em}
.page-head .mask{display:block;overflow:hidden;padding-bottom:.16em;margin-bottom:-.16em}
.page-head .in{display:block}

/* label + content bands */
.band{position:relative;display:grid;gap:16px;padding-block:30px 44px}
.band::before{content:"";position:absolute;left:0;right:0;top:0;height:1px;background:var(--rule);transform-origin:left}
.band:last-child{padding-bottom:0}
.label{font-family:var(--body);font-size:12.5px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);line-height:1.5}
.band .body{min-width:0;max-width:700px}
.band .body>p{margin-top:18px}
@media(min-width:820px){
  .band{grid-template-columns:232px minmax(0,1fr);gap:56px;padding-block:34px 60px}
  .label{position:sticky;top:92px;align-self:start;padding-top:5px}
}

/* home statements */
.scope{list-style:none;margin:0;padding:0}
.scope li{position:relative;padding:20px 0;font-family:var(--display);font-weight:400;font-size:clamp(21px,2.35vw,28px);line-height:1.26;letter-spacing:-.014em;text-wrap:balance}
.scope li:first-child{padding-top:0}
.scope li+li::before{content:"";position:absolute;left:0;right:0;top:0;height:1px;background:var(--rule);transform-origin:left}
.scope li:last-child{padding-bottom:0}

/* background */
.roles{list-style:none;margin:0;padding:0;display:grid;gap:22px}
.roles b{display:block;font-family:var(--display);font-weight:500;font-size:21px;line-height:1.25;letter-spacing:-.012em}
.roles span{display:block;margin-top:3px;color:var(--muted);font-size:15.5px;font-variant-numeric:tabular-nums}
.points{list-style:none;margin:11px 0 0;padding:0;display:grid;gap:7px}
.points li{position:relative;padding-left:22px;font-size:16px;line-height:1.5}
.points li::before{content:"";position:absolute;left:0;top:.74em;width:10px;height:1px;background:var(--brass)}
.pubs{list-style:none;counter-reset:pub;margin:0;padding:0;font-size:15.5px;line-height:1.55}
.pubs li{counter-increment:pub;position:relative;padding:0 0 14px 38px}
.pubs li:last-child{padding-bottom:0}
.pubs li::before{content:counter(pub,decimal-leading-zero);position:absolute;left:0;top:.28em;font-size:11.5px;font-weight:600;letter-spacing:.08em;color:var(--brass);font-variant-numeric:tabular-nums}

/* contact */
.mail{display:inline-block;font-family:var(--display);font-weight:400;font-size:clamp(25px,4.6vw,52px);line-height:1.15;letter-spacing:-.025em;color:var(--ink);overflow-wrap:anywhere;padding-bottom:.12em;background:linear-gradient(var(--accent),var(--accent)) 0 100%/100% 1px no-repeat,linear-gradient(var(--rule),var(--rule)) 0 100%/100% 1px no-repeat}
.mail:hover{color:var(--accent-ink)}

footer{border-top:1px solid var(--rule)}
footer .wrap{padding-block:22px;font-size:14px;color:var(--muted);display:flex;flex-wrap:wrap;justify-content:space-between;gap:8px 24px}
footer a{color:var(--muted)}
footer a:hover{color:var(--accent-ink)}

/* page-to-page crossfade */
@view-transition{navigation:auto}

/* motion: everything below is skipped for reduced-motion, and content is visible without it */
@media(prefers-reduced-motion:no-preference){
  a{transition:color .2s}
  .top nav a::after{transition:transform .4s var(--ease)}
  .mail{background-size:0 1px,100% 1px;transition:background-size .5s var(--ease),color .2s}
  .mail:hover,.mail:focus-visible{background-size:100% 1px,100% 1px}
  ::view-transition-old(root){animation-duration:.2s}
  ::view-transition-new(root){animation-duration:.36s}

  @keyframes rise{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}
  @keyframes fade{from{opacity:0}to{opacity:1}}
  @keyframes mask-up{from{transform:translateY(108%)}to{transform:none}}
  @keyframes draw{from{transform:scaleX(0)}to{transform:scaleX(1)}}
  @keyframes unveil{from{clip-path:inset(100% 0 0 0)}to{clip-path:inset(0 0 0 0)}}
  @keyframes settle{from{transform:scale(1.09)}to{transform:none}}

  .home .top nav{animation:fade .8s ease .55s both}
  .kicker{animation:fade .7s ease .05s both}
  .kicker::before{animation:draw .8s var(--ease) .1s both}
  .hero .name .in{animation:mask-up 1s var(--ease) .12s both}
  .hero .role{animation:rise .8s var(--ease) .42s both}
  .portrait{animation:unveil 1.15s var(--ease) .22s both}
  .portrait img{animation:settle 1.7s var(--ease) .22s both}

  .page-head .in{animation:mask-up .9s var(--ease) .05s both}
  main .band::before{animation:draw 1s var(--ease) both}
  main .band>*{animation:rise .8s var(--ease) both}
  .inner main .band:nth-of-type(1)::before,.inner main .band:nth-of-type(1)>*{animation-delay:.22s}
  .inner main .band:nth-of-type(2)::before,.inner main .band:nth-of-type(2)>*{animation-delay:.32s}
  .home main .band:nth-of-type(1)::before,.home main .band:nth-of-type(1)>.label{animation-delay:.6s}
  .home main .band:nth-of-type(2)::before,.home main .band:nth-of-type(2)>.label{animation-delay:1.02s}
  .home main .band>.body{animation:none}
  .scope li{animation:rise .8s var(--ease) both}
  .scope li+li::before{animation:draw .9s var(--ease) both}
  .home .band:nth-of-type(1) .scope li:nth-child(1){animation-delay:.68s}
  .home .band:nth-of-type(1) .scope li:nth-child(2),.home .band:nth-of-type(1) .scope li:nth-child(2)::before{animation-delay:.78s}
  .home .band:nth-of-type(1) .scope li:nth-child(3),.home .band:nth-of-type(1) .scope li:nth-child(3)::before{animation-delay:.88s}
  .home .band:nth-of-type(2) .scope li{animation-delay:1.08s}

  /* further down the page, reveal on scroll where the browser can do it in CSS alone */
  @supports (animation-timeline:view()){
    .inner main .band:nth-of-type(n+3)::before,.inner main .band:nth-of-type(n+3)>*{animation-timeline:view();animation-range:entry 0% entry 42%;animation-duration:auto;animation-timing-function:linear;animation-delay:0s}
  }
}
@media print{*,*::before,*::after{animation:none!important}.top,footer{display:none}}
"""

NAV = [("Background", "background.html"), ("Contact", "contact.html")]

ICON = quote("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' rx='13' fill='#1f4a40'/><text x='32' y='43' font-family='Georgia,serif' font-size='29' fill='#fff' text-anchor='middle'>LR</text></svg>")

def shell(title, body, depth, current, hero=False, desc=""):
    pre = "../" * depth
    parts = []
    for label, href in NAV:
        cur = ' aria-current="page"' if href == current else ""
        parts.append(f'<a href="{pre}{href}"{cur}>{label}</a>')
    nav = "".join(parts)
    hero_html = f"""
<header class="hero">
  <div class="wrap">
    <div class="text">
      <p class="kicker">Philadelphia</p>
      <h1 class="name"><span class="mask"><span class="in">Lee Rogers<small>PhD</small></span></span></h1>
      <p class="role">Director of Strategic Research and Insights<span>PICPA and CPA Crossings</span></p>
    </div>
    <figure class="portrait"><img src="{pre}assets/portrait.jpg" alt="Lee Rogers" width="870" height="1000"></figure>
  </div>
</header>""" if hero else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="{'#255649' if hero else '#f4f2ec'}">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{'' if current == 'index.html' else current}">
<meta property="og:type" content="{'profile' if hero else 'website'}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}/{'' if current == 'index.html' else current}">
<meta property="og:image" content="{SITE}/assets/portrait.jpg">
<meta name="twitter:card" content="summary">
{PERSON if hero else ''}<link rel="preload" href="{pre}assets/fonts/fraunces-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{pre}assets/fonts/instrument-sans-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{pre}assets/site.css">
<link rel="icon" href="data:image/svg+xml,{ICON}">
</head>
<body class="{'home' if hero else 'inner'}">
<div class="top"><div class="wrap">
  <a class="brand" href="/">Lee Rogers<span>PhD</span></a>
  <nav aria-label="Site">{nav}</nav>
</div></div>{hero_html}
<main><div class="wrap">
{body}
</div></main>
<footer><div class="wrap"><span>Lee Rogers, Philadelphia</span><a href="mailto:{EMAIL}">{EMAIL}</a></div></footer>
</body>
</html>
"""

PERSON = '<script type="application/ld+json">' + json.dumps({
    "@context": "https://schema.org", "@type": "Person",
    "name": "Lee Rogers", "honorificSuffix": "PhD",
    "jobTitle": "Director of Strategic Research and Insights",
    "worksFor": [{"@type": "Organization", "name": "PICPA"}, {"@type": "Organization", "name": "CPA Crossings"}],
    "address": {"@type": "PostalAddress", "addressLocality": "Philadelphia", "addressRegion": "PA"},
    "url": SITE + "/", "image": SITE + "/assets/portrait.jpg",
}) + "</script>"

def page(title, intro, body):
    return f"""
<div class="page-head">
  <h1><span class="mask"><span class="in">{title}</span></span></h1>
</div>
{body}
"""

# ---------------------------------------------------------------- home
HOME = """
<section class="band">
  <h2 class="label">At PICPA and CPA Crossings</h2>
  <div class="body">
    <ul class="scope">
      <li>Strategy advisor to the chief executives of PICPA and CPA Crossings</li>
      <li>The evidence behind Board of Directors decisions on membership, growth, and strategy</li>
      <li>AI strategy and governance for PICPA and CPA Crossings</li>
    </ul>
  </div>
</section>

<section class="band">
  <h2 class="label">Service</h2>
  <div class="body">
    <ul class="scope">
      <li>External member, Institutional Review Board, Holy Family University</li>
    </ul>
  </div>
</section>
"""

BACKGROUND = page("Background", "", """
<section class="band">
  <h2 class="label">Experience</h2>
  <div class="body">
    <ul class="roles">
      <li><b>Director of Strategic Research and Insights</b><span>PICPA and CPA Crossings, April 2026 to present</span>
        <ul class="points">
          <li>Strategy advisor to the chief executives of PICPA and CPA Crossings</li>
          <li>The evidence behind Board of Directors decisions on membership, growth, and strategy</li>
          <li>AI strategy and governance for PICPA and CPA Crossings</li>
        </ul>
      </li>
      <li><b>Acting Director of Research (Research Specialist)</b><span>PICPA and CPA Crossings, July 2025 to April 2026</span></li>
      <li><b>Professor</b><span>Drexel University</span></li>
      <li><b>Market and user research consulting</b>
        <ul class="points">
          <li>Market and user research for global product makers, from foldable smartphones to medical devices</li>
          <li>Made the case at the HFES Health Care Symposium for changing FDA policy on device testing, toward better science that saves lives</li>
        </ul>
      </li>
      <li><b>Cognitive neuroscience laboratory</b>
        <ul class="points">
          <li>Led the lab's operations and its research team</li>
          <li>Responsible for running a multi-million-dollar MRI scanner safely with human participants</li>
          <li>Authored peer-reviewed scientific publications on the cognitive neuroscience of how people learn and decide</li>
        </ul>
      </li>
    </ul>
  </div>
</section>

<section class="band">
  <h2 class="label">Service</h2>
  <div class="body">
    <ul class="roles">
      <li><b>Institutional Review Board, External Member</b><span>Holy Family University, October 2025 to present</span>
        <ul class="points">
          <li>Independent oversight of research involving people, on the board with authority to approve or stop it</li>
          <li>Holds the outside seat that federal regulations require, answerable to the public and not the institution</li>
          <li>Votes on participant risk, consent, privacy, and data protection</li>
        </ul>
      </li>
    </ul>
  </div>
</section>

<section class="band">
  <h2 class="label">Education</h2>
  <div class="body">
    <ul class="roles">
      <li><b>PhD, Psychological and Brain Sciences</b><span>University of Delaware</span></li>
      <li><b>MS, Experimental Psychology</b><span>Villanova University</span></li>
      <li><b>BA, Psychology</b><span>Temple University</span></li>
    </ul>
  </div>
</section>
""")

CONTACT = page("Contact", "", f"""
<section class="band">
  <h2 class="label">Email</h2>
  <div class="body"><a class="mail" href="mailto:{EMAIL}">{EMAIL}</a></div>
</section>
""")

PAGES = {
    "index.html": ("Lee Rogers, PhD", HOME, 0, "index.html", True,
                   "Lee Rogers, PhD. Director of Strategic Research and Insights at PICPA and CPA Crossings in Philadelphia."),
    "background.html": ("Background · Lee Rogers, PhD", BACKGROUND, 0, "background.html", False,
                        "Experience, service and education of Lee Rogers, PhD."),
    "contact.html": ("Contact · Lee Rogers, PhD", CONTACT, 0, "contact.html", False,
                     "Contact Lee Rogers, PhD."),
}

def redirect(target):
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="robots" content="noindex">
<link rel="canonical" href="{SITE}/{target}">
<meta http-equiv="refresh" content="0; url=/{target}">
<title>Lee Rogers, PhD</title></head>
<body><p><a href="/{target}">This page has moved.</a></p></body></html>
"""

NOT_FOUND = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>Page not found · Lee Rogers, PhD</title>
<link rel="stylesheet" href="/assets/site.css">
</head>
<body class="inner">
<div class="top"><div class="wrap">
  <a class="brand" href="/">Lee Rogers<span>PhD</span></a>
  <nav aria-label="Site"><a href="/background.html">Background</a><a href="/contact.html">Contact</a></nav>
</div></div>
<main><div class="wrap">
<div class="page-head"><h1><span class="mask"><span class="in">Page not found</span></span></h1></div>
<section class="band"><h2 class="label">404</h2><div class="body"><a class="mail" href="/">Go to the home page</a></div></section>
</div></main>
</body>
</html>
"""

if __name__ == "__main__":
    (ROOT / "assets").mkdir(parents=True, exist_ok=True)
    (ROOT / "assets" / "site.css").write_text(CSS.strip() + "\n")
    for rel, (title, body, depth, cur, hero, desc) in PAGES.items():
        (ROOT / rel).write_text(shell(title, body, depth, cur, hero, desc))
        print("wrote", rel)
    (ROOT / "404.html").write_text(NOT_FOUND)
    (ROOT / "CNAME").write_text(DOMAIN + "\n")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    urls = "".join(f"  <url><loc>{SITE}/{'' if r == 'index.html' else r}</loc></url>\n" for r in PAGES)
    (ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    (ROOT / "draft").mkdir(exist_ok=True)
    for old, target in [("index.html", ""), ("background.html", "background.html"), ("contact.html", "contact.html")]:
        (ROOT / "draft" / old).write_text(redirect(target))
    print("wrote 404.html, robots.txt, sitemap.xml, draft/ redirects")
