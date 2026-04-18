# Model Selection for Pet Ads

**Default:** Seedance V2.

Pets have specific prompting challenges — coat detail, species motion, eye life, anatomy correctness. Some models handle these better than others.

---

## Fast Decision Tree

```
Realistic pet with natural motion + body language?
 → Seedance V2 (default)

Cinematic pet montage, dreamy brand film look, short prompts?
 → Kling 3

Static hero portrait only (no motion)?
 → Nano Banana Pro alone

Multi-pet coordinated scene?
 → Seedance V2 with multiple image inputs

Talking-pet humor (meme-style, stylized)?
 → Seedance V2 with lip sync via quotation marks on muzzle

Extreme close-up of eyes, nose, paw details?
 → Nano Banana Pro (image) → extend to 2s motion via Seedance V2

Breed-intense detail (brindle, merle, calico, tortie)?
 → Seedance V2 with high-res reference image (Kling 3 loses pattern detail)

4K final delivery?
 → Generate Seedance V2 (720p), upscale via Topaz or Adobe

None of the above?
 → Seedance V2 (default)
```

---

## Model-by-Model Notes for Pet Ads

### Seedance V2 — Default

**Strengths for pets:**
- Multi-input generation: pet image + product image + optional environment video
- Preserves coat patterns through motion (with high-res reference)
- Handles species-specific motion (cat silent paws vs dog heavy paws)
- Character identity preservation across frames
- Text/logo on product packaging stays sharp during pet interaction

**Weaknesses for pets:**
- Max 720p — pet coat detail can soften at this resolution
- Dead-eye risk without explicit eye state prompting
- Can simplify complex coat patterns if prompt is vague

**Best for:**
- Treat reactions
- Toy play
- Product fit (wearables)
- Day-in-life montages
- Grooming reveals
- Multi-pet scenes

**Worst for:**
- Pure cinematic mood (Kling 3 wins)
- Extreme macro detail (Nano Banana Pro still holds)

---

### Kling 3

**Strengths for pets:**
- Dreamy, filmic, emotional brand-film feel
- Short prompts work — useful for vibe-first ads
- Color grading feels cinematic

**Weaknesses for pets:**
- Coat pattern detail degrades more than Seedance
- Character identity drifts across shots
- No multi-input — can't reference persona AND product together
- Species motion feels more generic

**Best for:**
- Brand film opens / hero videos
- Slow-motion emotional moments
- Stylized dreamy vibes (golden-hour beach dog, soft snow cat)

**Worst for:**
- Product-forward ads
- Precise breed/coat representation
- Multi-scene consistency

---

### Nano Banana Pro (image, used as upstream)

**Strengths for pets:**
- Best coat detail of any model — brindle, merle, calico render correctly
- Eye life and detail at close range
- Multi-angle reference generation
- Pet + product compositing
- Before-after state generation (same pet, different conditions)

**Use for:**
- Persona lock image (always)
- Multi-angle variant library
- Before-after pair generation for grooming ads
- Pet-wearing-product composites

**Don't use for:**
- Motion (it's an image model)
- Dynamic sequences

---

### Enhancor V4

**Strengths for pets:**
- Subtle close-range detail on fur/features
- Longer-form clips (15-30s+)
- Different color treatment — less "polished AI" feel

**Weaknesses:**
- Less editing capability than Seedance
- Character consistency across clips harder
- Lower overall fidelity

**Best for:**
- Long-form pet spokesperson clips (animated brand mascot pet speaking directly to camera)
- Pet "testimonial" stylized pieces

**Worst for:**
- Multi-scene ads
- Product-focused shots

---

### Veo (V3.1 / waiting for V4)

**Current state:** Decent general video quality but expensive and not specifically tuned for pets. Coat detail inconsistent.

**Use when:** budget allows and you want to compare Seedance V2 output with a different model's take. Otherwise skip.

---

## Use-Case to Model Matrix (Pet-specific)

| Use case | Primary | Fallback |
|---|---|---|
| Treat reaction | Seedance V2 | — |
| Toy play | Seedance V2 | Kling 3 (if stylized) |
| Product fit (wearable) | Seedance V2 | — |
| Grooming before-after | Seedance V2 | Nano Banana Pro for static pair |
| Day-in-the-life montage | Seedance V2 | — |
| Brand film / cinematic | Kling 3 | Seedance V2 |
| Multi-pet household | Seedance V2 | — |
| Talking-pet humor | Seedance V2 | — |
| Hero portrait only | Nano Banana Pro | — |
| Macro close-up (eye, nose) | Nano Banana Pro → Seedance V2 | — |

---

## Breed Complexity → Model Choice

Some coat patterns are harder for video models than others. Adjust accordingly.

| Coat complexity | Model recommendation |
|---|---|
| Solid colors (black lab, cream retriever) | Any model works |
| Simple patterns (white socks, blaze) | Seedance V2 / Kling 3 |
| Medium patterns (tabby, piebald) | Seedance V2 (with high-res ref) |
| Complex patterns (brindle, merle, calico, tortie) | Seedance V2 + Nano Banana Pro upstream for max detail |
| Extreme patterns (double merle, heavily mottled) | Seedance V2 only, verify each generation |

---

## Cost / Speed Benchmarks

Rough order of magnitude:

| Model | Cost per ~5s clip | Speed |
|---|---|---|
| Seedance V2 | ~$0.20-0.50 | ~60s |
| Kling 3 | ~$0.30-0.80 | ~60-90s |
| Enhancor V4 | ~$0.20-0.40 | ~45-75s |
| Nano Banana Pro (image) | ~$0.04-0.10 | ~10-20s |
| Veo 3 | ~$3.00 | ~90-120s |

Build personas with Nano Banana (cheap, detailed) → animate with Seedance V2 (affordable, high quality). The combined cost per final clip sits around $0.50-0.70.

---

## Multi-Model Pipeline (standard for pet ads)

Real pet campaigns layer models:

1. **Nano Banana Pro** → persona source image (1-time cost per pet)
2. **Nano Banana Pro** → multi-angle variants (one-time library)
3. **Nano Banana Pro** → pet-wearing-product or pet-before-after composites
4. **Seedance V2** → animated ad clips with multi-input
5. **Kling 3** (optional) → cinematic b-roll intercuts
6. **Topaz / Adobe** → upscale to 4K + final edit

Don't pick one model — pick the right model per stage.

---

## When Models Fail

### Dead-eyed pet

- **Cause:** model not prompting eye state
- **Fix:** explicitly describe eye state every prompt — "bright eyes with natural shine, visible catchlight, pupils focused on [X]"

### Extra paws appear

- **Cause:** anatomy lock missing or too weak
- **Fix:** "four legs total, two ears, one tail, no extra limbs, correct anatomy, correct joint angles"

### Coat simplifies to beige/gray

- **Cause:** low-res reference image OR vague pattern description
- **Fix:** higher-res image 1 AND explicit coat description in prompt ("red merle with mottled red, cream, and dark brown patches")

### Pet looks like different dog across variants

- **Cause:** relying on text description alone
- **Fix:** always use image 1 reference — never generate pets from text alone for campaign work

### Toy/product morphs during pet interaction

- **Cause:** model prioritizing motion over object permanence
- **Fix:** "toy maintains exact shape and color throughout motion, does not deform"

### Cat motion feels heavy / dog motion feels floaty

- **Cause:** wrong species physics
- **Fix:** species-specific motion descriptors in prompt ("silent paw placement," "heavy weight-bearing stride")

---

_Update this file as new models drop or as you discover per-model quirks in pet generation._
