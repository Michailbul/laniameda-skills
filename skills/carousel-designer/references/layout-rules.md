# Layout & Design Rules — LinkedIn Carousel
# Professional standards. Follow precisely.

---

## 1. ALIGNMENT — the single most broken rule in AI-generated carousels

**Always left-align text. No exceptions.**
- `text-left` on everything inside `.chrome`
- Set `text-align: left` on the `.chrome` div itself as a default
- NEVER center-align body text, subtitles, or headlines
- NEVER justify text

**The one allowed exception:**
- Centered text ONLY on a single-word bleed headline where the word fills >80% of the slide width

**Why:** Left alignment creates a strong vertical axis. The eye has a clear entry point (top-left) and scans down. Center alignment makes slides feel like greeting cards — weak and amateur.

---

## 2. VERTICAL AXIS — the invisible spine

Every slide must have one clear vertical alignment axis running top to bottom.

**Rule:** All block-level elements start at the same left edge (76px from slide border = the chrome padding).

**Breaking it intentionally:** If you use an asymmetric layout or a bleed element, the break must be deliberate and singular — only ONE element deviates from the axis per slide.

```
✓ Good:
  [kicker         ]
  [headline       ]
  [subtitle       ]
  [metric card    ]
  
✗ Bad:
  [kicker    ]
       [headline]
  [subtitle         ]
```

---

## 3. SCALE CONTRAST — the most powerful tool in a carousel

Great slides use extreme scale contrast between elements:

**The ratio rule:** Main element should be 3–5× larger than supporting text.

```
✓ Strong contrast:
  KICKER      20px mono
  BIG NUMBER  112px display   ← 5.6× ratio
  label       20px mono

✗ Weak contrast:
  KICKER      24px
  Headline    72px             ← only 3× ratio, feels flat
  Subtitle    38px             ← too close to headline
```

**Practical application:**
- Equation slide: numbers at 88px, operators at 72px, unit labels at 32px → clear 3-tier hierarchy
- Metric slide: value at 112px, label at 20px → only 2 sizes, dramatic contrast
- Checklist slide: strong labels at 36px bold, support text at 30px regular → subtle but functional

---

## 4. NEGATIVE SPACE — what you remove matters more than what you add

**The 40% rule:** At least 40% of every slide should be empty (white or grid).

Signs you've violated this:
- Text touches or comes within 60px of the slide border (inside chrome padding)
- More than 4 distinct elements on a single slide
- Body text longer than 2 lines

**Spacing rhythm:**
- After kicker: exactly `mt-8` (32px)
- After headline: exactly `mt-6` (24px) to `mt-8` (32px)
- Between list items: `gap-5` (20px) minimum
- Between cards: `gap-4` (16px) minimum
- CTA bottom element: always `mt-auto` — let it breathe to the bottom

---

## 5. TYPOGRAPHIC HIERARCHY — 3 levels max per slide

Each slide should have exactly 2–3 typographic levels. Never more.

| Level | Role | Style |
|-------|------|-------|
| 1 | Dominant (headline/number) | display font, largest size |
| 2 | Supporting (subtitle/label) | body or mono, medium size |
| 3 | Tertiary (optional) | mono, smallest, muted opacity |

