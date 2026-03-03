# Typography System

Typography follows an **editorial print** hierarchy: humanist serif for display, clean geometric sans for body, technical monospace for labels and data.

---

## Font Families

### 1. Instrument Serif — Display & Hero

- **Source**: Google Fonts (`Instrument_Serif`, weight 400)
- **Fallback**: `Georgia, "Times New Roman", serif`
- **CSS var**: `--font-display`
- **Character**: Warm, editorial, slightly calligraphic
- **Use**: Hero headlines, empty states, sheet headers, brand wordmark
- **Rule**: ALWAYS italic for display moments
- **Loading**: `display: swap`, Latin subset only

### 2. Geist Sans — Body & UI

- **Source**: Vercel Geist (`next/font/google` → Inter as fallback)
- **Fallback**: `system-ui, -apple-system, sans-serif`
- **CSS var**: `--font-sans`
- **Character**: Clean, geometric, highly legible at small sizes
- **Use**: All body text, nav, forms, descriptions, metadata
- **Note**: In Pencil designs, map to `Inter`

### 3. Geist Mono — Labels & Data

- **Source**: Vercel Geist Mono (`next/font/google` → JetBrains Mono as fallback)
- **Fallback**: `ui-monospace, monospace`
- **CSS var**: `--font-mono`
- **Character**: Technical, precise, industrial
- **Use**: Section labels (uppercase), badges, code blocks, terminal text, button labels (brutalist), nav items, timestamps
- **Note**: In Pencil designs, map to `JetBrains Mono`

---

## Type Scale (7 tiers — no exceptions)

| Tier | Token | Size | Line Height | Use |
|------|-------|------|-------------|-----|
| micro | `--text-micro` | 10px | 1.4 | Section labels (uppercase mono, tracking 0.4em) |
| xs | `--text-size-xs` | 11px | ~1.4 | Badges, timestamps, sidebar labels, nav items |
| sm | `--text-size-sm` | 13px | ~1.5 | Body text, button labels, tag pills |
| base | `--text-size-base` | 15px | ~1.6 | Primary content, descriptions, panel body |
| lg | `--text-size-lg` | 18px | ~1.5 | Section headings, panel headers |
| xl | `--text-size-xl` | 24px | ~1.3 | Page headings, major titles |
| display | `--text-size-2xl` / `3xl` | 32-48px | ~1.2 | Hero text (Instrument Serif italic) |

**No font sizes outside this scale.**

---

## Weight System

| Weight | Value | Use |
|--------|-------|-----|
| Regular | 400 | Body text, descriptions |
| Medium | 500 | Nav labels, mono labels, interactive text |
| Semibold | 600 | Active nav, selected tags, stat values |
| Bold | 700 | Sparingly — max emphasis headings |
| Extra Bold | 800-900 | Hero headlines (Inter/Geist Sans only) |

---

## Letter Spacing

| Context | Tracking |
|---------|----------|
| Micro labels (10px mono) | `0.4em` |
| Uppercase mono labels | `0.12-0.22em` |
| Active nav items | `0.1em` (wider than inactive 0.08em) |
| Hero headlines (Inter 800) | `-0.04em` (tightened) |
| Brand wordmark | `-0.01em` |
| Standard body text | Normal (default) |

---

## Text Transform Patterns

| Pattern | Where |
|---------|-------|
| `uppercase` | All mono labels, section headers, button text, nav items, badge text |
| `italic` | Display/hero text (Instrument Serif), brand suffix, sheet headers |
| Normal case | Body text, descriptions, user content |

---

## Common Combinations

### Hero Headline
```css
font-family: var(--font-sans);  /* Inter/Geist Sans */
font-size: 48-56px;
font-weight: 800;
letter-spacing: -0.04em;
line-height: 1.1;
color: var(--ink);
```

### Display Serif Moment
```css
font-family: var(--font-display);  /* Instrument Serif */
font-style: italic;
font-size: 32-88px;
font-weight: 400;
line-height: 1.0-1.1;
color: var(--ink);
```

### Section Label (Eyebrow)
```css
font-family: var(--font-mono);  /* Geist Mono */
font-size: var(--text-size-xs);  /* 11px */
font-weight: 500;
text-transform: uppercase;
letter-spacing: 0.12em;
color: var(--coral);  /* or --text-tertiary */
```

### Body Text
```css
font-family: var(--font-sans);
font-size: var(--text-size-base);  /* 15px */
font-weight: 400;
line-height: 1.6;
color: var(--text-secondary);
```

### Badge / Tag
```css
font-family: var(--font-mono);
font-size: 10-11px;
font-weight: 500;
text-transform: uppercase;
letter-spacing: 0.12em;
```

### Terminal / Code
```css
font-family: var(--font-mono);
font-size: 13px;
font-weight: 400;
line-height: 1.5;
color: #e0e0e0;  /* on dark bg */
```

---

## Rules

- No font sizes outside the 7-tier scale
- No sans-serif for display/hero text — always serif (Instrument Serif)
- No serif for UI labels — always mono or sans
- Mono labels are ALWAYS uppercase with intentional tracking
- Display text is ALWAYS italic Instrument Serif
- Body text uses Geist Sans at 400 or 500
- Type scale is FIXED — does not change at breakpoints
