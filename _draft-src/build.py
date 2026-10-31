#!/usr/bin/env python3
"""Build the unlisted portfolio draft into ../draft/.

Run:  python3 build.py
Every page carries noindex/nofollow; the site-wide robots.txt also blocks crawlers.
Content lives in this file so the whole draft can be regenerated after edits.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "draft"
EMAIL = "Leeland.Rogers@gmail.com"

CSS = r"""
@font-face{font-family:"Fraunces";src:url("fonts/fraunces-latin.woff2") format("woff2");font-weight:100 900;font-style:normal;font-display:swap}
@font-face{font-family:"Fraunces";src:url("fonts/fraunces-italic-latin.woff2") format("woff2");font-weight:100 900;font-style:italic;font-display:swap}
:root{
  --bg:#f5f5f2; --paper:#fbfbf9; --ink:#191b1e; --muted:#5f646a; --rule:#d8dad5; --accent:#2a5a4e; --accent-ink:#1f4339;
  --display:"Fraunces",Georgia,"Times New Roman",serif;
  --body:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
  --mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--body);font-size:17px;line-height:1.6;
  padding-left:max(20px,env(safe-area-inset-left,0px));padding-right:max(20px,env(safe-area-inset-right,0px))}
a{color:var(--accent-ink);text-decoration:none;border-bottom:1px solid rgba(42,90,78,.35)}
a:hover,a:focus-visible{border-bottom-color:currentColor;outline:none}
.frame{max-width:1120px;margin:0 auto;display:grid;grid-template-columns:1fr;gap:40px;padding-block:36px 72px}
@media(min-width:900px){.frame{grid-template-columns:272px minmax(0,1fr);gap:80px;padding-block:72px 96px}}
/* rail */
.rail{display:flex;flex-direction:column;gap:18px;min-width:0}
@media(min-width:900px){.rail{position:sticky;top:48px;align-self:start}}
.rail img{width:132px;height:132px;object-fit:cover;object-position:top;border-radius:50%;display:block;max-width:100%}
.rail .name{font-family:var(--display);font-size:30px;font-weight:500;line-height:1.1;margin:0;letter-spacing:-.01em}
.rail .name span{font-weight:400;color:var(--muted);font-size:.6em;margin-left:.25em;letter-spacing:0}
.rail .role{margin:0;color:var(--muted);font-size:15px;line-height:1.45;max-width:28ch}
.rail nav{display:flex;flex-wrap:wrap;gap:4px 18px;font-size:15px;margin-top:4px}
@media(min-width:900px){.rail nav{flex-direction:column;gap:6px;border-top:1px solid var(--rule);padding-top:16px}}
.rail nav a{border:0;color:var(--ink)}
.rail nav a[aria-current]{color:var(--accent-ink)}
.rail nav a:hover{color:var(--accent-ink)}
.rail .foot{font-size:13px;color:var(--muted);margin:0}
@media(min-width:900px){.rail .foot{margin-top:12px}}
/* main */
main{min-width:0;max-width:640px}
section{margin:0 0 64px}
section:last-child{margin-bottom:0}
.eyebrow{font-size:12.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin:0 0 16px;font-weight:600}
h1{font-family:var(--display);font-weight:500;font-size:clamp(30px,4.6vw,40px);line-height:1.15;letter-spacing:-.012em;margin:0 0 18px;text-wrap:balance}
h2{font-family:var(--display);font-weight:500;font-size:28px;line-height:1.2;letter-spacing:-.01em;margin:0 0 18px;text-wrap:balance}
h3{font-family:var(--display);font-weight:500;font-size:22px;line-height:1.25;margin:0 0 6px}
p{margin:0 0 1em}
p.lede{font-size:20px;line-height:1.5}
.when{font-family:var(--mono);font-size:12.5px;color:var(--muted);letter-spacing:.02em}
/* entry lists */
.entries{list-style:none;margin:0;padding:0;display:flex;flex-direction:column}
.entries li{padding:22px 0;border-top:1px solid var(--rule)}
.entries li:last-child{border-bottom:1px solid var(--rule)}
.entries h3 a{border:0;color:var(--ink)}
.entries h3 a:hover{color:var(--accent-ink)}
.entries p{margin:0;color:var(--ink)}
.entries p+p{margin-top:6px}
.entries .meta{color:var(--muted);font-size:14.5px}
.entries .more{display:inline-block;margin-top:8px;font-size:15px}
/* background */
.creds{list-style:none;margin:0 0 18px;padding:0;display:grid;gap:4px}
.creds li{display:grid;grid-template-columns:minmax(0,1fr);gap:0}
.creds b{font-weight:600}
.creds span{color:var(--muted)}
details{border-top:1px solid var(--rule);border-bottom:1px solid var(--rule);padding:12px 0;margin:18px 0 0}
summary{cursor:pointer;font-weight:600;font-size:15px}
summary::-webkit-details-marker{color:var(--muted)}
details ol{margin:12px 0 4px;padding-left:22px;font-size:15px;color:var(--ink)}
details li{margin-bottom:8px}
details em{font-style:italic}
/* contact */
.contact p{font-size:19px}
.contact .email{font-family:var(--mono);font-size:16px}
/* article pages */
article header{margin-bottom:36px;padding-bottom:24px;border-bottom:1px solid var(--rule)}
article header p{color:var(--muted);margin:0}
article h2{font-size:24px;margin-top:40px}
article ul,article ol{padding-left:22px}
article li{margin-bottom:8px}
.facts{list-style:none;padding:0;margin:0 0 8px;display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:16px 24px}
.facts li{display:flex;flex-direction:column;gap:2px}
.facts b{font-family:var(--display);font-weight:500;font-size:28px;line-height:1.1;font-variant-numeric:tabular-nums}
.facts span{font-size:14px;color:var(--muted);line-height:1.35}
.callout{border-left:3px solid var(--accent);padding:4px 0 4px 18px;margin:28px 0;color:var(--ink)}
.callout b{font-family:var(--display);font-weight:500;font-size:26px;display:block;line-height:1.1;margin-bottom:4px}
.callout p{margin:0;font-size:16px}
.back{font-size:14.5px;color:var(--muted);border:0}
@media(prefers-reduced-motion:no-preference){a{transition:color .15s,border-color .15s}}
"""

def shell(title, body, depth, current):
    pre = "../" * depth
    nav = []
    for label, href, key in [("Papers", "index.html#papers", "home"), ("Research", "index.html#research", "home"),
                             ("Background", "index.html#background", "home"), ("Writing", "index.html#writing", "home"),
                             ("Contact", "index.html#contact", "home")]:
        cur = ' aria-current="page"' if key == current else ""
        nav.append(f'<a href="{pre}{href}"{cur}>{label}</a>')
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow, noarchive">
<title>{title}</title>
<link rel="stylesheet" href="{pre}assets/site.css">
<link rel="icon" href="data:,">
</head>
<body>
<div class="frame">
  <aside class="rail">
    <img src="{pre}assets/portrait.jpg" alt="Lee Rogers" width="132" height="132">
    <p class="name">Lee Rogers<span>PhD</span></p>
    <p class="role">Director of Strategic Research and Insights, PICPA and CPA Crossings. Philadelphia.</p>
    <nav aria-label="Site">{''.join(nav)}</nav>
    <p class="foot"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
  </aside>
  <main>
{body}
  </main>
</div>
</body>
</html>
"""

