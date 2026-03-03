# Laniameda Design Tokens — Complete Reference

## CSS Custom Properties

Drop these into any project's `:root` for the full laniameda palette.

```css
:root {
  /* SURFACES (Paper Stack) */
  --paper: #fffaf5;
  --paper-muted: #f5eee7;
  --surface-0: #fffaf5;
  --surface-1: #fff4ea;
  --surface-2: #f7ede2;
  --surface-3: #efe2d4;
  --surface-4: #e4d4c4;

  /* TEXT HIERARCHY (Ink Scale) */
  --ink: #201710;
  --text-primary: #201710;
  --text-secondary: #4c3a2d;
  --text-tertiary: #7d6755;
  --text-ghost: #ab9381;

  /* BORDERS */
  --border-subtle: rgba(32, 23, 16, 0.08);
  --border-default: rgba(32, 23, 16, 0.16);
  --border-strong: rgba(32, 23, 16, 0.24);
  --border-accent: rgba(255, 122, 100, 0.35);

  /* AMBER/CORAL ACCENT RAMP (12 steps) */
  --amber-1: #fff7f3;
  --amber-2: #ffece4;
  --amber-3: #ffe2d8;
  --amber-4: #ffd6ca;
  --amber-5: #ffc9ba;
  --amber-6: #ffbaa9;
  --amber-7: #ffa791;
  --amber-8: #f2977b;
  --amber-9: #ff7a64;    /* Primary accent — Ember Coral */
  --amber-10: #ff917d;   /* Hover variant */
  --amber-11: #ffb7a8;
  --amber-12: #ffe0d6;

  /* Accent aliases */
  --coral: #ff7a64;
  --coral-hover: #ff917d;
  --warm-accent: #e8614f;
  --accent-subtle: rgba(255, 122, 100, 0.10);
  --accent-glow: rgba(255, 122, 100, 0.18);

  /* SEMANTIC MAPPINGS (shadcn-compatible) */
  --background: var(--surface-0);
  --foreground: var(--text-primary);
  --card: var(--paper);
  --card-foreground: var(--text-primary);
  --primary: var(--coral);
  --primary-foreground: #ffffff;
  --secondary: var(--surface-2);
  --secondary-foreground: var(--text-secondary);
  --muted: var(--surface-2);
  --muted-foreground: var(--text-secondary);
  --destructive: oklch(0.62 0.2 27);
  --border: var(--border-default);
  --ring: var(--coral);

  /* INVERSE (Dark panels) */
  --bg-inverse: #18181b;
  --text-inverse: #fafafa;

  /* STATUS */
  --status-running: var(--coral);
  --status-success: #16a34a;
  --status-error: #dc2626;
  --status-queued: var(--text-tertiary);

  /* TYPOGRAPHY SCALE */
  --text-micro: 10px;
  --text-size-xs: 11px;
  --text-size-sm: 13px;
  --text-size-base: 15px;
  --text-size-lg: 18px;
  --text-size-xl: 24px;
  --text-size-2xl: 32px;
  --text-size-3xl: 48px;

  /* FONT STACKS */
  --font-sans: system-ui, -apple-system, sans-serif;
  --font-mono: ui-monospace, monospace;
  --font-display: Georgia, "Times New Roman", serif;

  /* LAYOUT */
  --radius: 1.25rem;  /* 20px base */
  --sidebar-width: 240px;
  --sidebar-collapsed-width: 64px;

  /* TIMING */
  --duration-instant: 80ms;
  --duration-fast: 150ms;
  --duration-normal: 250ms;
  --duration-slow: 400ms;
  --duration-glacial: 600ms;

  /* EASING */
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-in: cubic-bezier(0.55, 0, 1, 0.45);
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);

  /* SHADOWS (Soft / Editorial) */
  --shadow-sm: 0 1px 3px rgba(32,23,16,0.06), 0 1px 2px rgba(32,23,16,0.04);
  --shadow-md: 0 4px 12px rgba(32,23,16,0.08), 0 2px 4px rgba(32,23,16,0.04);
  --shadow-lg: 0 12px 40px rgba(32,23,16,0.12), 0 4px 8px rgba(32,23,16,0.06);
  --shadow-sharp: 0 4px 12px rgba(0,0,0,0.08);
  --shadow-elevated: 0 20px 40px -10px rgba(0,0,0,0.12);

  /* SHADOWS (Brutalist / Industrial) */
  --shadow-brutal: 4px 4px 0 0 var(--ink);
  --shadow-brutal-sm: 2px 2px 0 0 var(--ink);
}
```

---

## Color Palette Deep Dive

### Surfaces (Paper Stack)

A 5-tier depth system from lightest background to deepest interactive fill. All surfaces have warmth baked in — never cold white.

| Token | Hex | Name | Use |
|-------|-----|------|-----|
| `--paper` | `#fffaf5` | Warm Parchment | Page background, lightest canvas |
| `--paper-muted` | `#f5eee7` | Aged Linen | Subtle background variation |
| `--surface-1` | `#fff4ea` | Sunlit Cream | Sidebar fills, stat panels, secondary areas |
| `--surface-2` | `#f7ede2` | Warm Sand | Card backgrounds, hover fills, muted zones |
| `--surface-3` | `#efe2d4` | Desert Clay | Deeper fills, selected states |
| `--surface-4` | `#e4d4c4` | Weathered Stone | Deepest non-accent surface, heavy emphasis |

### Text Hierarchy (Ink Scale)

