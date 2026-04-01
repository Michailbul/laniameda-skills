---
name: brand-visuals-ai
description: >
  Translates a brand identity into an AI visual production kit — a Visual DNA spec,
  prompt directions, and asset workflow for creating brand visuals with generative AI
  (text-to-image, image-to-image, image-to-video). Use this skill whenever the user
  is designing a brand and wants to create visuals with AI tools. Triggers include:
  "design visuals for my brand", "create AI prompts for my brand", "I want to design
  [product/brand] with AI", "help me make brand assets", "generate mockups for my product",
  "design a brand for X and create visuals", or any request combining brand work with
  generative AI image or video creation. Always use this skill BEFORE writing any image
  or video prompt for a brand project — it keeps everything consistent and on-brand.
  Works from a full brand brief OR a rough idea.
---

# Brand Visuals AI

Turns a brand into an AI-ready visual production system. Output: a **Visual DNA** spec
and **prompt directions** the creator can take into any generative AI tool.

Goal: **lead the creator, propose directions, maintain consistency.**

---

## STEP 1 — START WITH THE RIGHT QUESTIONS

Before anything else, ask these three things if you don't already know them:

1. **Who is your customer?**
2. **How do you want your brand to feel?**
3. **What is a good example you can steal from?** (brand, film, aesthetic — any industry)

These three answers drive everything. Don't skip them.

---

## STEP 2 — BRAND INTAKE

Check if a saved `[brand-name]-brand` skill exists. If yes, load it and skip to Step 3.

If no brand exists, collect what you need:

| Field | Example |
|---|---|
| Brand name + what it is | PawHaus — premium streetwear for French Bulldogs |
| Target customer | French Bulldog owners, 25–40, urban, fashion-conscious |
| Brand feel (3–5 words) | Bold, urban, playful, luxury |
| Reference example to steal from | Supreme meets luxury pet |
| Assets needed | See checklist below |

If you have a URL or uploaded images — analyze them first, only ask for gaps.

> If no brand system exists yet, offer to run `brand-guidelines-builder` first.
> For quick projects, proceed with what you have and fill gaps with judgment.

---

## STEP 3 — ASSET CHECKLIST

Use this as the canonical list. Go through it with the user and mark what's needed.
Not everything is required for every project — prioritize what matters for the stage.

### Core identity (always start here)
- [ ] **Logo** — wordmark or wordmark + symbol
- [ ] **Logomark** — standalone symbol / icon version
- [ ] **2 fonts** — heading font + body/copy font
- [ ] **Colour palette** — full palette (primary + secondary + neutrals + accent)

### Extended brand system (when ready to go deeper)
- [ ] **Custom illustrations** — brand illustration style
- [ ] **Custom icons** — icon set in consistent style
- [ ] **Consistent styles** — lines, weights, spacing, UI rules
- [ ] **Alignment with target customer** — does it visually speak to them?

### Production assets (AI-generated)
- [ ] Product hero shot
- [ ] Product in lifestyle scene
- [ ] Web / landing page hero image
- [ ] Social posts / covers
- [ ] Brand texture / background
- [ ] Promo video (image-to-video)

---

## STEP 4 — DEFINE THE VISUAL DNA

Distill the brand into a **Visual DNA block** before writing any prompt.
This is the consistency anchor — every prompt inherits from it.

```
VISUAL DNA: [Brand Name]
────────────────────────────────────────────────
MOOD:        [2–3 words — e.g. "cinematic, raw, urban"]
PALETTE:     Primary #XXXXXX | Secondary #XXXXXX | Accent #XXXXXX
SURFACES:    [e.g. "worn leather, raw concrete, brushed metal"]
LIGHT:       [what the light does — e.g. "warm side light raking across
              the surface, deep shadows on the opposite side, no fill"]
COMPOSITION: [e.g. "tight crops, negative space, centered subjects"]
REFERENCES:  [2–3 visual touchstones — films, brands, photographers]
AVOID:       [e.g. "stock photo feel, white backgrounds, cartoon style"]
────────────────────────────────────────────────
```

**Lighting rule:** describe what light *does*, never what it *is*.
"A shaft of warm amber light falls across the left side, everything else
drops into near-black" — not "there is a softbox on the left."

---

## STEP 5 — PROMPT DIRECTIONS

For each asset the user needs, write a prompt direction — a starting point to iterate from.

### Prompt anatomy (always use this order)

```
[SUBJECT — what / who, doing what]
[ENVIRONMENT — where, what surfaces, background]
[LIGHT — what it does, direction, quality, temperature]
[MOOD / TEXTURE — material feel, atmosphere]
[COMPOSITION — framing, crop, angle]
[OUTPUT STYLE — photorealistic / editorial / cinematic / etc.]
```

### Format per asset

```
ASSET: [Name]
APPROACH: [text-to-image / image-to-image / image-to-video]

PROMPT DIRECTION:
[Plain descriptive language. Visual DNA elements baked in.
Describe the scene as if painting a picture.]

VARIATIONS TO TRY:
• [Different angle, lighting, or crop]
• [Push a different personality aspect]

WATCH FOR:
• [1 common failure mode + fix]
```

### Notes by asset type

**Logo / Logomark**
Generate in Ideogram or Recraft.ai — these handle typography and graphic marks
better than general image models. Try multiple directions (wordmark only, icon only,
combined) and iterate on the strongest.

**Colour palette**
Use coolors.co to explore and lock the palette before generating anything.
Pull hex values from there into the Visual DNA block. Don't guess colors —
lock them first, then paste into prompts.

**Product hero shot**
Always generate the product isolated first (neutral background, clean light,
straight-on angle). That image becomes the reference input for all lifestyle scenes.

**Lifestyle / scene shots**
Image-to-image from the isolated product shot. Describe the new environment and
light — the product stays consistent because it's the input.

**Promo video**
Generate a strong still keyframe first. That keyframe is your image-to-video input.
Never go to video from a text prompt alone — always start with a locked image.

**Text on images (social, web)**
Generate the background / scene first. Add text in a design tool afterward.
Don't fight text rendering in image models.

---

## STEP 6 — CONSISTENCY STRATEGY

Two things keep all assets feeling like one brand:

**1. Visual DNA as prompt anchor**
Every prompt pulls from the same mood, palette, light behavior, surfaces, and avoids.
Paste the relevant lines directly — don't rewrite them per asset.

**2. Hero reference images**
After generating the first 2–3 hero images, pick the one that feels most on-brand.
Use it as the style reference / img2img seed for everything that follows.
Everything else should feel like it lives in the same world as that image.

---

## STEP 7 — DELIVER

```
# AI Visual Production Kit: [Brand Name]

## Visual DNA
[Block from Step 4]

## Asset Checklist
[Marked-up list from Step 3]

## Prompt Directions
[All asset blocks from Step 5]

## Consistency Strategy
[2-point summary from Step 6]
```

After delivering:
- Offer a downloadable `.md` file
- Offer to go deeper on any specific asset
- Offer to save as a `[brand]-visuals` skill for the project

---

## AGENT NOTES

- Always start with the three questions: customer, feel, reference to steal from.
- Use the asset checklist every time — it keeps scope clear.
- Propose directions, don't over-specify. The creator iterates.
- Check `design-inspiration` skill before finalizing visual direction.
- Stay tool-agnostic except where a tool is genuinely the right fit for the task
  (Ideogram/Recraft for logos, coolors for palette — these are worth naming).