# ---------------------------------------------------------------- home
HOME = f"""
<section id="top">
  <p class="lede">I run the research operation at the Pennsylvania Institute of CPAs and its national research arm, CPA Crossings. The papers I write there go out under the names of state CPA societies across the country.</p>
  <p>Before this I spent a decade in cognitive science, studying how people learn, attend, and decide. That turned out to be the right preparation for the question most organizations are now working through: what happens when skilled people are handed AI, and what it takes for them to keep using it.</p>
</section>

<section id="papers">
  <p class="eyebrow">Papers</p>
  <ol class="entries">
    <li>
      <h3><a href="work/start-from-trust.html">Start from Trust</a></h3>
      <p class="meta">Insights series · 2026</p>
      <p>Technology adoption for small and mid-size CPA firms, built around a framework that maps people by how much they use AI and how much they trust it. Six state CPA organizations license it under their own brands, and a companion CPE webinar runs on the national circuit.</p>
    </li>
    <li>
      <h3><a href="work/college-to-career.html">College to Career</a></h3>
      <p class="meta">Insights series · 2026</p>
      <p>What the first year at a firm asks of new accountants, and what firms and professors can do before day one. Built from roundtables with firm leaders and the published research; every recommended practice carries an evidence grade. The second package in the series.</p>
    </li>
  </ol>
</section>

<section id="research">
  <p class="eyebrow">The research operation</p>
  <p>PICPA is the second-oldest state CPA society in the country, with about 20,000 members. I took its research function from one publication line to the evidence base behind membership, workforce, advocacy, and revenue decisions. Some of the pieces:</p>
  <ul class="entries">
    <li>
      <h3><a href="work/census.html">The Pennsylvania CPA Census</a></h3>
      <p>A full-population portrait of the state's profession from the public licensing roster, reported in aggregate with small-cell suppression. The first whole-population evidence base the organization has had.</p>
    </li>
    <li>
      <h3><a href="work/forecast.html">Membership to 2035</a></h3>
      <p>A cohort-replacement forecast, backtested to under 1% error, with a scenario simulator leadership uses to test recruitment, retention, and pricing levers.</p>
    </li>
    <li>
      <h3><a href="work/the-missing-62.html">The Missing 62%</a></h3>
      <p>Roughly 16,000 licensed CPAs in the state were not members. A four-stage AI pipeline researched them from public sources, passed an accuracy audit with zero wrong entries, and surfaced a seven-figure opportunity. Built alone, on a flat $200-a-month subscription.</p>
    </li>
    <li>
      <h3>Peer-society intelligence</h3>
      <p>A verified base covering 17 state CPA societies: offerings, dues mechanics, financials. Built with paired gather-and-verify agents and adversarial checking, so every claim traces to a source.</p>
    </li>
    <li>
      <h3>The member survey</h3>
      <p>The organization's largest member survey to date, analyzed end to end: the outcome of a board-level KPI, the strongest driver of perceived value, and a weighting caveat on the reported NPS.</p>
    </li>
  </ul>
</section>

<section id="background">
  <p class="eyebrow">Background</p>
  <ul class="creds">
    <li><b>PhD, Psychological and Brain Sciences</b><span>University of Delaware</span></li>
    <li><b>MS, Experimental Psychology</b><span>Villanova University</span></li>
    <li><b>BA, Psychology</b><span>Temple University</span></li>
  </ul>
  <p>Before PICPA: teaching and research at Drexel University. User research on medical devices at Bresslergroup. Seven years of lab research at Delaware on visual statistical learning, reward, and attention.</p>
  <p>Six peer-reviewed publications and 21 conference talks and posters. In progress: an MBA, and the IAPP AI Governance Professional credential.</p>
  <details>
    <summary>Publications</summary>
    <ol>
      <li>Park, Rogers, Vickery (2021). Reward impacts visual statistical learning. <em>Cognitive, Affective, and Behavioral Neuroscience</em>.</li>
      <li>Rogers, Park, Vickery (2021). Visual statistical learning is modulated by arbitrary and natural categories. <em>Psychonomic Bulletin and Review</em>.</li>
      <li>Park, Rogers, Vickery (2018). The roles of order, distance, and interstitial items in temporal visual statistical learning. <em>Attention, Perception, and Psychophysics</em>, 80(6).</li>
      <li>Kan, Garrison, Drummey, Emmert, Rogers (2017). The roles of chronological age and time perspective in memory positivity. <em>Aging, Neuropsychology, and Cognition</em>, 25(4).</li>
      <li>Rogers, Friedman, Vickery (2016). No apparent influence of reward upon visual statistical learning. <em>Frontiers in Psychology</em>, 7.</li>
      <li>Anderson, Folk, Garrison, Rogers (2016). Mechanisms of habitual approach. <em>Journal of Experimental Psychology: General</em>, 145(6).</li>
    </ol>
  </details>
</section>

<section id="writing">
  <p class="eyebrow">Writing</p>
  <ul class="entries">
    <li>
      <h3><a href="writing/adoption.html">Most AI projects don't fail on the technology. They fail on adoption.</a></h3>
      <p class="meta">What a behavioral scientist sees in stalled AI rollouts</p>
    </li>
    <li>
      <h3><a href="writing/the-missing-62.html">The Missing 62%: researching 16,000 people on a $200 subscription</a></h3>
      <p class="meta">The build story, and the design rule that mattered more than the model</p>
    </li>
  </ul>
</section>

<section id="contact" class="contact">
  <p class="eyebrow">Contact</p>
  <p>Talks and advisory, by email.</p>
  <p class="email"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
</section>
"""

