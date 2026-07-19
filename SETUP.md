# Hermes for Parenting — Setup & Architecture

## Overview

黄羊育儿经 (Yellow Sheep Parenting Guide) is an AI-powered parenting advisor for a Hong Kong mom with a 13-year-old daughter on the DSE track.

**Core workflow:**
```
Mom (WeChat) → Hermes parenting profile → Research + Verify → HTML page → GitHub Pages → Link back to mom
```

## Architecture Decisions

### Why Hermes profiles (not E2B, not separate agent)?

Hermes profiles provide full data isolation out of the box:
- `~/.hermes/profiles/parenting/` is a completely independent HERMES_HOME
- Separate MEMORY.md, USER.md, SOUL.md, config.yaml, sessions, skills
- Zero risk of parenting data leaking into Harry's personal profile
- WeChat iLink Bot API works from Mac (already set up)

E2B was considered but adds complexity without benefit here:
- WeChat connectivity requires the iLink Bot HTTP API (works from anywhere, not macOS-specific)
- GitHub Pages already provides cloud hosting for the HTML output
- Hermes profile isolation is sufficient for data separation

### Why GitHub Pages (not Notion, not PDF)?

- Public URL with QR code — mom just scans and reads
- No login required, works on any phone
- Each topic is a standalone page (linkable, shareable)
- Auto-deploys on git push
- Mom can forward links to the daughter directly

### Dual-tab design (家长指南 + 给孩子看)

Two audiences, one page:
- **Tab 1 (家长指南):** Mom reads this. Research-backed, practical, gentle tone.
- **Tab 2 (给孩子看):** Mom forwards this to her 13-year-old daughter. Fun, visual, discussion-oriented.

### Content philosophy

- Each response: exactly 1 actionable suggestion (max 3)
- "可以试试" not "你应该" — suggestions, not commands
- Led by research, verified by cross-checking
- Never criticize the mom's current approach
- Never create anxiety ("your kid will fail if you don't...")

## Technical Setup

### Hermes Profile
```bash
hermes profile create parenting --clone   # already done
parenting gateway start                    # start WeChat gateway
```

### GitHub Repo
- Repo: `onezion12344/hermes-for-parenting`
- Pages: `https://onezion12344.github.io/hermes-for-parenting/`
- Source: `/docs` on `main` branch
- Deploy: automatic on push

### File Structure
```
hermes-for-parenting/
├── docs/
│   ├── index.html           # Homepage (dynamic topic list)
│   ├── topic-template.html  # Template for new topic pages
│   ├── topics.json          # Topic index (auto-updated)
│   └── {topic-slug}/        # Per-topic pages
│       └── index.html
├── scripts/
│   └── update_topics.py     # Add topic to topics.json
├── SETUP.md                 # This file
└── README.md
```

### Topic Page Template Variables

When Hermes generates a new page, it replaces these placeholders:
- `{{TITLE}}` — page title
- `{{DATE}}` — publication date
- `{{ORIGINAL_QUESTION}}` — mom's original question
- `{{DECOMPOSED_QUESTIONS}}` — broken-down sub-questions
- `{{RESEARCH_FINDINGS}}` — research results with source tags
- `{{PRACTICAL_ADVICE}}` — actionable suggestions
- `{{RESOURCES}}` — recommended books, articles, tools
- `{{CAVEATS}}` — warnings and common mistakes
- `{{KID_EMOJI}}`, `{{KID_TITLE}}`, `{{KID_CONTENT}}` — kid-facing tab
- `{{KID_DISCUSSION_PROMPT}}` — discussion starter for parent-child

## Family Context (not public — stored in Hermes profile memories only)

The parenting profile's `~/.hermes/profiles/parenting/memories/` contains:
- USER.md: mom's background, parenting style, communication preferences
- MEMORY.md: known strategies, verified resources, workflow rules

These are NEVER deployed to GitHub Pages. They exist only in the local Hermes profile.

## Future Ideas

1. **DSE English resource finder** — tailored to DSE exam requirements
2. **Teen girl content module** — age-appropriate content for 13-year-old girls
3. **Conversation script generator** — exact phrases mom can use
4. **Daily micro-action card** — one tiny action per day, zero thinking required
5. **Progress tracker** — track which suggestions mom tried and how they went
