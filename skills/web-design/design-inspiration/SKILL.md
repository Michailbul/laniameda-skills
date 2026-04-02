---
name: design-inspiration
description: >
  Loads visual design references to guide any design creation or modification task.
  ALWAYS use this skill whenever Claude is about to create or modify any design artifact —
  including UI components, landing pages, web interfaces, dashboards, React/HTML code,
  Figma outputs, slide decks, or any visual/frontend work. Even if the user doesn't say
  "use my references" — if a design is being made or changed, consult this skill first.
  The references folder contains images and notes representing the target aesthetic;
  Claude must read and internalize them before producing any design output.
  Also use this skill when the user says "save to gallery", "add to gallery", "save this design",
  or wants to archive a reference, screenshot, or URL into the laniameda.gallery Design pillar.
---

# Design Inspiration

This skill has two responsibilities:

1. **Load references** — read visual inspiration files before any design task
2. **Save to gallery** — ingest design references into laniameda.gallery under the **Designs** pillar

---

## Workflow A — Load references before designing

### Step 1 — Load references

Before writing a single line of design code or producing any visual output:

1. Run `ls /mnt/skills/user/design-inspiration/references/` to see what's available.
2. For every image file found, load it with the `view` tool and study it carefully.
3. For every `.md` or `.txt` file found, read it with the `view` tool.
4. Synthesize what you observe into a mental model of the target aesthetic (see below).

If no references exist yet, note this to the user and proceed with your best judgement,
suggesting they populate the folder (see **Adding References** below).

### Step 2 — Extract the design language

From the references, identify and internalize:

| Dimension | What to look for |
|---|---|
| **Color palette** | Background, surface, accent, text, border colors. Exact hex values if readable. |
| **Typography** | Font families, weights, sizes, line heights, letter spacing. |
| **Spacing & layout** | Grid density, padding rhythm, margin scale, component gaps. |
| **Shape language** | Border radius, sharp vs. rounded, card styles, button shapes. |
| **Depth & elevation** | Shadows, blur, layering, glassmorphism, flat vs. skeuomorphic. |
| **Motion cues** | Any noted animations, transitions, interaction patterns. |
| **Mood / tone** | Minimal, brutalist, editorial, dark luxury, playful, corporate, etc. |
| **Recurring patterns** | Repeated UI motifs, icon styles, dividers, decorative elements. |

### Step 3 — Apply to the design task

Use the extracted design language as constraints when generating code or describing designs:

- Match the color palette precisely — don't default to generic blues/grays.
- Mirror the typography choices, including weight and size relationships.
- Preserve the spacing rhythm and layout density.
- Replicate the shape and depth language.
- Comment in your code what reference(s) you're drawing from.

### Step 4 — Call out deviations