# ---------------------------------------------------------------- case studies
def article(eyebrow, title, sub, facts, body):
    f = "".join(f"<li><b>{v}</b><span>{l}</span></li>" for v, l in facts)
    return f"""
<article>
  <header>
    <p class="eyebrow">{eyebrow}</p>
    <h1>{title}</h1>
    <p>{sub}</p>
  </header>
  <ul class="facts">{f}</ul>
{body}
  <p style="margin-top:48px"><a class="back" href="../index.html">&larr; Lee Rogers</a></p>
</article>
"""

SFT = article("Insights series · 2026", "Start from Trust",
  "A research package that meets a skeptical profession where it stands. PICPA and CPA Crossings. Author and lead researcher.",
  [("6", "state CPA organizations license the research"), ("4", "starting points in the AI Trust and Usage Quadrant"), ("1 hr", "companion CPE webinar on the national circuit")],
  """
<h2>The challenge</h2>
<p>Small and mid-size accounting firms were hearing the same advice from every direction: adopt AI faster. The advice ignored the defining trait of the profession, a deliberate and well-placed skepticism. Firms needed a way to adopt technology on their own terms, without dismissing AI and without over-trusting it.</p>
<h2>The approach</h2>
<p>I built the package around a reframe: treat professional caution as an asset and design adoption around it. The anchor is a primary research paper, supported by tools a firm can put to work the same week: a vendor-evaluation checklist, a where-do-I-start guide, a discussion guide for firm leaders, and a quick-start list of actions.</p>
<p>At the center is the AI Trust and Usage Quadrant, which maps people on two axes: how much they use AI, and how much they trust it. Each quadrant is a different starting point, and each needs a different first move.</p>
<div class="callout"><b>Licensed nationally</b><p>Six state CPA organizations have licensed and rebranded the package for their own members.</p></div>
<h2>The results</h2>
<p>The package shipped as a published report with supporting tools, blog content, infographics, and video. Six state CPA organizations license and rebrand it for their members, and a companion one-hour CPE webinar built from the research runs on the national state-society circuit.</p>
<h2>What I learned</h2>
<p>The reframe did the heavy lifting. Research that treats skepticism as professional judgment gets a hearing that another adopt-faster report never would. Firms listened because the work respected how they already make decisions.</p>
""")

