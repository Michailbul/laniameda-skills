# Pet Body Language Library

**The rule:** Pets don't talk, and vision models have no idea what "happy" means for a dog vs. a cat vs. a rabbit. Describe body language, not emotions. The model renders what you describe.

This is the pet equivalent of the human `emotion-muscle-library.md`. Same principle, different anatomy.

---

## The Universal Failure Modes

Vision models fail predictably on pets. Guard against these in every prompt:

1. **Dead-eye syndrome** — pupils uniform, no shine, no blink. Fix: always describe eye state (shine, dilation, blink timing, focus).
2. **Extra limbs** — 5-legged dogs, cats with 3 ears. Fix: anatomy lock — "four legs total, two ears, one tail, natural anatomy."
3. **Joint-angle violations** — backwards knees, impossible tail curves. Fix: "correct natural joint angles for [species]."
4. **Coat simplification** — brindle becomes beige, calico becomes gray. Fix: detailed coat description + high-res image reference.
5. **Uncanny "acting"** — pet looks coached, facial expression too human. Fix: describe natural species behavior, not human-mapped emotion.
6. **Wrong species motion** — cat running like a dog, dog walking like a horse. Fix: species-specific gait description.

---

## Dogs — Body Language → Prompt Language

### State: Excited / Happy

**Don't write:** "The dog is excited."

**Write:** "Loose relaxed body, tail wagging in a wide arc at mid-height, mouth slightly open with tongue visible, ears forward and slightly up, weight shifted forward onto front paws, quick alert breathing, eyes bright with pupils in normal focus."

### State: Curious / Investigating

"Head tilted 20 degrees to one side, ears rotated forward, eyes focused on the object, body still and slightly leaning in, one front paw lifted or hovering, closed mouth, steady quiet breathing."

### State: Playful

"Play bow posture — front legs extended flat with chest low, hindquarters up, tail wagging high over the back, mouth open in a relaxed 'play face,' bright alert eyes, ready to spring."

### State: Content / Relaxed

"Lying on side with legs loose, soft half-closed eyes, mouth relaxed in a soft closed smile or slight pant, tail flat and still or slow soft thumping, slow rise-and-fall of the ribcage, occasional slow blink."

### State: Sleepy / Drifting

"Eyes heavy-lidded and slowly closing, head resting on paws or floor, body completely loose, slow deep breathing with visible ribcage movement, occasional ear twitch, tail motionless."

### State: Alert / Watchful

"Body tense and forward, ears pricked fully up and rotated toward the sound, tail held high and still, eyes wide and locked on target, mouth closed tight, weight loaded on front paws ready to move."

### State: Nervous / Cautious

"Body lowered and slightly crouched, tail tucked low or between legs, ears back and flat against skull, 'whale eye' — whites visible at the corners, slow careful movements, mouth closed tight, cautious steps."

### State: Focused on Food / Treat Approach

"Nose lowered toward the object, ears forward, eyes locked on the target, slight drool or lip-lick, weight forward, body slightly tense with anticipation, tail held mid-height wagging slowly."

### Micro-gestures (add at least one)

- Single slow blink at the camera
- Head tilt with one ear higher than the other
- Quick nose sniff — visible nostril flare
- Paw lift without putting it down
- Tongue flick across nose
- Shake-off motion (whole body shake starting at head)
- Yawn with full mouth visible
- Scratch with hind leg, one beat only
- Tail thump on the floor (if seated)
- Full-body stretch with extended front legs and arched back

### Breed-specific notes

- **Sight hounds** (greyhound, whippet) — more reserved, subtle body language, tall lean posture
- **Bully breeds** (pitbull, bulldog) — big head tilts, exaggerated play bows, wide grins
- **Working dogs** (border collie, german shepherd) — intense focus, high alert posture, ear rotation
- **Small toy breeds** (chihuahua, pomeranian) — quick sharp movements, exaggerated expressions
- **Retrievers** (golden, lab) — signature happy-mouth, loose body language, tail constantly in motion

Add a breed-specific tell when you can — it's a specificity win.

---

## Cats — Body Language → Prompt Language

### State: Content / Relaxed

**Don't write:** "The cat is happy."

**Write:** "Loaf position — legs tucked under body, tail wrapped around flank, eyes half-closed giving a slow blink every few seconds, ears in neutral forward position, soft visible breathing, stillness punctuated by occasional ear twitch."

### State: Curious / Investigating

"Body upright and alert, ears rotated forward, pupils normal to slightly dilated, tail held upright with a soft curl at the tip, cautious slow approach with one paw testing forward, nose extended toward the object for sniff."

### State: Playful / Hunting Mode

"Body low to the ground and coiled, pupils fully dilated to dark pools, ears forward and flattened slightly, tail twitching rapidly at the tip only, hindquarters making a subtle side-to-side 'butt wiggle' before launch, complete stillness in the upper body."

### State: Affectionate

"Tail held straight up with a soft curl or hook at the tip — the greeting signal. Slow blink at camera. Head-bonking motion toward owner's hand, cheek rub against object or person, eyes half-closed in trust."

### State: Startled / Defensive

"Body arched high or crouched low, pupils blown fully wide, ears flattened back against the skull, tail puffed out to twice normal size, mouth slightly open with a visible huff, fur raised along the spine."

### State: Enjoying Food

"Eyes half-closed in concentration, tail tip lightly twitching, ears forward but relaxed, occasional pause between bites with a slow blink, whiskers pushed forward over the food."

