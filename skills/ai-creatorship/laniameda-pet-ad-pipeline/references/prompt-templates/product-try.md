# Product Fit Template (Wearables)

**Use when:** pet wearable products — collars, harnesses, leashes, apparel, cones, booties, bandanas, carriers. The ad has to show the product fits naturally AND the pet is comfortable in it.

**Inputs required:**
- Image 1: pet persona reference
- Image 2: product image (clean shot, on a neutral background ideally)
- Optional image 3: pet-wearing-product composite (via Nano Banana Pro)

---

## Template

```
Multi-input video generation, Seedance V2.

SUBJECT: The [BREED] from image 1, exact same pet — identical coat pattern,
same size, same features. Do not alter markings, colors, or proportions.

PRODUCT: The [COLLAR / HARNESS / APPAREL] from image 2, preserving exact
color, material, pattern, hardware, and branding. Product fits naturally
on the pet — correct size, correct position on the body, no floating
or clipping.

SETTING: [ENVIRONMENT: outdoor sidewalk morning / home entryway / grass
park / clean studio backdrop]. Setting should contextualize why the
product is being worn (a walk, a meeting, an adventure).

PRODUCT POSITIONING:
- [COLLAR: fits snugly around neck, buckle or D-ring visible, tag jingles
  with motion]
- [HARNESS: straps positioned correctly across chest and behind front
  legs, not riding up into armpits, padding visible if applicable]
- [APPAREL: lies flat on body with natural fabric drape, leg openings
  aligned, neck opening snug but not tight]
- [LEASH: clipped to collar/harness correctly, visible attachment point,
  hangs with natural weight]

BEAT 1 (Initial moment):
Pet wears the product in a natural resting or standing position. Body
language is relaxed — [LOOSE POSTURE: ears neutral, mouth soft, tail
at mid-height]. Product sits correctly on body.

BEAT 2 (Motion):
Pet moves naturally — [WALKS / TURNS HEAD / SHAKES OFF / SITS / TROTS
FORWARD]. Product moves with the body — fabric flexes, hardware jingles,
straps stay in correct position. No shifting or misalignment.

BEAT 3 (Micro-moment of comfort):
Pet shows a clear comfort signal: [SLOW BLINK / SHAKE-OFF SETTLES /
PAUSE TO LOOK AT CAMERA / RELAXED PANT]. Ears neutral or forward, body
loose, no sign of irritation.

CAMERA: Medium shot framing — full body or upper body including product.
Starts steady, optionally follows pet's motion. Shot at pet's eye level
or slightly above for a soft angle. 50mm equivalent lens.

LIGHTING: Clean natural light — outdoor morning or soft window — that
clearly shows the product's color, material texture, and any details.
No harsh shadows obscuring the product.

AUDIO: Light ambient sounds — [COLLAR/TAG JINGLE / LEASH CLIP / OUTDOOR
AMBIENT / ROOM TONE]. No music. Voiceover optional below.

VOICEOVER (optional, off-camera human narrator):
"[SHORT LINE — 5-10 words, e.g. 'Finally, a harness that doesn't rub.']"

CONSISTENCY: Pet identical to image 1 throughout. Product identical to
image 2 — color, material, hardware, and pattern unchanged throughout
motion. Product fit stays correct — does not slip, clip through, or
change size.

ANATOMY LOCK: Four legs total, two ears, one tail. Natural anatomy. No
extra limbs. Product does not clip through the pet's body or fur.

DURATION: ~6-8 seconds.
```

---

## Product-specific fit rules

### Collars

- Should sit just below the ears, above the shoulder blades
- 2-finger rule: not visibly too tight or too loose
- Buckle or D-ring visible from some angle
- Tags (if any) should hang naturally and jingle with motion
- Fix common AI fail: collars floating above fur — add "collar sits flat against fur, pressing into coat slightly, not floating."

### Harnesses

- Front strap across chest, not over throat
- Side straps behind front legs, not in armpits
- D-ring position on back (for most designs)
- Padding visible if applicable
- Fix common AI fail: straps crossing through the body — add "harness straps visible on surface of coat only, no strap passes through body."

### Apparel (sweaters, rain jackets, cooling vests)

