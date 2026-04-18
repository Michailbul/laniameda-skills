# Treat Reaction Template

**Use when:** pet food or treat brand. The money shot is the first-bite reaction — the pause before, the commitment, the crunch, the satisfied body language after.

**Inputs required:**
- Image 1: pet persona reference
- Image 2: treat/food product image (bag, container, or loose treat visible)
- Optional image 3: owner's hand holding treat (if you want hand in frame)

---

## Template

```
Multi-input video generation, Seedance V2.

SUBJECT: The [BREED] from image 1, exact same pet — identical coat pattern
([SPECIFIC DESCRIPTION: e.g. "red merle with white chest blaze, one blue eye
one brown eye, white sock on left front paw"]), same size, same features.
Do not alter markings, colors, or eye color.

PRODUCT: The treat/food from image 2, preserving all packaging text, logo,
and color. If a single treat is visible, preserve its exact shape and color.

SETTING: [ENVIRONMENT: warm home kitchen with natural light / clean studio
backdrop / cozy living room with soft lighting]. Pet is sitting or standing
on [floor surface — hardwood, tile, soft rug] with natural alert posture.

ACTION: [OWNER'S HAND from off-camera OR visible in frame] extends a single
treat toward the pet at nose height, about 6 inches from the pet's face.

BEAT 1 (Approach):
Pet's nose extends forward, nostrils flare visibly for a sniff, ears rotate
forward and up, weight shifts onto front paws, tail held at mid-height with
slow wag. Pet holds position for one full second of investigation.

BEAT 2 (Commitment):
Pet takes the treat with a gentle mouth close — no snatching. Head pulls back
slightly as treat is taken. Eyes close for a brief half-blink on contact.

BEAT 3 (Enjoyment / Verdict):
Visible chewing motion — jaw working, ears relax into soft forward position,
eyes half-close in concentration, single slow blink. Tail wag picks up in
rhythm and width, loose body posture. Tongue flicks once over the nose
after swallowing.

CAMERA: Medium close-up, pet's head and front shoulders in frame, shot at
pet's eye level (low angle for a dog, slightly higher for a cat), 50mm
equivalent lens, slight hand-held feel but steady.

LIGHTING: Natural warm light from camera-left, soft fill from camera-right,
no harsh shadows on the pet's face. Coat pattern clearly legible, eyes catch
light with natural shine.

AUDIO: Audible crunch of the treat, soft panting before and after, ambient
kitchen/room tone, no music, no dialogue unless voiceover specified below.

VOICEOVER (optional, off-camera): A human voice softly says:
"[SHORT LINE — 5-8 words max, e.g. 'The only treat he actually waits for.']"
Delivered conversationally with a slight smile in the voice.

CONSISTENCY: Pet identical to image 1 throughout — coat, eyes, features,
markings unchanged. Product identical to image 2. Treat stays consistent
shape and color as it's taken.

ANATOMY LOCK: Four legs total, two ears, one tail, natural anatomy, correct
joint angles. No extra paws. No disfigured limbs.

DURATION: ~7-8 seconds.
```

---

## Swap points

- `[BREED]` and coat description — for breed-variant tests, regenerate persona but keep script
- `[ENVIRONMENT]` — setting
- `[OWNER'S HAND configuration]` — in frame vs off-camera
- Voiceover line (if used)
- Language of voiceover (localization)

Keep constant:
- Body language beat structure (sniff → commit → enjoy)
- Camera framing
- Anatomy + consistency locks

---

## Failure watchouts

- **Pet snatches instead of taking gently** — add "gentle mouth close, no snatching, head position steady during taking."
- **Extra paws appear** — strengthen anatomy lock: "exactly four legs visible throughout, no phantom limbs, no extra paws near the face."
- **Coat pattern simplifies** — add higher-res image 1, restate pattern explicitly, add "preserve all coat pattern detail, do not simplify markings."
- **Pet eyes look dead/glassy** — add "eyes bright with natural shine and visible catchlight, pupils focused on the treat, one blink during the clip."
- **Product label warps during hand motion** — use higher-res product image, add "product label sharp and legible throughout, does not warp or blur."
- **Reaction looks like "acting"** — remove any human-mapped emotion language. Stick to body-language facts (tail, ears, posture).

---

## Variation axes

**Breed A/B:** same product, same script, swap persona image. Test which breed converts best per segment.
**Environment A/B:** same pet, same product, different settings (kitchen vs outdoor vs couch).
**Treat variant A/B:** same pet, same script, different product image (flavor variants of the same line).
**Size A/B:** small treat vs large chew — adjust beat timing accordingly.
**Voiceover A/B:** same clip, swap the off-camera voiceover line to test hooks.

---

## Hook patterns that work for pet treats

For voiceovers, run these through `human-copy-standards` first. Kill anything that smells like "beloved fur baby" or "pawsitively."

- "The only treat he actually waits for."
- "Slow down, buddy. It's not going anywhere."
- "Day 47 of trying to get a non-blurry photo."
- "She went from 'meh' to 'more?' in three seconds."
- "Turns out he has a preferred flavor."
- "Three ingredients. That's it."

What to avoid:
- "Give your fur baby the love they deserve" (generic, AI-speak)
- "Pawsitively irresistible!" (pet-brand cliche)
- "Premium nutrition for your best friend" (corporate)

---

## Example — Treat reaction beat structure (worked)

Setup:
- Persona: Australian Shepherd, red merle, locked as Juno
- Product: single-ingredient salmon training treat
- Setting: kitchen tile floor, morning light

Prompt core:
> Juno sits on kitchen tile, alert but steady. A human hand extends a small
> salmon-colored treat at nose height. Juno's nostrils flare visibly as he
> sniffs — two short sniffs — then the ears rotate fully forward. He takes
> the treat with a soft mouth close, head pulling back a half-inch. Chews
> with visible jaw motion, eyes half-closing in focus. Single tongue flick
> across the nose. Tail wag picks up from mid-height to wide arc. Camera
> holds steady at dog-eye level, morning light from window.

Voiceover: "The only treat he actually waits for."

Why it works:
- Beats are specific and describable (sniff count, ear rotation, head pull-back)
- Body language tells the story, not the voiceover
- Voiceover is short, specific, and funny — earns its place
- Product is visible but not the star — the pet is
