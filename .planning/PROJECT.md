# Portfolio Website

## What This Is

A personal portfolio site hosted on GitHub Pages (fingers53.github.io) that showcases Robert Treacy's work through explainer articles and links to live projects. Positioned as "analyst who builds" — bridging data analysis, writing, and full-stack engineering. Target audience is recruiters and hiring managers across industries, not just finance/betting.

## Core Value

Every piece must be immediately understandable by a non-technical recruiter — the work speaks for itself without requiring domain knowledge.

## Requirements

### Validated

(None yet — ship to validate)

### Active

- [ ] Landing page with brief bio and links to all pieces
- [ ] AIB Scammer explainer article (convert notebook to web article)
- [ ] Gambling Industry Article 1: Pricing & Calibration (theory — how probabilistic pricing works, favourite-longshot bias, calibration as a universal concept)
- [ ] Gambling Industry Article 2: LLM Triage & Dashboards (operational — automated analytical triage pipeline, compress → rank → summarize, LLM as junior analyst)
- [ ] Gambling Industry Article 3: Optimisation & Classification (methods — knapsack constraints, simple classification rules, when simplicity beats complexity)
- [ ] Links to existing live projects (SEC Parser, Badminton App)
- [ ] Link to existing Irish Elections article
- [ ] Consistent visual style across all articles (Georgia serif, cream background, dark green headers — matching Irish elections piece)
- [ ] Mobile-responsive design

### Out of Scope

- Blog/CMS functionality — static HTML pages only, no dynamic content
- Contact forms — LinkedIn link is sufficient
- Trading/Deribit/Polymarket projects — save for quant-specific applications
- Productivity App, QuizUp Clone, Cortix Games — not ready for public display
- AlertaAlba deep rebuild — heavy subject matter, parking for now
- Interactive visualizations (Plotly, D3) — static PNG charts match existing style

## Context

- Robert is a Senior Insights Analyst at Virgin Bet (Gibraltar), previously at PENN Entertainment (Barstool/ESPN Bet)
- GitHub account is `fingers53`
- Irish Elections article already live at `fingers53.github.io/irish-elections-analysis/` — this is the design template
- Irish elections style: vanilla HTML/CSS, Georgia serif, cream (#fafaf8) background, dark green (#1b3a2d) headers, max-width 720px, static PNG charts, single-column layout
- SEC Parser live at `http://77.42.91.97:5000/`
- Badminton App live at `https://gibbadminton.duckdns.org`
- Gambling Industry PDF is a 9-page writeup with charts already generated (calibration curves, margin plots, knapsack comparisons, triage pipeline diagram)
- AIB Scammer notebook is a single Jupyter notebook that reverse-engineered a phishing site and flooded it with 4,000 fake bank credentials
- Landing page positioning: "analyst who builds" — bridges analytics thinking with shipping real products

## Constraints

- **Hosting**: GitHub Pages (free, static HTML only)
- **Style**: Must match Irish elections article design (Georgia serif, cream/green palette)
- **Content**: No proprietary data or employer-specific details — gambling articles use synthetic/illustrative data (the existing PDF already does this)
- **Scope**: Explainer articles, not full reproductions — narrative + key visuals, not runnable code

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| GitHub Pages over VPS | Free, simple, matches existing Irish elections setup | — Pending |
| Split gambling writeup into 3 | Each piece is digestible and stands alone; theory/operational/methods split | — Pending |
| Match Irish elections style | Consistent brand across all articles, already proven design | — Pending |
| Static PNG charts over interactive | Matches existing style, simpler, works on GitHub Pages | — Pending |
| "Analyst who builds" positioning | Broader appeal than "betting analyst", reflects both writeups and live apps | — Pending |

---
*Last updated: 2026-03-14 after initialization*
