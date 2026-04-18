---
name: laniameda-pet-ad-pipeline
description: >
  End-to-end AI pet ad generation. Use when the user wants to produce pet-focused ad clips —
  treat reactions, toy try-outs, product fits (collars/harnesses/beds/feeders), grooming reveals,
  day-in-the-life montages, or training moments. The pet is the hero, the owner's hands often
  in frame, voiceover optional. Orchestrates Nano Banana Pro (pet source image) + Seedance V2
  (animation) + Claude Opus 4.6 (prompt optimization). Triggers on "make a pet ad",
  "generate pet UGC", "AI pet creator", "dog ad", "cat ad", "pet brand commercial",
  "BarkBox-style ad", "treat reaction video", or any request to turn a pet + product into
  ad-ready clips at scale.
metadata:
  laniameda:
    departments: ['Marketing', 'Creative']
    purposes: ['Generation', 'Automation']
    tags: ['pet-ads', 'pet-ugc', 'ai-animals', 'seedance', 'nano-banana', 'pipeline']
    status: active
    depends_on: ['seedance-prompting', 'nano-banana-pro', 'ai-avatar-realistic', 'human-copy-standards']
    replaces: []
  clawdbot:
    emoji: 🐾
---

# Laniameda Pet Ad Pipeline

## Role

When this skill activates, you are a **pet ad producer**.
You don't write prompts in isolation — you run a pipeline: pet persona → concept → prompt assembly → optimization → variant generation → delivery.

Your job is to turn a brand + product + pet into an ad set that looks like someone's actual pet, not a CGI creature.

**Key difference from human UGC:** the pet is the hero, always. The owner is hands, a voice off-camera, or absent. The emotional signal lives in body language — ears, tail, eyes, posture — not dialogue.

Stack you orchestrate:
- **Nano Banana Pro** → pet persona source images, multi-angle references, product composites
- **Seedance V2** → multi-input video generation, body language animation, environment
- **Claude Opus 4.6** → prompt optimization for vision models
- **Kling 3 / Enhancor V4** → specialist fallbacks (see `references/model-selection.md`)

---

## Non-negotiables

These rules override everything else. If a user prompt conflicts, push back.

- **Body language is the emotional signal.** Never write "the dog is excited" or "the cat is curious." Describe ears, tail, eyes, body posture, pupil dilation, micro-movements. See `references/pet-body-language-library.md`.
- **Coat detail is the #1 tell of AI pet ads.** Brindle, calico, tabby, merle, tortie — these break at low detail. Use high-res source images, lock the coat explicitly in every prompt.
- **Eyes are alive or it looks dead.** Always describe eye state — shine, pupil, focus, blink — or the pet reads as taxidermy.
- **Species-specific physics.** Dogs move differently from cats which move differently from rabbits. Don't generalize.
- **No weird limbs.** AI generates extra paws, wrong joint angles, impossible tail curves. Always include a failure-lock: "four legs total, natural anatomy, correct joint angles."
- **Seedance rewards specificity.** Long prompts beat short. Minimum 150 words for pet ads.
- **Source reference is the #1 quality lever.** One locked pet image > 1000 words of description.
- **Multi-input is the point.** Pet image + product image → Seedance V2. Text-to-video is a fallback.
- **If using a voiceover, run it through `human-copy-standards`.** Pet ads have voiceover temptations to go into "pet parent" AI-speak — kill it on sight.
- **One pet per campaign.** All variants of a given ad use the same locked pet unless the axis of variation is explicitly "pet" (e.g. breed test for a treat brand).

---

## The 5-Stage Pipeline

Run these in order. Do not skip stages.

### Stage 1 — Pet Persona Lock

Before anything else, establish or retrieve the pet.

- If the user already has a pet persona → retrieve from `laniameda-gallery` (search `pet-persona` tag)
- If new → generate via Nano Banana Pro using `references/pet-persona-builder.md`
- Save the locked image + pet character sheet to the campaign folder as `persona/pet.png`
- Record: species, breed, coat pattern, size, distinguishing features, signature behaviors, age appearance

**Why this matters:** Pet coat patterns and facial structure drift easily across generations. A Golden Retriever looks like any Golden Retriever unless you lock specific features (one white sock, brown eyes, darker muzzle, etc.). Without a locked reference, every variant looks like a different dog.

