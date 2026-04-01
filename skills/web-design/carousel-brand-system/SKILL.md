---
name: carousel-brand-system
description: >
  Build a complete brand design system tuned for social media carousel production.
  Interactive workflow: propose color palettes with reasoning, explore font pairings,
  generate an HTML picker for the user to click what resonates, analyze picks,
  lock the system in Figma, and produce carousel-format combo cards.

  Triggers: "build a carousel design system", "create brand colors for carousels",
  "design system for social media", "carousel brand system", "explore colors for our brand",
  "pick fonts for carousels", "lock our design system", "brand system for content production",
  "social media design system", or any request to build a visual identity system
  specifically for carousel / social media content production.

  Does NOT trigger for: building individual carousels (use carousel-designer),
  general brand guidelines docs (use brand-guidelines-builder), or website design
  systems (use laniameda-brand-design).
version: 0.1.0
---

# Carousel Brand System

Build a locked, production-ready brand design system for social media carousels. The output is a color + typography + gradient + combo system that feeds directly into carousel production (Canva, Figma, or HTML).

This skill runs as an interactive conversation, not a one-shot generation. The user explores, picks, and you lock.

---

## When to use this vs. other skills

| Skill | Use when |
|-------|----------|
| **carousel-brand-system** (this) | Building the visual system that powers all carousels |
| **carousel-designer** | Producing an individual carousel using an existing system |
| **brand-guidelines-builder** | Creating a general brand identity doc from scratch |
| **laniameda-brand-design** | Building website/landing page designs in Pencil |
| **typography-master** | Deep-diving into font exploration independently |

---

## Workflow — 6 phases, always in order

### Phase 1: Audit

Before proposing anything, understand what exists.

**Read first:**
- Any existing brand guidelines (e.g. `studio/brand-guidelines.md`)
- Any Figma design system pages (use `use_figma` to inspect)
- Any color/font exploration files in `brand/`
- The user's CLAUDE.md for brand identity context

**Extract:**
- Locked colors (base palette)
- Locked fonts
- Brand DNA keywords (mood, feeling, audience)
- What's working vs. what needs to change
- Carousel format requirements (platform, dimensions)

**Output:** Brief internal summary. Don't dump this on the user — just confirm: "I see your base palette is X, fonts are Y, and the mood is Z. Ready to explore accent directions?"

---

### Phase 2: Propose Color Directions

Generate 3-4 distinct accent palette directions. Each direction should:

1. **Have a name and vibe** — a 2-3 word mood descriptor
2. **Include 4-6 accent colors** — with hex, name, and specific role
3. **Explain the reasoning** — why this works with the base palette and brand DNA
4. **Identify the risk** — what could go wrong or feel off

**Format as an HTML page** (not just text). The page should:
- Show the locked base palette for reference
- Show each direction with color swatches
- Include 2-3 combo cards per direction showing color + sample text together
- Include gradient strips showing how colors flow together
- Have a comparison table at the bottom

**Key principles for color proposals:**
- Always keep the base palette untouched
- Propose in tiers: Primary Accents (high-frequency) → Supporting (contextual) → Situational (sparingly)
- Warm brands need cool counterpoints. Cool brands need warm signals.
- Fewer high-impact colors > many diluted ones
- Every accent needs a clear job description — no overlapping roles

**Write the HTML to `brand/color-exploration.html`** and open it in the browser.

Wait for user reaction before proceeding.

---

### Phase 3: Propose Font Pairings

If fonts aren't already locked, explore pairings. Two approaches:

**A) Figma specimens** — Create font pairing cards in Figma showing headline + body samples at carousel scale (1080x1350). Each card uses a different pairing with the same sample text.

**B) HTML specimens** — Generate an HTML page with all candidate pairings rendered at real sizes, using Google Fonts imports.

**Pairing rules:**
- Always pair a display/headline font with a body/reading font
- Contrast is key: serif + sans, heavy + light, expressive + neutral
- Test at carousel scale — if it doesn't read at phone size, it fails
- Include the font pairing name on each specimen card
- 5-8 pairings is the sweet spot for exploration

Wait for user feedback. Some pairings will get cut.

---

### Phase 4: Interactive Picker

Generate an HTML picker page that lets the user click to select what they like. This is the core of the workflow.

**The picker must include:**

1. **Accent Colors** — All proposed colors as clickable swatches
2. **Font Pairings** — All proposed pairings as clickable cards with live font rendering
3. **Combo Cards** — Carousel-format (1080:1350 aspect ratio) cards showing color + font together. Each card should vary:
   - Background color
   - Headline accent color
   - Font pairing
   - Copy (use real brand-relevant lines, not lorem ipsum)
