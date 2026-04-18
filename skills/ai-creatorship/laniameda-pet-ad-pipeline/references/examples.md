# Worked Examples — Pet Ad Pipeline

Reference examples to model new campaigns on. Each example shows the full setup, prompt, voiceover, and why it works. Use them as pattern libraries, not templates to copy verbatim.

---

## Example 1 — Treat Brand: Single-Ingredient Reaction

**Brand:** indie single-ingredient treat company
**Product:** freeze-dried salmon bites, bag visible
**Persona:** Juno — Australian Shepherd, red merle, one blue eye one brown, white chest blaze
**Axis:** reaction (this one clip, designed to scale to breed variants)

**Prompt (post-optimization):**

```
Multi-input video generation, Seedance V2.

SUBJECT: The Australian Shepherd from image 1, exact same dog — red merle
coat with mottled red, cream, and darker brown patches; white chest blaze
extending from throat to front paws; one blue eye (left), one brown eye
(right); white sock on left front paw; medium feathered coat. Do not alter
markings, colors, or eye color. Same dog identity throughout.

PRODUCT: The bag of freeze-dried salmon treats from image 2, preserving
the exact label text, logo, and orange-cream packaging color. Single treat
visible in owner's hand — salmon-pink color, small rectangular shape,
matte texture. Product identical to image 2.

SETTING: Bright home kitchen, hardwood floor, morning light from window
camera-left. Slight blur in background shows kitchen counter and a second
stool. Clean, warm, not staged.

BEAT 1 (Approach, 0-2s):
Juno sits on hardwood floor in natural alert posture. A human hand enters
frame from camera-right holding a single salmon treat at his nose height,
about 6 inches away. Juno's nostrils flare visibly — two short sniffs,
audible. Ears rotate fully forward. Eyes lock on the treat, pupils
focused with bright catchlight. Weight shifts onto front paws. Tail held
at mid-height with slow single wag.

BEAT 2 (Commitment, 2-4s):
Juno takes the treat with a gentle, deliberate mouth close — no snatching.
Head pulls back half an inch as treat leaves the hand. Eyes close briefly
in a single slow blink on contact. Ears soften from forward to neutral.

BEAT 3 (Enjoyment, 4-7s):
Visible chewing motion — jaw working side to side. Audible crunch.
Eyes half-close in concentration. Single slow blink. Tail wag picks up
from mid to wide arc. Body visibly relaxes — shoulders drop half an inch.
After swallow: tongue flicks once across the nose, a small satisfied
exhale through the nostrils.

CAMERA: Medium close-up, head and front shoulders in frame. Shot at
dog-eye level. 50mm equivalent lens. Steady with subtle hand-held feel.
Shallow depth of field — background softly blurred.

LIGHTING: Warm morning light from camera-left, soft fill from camera-right.
No harsh shadows on Juno's face. Coat pattern clearly legible — merle
mottling visible, white chest blaze bright. Eyes catch light with visible
shine on each pupil.

AUDIO: Audible crunch of the treat, soft breathing/panting before and after,
ambient kitchen tone (distant hum of fridge), no music.

VOICEOVER (off-camera human narrator, warm and quiet):
"The only treat he actually waits for."

CONSISTENCY: Juno identical to image 1 throughout — coat, markings, eyes
unchanged. Product and single treat identical to image 2. No drift during
motion.

ANATOMY LOCK: Four legs total, two ears, one tail, correct joint angles.
No extra paws near the face or body. Natural dog anatomy.

DURATION: 7 seconds.
```

**Why it works:**
- Pet identity locked with specific distinguishing features (heterochromia, white sock) — hard to drift
- Body language carries the whole story — sniff, slow blink on contact, tongue flick after
- Voiceover is one line and specific — earns its place
- Product is visible but not dominating; the pet is the hero
- Crunch sound = the emotional peak

**Variants to generate from this base:**
- Breed swap: same script with a Chihuahua, a Labrador, a French Bulldog (test breed-matched ad targeting)
- Setting swap: same pet + script, outdoor park backdrop
- Voiceover swap: same clip, 3 different hooks tested

---

## Example 2 — Toy Brand: Durable Squeaker Ball

**Brand:** durable pet toys
**Product:** rubber squeaker ball, orange with black accents
**Persona:** Juno
**Axis:** environment (test indoor vs outdoor play)

**Prompt (outdoor version):**

