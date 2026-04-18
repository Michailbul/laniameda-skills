# Reaction / Taste-Test Template

**Use when:** creator is trying a product on camera — food, drink, skincare, first-touch unboxing, first-use reaction. The money shot is the expression shift.

**Inputs required:**
- Image 1: persona reference (locked face)
- Image 2: product image (clear, well-lit, label visible if branded)
- Optional video 1: motion reference if replicating a specific camera move

---

## Template

```
Multi-input video generation, Seedance V2.

SUBJECT: The woman from image 1, same face exactly, same features, do not alter
facial structure. She is in a [ENVIRONMENT: warm home kitchen / modern living room /
clean minimal bathroom], natural soft lighting from camera left, slight warm tone.

PRODUCT: She is holding the exact product from image 2, preserving all label text,
logo, color, and proportions. The product is positioned in her right hand at chest height.

ACTION: She takes the product, pauses for a breath, then takes a [small sip / first
bite / first swipe / first spray]. Her initial expression is neutral with lips
pressed together in mild skepticism, one eyebrow slightly raised. Within half a
second of trying the product, her eyebrows lift, her eyes widen for one beat, and
the corners of her mouth pull up into a closed-lip smile. She blinks once, then
looks back at the camera.

DIALOGUE: She says
"Okay, quick taste test."
Pauses as she tries the product, then continues:
"Huh. Wait, that's actually nice. It's not super sweet. It's really clean.
I wasn't expecting that."
She finishes with a small nod and a quiet exhale through her nose.

CAMERA: Medium close-up, chest-up framing, 50mm equivalent lens, slight hand-held
sway, shot at eye level. Minimal camera movement — subject motion carries the shot.

LIGHTING: Natural window light from camera-left, warm pendant overhead, soft
shadows, no harsh contrast. Film-like grain minimal.

AUDIO: Quiet room tone, subtle ambient kitchen sounds, no music, clean vocal capture
as if recorded on a phone mic at arm's length.

CONSISTENCY: Face identical to image 1 throughout. Product identical to image 2
throughout — text, logo, color, and shape must not warp, wrap, or alter.

DURATION: ~7 seconds.
```

---

## Swap points

Replace these per-variant:

- `[ENVIRONMENT]` — setting
- Product action (sip / bite / swipe / spray / etc.)
- Opening emotion (skeptical / neutral / curious / tired / etc.)
- Dialogue inside quotes
- Language of dialogue (for translation variants)

Keep constant:
- Persona reference (image 1)
- Product reference (image 2)
- Camera framing and lens
- Muscle-movement structure
- Consistency lock phrasing

---

## Failure watchouts

- If the model renders a different face — add `"same person as image 1, identical facial features, do not interpret or stylize"` to the consistency lock
- If product text warps — generate a higher-res product image as image 2, retry
- If expression reads rehearsed — add `"initial smile softens within one second, becomes natural and slightly asymmetrical"`
- If dialogue feels robotic — add more breath/pause cues between phrases, shorten sentences

---

## Hook variants for A/B testing

Swap only the opening line. Keep everything else identical.

1. "Okay, quick taste test." (neutral)
2. "I was skeptical about this, but..." (direct appeal to skeptics)
3. "Wait, this is actually..." (pattern interrupt)
4. "I keep hearing about this so..." (social proof entry)
5. "Not what I expected, in a good way." (verdict-first)

---

## Example — from Sirio Berati's Seedance V2 demo (soda taste test)

Original spoken line:
> "Okay quick taste test. Huh. Wait, that's actually nice. It's not super sweet. It's really clean. I wasn't expecting that. Yeah, I'd drink this."

This worked because:
- Filler word "huh" between the initial try and the verdict
- Mid-sentence pause ("Wait, that's actually nice")
- Skeptical-to-surprised transition described as muscle movements
- Final verdict is casual and low-energy ("yeah, I'd drink this") — not overhyped
- Product text on the bottle stayed consistent throughout

Replicate the *rhythm*, not just the words.
