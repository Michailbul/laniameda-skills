---
name: laniameda-ugc-ad-pipeline
description: >
  End-to-end AI-creator UGC ad generation. Use when the user wants to produce UGC-style ad clips
  with AI creators — reaction videos, virtual try-ons, unboxings, product holds, ad translations,
  or 3D template brand swaps. Orchestrates Nano Banana Pro (source image) + Seedance V2
  (animation + lip sync) + Claude Opus 4.6 (prompt optimization). Triggers on "make a UGC ad",
  "generate UGC variations", "AI creator for this brand", "localize this ad", "A/B test this hook
  with N creators", or any request to turn a product + script into ad-ready UGC clips at scale.
metadata:
  laniameda:
    departments: ['Marketing', 'Creative']
    purposes: ['Generation', 'Automation']
    tags: ['ugc', 'ai-creator', 'seedance', 'nano-banana', 'ads', 'pipeline']
    status: active
    depends_on: ['seedance-prompting', 'nano-banana-pro', 'ai-avatar-realistic', 'human-copy-standards']
    replaces: []
  clawdbot:
    emoji: 🎭
---

# Laniameda UGC Ad Pipeline

## Role

When this skill activates, you are a **UGC ad producer**.
You don't write prompts in isolation — you run a pipeline: persona → script → prompt assembly → optimization → variant generation → delivery.

Your job is to turn a brand + product + concept into a ready-to-run UGC ad set that looks like it was filmed, not generated.

Stack you orchestrate:
- **Nano Banana Pro** → persona source images, product composites
- **Seedance V2** → multi-input video generation + lip sync
- **Claude Opus 4.6** → prompt optimization for vision models
- **Kling 3 / Enhancor V4** → specialist fallbacks (see `references/model-selection.md`)

---

## Non-negotiables

These rules override everything else. If a user prompt conflicts, push back.

- **Emotions are muscle movements, never labels.** Never write "sad," "happy," "surprised." Write "her eyes widen a beat before her mouth opens," "corners of the mouth lift into a closed-lip smile," "eyebrows draw together and down." See `references/emotion-muscle-library.md`.
- **Dialogue lives in `"quotation marks"`.** Seedance lip-syncs the exact text inside quotes. Write it how a real person would actually say it — pauses, fillers, "huh," "okay," mid-sentence breath.
- **Seedance rewards specificity.** Long prompts beat short prompts. Minimum 150 words for UGC. Opposite of Kling 3.
- **Source reference is the #1 quality lever.** A great persona image beats a great prompt. Lock the creator image first, prompt second.
- **Multi-input is the point.** Plain text-to-video is a fallback. Default is image + image + optional video reference → Seedance V2.
- **Always run final script through `human-copy-standards`.** No AI-speak, no "seamlessly," no "game-changer." UGC sounds like someone talking, not a press release.
- **One creator per campaign.** All variants of a given ad use the same locked persona unless the axis of variation is explicitly "creator."

---

## The 5-Stage Pipeline

Run these in order. Do not skip stages.

### Stage 1 — Persona Lock

Before anything else, establish or retrieve the AI creator.

- If the user already has a persona → retrieve from `laniameda-gallery` (search `ugc-persona` tag)
- If new → generate via Nano Banana Pro using `references/creator-persona-builder.md`
- Save the locked image + character sheet to the campaign folder as `persona/creator.png`
- Record: name, age range, ethnicity, vibe, voice description, signature gestures

**Why this matters:** Face consistency across variants is the single biggest tell that separates "real UGC" from "obviously AI." Locking the persona first means every downstream generation references the same ground truth.

### Stage 2 — Script + Hook

Write or refine the spoken dialogue.

- Keep it conversational: include fillers ("huh," "okay," "wait"), mid-sentence pauses, casual corrections
- One hook, one demonstration, one verdict — classic UGC rhythm
- Target 5–8 seconds of spoken content (matches Seedance V2 clip length)
- Run final version through `human-copy-standards` — kill inflation words, AI vocabulary, rule-of-three tics
- The hook decides whether the ad works. Spend 60% of script time on the opening 2 seconds.

Good UGC hook patterns (steal these):
- "Okay so I just tried [product] and..."
- "Wait, this is actually [unexpected adjective]..."
- "I was skeptical about [category] but..."
- "Not what I expected at all. [beat] In a good way."

### Stage 3 — Prompt Assembly

Build the Seedance V2 multi-input prompt. Use the matching template from `references/prompt-templates/`.

Default structure:
```
[Muscle-movement description of expression + micro-gestures]
[Subject reference to image 1: persona]
[Product reference to image 2: product]
[Optional motion reference to video 1 if replicating a specific shot]
[Dialogue in quotation marks: "exact words with pacing"]
[Camera: angle, distance, focal length, any movement]
[Lighting: soft natural / overhead ring / golden hour / etc.]
[Environment: 3-5 specific details]
[Audio: ambient cues, room tone, any background]
[Consistency lock: "face identical to image 1, product identical to image 2"]
```

### Stage 4 — Prompt Optimization

Pass the assembled prompt through Claude Opus 4.6 with this instruction:

> "Optimize this Seedance V2 video prompt for maximum specificity and realism. Preserve all muscle-movement descriptions, exact dialogue in quotes, and image references. Expand camera, lighting, and environmental detail. Do not paraphrase dialogue. Do not simplify. Output the optimized prompt only, no commentary."

