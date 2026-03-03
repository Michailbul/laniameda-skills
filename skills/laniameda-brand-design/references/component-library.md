# Laniameda Component Library — Pencil Specs

## Overview

These reusable components form the foundation for laniameda landing pages. Build them first (with `reusable: true`), then instantiate as `ref` nodes throughout screens.

---

## 1. macOS Window Chrome

A macOS-style window frame with traffic light dots and title bar — the signature element for developer-focused designs.

### Structure
```
macOS Window (frame, reusable: true)
├── Titlebar (frame, horizontal)
│   ├── Red dot (ellipse, 12x12, fill: #ff5f56)
│   ├── Yellow dot (ellipse, 12x12, fill: #ffbd2e)
│   ├── Green dot (ellipse, 12x12, fill: #27c93f)
│   └── Title (text, "SOUL.md", JetBrains Mono 11px, ghost color)
└── Body (frame, placeholder: true)
```

### Properties
| Property | Value |
|----------|-------|
| Width | 600 (default, override per instance) |
| Height | fit_content |
| Fill | `#1a1a1a` (dark) |
| Corner Radius | `[12, 12, 0, 0]` top corners only |
| Border | 1px `rgba(255,255,255,0.08)` |
| Titlebar height | 40px |
| Titlebar fill | `#2a2a2a` |
| Titlebar padding | `[0, 16, 0, 16]` |
| Dot gap | 8px |
| Body padding | 24px |

### Usage
```javascript
terminal=I(hero, { type: "ref", ref: "macWindowId", width: 560 })
U(terminal+"/titleId", { content: "agent-hub" })
// Add content to body
code=I(terminal+"/bodyId", {
  type: "text",
  content: "$ npx @laniameda/agent-hub",
  fontFamily: "JetBrains Mono",
  fontSize: 13,
  fill: "#e0e0e0"
})
```

---

## 2. CTA Pill

Primary call-to-action button — coral background with monospace command text.

### Structure
```
CTA Pill (frame, reusable: true)
├── Prompt (text, "$_", JetBrains Mono 13px, rgba(255,255,255,0.6))
└── Command (text, "npx @laniameda/agent-hub", JetBrains Mono 14px, white bold)
```

### Properties
| Property | Value |
|----------|-------|
| Layout | horizontal, gap: 8, alignItems: center |
| Fill | `#ff7a64` (coral) |
| Corner Radius | 9999 (pill) |
| Padding | `[16, 28, 16, 28]` |
| Width | fit_content |
| Height | fit_content |
| Shadow | `--shadow-brutal` on hover |

### Usage
```javascript
cta=I(hero, { type: "ref", ref: "ctaPillId" })
U(cta+"/commandId", { content: "npx @laniameda/agent-hub" })
```

---

## 3. Ghost Button

Secondary action — ink outline with monospace label, used for "View on GitHub" etc.

### Structure
```
Ghost Button (frame, reusable: true)
└── Label (text, "View on GitHub →", JetBrains Mono 13px, ink)
```

### Properties
| Property | Value |
|----------|-------|
| Layout | horizontal, alignItems: center, justifyContent: center |
| Fill | transparent |
| Stroke | 2px `#201710` |
| Corner Radius | 9999 (pill) |
| Padding | `[14, 28, 14, 28]` |
| Width | fit_content |
| Height | fit_content |
| Hover | fill `#201710`, text `#fafafa`, translate(-2px,-2px), shadow brutal-sm |

### Usage
```javascript
btn=I(ctaRow, { type: "ref", ref: "ghostBtnId" })
U(btn+"/labelId", { content: "View on GitHub →" })
```

---

## 4. Section Label

Monospace coral eyebrow text with `//` prefix — marks the start of each page section.

### Structure
```
Section Label (text, reusable: true)
  content: "// section_name"
  font: JetBrains Mono, 11px, weight 500
  fill: #ff7a64 (coral)
  letterSpacing: 0.12
  textTransform: uppercase
```

### Properties
| Property | Value |
|----------|-------|
| Font | JetBrains Mono |
| Size | 11px |
| Weight | 500 |
| Fill | `#ff7a64` |
| Letter Spacing | 0.12 |
| Transform | uppercase |

### Usage
```javascript
label=I(section, { type: "ref", ref: "sectionLabelId" })
U(label+"/labelTextId", { content: "// features" })
```

---

## 5. Brutalist Card

Zero-radius card with ink offset shadow — used for problems, features, dense layouts.

### Structure
```
Brutalist Card (frame, reusable: true)
├── Icon (text, emoji, 24px)
├── Title (text, Inter 16px bold, ink)
└── Description (text, Inter 14px, text-secondary)
```

