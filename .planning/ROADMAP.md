# Roadmap: Portfolio Website

## Overview

Four phases get a recruiter-ready portfolio live as fast as possible. Phase 1 deploys a styled landing page to GitHub Pages immediately — something exists on the internet from day one. Phase 2 adds the AIB Scammer article (notebook-to-HTML conversion, self-contained). Phase 3 adds the three gambling industry articles in parallel. Phase 4 wires in the live project cards and cross-links everything.

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [x] **Phase 1: Foundation** - Landing page + shared CSS deployed to GitHub Pages (completed 2026-03-14)
- [ ] **Phase 2: AIB Scammer Article** - Notebook converted to standalone web article
- [ ] **Phase 3: Gambling Industry Articles** - Three articles covering pricing, triage, and optimisation
- [ ] **Phase 4: Polish & Links** - Live project cards, cross-linking, final responsive pass

## Phase Details

### Phase 1: Foundation
**Goal**: A live, styled portfolio exists at fingers53.github.io
**Depends on**: Nothing (first phase)
**Requirements**: LAND-01, LAND-02, LAND-03, STYLE-01, STYLE-02, STYLE-03
**Success Criteria** (what must be TRUE):
  1. Visiting fingers53.github.io shows a landing page with name, "analyst who builds" positioning, and placeholder links to all planned pieces
  2. LinkedIn and GitHub profile links are present and open in a new tab
  3. Page renders correctly on a 375px mobile viewport with no horizontal scroll and tap targets at least 44px
  4. All articles use Georgia serif, cream (#fafaf8) background, dark green (#1b3a2d) headers, max-width 720px — matching the Irish elections piece
  5. Charts (when added) render as static PNGs with 1px border and 4px border-radius
**Plans**: 1 plan

Plans:
- [ ] 01-01-PLAN.md — Shared stylesheet (style.css) and landing page (index.html)

### Phase 2: AIB Scammer Article
**Goal**: A recruiter can read the full AIB Scammer story as a web article
**Depends on**: Phase 1
**Requirements**: SCAM-01, SCAM-02
**Success Criteria** (what must be TRUE):
  1. Article explains how the phishing site worked (mobile-only serving, user agent detection, credential harvesting) in plain language a non-technical reader follows
  2. Article explains the counter-attack (spoofed user agents, fake Irish IPs, 4,000 fake credentials) and why poisoning the dataset was the goal
  3. Landing page link to the article resolves and renders with consistent site styling
**Plans**: TBD

### Phase 3: Gambling Industry Articles
**Goal**: All three gambling industry articles are live and readable
**Depends on**: Phase 1
**Requirements**: GAMB-01, GAMB-02, GAMB-03
**Success Criteria** (what must be TRUE):
  1. Article 1 (Pricing & Calibration) explains implied probability, calibration curves, and favourite-longshot bias in terms that transfer to any pricing business — no betting domain knowledge required
  2. Article 2 (Automated Triage) explains the compress-rank-summarize pipeline and positions the LLM as a constrained junior analyst directing human attention to highest-impact areas
  3. Article 3 (Optimisation & Classification) explains knapsack-style selection and threshold classification with a clear "when simplicity beats complexity" conclusion
  4. All three articles link back to the landing page and to each other as a series
**Plans**: TBD

### Phase 4: Polish & Links
**Goal**: Every live project is linked, cross-links are complete, and the site is fully navigable
**Depends on**: Phase 2, Phase 3
**Requirements**: LIVE-01, LIVE-02, LIVE-03
**Success Criteria** (what must be TRUE):
  1. SEC Parser card on landing page links to http://77.42.91.97:5000/ with a 1-2 sentence description of what it does
  2. Badminton App card links to https://gibbadminton.duckdns.org with a 1-2 sentence description
  3. Irish Elections card links to fingers53.github.io/irish-elections-analysis/ with a 1-2 sentence description
  4. All article pages have a working "back to portfolio" navigation link
**Plans**: TBD

## Progress

**Execution Order:**
Phases execute in numeric order: 1 -> 2 -> 3 -> 4

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Foundation | 1/1 | Complete    | 2026-03-14 |
| 2. AIB Scammer Article | 0/TBD | Not started | - |
| 3. Gambling Industry Articles | 0/TBD | Not started | - |
| 4. Polish & Links | 0/TBD | Not started | - |
