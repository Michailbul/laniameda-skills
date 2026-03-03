# Color System

Colors are drawn from **natural warm materials** — sun-bleached paper, aged ink, terracotta, volcanic ember. Pure white and pure black are never used.

---

## Core Palette

### Surfaces (Paper Stack)

Five-tier depth system. All surfaces have warmth baked in.

| Token | Hex | Name | Use |
|-------|-----|------|-----|
| `--paper` | `#fffaf5` | Warm Parchment | Page background, lightest canvas |
| `--paper-muted` | `#f5eee7` | Aged Linen | Subtle background variation |
| `--surface-1` | `#fff4ea` | Sunlit Cream | Sidebars, secondary areas, stat panels |
| `--surface-2` | `#f7ede2` | Warm Sand | Card backgrounds, hover fills, muted zones |
| `--surface-3` | `#efe2d4` | Desert Clay | Deeper fills, selected states |
| `--surface-4` | `#e4d4c4` | Weathered Stone | Heaviest non-accent surface |

### Text (Ink Scale)

| Token | Hex | Name | Use |
|-------|-----|------|-----|
| `--ink` | `#201710` | Deep Volcanic Ink | Brand mark, absolute darkest |
| `--text-primary` | `#201710` | = ink | Headlines, body, primary labels |
| `--text-secondary` | `#4c3a2d` | Aged Walnut | Metadata, descriptions |
| `--text-tertiary` | `#7d6755` | Warm Driftwood | Section labels, tertiary info |
| `--text-ghost` | `#ab9381` | Faded Sandstone | Placeholders, disabled states |

### Borders

| Token | Value | Use |
|-------|-------|-----|
| `--border-subtle` | `rgba(32, 23, 16, 0.08)` | Dividers, section separators |
| `--border-default` | `rgba(32, 23, 16, 0.16)` | Card outlines, inputs |
| `--border-strong` | `rgba(32, 23, 16, 0.24)` | Hover borders, active outlines |
| `--border-accent` | `rgba(255, 122, 100, 0.35)` | Active tags, coral highlights |

---

## Accent (Amber-Coral Ramp)

Primary accent = warm coral evoking volcanic embers. Full 12-step ramp.

| Step | Hex | Description |
|------|-----|-------------|
| 1 | `#fff7f3` | Barely-there blush |
| 2 | `#ffece4` | Lightest accent bg |
| 3 | `#ffe2d8` | Soft accent wash |
| 4 | `#ffd6ca` | Light accent fill |
| 5 | `#ffc9ba` | Medium-light |
| 6 | `#ffbaa9` | Approaching mid |
| 7 | `#ffa791` | Warm mid-tone |
| 8 | `#f2977b` | Rich warm |
| **9** | **`#ff7a64`** | **Ember Coral — Primary accent** |
| 10 | `#ff917d` | Hover variant |
| 11 | `#ffb7a8` | Light text-on-dark |
| 12 | `#ffe0d6` | Lightest accent text |

### Accent Aliases

| Token | Value | Use |
|-------|-------|-----|
| `--coral` | `#ff7a64` | Primary CTAs, active indicators |
| `--coral-hover` | `#ff917d` | Hover state |
| `--warm-accent` | `#e8614f` | Deeper emphasis |
| `--accent-subtle` | `rgba(255,122,100,0.10)` | Active tag bg tint |
| `--accent-glow` | `rgba(255,122,100,0.18)` | Glow effects |

### Coral Usage Rules

- Use sparingly — CTAs, labels, accent moments only
- Never use for large background fills
- On dark panels: excellent for syntax highlighting
- Maximum 2-3 coral elements visible at once per viewport
- Pair with ink for maximum contrast

---

## Dark / Inverse

For terminal windows, code blocks, and occasional dark sections within the warm light canvas:

| Token | Hex | Use |
|-------|-----|-----|
| `--bg-inverse` | `#18181b` | Dark panel backgrounds |
| `--text-inverse` | `#fafafa` | Text on dark panels |
| Terminal bg | `#0f0f0f` | Terminal interior (darker) |
| Terminal surface | `#1a1a1a` | Terminal titlebar |
| Terminal border | `rgba(255,255,255,0.08)` | Subtle light border |

### Terminal / Code Syntax Colors

| Element | Color |
|---------|-------|
| Default text | `#e0e0e0` |
| Comments / success | `#27c93f` (green) |
| Strings / accents | `#ff7a64` (coral) |
| Prompts / muted | `#ab9381` (ghost) |
| Traffic light red | `#ff5f56` |
| Traffic light yellow | `#ffbd2e` |
| Traffic light green | `#27c93f` |

---

## Status Colors

| Token | Value | Use |
|-------|-------|-----|
| `--status-running` | `#ff7a64` | Active/in-progress |
| `--status-success` | `#16a34a` | Completion |
| `--status-error` | `#dc2626` | Error states |
| `--status-queued` | `#7d6755` | Pending |

---

## Rules

- Never use pure white (`#ffffff`) as a background — use `--paper` or `--surface-*`
- Never use pure black (`#000000`) for text — use `--ink` or `--text-*`
- Never hardcode hex values in components — use token references
- All shadows use warm ink base `rgba(32,23,16,...)` — never neutral gray
- Coral is the ONLY accent color — no blues, greens, or purples in the brand palette