CTC = article("Insights series · 2026", "College to Career",
  "Stronger starts, sharper professionals. PICPA and CPA Crossings. Author and lead researcher.",
  [("30", "sourced references"), ("Graded", "evidence behind every recommended practice"), ("4", "audiences: students, new hires, firms, professors")],
  """
<h2>The challenge</h2>
<p>Almost every career resource for accounting students stops at the offer letter. Explore the career, win the scholarship, pass the exam, land the internship, and then silence. School teaches the accounting; nobody teaches the rest. Firms, meanwhile, were describing the same first-year gaps to each other and not to the students.</p>
<h2>The approach</h2>
<p>I built the package from direct conversations with the people who lead and hire at CPA firms, then grounded each claim in the published research. The paper names the practices that hold up, grades the evidence behind each one, and names the famous statistics nobody should be citing. It travels with a set of pages written for each audience: the real recruiting calendar for students, a 12-behavior scorecard for the first 90 days, a six-move onboarding plan for firms that run without a training department, and a classroom session for professors.</p>
<div class="callout"><b>Four doors, one body of evidence</b><p>Students, new hires, firm leaders, and professors each get a page that hands them something usable the same day, all drawn from the same graded research.</p></div>
<h2>Where it stands</h2>
<p>The second package in the Insights series, delivered to state CPA societies for their own branding, with a partner webinar and a classroom offer alongside.</p>
""")