4. **Gradients** — Clickable gradient strips
5. **Palette Directions** — Full direction cards if applicable

**Picker UX requirements:**
- Click to toggle selection (visual checkmark + border highlight)
- Live counter in a sticky bottom bar showing total picks
- "Export Picks" button that generates a copyable text summary
- "Clear all" button
- The export format must be structured and parseable:

```
=== BRAND PICKS ===

## Base (locked)
[list locked colors]

## Accent Colors I Like
- [Name] [Hex]

## Font Pairings I Like
- [Headline font] + [Body font]

## Combo Cards I Like
- [Description of combo]

## Gradients I Like
- [Color A] → [Color B]
```

**Write the picker to `brand/color-picker.html`** and open it.

Tell the user: "Click everything you like, hit Export Picks, paste the summary back to me."

---

### Phase 5: Analyze Picks & Propose Final System

When the user pastes their picks:

1. **Count frequency** — Which colors, fonts, and combos appeared most?
2. **Identify the palette** — Rank accents by usage into tiers:
   - **Primary Accents** (appeared in 3+ combos) — high-frequency use
   - **Supporting** (appeared in 1-2 combos) — contextual depth
   - **Situational** (appeared once) — sparingly
3. **Identify cuts** — Colors/fonts that were never picked get dropped
4. **Check for conflicts** — Colors that compete, insufficient contrast pairs, too many similar tones

**Present the analysis as a clear summary table:**
- Tier | Color | Hex | Appearances | Role
- Plus: which fonts stayed, which gradients, what got cut

**Ask two questions max** before locking:
- Any tiebreakers (e.g. "keep both Teals or replace?")
- "Ready to lock?"

---

### Phase 6: Lock in Figma

Build the design system page in Figma using `use_figma` MCP tool.

**Page structure (vertical auto-layout, no background fill):**

```
Header — Brand name + "Design System v[X].0"
01 COLOR SYSTEM
  Primary Palette — base color swatches (locked)
  Primary Accents — tier 1 accent swatches
  Supporting Accents — tier 2 swatches
  Situational Accents — tier 3 swatches
  Color Usage Rules — panel with pairing rules

02 TYPOGRAPHY
  Font Showcase — carousel-format cards (1080x1350) using locked pairings
    Layout: top group (label + accent bar + headline) → flex spacer → bottom group (body + meta)
    Each card: different color combo + font pairing
    Organized in rows of 3
  Type Scale — if needed

02B THEMES
  Dark/Light side-by-side preview cards

01B COLOR PAIRINGS
  Primary Reading Pairs
  Accent on Dark Surfaces
  Statement Backgrounds

03 GRADIENTS
  Rows of gradient strips with labels

04 USAGE GUIDELINES
  DO / DON'T columns
  Carousel Pairing Cheatsheet — specific recipes (bg + headline font + headline color + body font)

Footer
```

**Carousel combo card template (for Figma):**
```
Frame: 1080x1350, cornerRadius 16, vertical auto-layout
  paddingTop: 64, paddingBottom: 56, paddingLeft: 64, paddingRight: 64

  Top group (auto, vertical, gap 16):
    Label — 13px Inter Regular, uppercase, letter-spacing 10%, opacity 0.4
    Accent bar — 48x4, cornerRadius 2
    Headline — [headline font], [headline size], letterSpacing -2%

  Flex spacer — layoutSizingVertical: FILL

  Bottom group (auto, vertical, gap 16):
    Body text — [body font], 24px, lineHeight 38px, opacity 0.75
    Meta label — 11px Inter Regular, uppercase, letter-spacing 8%, opacity 0.25
```

**After building:** Take screenshots to verify. Fix any layout issues (collapsed auto-layout, wrong fills, missing text).

---

## Color Proposal Principles

### How to think about accent palettes

Start from the brand's emotional core, not from color theory abstractions.

**Temperature mapping:**
- Warm brands (Laniameda-like) → need 1-2 cool counterpoints for depth (Slate Blue, Muted Teal)
- Cool brands → need warm signals for humanity (Amber, Coral, Ochre)
- The tension between warm and cool is where interesting palettes live

**Tier architecture:**
- **Primary (2-3 colors):** These do 80% of the accent work. Must have distinct temperatures and roles.
- **Supporting (3-4 colors):** Background alternatives, gradient endpoints, subtle accents. Never used as headlines.
- **Situational (2-3 colors):** Statement moments only. If used on every slide, they lose power.

