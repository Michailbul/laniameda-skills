---
name: crea-gallery
description: >
  Save, update, delete, and manage content in laniameda.gallery — Crea's AI creatorship vault.
  Use when Michael says save this, add to vault, add to gallery, store this prompt, save to KB,
  remember this image, update this entry, delete this, or when a strong prompt or image needs
  to be preserved after a generation or digest session. Handles prompts, images, design
  inspirations, and variations. Auto-classifies into the correct pillar. Always use this
  skill for any gallery operation — never call the ingest script directly without it.
version: 1.0.0
status: active
created: 2026-03-26
updated: 2026-03-26
owner: Crea
agents: [Crea]
departments: [AI Creatorship]
purposes: [Knowledge Base, Vault, Prompt Storage, Asset Management]
tags:
  - gallery
  - vault
  - prompts
  - images
  - ingest
  - convex
  - knowledge-base
---

# crea-gallery

**Purpose:** Crea's master interface for laniameda.gallery. Save prompts, images, design references. Update metadata. Delete entries. Everything goes through the `laniameda-kb` ingest script.

**Script:**
```bash
bun run ~/.agents/skills/laniameda-kb/scripts/ingest.ts '<json>'
```

**Env vars** (already set in `/root/.openclaw/.env`):
- `KB_OWNER_USER_ID=278674008` — never pass this in payload, script reads it automatically
- `CONVEX_URL` — Convex deployment URL

---

## Pillar Classification (always set before saving)

| Pillar | What goes here |
|--------|---------------|
| `creators` | AI people — portraits, fashion, influencer, editorial, character, beauty, lookbook |
| `cars` | Automotive — cars, vehicles, roads, racing, mechanical, motion blur |
| `designs` | UI/UX — websites, landing pages, dashboards, mobile apps, components, Figma |
| `dump` | Everything else — abstract, nature, architecture, general prompts, misc |

**When in doubt → `dump`. Never leave pillar empty.**

Quick examples:
- Cinematic fashion portrait → `creators`
- BMW M3 on mountain road → `cars`
- SaaS dark theme landing page → `designs`
- Sunset watercolor → `dump`

---

## Operations

### CREATE — Save a prompt + image
```bash
bun run ~/.agents/skills/laniameda-kb/scripts/ingest.ts '{
  "pillar": "creators",
  "promptText": "Cinematic close-up, golden hour, 35mm film grain...",
  "promptType": "image_gen",
  "generationType": "image_gen",
  "modelName": "Nano Banana Pro",
  "modelProvider": "google",
  "imagePath": "/root/.openclaw/media/inbound/file_xxx.jpg",
  "typedTags": [
    { "name": "fashion", "category": "style", "pillar": "creators", "source": "agent" },
    { "name": "cinematic", "category": "style", "pillar": "creators", "source": "agent" }
  ]
}'
```

### CREATE — Prompt only (no image)
```bash
bun run ~/.agents/skills/laniameda-kb/scripts/ingest.ts '{
  "pillar": "dump",
  "promptText": "...",
  "allowPromptOnly": true,
  "modelName": "FLUX",
  "modelProvider": "flux",
  "tagNames": ["prompts", "dump"]
}'
```

### CREATE — Image from URL
```bash
bun run ~/.agents/skills/laniameda-kb/scripts/ingest.ts '{
  "pillar": "cars",
  "url": "https://example.com/image.jpg",
  "promptText": "...",
  "modelName": "Midjourney",
  "modelProvider": "midjourney",
  "tagNames": ["prompts", "cars"]
}'
```

### CREATE — Design inspiration (no prompt)
```bash
bun run ~/.agents/skills/laniameda-kb/scripts/ingest.ts '{
  "pillar": "designs",
  "typedTags": [
    { "name": "saas", "category": "design_type", "pillar": "designs", "source": "agent" }
  ],
  "designInspiration": {
    "title": "Stripe pricing layout",
    "summary": "Strong hierarchy, simple plan cards",
    "sourceUrl": "https://stripe.com/pricing",
    "inspirationType": "website",
    "platform": "web",
    "workflowType": "page_prompt",
    "ingestKey": "design:stripe:pricing:v1"
  }
}'
```

