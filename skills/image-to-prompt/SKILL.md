---
name: image-to-prompt
version: 1.0.0
status: active
created: 2026-02-01
updated: 2026-03-24
owner: Lani
agents: [Lani, Meda, Persey]
departments: [Marketing, Operations]
purposes: [AI Creatorship, Prompt Engineering]
tags:
  - image-to-prompt
  - reverse-engineering
  - prompt-generation
  - midjourney
  - flux
  - ai-image
  - cinematic
description: >
  Analyze an image and reverse-engineer it into a detailed text-to-image prompt.
  Use when the user sends an image and wants a prompt to recreate, remix, or generate similar images.
  Triggers on: "describe this image as a prompt", "how do I recreate this", "give me a prompt for this image",
  "reverse engineer this image", "what's the prompt for this".
---

# Image → Prompt Skill

Analyze an image and output a structured prompt following the laniameda cinematic prompt formula.

## Core Formula (non-negotiable)

**Subject → Scene → Composition/Camera → Lighting/Color → Style Intent → Quality Constraints → Negative Constraints**

## Output Format

```
## Image Analysis

**Subject:** [who/what, distinctive attributes, clothing, props]
**Scene:** [location, environment, time of day, weather]
**Composition:** [shot type, angle, framing, lens feel]
**Lighting:** [source, direction, quality, color temperature]
**Style:** [aesthetic references, era, visual mood]
**Texture/Detail:** [materials, surfaces, grain, rendering style]

---

## Reconstructed Prompt

[Full prompt following the formula — copy-paste ready]

---

## Variants

**V1 (composition shift):** `[alternate framing]`
**V2 (lighting shift):** `[alternate lighting]`
**V3 (style shift):** `[alternate style]`

---

## Recommended Models
- Best match: [model name + why]

## Negative Constraints
`[no X, no Y, no Z]`
```

## Quality Rules

- Concrete over vague — "golden hour sidelight casting long shadows" not "nice lighting"
- One style direction — don't stack incompatible aesthetics
- Include texture cues — grain, material, render quality anchors output
- State what's NOT wanted — negative constraints stabilize results
