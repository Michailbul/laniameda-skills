---
name: design-playground
description: "Spin up isolated React playgrounds with Leva control panels to experiment with UI effects, animations, shadows, hover states, and interaction patterns. Use when: 'build me a playground', 'give me knobs for', 'I want to experiment with', 'let me tweak', 'playground for X', 'try this effect', or when user wants to visually dial in a UI technique before integrating into production code. Also triggers when user shares a URL/tweet/CodePen and says 'I want to play with this' or 'let me try this technique'."
---

# Design Playground — Interactive UI Experimentation with Leva Controls

You build isolated, interactive playgrounds for experimenting with UI effects, animations, and design techniques. Every playground comes with a **Leva control panel** so the user can visually tweak every relevant parameter in real time — then export clean production code when they're happy.

**Your standard:** Fast to spin up. Beautiful defaults. Every knob that matters is exposed. Code exports clean.

---

## When This Skill Triggers

- "build me a playground for [effect]"
- "give me knobs for [component/animation]"
- "I want to experiment with [technique]"
- "let me tweak [shadows/timing/easing/colors/spacing]"
- "playground for hover animations"
- User shares a URL + "I want to play with this" / "let me try this technique"
- "try this effect on our components"
- Any request to visually dial in a UI technique before committing to production

---

## Stack

| Layer | Tool | Why |
|---|---|---|
| Scaffold | **Vite + React + TypeScript** | Fastest cold start, HMR, zero config |
| Controls | **Leva** (`leva`) | Best React control panel — auto-generates UI for any parameter |
| Styling | **Tailwind CSS** | Rapid utility-first styling |
| Animation | **Motion** (`motion/react`) | When the effect involves animation |
| 3D (optional) | **Three.js / R3F** | Only when the effect is 3D |

**Core install:**
```bash
npm create vite@latest playground-[name] -- --template react-ts
cd playground-[name]
npm install leva motion tailwindcss @tailwindcss/vite
```

---

## Playground Location

All playgrounds live in: `~/work/playgrounds/`

```
~/work/playgrounds/
  hover-cards/           # one playground per experiment
  shadow-layers/
  waveform-icons/
  ...
```

Each playground is standalone — no shared dependencies between experiments.

---

## Execution Protocol

### Step 1 — Understand the Experiment

Before scaffolding, clarify:
- **What effect?** (hover animation, shadow technique, micro-interaction, layout pattern, etc.)
- **Reference material?** (URL, screenshot, CodePen, tweet — if provided, fetch and analyze first)
- **Target context?** (what project/component will this eventually go into?)

If user provides a URL reference:
1. Fetch and read the source (use WebFetch or firecrawl)
2. Extract the core technique — CSS properties, animation values, the "trick"
3. Build the playground around that technique with Leva controls for all parameters

### Step 2 — Scaffold the Playground

```bash
cd ~/work/playgrounds
npm create vite@latest playground-[name] -- --template react-ts
cd playground-[name]
npm install leva motion tailwindcss @tailwindcss/vite
```

Set up Tailwind with Vite plugin in `vite.config.ts`:
```ts
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [react(), tailwindcss()],
})
```

Add to `src/index.css`:
```css
@import "tailwindcss";
```

### Step 3 — Build the Effect + Wire Up Leva

This is the core. For every playground:

1. **Implement the effect** with sensible defaults that look good immediately
2. **Identify every tweakable parameter** — timing, easing, colors, sizes, shadows, opacities, spreads, delays, spring configs, etc.
3. **Wire each parameter to Leva** using `useControls`
4. **Group controls logically** — use Leva folders for organization

**Leva patterns:**

```tsx
import { useControls, folder } from 'leva'

function Playground() {
  const controls = useControls({
    'Animation': folder({
      duration: { value: 0.3, min: 0.05, max: 2, step: 0.05 },
      easing: { options: ['ease', 'ease-in', 'ease-out', 'ease-in-out', 'linear'] },
      delay: { value: 0, min: 0, max: 1, step: 0.05 },
    }),
    'Visual': folder({
      background: '#ffffff',
      borderRadius: { value: 12, min: 0, max: 48, step: 1 },
      shadowLayers: { value: 3, min: 1, max: 6, step: 1 },
      shadowOpacity: { value: 0.1, min: 0, max: 1, step: 0.01 },
      shadowSpread: { value: 1, min: -10, max: 20, step: 0.5 },
    }),
    'Layout': folder({
      gap: { value: 16, min: 0, max: 64, step: 4 },
      padding: { value: 24, min: 0, max: 64, step: 4 },
      columns: { value: 3, min: 1, max: 6, step: 1 },
    }),
  })

  // Use controls.duration, controls.background, etc. directly in JSX/styles
}
```

