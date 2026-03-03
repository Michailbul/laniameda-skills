# Spacing, Layout & Dimensions

4px base unit. Editorial aesthetic demands generous whitespace — never cram.

---

## Spacing Scale

| Token | Pixels | Common Use |
|-------|--------|-----------|
| `0.5` | 2px | Micro gaps, indicator offsets |
| `1` | 4px | Tightest content gaps |
| `1.5` | 6px | Badge padding, tag inner gaps |
| `2` | 8px | Button padding, card inner |
| `2.5` | 10px | Button horizontal padding |
| `3` | 12px | Card padding, masonry gutter |
| `4` | 16px | Standard section padding |
| `5` | 20px | Button horizontal (lg) |
| `6` | 24px | Section vertical spacing |
| `8` | 32px | Major section gaps |
| `10` | 40px | Large vertical spacing |
| `12` | 48px | Page-level rhythm |
| `16` | 64px | Major layout gaps |
| `20` | 80px | Hero section padding |
| `24` | 96px | Maximum spacing |

---

## Border Radius Scale

Base radius: `1.25rem` (20px). Generous rounding is signature.

| Token | Value | Pixels | Use |
|-------|-------|--------|-----|
| `--radius-sm` | `calc(var(--radius) - 4px)` | ~16px | Input fields, small cards |
| `--radius-md` | `calc(var(--radius) - 2px)` | ~18px | Standard buttons, badges |
| `--radius-lg` | `var(--radius)` | 20px | Cards, containers |
| `--radius-xl` | `calc(var(--radius) + 4px)` | 24px | Modals, large panels |
| `full` | `9999px` | Pill | Buttons, badges, avatars |

### Component Radii

| Component | Radius |
|-----------|--------|
| Buttons (all) | `rounded-full` (pill) — non-negotiable |
| Badges | `rounded-full` (pill) |
| Soft cards | 20px |
| Brutalist cards | 0px (zero) |
| Image cards | 24px |
| macOS window | 12px top corners |
| Nav items | 6px |
| Checkboxes | 2px |
| Scrollbar thumb | 4px |

---

## Layout Dimensions

| Token | Value | Use |
|-------|-------|-----|
| `--sidebar-width` | 240px | Desktop sidebar expanded |
| `--sidebar-collapsed-width` | 64px | Sidebar collapsed |
| `--mobile-bottom-nav-height` | 56px | Mobile bottom nav |
| Detail panel width | 380px | Side panel on desktop |

---

## Grid & Layout Patterns

### Masonry Grid

| Breakpoint | Columns | Gutter |
|------------|---------|--------|
| < 640px | 2 | 12px |
| 640-1024px | 3 | 12px |
| 1024-1280px | 4 | 12px |
| > 1280px | 5 | 12px |

No CSS transforms on masonry items — they break multi-column.

### Sidebar + Content
```
┌──────────┬───────────────────────────────┐
│ Sidebar  │         Main Content          │
│  240px   │    (margin-left: sidebar)     │
└──────────┴───────────────────────────────┘
```

### Responsive Breakpoints

| Breakpoint | Width | Changes |
|------------|-------|---------|
| Mobile | < 640px | 2-col masonry, bottom nav, no sidebar |
| Tablet | 640-767px | 3-col masonry, bottom nav |
| Desktop | 768px+ | Sidebar visible, top filter bar |
| Wide | 1024px+ | 4-col masonry |
| Ultra-wide | 1280px+ | 5-col masonry |

### Content Padding

| Context | Padding |
|---------|---------|
| Desktop main | `px-4` to `px-6` |
| Mobile main | `px-3` |
| Sidebar sections | `px-2` to `px-3` |
| Card internal | `p-3` |

---

## Rules

- No spacing outside the scale
- No CSS transforms on masonry items
- Always generous whitespace — editorial layouts breathe
- Mobile: always account for `safe-area-inset-bottom`
- Sidebar transitions: `--duration-normal` with `--ease-out`