| Token | Hex | Name | Use |
|-------|-----|------|-----|
| `--ink` | `#201710` | Deep Volcanic Ink | Brand mark, absolute darkest |
| `--text-primary` | `#201710` | = ink | Headlines, body text, primary labels |
| `--text-secondary` | `#4c3a2d` | Aged Walnut | Metadata, secondary labels, descriptions |
| `--text-tertiary` | `#7d6755` | Warm Driftwood | Section labels, tertiary info |
| `--text-ghost` | `#ab9381` | Faded Sandstone | Placeholders, disabled states, hints |

### Accent Usage Rules

- **Coral (`#ff7a64`)** is the primary action color — use sparingly for CTAs, active indicators
- Never use coral for large background areas
- On dark panels, coral text renders well for syntax highlighting
- Hover: `#ff917d`, Deeper emphasis: `#e8614f`
- Subtle bg tint: `rgba(255, 122, 100, 0.10)`
- Glow effect: `rgba(255, 122, 100, 0.18)`

### Terminal / Code Colors

For dark terminal/code blocks within light pages:

| Element | Color |
|---------|-------|
| Terminal BG | `#0f0f0f` or `#1a1a1a` |
| Terminal text (default) | `#e0e0e0` or `#ffffff` |
| Comments | `#27c93f` (green) |
| Strings/values | `#ff7a64` (coral) |
| Prompts | `#ab9381` (ghost) |
| Success indicators | `#27c93f` |
| Traffic light red | `#ff5f56` |
| Traffic light yellow | `#ffbd2e` |
| Traffic light green | `#27c93f` |

---

## Typography Deep Dive

### Font Family Mapping

| Design System Font | Web Implementation | Pencil Implementation |
|-------------------|-------------------|----------------------|
| Instrument Serif (italic) | Google Fonts, `display: swap` | Playfair Display (italic) |
| Geist Sans | Vercel font package | Inter |
| Geist Mono | Vercel font package | JetBrains Mono |

### Type Scale (7 tiers — no exceptions)

| Tier | Size | Line Height | Use |
|------|------|-------------|-----|
| micro | 10px | 1.4 | Section labels (uppercase mono, 0.4em tracking) |
| xs | 11px | ~1.4 | Badges, timestamps, sidebar labels, nav items |
| sm | 13px | ~1.5 | Body text, button labels, tag pills |
| base | 15px | ~1.6 | Primary content text, descriptions |
| lg | 18px | ~1.5 | Section headings, panel headers |
| xl | 24px | ~1.3 | Page headings, major titles |
| display | 32-48px | ~1.2 | Hero text (Instrument Serif italic) |

### Weight System

| Weight | Value | Use |
|--------|-------|-----|
| Regular | 400 | Body text, descriptions |
| Medium | 500 | Nav labels, mono labels, interactive text |
| Semibold | 600 | Active nav, selected tags, stat values |
| Bold | 700 | Sparingly — max emphasis headings only |
| Extra Bold | 800-900 | Hero headlines (Inter only) |

### Letter Spacing

| Context | Tracking |
|---------|----------|
| Micro labels | `0.4em` |
| Uppercase mono labels | `0.12-0.22em` |
| Active nav items | `0.1em` |
| Standard text | Normal |
| Brand wordmark | `-0.01em` |
| Headlines (Inter 800) | `-0.04em` |

---

## Shadow System Deep Dive

### Soft / Editorial Shadows

All use warm ink base `rgba(32, 23, 16, ...)` — never neutral gray.

```
Level 0: Page surface (no shadow)
Level 1: Cards at rest (--shadow-sm or --shadow-sharp)
Level 2: Hovered cards (--shadow-elevated + pillar glow ring)
Level 3: Floating panels (--shadow-lg)
Level 4: Modals (--shadow-lg + backdrop blur)
```

### Brutalist Shadows

Sharp, unblurred offset shadows — letterpress printing feel.

```
Rest:    transform: translate(0, 0);    box-shadow: none or 4px 4px 0 #201710;
Hover:   transform: translate(-2px, -2px); box-shadow: 6px 6px 0 #201710;
Active:  transform: translate(0, 0);    box-shadow: none;
```

### Glass Surface

```css
background: rgba(255, 250, 245, 0.82);
backdrop-filter: blur(20px) saturate(120%);
border: 1px solid rgba(32, 23, 16, 0.09);
```

---

## Spacing Scale

4px base unit. Editorial layouts demand generous whitespace.

| Token | Pixels | Common Use |
|-------|--------|-----------|
| 1 | 4px | Tightest content gaps |
| 2 | 8px | Button padding, card inner padding |
| 3 | 12px | Card padding, section gaps |
| 4 | 16px | Standard section padding |
| 6 | 24px | Section vertical spacing |
| 8 | 32px | Major section gaps |
| 12 | 48px | Page-level vertical rhythm |
| 16 | 64px | Major layout gaps |
| 20 | 80px | Hero section padding |

## Border Radius Scale

Base radius: 20px (`1.25rem`).

| Component | Radius |
|-----------|--------|
| Buttons | `rounded-full` (pill) — non-negotiable |
| Badges | `rounded-full` (pill) |
| Soft cards | 20px (`rounded-xl`) |
| Brutalist cards | 0px (zero radius) |
| Image cards | 24px (`rounded-xl`) |
| Nav items | 6px |
| macOS window chrome | 12px top corners |

---

## Pillar Theming

The design system supports 4 accent color pillars via `data-pillar` attribute:

| Pillar | Accent | Hex |
|--------|--------|-----|
| creators (default) | Ember Coral | `#ff7a64` |
| cars | Crimson Heat | `#e5534b` |
| designs | Electric Indigo | `#5d6bfa` |
| dump | Teal Catch-all | `#2eb8b4` |

Pillar colors override `--amber-*`, `--coral`, and related tokens dynamically.
