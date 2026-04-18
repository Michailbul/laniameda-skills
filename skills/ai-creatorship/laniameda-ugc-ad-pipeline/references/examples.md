# Examples — Sirio Berati's Seedance V2 Ground-Truth Demos

These are the 6 demos from the Sirio × Greg Isenberg walkthrough (2026-04-17). Use them as reference prompts and pattern libraries. Every demo here is a known-working Seedance V2 setup.

**Source:** `content-kb/sources/youtube/2026-04-17-seedance-v2-sirio/`

---

## Demo 1 — Green-Screen Character + Background Replacement

**Use case:** Replace two characters and the background in a green-screen shot from a single prompt. Motion preserved.

**Inputs:**
- Video 1: AI-generated green-screen video with 2 characters
- Image 1: replacement character 1 reference
- Image 2: replacement character 2 reference
- Image 3: background reference

**What makes it work:**
- Multi-input (video + 3 images) handled in one call
- Motion of original preserved via natural-language instruction
- All 3 replacement elements referenced by tag in prompt

**Pattern lesson:** Seedance V2 can treat a green-screen video as a motion skeleton. The characters are just textures on that skeleton. This unlocks cheap scene production — film once, cast infinitely.

**Business angle:** Production studios building demo clips for landing pages or social. Traditional equivalent cost: multi-day shoot + green-screen studio + post comp. Seedance: one prompt, ~60 seconds.

---

## Demo 2 — Virtual Try-On in Montreal (-30°C)

**Use case:** Sirio filmed himself in shorts in cold weather. AI put him in a winter outfit + added a bear walking by.

**Inputs:**
- Video 1: original footage (Sirio in shorts)
- Image 1: winter outfit reference
- (optional) reference for bear

**What makes it work:**
- Face stayed identical to original footage
- Outfit pattern matched exactly (boots, pants pattern, jacket cut)
- Bear was tracked by Sirio's eyes and head — showed the model understood spatial awareness
- Weather-appropriate detail not explicitly prompted but inferred from environment

**Sirio's note:** "Input was very simple. I didn't go into any details. I could have been way more specific and described my outfit so the outfit could have been more accurate."

**Pattern lesson:** Source footage carries the identity and motion. Outfit reference carries the product. Seedance only has to swap the fabric layer. This is why virtual try-on is one of the strongest commercial use cases.

**Business angle:** E-com. One model shoot, infinite outfit variants. Preserves identity + motion for consistent brand feel.

---

## Demo 3 — Ad Translation (Chinese → English with Character Swap)

**Use case:** Chinese-speaking model selling glasses → English-speaking AI model with identical motion, wink, and camera focus.

**Inputs:**
- Video 1: original Chinese glasses ad
- Image 1: new AI-generated English-speaking persona

**Prompt (screenshot in video, reconstructed from context):**
Replace the woman in video 1 with image 1. Translate all spoken dialogue from Mandarin to English. Preserve the wink at second X, the hand-to-glasses gesture, the camera focus shift on the reveal. Preserve all product timing and framing. Match motion and expression arcs exactly.

**Result (English):** "It's flattering and versatile. Must have."

**What makes it work:**
- Wink timing preserved exactly
- Hand motion on glasses preserved exactly
- Camera focus blur shift preserved
- Lip sync adjusted for English phonemes
- Face identity locked to image 1 (not original speaker)

**Pattern lesson:** The source ad is the creative DNA. Translation is a surface-layer operation on top of that DNA. This is why ad translation via Seedance is the highest-leverage use case — you keep the expensive parts (timing, motion, framing) and change only the cheap parts (face, language).

**Business angle:** A/B testing creative across languages and demographics while holding the motion and framing constant to isolate the variable. Continuous optimization at near-zero marginal cost per variant.

---

## Demo 4 — 3D Product Template with Brand Texture Swap

**Use case:** Generic 3D package render (Freepik-style template) → swap in branded packaging design. Background color (yellow) preserved.

**Inputs:**
- Video 1: generic 3D package rotation
- Image 1: branded package design

**What makes it work:**
- Logo stayed consistent through rotation
- Yellow brand background preserved
- Product geometry from template unchanged
- Only surface texture changed