```
Multi-input video generation, Seedance V2.

SUBJECT: The Australian Shepherd from image 1 — [full coat lock, same
as Example 1].

PRODUCT: Orange rubber squeaker ball from image 2, preserving exact color
and black accent stripes. Ball maintains exact shape and color during
motion — does not deform.

SETTING: Backyard grass in afternoon light, warm golden-hour tone, slightly
blurred background of fence and garden.

BEAT 1 (Discovery, 0-2s):
Juno on green grass, orange ball on ground in front of him about 2 feet
away. Head lowered, takes two audible sniffs at the ball. Ears forward
and rotating. Extends one front paw and pokes the ball — the ball squeaks.
Juno's ears snap forward and up, pupils dilate, body tenses.

BEAT 2 (Play bow, 2-4s):
Juno drops into a full play bow — front legs flat on grass, chest low,
hindquarters up and back end wagging tail high over his back. Eyes bright
and locked on ball. Mouth open in relaxed play face, tongue slightly
visible.

BEAT 3 (Play escalation, 4-7s):
Launches forward, grabs ball in soft mouth — ball visible protruding
from muzzle. Head-shakes side to side twice — rapid motion, coat
bouncing. Drops ball. Pounces on it with both front paws. Quick direction
change. Ball squeaks once during pounce.

BEAT 4 (Settle, 7-9s):
Juno sits in the grass with ball held between front paws. Tongue out
panting. Eyes bright. Tail wagging in wide relaxed arc. One slow blink.

CAMERA: Wide-to-medium. Starts at wider framing showing ball and dog,
pushes in slightly during play escalation. Follows motion with slight
hand-held feel. Shot at dog-eye level, 35mm equivalent.

LIGHTING: Afternoon golden-hour, natural sun from camera-left, warm and
soft. Coat texture catches light, orange ball pops against grass.

AUDIO: Ball squeak audible (twice — on paw-poke and on pounce), Juno's
playful huffing and panting, grass rustle under paws, ambient outdoor
sounds (distant birdsong), no music.

VOICEOVER (off-camera, warm):
"The squeak is the whole sell."

CONSISTENCY: Juno identical to image 1 throughout, coat pattern preserved
during motion. Ball identical to image 2, does not deform or change color.

ANATOMY LOCK: Four legs total, two ears, one tail, correct joint angles
especially during play bow and head-shakes. No extra limbs.

DURATION: 9 seconds.
```

**Why it works:**
- Beat structure mimics real dog play (discover → bow → explode → settle)
- Breed-appropriate behavior — Aussies are play-bow prone
- Ball squeak is the emotional signal, called out in audio
- Voiceover is honest and funny — no "ultimate play experience" corporate-speak
- Settle beat gives breathing room for a call-to-action in post

**Variants:**
- Indoor version (hardwood floor, living room)
- Multi-pet version (second dog joins the play)
- Different toy (rope instead of ball)

---

## Example 3 — Grooming Brand: Shedding Supplement Before-After

**Brand:** omega-3 supplements for dogs
**Product:** chew-form supplement, bottle visible
**Persona:** Juno (used for both before and after states, same dog, different coat condition)

**Setup:**
- Image 1: Juno standard (healthy shiny coat) — the "after"
- Image 2: Juno modified (dull, slightly matted coat) — the "before," generated via Nano Banana Pro using the standard persona with modified coat condition
- Image 3: Supplement bottle

**Prompt (time-lapse approach):**

```
Multi-shot video generation, Seedance V2.

SAME DOG THROUGHOUT ALL SHOTS. Australian Shepherd with red merle coat,
white chest blaze, one blue eye, one brown eye, white sock on left front
paw. Same markings and features in all states — only coat condition
changes across scenes.

[0s] SCENE 1 — BEFORE
Juno from image 2 sits on kitchen hardwood floor. Coat dull and slightly
matted, fur lays flat with small tangle visible on chest. Ears soft,
neutral eye shine. Body language quiet — not sad, just less bright.
Medium shot, side lighting.

[3s] SCENE 2 — PRODUCT USE
Cut to: Juno's food bowl on floor. Human hand from camera-right holds
supplement bottle from image 3 — branded label clearly visible, bottle
color preserved. Hand twists cap off, takes out one chew-form supplement,
places it on top of kibble in the bowl. Brand visible on label throughout.
Bowl lifts up or camera cuts to Juno eating.

[6s] SCENE 3 — AFTER
Juno from image 1 stands in the same kitchen, same framing angle as
Scene 1. Coat is fuller and shinier — red merle pattern vibrant, white
chest blaze bright, visible coat shine catching window light. Ears
pricked forward. Eyes bright with catchlight. Small head shake — coat
bounces with the motion. Single slow blink at camera. Tail held high
with wag.

CAMERA: Consistent 50mm equivalent across all shots, shot at dog-eye level.
Scenes 1 and 3 framed identically for direct visual comparison.

LIGHTING: Morning light from kitchen window in all scenes, consistent but
with slight warming progression (Scene 1 cooler, Scene 3 warmer to signal
health/vitality shift).

AUDIO: Ambient kitchen tone in all scenes. Scene 2: click of bottle cap,
soft kibble scatter into bowl. Scene 3: head-shake sound, soft paw click.
No music. Voiceover throughout.

VOICEOVER:
[0s-3s]: "Three weeks ago, Juno's coat was getting duller every month."
[3s-6s]: "Our vet suggested omega-3s. We tried [brand] because the
          ingredient list is short — just fish oil and vitamin E."
[6s-9s]: "Same dog. Better coat."

TRANSITIONS: Soft cross-dissolves between scenes. Scene 2 cuts crisper
to emphasize the product moment.

CONSISTENCY: Same dog across all scenes. Coat pattern (merle distribution,
white chest blaze, eye colors) identical — only condition changes. Product
identical to image 3 in Scene 2.

ANATOMY LOCK: Four legs, two ears, one tail in every scene. Correct
anatomy during head-shake in Scene 3.

DURATION: 9 seconds total.
```