If you intentionally deviate from the references (e.g. for accessibility, technical
constraints, or because a reference doesn't cover the required component), say so explicitly.

---

## Workflow B — Save to laniameda.gallery (Design pillar)

Use this workflow when the user wants to save a design reference, screenshot, URL, or note
to the gallery. All design saves go to `pillar: "designs"`.

### Trigger phrases

- "save to gallery"
- "add to gallery"
- "save this design / reference / inspiration"
- "archive this"
- "log this to the gallery"

### Step 1 — Collect what to save

Determine the content type from what the user provides:

| What they give you | Content type |
|---|---|
| A URL (Dribbble, Figma, website, etc.) | `url` |
| A local image file path | `imagePath` |
| A description / notes only | `designInspiration` text + `allowPromptOnly: true` |
| An uploaded image | Save it locally first, then use `imagePath` |

### Step 2 — Extract tags

From the content being saved, extract relevant `typedTags`. Use only valid categories:

- `design_style` — e.g. "dark-luxury", "brutalist", "editorial", "glassmorphism"
- `design_type` — e.g. "landing-page", "dashboard", "card", "navigation", "modal"
- `color` — e.g. "amber", "near-black", "warm-white"
- `style` — e.g. "minimal", "dense", "airy"
- `content_type` — e.g. "ui-screenshot", "figma-export", "mockup"
- `platform` — e.g. "web", "mobile", "desktop"
- `component_type` — e.g. "button", "input", "hero-section"

Format: `{ "category": "<category>", "value": "<value>" }`

### Step 3 — Build the ingest payload

```json
{
  "pillar": "designs",
  "designInspiration": "<brief description of what this is and why it's inspiring>",
  "url": "<url if applicable>",
  "imagePath": "<local path if applicable>",
  "allowPromptOnly": true,
  "ingestKey": "design-<slug>-<YYYY-MM-DD>",
  "typedTags": [
    { "category": "design_style", "value": "dark-luxury" },
    { "category": "design_type", "value": "landing-page" }
  ]
}
```

**Rules:**
- Always set `pillar: "designs"`
- Always provide at least one of: `url`, `imagePath`, or `designInspiration`
- Set `allowPromptOnly: true` when saving text/notes without a file or URL
- Use a stable, human-readable `ingestKey` for retry safety (e.g. `design-vercel-dashboard-2026-03-27`)
- Never hardcode `ownerUserId` — it's read from env (`KB_OWNER_USER_ID=278674008`)

### Step 4 — Run the ingest script

```bash
bun run ~/.agents/skills/laniameda-gallery-ingest/scripts/ingest.ts '<payload-json>'
```

If env vars aren't set in the shell, prefix them:

```bash
CONVEX_URL=<from-env> KB_OWNER_USER_ID=278674008 \
  bun run ~/.agents/skills/laniameda-gallery-ingest/scripts/ingest.ts '<payload-json>'
```

Both `CONVEX_URL` and `KB_OWNER_USER_ID` are already set in `/root/.openclaw/.env` — no need to pass them manually in most contexts.

### Step 5 — Confirm to user

After a successful ingest, confirm with:
- What was saved (title/description)
- The `ingestKey` used (useful for future updates)
- Pillar: Designs ✓

If the ingest fails, show the error and suggest checking `CONVEX_URL` env var or verifying the skill is installed:
```bash
bunx skills add https://github.com/laniamedaHQ/laniameda-gallery/tree/main/skills/laniameda-gallery-ingest -g -a openclaw
```

### Example payloads

**Save a URL:**
```json
{
  "pillar": "designs",
  "designInspiration": "Vercel dashboard — clean dark UI with tight spacing and monospace data display",
  "url": "https://vercel.com/dashboard",
  "allowPromptOnly": true,
  "ingestKey": "design-vercel-dashboard-2026-03-27",
  "typedTags": [
    { "category": "design_style", "value": "dark-minimal" },
    { "category": "design_type", "value": "dashboard" },
    { "category": "platform", "value": "web" }
  ]
}
```

**Save a local screenshot:**
```json
{
  "pillar": "designs",
  "designInspiration": "UI screenshot showing amber-on-dark card layout with tight grid",
  "imagePath": "/Users/michael/Desktop/card-reference.png",
  "ingestKey": "design-card-amber-dark-2026-03-27",
  "typedTags": [
    { "category": "design_style", "value": "dark-luxury" },
    { "category": "design_type", "value": "card" },
    { "category": "color", "value": "amber" }
  ]
}
```

**Save notes only:**
```json
{
  "pillar": "designs",
  "designInspiration": "Reference aesthetic: near-black bg #0A0A0A, amber accent #F59E0B, Inter font, 8px radius on cards, no shadows — depth via layering only",
  "allowPromptOnly": true,
  "ingestKey": "design-aesthetic-notes-2026-03-27",
  "typedTags": [
    { "category": "design_style", "value": "dark-luxury" },
    { "category": "color", "value": "amber" }
  ]
}
```

---

## Adding local references

To add design references to this skill's local folder, place files in:

```
/mnt/skills/user/design-inspiration/references/
```

**Accepted file types:**
- `.png`, `.jpg`, `.webp`, `.gif` — screenshots, mockups, inspiration images
- `.md` — written design notes, token values, brand guidelines
- `.txt` — color palettes, font stacks, spacing scales

**Tips:**
- Include screenshots of UI you admire — the more specific the better.
- Add a brief `.md` note alongside each image describing *what* you like about it.
- Group related references with a common prefix (e.g. `dark-card-01.png`, `dark-card-02.png`).

---

## Skill maintenance

- Update local references whenever the design direction evolves.
- Remove outdated references to keep the aesthetic signal clean.
- If references conflict, newer files take precedence — or add a `PRIORITY.md` to explicitly rank them.
- When the ingest contract changes, the source of truth is always:
  `~/work/laniameda/laniameda.gallery/skills/laniameda-gallery-ingest/SKILL.md`
