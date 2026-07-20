# 黄羊成长记 — Product Spec (OpenOPC)

## Problem Statement

**Parents and teenagers can't communicate.** Parents default to authoritarian patterns ("听我的"), teenagers withdraw. The cycle: parent anxiety → control → rebellion → more anxiety.

**Current solution doesn't exist.** Existing parenting content is passive (articles, videos, books). Parents need an *interactive* coach that meets them where they are — on WeChat — and gives them concrete, research-backed scripts they can use today.

**Unique angle**: This isn't just for parents. Children can use it to help their parents understand them.

## Product

A WeChat bot that acts as a parenting communication coach.

### Core Flow

```
Parent scans QR → Bot: "Hi! I'm 黄羊. Let me learn about your family first."
  → Q1: Child's age, grade
  → Q2: What's the biggest challenge right now?
  → Q3: How would you describe your communication style?
  → Bot personalizes its responses based on answers
  
Every message from parent:
  → Decompose vague concern → Research → 1 actionable suggestion
  → Optional: generate HTML report → push to GitHub Pages → send link
```

### Pre-filled QR (v2)
When a child or sibling sets up the bot for their parent:
1. They answer the onboarding questions first
2. A QR is generated that carries this context
3. Parent scans → bot already knows the family context

## Architecture

```
Parent (WeChat) ↔ iLink Bot ↔ Agent Gateway ↔ DeepSeek API
                                              ↔ GitHub Pages (content delivery)
                                              ↔ Web Search (research)
```

| Component | Technology | Status |
|-----------|-----------|--------|
| WeChat bridge | iLink Bot API + nanobot/Hermes gateway | ⚠️ nanobot token unstable |
| Agent personality | SOUL.md (Chinese parenting coach) | ✅ Done |
| Content delivery | GitHub Pages (Jekyll-free /docs) | ✅ Live |
| Research pipeline | Web search + cross-verify + deep-research | ✅ Skills available |
| HTML templates | Dual-tab (parent guide + kid view) | ✅ Done |
| Daily digest | Cron job: AI edu + DSE + health | ✅ Configured |
| Cloud hosting | Oracle Cloud Always Free (ARM VM) | 🔄 Signup in progress |

## Integration with OneZion DSE Agent

The DSE agent already handles:
- HK DSE exam content generation
- Parent-facing educational materials
- Subject-specific research pipelines

**Synergy points:**
1. DSE agent provides exam-specific advice (English prep, subject strategies)
2. Sharing the same research/verification pipeline
3. Common HTML template system
4. Shared WeChat bot infrastructure

## OpenOPC Company Structure

| Role | Responsibility |
|------|---------------|
| CEO/PM | Product vision, parent interviews, content quality |
| CTO | Agent infrastructure, WeChat gateway, GitHub Pages |
| Content Lead | SOUL.md tuning, response quality, resource curation |
| Research Lead | Daily digest pipeline, fact-verification, source management |
| Growth | WeChat distribution, QR code placement, parent communities |

## Next Steps

1. **Stabilize WeChat gateway** — fix nanobot/Hermes token refresh
2. **Build onboarding flow** — Q&A after first scan, context storage
3. **Pre-fill QR generation** — encode onboarding answers into QR metadata
4. **Launch MVP** — mom as first user, iterate on response quality
5. **Open to parents** — distribute QR in HK parent WeChat groups