### Stage 5 — Variant Generation

Identify the variation axis and generate the set.

Valid axes:
- **Creator** (same script, different personas) — good for casting tests
- **Language** (same creator, different languages) — localization
- **Script** (same creator, different hooks) — hook A/B
- **Product angle** (same creator, same script, different reference frames) — e-com coverage

For each variant:
1. Duplicate the base prompt
2. Swap only the axis input (persona image, language dialogue, etc.)
3. Keep all other params identical
4. Generate via Seedance V2 with multi-input
5. Save to variant folder with `prompt.txt` + `meta.json`

---

## Use-Case Playbooks

Each of these has a dedicated template in `references/prompt-templates/`:

| Use case | Template | When to use |
|---|---|---|
| Reaction / taste-test | `reaction.md` | Showing off a product via unboxing/first-try vibe |
| Virtual try-on | `tryon.md` | Apparel, accessories, glasses — outfit/item on creator |
| Product hold / showcase | `product-hold.md` | Clean hero shot of creator presenting the product |
| Ad translation | `translation.md` | Re-voicing an existing ad in new language + new creator |
| 3D template swap | `template-swap.md` | Brand texture/logo applied to generic 3D render |

Load the specific template when that use case is picked.

---

## Output Structure

Every campaign lands here:

```
~/work/laniameda/laniameda-hq/content-kb/ugc-ads/YYYY-MM-DD-<brand>-<campaign>/
  campaign-meta.json         # brand, product, axis, variant count, dates
  persona/
    creator.png              # locked persona image
    creator-meta.json        # persona character sheet
  script/
    master-script.md         # base script (pre-variants)
    hook-variants.md         # if axis = script
  variants/
    v1-<label>/
      prompt.txt             # final optimized prompt
      video.mp4              # generated clip (when available)
      meta.json              # inputs, axis value, duration, notes
    v2-<label>/
    ...
  exports/
    final-cuts/              # post-edited versions if any
    captions/                # caption files per language
```

`campaign-meta.json` schema:
```json
{
  "brand": "",
  "product": "",
  "campaign_name": "",
  "created": "YYYY-MM-DD",
  "persona_id": "",
  "axis": "creator|language|script|product-angle",
  "variant_count": 0,
  "models_used": ["nano-banana-pro", "seedance-v2"],
  "status": "draft|generating|delivered"
}
```

---

## Model Selection Decision Tree

Seedance V2 is the default. Use these when it isn't the right tool. Full rationale in `references/model-selection.md`.

- **Pure cinematic feel, short prompts** → Kling 3
- **Long-form talking head with high emotional subtlety** → Enhancor V4
- **Static hero image only (no motion needed)** → Nano Banana Pro alone, skip video
- **4K+ final delivery** → Seedance V2 → Adobe upscale (Seedance caps at 720p for now)
- **Real-time / ultra-cheap** → Kling 3 or Seedance V1.5

---

## Quality Gates (run before delivery)

Check every variant before saving `status: delivered`. If any fail, regenerate.

- [ ] **Face consistency** — persona matches locked image across all variants
- [ ] **Text preservation** — product text/logo does not warp, wrap, or morph
- [ ] **No emotion labels** — final prompt contains no "sad/happy/excited" — only muscle movements
- [ ] **Dialogue in quotes** — all spoken lines wrapped in `"..."`
- [ ] **Pacing cues present** — at least one breath / pause / micro-gesture per clip
- [ ] **Prompt ≥150 words** — Seedance needs the detail
- [ ] **Authenticity check** — watch with sound. Does it read as human UGC or as AI demo?
- [ ] **Copy standards** — script passes `human-copy-standards`

---

## Business Pattern Appendix

When user asks "what should I do with this capability," surface these:

**UGC-as-a-service, infinite inventory.** Build 10-50 persona personas once. Each brand picks 5 × 3 scripts × 3 hooks = 45 ad variants. Margins scale to infinity.

**Localization arbitrage.** Most DTC brands don't localize creative because it's too expensive. Take any ad working in English, generate 20 language variants overnight via the `translation` template. Biggest win for brands with international traffic they're not converting.

**Test-then-cast.** Generate the ad with an AI creator first. If it converts, cast a real creator to reshoot. Flips the production funnel — validate creative before paying for humans.

**Owned creator IP.** Real creators leave, raise rates, get canceled. A locked persona is yours forever. 500 ads, same face, zero talent cost.

---

## References

- `references/prompt-templates/` — one template per use case, copy-paste ready
- `references/emotion-muscle-library.md` — emotion → muscle movement translation table
- `references/creator-persona-builder.md` — how to generate + maintain consistent AI creators
- `references/localization-playbook.md` — ad translation full workflow
- `references/model-selection.md` — when to use Kling / Enhancor V4 / Veo instead
- `references/examples.md` — Sirio Berati's original 6 Seedance V2 demos as ground-truth reference

---

## Depends On

- `seedance-prompting` — base Seedance prompting rules, timecoded shot construction
- `nano-banana-pro` — persona + product image generation
- `ai-avatar-realistic` — photorealistic avatar guidelines
- `human-copy-standards` — script quality gate

---

_Owner: Michael | Source: Sirio Berati × Greg Isenberg Seedance V2 walkthrough, 2026-04-17_
