---
name: laniameda-instagram-reel-digest
description: >
  Digest an Instagram reel (video with speech) so Michael doesn't have to watch it. Uses Supadata
  for transcript first, falls back to browser-use-cloud. Extracts what's said, shown, and actionable.
  Not for carousel posts (image slides) — use laniameda-instagram-carousel-extract for those.
  Keywords: instagram reel, digest reel, watch this reel, extract reel, instagram video.
version: 1.0.0
status: active
created: 2026-03-25
updated: 2026-03-25
owner: Lani
agents: [Lani, Meda]
departments: [Marketing, Operations]
purposes: [Ingestion, Research, Knowledge Base]
tags:
  - instagram
  - reel
  - video
  - transcript
  - digest
  - supadata
depends_on: [supadata, browser-use-cloud]
replaces: [instagram-extract]
---

# laniameda-instagram-reel-digest

**Purpose:** Watch an Instagram reel so Michael doesn't have to. Extract what's said, what's shown, what's actionable — and optionally save to KB or package as a skill.

**Source:** Instagram reels (video with audio/speech).
**Not for:** Instagram carousel posts (image slides) → use `laniameda-instagram-carousel-extract`.

---

## Triggers

- Instagram reel URL pasted
- "watch this reel"
- "what does she say in this"
- "digest this reel"
- "transcribe this reel"
- "extract from this reel"

---

## Workflow

### Step 1 — Try Supadata transcript first
```bash
curl -s "https://api.supadata.ai/v1/transcript?url=<REEL_URL>&text=true" \
  -H "x-api-key: $SUPADATA_API_KEY"
```
Also fetch metadata:
```bash
curl -s "https://api.supadata.ai/v1/metadata?url=<REEL_URL>" \
  -H "x-api-key: $SUPADATA_API_KEY"
```
Check the caption/description first — often contains the full workflow in text.

### Step 2 — If Supadata returns no transcript
Fall back to `browser-use-cloud` with visual extraction:
- Open the reel URL
- Play and capture any on-screen text
- VISUALLY READ any text overlaid on the video frames
- Extract caption from the page

### Step 3 — Distill

From transcript + caption + on-screen text, extract:
- What the workflow is (step by step)
- Any prompts shown or spoken
- Any tools mentioned
- Key techniques or insights
- What's worth saving vs what's filler

### Step 4 — Deliver verdict

```
[Author] — Instagram Reel

What it is: [one sentence]

Key points:
• [point 1]
• [point 2]
• [point 3]

Worth saving? [yes/no + why]
```

If user says "save it" or "make it a skill":
- Save structured notes to `content-kb/sources/instagram/YYYY-MM-DD-<slug>/`
- Or draft a SKILL.md if it contains a reusable workflow

---

## Hard Rules

- Supadata first, always. Never open browser without trying Supadata.
- Caption often has the full workflow — read it before the transcript.
- Deliver verdict first, full transcript only if asked.
- If reel has no speech and no on-screen text → say so clearly, report what visual content was there.
