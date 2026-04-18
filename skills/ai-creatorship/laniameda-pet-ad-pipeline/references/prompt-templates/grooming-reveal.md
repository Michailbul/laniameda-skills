# Grooming Reveal Template

**Use when:** grooming brands, coat/skin supplements, shampoos, dematting tools, bathing products, dental chews. The money shot is the before-after contrast — visible transformation.

**Inputs required:**
- Image 1: pet persona reference (base — the "after" version)
- Image 2: "before" state reference (same pet, but matted/dirty/dull coat — can be generated via Nano Banana Pro by modifying persona)
- Image 3: product image

---

## Template — Two approaches

### Approach A: Split-screen / same frame before-after

```
Multi-input video generation, Seedance V2.

SUBJECT: The [BREED] from image 1, exact same pet — identical breed,
size, features, eye color. The before state (image 2) and after state
(image 1) are the SAME PET, only coat/skin/teeth/nails differ.

LEFT HALF OF FRAME (BEFORE):
Pet as shown in image 2 — [COAT STATE: matted / dull / dry / tangled /
yellowed teeth / overgrown nails / skin redness]. Body language
slightly less animated — softer ears, less bright eyes.

RIGHT HALF OF FRAME (AFTER):
Same pet as image 1 — [COAT STATE: clean, shiny, fluffy, bright,
pearl-white teeth, trimmed nails, calm skin]. Body language brighter
— pricked ears, bright shine in eyes, tail held with more energy.

TRANSITION: Soft vertical wipe from before to after over 2 seconds,
OR hold split-screen throughout clip with subtle motion on both sides.

CONSISTENCY: Same breed, same coat pattern (just different condition),
same eye color, same anatomy. Only the grooming state differs.

ANATOMY LOCK: Four legs total, two ears, one tail. Both states anatomically
correct.

DURATION: ~5-7 seconds.
```

### Approach B: Time-lapse transformation

```
Multi-shot video generation, Seedance V2.

SAME PET THROUGHOUT ALL SHOTS. [BREED] from image 1, same coat pattern
in all states, only grooming condition changes across shots.

[0s] SCENE 1 — BEFORE STATE
Pet sits with [COAT STATE: matted, dull, tangled]. Neutral body language,
slight low-energy — head resting, softer ears. Medium shot, natural
lighting.

[3s] SCENE 2 — TRANSITION / PRODUCT USE
Product from image 3 is applied — [BRUSHING WITH TOOL / BATH SCENE /
SUPPLEMENT SCOOP INTO FOOD]. Brief 2-second demonstration. Pet tolerates
calmly — ears neutral, occasional blink, no distress.

[6s] SCENE 3 — AFTER STATE
Pet now visually transformed — [COAT STATE: clean, shiny, fluffy,
healthy]. Body language upgraded — pricked ears, bright eyes, energetic
tail wag, possibly a small head shake or full-body shake that shows
off the new coat movement. Medium shot, same framing as before.

VOICEOVER:
"[LINE 1, 0-3s — the problem]"
"[LINE 2, 3-6s — the solution naturally introduced]"
"[LINE 3, 6-9s — the payoff]"

CONSISTENCY: Same pet identity across all three scenes. Coat pattern
markings (e.g. specific white patches, merle distribution) identical
across all scenes — only coat condition changes.

ANATOMY LOCK: Four legs, two ears, one tail, natural anatomy in every shot.

DURATION: ~9 seconds.
```

---

## Grooming-specific rules

### Coat before-after

**Dull / matted coat (before):**
- Fur lays flat and close to body, clumped in places
- No visible shine — flat matte appearance
- Slight tangle/mat visible especially around ears, tail, chest
- Color reads darker/grayer than healthy
- Body language: slightly less alert

**Healthy coat (after):**
- Fur has visible shine and depth
- Slight volume — not pressed flat
- Pattern markings clearly visible and vibrant
- Light catches the coat differently — highlights and shadows
- Body language: more alert, tail carriage higher

### Teeth before-after

