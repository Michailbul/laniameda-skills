# Shadows & Elevation

Depth is communicated through a **dual shadow system**: soft diffused shadows for editorial warmth, and sharp offset shadows for brutalist emphasis. The two coexist — like a printed catalogue displayed on a concrete gallery wall.

All shadows use ink color `rgba(32, 23, 16, ...)` — warm-toned, never neutral gray.

---

## Soft / Editorial Shadows

Standard UI depth for cards, dropdowns, modals.

| Token | Value | Use |
|-------|-------|-----|
| `--shadow-sm` | `0 1px 3px rgba(32,23,16,0.06), 0 1px 2px rgba(32,23,16,0.04)` | Cards at rest, badges |
| `--shadow-md` | `0 4px 12px rgba(32,23,16,0.08), 0 2px 4px rgba(32,23,16,0.04)` | Hover states, dropdowns |
| `--shadow-lg` | `0 12px 40px rgba(32,23,16,0.12), 0 4px 8px rgba(32,23,16,0.06)` | Modals, floating panels |
| `--shadow-sharp` | `0 4px 12px rgba(0,0,0,0.08)` | Image cards at rest |
| `--shadow-elevated` | `0 20px 40px -10px rgba(0,0,0,0.12)` | Card hover, floating elements |

### Depth Hierarchy

```
Level 0: Page surface (--surface-0, no shadow)
Level 1: Cards at rest (--shadow-sm or --shadow-sharp)
Level 2: Hovered cards (--shadow-elevated + pillar glow ring)
Level 3: Floating panels, detail sidebar (--shadow-lg)
Level 4: Modals, overlay dialogs (--shadow-lg + backdrop blur)
```

---

## Brutalist / Industrial Shadows

Sharp, unblurred offset shadows — letterpress printing feel. No blur ever.

| Token | Value | Use |
|-------|-------|-----|
| `--shadow-brutal` | `4px 4px 0 0 var(--ink)` | Primary brutalist elements |
| `--shadow-brutal-sm` | `2px 2px 0 0 var(--ink)` | Smaller interactive elements |
| `--shadow-brutal-accent` | `4px 4px 0 0 rgba(255,122,100,0.5)` | Pillar-tinted CTA hover |

### Brutalist Interaction Pattern

```css
/* Rest */
transform: translate(0, 0);
box-shadow: 4px 4px 0 0 #201710;

/* Hover — lift up, shadow grows */
transform: translate(-2px, -2px);
box-shadow: 6px 6px 0 0 #201710;

/* Active — press down, shadow disappears */
transform: translate(0, 0);
box-shadow: none;
```

The illusion: a physical button lifted on hover, pressed on click.

---

## Glass Surface

Frosted volcanic glass — warm-toned, not cold blue/gray.

```css
.glass-surface {
  background: rgba(255, 250, 245, 0.82);
  backdrop-filter: blur(20px) saturate(120%);
  -webkit-backdrop-filter: blur(20px) saturate(120%);
  border: 1px solid rgba(32, 23, 16, 0.09);
}
```

---

## Pillar Glow Shadow

Colored glow ring that responds to the active accent:

```css
--shadow-pillar-glow:
  0 0 0 1.5px rgba(var(--pillar-r), var(--pillar-g), var(--pillar-b), 0.3),
  0 0 20px rgba(var(--pillar-r), var(--pillar-g), var(--pillar-b), 0.1);
```

### Card Hover (composite)
```css
box-shadow:
  var(--shadow-elevated),
  0 0 0 1px rgba(var(--pillar-r), var(--pillar-g), var(--pillar-b), 0.18);
```

### Card Selected (composite)
```css
box-shadow:
  var(--shadow-pillar-glow),
  0 0 24px rgba(var(--pillar-r), var(--pillar-g), var(--pillar-b), 0.18);
```

---

## Grain Texture

Barely perceptible noise overlay — felt more than seen (`opacity: 0.018`).

```css
.grain-overlay::after {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  opacity: 0.018;
  mix-blend-mode: multiply;
  /* fractalNoise SVG background */
}
```

---

## Body Background (Pillar-Aware)

```css
body {
  background:
    radial-gradient(ellipse 65% 50% at 8% 0%,
      rgba(var(--pillar-r), var(--pillar-g), var(--pillar-b), 0.11) 0%, transparent 65%),
    radial-gradient(ellipse 75% 55% at 92% 100%,
      rgba(var(--pillar-warm-r), var(--pillar-warm-g), var(--pillar-warm-b), 0.12) 0%, transparent 65%),
    linear-gradient(180deg, #fffdf9 0%, var(--surface-0) 45%, #fff6ed 100%);
}
```

---

## Rules

- No inline `style={{ boxShadow }}` — use tokens
- No cold/gray shadows — warm ink base always
- Brutalist shadows ALWAYS pair with translate offset
- Glass surfaces ALWAYS include both webkit and standard backdrop-filter
- Grain overlay is extremely subtle (0.018) — never visible at a glance
