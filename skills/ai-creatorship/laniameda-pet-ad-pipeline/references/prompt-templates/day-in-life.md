# Day-in-the-Life Template

**Use when:** subscription brands, premium food, wellness products, lifestyle pet brands. The arc is montage — multiple moments across a day stitched together to imply lifestyle value. Product appears throughout but naturally woven in.

**Inputs required:**
- Image 1: pet persona reference
- Image 2: hero product image
- Optional image 3+: additional product images if multiple SKUs featured

---

## Template

This is a multi-shot clip (3-4 scenes). Use Seedance V2 timecoded structure.

```
Multi-shot video generation, Seedance V2. Day-in-the-life montage.

SUBJECT: The [BREED] from image 1, exact same pet throughout all shots —
identical coat pattern, same features, same markings. Consistent lighting
and identity across all scenes.

PRODUCT: The [PRODUCT] from image 2, appears naturally in each scene where
relevant, preserving exact packaging, colors, branding. Does not dominate
the frame — fits into the lifestyle context.

SAME PET THROUGHOUT ALL SHOTS, same coat pattern, same eye color, same
markings every shot.

[0s] SCENE 1 — Morning wake-up
Pet in a cozy bed or on a couch, soft morning light filtering in. [BREED]
slowly wakes — eyes open, a full stretch (front legs extended, back arched,
yawn with full mouth). Product (food bag / treat / toy) partially visible
in background on a kitchen counter. Soft ambient morning sounds, slight
birdsong outside. Camera holds steady at pet eye level.

[3s] SCENE 2 — Mealtime / product moment
Transition cut. Pet now at food bowl in the kitchen. Owner's hand
(off-camera or in-frame) pours [PRODUCT] into bowl — visible product
interaction. Pet's nose drops into bowl, starts eating. Visible chewing,
occasional pause to look up with food still in mouth. Tail at mid-height
with slow wag. Camera at bowl-level, slightly over-the-shoulder of pet.

[6s] SCENE 3 — Activity / play
Transition cut. Pet running through grass outside OR playing with a toy
on the living room floor. Loose body language, full-arc tail, bright
eyes, mouth open in play face. Camera moves with pet — slight hand-held
motion. Warm natural light.

[9s] SCENE 4 — Rest / settle
Transition cut. Pet curled up in bed at end of day, soft evening light
or warm lamp glow. Eyes half-closed, slow breathing, deep relaxation.
Optional: product visible nearby (empty bowl, toy beside bed). Camera
slowly pushes in or holds steady.

VOICEOVER (off-camera narrator, throughout):
"[LINE 1, 0-3s — sets up the day]"
"[LINE 2, 3-6s — ties in the product naturally]"
"[LINE 3, 6-9s — the emotional payoff]"

TRANSITIONS: Soft cuts between scenes, not hard cuts. Optional cross-fade
if scene lighting differs significantly.

CAMERA STYLE: Consistent across scenes — same focal length, similar
framing logic, similar hand-held feel. The pet is the anchor, settings
change around them.

LIGHTING PROGRESSION: Morning (cool soft) → midday (warm bright) →
afternoon (golden) → evening (warm dim). Lighting tells the time-of-day
story.

AUDIO: Layered ambient sounds per scene (morning birdsong → kitchen
bowl-pour → outdoor grass rustle → evening quiet). Voiceover over all.
Optional soft instrumental music bed.

CONSISTENCY: Pet identical across all shots — coat, features, markings,
eye color must not change between scenes. Product identical when it
appears. Lighting natural and continuous within each scene but progresses
across the day.

ANATOMY LOCK: Four legs, two ears, one tail, natural anatomy in every
shot. Correct joint angles during stretching, running, and resting.

DURATION: ~10-12 seconds total (3-4 shots of 2-3s each).
```

---

## Swap points

- `[BREED]` — breed-variant generation
- `[PRODUCT]` — different SKUs can be featured in different scenes
- Scene count and specific moments
- Voiceover script
- Language of voiceover

Keep constant:
- 4-scene day arc (wake → mealtime → activity → rest)
- Pet identity across scenes (non-negotiable)
- Lighting progression logic

---

## Scene pattern libraries

Pick 3-4 scenes from this list to build the arc:

**Morning:**
- Wake-up with stretch
- First yawn of the day
- Morning water drink
- Window-looking at sunrise
- Greeting owner at door