M62 = article("Applied AI · PICPA", "The Missing 62%",
  "Member research at a scale no team could do by hand, verified by a zero-error audit. Designed and built solo.",
  [("0", "wrong entries in the accuracy audit"), ("≈16,000", "people to research"), ("3–4", "person-years of manual work, estimated"), ("~$200/mo", "flat AI subscription, no vendor contract")],
  """
<h2>The challenge</h2>
<p>A majority of Pennsylvania's licensed CPAs, roughly 16,000 people or about 62%, weren't PICPA members. The opportunity was obvious. The prospect list wasn't much help: names and license numbers only, without the firm, role, or seniority you'd need to reach anyone thoughtfully. Researching one person properly takes 20 to 30 minutes across multiple sources, which works out to an estimated three to four person-years of manual work. Commercial data vendors tested poorly, and they raised the kind of compliance and brand questions a professional association is obligated to ask.</p>
<h2>The approach</h2>
<p>I built a four-stage multi-agent AI pipeline:</p>
<ol>
  <li><b>Anchor</b> each person's identity, rejecting the look-alikes</li>
  <li><b>Corroborate</b> facts across five independent public sources</li>
  <li><b>Weigh</b> the evidence by source reliability</li>
  <li><b>Verify</b> every value against the page it was cited from</li>
</ol>
<p>Two design choices mattered more than any model choice. The pipeline runs locally, so sensitive member data never leaves the building. And it declines rather than guesses: every field carries a source and a confidence level, and when the evidence isn't there, the field stays empty.</p>
<div class="callout"><b>7/10, zero errors</b><p>In a bake-off against a commercial data tool, the pipeline scored 7 out of 10 with zero errors. The vendor managed 2 to 3 out of 10 and was confidently wrong.</p></div>
<h2>The results</h2>
<p>Thousands of records enriched, and an accuracy audit that found zero wrong entries. The output is a segmented, source-cited dataset behind a seven-figure membership opportunity, built solo on a flat ~$200/month AI subscription, without per-record metering or a data-vendor contract.</p>
<h2>What I learned</h2>
<p>The speed matters less than the trust. A pipeline that guesses confidently poisons its own results: the first wrong answer someone acts on discredits every row that was right. Provenance, confidence levels, and the discipline to leave a field blank are what make AI output something a team will build a campaign on.</p>
""")

CENSUS = article("Benchmarking · PICPA", "The Pennsylvania CPA Census",
  "A full-population portrait of a state's accounting profession. Designer and analyst.",
  [("Full population", "every licensee in the state, member or not"), ("Aggregate only", "reporting with small-cell suppression")],
  """
<h2>The context</h2>
<p>Membership organizations usually see only their member file, a partial and self-selected view of the market they serve. The question that matters is the whole profession: everyone licensed in the state, member or not.</p>
<h2>The method</h2>
<p>A full-population portrait built from public licensure data and governed by a strict privacy-containment model: a hard wall between public and internal data, aggregate-only reporting, and small-cell suppression so no individual is ever exposed. The result is a view of an entire state profession, its generations, its geography, and its membership penetration, built from data anyone could legally access and handled more carefully than required.</p>
<h2>What it demonstrates</h2>
<p>The method repeats in any state with an accessible licensure roster, which makes it a template for membership organizations that want to see their whole market rather than the slice that already joined. Privacy containment is built into the method itself, so the rigor doesn't depend on anyone's good intentions.</p>
""")

