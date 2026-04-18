# Toy Try-Out Template

**Use when:** pet toy brand. The arc is curiosity → play escalation → full engagement. The visual proof is the pet actually playing, not just posing with the toy.

**Inputs required:**
- Image 1: pet persona reference
- Image 2: toy product image
- Optional image 3: pet-holding-toy composite (via Nano Banana Pro)

---

## Template

```
Multi-input video generation, Seedance V2.

SUBJECT: The [BREED] from image 1, exact same pet — identical coat pattern,
same size, same features, same eye color. Do not alter markings.

PRODUCT: The toy from image 2, preserving its exact color, pattern, shape,
and any logo or branding. Toy maintains consistency throughout motion.

SETTING: [ENVIRONMENT: living room with soft rug / grass yard in afternoon
light / bright home office]. Pet is on the floor in a natural posture —
alert but relaxed.

BEAT 1 (Discovery, 0-2s):
The toy from image 2 is on the ground in front of the pet. Pet approaches
cautiously — head lowered to sniff level, ears forward and rotating for
sound, eyes focused on the toy, tail held mid-height with slow wag or
stillness. One single-paw pokes at the toy — tentative, exploratory.

BEAT 2 (Investigation, 2-4s):
Pet's posture shifts into curious engagement. Tail wag speeds up. Ears
fully forward. Mouth opens slightly in anticipation. [BREED-SPECIFIC
CUE: e.g. for herding breeds — subtle play bow; for terriers — sharp
quick head movements; for retrievers — mouth open and soft].

BEAT 3 (Play escalation, 4-7s):
Pet commits to the toy — [BREED-APPROPRIATE PLAY: e.g. grabs toy in mouth
and shakes head side to side vigorously / paws at toy with quick front-paw
motions / chases toy as it moves]. Body loose and animated. Tail wagging
at full arc. Mouth open in "play face" — relaxed, slightly panting.
Toy audible: [squeak / crinkle / rattle / chew].

BEAT 4 (Optional settle, 7-8s):
Pet sits or lies down with the toy between front paws, mouth on the toy
in a relaxed chew hold. Tail slows. Eyes focused on the toy.

CAMERA: Wide-to-medium framing, follows the pet's motion with slight
hand-held feel. Starts at a wider shot during discovery, pushes in during
play escalation. Shot at pet's eye level. 35mm equivalent for wider,
adjust toward 50mm as it tightens.

LIGHTING: Natural bright daylight from a window or outdoor ambient,
warm and even, no harsh shadows. Coat texture and toy colors both legible.

AUDIO: Toy sounds prominent (squeak/crinkle/rattle matching the toy type),
pet's play sounds (happy huffing, occasional playful bark or mrow),
ambient room tone, no music.

CONSISTENCY: Pet identical to image 1 throughout — coat pattern, markings,
features unchanged even during vigorous motion. Toy identical to image 2 —
does not morph or change as it's played with.

ANATOMY LOCK: Four legs total, two ears, one tail. Natural joint angles
especially during play — no impossible twists. Body maintains correct
proportions even during zoomies or head-shakes.

DURATION: ~7-10 seconds.
```

---

## Species-specific play behaviors

### Dogs

**Large breed retrievers (Lab, Golden):**
"Grabs toy in soft mouth, carries it in a happy trot, drops it, picks it up
again. Tail high. Mouth relaxed and open around toy."

**Terriers (Jack Russell, Yorkie, Cairn):**
"Sharp quick head shakes with toy in mouth. Pounce-and-grab motions.
Intense focus between bursts. Quick direction changes."

**Herding breeds (Border Collie, Aussie):**
"Crouched stalk, pounce, circle, pounce again. Low to ground, intense
eye contact with toy. Quick directional changes."

**Bulldogs / Pugs:**
"Short bursts of energy, play bow with front legs flat, shake toy with
surprising force, take breaks to pant heavily."

