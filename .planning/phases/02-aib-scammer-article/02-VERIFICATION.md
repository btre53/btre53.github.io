---
phase: 02-aib-scammer-article
verified: 2026-03-14T00:00:00Z
status: passed
score: 6/6 must-haves verified
re_verification: false
---

# Phase 2: AIB Scammer Article — Verification Report

**Phase Goal:** A recruiter can read the full AIB Scammer story as a web article
**Verified:** 2026-03-14
**Status:** passed
**Re-verification:** No — initial verification

## Goal Achievement

### Observable Truths

| #  | Truth                                                                                             | Status     | Evidence                                                                                        |
|----|---------------------------------------------------------------------------------------------------|------------|-------------------------------------------------------------------------------------------------|
| 1  | A non-technical recruiter can read the full AIB scammer story without prior technical knowledge   | VERIFIED   | 47-line prose article, no code blocks, all technical terms explained inline in parentheses      |
| 2  | Article explains how the phishing site worked (mobile-only, User-Agent detection, credential harvesting) | VERIFIED   | aib-scammer/index.html lines 18–22: desktop 404, mobile fake login, registration + PAC harvest |
| 3  | Article explains the counter-attack (fake Irish IPs, spoofed User-Agents, 4,000 fake credentials, poisoning goal) | VERIFIED   | Lines 34–42: nirsoft.net IP ranges, 72/28 Android/iOS split, 4,000 POST requests, 200:1 noise ratio |
| 4  | Article renders with same styling as the Irish elections piece                                    | VERIFIED   | `<link rel="stylesheet" href="../style.css">` — no inline styles; style.css confirms Georgia, #fafaf8, #1b3a2d |
| 5  | A back link returns the reader to the portfolio landing page                                      | VERIFIED   | `<a class="back-link" href="../">Back to portfolio</a>` at line 10                             |
| 6  | Landing page card links to aib-scammer/ and shows "Article" tag                                  | VERIFIED   | index.html: `href="aib-scammer/"` and `<span class="tag">Article</span>` at lines 46–48       |

**Score:** 6/6 truths verified

### Required Artifacts

| Artifact                  | Expected                  | Status     | Details                                                                                 |
|---------------------------|---------------------------|------------|-----------------------------------------------------------------------------------------|
| `aib-scammer/index.html`  | Full narrative article    | VERIFIED   | Exists, 47 lines, four-act structure (The Scam / Understanding the Target / Building the Ammunition / The Counter-Attack), substantive prose |
| `index.html`              | Updated landing page card | VERIFIED   | href updated from `#` to `aib-scammer/`, tag changed from "Coming soon" to "Article"; three other "Coming soon" cards untouched |

### Key Link Verification

| From                    | To                       | Via              | Status  | Details                                                              |
|-------------------------|--------------------------|------------------|---------|----------------------------------------------------------------------|
| `index.html` card       | `aib-scammer/index.html` | `href` attribute | WIRED   | `href="aib-scammer/"` present at index.html line 46                 |
| `aib-scammer/index.html` | `index.html`            | `.back-link` anchor | WIRED | `<a class="back-link" href="../">` present at article line 10      |

### Requirements Coverage

| Requirement | Source Plan  | Description                                                                                    | Status    | Evidence                                                                                   |
|-------------|--------------|------------------------------------------------------------------------------------------------|-----------|--------------------------------------------------------------------------------------------|
| SCAM-01     | 02-01-PLAN.md | Article explains how the phishing site worked (mobile-only, user agent detection, credential harvesting) | SATISFIED | aib-scammer/index.html "The Scam" section: User-Agent detection, desktop 404, mobile fake login, 8-digit reg + 5-digit PAC harvested |
| SCAM-02     | 02-01-PLAN.md | Article explains the counter-attack (spoofed user agents, fake Irish IPs, 4,000 fake credentials to poison the dataset) | SATISFIED | "The Counter-Attack" section: 4,000 POST requests, spoofed Irish IPs (nirsoft.net ranges), real mobile UA mix, 200 fake entries per real victim |

### Anti-Patterns Found

None detected. No TODO/FIXME/placeholder comments, no empty implementations, no stub returns, no console.log-only handlers.

### Human Verification Required

#### 1. Visual rendering in browser

**Test:** Open `aib-scammer/index.html` in a desktop browser and a mobile viewport (375px width).
**Expected:** Georgia serif body text, cream (#fafaf8) background, dark green (#1b3a2d) headers, max-width 720px centred, readable line length, no horizontal scroll at 375px.
**Why human:** CSS rendering cannot be verified programmatically — style.css is correctly linked but actual visual output requires a browser.

#### 2. Card navigation from landing page

**Test:** Open `index.html`, click the "Fighting a Phishing Site" card.
**Expected:** Browser navigates to the article page without a full reload error (i.e., the `aib-scammer/` directory and its `index.html` are served correctly by whatever local server or file:// the reviewer uses).
**Why human:** Relative path resolution (`aib-scammer/`) depends on the serving context; cannot confirm directory structure serves correctly without running it.

## Gaps Summary

No gaps. All six must-haves pass all three verification levels (exists, substantive, wired). Both SCAM-01 and SCAM-02 requirements are satisfied with specific evidence in the article text. Both key links are wired in both directions.

---

_Verified: 2026-03-14_
_Verifier: Claude (gsd-verifier)_
