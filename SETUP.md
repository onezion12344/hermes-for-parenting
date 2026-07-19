# Hermes for Parenting — Setup & Architecture

## Overview

黄羊成长记 (Yellow Sheep Parenting Guide) is an AI-powered parenting advisor for a Hong Kong mom with a 13-year-old daughter on the DSE track.

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

E2B was considered for 24/7 cloud operation but deferred as Phase 2:
- E2B sandboxes are fully isolated Linux VMs — even under the same account, Sandbox A cannot access Sandbox B's filesystem
- User already has products on E2B; parenting sandbox would be completely independent
- Hobby tier: free with $100 credit, 1-hour max session per sandbox
- Pro tier: $150/month + compute (~$72/month for 24/7 2vCPU)
- Cheaper approach: wake-on-demand (sandbox spins up every 2-3 min to poll, runs only minutes/day)

**Decision: Phase 1 = Hermes profile on Mac local. Phase 2 = E2B cloud fallback if mom frequently messages when Mac is off.**

Rationale:
- Mom's usage patterns are unknown — premature to pay for 24/7 cloud
- WeChat iLink Bot API is HTTP-based, will work from E2B Linux when needed
- Hermes profile data can be cloned to E2B sandbox when migrating
- GitHub Pages already provides 24/7 cloud web hosting (free)

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

1. **DSE English resource finder** — tailored to DSE exam requirements (English is the key subject for DSE → international transfer)
2. **Teen girl content module** — age-appropriate content for 13-year-old girls (hygiene, body changes, emotions)
3. **Conversation script generator** — exact phrases mom can use (she needs "具体怎么做" guidance)
4. **Daily micro-action card** — one tiny action per day, zero thinking required
5. **Progress tracker** — track which suggestions mom tried and how they went
6. **Phase 2: E2B cloud fallback** — deploy Hermes parenting gateway to E2B sandbox for 24/7 availability when Mac is off

## Key Design Constraints (from real conversations)

- Sister's grades are B+ — the problem is NOT academics, it's life habits, autonomy, and parent-child communication
- Mom already uses DeepSeek for parenting advice — she is AI-literate and receptive to an AI assistant
- Mom's core need: "具体怎么做？" — concrete, script-level guidance, not theory
- Education philosophy: 引导 > 灌输, 身教 > 言传, EQ > grades, health > cramming
- DSE self-study is viable (proven by the older sibling's own experience)
