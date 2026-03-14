---
phase: 02-aib-scammer-article
plan: 01
status: complete
started: 2026-03-14
completed: 2026-03-14
---

# Plan 02-01: AIB Scammer Article + Landing Page Wiring

## What Was Built

1. **aib-scammer/index.html** — Full narrative article in four acts (The Scam, Understanding the Target, Building the Ammunition, The Counter-Attack). Written for non-technical readers. All technical terms explained inline. No code blocks. ~700 words.

2. **index.html** — Updated the "Fighting a Phishing Site" card from placeholder (href="#", "Coming soon") to live link (href="aib-scammer/", "Article" tag).

## Key Files

- `aib-scammer/index.html` — The article
- `index.html` — Updated landing page

## Verification

Both automated checks passed:
- Article: ../style.css, back-link, href="../", title, User-Agent, aib.ie1.online, 4000, PAC, registration
- Landing page: aib-scammer/ href present, title present, 3 remaining "Coming soon" cards unchanged

## Deviations

None.

## Self-Check: PASSED
