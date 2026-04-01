# Font Selection Guide — Laniameda Context

## Quick Decision Matrix

| Need | Font | Why |
|---|---|---|
| Tech / SaaS product | Manrope SemiBold | Clean, legible, contemporary |
| AI-native / crypto / Web3 | Space Grotesk Bold | Techy retro-futuristic DNA |
| Creative studio / poster | Syne ExtraBold | Graphic, condensed, art-center |
| Old money / editorial | Fraunces | Warm expressive serif |
| App / dashboard UI | Inter SemiBold | Neutral, readable, huge weight range |
| Startup / lifestyle brand | Albert Sans | Soft, approachable, not corporate |
| Blog / long-form | Merriweather Bold | Screen-optimized, comfortable |
| Magazine / luxury | Tenor Sans | Narrow, refined, minimal |
| Big tech aesthetic | Google Sans Bold | Rounded, friendly, Google-clean |
| Enterprise / design system | IBM Plex Sans | Technical precision + human warmth |

## Laniameda Brand Stack

Primary visual language: dark, cinematic, AI-native, editorial

**Recommended stack:**
- **H1 / Hero:** Space Grotesk Bold — most "laniameda" of the 10
- **H2 / Section:** Syne ExtraBold — strong graphic moments
- **UI / Nav / Body:** Manrope — already in use, proven
- **Product / Docs:** Inter — safe universal fallback

## Typography Rules (from Amir's method)

### Kerning/Tracking
- Headlines: **-3% to -7%** (tight = luxurious)
- Body text: **0% to -2%** (natural to slightly tight)
- All-caps labels: **+5% to +10%** (open = proper spacing)

### Leading (Line Height)
- Display/Hero headline: **0.80–0.90** (blocky, solid, strong element)
- Subheadings: **0.95–1.05** (balanced)
- Body copy: **1.4–1.6** (comfortable reading)

### Color Pairings (high contrast)
- `#0A0A0A` bg + `#FFFFFF` text — maximum contrast, dark mode
- `#050505` bg + `#39FF14` accent — cyber/neon for Space Grotesk
- `#F5F0E8` bg + `#1A1A1A` text — warm editorial for Fraunces
- `#FFFFFF` bg + `#0A0A0A` text — clean minimal for Tenor Sans

## When to Use Reference Specimen

Use `--input-image specimen.png` when:
- Font weight precision matters (SemiBold vs Bold distinction)
- Kerning accuracy is critical
- Generating for brand/client work (not exploratory)

Skip specimen when:
- Quick exploration / draft pass
- Font is very distinctive (e.g. Fraunces — model knows it well)
- Testing different style directions

## All Specimens Location

After running `python3 scripts/generate_specimen.py --all`:
```
specimens/
  manrope-semibold.png
  fraunces-regular.png
  syne-extrabold.png
  inter-semibold.png
  albert-sans-semibold.png
  merriweather-bold.png
  tenor-sans-regular.png
  space-grotesk-bold.png
  google-sans-bold.png
  ibm-plex-sans-semibold.png
```