**Why it works:**
- Same-dog-different-state is the hardest pattern to nail — this prompt locks identity while allowing coat condition to change
- Scene 2 gives the product its own beat — not buried
- Voiceover is honest ("ingredient list is short") and specific (three weeks, omega-3)
- "Same dog. Better coat." is the close — simple, honest, earned by the visual proof
- Body language subtly improves from Scene 1 to Scene 3 (ears from soft to pricked, tail from low to high) — emotional proof of transformation

**Variants:**
- 30-day vs 6-month claim overlays
- Breed variants (same transformation, different dogs)
- Cat variant (omega-3 for cat coat health)

---

## Example 4 — Harness Brand: Outdoor Fit Demo

**Brand:** lightweight dog harness for active owners
**Product:** navy padded harness with reflective strips
**Persona:** Juno

**Prompt:**

```
Multi-input video generation, Seedance V2.

SUBJECT: [Juno full persona lock as in Example 1].

PRODUCT: Navy padded harness from image 2 with reflective strips on side
panels, D-ring on back, chest buckle visible. Preserve exact color, padding
texture, and reflective strip pattern. Straps visible on surface of coat
only.

SETTING: Urban morning sidewalk, concrete texture, slightly overcast cool
light, brick building softly blurred in background.

PRODUCT POSITIONING:
- Front strap sits across chest, clear of throat
- Side straps sit behind front legs, clear of armpits
- Padded chest piece presses naturally into fur
- D-ring visible on back at shoulder level
- Reflective strips catch light subtly

BEAT 1 (Static, 0-2s):
Juno stands on sidewalk wearing the harness. Neutral relaxed body —
ears soft, tail at mid-height, mouth closed. Harness sits correctly,
no pulling or adjustment. Coat visible around the harness straps.

BEAT 2 (Motion, 2-5s):
Juno takes three natural walking steps forward. Harness moves with his
body — padded chest piece flexes subtly with his stride, straps maintain
position, no shifting. D-ring moves with back. Reflective strip catches
morning light briefly on second step.

BEAT 3 (Comfort signal, 5-7s):
Juno pauses, shakes his whole body once — quick motion starting at head,
traveling to tail. Harness stays in position through shake. Settles with
ears forward, tail mid-height. Single slow blink at camera. Soft pant.

CAMERA: Medium full-body shot, slight follow with walking motion. 35mm
equivalent. Dog-eye level.

LIGHTING: Cool morning urban light, natural overcast, even soft shadows.
Harness details clearly visible.

AUDIO: Paw clicks on concrete, collar tag jingle on shake, ambient urban
tone (distant traffic), no music.

VOICEOVER:
"Finally, a harness that doesn't rub."

CONSISTENCY: Juno identical to image 1 throughout. Harness identical to
image 2 — color, pattern, reflective strips, hardware unchanged. Product
fit stays correct during motion and shake.

ANATOMY LOCK: Four legs, two ears, one tail. Correct joint angles during
walk and shake. No extra limbs. No straps passing through body.

DURATION: 7 seconds.
```

**Why it works:**
- Product fit is explicit and correct (strap positions called out)
- Motion beat proves the product holds up in use
- Shake-off is a real dog behavior that proves comfort — harness stays put through it
- Slow blink + neutral body language = "no stress from wearing"
- Voiceover claim is earned by the visual proof

**Variants:**
- Color variants (same clip, different harness color in image 2)
- Size variants (same product, different breed sizes to show it fits)
- Terrain variants (sidewalk → grass → gravel path → hiking trail)

---

## Lessons Across All Examples

1. **Specific coat description + locked image = pet identity holds.** No shortcut here.

2. **Body language carries the emotional story.** Voiceovers support, don't lead.

3. **Beats are explicit and describable.** Not "plays happily" — "grabs ball in soft mouth, head-shakes twice, drops, pounces." Writeability is a proxy for renderability.

4. **Product gets its own beat.** Whether it's a reaction clip or a montage, the product needs at least 1-2 seconds of clean screen time.

5. **One voiceover line is usually enough.** Sometimes none.

6. **Anatomy lock and consistency lock are not optional.** They prevent the most common failure modes.

7. **The settle / final beat matters.** A 7-second clip that ends on a slow blink feels complete. One that ends mid-motion feels unfinished.

---

_Add new worked examples to this file as you run real campaigns. Include the full prompt, voiceover, and a short "why it worked" note._
