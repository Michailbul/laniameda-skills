# Picker Page UX Spec

The picker is the core interaction of this workflow. It's an HTML page the user opens in their browser, clicks what they like, and exports a structured summary.

## Sections (top to bottom)

### 1. Header
- Brand name + "Brand Picker" title
- Subtitle in mono font
- Instructions: "Tap to select, tap again to deselect. Pick as many as you want. Hit Export Picks when done."

### 2. Accent Colors
- Grid of clickable swatches (all proposed accent colors)
- Each swatch: color block (88-120px tall) + name + hex code
- Exclude base/locked colors — those aren't up for selection

### 3. Font Pairings
- Grid of clickable cards
- Each card: pairing ID + headline sample in actual font + body sample in actual font
- Load all fonts via Google Fonts `@import`

### 4. Palette Directions (optional)
- Full direction cards if multiple directions were proposed
- Show gradient background + direction name + color dot row
- Useful when user wants to pick a whole direction rather than individual colors

### 5. Combo Cards
- Grid of clickable carousel-format cards (aspect-ratio: 1080/1350)
- Each card: background color + headline in locked font + body in locked font + accent bar
- Tag cards with their origin direction: `[B]`, `[C]`, etc.
- Vary: backgrounds, headline colors, font pairings, copy lines

### 6. Gradients
- Row of clickable gradient strips
- Each strip: gradient fill + label text

## Interactive Elements

### Selection behavior
```css
.selectable {
  cursor: pointer;
  position: relative;
}
.selectable.selected::after {
  border: 2.5px solid [brand-accent-color];
}
.selectable.selected::before {
  content: '✓'; /* checkmark badge */
  position: absolute; top: 8px; right: 12px;
  background: [brand-accent-color];
  border-radius: 50%;
}
```

### Floating bottom bar
- Fixed to bottom of viewport
- Shows: live pick count + "Clear all" button + "Export Picks" button
- Semi-transparent dark background with backdrop-filter blur

### Export modal
- Overlay with textarea containing structured pick summary
- "Copy to clipboard" button using `navigator.clipboard.writeText()`
- Close on overlay click or close button

## Data Attributes

Every selectable element needs:
```html
data-type="color|font|combo|gradient"
data-id="[descriptive identifier]"
```

The export function groups selections by type using these attributes.

## Copy Lines for Combo Cards

Use real brand-relevant lines, rotated across cards. Examples:
- "The work has weight or it doesn't ship."
- "Resonance over volume."
- "Artists first. Always."
- "Build in the open."
- "Craft is the filter."
- "Feel something."
- "AI-native creative studio."

Adapt these to the specific brand. Never use lorem ipsum or generic filler.

## Styling

- Dark background (#0e0c0a or similar)
- Brand fonts for headings
- JetBrains Mono or similar monospace for labels, hex codes, metadata
- Hover effects: translateY(-2px) on swatches and cards
- Max-width: 1600px, centered
- Responsive grid: `grid-template-columns: repeat(auto-fill, minmax(Xpx, 1fr))`
