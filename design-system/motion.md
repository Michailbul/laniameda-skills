# Motion & Animation

**Restrained and purposeful.** Animations guide attention and confirm interactions — never entertain or distract. Like turning pages in a premium art book.

No bouncy, no playful. Every animation should feel like a Tesla or Apple interface — smooth, inevitable, barely noticed.

---

## Timing Tokens

| Token | Duration | Use |
|-------|----------|-----|
| `--duration-instant` | 80ms | Hover states — snappy, no perceived delay |
| `--duration-fast` | 150ms | Tab switches, dropdowns, tag animations |
| `--duration-normal` | 250ms | Panel open/close, card entrance, toasts |
| `--duration-slow` | 400ms | Success flash, staggered card entrance |
| `--duration-glacial` | 600ms | Dramatic reveals (rare) |

---

## Easing Curves

| Token | Value | Use |
|-------|-------|-----|
| `--ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` | Default ENTER — panels, cards, toasts |
| `--ease-in` | `cubic-bezier(0.55, 0, 1, 0.45)` | Default EXIT — close, dismiss |
| `--ease-spring` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | Tag enter ONLY (subtle overshoot) |

---

## Entrance Animations

| Class | Duration | Description |
|-------|----------|-------------|
| `.animate-fade-in` | 300ms | General fade-in |
| `.animate-fade-in-up` | 250ms | Fade + slide up 12px |
| `.animate-card-entrance` | 400ms | Masonry card (opacity + translateY + scale) |
| `.animate-panel-slide-in` | 250ms | Detail panel from right |
| `.animate-sheet-slide-up` | 250ms | Mobile bottom sheet from bottom |
| `.animate-modal-enter` | 250ms | Modal scale 0.96→1 |
| `.animate-dropdown-enter` | 150ms | Dropdown slides down 4px |
| `.animate-toast-enter` | 250ms | Toast slides up 16px |
| `.animate-tag-enter` | 120ms | Tag scale 0.8→1 (spring) |

## Exit Animations

| Class | Duration | Description |
|-------|----------|-------------|
| `.animate-fade-out` | 200ms | General fade-out |
| `.animate-panel-slide-out` | 200ms | Panel exits right |
| `.animate-sheet-slide-down` | 200ms | Sheet exits down |
| `.animate-toast-exit` | 200ms | Toast slides down + fades |
| `.animate-tag-exit` | 100ms | Tag scale 1→0.8 |

## Ambient / Decorative

| Class | Duration | Description |
|-------|----------|-------------|
| `.animate-glow-pulse` | 3s infinite | Pillar-tinted glow pulse |
| `.animate-float-gentle` | 8s infinite | Gentle floating |
| `.animate-ember-breathe` | 6s infinite | Slow opacity + blur pulse |
| `.animate-ember-drift` | 20s infinite | Slow positional drift |

---

## Staggered Card Entrance

```css
animation-delay: ${index < 12 ? `${index * 30}ms` : "0ms"};
animation-fill-mode: backwards;
```

First 12 cards: 30ms incremental delays. Beyond 12: instant.

---

## CSS Transition Patterns

### Hover (fastest)
```css
transition: background-color 80ms, color 80ms, border-color 80ms;
```

### Interactive Surface
```css
transition: background-color 80ms, color 80ms, border-color 80ms, box-shadow 80ms;
```

### Brutalist Button
```css
transition: background-color 80ms, color 80ms, box-shadow 80ms, transform 80ms;
```

### Card Base
```css
transition: box-shadow 250ms cubic-bezier(0.16, 1, 0.3, 1), opacity 250ms;
```

### Image Hover Zoom
```css
transition: transform 200ms cubic-bezier(0.16, 1, 0.3, 1);
transform: scale(1.03);
```

### Pillar Color Shift
```css
transition: color 300ms ease, background-color 300ms ease,
            border-color 300ms ease, box-shadow 300ms ease;
```

---

## Shimmer (Loading)

```css
background: linear-gradient(90deg,
  transparent 0%,
  rgba(var(--pillar-r), var(--pillar-g), var(--pillar-b), 0.03) 50%,
  transparent 100%);
background-size: 200% 100%;
animation: shimmer 1.5s infinite linear;
```

---

## Rules

- No bouncy/springy animations except tag-enter
- No animations > 600ms for UI elements
- No `transition: all` — always specify individual properties
- Hover states always `--duration-instant` (80ms)
- Enters use `--ease-out`, exits use `--ease-in`
- Always include `animation-fill-mode: forwards` (or `backwards` for staggered)
- Always respect `prefers-reduced-motion`