- Neck opening snug but relaxed
- Leg openings aligned with front legs
- Back length appropriate for breed (longer for dachshunds, shorter for stocky breeds)
- Fabric drapes and wrinkles naturally with motion
- Fix common AI fail: apparel looks painted-on or rigid — add "fabric moves naturally with pet's motion, has realistic drape and subtle wrinkles."

### Leashes

- Clipped to attachment point (collar D-ring or harness back)
- Hangs with gravity — slight sag between clip and human hand
- Moves naturally as pet walks
- Fix common AI fail: leash floating or going through pet's body — add "leash has natural weight and drape, clipped correctly, does not pass through body."

### Booties / Paw Protection

- Fit snugly over paw without compressing toes
- Visible velcro or closure
- All four (or wear only on affected paws if narrative)
- Fix common AI fail: booties fall off or look wrong — add "booties snug on paws, visible straps, pet walks normally with correct gait."

### Cones / Recovery Collars

- Positioned around neck, blocks face access
- Pet wears with a mix of acceptance and slight awkwardness
- Natural resignation body language
- Comedic potential — lean in if tonally appropriate

---

## Swap points

- `[BREED]` — breed-variant testing
- `[ENVIRONMENT]` — setting
- Product type and position details (match template to product)
- Motion beat (walk / turn / sit / etc.)
- Voiceover line

Keep constant:
- Fit rules for that product category
- Comfort signal beat
- Consistency + anatomy locks

---

## Failure watchouts

- **Product floats above fur** — biggest common failure. Always add "product presses into fur/coat, sits flat against body, not floating."
- **Straps pass through body** — anatomical violation. Add "all straps visible on surface only, no clipping through body."
- **Product color shifts** — common with complex patterns. Higher-res image 2, restate pattern explicitly.
- **Product changes size mid-clip** — add "product maintains exact size and proportions throughout motion."
- **Fit looks uncomfortable** — remove ear-back, tail-tuck body language cues if the goal is comfort. Use neutral or relaxed postures.
- **Hardware (buckles, D-rings) morphs or disappears** — explicitly name hardware in prompt.

---

## Variation axes

**Color A/B:** same pet, same style, different product colors — brand variant testing.
**Size A/B:** same product across different breeds — sizing demonstration.
**Context A/B:** same product, different environments — urban walk, park, hike, home.
**Comfort demonstration A/B:** static wear vs active motion — show the product holds up.
**Multi-pet A/B:** same product on different breeds — sizing proof across sizes.

---

## Hooks that work for pet wearables

Voiceovers, run through `human-copy-standards`:

- "Finally, a harness that doesn't rub."
- "She actually let me put it on without drama. Progress."
- "Day 1 vs Day 30. Still holding."
- "He walks differently with it. In a good way."
- "Adjustable. Waterproof. Not chewable. Three for three."

Avoid:
- "The perfect accessory for your pet" (generic)
- "Premium quality and style" (corporate)
- "Your pup will look adorable" (AI-speak)

---

## Special case: Cones of shame

High-comedy territory. Lean into the awkwardness honestly.

Body language:
- Slight slump in posture (not dramatic — real)
- Ears back or neutral, not pricked
- Walks with wider stance to compensate for vision
- Occasional bumping into furniture (add as beat if tonally appropriate)
- Sad-eye moment (one slow blink at camera)

Voiceover patterns:
- "Day 3. Still bitter."
- "He's coping."
- "Surgery went well. The ego is struggling."

Cone ads convert on honesty, not slick marketing.

---

## Example — Harness product try (worked)

Setup:
- Persona: Australian Shepherd, Juno
- Product: lightweight padded harness, navy with reflective strips
- Setting: morning sidewalk, cool light

Prompt core:
> Juno stands on a concrete sidewalk in morning light wearing the navy
> harness. Front strap sits correctly across chest, not over throat.
> Side straps sit behind front legs, clear of armpits. Padded chest piece
> presses into his fur. Reflective strips visible on side panels. Juno
> takes three natural walking steps forward, harness moves with his body —
> straps stay in position, fabric flexes with motion. D-ring on back
> visible. Pauses, shakes his head once, ears settle. Slow blink at camera.
> Neutral relaxed body language throughout — no pulling or tugging at the
> harness.

Voiceover: "Finally, a harness that doesn't rub."

Why it works:
- Product fit is explicit and correct (straps in right position)
- Motion shows the product in use
- Comfort signal (shake settles, slow blink) sells "doesn't rub"
- Voiceover earns the claim by showing the proof
