---

## name: ai-typography
description: >
  Generate premium branded typography visuals using Nano Banana Pro + font specimen reference images.
  Replicates the LTX Elements workflow (font consistency via reference image injection) without needing LTX Studio.
  Use when: user wants to generate a typographic design with a specific font, needs branded text visuals,
  wants to apply font presets from the Amir Mushich method.
  Triggers on: "generate typography", "font design", "text visual", "branded text", "type treatment",
  "font preset", "ai typography", "make this look elite", "typographic visual".

# AI Typography Skill

Generate premium typographic visuals using Nano Banana Pro with font specimen reference images for consistency.

## The Method (No LTX Needed)

**What LTX Elements does:** Injects a font specimen image as a visual reference so the model stays consistent to that exact font weight, kerning, and spacing.

**How we replicate it:** Pass a pre-rendered font specimen PNG as `--input-image` to Nano Banana Pro. Same result — no LTX required.

Adapt the 

---

## Workflow

(

### Step 1 — Generate or use existing font specimen

```bash
# Generate a specimen for a font (one-time, store in specimens/)
python3 ~/skills/ai-typography/scripts/generate_specimen.py \
  --font "Manrope" \
  --weight "SemiBold" \
  --output ~/skills/ai-typography/specimens/manrope-semibold.png
```

Or use pre-built specimens from `specimens/` directory.

### Step 2 — Run typography generation

```bash
uv run ~/skills/nano-banana-pro/scripts/generate_image.py \
  --prompt "<typography prompt from templates below>" \
  --input-image "~/skills/ai-typography/specimens/<font>-<weight>.png" \
  --filename "$(date +%Y-%m-%d-%H-%M-%S)-typography-<font>.png" \
  --resolution 2K
```

---

## 10 Font Presets (Amir Mushich Method)

### 1. MANROPE — Clarity & Confidence

**Best for:** Tech, SaaS, digital products, interfaces, contemporary lifestyle brands
**Amir's personal pick** for social media designs.

**Settings:** SemiBold headlines, Regular body. Tracking: -4%, Leading: 0.85

**Prompt template:**

```
A premium typographic design featuring the exact text "[YOUR TEXT]" in Manrope SemiBold.
Clean, geometric sans-serif letterforms. Dark background #0A0A0A, white text #FFFFFF.
Tracking: tight (-4%). Line height: 0.85. Large display size, centered composition.
Minimal, contemporary, tech-forward aesthetic. No decorative elements. High contrast.
```

---

### 2. FRAUNCES — Premium "Old Money"

**Best for:** Heritage brands, food, editorial, friendly fintech, branding with classic serif voice

**Settings:** Regular or Light. Tracking: 0%, Leading: 0.9

**Prompt template:**

```
A premium typographic design featuring the exact text "[YOUR TEXT]" in Fraunces Regular.
Optical-size serif with warm personality. Cream/off-white background #F5F0E8, dark text #1A1A1A.
Tracking: natural (0%). Line height: 0.9. Large editorial headline treatment.
Old money aesthetic, refined, expressive serif personality.
```

---

### 3. SYNE — Artsier, Experimental

**Best for:** Creative studios, cultural institutions, posters, edgy editorial

**Settings:** Bold or ExtraBold. Tracking: -6%, Leading: 0.8

**Prompt template:**

```
A bold experimental typographic poster featuring the exact text "[YOUR TEXT]" in Syne ExtraBold.
Condensed geometric sans, strong graphic shapes. Black background, white or accent color text.
Tracking: very tight (-6%). Line height: 0.8. Maximum impact display treatment.
Contemporary art center aesthetic. Graphic, condensed, high visual weight.
```

---

### 4. INTER — System Workhorse

**Best for:** Apps, dashboards, documentation, any UI needing maximum clarity

**Settings:** Medium or SemiBold for display. Tracking: -2%, Leading: 1.0

**Prompt template:**

```
A clean UI-inspired typographic design featuring the exact text "[YOUR TEXT]" in Inter SemiBold.
Neutral, highly legible, humanist sans-serif. Background #111111, text #F0F0F0.
Tracking: slightly tight (-2%). Line height: 1.0. Balanced, system-native feel.
Digital product aesthetic, functional, clear visual hierarchy.
```

---

### 5. ALBERT SANS — Friendly Modern

**Best for:** Startups, lifestyle brands, landing pages, marketing sites

**Settings:** SemiBold or Bold for headlines. Tracking: -3%, Leading: 0.9

**Prompt template:**

```
A friendly modern typographic design featuring the exact text "[YOUR TEXT]" in Albert Sans SemiBold.
Soft approachable geometric grotesque. Warm dark background, clean white text.
Tracking: slightly tight (-3%). Line height: 0.9. Contemporary, approachable, startup aesthetic.
Less corporate than Helvetica, more personality. Clean negative space.
```

---

### 6. MERRIWEATHER — Editorial Serif

**Best for:** Blogs, editorial platforms, long-form content brands

**Settings:** Regular or Bold. Tracking: 0%, Leading: 1.2

**Prompt template:**

```
An editorial typographic design featuring the exact text "[YOUR TEXT]" in Merriweather Bold.
Screen-optimized serif, large x-height, sturdy forms. Off-white background, deep dark text.
Tracking: natural (0%). Line height: 1.2. Editorial magazine layout feel.
Premium publishing aesthetic, journalistic, authoritative.
```

---

### 7. TENOR SANS — Refined, Minimal

**Best for:** Magazines, luxury minimal brands, sophisticated editorial

**Settings:** Regular (only weight). Tracking: 2–5%, Leading: 1.1

**Prompt template:**

```
A refined minimal typographic design featuring the exact text "[YOUR TEXT]" in Tenor Sans Regular.
Narrow proportions, subtle editorial personality. White or near-white background, near-black text.
Tracking: open (3%). Line height: 1.1. Luxury magazine headline treatment.
Sophisticated, refined, editorial minimalism.
```

---

### 8. SPACE GROTESK — Techy Retro-Futuristic

**Best for:** Web3/crypto, dev tools, tech startups, data interfaces

**Settings:** Medium or Bold. Tracking: -5%, Leading: 0.85

**Prompt template:**

```
A techy retro-futuristic typographic design featuring the exact text "[YOUR TEXT]" in Space Grotesk Bold.
Inherits code DNA from Space Mono. Dark background #050505, bright accent text (electric blue or green).
Tracking: tight (-5%). Line height: 0.85. Digital, terminal-inspired aesthetic.
Developer tool / Web3 visual language. Distinctive, technical, slightly retro.
```

---

### 9. GOOGLE SANS — Clean Big Tech

**Best for:** Product pages, marketing sites, Google-adjacent brand aesthetic

**Settings:** Medium or Bold. Tracking: -2%, Leading: 0.9

**Prompt template:**

```
A clean modern typographic design featuring the exact text "[YOUR TEXT]" in Google Sans Bold.
Rounded geometric humanist forms. Light or dark background, strong contrast text.
Tracking: tight (-2%). Line height: 0.9. Big tech, clean, product marketing aesthetic.
Friendly, modern, trustworthy. Bold heading treatment with generous negative space.
```

---

### 10. IBM PLEX SANS — Corporate Precision

**Best for:** Enterprise products, design systems, documentation, tech brands

**Settings:** SemiBold headlines, Regular body. Tracking: -2%, Leading: 0.95

**Prompt template:**

```
A corporate-precise typographic design featuring the exact text "[YOUR TEXT]" in IBM Plex Sans SemiBold.
Technical humanist sans-serif, precision engineering aesthetic. Dark background, clean white text.
Tracking: slightly tight (-2%). Line height: 0.95. Enterprise, systematic, authoritative.
Balances technical precision with human warmth. Design system scale.
```

---

## Pro Typography Settings

These aren't random — they're the difference between generic and premium:


| Setting                  | Value       | Effect                                   |
| ------------------------ | ----------- | ---------------------------------------- |
| **Tracking (headlines)** | -3% to -7%  | Tight, luxurious spacing                 |
| **Leading (headlines)**  | 0.8–0.9     | Blocky, solid headline as design element |
| **Leading (body)**       | 1.2–1.4     | Comfortable reading rhythm               |
| **All caps tracking**    | +5% to +10% | Proper letterspaced caps                 |


---

## Laniameda Font Recommendations

Based on brand aesthetic (dark, cinematic, AI-native, editorial):


| Role                    | Font          | Why                                            |
| ----------------------- | ------------- | ---------------------------------------------- |
| **Primary headlines**   | Space Grotesk | AI-native, techy retro — perfect for laniameda |
| **Secondary / UI**      | Manrope       | Already in use, clean, works everywhere        |
| **Editorial / feature** | Syne          | Most distinctive, poster-ready                 |
| **Body / product**      | Inter         | Safe, readable, system-native                  |
| **Luxury accent**       | Tenor Sans    | For premium/editorial contexts                 |


---

## Quick Reference (full workflow)

```bash
# 1. Generate a typography visual (pick font + replace text)
uv run ~/.codex/skills/nano-banana-pro/scripts/generate_image.py \
  --prompt "A premium typographic design featuring the exact text 'YOUR TEXT HERE' in Space Grotesk Bold. Techy retro-futuristic. Dark background #050505, electric text. Tracking: tight (-5%). Line height: 0.85." \
  --filename "$(date +%Y-%m-%d-%H-%M-%S)-type-spacegrotesk.png" \
  --resolution 2K

# 2. With reference specimen (higher font consistency)
uv run ~/.codex/skills/nano-banana-pro/scripts/generate_image.py \
  --prompt "..." \
  --input-image "~/.openclaw/skills/ai-typography/specimens/space-grotesk-bold.png" \
  --filename "$(date +%Y-%m-%d-%H-%M-%S)-type-spacegrotesk.png" \
  --resolution 2K
```

---

## Specimen Generation Script

See `scripts/generate_specimen.py` — generates a clean PNG specimen for any Google Font.
Run once per font, stored in `specimens/` for reuse.

---

## Source

Based on Amir Mushich's "10 AI presets to make your brand look elite" method.
Full juice: `laniameda-hq/knowledge-base/sources/article/2026-02-27-amirmushich-ai-font-presets/juice.md`