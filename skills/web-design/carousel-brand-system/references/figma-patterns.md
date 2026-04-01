# Figma MCP Patterns for Carousel Brand Systems

Patterns proven during the Laniameda v2.0 build. Reference these when building the Figma design system page.

## Page Structure

```
Master Frame — vertical auto-layout, no fills, 60px padding, 32px itemSpacing
  Header
  01 COLOR SYSTEM section header
    Primary Palette label + swatches row
    Primary Accents label + swatches row
    Supporting Accents label + swatches row
    Situational Accents label + swatches row
    Color Rules panel
  02 TYPOGRAPHY section header
    Font Showcase Row 1 (3 cards)
    Font Showcase Row 2 (3 cards)
    Font Showcase Row 3 (3 cards)
    Font Showcase Row 4 (3 cards)
    Type Scale (optional)
  02B THEMES header
    Theme Cards (dark + light side by side)
  01B COLOR PAIRINGS header
    Primary Reading Pairs label + row
    Accent on Dark Surfaces label + row
    Statement Backgrounds label + row
  03 GRADIENTS header
    Gradient Row 1
    Gradient Row 2
  04 USAGE GUIDELINES header
    Do / Don't columns
    Carousel Cheatsheet panel
  Footer
```

## Color Swatch Component

```js
// Swatch: 240x~175, vertical auto-layout
const swatch = figma.createFrame();
swatch.layoutMode = 'VERTICAL';
swatch.primaryAxisSizingMode = 'AUTO';
swatch.counterAxisSizingMode = 'AUTO';
swatch.cornerRadius = 12;
swatch.clipsContent = true;

// Color block (top)
const colorBlock = figma.createFrame();
colorBlock.resize(240, 120);
colorBlock.fills = [{ type: 'SOLID', color: { r, g, b } }];
swatch.appendChild(colorBlock);

// Info block (bottom)
const info = figma.createFrame();
info.layoutMode = 'VERTICAL';
info.primaryAxisSizingMode = 'AUTO';
info.counterAxisSizingMode = 'FIXED';
info.resize(240, 10);
info.paddingTop = 12; info.paddingBottom = 12;
info.paddingLeft = 14; info.paddingRight = 14;
info.itemSpacing = 4;
info.fills = [{ type: 'SOLID', color: { r: 0.1, g: 0.09, b: 0.08 } }];
swatch.appendChild(info);
// Add name (Inter Bold 14), hex (Inter Regular 11), role (Inter Regular 10) text nodes
```

## Carousel Combo Card (1080x1350)

The most important component. Matches the HTML picker card layout.

```js
const card = figma.createFrame();
card.resize(1080, 1350);
card.layoutMode = 'VERTICAL';
card.primaryAxisSizingMode = 'FIXED';  // height stays 1350
card.counterAxisSizingMode = 'FIXED';  // width stays 1080
card.paddingTop = 64;
card.paddingBottom = 56;
card.paddingLeft = 64;
card.paddingRight = 64;
card.itemSpacing = 0;
card.clipsContent = true;
card.cornerRadius = 16;
card.fills = bgFills;

// TOP GROUP — label + bar + headline
const top = figma.createFrame();
top.layoutMode = 'VERTICAL';
top.primaryAxisSizingMode = 'AUTO';
top.counterAxisSizingMode = 'AUTO';
top.itemSpacing = 16;
top.fills = [];
card.appendChild(top);
top.layoutSizingHorizontal = 'FILL';  // AFTER appendChild

  // Label: Inter Regular 13px, uppercase, letterSpacing 10%, opacity 0.4
  // Accent bar: 48x4, cornerRadius 2, fill = accent color
  // Headline: [font family + style], [size], letterSpacing -2%

// FLEX SPACER — pushes bottom group down
const spacer = figma.createFrame();
spacer.fills = [];
spacer.resize(100, 100);
card.appendChild(spacer);
spacer.layoutSizingHorizontal = 'FILL';
spacer.layoutSizingVertical = 'FILL';  // this is the magic — fills remaining space

// BOTTOM GROUP — body text + meta label
const bottom = figma.createFrame();
bottom.layoutMode = 'VERTICAL';
bottom.primaryAxisSizingMode = 'AUTO';
bottom.counterAxisSizingMode = 'AUTO';
bottom.itemSpacing = 16;
bottom.fills = [];
card.appendChild(bottom);
bottom.layoutSizingHorizontal = 'FILL';

  // Body: [body font] 24px, lineHeight 38px, opacity 0.75
  // Meta: Inter Regular 11px, uppercase, letterSpacing 8%, opacity 0.25
```

## Gradient Card

```js
const gradCard = figma.createFrame();
gradCard.resize(1300, 200);
gradCard.cornerRadius = 16;
gradCard.fills = [{
  type: 'GRADIENT_LINEAR',
  gradientTransform: [[1, 0, 0], [0, 1, 0]], // left→right
  gradientStops: [
    { position: 0, color: { ...color1, a: 1 } },
    { position: 1, color: { ...color2, a: 1 } }
  ]
}];
// Add label text node at bottom-left
```

## Color Pairing Swatch

```js
// Small card showing text color on background color
const pair = figma.createFrame();
pair.resize(260, 140);
pair.cornerRadius = 12;
pair.fills = [{ type: 'SOLID', color: bgColor }];
pair.layoutMode = 'VERTICAL';
pair.primaryAxisSizingMode = 'FIXED';
pair.counterAxisSizingMode = 'FIXED';
pair.paddingTop = 16; pair.paddingLeft = 20;
pair.paddingRight = 20; pair.paddingBottom = 16;
pair.itemSpacing = 6;

// "Aa" sample at 32px Bold
// Label at 10px Regular: "[text color] on [bg color]"
```

## Common Gotchas

1. **`layoutSizingHorizontal = 'FILL'`** must be set AFTER `parent.appendChild(child)` — it won't stick if set before
2. **`counterAxisSizingMode`** only accepts `'FIXED'` or `'AUTO'` — never `'FILL'`
3. **Font style names have spaces**: `'Semi Bold'` not `'SemiBold'`, `'Extra Bold'` not `'ExtraBold'`
4. **`figma.setCurrentPageAsync(page)`** not `figma.currentPage = page`
5. **Frames created with `resize(w, 10)`** then `primaryAxisSizingMode = 'AUTO'` will auto-expand — but only if children have defined heights
6. **Colors are 0-1 range** not 0-255
7. **Always `await figma.loadFontAsync()`** before creating text nodes