FORECAST = article("Forecasting · PICPA", "Membership to 2035",
  "A membership forecast built overnight by autonomous AI agents, then made to prove itself. Architect.",
  [("<1%", "backtest error on the full sample"), ("Overnight", "autonomous multi-agent build, quality-gated")],
  """
<h2>The context</h2>
<p>Membership organizations plan against demographic change they can feel but rarely quantify. Leadership needed a forecast rigorous enough to build strategy on, plus levers they could test themselves rather than a static chart.</p>
<h2>The method</h2>
<p>A cohort-replacement forecast designed, built, and quality-gated by an autonomous overnight multi-agent AI run. Two candidate models were built and judged in an independent bake-off; the winner backtested to under 1% error on the full sample and was validated against a blind holdout. The deliverables include an interactive scenario simulator that lets leadership test recruitment, retention, and pricing levers directly.</p>
<h2>What it demonstrates</h2>
<p>Quantitative strategy work run by AI can be held to the same standards as work run by a research team: competing models, backtests, and independent judging before anything reached a decision-maker. The overnight-run pattern, a defined contract with gated quality checks, generalizes to any analysis too large for a single working session.</p>
""")

# ---------------------------------------------------------------- essays
def essay(title, sub, body):
    return f"""
<article>
  <header>
    <p class="eyebrow">Writing</p>
    <h1>{title}</h1>
    <p>{sub}</p>
  </header>
{body}
  <p style="margin-top:48px"><a class="back" href="../index.html">&larr; Lee Rogers</a></p>
</article>
"""

ADOPTION = essay("Most AI projects don't fail on the technology. They fail on adoption.",
  "What a behavioral scientist sees in stalled AI rollouts", """
<p>Walk into any organization that "adopted AI last year" and ask a simple question: who is using it, daily, for real work?</p>
<p>The honest answer is usually a small fraction of the people who were supposed to. The licenses are paid for. The kickoff went fine. The technology works. And adoption quietly stalled anyway.</p>
<p>That is a human failure, not a technology failure, and it is predictable.</p>
<h2>Three ways rollouts stall</h2>
<h3>Trust is miscalibrated</h3>
<p>People don't need to trust AI more; they need to trust it accurately. Some ignore the tool entirely because one early error convinced them it can't be relied on. Others accept everything it produces without checking, right up until it's confidently wrong about something that matters. Both patterns are well documented in the research on automation bias, and both are expensive: one wastes the tool, the other creates risk.</p>
<h3>The habit never forms</h3>
<p>Using AI means interrupting a workflow someone has run, comfortably, for years. That switch has a cost every single time, and if the payoff isn't immediate and obvious, the old way wins. A mandate can't fix that. The design has to, by meeting people inside the work they already do instead of in a separate window they have to remember to open.</p>
<h3>Judgment feels threatened</h3>
<p>Skilled professionals hear "AI will make you more efficient" as "AI will make you less necessary." Unless the rollout is explicit about where human judgment stays in the loop, resistance is rational. People are defending the part of the job that makes them valuable.</p>
<h2>Caution is not the enemy</h2>
<p>In my research with accounting firms, a profession famous for its skepticism, the most useful reframe was to treat professional caution as a strength to build on rather than a lag to overcome. The firms that adopt AI well aren't the fastest. They're the ones that moved deliberately, matching their usage to their trust and closing the gap in both directions.</p>
<p>That's the thinking behind the AI Trust and Usage Quadrant, a framework from my published adoption research. Map where people sit on two axes, how much they use AI and how much they trust it, and you get four very different starting points. The over-trusting experimenter needs guardrails. The capable skeptic needs a low-stakes win. Treat them identically and the rollout produces risk and resentment at the same time.</p>
<h2>What works</h2>
<p>Nothing here requires a bigger model. It requires designing for the humans:</p>
<ul>
  <li>Start where trust already exists. Find the workflow where people already double-check everything, and give them AI that shows its sources, so verifying its work feels natural rather than burdensome.</li>
  <li>Make the first win personal. Adoption spreads through "look what this just did for me," and almost never through training decks.</li>
  <li>Be explicit about the division of labor. Write down what the AI drafts and what the human decides; ambiguity breeds both over-reliance and refusal.</li>
  <li>Measure usage, not access. Weekly real-work usage, trust calibration, and time to first value say more than the number of licenses provisioned.</li>
</ul>
<p>The organizations getting real value from AI treat adoption as what it is: a behavior-change problem, with decades of science behind it, sitting right where most rollouts never look.</p>
""")