### CREATE — Prompt variations (multiple images, one prompt)
Use the same `promptIngestKey` across all items:
```bash
bun run ~/.agents/skills/laniameda-kb/scripts/ingest.ts '[
  {
    "pillar": "cars",
    "promptText": "Low-angle Porsche at sunset...",
    "promptIngestKey": "cars:porsche:sunset:v1",
    "ingestKey": "cars:porsche:sunset:v1:a",
    "imagePath": "/path/shot-a.jpg",
    "tagNames": ["prompts", "cars"]
  },
  {
    "pillar": "cars",
    "promptText": "Low-angle Porsche at sunset...",
    "promptIngestKey": "cars:porsche:sunset:v1",
    "ingestKey": "cars:porsche:sunset:v1:b",
    "imagePath": "/path/shot-b.jpg",
    "tagNames": ["prompts", "cars"]
  }
]'
```
⚠️ **Orphan prevention:** Always include both `promptText` + `promptIngestKey` in variation batches. Omitting them creates orphaned assets with no prompt link.

### UPDATE — Patch metadata
Pass `target` with the record type + `id` or `ingestKey`:
```bash
bun run ~/.agents/skills/laniameda-kb/scripts/ingest.ts '{
  "target": { "type": "asset", "ingestKey": "cars:porsche:sunset:v1:a" },
  "pillar": "cars",
  "tagNames": ["prompts", "cars", "porsche", "cinematic"]
}'
```
> Update is **metadata only** — to replace the actual image: delete + create.

### DELETE — Remove an entry
```bash
bun run ~/.agents/skills/laniameda-kb/scripts/ingest.ts '{
  "target": { "type": "asset", "ingestKey": "cars:porsche:sunset:v1:a" },
  "delete": true
}'
```
Idempotent — safe to call twice. Works for `asset`, `prompt`, `designInspiration`.

---

## Asset fidelity rules

When Michael says "save this" — save the **actual asset**, not metadata.

| Source | What to save |
|--------|-------------|
| Telegram image/file | The actual attached file via `imagePath` |
| Carousel | The actual slide images — not og:image or thumbnail |
| Prompt screenshot | Extract the text → `promptText`. The screenshot is the container, not the asset |
| Generated image | The output image via `imagePath` or `imageUrl` |

**Never substitute:** og:image, page thumbnail, caption-only summary, or inferred reconstruction — unless Michael explicitly approves a fallback.

If the real asset can't be reached: try `browser-use-cloud` with saved profile → then Michael's Mac node browser → then ask before falling back to metadata.

---

## Validator quick reference

**`modelProvider`:** `openai` · `anthropic` · `google` · `xai` · `meta` · `flux` · `midjourney` · `runway` · `other`
→ Use `other` for Kling, Seedance, Nano Banana, Kora Reality, and any non-listed provider.

**`promptType`:** `image_gen` · `video_gen` · `ui_design` · `cinematic` · `ugc_ad` · `other`

**`generationType`:** `image_gen` · `video_gen` · `ui_design` · `other`

**`workflowType`:** `component_prompt` · `page_prompt` · `system_prompt` · `asset_recipe` · `other`

**`typedTags[].category`:** `model_name` · `style` · `content_type` · `platform` · `color` · `camera_angle` · `lighting` · `composition` · `car_make` · `car_model` · `car_angle` · `environment` · `design_style` · `design_type` · `workflow_type` · `component_type` · `custom`
→ No `subject` — use `content_type` instead.

**`promptSections` fields:** `finalPrompt` (required) · `generationNotes` · `negativePrompt`
→ No other keys — extra fields cause validation errors.

---

## Tagging conventions

Always include:
- Pillar as a tag: `creators` / `cars` / `designs` / `dump`
- Content category: `prompts` / `tutorials` / `resources` / `ideas`
- Model name as tag: `nano-banana-pro` / `flux` / `midjourney` / `kling` / etc.
- Relevant style tags: `cinematic` / `fashion` / `portrait` / `automotive` / `ui` / etc.

---

## After saving

Always report back:
- Pillar assigned
- What was saved (prompt / image / design ref)
- Model tagged
- Tags applied
- ingestKey used (for future update/delete reference)

If duplicate (same ingestKey already exists) → "already in vault, skipped."

---

## Schema updates

If Convex schema has changed since this skill was last updated:
- Read `references/schema-contract.md` for current table/field map
- Read `references/ingest-examples.md` for copy-ready patterns
- Pull latest from gallery repo: `cd ~/work/laniameda/laniameda.gallery && git pull && bun run skills:update`

When Michael says he pushed gallery repo changes → pull + update immediately, no asking.