**Yellowed teeth (before):**
- Visible plaque/tartar, yellow-brown discoloration
- Slightly swollen gums possible
- Bad-breath implication (no visual, but subject gestures — not licking too close)

**Clean teeth (after):**
- White teeth, visible enamel shine
- Healthy pink gums
- Comfortable mouth opening — jaw relaxed

### Nails before-after

**Overgrown (before):**
- Nails curl past paw pad
- Click-click sound on hard floor (audio cue)
- Slightly uncomfortable walking posture

**Trimmed (after):**
- Nails just clear of the floor
- Clean walking gait
- Silent paws on hard surface

### Skin before-after

**Irritated (before):**
- Visible pink/red patches
- Hot spots or thinning fur
- Pet licking or scratching

**Calm (after):**
- Even skin tone
- Full coat coverage
- No scratching/licking

---

## Common failure modes

- **The "before" pet looks like a different dog** — biggest failure. You need image 2 to be the SAME pet with different coat condition. If you don't have this, regenerate via Nano Banana Pro using the main persona with modified coat.
- **Transformation too dramatic to be believable** — looks fake. Real grooming results are visible but not miraculous. Tone it down if the before is too extreme.
- **Body language doesn't shift** — the "after" state should have slightly more alert/happy body language as emotional proof.
- **Markings change between before and after** — the coat pattern (white patches, merle distribution) must be identical. Only condition changes.
- **Product use is glossed over** — give the product its moment in the transition scene. Show the brush/bath/scoop clearly.

---

## Swap points

- `[BREED]` — breed variants
- `[COAT STATE before / after]` — condition specifics
- `[PRODUCT USE in transition]` — demonstration type
- Voiceover
- Split-screen vs time-lapse approach

Keep constant:
- Same pet identity across all states
- Transformation is believable (not miraculous)
- Body language improves with grooming state

---

## Variation axes

**Transformation axis A/B:** coat focus vs teeth focus vs skin focus vs nail focus — test which pain point converts best.
**Severity A/B:** mild before vs severe before — test emotional pull.
**Time frame A/B:** "1 week" vs "30 days" vs "6 months" text overlay — different commitment asks.
**Format A/B:** split-screen vs time-lapse — different feeds may favor different formats.

---

## Hooks for grooming / coat products

Run through `human-copy-standards`. Honesty converts.

- "Three weeks ago vs today. Same dog."
- "I finally figured out what was causing the itching."
- "The shedding was driving me insane. Past tense."
- "Vet said it would take time. It took two weeks."
- "He's not a different dog. Just a comfortable one."

Avoid:
- "Transform your pup today!" (corporate + AI-speak)
- "Miracle results in days!" (hyperbolic, triggers skepticism)
- "The secret every pet parent needs to know" (clickbait cliche)

---

## Example — Coat transformation (worked)

Setup:
- Persona: Juno, red merle Australian Shepherd
- Before image: Juno with dull, slightly matted coat (generated from persona via Nano Banana Pro — same markings, worse condition)
- After image: Juno with shiny, full coat (the standard persona)
- Product: omega-3 supplement for dogs

Prompt core (time-lapse approach):

```
[0s] Juno sits on kitchen floor. Coat slightly dull, fur lays flat, one
small tangle visible on chest. Ears soft, eyes quiet. Side lighting.

[3s] Human hand appears in frame with supplement scoop from branded
container. Pours scoop into Juno's food bowl. Juno eats from bowl, chewing
visible. Subtle product branding visible on container.

[6s] Juno stands in same kitchen, same framing. Coat full and shiny,
red merle pattern vibrant, white chest blaze bright. Ears pricked,
bright eyes with visible catchlight. Small head shake — coat bounces
with the motion. Single slow blink at camera.
```

Voiceover:
- "Three weeks ago, Juno's coat was getting duller every month."
- "Our vet recommended omega-3s. We tried [brand] because the ingredients are short."
- "Same dog. Better coat."

Why it works:
- Same pet identity across states (critical)
- Transformation is visible but realistic
- Product use gets its own beat — not rushed
- Body language improves subtly (ears pricked, eyes brighter) — the emotional proof
- Voiceover is honest, specific, short