### Properties
| Property | Value |
|----------|-------|
| Layout | vertical, gap: 12 |
| Fill | `#fffaf5` (paper) or `#fff4ea` (surface-1) |
| Stroke | 2px `#201710` |
| Corner Radius | 0 (zero — brutalist) |
| Padding | 24px |
| Shadow | `4px 4px 0 #201710` |
| Width | fill_container (in grid) |
| Height | fit_content |
| Hover | translate(-2px,-2px), shadow `6px 6px 0` |

### Variants
- **Dark variant**: fill `#1a1a1a`, stroke `rgba(255,255,255,0.1)`, text white
- **Coral shadow variant**: shadow `4px 4px 0 #ff7a64`

### Usage
```javascript
card=I(grid, { type: "ref", ref: "brutalCardId", width: "fill_container" })
U(card+"/iconId", { content: "⬜" })
U(card+"/titleId", { content: "Multi-pane editor" })
U(card+"/descId", { content: "VSCode-style up to 4 panes." })
```

---

## 6. Soft Card

Rounded card with editorial shadow — used for lighter, more premium layouts.

### Structure
```
Soft Card (frame, reusable: true)
├── Icon (text, emoji, 24px)
├── Title (text, Inter 16px semibold, ink)
└── Description (text, Inter 14px, text-secondary)
```

### Properties
| Property | Value |
|----------|-------|
| Layout | vertical, gap: 12 |
| Fill | `#fff4ea` (surface-1) |
| Stroke | 1px `rgba(32,23,16,0.1)` |
| Corner Radius | 20px |
| Padding | 24px |
| Shadow | `--shadow-sm` (soft editorial) |
| Width | fill_container |
| Height | fit_content |
| Hover | shadow `--shadow-md`, subtle lift |

### Usage
```javascript
card=I(grid, { type: "ref", ref: "softCardId", width: "fill_container" })
U(card+"/iconId", { content: "🧩" })
U(card+"/titleId", { content: "Skill browser" })
U(card+"/descId", { content: "All skills in one sidebar." })
```

---

## 7. Badge — Ink Variant

Dark pill badge for metadata labels.

### Structure
```
Badge Ink (frame, reusable: true)
└── Label (text, JetBrains Mono 10px, white, uppercase)
```

### Properties
| Property | Value |
|----------|-------|
| Fill | `#201710` (ink) |
| Corner Radius | 9999 (pill) |
| Padding | `[6, 14, 6, 14]` |
| Text fill | `#ffffff` |

### Usage
```javascript
badge=I(row, { type: "ref", ref: "badgeInkId" })
U(badge+"/labelId", { content: "MIT LICENSE" })
```

---

## 8. Badge — Coral Variant

Accent pill badge for highlighted labels.

### Structure
```
Badge Coral (frame, reusable: true)
└── Label (text, JetBrains Mono 10px, white, uppercase)
```

### Properties
| Property | Value |
|----------|-------|
| Fill | `#ff7a64` (coral) |
| Corner Radius | 9999 (pill) |
| Padding | `[6, 14, 6, 14]` |
| Text fill | `#ffffff` |

### Usage
```javascript
badge=I(row, { type: "ref", ref: "badgeCoralId" })
U(badge+"/labelId", { content: "OPEN SOURCE" })
```

---

## Component ID Reference

When working with an existing laniameda Pencil document, common component IDs (may vary per file):

| Component | Typical ID | Key Descendants |
|-----------|-----------|-----------------|
| macOS Window | `mPZJ7` | titlebar: `cIJkm`, body: `F0ONo`, title: `o7veF` |
| CTA Pill | `eEeBZ` | prompt: `sbHfR`, command: `A01jK` |
| Ghost Button | `tQz0i` | label: `vTlio` |
| Section Label | `lmwEH` | label: `IYXf6` |
| Brutalist Card | `vNRUQ` | icon: `zVXCV`, title: `Xt8NU`, desc: `Ui1sl` |
| Soft Card | `x6RiC` | icon: `2qL6u`, title: `7i7mk`, desc: `DtAOn` |
| Badge Ink | `2UhyS` | label: `SXONw` |
| Badge Coral | `D4PHq` | label: `N5whr` |

**Note**: These IDs are from the Agent Hub landing page project. For new projects, build fresh components and note their IDs.

---

## Assembly Order

1. Create all components with `reusable: true` FIRST
2. Note their IDs and descendant IDs
3. Build screens by inserting `ref` instances
4. Customize instances via `U(instance+"/descendantId", {...})`
5. Never modify the component definition once instances exist (modify instances instead)
