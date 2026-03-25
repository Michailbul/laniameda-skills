---
name: crea-cinematic-prompts
description: >
  Turn a concept into cinematic AI still + cinematic AI video prompts using a structured formula.
  Prompt-writing first workflow (no seed-first teaching): build strong semantic control through
  subject, scene, composition, lighting, style, and constraints.
metadata:
  laniameda:
    departments: ['Operations']
    purposes: ['Automation']
    tags: ['operations']
    status: active
    depends_on: []
    replaces: []
  clawdbot:
    emoji: 🎬
---

# Crea — Cinematic Prompt Writing Skill

## Core Rule (non-negotiable)
**Prompt writing quality is primary.**
Do **not** teach seed as a core method. Consistency should come from explicit language:
subject anchors, scene anchors, composition anchors, and constraints.

## Scope split (avoid duplication)
- **This skill = detailed execution** (templates, workflows, checklists).
- **Agent knowledge files = high-level principles only**.

## Default Deliverables
When asked for cinematic output, always provide:
1) **Hero still prompt** (image)
2) **2–3 video prompts** (establishing + action + close-up)
3) **Why each variant differs** (composition OR lighting OR style)
4) **Final tightened winner prompt**
5) **Negative constraints**

## Master Prompt Formula
Use this order:

**Subject → Scene → Composition/Camera → Lighting/Color → Style Intent → Quality Constraints → Negative Constraints**

### Copy-paste template
`[subject + distinctive attributes], [scene/environment], [composition/camera], [lighting/color mood], [style intent], [quality constraints], [negative constraints]`

---

## High-Quality Prompt Writing Rules

1. **Subject clarity first**
   - Name identity traits explicitly (age band, clothing, distinctive markers, prop).
2. **Scene must be physically coherent**
   - Location, materials, weather/time-of-day, and context should match.
3. **Composition must be intentional**
   - Framing + angle + shot distance + lens feel.
4. **Lighting should be concrete**
   - Source + direction + intensity + color temperature/mood.
5. **Style intent should be bounded**
   - Keep references specific; avoid stacking incompatible styles.
6. **Constraints make outputs stable**
   - State what must be present and what must be excluded.

---

## Controlled Iteration Protocol (no seed-talk)

1) Write one strong **base prompt**.
2) Create 3 variants:
   - **V1:** change composition only
   - **V2:** change lighting only
   - **V3:** change style only
3) Compare outputs with rubric.
4) Tighten winner:
   - remove vague adjectives
   - keep concrete visual descriptors
   - keep only one clear artistic direction

---

## Cinematic Still Prompt Checklist
A cinematic still prompt should explicitly include:
- Subject identity anchors
- Environment + time-of-day
- Composition (rule-of-thirds/off-center unless asked otherwise)
- Lighting plan (motivated source + contrast)
- Texture realism cues
- Negative constraints

### Quick still template
`[LOCATION]. [SUBJECT + anchor traits] [micro-action]. [COMPOSITION + camera angle/lens feel]. [LIGHT SOURCE] creates [contrast/mood]. [TIME OF DAY], [COLOR GRADE]. [TEXTURE CUES]. [NEGATIVE CONSTRAINTS].`

---

## Camera Move Menu (video prompts)
Pick 1–2 max:
- Static
- Handheld
- Zoom In / Zoom Out
- Camera follows
- Pan left / Pan right
- Tilt up / Tilt down
- Orbit around
- Dolly in / Dolly out

---

## Negative Constraints Defaults
Use as needed:
- `no exaggerated body deformation`
- `no plastic skin`
- `no over-smoothed textures`
- `no duplicated subjects`
- `no random text overlays`
- `no cartoon/anime look (unless requested)`

---

## Output Format (strict)

### Base Prompt
`...`

### Variants
- **V1 (composition change):** `...`
- **V2 (lighting change):** `...`
- **V3 (style change):** `...`

### Best Candidate + Why
- Winner: `Vx`
- Why: `[identity clarity / composition / lighting coherence / style fidelity]`

### Final Tight Prompt
`...`

---

## Operator Questions (minimal)
Ask only:
1) What is the scene in one sentence?
2) Who/what is the subject (+ key visual anchors)?
3) What camera vibe do you want?
4) What mood/lighting direction?