**Sirio's note:** "You can find any 3D asset out there. You can start applying texture to all these 3D assets by combining the source reference with image references."

**Pattern lesson:** Templates become infinitely reusable when branding is just a texture layer. Build a library of 10-20 package shapes, swap brand per campaign.

**Business angle:** Evergreen ad production. Pre-launch mockups. Multi-SKU testing. Localized packaging variants.

---

## Demo 5 — Video Extension (End Fill + Middle Fill)

**Two sub-cases:**

**5a — Extend the end:** 3-second clip → generate 15 more seconds continuing the scene. Sirio: "We have our 3 second video and we don't know what's happening next. We can recreate this entire scene."

**5b — Fill the middle:** Two video clips → Seedance generates the bridge between them.

**What makes it work:**
- Continuation uses last frame as anchor
- Middle-fill uses first and last frames as anchors
- Prompt describes what should happen in the gap
- Motion and lighting continuity preserved across the join

**Sirio's note (on middle-fill):** "There's two videos and it's going to figure out what goes in the middle, which is insane to me."

**Pattern lesson:** Most other models only extend the end. Middle-fill is a Seedance V2 differentiator. Means you can shoot / generate two hero shots and let AI build the connective tissue.

**Business angle:** Ad production pain point solved — "I need 3 more seconds of that shot" used to mean reshooting. Now it's a prompt. Same for traditional filmmaking.

---

## Demo 6 — AI Influencer + Lip Sync

**Use case:** AI persona (generated via Nano Banana Pro) delivering a product pitch with realistic emotion and lip sync.

**Inputs:**
- Image 1: persona reference (Nano Banana Pro generated)
- Image 2 (second example): product reference

**First example dialogue:**
> "This is what I mean. The way I breathe, the way I talk right after moving, it's all generated inside Enhancer."

**Second example dialogue (taste test):**
> "Okay quick taste test. Huh. Wait, that's actually nice. It's not super sweet. It's really clean. I wasn't expecting that. Yeah, I'd drink this."

**What makes it work:**
- Dialogue in quotation marks for lip sync
- Muscle-movement descriptions for emotional transitions (not emotion labels)
- Breath and pacing cues baked into the prompt
- Long detailed prompts — Seedance rewards specificity
- Product text preserved (soda bottle label stayed consistent)

**Sirio's quote on emotion prompting:**
> "You do not prompt emotions by saying 'the character is sad or the character is happy.' You have to describe the muscle movements... by describing the transition in emotion, transition in tone, in body language, it's able to achieve more realistic results."

**Sirio's quote on lip sync:**
> "Everything inside quotation marks is what the avatar will say."

**Pattern lesson:** This is the cornerstone demo — every rule in the skill flows from this one. Muscle movements, quotation marks, long prompts, Nano Banana Pro for source image.

**Business angle:** UGC at infinite scale. AI influencers that never leave, never raise rates, always on-brand.

---

## Meta-Lessons Across All 6 Demos

1. **Multi-input is the superpower.** Every demo used 2+ inputs. Text-to-video is a fallback; multi-input is the product.

2. **Source references determine ceiling.** Great references → great output. Mediocre references → mediocre output, regardless of prompt quality.

3. **Motion preservation is underrated.** Demos 1, 2, 3, 5 all preserved motion from a source video. This is where Seedance beats alternatives.

4. **Specificity beats cleverness.** Sirio's best results come from long detailed prompts, not clever short ones. Opposite of Midjourney/Kling instincts.

5. **Claude Opus 4.6 is the prompt optimizer.** Named specifically as best for vision-model prompting.

6. **The editor framing matters.** Sirio kept repeating: "Seedance V2 is not just a generator, it's an editor." Every demo reinforces this — the model operates on existing content, not from scratch.

---

## How to Use This File

When starting a new UGC campaign:
1. Find the demo that most closely matches the use case
2. Read the "What makes it work" + "Pattern lesson"
3. Load the matching template from `prompt-templates/`
4. Adapt the pattern to the specific brand/product
5. Generate and compare to the reference

If results drift from expected quality, come back to this file and diagnose which lesson wasn't applied.