### State: Kneading / "Making Biscuits"

"Front paws alternating in a slow rhythmic push-pull motion, paws splayed with claws extending and retracting, eyes half-closed in bliss, drooling possible, purring visible as subtle ribcage vibration."

### State: Alert / Watching

"Eyes wide and locked on the target, pupils adjusting to focus, ears fully upright and rotated forward, body still with high tension, tail flat and motionless or slowly twitching at tip, whiskers pushed forward."

### Micro-gestures (add at least one)

- Slow blink — the universal cat "I trust you"
- Single ear flick
- Tail-tip twitch
- Whisker push forward
- Paw lick with one quick tongue motion
- Kneading paw motion
- Cheek rub against surface
- Stretch with arched back and full leg extension
- Silent "mew" mouth opening
- Single tooth visible during mouth movement

### Breed-specific notes

- **Oriental / Siamese / Bengal** — more vocal, more motion, pointier body language
- **Persian / Ragdoll / Maine Coon** — slower, more regal, less frantic
- **Scottish Fold / Munchkin** — body shape affects posture; folded ears don't rotate the same way

---

## Rabbits / Small Mammals

### State: Content (rabbit)

"Lying in full 'flop' position with legs extended — a trust signal. Ears relaxed backward along the body. Eyes half-closed. Occasional nose twitch. Complete stillness."

### State: Happy / Excited (rabbit binky)

"Mid-air twist — jumping straight up with a body-rotation twist, all four legs off the ground, ears flopping from motion, fast head turn, kicking legs at the peak. Landing with a small kick-out."

### State: Alert / Nervous (rabbit)

"Body compressed into upright 'loaf' with ears standing tall and rotating, eyes wide with no blinking, nose twitching rapidly, complete stillness waiting for threat to pass."

### Guinea Pig

- **Popcorning:** vertical hops in place, all four feet leaving the ground, head flicks, body twists mid-air
- **Wheek:** mouth opens for the call — describe the whistle-like mouth shape
- **Rumblestrut:** low hip-swaying walk with vibrating body

### Ferret

- **War dance:** bouncing leaps in all directions, mouth open, often arching back, chattering sounds
- **Dook:** soft clucking, mouth forming small open shapes

---

## Birds (parrots, macaws, cockatiels)

### State: Curious

"Head cocked sideways to focus one eye on the object, eye-ring tightening as pupils pin (rapid dilation), crest feathers rising slightly, small head bob."

### State: Happy / Excited

"Crest fully raised, eyes pinning (pupils rapidly dilating and contracting), body bouncing lightly on the perch, wing flutter, soft vocalization, foot-raising motion."

### State: Fluffed / Content

"Feathers puffed out all over the body, eyes half-closed, one foot tucked up into chest feathers, head tilted back into wing area, slow breathing."

### State: Aggressive / Warning

"Body tall and rigid, feathers slicked flat against body, eyes pinned wide and hard, beak slightly open, leaning forward, wings partially spread."

### Micro-gestures

- Beak grind — sign of contentment, quiet clicking sound
- Head bob at music/sound
- Foot scratching head feathers
- Regurgitation offer (affection — looks odd to humans, is a gift)

---

## Mixed-Species / Multi-Pet Scenes

Coordinating multiple pets in one clip:

- **Dog + cat:** usually describe them ignoring each other or one watching the other — realistic is not them "reacting" together. Cat on counter watching dog eat. Dog at feet of sleeping cat.
- **Two dogs:** synchronous eating, one playing while other watches, side-by-side at window.
- **Multiple cats:** rarely together unless family — more often in separate parts of frame, one grooming, one loafing, one looking alert.
- **Small pet + larger pet:** size-appropriate separation, small pet behind barrier or in cage, larger pet observing with controlled body language.

Lock each pet to its own reference image. Multi-pet prompts need image 1, image 2, image 3 (each a different pet), plus explicit instructions on which is which and where they are in frame.

---

## Breathing, Pacing, Sound Cues

Real animals breathe, sigh, blink, twitch. AI animals freeze.

Always include at least one of:
- "Visible ribcage rise and fall with breathing"
- "Tail thumps once every few seconds"
- "Ear flicks at a sound"
- "Soft pant with tongue slightly extended"
- "Slow blink once during the clip"
- "Nose twitches with sniff"
- "Occasional tail-tip twitch"

And for audio:
- Panting (rhythm: rhythm matches physical state — excited = fast)
- Purring (describe as "subtle body vibration" if audio isn't captured)
- Crunch of kibble / squeak of toy
- Collar jingle on movement
- Claws clicking on hard floor

---

## Compare: Dog vs Cat State Translation

Same emotional state, very different body language. A prompt that says "happy" is wrong for both. A prompt that specifies body language is right for both.

| Emotional state | Dog body language | Cat body language |
|---|---|---|
| Content | Tail flat, thumping | Loaf, slow blink |
| Excited | Wide-arc tail wag, mouth open | Pupils dilate, tail whip |
| Curious | Head tilt, ears forward | Tail up, forward ear rotation |
| Affectionate | Leaning into, nuzzle | Head bonk, cheek rub, tail up |
| Playful | Play bow | Coiled-low stalk posture |
| Nervous | Tail tuck, whale eye | Ears flat, puffed tail |
| Alert | Pricked ears, high tail | Forward ear, body tension |

---

_Add to this file when you discover new species or breed-specific body language mappings. Cite the source (observation, vet behavior resource, successful ad generation)._