**Toy breeds (Chihuahua, Pomeranian):**
"Exaggerated movements, quick zoomies, sharp barks, tail held straight up."

### Cats

**General cat play:**
"Pupils fully dilated to dark pools. Body coils low to ground before
launch. Tail tip twitches rapidly. Pounces with both front paws extended.
Batting motion with front paws. Occasional grab-and-bunny-kick with
hind feet. Between bursts: complete stillness."

**With a feather wand / interactive toy:**
"Tracks toy with intense focus, ears forward and flat. Chirrup or chatter
(mouth opens in rapid silent-looking motion). Vertical leap with paw swipe."

**With a solid toy:**
"Carries toy in mouth, drops, pounces on it again. Sometimes places toy
on owner or in water bowl (realistic cat behavior)."

### Small pets

**Rabbit with toy:**
"Investigates by nose-nudging, tosses toy with quick head-flick, binkies
mid-play (twist jump in air)."

**Guinea pig with toy:**
"Popcorns in place, wheeking sounds, rubs cheek on toy (scent marking)."

---

## Swap points

- `[BREED]` — for breed-variant generation
- `[ENVIRONMENT]` — setting
- `[BREED-SPECIFIC CUE]` — play behavior
- Toy sound type
- Camera framing preference

Keep constant:
- 4-beat arc structure (discover → investigate → escalate → settle)
- Anatomy + consistency locks

---

## Failure watchouts

- **Toy morphs during motion** — more common with soft/plush toys. Fix: higher-res image 2, add "toy maintains exact shape and color throughout motion, does not deform."
- **Play motion looks staged / robotic** — add breed-specific play language. Real dogs don't "play" in generic ways.
- **Pet holds perfectly still while "playing"** — explicitly describe motion in each beat. Add "body loose and animated."
- **Extra paws during rapid motion** — strengthen anatomy lock, reduce motion speed if needed.
- **Coat blurs into beige during fast motion** — add "coat pattern stays legible even during motion blur."

---

## Variation axes

**Toy variant A/B:** same pet, same script, swap toy (squeak vs rope vs ball vs plush).
**Environment A/B:** indoor rug vs outdoor grass vs hardwood — affects play style.
**Play intensity A/B:** calm gentle play vs high-energy zoomies.
**Solo vs multi-pet:** solo play vs two pets sharing/competing.
**Breed A/B:** same toy, same script, swap persona — test which breed sells the toy best.

---

## Hooks that work for pet toys

Voiceovers should feel like the owner talking about their pet, not the brand talking. Run through `human-copy-standards`.

- "Paid $40 for a toy and she went straight for the Amazon box."
- "Three weeks. That's how long this one lasted. Actual record."
- "The squeak is the whole sell."
- "Why does he body-slam every new toy? Why."
- "She's owned this ball for longer than I've owned my apartment."

Avoid:
- "Give your pet endless fun with..." (generic)
- "The ultimate play experience!" (corporate)
- "Your pup will love this!" (cliche + AI-speak)

---

## Example — Toy try-out beat structure (worked)

Setup:
- Persona: Australian Shepherd, Juno
- Product: durable rubber squeaker ball, orange with black stripes
- Setting: backyard grass, afternoon

Prompt core:
> Juno on green grass, orange ball on ground in front of him. Nose down,
> two sniffs, one front paw pokes the ball — it squeaks — ears snap
> forward and up. Pupils dilate. Body drops into play bow, front legs
> flat, rear high, tail wagging at full arc over his back. Launches
> forward, grabs ball in soft mouth, head-shakes side to side twice,
> drops it, pounces again with both front paws. Stops with ball between
> front paws, tongue out panting, eyes bright.

Voiceover: "The squeak is the whole sell."

Why it works:
- Beats specific and visually describable
- Breed-appropriate behavior (play bow is very Aussie)
- Squeak sound drives the emotional peak
- Voiceover is honest and funny