**Common accent roles:**
| Role | Example | Usage |
|------|---------|-------|
| Warm signal | Amber, Gold | Headlines on dark, highlight moments |
| Emotional dark | Plum, Deep Indigo | Background for moody slides |
| Cool ground | Slate Blue, Steel | Professional/editorial frames |
| Hot signal | Vermillion, Hot Pink | CTAs, stop-and-look moments |
| Neutral depth | Graphite, Charcoal | Layering, subtle backgrounds |
| Quiet organic | Muted Teal, Sage | Dividers, secondary accents |
| Glow text | Electric Cream, Warm White | Text on dark moody backgrounds |

### Naming colors

Always give colors evocative names, not technical descriptions:
- "Plum" not "Dark Purple"
- "Charcoal Violet" not "Dark Gray Purple"
- "Electric Cream" not "Light Yellow"

Names should feel like they belong in the brand's world.

---

## Font Pairing Principles

### What makes a good carousel font pairing

1. **Contrast** — headline and body should look obviously different (weight, style, family)
2. **Readability at phone scale** — body text must work at 24px on a 1080px canvas
3. **Personality match** — the headline font carries the brand voice, the body font stays neutral
4. **Monospace for meta** — use a mono font for labels, counters, attribution (JetBrains Mono, Space Mono)

### Proven pairing structures
- Serif headline + Sans body (editorial, premium)
- Heavy grotesque headline + Mono body (tech, brutalist)
- Display headline + Neutral body (expressive, varied)
- Mono headline + Mono body (developer, minimal)

---

## HTML Page Standards

All generated HTML pages should:
- Import fonts from Google Fonts
- Use dark backgrounds (`#0e0c0a` or similar)
- Use the brand's typography for headings and labels
- Be self-contained (no external CSS/JS files)
- Render well at 1400-1600px viewport width
- Use CSS Grid or Flexbox for layout
- Include hover states on interactive elements
- Use the brand's color palette for the page itself (eat your own cooking)

---

## Figma MCP Patterns

### Font loading
Always `await figma.loadFontAsync({ family, style })` before creating text nodes. Common gotchas:
- "Semi Bold" has a space (not "SemiBold") for Inter
- "Extra Bold" has a space for Syne
- Use `figma.setCurrentPageAsync(page)` not `figma.currentPage = page`

### Auto-layout
- Set `layoutSizingHorizontal = 'FILL'` AFTER `parent.appendChild(child)`
- Use `primaryAxisSizingMode = 'FIXED'` for cards with fixed height
- Use `layoutSizingVertical = 'FILL'` for flex spacers
- `counterAxisSizingMode` only accepts `'FIXED'` or `'AUTO'` (not `'FILL'`)

### Gradients
```js
fills = [{
  type: 'GRADIENT_LINEAR',
  gradientTransform: [[1, 0, 0], [0, 1, 0]], // left to right
  // or [[0, 1, 0], [-1, 0, 1]] for top to bottom
  gradientStops: [
    { position: 0, color: { r, g, b, a: 1 } },
    { position: 1, color: { r, g, b, a: 1 } }
  ]
}]
```

### Colors
Figma uses 0-1 range, not 0-255. Convert: `r/255, g/255, b/255`.

---

## Deliverables Checklist

At the end of this workflow, the user should have:

- [ ] `brand/color-exploration.html` — Color direction proposals
- [ ] `brand/color-picker.html` — Interactive picker with all options
- [ ] Figma Design System page — Locked, organized, production-ready
- [ ] Carousel combo cards in Figma — Showing every font pairing + color combo
- [ ] Color rules and pairing guides — In Figma and/or markdown
- [ ] Carousel cheatsheet — Specific bg + font + color recipes for common slide types
- [ ] Updated `brand-guidelines.md` or `CLAUDE.md` — Reflecting the locked system

---

## Example Session Flow

```
User: "Let's build a design system for our social media carousels"

→ Phase 1: Read existing brand docs, Figma, CLAUDE.md
→ "I see your base is Coral + Carbon + Teal + Linen with 7 font pairings.
   The screaming accents feel off-brand. Ready to explore new directions?"

User: "Yes, let's explore"

→ Phase 2: Generate color-exploration.html with 3-4 directions
→ Open in browser
→ "What direction pulls you?"

User: "I like B and C"

→ Phase 3: Generate more B+C hybrids with font pairings in combo cards
→ "Want to try the picker?"

User: "Yes"

→ Phase 4: Generate color-picker.html
→ "Click everything you like, export, paste back"

User: [pastes picks]

→ Phase 5: Analyze picks, identify tiers, propose final system
→ "Here's what emerged. Ready to lock?"

User: "Lock it"

→ Phase 6: Build in Figma, verify with screenshots
→ "Done. Design System v2.0 is locked."
```
