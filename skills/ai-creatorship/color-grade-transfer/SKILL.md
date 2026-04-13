---
name: color-grade-transfer
description: >
  Transfer cinematic color grading from a reference image onto a source photo using Nano Banana 2.
  Use when the user wants to apply a cinematic look, color style, mood, or tonal treatment from one image to another.
  Also triggers when user mentions: "match the colors", "apply this look", "transfer the grade", "make it look like this",
  "copy the mood", "apply color grading", "stylize my photo like this", "cinematic color transfer", or shares two images and asks to blend/match styles.
---

# Color Grade Transfer — Nano Banana 2

## Your Role for This Skill

When this skill activates, you are operating as a **professional colorist**. You think in the language of color science and cinematography — not generic descriptions.

Before running anything: **analyze the reference image like a colorist would.** Read the grade, name it precisely, then encode that reading into the prompt. This is what separates a mediocre transfer from one that actually holds the look.

---

## Step 0 — Analyze the Reference Like a Colorist

Before touching the script, read the reference image across these axes:

**Tonal structure**
- Where do the shadows sit? Lifted (milky/crushed black) or deep/pure black?
- How compressed are the highlights — blown to white, or rolled off softly?
- What's the overall contrast curve — flat/matte, standard, or punchy S-curve?

**Color science**
- Shadow hue: cool (blue/teal/cyan) or warm (amber/orange)? Neutral?
- Highlight hue: warm (golden/orange) or cool (white/blue)?
- Midtone cast: is there a dominant hue in skin tones and neutrals?
- Classic looks to name explicitly: teal-orange, bleach bypass, day-for-night, warm analog, cool Scandinavian, vintage fade, high-contrast noir

**Saturation profile**
- Fully desaturated (black & white or near), muted/film-like, neutral, or pushed/vivid?
- Does saturation vary by luminance (shadows desaturated, highlights vivid — or vice versa)?

**Film / grain / texture cues**
- Is there grain or texture visible? Fine, coarse, colored?
- Does it feel digital-clean or analog-warm?

**Name the look.** Examples:
- "Teal-orange cinematic — lifted shadows with cyan push, warm orange skintones, moderate contrast"
- "Bleach bypass — desaturated midtones, crushed blacks, blown highlights, high contrast"
- "Warm golden hour analog — amber shadows, ivory highlights, slightly faded blacks, low grain"
- "Cool editorial — neutral shadows, desaturated cool midtones, slightly lifted blacks"

This named description goes into `--extra-prompt` to reinforce the model's transfer.

---

## What You Need

- **Image 1 (source)** — the photo whose content must be preserved
- **Image 2 (reference)** — the image whose color grade you want to apply

If the user hasn't provided both, ask before proceeding.

---

## How to Run It

Use the bundled script. It calls Nano Banana 2 (`gemini-2.0-flash-preview-image-generation`) with both images in a single API call.

**Standard run (after colorist analysis):**
```bash
uv run ~/skills/color-grade-transfer/scripts/color_grade_transfer.py \
  --source path/to/source.jpg \
  --reference path/to/reference.jpg \
  --filename YYYY-MM-DD-HH-MM-SS-graded.png \
  --resolution 2K \
  --extra-prompt "[YOUR COLORIST READING — named look + key axes]"
```

**Example with real colorist extra-prompt:**
```bash
uv run ~/skills/color-grade-transfer/scripts/color_grade_transfer.py \
  --source source.jpg \
  --reference blade-runner-2049-ref.jpg \
  --filename 2026-04-01-22-00-00-graded.png \
  --resolution 2K \
  --extra-prompt "Teal-orange cinematic grade: push shadows to teal-cyan, skintones to warm amber-orange, lifted blacks (not crushed), soft highlight rolloff, moderate contrast S-curve, filmic grain texture."
```

**Filename pattern:** `YYYY-MM-DD-HH-MM-SS-descriptive-name.png`

**API key:** Script reads `GEMINI_API_KEY` from env. Pass `--api-key KEY` to override.

---

## Base Prompt (built into the script)

The script always sends this as the foundation — your `--extra-prompt` appends on top:

```
Transfer the exact color correction and tonal treatment from Image 2 onto Image 1.
Preserve the frame composition completely: framing, focus, and lighting direction must remain unchanged.
Do not alter the subject's pose, depth of field, or camera perspective.
```

---

## Workflow

1. **Analyze the reference** using the colorist framework above — name the look
2. **Confirm both image paths** exist
3. **Run at 2K** with colorist reading encoded in `--extra-prompt`
4. **Evaluate the output:**
   - Does the grade match (shadows, midtones, highlights, saturation)?
   - Is the source composition intact?
5. **Iterate if needed** — tighten the `--extra-prompt` based on what drifted
6. **Final pass at 4K** once the grade is locked

---

## Colorist Language Cheat Sheet (for --extra-prompt)

Use these terms — they translate directly into color science the model understands:

| What you mean | What to write |
|---|---|
| Shadows pushed blue/green | "teal shadows", "cyan shadow push", "cool crushed blacks" |
| Warm skintones | "amber midtones", "orange-warm skintones", "golden skin bias" |
| Faded/low contrast look | "lifted blacks", "milky shadows", "low contrast matte" |
| Punchy cinematic contrast | "deep blacks", "S-curve contrast", "punchy highlights" |
| Desaturated film look | "muted saturation", "desaturated midtones", "analog color fade" |
| Blown highlights | "soft highlight rolloff", "clipped whites", "blown specular" |
| Grain/texture | "fine film grain", "coarse analog grain", "clean digital — no grain" |
| Warm overall tone | "warm amber cast", "golden hour toning", "orange-yellow bias" |
| Cool/Scandinavian | "cool neutral grade", "desaturated blue-grey midtones", "cold ambient" |

---

## Troubleshooting

| Symptom | Fix |
|---|---|
| Grade transfer too subtle | More specific `--extra-prompt` — name the shadow hue, highlight hue, and contrast explicitly |
| Composition shifted or pose changed | Add to extra-prompt: "Absolutely do not alter the subject position, crop, or perspective." |
| Skin tones off | Add: "Preserve natural skin tones — only shift color cast in shadows and highlights." |
| Highlights blown when they shouldn't be | Add: "Preserve highlight detail — soft rolloff only, no clipping." |
| Script fails | Confirm `GEMINI_API_KEY` is valid and set |

---

## Good Reference Sources

- Film stills: **Blade Runner 2049** (teal-orange), **Manchester by the Sea** (desaturated naturalistic), **The Godfather** (warm amber), **Mad Max: Fury Road** (warm high-contrast), **Call Me by Your Name** (warm golden summer)
- **Roger Deakins** stills — precise, controlled, often desaturated with subtle warmth
- **Criterion Collection** covers — wide range of intentional grades
- Screenshot directly from a streaming service — pause on the exact frame you want, screenshot it

---

## What This Skill Does NOT Do

- Does not change composition, subject pose, or camera perspective
- Does not add/remove objects or elements
- This is **color transfer only** — not full stylization or concept transfer
- For full image stylization or generative edits → use `nano-banana-pro` skill
