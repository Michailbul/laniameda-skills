# Color Exploration Page Structure

Template structure for the `color-exploration.html` page generated in Phase 2.

## Page Layout

```
Title: "[Brand] — Color Palette Exploration"
Subtitle: "complementary accent directions"

Section: Current Locked Palette
  → Base palette swatches
  → Current accents (if any — to compare against)

---

Section: Option [X] — [Direction Name]
  Tag: [mood keyword]
  Vibe: [one-line italic description]

  Swatch row: 5 accent colors with name + hex + role

  Combo cards (3 per direction):
    - Dark bg variant
    - Colored bg variant
    - Light bg variant
    Each card: 320x420, rounded, headline + body text + label

  Gradient strips (3-4 per direction):
    - Key gradient combinations using the direction's colors

[Repeat for 3-4 directions]

---

Section: Quick Comparison
  Table: Direction | Temperature | Mood | Best for | Risk

Section: Recommendation (optional)
  Highlighted panel with reasoning for top pick
```

## CSS Architecture

```css
/* Base */
body { background: #0e0c0a; color: #F0EBE8; font-family: 'Inter', sans-serif; }

/* Swatches */
.swatch { border-radius: 12px; background: #1a1714; border: 1px solid #2a2520; }
.swatch-color { height: 100-120px; }
.swatch-info { padding: 12-14px; }

/* Combo cards — carousel aspect ratio */
.combo-card {
  width: 320px;
  height: 420px; /* or use aspect-ratio: 1080/1350 */
  border-radius: 12px;
  padding: 32px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

/* Gradients */
.gradient-strip {
  height: 72-80px;
  border-radius: 10px;
  display: flex;
  align-items: flex-end;
  padding: 10px 14px;
}

/* Tags */
.tag {
  font-family: monospace;
  font-size: 0.7rem;
  padding: 3px 10px;
  border-radius: 3px;
  text-transform: uppercase;
}
```

## Combo Card Content

Each combo card should show:
1. **Top:** Small label describing the combination (mono, uppercase, small)
2. **Accent bar:** Thin colored line (40px wide, 4px tall)
3. **Headline:** 2-3 words in display font at ~2.2rem
4. **Bottom:** Body text in body font at ~0.85rem

Use brand-relevant copy. Rotate through 4-5 different lines.

## Direction Naming Convention

Each direction needs:
- **A name** (2 words max): "Burnt Earth", "Midnight Studio", "Signal + Silence", "Atelier"
- **A vibe line** (one sentence, italic): "Late-night creative session. Coffee and code."
- **A tag** with mood keyword: "warm analog", "minimal impact", "studio warmth"