**Key Leva input types to use:**
- `{ value: number, min, max, step }` — sliders for numeric values
- `{ options: [...] }` — dropdown for discrete choices
- `'#hex'` — color picker (just pass a hex string)
- `{ value: boolean }` — toggle
- `{ value: [x, y] }` — 2D point
- `folder({...})` — group related controls
- `button(() => action)` — action buttons (reset, randomize, export)

### Step 4 — Add Utility Features

Every playground should include:

**Export button** — copies the current parameter values as clean CSS/React code:
```tsx
import { button } from 'leva'

useControls({
  'Export': button(() => {
    const code = generateCode(controls)
    navigator.clipboard.writeText(code)
    console.log('Copied to clipboard!')
  }),
})
```

**Reset button** — snap back to defaults:
```tsx
useControls({
  'Reset': button(() => window.location.reload()),
})
```

**Multiple variants** — show the effect applied to several different elements (cards, buttons, icons) so the user sees how it scales:
```tsx
// Show a grid of cards, buttons, or components all using the same Leva-controlled values
```

### Step 5 — Run and Iterate

```bash
npm run dev
```

Open in the browser. The Leva panel appears in the top-right by default. User tweaks parameters, sees changes instantly via HMR + React state.

When the user says they're happy:
1. Read the current Leva values
2. Generate clean, production-ready code (no Leva dependency)
3. Output as a copyable snippet or write directly to the target project

---

## Playground Templates

### Shadow Layers (a la James McDonald / Yakob)
Multi-layered box-shadow technique. Controls: number of layers, base opacity, spread progression, color, blur factor.

### Hover Cards
Card grid with hover effects. Controls: scale, translateY, shadow elevation, transition timing, easing curve, border glow.

### Micro Animations
Icon/button micro-interactions. Controls: animation type (pulse, bounce, wiggle, spin), duration, spring stiffness, spring damping.

### Border Draw
CSS border-drawing animations on hover (corners → edges). Controls: border width, color, draw speed, secondary tracer delay, easing.

### Text Reveals
Text animation on scroll/view. Controls: stagger delay, direction (up/down/fade), blur amount, letter vs word split.

### Waveform / Audio Icons
Animated audio visualizer icons. Controls: bar count, animation speed, min/max height, style (bars/wave/dots), muted state.

---

## Reference-Based Playgrounds

When user provides a URL, tweet, or CodePen:

1. **Fetch the source** — read the HTML/CSS/JS
2. **Extract the core technique** — what makes it tick? (specific CSS properties, animation approach, math)
3. **Identify parameters** — what values would a designer want to tweak?
4. **Build playground** — implement the technique with all parameters wired to Leva
5. **Show before/after** — default values vs. the reference values, so user understands the range

Tell the user: "Here's the technique from [source]. I've wired up [N] controls. The defaults match the reference — start tweaking."

---

## Code Export Format

When exporting from a playground, output clean production code:

**React component** (no Leva, hardcoded best values):
```tsx
// hover-card.tsx — exported from playground
// Technique: multi-layer shadow border + scale hover

export function HoverCard({ children }: { children: React.ReactNode }) {
  return (
    <div className="group relative rounded-xl bg-white p-6 transition-all duration-300 ease-out hover:scale-[1.02] hover:-translate-y-1"
      style={{
        boxShadow: `
          0 1px 2px rgba(0,0,0,0.04),
          0 2px 4px rgba(0,0,0,0.04),
          0 4px 8px rgba(0,0,0,0.04)
        `,
      }}>
      {children}
    </div>
  )
}
```

**CSS custom properties** (for non-React targets):
```css
:root {
  --card-shadow: 0 1px 2px rgba(0,0,0,0.04), 0 2px 4px rgba(0,0,0,0.04), 0 4px 8px rgba(0,0,0,0.04);
  --card-radius: 12px;
  --card-hover-scale: 1.02;
  --card-hover-lift: -4px;
  --card-transition: all 0.3s ease-out;
}
```

---

## Hard Rules

- **Leva is mandatory.** Every playground has a control panel. No exceptions.
- **Beautiful defaults.** The playground should look good the moment it loads — not broken waiting for tweaks.
- **Standalone.** Each playground is its own Vite app. No coupling between experiments.
- **Fast.** Scaffold → working playground should take under 2 minutes.
- **Export clean.** When exporting, strip all Leva/playground scaffolding. Output production-ready code only.
- **Don't over-engineer.** A playground is disposable. It exists to find the right values, not to be a product.
- **Show multiple variants.** Always render the effect on several elements so the user sees how it scales across different sizes/content.
