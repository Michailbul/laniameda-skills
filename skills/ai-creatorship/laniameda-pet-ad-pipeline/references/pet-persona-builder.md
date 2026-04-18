# Pet Persona Builder

**Goal:** Lock a consistent AI pet identity once, reuse across 100s of ads.

A pet persona is not just a breed. It's a bundle: species, breed, exact coat pattern, size, distinguishing markings, eye color, age appearance, signature gestures. Every ad variant references the same bundle.

---

## Why This Matters More Than Human Personas

Pet coats are **the hardest thing to keep consistent.** Vision models simplify patterns aggressively:
- Brindle → solid brown
- Calico → gray mix
- Merle → messy blur
- Tortie → dark patches
- Tabby → generic striped

Without a locked reference image, every variant looks like a different animal of the same breed — which is the UGC equivalent of casting a different human creator mid-ad.

A locked pet persona is the single biggest lever you have.

---

## When to Build a New Pet Persona

Build when:
- Starting a new brand that needs its own pet hero
- A brand wants breed diversity (build one persona per target breed — don't try to make one pet work for "dog owners")
- The existing persona has drifted or no longer fits the brand vibe

Do not build when:
- An existing persona fits — reuse it
- You're just running a language/geographic variant (reuse the pet)
- The ad is about a human reviewing a pet product (use `laniameda-ugc-ad-pipeline` instead — human as hero)

---

## Pet Persona Generation Workflow

### Step 1 — Brief

Fill in this template before generating:

```
PET PERSONA BRIEF
=================
Species: [dog / cat / rabbit / bird / other]
Breed (or mix): [specific — "Australian Shepherd" not "medium dog"]
Size: [toy / small / medium / large / giant]
Age appearance: [puppy/kitten / young adult / adult / senior]
Coat pattern: [specific — "red merle with white chest blaze and one blue eye, one brown eye"]
Coat length: [short / medium / long / double coat]
Distinguishing features: [specific marking, scar, unusual color — give the pet identity]
Eye color: [specific — "one brown, one blue" or "green" or "gold with dark rims"]
Vibe: [3 adjectives — playful / gentle / dignified / goofy / serious / zoomie-prone]
Signature behavior: [one physical tell — e.g. head tilt on command, always lifts left paw]
Setting default: [bright kitchen / cozy couch / outdoor yard / minimal studio]
Avoid: [features to exclude — too show-dog-groomed, costume-y, cartoonish]
```

### Step 2 — Generate base image via Nano Banana Pro

Use a prompt that produces a clear, well-lit, neutral-posture portrait. This is the ground truth for all future generations.

Reference prompt pattern (copy and adapt):

```
Photorealistic full-body portrait of an Australian Shepherd, medium size, young adult
(~3 years old). Red merle coat with distinct mottled pattern of red, cream, and darker
patches; white chest blaze extending to front paws; one blue eye, one brown eye; medium
feathered coat; natural alert ear position (semi-erect, not cropped); plume tail at
medium height. Standing on grass in soft outdoor light, late afternoon, natural lighting
from camera-left. Neutral alert expression, mouth closed. Shot at dog-eye level, 50mm
equivalent, shallow depth of field, background is softly blurred garden. Natural anatomy:
four legs total, correct joint angles, natural tail carriage. Looks like a real family
pet, not a show dog or stock photo.
```

Generate 3-5 variants. Pick the one with the **most specific and distinctive coat pattern** — not the "prettiest." Prettiest tends to be genericized. Distinctive holds up across variants.

### Step 3 — Pet Character Sheet

From the locked image, build the character sheet. Save as `persona/pet-meta.json`:

```json
{
  "pet_persona_id": "pet-ugc-001",
  "name_internal": "Juno",
  "species": "dog",
  "breed": "Australian Shepherd",
  "age_appearance": "young adult, ~3 years",
  "size": "medium (~50lbs equivalent framing)",
  "coat": {
    "pattern": "red merle",
    "description": "mottled red, cream, and darker brown patches; white chest blaze from throat to front paws; darker muzzle mask; lighter underbelly",
    "length": "medium, lightly feathered",
    "distinguishing": "white sock on left front paw only; small white tail tip"
  },
  "features": {
    "eyes": "heterochromia — left eye blue, right eye brown",
    "ears": "semi-erect, natural (not cropped)",
    "tail": "plume tail, carried at mid-height",
    "build": "athletic, standard for breed"
  },
  "personality_descriptors": ["alert", "playful", "intelligent"],
  "signature_behaviors": {
    "primary": "head tilts to the right with ears forward when curious",
    "secondary": ["lifts left paw when waiting", "slow blink before settling"]
  },
  "motion_notes": {
    "gait": "light athletic trot, signature for herding breeds",
    "sit_posture": "upright and attentive, not slumped",
    "resting": "side-lie with legs extended forward"
  },
  "setting_defaults": {
    "location": "bright home kitchen or outdoor grass yard",
    "lighting": "natural window or afternoon outdoor sun",
    "background": "slightly blurred, warm and clean"
  },
  "source_image": "persona/pet.png",
  "variant_images": [
    "persona/variants/side-profile.png",
    "persona/variants/lying-down.png",
    "persona/variants/looking-up.png",
    "persona/variants/mouth-open-panting.png"
  ],
  "created": "YYYY-MM-DD",
  "used_in_campaigns": []
}
```

### Step 4 — Generate Multi-Angle Reference Variants

Generate 4-6 additional images of the same pet in different poses, angles, and expressions. These become multi-image references when Seedance needs them.

Useful variants to pre-generate:
- Side profile standing
- Lying down / resting
- Looking up at camera (from above angle)
- Mouth open / panting (for reaction shots)
- Head tilt (for curious shots)
- Full body running / in motion

Save under `persona/variants/`.

### Step 5 — Save to laniameda-gallery

Tag the persona:
- Primary tag: `pet-persona`
- Secondary tags: species, breed, size, vibe, brand fit
- Asset type: `character-reference`

Use the `laniameda-gallery-ingest` skill to save properly.

---

## Consistency Rules

These keep the pet from drifting across generations.

- **Always reference `persona/pet.png` as image 1 in every Seedance prompt.** Never rely on breed description alone.
- **Lock coat phrasing in the prompt:**
  `"Pet identical to image 1: [coat pattern in 1 sentence], [distinguishing features], [eye color]. Do not alter markings or colors."`
- **Do not let the model "interpret" the coat.** If a generation simplifies the pattern (brindle → beige, calico → gray) — regenerate. Do not accept.
- **Anatomy lock every prompt:**
  `"Four legs total, two ears, one tail, natural anatomy, correct joint angles. No extra limbs."`
- **Size context can change per ad, breed cannot.** Explicit: `"[Breed] only — do not substitute breed features."`
- **Age can shift slightly for different ads (puppy → adult for a product that grows with them), but lock per campaign.**

---

## Testing Consistency

Before shipping a persona, run this check:

1. Generate 10 test clips with the pet in different scenes
2. Stack thumbnails side by side
3. If any thumbnail looks like a different animal → the persona isn't locked enough → regenerate the base image with more specific coat description → retest

Persona passes when all 10 thumbnails read as the same pet.

Extra-strict check for heavily-patterned coats (brindle, merle, calico, tortie): zoom into the coat on each variant. If the pattern's *distribution* (where the dark spots are) shifts materially, reject.

---

## Pet Persona Library Strategy

Don't build one persona and stop. Build a small library that covers common brand needs.

**Tier 1 personas (build first):**
- Small dog (e.g. French Bulldog or Pomeranian) — apartment pet brands
- Medium dog (e.g. Golden Retriever or Australian Shepherd) — family brands
- Large dog (e.g. German Shepherd or Labrador) — active/outdoor brands
- Short-hair cat (e.g. Tabby or Tortie)
- Long-hair cat (e.g. Maine Coon or Ragdoll)

5 personas cover ~80% of pet brand requests.

**Tier 2 personas (build on demand):**
- Senior dog (grey muzzle, slower vibe) — health/senior care brands
- Puppy — training / food brands targeting new owners
- Working dog (border collie, husky) — athletic brands
- Doodle mix (goldendoodle, labradoodle) — trending
- Exotic small pet (rabbit, guinea pig) — specialty brands

---

## Persona Lifecycle

- **Active** — currently in use across campaigns
- **Archived** — no longer used but kept for reference
- **Retired** — conversion dropped / brand moved on

Record status in `pet-meta.json`. Archive old personas to `~/work/laniameda/laniameda-hq/content-kb/pet-ads/_personas-archive/` after 90 days unused.

---

## Special Case: "The Real Pet"

Sometimes a brand has a real pet (founder's dog, mascot) and wants ads with *that* pet, not an AI pet.

Workflow:
1. Collect 15-20 reference photos of the real pet — multiple angles, lighting, poses
2. Use the best 5-6 as persona variant library
3. Use the clearest front-facing shot as `persona/pet.png`
4. Build the character sheet from the real pet's actual features
5. Lock the coat pattern from real photos (most accurate reference possible)
6. Generate variants via Seedance V2 with the real photo as image 1

This works better than most people expect — Seedance preserves real-pet identity well when given high-res reference.

---

_The pet persona is the most valuable asset in the pipeline. A good pet persona can power 500+ ads for years._