**Opacity trick for hierarchy without extra sizes:**
- Primary text: `text-brand` (full opacity, #09090B)
- Secondary text: `text-brand/70` (70% opacity)
- Tertiary/label: `text-brand/40` to `text-brand/50` (40-50% opacity)

This creates depth without adding more font sizes — the professional move.

---

## 6. LINE LENGTH — readability constraint

**Max line length for body text: 880px (max-w-[880px])**
At 38px body size, this allows ~18–22 characters per line — the readable sweet spot.

For smaller text (30px): `max-w-[820px]`
For kickers/badges: no max-width constraint (they're short by nature)

**Headline line length:**
- Hero/bleed headlines: allow overflow or set `max-w-none`
- Section headlines (120px): keep to 1–2 words per line naturally, never force wrapping with width constraints

---

## 7. CARD DESIGN — shadow-offset pattern

All card elements use the shadow-offset style (not rounded corners, not drop shadows):

```css
/* Standard card */
border: 4px solid #09090B;
background: #ffffff;
box-shadow: 12px 12px 0 0 #8566AF;   ← purple offset

/* Emphasis card (CTA, featured) */
box-shadow: 12px 12px 0 0 #09090B;   ← black offset

/* Secondary card */
box-shadow: 8px 8px 0 0 #BA943B;     ← gold offset
```

**NEVER use:**
- `border-radius` (brutalist = sharp corners)
- `box-shadow` with blur (soft/diffuse shadows are not part of this aesthetic)
- `drop-shadow` filter

---

## 8. COLOR BLOCKING — when to fill backgrounds

Slides are white by default. Use background color fills sparingly:

**Allowed fills:**
- Terminal block: `bg-brand` (near-black) — maximum 1 per carousel
- Kicker badge: `bg-secondary` (gold)
- Accent badge: `bg-accent` (red-orange)
- Asymmetric sidebar: `bg-primary/10` (very light purple tint)
- Table header: `bg-brand` (near-black)

**Never fill:**
- The entire slide background with color (the white + grid IS the design)
- More than 25% of a slide with a color block

---

## 9. THE GRID AS LAYOUT TOOL

The 54px grid is not just decoration — use it as an actual layout guide.

**Snap to grid:**
- Card widths should be multiples of 54px where possible
- Gap between grid-based elements: 54px (`gap-[54px]`) for major sections
- Minor gaps: 27px (`gap-[27px]`) for related items

**Grid-breaking:**
One element per slide may intentionally break the grid (bleed headline, oversized metric). All other elements must respect it.

---

## 10. SLIDE FLOW — narrative arc across the carousel

Each slide should set up the next. Transitions have logic:

```
Slide 1 (cover):   STATE THE TENSION      "Throughput > Prompts"
Slide 2 (problem): WHY IT MATTERS         "The math is brutal"
Slide 3 (stat):    PROVE IT WITH DATA     "48 shots × 6 gens = 288 videos"
Slide 4 (stat):    AMPLIFY THE PROOF      "That's 3h 13m at $54/month"
Slide 5 (system):  THE SOLUTION EXISTS    "3 things that fix it"
Slide 6 (tools):   MAKE IT CONCRETE       "Google Flow + Freepik Pro"
Slide 7 (CTA):     GIVE THEM THE NEXT STEP "Comment THROUGHPUT"
```

**Transition test:** Cover slide 1 and read slides 2–7. The argument should still hold. If it doesn't, the narrative is broken.

---

## 11. COVER SLIDE RULES — the most important slide

The cover must do 3 things in under 1.5 seconds:
1. State the TENSION (not the topic)
2. Promise a PAYOFF (what will they learn?)
3. Be visually DISTINCT (would stop mid-scroll)

**Cover checklist:**
- [ ] Headline states a tension, not a description ("Throughput > Prompts" not "AI Video Tools")
- [ ] Subtitle promises specific value ("here's the math + the fix")
- [ ] At least one element would work as a standalone Tweet/screenshot
- [ ] Badge row shows credibility signals (numbers, categories)
- [ ] Nothing below the fold (no content cut off at the bottom)

---

## 12. CTA SLIDE RULES — the most skipped slide

Most AI-generated CTA slides are lazy. Yours should feel earned.

**Structure:**
```
[kicker: "THE TAKEAWAY"]
[headline: "You don't have a model problem."]
[1-line support: "You have a throughput problem."]
[ordered list: 3-4 specific, actionable things they learned]
[closing line: "Comment KEYWORD ↓"]
```

**Rules:**
- The keyword must be 1–2 words, all caps, typed in accent color
- "Comment X" is more effective than "DM me" for LinkedIn algorithm
- The ordered list is a SUMMARY, not new information
- Closing line is always `mt-auto` — pinned to the bottom