**Meal:**
- Food bowl drop (from above angle)
- First bite / eating focus
- Finishing bowl (lick-clean)
- Treat moment (reward)
- Water drink with product bowl visible

**Activity:**
- Walk on leash (outdoor)
- Play with toy (indoor)
- Training moment (sit/stay/trick)
- Zoomies across room
- Fetch / chase / tug

**Rest:**
- Post-meal nap
- Afternoon sunbeam lie-down
- Evening curl-up
- Bedtime yawn
- Dreaming (paw twitches, ear flicks)

**Connection / owner:**
- Belly rub / head scratch
- Sitting at feet
- Looking up at owner
- Offering a paw
- Sleeping against leg

Combine: Morning + Meal + Activity + Rest is the classic. Morning + Connection + Activity + Rest is softer. Meal + Play + Cuddle + Rest is brand-friendly for premium food.

---

## Voiceover arc patterns

Voiceovers need to feel like the owner, not the brand. Run through `human-copy-standards`.

**Pattern 1 — the transformation:**
> "Before [product], mornings were a struggle. Now she wakes up ready.
> She eats every bite. She plays like she's four again.
> Something's working."

**Pattern 2 — the love letter:**
> "This is Juno. Three years old. Obsessed with tennis balls.
> He eats [product] because I can't keep up with the research and
> he seems to know what's good for him.
> I just make sure the bowl stays full."

**Pattern 3 — the skeptic:**
> "I tried everything before this. Kibble, freeze-dried, raw, fresh.
> She'd pick at it. I was this close to giving up.
> Then she finished a bowl for the first time in months."

**Pattern 4 — the simple truth:**
> "Good morning. Good food. Good walk. Good nap.
> That's the whole recipe."

---

## Failure watchouts

- **Pet identity drifts between scenes** — biggest failure mode. Always restate the coat pattern lock for each scene.
- **Lighting inconsistency** — pet is in warm light in scene 1 and cool light in scene 2 without a time-of-day explanation. Fix: explicitly name time of day for each scene and match lighting.
- **Transitions look abrupt** — add transition language: "soft cut to" / "dissolves into" / "continues to."
- **Product crammed into every frame** — ads feel forced. Fix: product prominent only in the meal/use scene, background elsewhere.
- **Voiceover timing mismatched** — voiceover is trying to deliver 20 words in 3 seconds. Fix: shorter copy per scene, allow breath between lines.
- **Multi-shot drift** — Seedance can drift character across shots. Fix: keep to 3-4 shots max, use strong identity lock language.

---

## Variation axes

**Narrative A/B:** same pet, same product, different voiceover arc (transformation vs love letter vs skeptic).
**Time of day axis:** morning-focused vs full-day vs evening-focused edit.
**Scene composition A/B:** kitchen-heavy vs outdoor-heavy scene balance.
**Voice style A/B:** male vs female vs non-binary narrator, different tones.
**Music bed A/B:** piano soft vs acoustic warm vs ambient electronic.

---

## Example — Day-in-the-life for premium dog food brand (worked structure)

Setup:
- Persona: Juno (Australian Shepherd)
- Product: premium fresh food subscription, branded packaging visible
- 4 scenes: wake / meal / play / rest
- Voiceover: the-simple-truth pattern

Scene-by-scene core:

```
[0s] Juno on his bed in morning light. Stretches front legs, yawns wide,
tail thumps once. Warm window light. Soft sound of a kitchen in background.

[3s] Juno at stainless steel bowl. Owner's hand pours [product] from
branded packaging — visible label, brand color. Juno's head drops in,
starts eating with visible chewing. Tail wag picks up.

[6s] Juno running through late-afternoon grass, ears back, mouth open in
play face, tail full-arc wag. Golden sunlight. Loose athletic motion.

[9s] Juno curled up on couch in warm evening lamp light. Eyes closed,
deep slow breathing, completely relaxed.
```

Voiceover: "Good morning. Good food. Good walk. Good nap. That's the whole recipe."

Why it works:
- Arc tells a full day without being too long
- Product appears naturally in the meal scene, not every scene
- Voiceover is short enough to breathe between lines
- Pet is the anchor; the lifestyle is implied around it
- Emotional payoff is the rest scene — the final relaxation is the "outcome"
