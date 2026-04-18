# Creator Persona Builder

**Goal:** Lock a consistent AI creator identity once, reuse across 100s of ads.

A persona is not just a face. It's a bundle: face, body proportions, voice style, vibe, signature gestures, wardrobe defaults. Every ad variant references the same bundle.

---

## When to Build a New Persona

Build when:
- Starting a new brand account that needs its own creator face
- A brand wants demographic diversity (build one persona per demo, not one that tries to be all)
- Existing persona has drifted or is no longer converting

Do not build when:
- You already have a persona that fits the brand vibe — reuse it
- You're just translating an existing ad (use the existing creator or swap only the language axis)

---

## Persona Generation Workflow

### Step 1 — Brief

Fill in this template before generating:

```
PERSONA BRIEF
=============
Target demographic: [age range, gender, region]
Brand vibes: [3 adjectives — e.g. warm, casual, unpretentious]
Voice style: [conversational / confident / nerdy / chill / fast-talker]
Signature gesture: [one physical tell — e.g. tucks hair behind ear before speaking]
Wardrobe default: [casual t-shirt / athleisure / streetwear / minimal / etc.]
Setting default: [kitchen / bedroom with soft lighting / outdoor / car / etc.]
Lighting default: [natural window / ring light / golden hour / etc.]
Avoid: [list any features to exclude — too polished, heavy makeup, commercial look]
```

### Step 2 — Generate base image via Nano Banana Pro

Use a prompt that produces a flat, well-lit, neutral-expression portrait. This is the ground truth for all future generations.

Reference prompt pattern (copy and adapt):

```
Photorealistic portrait of [demographic] woman, late 20s, [ethnicity], warm skin tone,
natural light from window camera-left, neutral closed-lip expression, direct eye contact
with camera, head and shoulders framing, wearing [wardrobe default], background is
slightly blurred [setting default], shot on 50mm lens at f/2.8, film grain minimal,
no heavy retouching, no makeup heavier than a natural daily look. Image should read
as a real person, not a stock photo or a commercial model.
```

Generate 3-5 variants. Pick the one that feels most like a real person, not the most beautiful one.

### Step 3 — Character Sheet

From the locked image, build the character sheet. Save as `persona/creator-meta.json`:

```json
{
  "persona_id": "lani-ugc-001",
  "name_internal": "Maya",
  "demographic": {
    "age_range": "26-30",
    "ethnicity": "mixed Latina",
    "gender": "female"
  },
  "appearance": {
    "hair": "dark brown, shoulder length, naturally wavy",
    "eyes": "hazel brown",
    "skin": "warm olive, slight freckles across nose",
    "build": "average, 5'6 equivalent framing",
    "wardrobe_default": "oversized cream knit sweater, minimal jewelry"
  },
  "voice": {
    "style": "conversational, warm, slight upspeak",
    "pace": "medium",
    "fillers": ["okay", "like", "huh", "I mean"],
    "signature_phrase": null
  },
  "gestures": {
    "signature": "tucks hair behind right ear before speaking",
    "secondary": ["brief glance down before verdict", "half-laugh between phrases"]
  },
  "setting_defaults": {
    "location": "home kitchen with warm pendant light",
    "lighting": "natural window + warm overhead, soft shadows",
    "time_of_day": "afternoon"
  },
  "source_image": "persona/creator.png",
  "variant_images": [
    "persona/variants/side-angle.png",
    "persona/variants/laughing.png"
  ],
  "created": "YYYY-MM-DD",
  "used_in_campaigns": []
}
```

### Step 4 — Generate Reference Variants

Generate 3-5 additional images of the same persona in different poses, expressions, and angles. These become multi-angle references when Seedance needs them.

Useful variants to pre-generate:
- 3/4 angle portrait
- Laughing / mouth open mid-expression
- Hand near face (gesture reference)
- Full body standing
- Product-holding pose (can be generic product)

Save under `persona/variants/`.

### Step 5 — Save to laniameda-gallery

Tag the persona so it's findable:
- Primary tag: `ugc-persona`
- Secondary tags: demographic, vibe, brand fit
- Asset type: `character-reference`

Use the `laniameda-gallery-ingest` skill to save properly.

---

## Consistency Rules

These keep the persona from drifting across 100s of generations.

- **Always reference `persona/creator.png` as image 1 in every Seedance prompt.** Never rely on text description alone.
- **Lock phrasing in the prompt:** `face identical to image 1, same person, same features, do not alter facial structure.`
- **Do not let the model "interpret" the persona.** If a generation drifts, regenerate — do not accept and move on.
- **Wardrobe can change per ad, face cannot.** Explicit: `different outfit from image 1, same face exactly.`
- **Lighting can change per ad, facial proportions cannot.** Explicit: `different lighting setup from image 1, same facial features.`

---

## Testing Consistency

Before shipping a persona, run this check:

1. Generate 10 test clips with the persona in different scenes
2. Stack thumbnails side by side
3. If any thumbnail looks like a different person → the persona isn't locked enough → regenerate the base image with more specificity → retest

Persona passes when all 10 thumbnails read as the same human.

---

## Persona Lifecycle

- **Active** — currently in use across campaigns
- **Archived** — no longer used but kept for reference (brand might return)
- **Retired** — conversion dropped / brand moved on / demographic mismatch

Record status in `creator-meta.json`. Archive old personas to `~/work/laniameda/laniameda-hq/content-kb/ugc-ads/_personas-archive/` after 90 days unused.

---

_The persona is the most valuable asset in the pipeline. Protect it like IP._
