# Model Selection Decision Tree

**Default for UGC ads:** Seedance V2.

But Seedance is not always the right tool. This file is the decision layer.

---

## Fast Decision Tree

Start here. If any branch hits, use the specified model.

```
Need cinematic feel + short prompts that just work?
 → Kling 3

Need pure talking-head realism with subtle long-form emotion?
 → Enhancor V4

Need 4K+ final delivery?
 → Generate in Seedance V2 (720p), upscale in Adobe or Topaz

Need static hero image only (no motion)?
 → Nano Banana Pro (skip video entirely)

Need real-time or ultra-cheap generation?
 → Kling 3 or Seedance V1.5

None of the above?
 → Seedance V2 (default)
```

---

## Model-by-Model Notes

### Seedance V2 — Default

**Strengths:**
- Multi-input generation (up to 2 images + 2 videos + 1 audio)
- Preserves text and logos on products through motion
- Character identity preservation across frames
- Lip sync with dialogue in quotation marks
- Works as an editor, not just a generator — character swap, background swap, outfit swap, ad translation, template population

**Weaknesses:**
- Max 720p resolution (1080p version pending)
- Rewards long specific prompts — short prompts underperform
- ~60s per generation (slower than some alternatives)

**Best for:**
- UGC ads (default)
- Ad translation / localization
- Virtual try-ons
- Product template brand swaps
- Video extension (end-fill or middle-fill)
- AI influencer lip sync

**Worst for:**
- Cinematic film-look shots — feels clinical vs Kling 3
- Long-form (>10s) single-take talking head — drift increases

---

### Kling 3

**Strengths:**
- Cinematic color grading and motion feel
- Responds well to short punchy prompts
- Strong at dreamy / stylized / filmic look

**Weaknesses:**
- Character identity drifts more than Seedance
- No multi-input (as of this writing)
- Text on products warps

**Best for:**
- Mood pieces, brand films, teasers
- Fashion / lifestyle b-roll
- Anything where vibe > identity-preservation

**Worst for:**
- Product-forward ads with text/logos
- UGC with a locked persona
- Translation (no multi-input = no motion reference)

---

### Enhancor V4

**Strengths:**
- Talking-head realism optimized — depth, background treatment, subject isolation
- Better for long-form narration (15-30s+ clips)
- Different color scheme feel — more natural, less "AI-polished"
- Handles subtle emotional shifts better than Seedance

**Weaknesses:**
- Lower fidelity overall than Seedance
- Character consistency across clips is harder
- Fewer editing capabilities (no multi-input at Seedance's level)

**Best for:**
- AI spokesperson / brand explainer videos
- Long-form testimonials
- "Hi guys, I'm not even real" style talking heads where authenticity matters more than polish

**Worst for:**
- Multi-character scenes
- Product-focused shots
- High-motion action

---

### Nano Banana Pro (image, not video)

**Strengths:**
- Best-in-class image editing, compositing, and character consistency
- Ideal for generating persona source images and product composites
- Image-to-image workflow is unmatched

**Weaknesses:**
- Not a video model — obviously
- Use as upstream feeder for Seedance V2, not as a replacement

**Best for:**
- Persona generation (the most important upstream step)
- Product composites (creator holding product)
- Reference frames for Seedance prompts

---

### Veo (waiting for V4)

**Current state:** V3.1 attempts some video extension but Seedance V2 does it better. V4 rumored to close the gap.

**Watch for:** When V4 drops, re-evaluate. Google has the compute and the model DNA to leapfrog.

---

## Use Case → Model Matrix

| Use case | Primary | Fallback |
|---|---|---|
| UGC reaction / taste-test | Seedance V2 | Enhancor V4 |
| Virtual try-on | Seedance V2 | — |
| Product hold / showcase | Seedance V2 | Kling 3 (for mood) |
| Ad translation | Seedance V2 | — (no equal alternative) |
| 3D template brand swap | Seedance V2 | — |
| Long talking-head spokesperson | Enhancor V4 | Seedance V2 |
| Cinematic brand film | Kling 3 | Seedance V2 (less filmic) |
| AI influencer lip sync | Seedance V2 | Enhancor V4 |
| Video extension (end) | Seedance V2 | Veo V3.1 |
| Video extension (fill middle) | Seedance V2 | — (unique capability) |
| Hero image only (no motion) | Nano Banana Pro | — |
| Mood piece / stylized | Kling 3 | — |

---

## Cost / Speed Considerations

Rough order of magnitude (prices shift, check current):

| Model | Cost per ~5s clip | Speed |
|---|---|---|
| Seedance V2 | ~$0.20-0.50 | ~60s |
| Kling 3 | ~$0.30-0.80 | ~60-90s |
| Enhancor V4 | ~$0.20-0.40 | ~45-75s |
| Veo 3 | ~$3.00 | ~90-120s |
| Seedance V1.5 | ~$0.10-0.20 | ~30-45s |

Veo is ~10x more expensive than Seedance V2. It's rarely the right default for production UGC.

---

## When to Use Multiple Models

Real campaigns often layer models:

- **Nano Banana Pro** → persona image
- **Nano Banana Pro** → product composite (creator holding product)
- **Seedance V2** → animated UGC clip with lip sync
- **Kling 3** → optional cinematic b-roll intercuts
- **Adobe / Topaz** → upscale + post-editing

Don't pick one model — pick the right model per stage of the pipeline.

---

_Keep this file updated as models evolve. Seedance V3, Kling 4, Veo 4 all change the map when they drop._
