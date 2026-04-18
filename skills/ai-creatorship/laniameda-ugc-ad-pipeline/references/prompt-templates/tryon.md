# Virtual Try-On Template

**Use when:** creator wears an item on camera — apparel, accessories, glasses, shoes, jewelry. Motion and face stay constant, the item swaps in.

**Inputs required:**
- Image 1: persona reference (locked face and body proportions)
- Image 2: item/outfit reference (clean product shot or on-mannequin reference)
- Optional video 1: existing motion reference if replicating a specific shot

---

## Template

```
Multi-input video generation, Seedance V2.

SUBJECT: The woman from image 1, same face exactly, same body proportions, do not
alter facial structure or build.

OUTFIT: She is wearing the exact outfit from image 2 — preserve pattern, cut, color,
fabric texture, and all visible details (buttons, seams, logos, prints). Outfit
fits naturally on her body, drapes realistically, moves with her.

ACTION: She is [WALKING / STANDING / TURNING / POSING] in [ENVIRONMENT: outdoor
street scene / studio backdrop / urban setting / interior with soft lighting].
Her movement is natural and unchoreographed — slight weight shifts, a small
gesture with her hand, a glance off camera then back.

ENVIRONMENT DETAILS: [Add 3-5 specific details — e.g. "snow-dusted sidewalk in
Montreal, -30 degrees, breath visible in the air, overcast grey sky, parked cars
along the curb, a bear walks past in the background and she tracks it briefly
with her eyes."]

CAMERA: [Medium shot / full body / 3/4 framing], 35mm equivalent lens, slight
hand-held feel, shot at chest height, minimal zoom. Camera holds steady while
subject moves within frame.

LIGHTING: [Match the environment — natural overcast for outdoor, soft window
for interior, golden hour for street]. Consistent with source reference if video 1
is provided.

AUDIO: Ambient environment audio (wind, distant traffic, room tone), no music,
no dialogue unless specified.

CONSISTENCY: Face identical to image 1 throughout. Outfit identical to image 2
throughout — pattern, cut, color, and details must not morph or simplify. Body
proportions consistent with image 1.

DURATION: ~5-7 seconds.
```

---

## Swap points

- `[WALKING / STANDING / TURNING / POSING]` — action
- `[ENVIRONMENT]` — setting
- `Environment details` — specifics
- Camera framing and lens

Keep constant:
- Persona (image 1)
- Outfit (image 2)
- Consistency lock

---

## Failure watchouts

- **Pattern simplification** — fabric prints or logos get smoothed out. Fix: use higher-res image 2, add `"preserve all fabric pattern detail, do not simplify print or texture"`.
- **Outfit morph mid-clip** — cut or color changes during motion. Fix: add `"outfit maintains identical cut and color throughout the clip, no transformation"`.
- **Face swap** — model renders a different person. Fix: add the standard face-lock phrasing, regenerate.
- **Unnatural gait** — walk looks staged. Fix: add `"natural walking pace, slight weight shift, not a runway walk"`.

---

## Variation axes

**Outfit A/B:** same persona, same environment, swap image 2.
**Environment A/B:** same persona, same outfit, change environment paragraph.
**Season/weather A/B:** swap environment + adjust lighting + adjust any weather-specific elements (breath visible, snow, etc.).
**Motion A/B:** swap action verb (walking / leaning / turning / picking up / etc.).

---

## Example — from Sirio Berati's Seedance V2 demo (Montreal winter outfit)

Setup:
- Image 1: Sirio in shorts and a tee (real footage)
- Image 2: full winter outfit on a mannequin reference
- Environment: Montreal street, -30°C
- Added element: bear walking past

Result: outfit swapped exactly (boots, pants pattern, jacket), face identical, weather convincing (snow, breath), bear tracked by eyes.

What made it work:
- The source footage carried the motion — Seedance just swapped the outfit on top
- Environment detail was specific ("Montreal, -30°, breath visible")
- Micro-gesture added (bear tracking with eyes) broke any AI-demo feel
- Outfit reference was complete (not just a jacket — whole fit)
