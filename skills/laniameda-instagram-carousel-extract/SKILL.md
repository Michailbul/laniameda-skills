---
name: laniameda-instagram-carousel-extract
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
  - carousel
  - image-slides
  - extract
  - prompts
  - browser-use-cloud
depends_on: [browser-use-cloud, supadata]
replaces: [instagram-extract]
---

# laniameda-instagram-carousel-extract

**Purpose:** Extract content from Instagram carousel posts (image slides). Read text overlaid on slides, extract prompts, workflows, checklists, or frameworks — and save to KB.

**Source:** Instagram carousels (multi-image posts, slides with text).
**Not for:** Instagram reels (video) → use `laniameda-instagram-reel-digest`.

---

## Triggers

- Instagram carousel post URL pasted
- "extract this carousel"
- "what's in these slides"
- "save this carousel"
- "get the prompts from this post"
- "extract the workflow from this"

---

## Workflow

### Step 1 — Check caption via Supadata metadata first (fast)
```bash
curl -s "https://api.supadata.ai/v1/metadata?url=<POST_URL>" \
  -H "x-api-key: $SUPADATA_API_KEY"
```
Caption often contains the full text of the slides. If caption is complete → no need for browser.

### Step 2 — If caption is truncated or slides have visual text
Use `browser-use-cloud` to scroll through slides:

Task prompt template:
```
Go to [URL]. This is an Instagram carousel. Scroll through EVERY slide one by one.
For EACH slide: VISUALLY READ any text shown in the image and transcribe it exactly.
These may contain prompts, steps, frameworks, or tips overlaid on the image.
Also extract the full caption and any links mentioned.
```

Use `bu-mini` model. Set `maxCostUsd: 0.50`. Use `BROWSER_USE_PROFILE_ID` if available.

### Step 3 — Classify content

Decide what this is:
- A prompt → save to `laniameda-kb` with correct pillar
- A workflow/tutorial → save to `content-kb/sources/instagram/YYYY-MM-DD-<slug>/`
- A framework/checklist → save as notes + optionally draft a skill

### Step 4 — Deliver

```
[Author] — Instagram Carousel ([X] slides)

What it is: [one sentence]

Key content:
• [slide 1 summary or exact text]
• [slide 2 summary or exact text]
• ...

Worth saving as: [prompt / workflow / reference / skill]
```

Then save based on Michael's direction or your judgment.

---

## Hard Rules

- Always check caption via Supadata first — saves a browser call.
- Tell the browser agent to VISUALLY READ text in images — not just extract HTML alt text.
- If slides are all images with no text → report that and save image URLs for reference.
- Classify and route to the right save destination, don't just dump raw text.
