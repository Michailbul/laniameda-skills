# Laniameda Design System

Portable design system for the laniameda brand. Drop into any project to maintain consistent visual identity.

**Style**: Warm editorial + brutalist hybrid
**Audience**: Technical / developer-focused
**Mode**: Light only (dark elements are accent moments)

---

## Quick Start

### 1. Import tokens
```css
@import "./design-system/tokens.css";
```

### 2. Load fonts
```html
<!-- Google Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@1&display=swap" rel="stylesheet">

<!-- Or with Next.js -->
import { Geist, Geist_Mono } from "next/font/google";
import { Instrument_Serif } from "next/font/google";
```

### 3. Apply base styles
```css
body {
  background: var(--paper);
  color: var(--text-primary);
  font-family: var(--font-sans);
  -webkit-font-smoothing: antialiased;
}
```

---

## Files

| File | Purpose |
|------|---------|
| `tokens.css` | All CSS custom properties — drop-in ready |
| `brand.md` | Voice, tone, audience, design principles |
| `colors.md` | Complete palette, accent rules, terminal colors |
| `typography.md` | Font families, scale, weights, spacing |
| `shadows-elevation.md` | Dual shadow system, glass, grain |
| `spacing-layout.md` | Spacing scale, radius, grid, breakpoints |
| `components.md` | All component patterns and specs |
| `motion.md` | Animation tokens, easing, transition patterns |

---

## Core Identity at a Glance

| Element | Value |
|---------|-------|
| Page background | `#fffaf5` (warm parchment) |
| Primary text | `#201710` (volcanic ink) |
| Accent | `#ff7a64` (ember coral) |
| Display font | Instrument Serif italic |
| Body font | Geist Sans (Inter fallback) |
| Label font | Geist Mono (JetBrains Mono fallback) |
| Base radius | 20px |
| Button shape | Pill (always) |
| Brutalist shadow | `4px 4px 0 #201710` (no blur) |
| Editorial shadow | Warm ink-based diffused |
| Hover timing | 80ms |
| Enter easing | `cubic-bezier(0.16, 1, 0.3, 1)` |

---

## Never Do

- Use pure white (`#ffffff`) backgrounds
- Use pure black (`#000000`) text
- Use cold/gray shadows
- Use bouncy animations
- Use neon or cold accent colors
- Use more than 2-3 coral elements per viewport
- Break the 7-tier type scale
- Use sans-serif for hero/display text
- Add blur to brutalist shadows
