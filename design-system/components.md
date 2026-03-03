# Component Patterns

Warm brutalist-editorial hybrid: soft paper surfaces and pill shapes meet industrial monospace labels and sharp offset shadows.

Components use **CVA (class-variance-authority)** for variants and **Radix UI** for accessibility.

---

## Buttons

### Variants

| Variant | Fill | Text | Hover | Use |
|---------|------|------|-------|-----|
| default | `--coral` | white | coral/90 | Primary CTAs |
| outline | transparent | `--foreground` | `--muted` fill | Secondary actions |
| secondary | `--surface-2` | `--text-secondary` | secondary/80 | Tertiary |
| ghost | transparent | inherited | `--muted` fill | Toolbar, icon |
| destructive | destructive/10 | `--destructive` | destructive/20 | Delete |
| link | transparent | `--coral` | underline | Inline |

### Sizes

| Size | Height | Padding |
|------|--------|---------|
| xs | 24px | `px-2` |
| sm | 28px | `px-2.5` |
| default | 32px | `px-3` |
| lg | 36px | `px-4` |

**Shape**: All `rounded-full` (pill). Non-negotiable.
**Active**: `active:scale-[0.98]` press feedback.

---

## Brutalist Buttons

Industrial CTAs using CSS classes, not CVA.

### `.btn-brutal` (Primary)
```
Rest:   bg: #18181b, text: white, mono 11px uppercase, tracking 0.12em
Hover:  bg: coral, shadow: 4px 4px 0 ink, translate(-2px, -2px)
Active: shadow: none, translate(0, 0)
```

### `.btn-brutal-outline` (Outline)
```
Rest:   bg: transparent, border: --border-strong, text: ink, mono 10px uppercase
Hover:  bg: #18181b, text: white, shadow: 2px 2px 0 ink, translate(-1px, -1px)
Active: shadow: none, translate(0, 0)
```

---

## Badges

Pill-shaped indicators.

| Variant | Style |
|---------|-------|
| default | Coral fill, white text |
| secondary | Surface-2 fill, secondary text |
| outline | Bordered, foreground text |
| ghost | Transparent, muted text |

Shape: `rounded-full`, height `h-6` (24px), font `text-xs font-medium`.

---

## Cards

### Brutalist Card
- **Fill**: paper or surface-1
- **Stroke**: 2px ink
- **Radius**: 0px (zero)
- **Shadow**: `4px 4px 0 #201710`
- **Hover**: translate(-2px,-2px), shadow 6px 6px 0
- **Content**: icon + title (16px bold) + desc (14px secondary)

### Soft Card
- **Fill**: surface-1
- **Stroke**: 1px `rgba(32,23,16,0.1)`
- **Radius**: 20px
- **Shadow**: `--shadow-sm`
- **Hover**: `--shadow-md`, subtle lift
- **Content**: icon + title (16px semibold) + desc (14px secondary)

### Image Card (Masonry)
- **Radius**: 24px
- **Shadow**: `--shadow-sharp` at rest
- **Hover**: `--shadow-elevated` + pillar glow ring + image scale(1.03)
- **Selected**: `--shadow-pillar-glow` + extended glow
- **Badges**: model (glass bg, mono 9px) + pillar (colored dot)
- **Overlay**: gradient from transparent to dark, mono 10px prompt text

---

## macOS Window Chrome

Developer-focused container mimicking macOS window:

```
┌─ [🔴 🟡 🟢] ─── title.md ─────────┐
│                                       │
│   Terminal / code content here        │
│                                       │
└───────────────────────────────────────┘
```

- **Titlebar**: 40px, fill `#2a2a2a`, traffic lights (12x12px circles)
- **Body**: placeholder, fill `#1a1a1a`, padding 24px
- **Corner radius**: 12px top corners
- **Border**: 1px `rgba(255,255,255,0.08)`
- **Traffic lights**: red `#ff5f56`, yellow `#ffbd2e`, green `#27c93f`

---

## Section Labels (Eyebrows)

Monospace coral text marking section starts:

```css
font: 11px JetBrains Mono/Geist Mono, weight 500;
color: var(--coral);
text-transform: uppercase;
letter-spacing: 0.12em;
content: "// section_name";
```

---

## CTA Pill

Primary install action — coral background, monospace command:

```
┌─ $_  npx @laniameda/agent-hub ─┐
└────────────────────────────────────┘
```

- **Fill**: coral
- **Radius**: pill (9999px)
- **Padding**: 16px 28px
- **Prompt**: `$_` in 60% white opacity
- **Command**: white bold mono 14px

---

## Ghost Button

Secondary action — ink outline, mono label:

```
┌─── View on GitHub → ───┐
└────────────────────────────┘
```

- **Fill**: transparent
- **Stroke**: 2px ink
- **Radius**: pill
- **Padding**: 14px 28px
- **Hover**: fill ink, text inverse, shadow brutal-sm

---

## Tag Pills

Interactive filter tags:

| State | Background | Border | Text |
|-------|-----------|--------|------|
| Inactive | transparent | `--border-default` | `--text-secondary` |
| Inactive:hover | `--surface-2` | `--border-strong` | `--text-primary` |
| Active | `--accent-subtle` | coral/35 | `--coral` |

Shape: pill, font 13px medium, enter animation: scale 0.8→1 (120ms spring).

---

## Sidebar Navigation

### NavItem States

| State | Background | Text | Indicator |
|-------|-----------|------|-----------|
| Inactive | transparent | `--text-secondary` | Hidden |
| Hover | white/42 | `--text-primary` | Hidden |
| Active | white/52 | `--text-primary` | Coral diamond 7x7 |

Icon container: 26x26px, rounded-[6px], bordered.
Label: mono 11px uppercase, tracking 0.08→0.1em active.

---

## Interactive Utility Classes

| Class | Hover Effect |
|-------|-------------|
| `.interactive-ghost` | surface-2 bg, text-primary color |
| `.interactive-surface` | surface-3 bg, text-primary color |
| `.interactive-primary` | coral-hover bg, brutal-accent shadow, translate(-1px) |

---

## Rules

- No custom radius outside the scale — buttons pill, cards xl or 0
- All interactive elements have visible focus states (coral ring, 2px offset)
- All buttons include `active:scale-[0.98]`
- Brutalist elements always pair shadow with transform offset
- No `onMouseEnter/Leave` for styling — use CSS hover