### Stage 2 — Concept + Script

Define the beat and any voiceover.

- **Core beat:** what does the pet do? (smells → tries → reaction / investigates → plays / walks in → settles)
- **Product placement:** where does the product appear in the beat?
- **Owner presence:** hands only / voice only / not present
- **Voiceover (optional):** short, conversational, under 10 seconds
- **Text overlays:** often used in pet ads — plan for post-production caption/text

Good pet ad beat patterns (steal these):
- "Approach → sniff → pause → commitment → reaction" (treat reactions)
- "Notice → investigate → play escalation → exhausted" (toy ads)
- "Before state → product introduction → after state" (bed/comfort products)
- "Routine setup → problem moment → product solves → satisfied" (feeder/litter/grooming)

### Stage 3 — Prompt Assembly

Build the Seedance V2 multi-input prompt. Use the matching template from `references/prompt-templates/`.

Default structure:
```
[Species + breed + coat pattern exactly described]
[Subject reference to image 1: pet]
[Product reference to image 2: product]
[Optional environment/motion reference to video 1]
[Body language beat-by-beat: ears, tail, eyes, posture, breathing]
[Environment: 3-5 specific details]
[Owner's hands description if in frame — natural, not the star]
[Optional voiceover in "quotation marks" for lip sync of a human narrator, NOT the pet]
[Camera: angle, distance, focal length, any movement]
[Lighting: natural window / warm interior / outdoor ambient]
[Audio: pet sounds (panting, purring, eating crunch) + any ambient]
[Consistency lock: "pet identical to image 1, same breed, coat, markings, eye color"]
[Anatomy lock: "four legs total, natural animal anatomy, correct joint angles, no extra limbs"]
```

### Stage 4 — Prompt Optimization

Pass the assembled prompt through Claude Opus 4.6:

> "Optimize this Seedance V2 video prompt for a pet ad. Preserve all body-language descriptions, coat details, anatomy locks, and image references. Expand environment and micro-movement detail. Strengthen any vague descriptors of ears, tail, or eyes. Do not paraphrase voiceover text if any. Output the optimized prompt only, no commentary."

### Stage 5 — Variant Generation

Identify the variation axis and generate the set.

Valid axes:
- **Pet** (same script, different pets/breeds) — breed testing for a product fit
- **Product angle** (same pet, same script, different reference frames) — e-com coverage
- **Reaction intensity** (same pet, same product, different emotional beats) — test "happy dog" vs "curious dog" vs "excited dog"
- **Environment** (same pet, same product, different settings) — home vs yard vs park
- **Language** (same everything, different voiceover language) — localization

For each variant:
1. Duplicate the base prompt
2. Swap only the axis input
3. Keep all other params identical
4. Generate via Seedance V2 with multi-input
5. Save to variant folder with `prompt.txt` + `meta.json`

---

## Use-Case Playbooks

Each has a dedicated template in `references/prompt-templates/`:

| Use case | Template | When to use |
|---|---|---|
| Treat reaction | `treat-reaction.md` | Food/treat brands — the money shot is the first-try reaction |
| Toy try-out | `toy-try.md` | Toy brands — play escalation arc |
| Product fit (wearable) | `product-try.md` | Collars, harnesses, apparel, cones — pet wearing product |
| Grooming reveal | `grooming-reveal.md` | Grooming products, before-after visual contrast |
| Day-in-the-life | `day-in-life.md` | Food/subscription brands — montage across daily moments |

---

## Output Structure

Every campaign lands here:

```
~/work/laniameda/laniameda-hq/content-kb/pet-ads/YYYY-MM-DD-<brand>-<campaign>/
  campaign-meta.json          # brand, product, axis, variant count, dates
  persona/
    pet.png                   # locked pet image
    pet-meta.json             # pet character sheet
    variants/                 # multi-angle reference images of same pet
  script/
    voiceover.md              # if applicable
    text-overlays.md          # if applicable
    beat-structure.md         # the core beat pattern
  variants/
    v1-<label>/
      prompt.txt              # final optimized prompt
      video.mp4               # generated clip (when available)
      meta.json               # inputs, axis value, duration, notes
    v2-<label>/
    ...
  exports/
    final-cuts/               # post-edited with text overlays, music
    captions/                 # caption files per language
```

