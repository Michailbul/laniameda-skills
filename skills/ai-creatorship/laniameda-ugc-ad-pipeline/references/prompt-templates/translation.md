# Ad Translation Template

**Use when:** an existing ad is working in one language — take it to a new market. Preserve motion, camera, framing, energy. Swap speaker (optional), swap language, re-lip-sync.

**Inputs required:**
- Video 1: original ad (the motion + framing ground truth)
- Image 1: new persona reference (locked face) — can be same or different from original speaker
- Image 2: product image from the ad (for text/logo preservation)

---

## Template

```
Multi-input video generation, Seedance V2.

SOURCE VIDEO REFERENCE: Use video 1 as the motion, camera, and framing reference.
Preserve the exact timing of all gestures — winks, hand movements, head turns,
camera focus shifts. Preserve lighting setup. Preserve the product placement
and how it moves through the frame.

SUBJECT SWAP: Replace the speaker in video 1 with the woman from image 1.
Same face exactly, same features from image 1. The new speaker inherits all
motion, gestures, and timing from video 1 — the only thing that changes is
the face and the spoken language.

PRODUCT: The product from image 2 stays identical throughout — label text, logo,
color, and proportions preserved. Product position and motion match video 1 exactly.

LANGUAGE SWAP: The new speaker delivers the dialogue in [TARGET LANGUAGE]. The
mouth shapes and lip sync match the new language, not the original. Dialogue
timing matches the original ad's rhythm — each gesture and camera beat lines up
with the translated phrase at the same point in the clip.

DIALOGUE: She says (in [TARGET LANGUAGE]):
"[TRANSLATED LINE 1 — match timing of original line 1]"
"[TRANSLATED LINE 2 — match timing of original line 2]"

EMOTIONAL CONTINUITY: Preserve the exact emotional arc of the source video.
If the original speaker winks at second 2, the new speaker winks at second 2
with the same intensity. If the original smiles on the verdict, the new speaker
smiles on the verdict.

CAMERA: Match video 1 frame-for-frame — same angle, same focal length, same
push-in / pan / handheld feel. Do not reinterpret the camera.

LIGHTING: Match video 1 exactly — same direction, same color temperature, same
shadow pattern on face.

CONSISTENCY: Face identical to image 1 (new persona). Product identical to
image 2. Motion identical to video 1. Language is the only intentional change
beyond the face swap.

DURATION: Match video 1 exactly.
```

---

## Swap points per language variant

Duplicate the base prompt, change only:

- `[TARGET LANGUAGE]` — e.g. Spanish (neutral), French (Parisian), Japanese, Portuguese (Brazilian)
- Dialogue translation inside quotes — must be natural in-market, not word-for-word
- Optionally: persona image (for demographic match with target market)

Keep identical:
- Source video reference
- Product reference
- Camera, lighting, motion, timing notes
- Consistency lock

---

## Translation quality rules

**Do not translate literally.** Localize. A line that's casual in English needs to sound casual in the target language — not formal because the direct translation is formal.

**Match the syllable count roughly.** Lip sync works better when the translated line is roughly the same length as the original. Rewrite if needed.

**Preserve the hook structure.** If the original opens with a pattern interrupt, the translation opens with a pattern interrupt in that language's convention.

**Use a native speaker or Claude Opus 4.6 for translation.** Not Google Translate. Tell Claude:
> "Translate this UGC ad line to [LANG]. Match syllable count ±20%. Keep the casual conversational register. Use fillers natural in [LANG]. Return only the translation."

---

## Failure watchouts

- **Lip sync drift** — mouth shapes don't match the new language. Fix: ensure Seedance is running in lip-sync mode (dialogue in quotes), and the translation syllable count is close to original.
- **Motion loss** — new speaker stands still instead of inheriting gestures. Fix: add `"inherit all motion and gesture timing from video 1 exactly, do not simplify or drop gestures"`.
- **Face drift** — new speaker's face changes mid-clip. Fix: strengthen face-lock phrasing, use higher-res persona image.
- **Product text re-rendered in wrong language** — model translates the label. Fix: add `"product label text from image 2 preserved exactly in original language, do not translate or re-render label"`.

---

## Variation axes

**Pure language variants:** same persona, same product, swap language + translate dialogue. Fastest path to N market variants.

**Persona + language variants:** new persona per market (demographic match), swap language. More authentic per market but harder to scale.

**Hook variants within a language:** same persona, same language, swap opening line. Test which hook converts per market.

---

## Scaling to N languages

Production workflow for translating one ad to 10 markets:

1. Lock the persona (one new persona, or reuse original)
2. Run translation prompt through Claude Opus 4.6 for all 10 target languages at once
3. Review translations for natural register — flag anything too formal/stiff
4. Build 10 variant prompts using this template, only language + dialogue swapped
5. Submit all 10 to Seedance V2 in a batch
6. QA pass: watch each with native-speaker review if possible
7. Save to `variants/` with language code in folder name (`v1-es`, `v2-fr`, `v3-ja`, etc.)

---

## Example — Sirio's Chinese-to-English glasses ad

Source: Chinese-speaking model selling glasses with a wink, hand-to-glasses gesture, camera focus shift on reveal.

What was preserved:
- The wink at the specific beat
- The hand-to-glasses gesture on the verdict line
- The camera focus shift on the reveal
- The product (glasses) throughout

What changed:
- Speaker (new AI-generated persona)
- Language (Mandarin → English)
- Lip sync adjusted for English phonemes

Result: "It's flattering and versatile. Must have." delivered in English with the exact wink timing of the original.

Why it worked: the motion reference video carried all the expensive parts (timing, framing, gestures). The translation layer only had to swap face and language on top of that frame. This is why ad translation via Seedance V2 is cheaper than reshoots — you keep the creative DNA and change only the market signal.
