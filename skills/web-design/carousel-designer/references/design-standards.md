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

---

## Fonts (v2)
```
Display:  Bebas Neue  (Google Fonts CDN)
Body:     Space Grotesk (Google Fonts CDN)
Mono:     JetBrains Mono (Google Fonts CDN)
```
**NEVER use:** Arial, Inter, Roboto, Helvetica Neue as primary display font.
Arial Black is acceptable as a fallback only.

Google Fonts link tag (required in every HTML):
```html
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
```

---

## Typography scale
| Role              | Font      | Size  | Weight |
|-------------------|-----------|-------|--------|
| Bleed headline    | display   | 220px | —      |
| Hero headline     | display   | 180px | —      |
| Section headline  | display   | 120px | —      |
| Metric value      | display   | 112px | —      |
| Equation number   | display   | 88px  | —      |
| Stack card title  | display   | 58px  | —      |
| Body/subtitle     | body      | 38px  | 600    |
| Checklist label   | body      | 36px  | 700    |
| Checklist support | body      | 30px  | 400    |
| Stack card body   | body      | 28px  | 400    |
| Kicker / badge    | mono      | 20-22px | 700  |
| Slide counter     | mono      | 18px  | 700    |
| Table header      | mono      | 22px  | 700    |
| Table row         | body      | 30px  | 600    |

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
| Color          | Hex       | Allowed uses                          | Never use for              |
|----------------|-----------|---------------------------------------|----------------------------|
| brand (text)   | #09090B   | All body text, borders, structure     | Backgrounds (except terminal) |
| secondary gold | #BA943B   | Kicker backgrounds only               | Headlines, borders         |
| primary purple | #8566AF   | Shadow-offsets, badges, eq operators  | Dominant fills             |
| accent red     | #EA3F2C   | CTA text, equation answer, 1 emphasis | More than 1 element/slide  |
| white          | #FFFFFF   | Slide bg, card bg                     | Text on light bg           |

Accent (`#EA3F2C`) on ≤1 element per slide — no exceptions.

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