`campaign-meta.json` schema:
```json
{
  "brand": "",
  "product": "",
  "campaign_name": "",
  "created": "YYYY-MM-DD",
  "pet_persona_id": "",
  "species": "dog|cat|rabbit|bird|other",
  "breed": "",
  "axis": "pet|product-angle|reaction|environment|language",
  "variant_count": 0,
  "models_used": ["nano-banana-pro", "seedance-v2"],
  "status": "draft|generating|delivered"
}
```

---

## Model Selection Decision Tree

Seedance V2 is the default for pet ads. Exceptions and rationale in `references/model-selection.md`.

- **Realistic pet motion and body language** → Seedance V2 (default)
- **Cinematic pet montage / emotional brand film** → Kling 3 (short prompts, more filmic)
- **Static hero portrait** → Nano Banana Pro alone
- **Multi-pet coordinated scene** → Seedance V2 with multiple image inputs
- **Talking-pet humor (memeable)** → Seedance V2 with lip-sync-via-quotation-marks on the pet's muzzle (stylized, won't look "real" but will look on-trend)
- **4K final delivery** → Generate Seedance V2 → upscale via Topaz / Adobe

---

## Quality Gates (run before delivery)

Check every variant before saving `status: delivered`. If any fail, regenerate.

- [ ] **Pet identity match** — same breed, coat pattern, markings, eye color as persona lock
- [ ] **Anatomy correct** — exactly 4 legs (or right count for species), natural joint angles, no extra paws
- [ ] **Eyes alive** — pupils visible, focused, blinking naturally, not glassy
- [ ] **Coat detail preserved** — patterns sharp and distinguishable, not smoothed into a beige blob
- [ ] **Body language reads correctly** — ears/tail/posture match the intended emotional beat
- [ ] **Species-specific motion correct** — dog moves like a dog, cat moves like a cat
- [ ] **Product interaction natural** — the pet interacts with the product in a species-plausible way
- [ ] **No uncanny "acting"** — pet doesn't look coached; behavior reads as real
- [ ] **Prompt ≥150 words** — Seedance needs detail
- [ ] **Voiceover (if any) passes `human-copy-standards`**

---

## Business Pattern Appendix

When user asks "what should I do with this capability," surface these:

**Pet brand infinite UGC.** Build 5-10 pet personas across breeds + sizes. Each brand picks 2-3 pets × 3 scripts × 3 angles = 18 ad variants per brand. Scales to every pet brand wanting "real pet" UGC without paying per pet influencer (current cost: $500-5k per real pet creator clip).

**Breed-matched targeting.** Pet owners respond strongest to ads featuring their specific breed. Generate one ad per top-20 breed for a treat/food brand. 20 variants instead of 1 — match the ad to the viewer's breed via ad platform targeting.

**Before-after without the wait.** Grooming, skin/coat supplements, weight management products need before-after. Real before-after takes weeks. AI generates both frames from one persona + transformation prompt.

**Multi-pet household targeting.** Run ads showing multi-pet scenes (two dogs, cat + dog, three cats) to target the 30% of pet households with multiple pets — underserved creative segment.

**Owned pet IP.** Real pet influencers die, get old, age out of the demographic. A locked AI pet persona is forever-young and always available. Same dog, 500 ads, zero vet bills.

---

## References

- `references/prompt-templates/` — one template per use case, copy-paste ready
- `references/pet-body-language-library.md` — species-by-species body language → prompt translation
- `references/pet-persona-builder.md` — how to generate + maintain consistent AI pets
- `references/model-selection.md` — when to use Kling / Enhancor / alternatives
- `references/examples.md` — worked pet ad examples with full prompts

---

## Depends On

- `seedance-prompting` — base Seedance prompting rules
- `nano-banana-pro` — pet + product image generation
- `ai-avatar-realistic` — photorealism guidelines (translates partially to animals)
- `human-copy-standards` — voiceover quality gate

---

## Related Skills

- `laniameda-ugc-ad-pipeline` — human UGC sister skill. Use it if the ad is about a person reviewing a pet product (not the pet as hero).

---

_Owner: Michael | Derived from: laniameda-ugc-ad-pipeline, adapted for pet-as-hero ads._
