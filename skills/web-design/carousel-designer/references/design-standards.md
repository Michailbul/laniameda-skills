# Design Standards v2 — LinkedIn Carousel

## The Unforgettable Rule (most important)
Every carousel must have **one element** that works as a standalone viral image.
Ask before building: *"If someone screenshots just slide 1, would they stop scrolling?"*

Execution options:
- A bleed headline (text overflows right edge intentionally)
- An equation in huge monospace that tells the whole story
- A data table that no one has seen formatted like this before
- A stark comparison: one word left, one number right, nothing else

If the cover slide looks like 50 other LinkedIn posts → start over.

Additional validated rule (2026-04-03):
- Slide 1 must not only be visually strong — the hook copy must be readable in-feed. If the eyebrow or headline is too small to parse at thumbnail size, the slide fails even if the image is beautiful.

---

## Fonts (v2)
Use the active brand-system typography for the current brand context. Do not hardcode a single trio across all carousel work.

When working in the original LinkedIn brutalist mode, the defaults remain:
```
Display:  Bebas Neue  (Google Fonts CDN)
Body:     Space Grotesk (Google Fonts CDN)
Mono:     JetBrains Mono (Google Fonts CDN)
```

When working in Laniameda brand mode, follow the typography defined in the active brand guidelines (for example: Darker Grotesque / Inter / JetBrains Mono, plus approved alternates).

What matters more than the specific font names:
- strong scale contrast
- readable hook at thumbnail size
- clean hierarchy (eyebrow -> hero -> support)
- text contrast that survives complex image backgrounds

Google Fonts link tags should match the chosen type system.
Never use generic fallback-looking display typography as the intended design.

---

## Typography scale
Use the brand-system fonts for the current context, but preserve these hierarchy ratios and lessons:

| Role | Typical size range | Why |
|---|---:|---|
| Hero headline | 72–220px | Must dominate. If it doesn't instantly anchor the slide, it is too small. |
| Section / slide headline | 44–120px | Should clearly outrank every support element. |
| Eyebrow / kicker | 14–36px | This was a repeated failure point: too small = invisible. |
| Body / subtitle | 18–38px | Must stay readable on mobile. |
| Mono labels / chrome | 12–22px | Small but legible; never ghosted below useful contrast. |

### Repeated typography failures (validated)
| Failure | Why it was bad | Fix |
|---|---|---|
| Eyebrow at 12–14px over busy image | Lost immediately; hook context vanished | Increase size and/or weight; minimum 14px mono or ~28px display for image-led covers |
| Support text at 0.22–0.38 opacity | Felt elegant in theory, unreadable in practice | Raise to 0.55+ when over imagery; add text-shadow |
| Hero text top-anchored by padding | Read as layout drift, not intention | Center the hook block when the image is the hero |
| Bottom labels adapting to slide bg | Wrong mental model — they sit over the dark image fade | Keep image-layer labels light regardless of slide bg |
| Comparison badge / "VS" misaligned | Breaks polish instantly | Align with flex; if it still looks awkward, remove it |

Rule: pick fonts from the brand guidelines, but solve for size, hierarchy, position, and contrast first.

---

## Slide structure rules
- **1 idea per slide.** Period.
- **Hierarchy per slide:** kicker → headline → ONE visual element → (optional) subtitle
- Slide counter `"0N / 07"` bottom-right on every slide (absolute positioned)
- `chrome` div is flex column — use `mt-auto` to push elements to bottom

### Slide patterns by type
| # | Type      | Required elements                                        |
|---|-----------|----------------------------------------------------------|
| 1 | Cover     | kicker, headline (bleed or hero), subtitle, badge-row   |
| 2 | Problem   | kicker, section-headline, subtitle                      |
| 3 | Stat/Math | kicker, section-headline, equation OR metric-card       |
| 4 | Stat/Math | kicker, section-headline, data-table OR metric-card     |
| 5 | System    | kicker, section-headline, checklist OR terminal-block   |
| 6 | Solution  | kicker, section-headline, stack-grid OR asymmetric      |
| 7 | CTA       | kicker, section-headline, ordered-list, closing-line    |

---

## Color usage rules
Always follow the active brand system first.

Validated anti-patterns for carousel backgrounds:
- purple-adjacent backgrounds that read off-brand
- blue-grey backgrounds that flatten warmth
- pure black / pure white instead of warm near-black / warm light neutrals

For Laniameda-branded carousels, the validated carousel background set is:
- Obsidian `#0A0805`
- Carbon `#191919`
- Graphite `#3A3A3A`
- Linen `#FFF4EA`
- Amber `#E8A838`

Validated rejects:
- Charcoal Violet `#3D2E42`
- Slate Blue `#4A5E7A`
- pure black `#000000`
- pure white `#FFFFFF`

Accent on ≤1 element per slide remains the rule.

---

## Spacing system (4px grid)
- Slide padding (chrome): `padding: 78px 76px`
- After kicker: `mt-8` (32px)
- After headline: `mt-6` to `mt-8`
- Between list items: `gap-5` or `gap-6`
- Between stack cards: `gap-4`
- Shadow-offset cards: `shadow-[12px_12px_0_0_#8566AF]`
- CTA closing line: `mt-auto` + `border-t-[4px] border-brand pt-7`
- Slide counter: `absolute bottom-[28px] right-[32px]`

---

## Structural rules
- Black border: `border-left/right: 12px; border-top/bottom: 14px; color: #09090B`
- Grid overlay via `::before` — 54px cell, 7% opacity
- Grain overlay via `::after` — SVG feTurbulence noise, 2.5% opacity
- `.chrome` is `z-index: 1`, overlays both pseudo-elements
- Slide counter is `z-index: 2`

---

## Quality checklist (run after every render)
### Slide 1 / Hook
- [ ] Headline reads at thumbnail size
- [ ] Eyebrow is visible, not decorative dust
- [ ] Hook block feels centered/intentionally placed when image-led
- [ ] No opaque text container over the hero image unless explicitly part of the brief

### Layout
- [ ] No text clipping at right/bottom edges
- [ ] Slide counter present bottom-right every slide
- [ ] Black border visible all 4 sides
- [ ] Grid + grain overlays visible but subtle

### Fonts
- [ ] Bebas Neue loading (check: headings should be condensed, not wide)
- [ ] Space Grotesk loading (check: body text should feel modern, not generic)
- [ ] JetBrains Mono loading (check: monospace elements should look code-like)

### Hierarchy
- [ ] One dominant visual element per slide
- [ ] Kicker visible on every slide
- [ ] Slide 1 passes the unforgettable test

### Brand
- [ ] Accent used on ≤1 element per slide
- [ ] Gold only on kicker backgrounds
- [ ] No Lorem Ipsum or placeholder text

### Content
- [ ] All numbers are from the brief (not invented)
- [ ] CTA keyword present on slide 7
- [ ] Slide 6 solution is clearly differentiated from slide 5 problem

---

## Common Codex failures → feedback format
```
slide_1.headline: Bebas Neue not loading — fallback to Impact, add font preconnect
slide_3.equation: accent on 2 elements — keep only on the answer number
slide_4.metric-card: no shadow-offset — add shadow-[12px_12px_0_0_#8566AF]
slide_5.checklist: 5 items, too many — cut to 3 strongest
slide_7.cta: no keyword — add "Comment THROUGHPUT and I'll send it"
global: slide counter missing — add .slide-counter span to all 7 slides
```