M62_ESSAY = essay("The Missing 62%: researching 16,000 people on a $200 subscription",
  "The build story, and the design rule that mattered more than the model", """
<p>I needed to research 16,000 people.</p>
<p>Done properly, one person takes 20 to 30 minutes: confirm the identity, find the firm, figure out the role, check that you haven't mixed them up with someone who shares the name. Multiply that across the list and it comes to an estimated three to four person-years of full-time work. I didn't have a team. I had a flat AI subscription that costs about $200 a month.</p>
<p>Here's how the list got that big. At PICPA, the Pennsylvania Institute of CPAs, a majority of the state's licensed CPAs, about 62%, weren't members. Leadership wanted to change that thoughtfully, but the prospect list held names and license numbers and nothing else. You can't write a thoughtful letter to a license number.</p>
<p>The obvious answer was a commercial data vendor. We tested that first, and the test settled it: scored head to head, the vendor managed 2 to 3 out of 10, and it delivered its wrong answers with total confidence. For a professional association, confident wrong answers are a compliance problem and a brand problem at the same time.</p>
<p>So I built the researcher I needed out of AI agents. The pipeline treats each person as a small research project: it pins down identity before anything else, gathers facts from five independent public sources, weighs the evidence by how reliable each source has proven, and then checks every value against the page it was cited from. In the same head-to-head test, it scored 7 out of 10 with zero errors.</p>
<p>Two rules shaped the design more than any technical decision. Member data stays local, on machines we control. And when the evidence is thin, a field stays blank; a blank cell is honest, and a plausible guess is a small landmine for whoever acts on it.</p>
<p>The result: thousands of records enriched, an audit that found zero wrong entries, and a segmented, source-cited dataset behind a seven-figure membership opportunity. The monthly bill never changed.</p>
<h2>The lesson</h2>
<p>Accuracy is the product. The first time a colleague acts on a wrong answer, they stop trusting the whole dataset, and no amount of speed buys that trust back. What made this one hold up is that it's checkable: every value carries its source, so nobody has to take the machine's word for anything.</p>
""")

PAGES = {
    "index.html": ("Lee Rogers", HOME, 0, "home"),
    "work/start-from-trust.html": ("Start from Trust · Lee Rogers", SFT, 1, "work"),
    "work/college-to-career.html": ("College to Career · Lee Rogers", CTC, 1, "work"),
    "work/the-missing-62.html": ("The Missing 62% · Lee Rogers", M62, 1, "work"),
    "work/census.html": ("The Pennsylvania CPA Census · Lee Rogers", CENSUS, 1, "work"),
    "work/forecast.html": ("Membership to 2035 · Lee Rogers", FORECAST, 1, "work"),
    "writing/adoption.html": ("AI fails on adoption · Lee Rogers", ADOPTION, 1, "writing"),
    "writing/the-missing-62.html": ("The Missing 62% · Lee Rogers", M62_ESSAY, 1, "writing"),
}

if __name__ == "__main__":
    (ROOT / "assets").mkdir(parents=True, exist_ok=True)
    (ROOT / "assets" / "site.css").write_text(CSS.strip() + "\n")
    for rel, (title, body, depth, cur) in PAGES.items():
        out = ROOT / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(shell(title, body, depth, cur))
        print("wrote", out.relative_to(ROOT.parent))
