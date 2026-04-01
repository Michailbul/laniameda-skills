---
name: magnetic-dots-background
description: Implement an interactive magnetic dotted canvas background with ripple effects, flow animation, and mouse attraction physics. Use when building landing pages, hero sections, or any full-screen interactive background in React / Next.js. The surface is achromatic and dark-mode-aware — dots are white on dark, gray on light. Supports click-triggered ripple waves and sinusoidal ambient flow. Drop-in component with full prop control.
---

# Magnetic Dots Background

## What This Is

A canvas-based animated background where:
- Dots sit on an angled grid and drift with a sinusoidal flow field
- The mouse exerts magnetic attraction — dots pull toward the cursor
- Clicking sends expanding ripple waves outward from the click point
- Multiple ripples can exist simultaneously and interact
- Dark mode: white dots. Light mode: semi-transparent gray dots
- Responds to window resize automatically

This is the aesthetic: minimal, achromatic, motion-heavy surface beneath sparse editorial content. The motion does the talking.

## Source Project

Reference: `/Users/michael/work/laniameda/portfolio-websites/magnetic-dots/`
Stack: Next.js 16, Tailwind CSS v4, shadcn/ui, React 19

---

## Design System

### Color System (oklch, achromatic)

All tokens use zero chroma — purely grayscale using oklch. No accent colors.

```css
/* Light mode */
:root {
  --background: oklch(1 0 0);           /* pure white */
  --foreground: oklch(0.145 0 0);       /* near-black */
  --card: oklch(1 0 0);
  --muted: oklch(0.97 0 0);
  --muted-foreground: oklch(0.556 0 0);
  --border: oklch(0.922 0 0);
  --input: oklch(0.922 0 0);
  --ring: oklch(0.708 0 0);
  --radius: 0.625rem;
}

/* Dark mode */
.dark {
  --background: oklch(0.145 0 0);       /* near-black */
  --foreground: oklch(0.985 0 0);       /* near-white */
  --card: oklch(0.205 0 0);
  --muted: oklch(0.269 0 0);
  --muted-foreground: oklch(0.708 0 0);
  --border: oklch(1 0 0 / 10%);
  --input: oklch(1 0 0 / 15%);
  --ring: oklch(0.556 0 0);
  --accent: oklch(0.371 0 0);
}
```

### Typography

Three fonts loaded via `next/font/google`:

| Role | Font | Usage |
|---|---|---|
| `--font-sans` | Geist | Default body, UI elements |
| `--font-mono` | Geist Mono | Headings, labels, code — the **primary display voice** |
| `--font-serif` | Source Serif 4 | Accent / editorial use |

**Key pattern:** Headings use `font-mono font-light` — not sans. This gives the tech-minimal feel. Example:
```tsx
<h1 className="text-5xl tracking-tight font-mono font-light text-balance">...</h1>
<p className="text-lg text-muted-foreground font-mono text-pretty">...</p>
```

### Shadow System

Computed from CSS variables, minimal opacity:
```css
--shadow-x: 0px;
--shadow-y: 1px;
--shadow-blur: 2px;
--shadow-spread: 0px;
--shadow-opacity: 0.05;       /* 5% — barely visible */
--shadow-color: #000000;
```

### Border Radius
- Base: `0.625rem`
- `--radius-sm`: base - 4px
- `--radius-md`: base - 2px
- `--radius-lg`: base
- `--radius-xl`: base + 4px

---

## The MagneticDots Component

Full component code — copy verbatim into `components/magnetic-dots.tsx`:

```tsx
"use client"

import { useEffect, useRef } from "react"

interface Dot {
  x: number
  y: number
  baseX: number
  baseY: number
  vx: number
  vy: number
  flowOffset: number
}

interface Ripple {
  x: number
  y: number
  startTime: number
  duration: number
}

interface MagneticDotsProps {
  dotSize?: number
  dotSpacing?: number
  attractionRadius?: number
  attractionStrength?: number
  springStrength?: number
  damping?: number
  dotColor?: string
  className?: string
  flowAngle?: number
  flowSpeed?: number
  flowAmplitude?: number
  rippleSpeed?: number
  rippleStrength?: number
  rippleDuration?: number
}

export function MagneticDots({
  dotSize = 2,
  dotSpacing = 15,
  attractionRadius = 1000,
  attractionStrength = 300,
  springStrength = 0.003,
  damping = 0.96,
  dotColor = "rgba(100, 100, 100, 0.5)",
  className = "",
  flowAngle = 25,
  flowSpeed = 0.02,
  flowAmplitude = 15,
  rippleSpeed = 600,
  rippleStrength = 80,
  rippleDuration = 1500,
}: MagneticDotsProps) {
  const canvasRef = useRef<HTMLCanvasElement>(null)
  const dotsRef = useRef<Dot[]>([])
  const mouseRef = useRef({ x: -1000, y: -1000 })
  const animationFrameRef = useRef<number>()
  const timeRef = useRef<number>(0)
  const isDarkRef = useRef(false)
  const ripplesRef = useRef<Ripple[]>([])

  useEffect(() => {
    const checkDarkMode = () => {
      isDarkRef.current = document.documentElement.classList.contains("dark")
    }
    checkDarkMode()
    const observer = new MutationObserver(checkDarkMode)
    observer.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ["class"],
    })
    return () => observer.disconnect()
  }, [])

  useEffect(() => {
    const canvas = canvasRef.current
    if (!canvas) return
    const ctx = canvas.getContext("2d")
    if (!ctx) return

    const resizeCanvas = () => {
      canvas.width = window.innerWidth
      canvas.height = window.innerHeight
      initializeDots()
    }

    const initializeDots = () => {
      const dots: Dot[] = []
      const angleRad = (flowAngle * Math.PI) / 180
      const cols = Math.ceil((canvas.width + canvas.height * Math.abs(Math.tan(angleRad))) / dotSpacing) + 2
      const rows = Math.ceil((canvas.height + canvas.width * Math.abs(Math.tan(angleRad))) / dotSpacing) + 2

      for (let i = 0; i < cols; i++) {
        for (let j = 0; j < rows; j++) {
          const x = i * dotSpacing - j * dotSpacing * Math.sin(angleRad)
          const y = j * dotSpacing
          if (
            x > -dotSpacing * 2 &&
            x < canvas.width + dotSpacing * 2 &&
            y > -dotSpacing * 2 &&
            y < canvas.height + dotSpacing * 2
          ) {
            dots.push({ x, y, baseX: x, baseY: y, vx: 0, vy: 0, flowOffset: (i + j) * 0.5 })
          }
        }
      }
      dotsRef.current = dots
    }

    const handleMouseMove = (e: MouseEvent) => {
      mouseRef.current = { x: e.clientX, y: e.clientY }
    }
    const handleMouseLeave = () => {
      mouseRef.current = { x: -1000, y: -1000 }
    }
    const handleClick = (e: MouseEvent) => {
      ripplesRef.current.push({
        x: e.clientX,
        y: e.clientY,
        startTime: Date.now(),
        duration: rippleDuration,
      })
    }

    const animate = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height)
      timeRef.current += flowSpeed
      const currentTime = Date.now()

      ripplesRef.current = ripplesRef.current.filter(
        (ripple) => currentTime - ripple.startTime < ripple.duration
      )

      const mouseX = mouseRef.current.x
      const mouseY = mouseRef.current.y

      dotsRef.current.forEach((dot) => {
        const flowX = Math.sin(timeRef.current + dot.flowOffset) * flowAmplitude
        const flowY = Math.cos(timeRef.current + dot.flowOffset * 0.7) * (flowAmplitude * 0.5)
        const targetBaseX = dot.baseX + flowX
        const targetBaseY = dot.baseY + flowY

        const dx = mouseX - dot.x
        const dy = mouseY - dot.y
        const distance = Math.sqrt(dx * dx + dy * dy)

        if (distance < attractionRadius && distance > 0) {
          const normalizedDistance = distance / attractionRadius
          const force = (1 - normalizedDistance) * attractionStrength
          dot.vx += (dx / distance) * force * 2.0
          dot.vy += (dy / distance) * force * 2.0
        }

        ripplesRef.current.forEach((ripple) => {
          const elapsed = currentTime - ripple.startTime
          const progress = elapsed / ripple.duration
          const rdx = dot.x - ripple.x
          const rdy = dot.y - ripple.y
          const rippleDistance = Math.sqrt(rdx * rdx + rdy * rdy)
          const rippleRadius = progress * rippleSpeed
          const distanceFromWave = Math.abs(rippleDistance - rippleRadius)
          const waveWidth = 100

          if (distanceFromWave < waveWidth) {
            const waveStrength = Math.cos((distanceFromWave / waveWidth) * Math.PI) * 0.5 + 0.5
            const fadeFactor = 1 - progress
            const totalStrength = waveStrength * fadeFactor * rippleStrength
            if (rippleDistance > 0) {
              dot.vx += (rdx / rippleDistance) * totalStrength
              dot.vy += (rdy / rippleDistance) * totalStrength
            }
          }
        })

        const springDx = targetBaseX - dot.x
        const springDy = targetBaseY - dot.y
        dot.vx += springDx * springStrength
        dot.vy += springDy * springStrength
        dot.vx *= damping
        dot.vy *= damping
        dot.x += dot.vx
        dot.y += dot.vy

        ctx.fillStyle = isDarkRef.current ? "rgba(255, 255, 255, 1)" : dotColor
        ctx.beginPath()
        ctx.arc(dot.x, dot.y, dotSize, 0, Math.PI * 2)
        ctx.fill()
      })

      animationFrameRef.current = requestAnimationFrame(animate)
    }

    resizeCanvas()
    window.addEventListener("resize", resizeCanvas)
    window.addEventListener("mousemove", handleMouseMove)
    window.addEventListener("mouseleave", handleMouseLeave)
    window.addEventListener("click", handleClick)
    animate()

    return () => {
      window.removeEventListener("resize", resizeCanvas)
      window.removeEventListener("mousemove", handleMouseMove)
      window.removeEventListener("mouseleave", handleMouseLeave)
      window.removeEventListener("click", handleClick)
      if (animationFrameRef.current) cancelAnimationFrame(animationFrameRef.current)
    }
  }, [
    dotSize, dotSpacing, attractionRadius, attractionStrength,
    springStrength, damping, dotColor, flowAngle, flowSpeed,
    flowAmplitude, rippleSpeed, rippleStrength, rippleDuration,
  ])

  return <canvas ref={canvasRef} className={`fixed inset-0 ${className}`} style={{ pointerEvents: "none" }} />
}
```

---

## Page Layout Pattern

The canvas is `fixed inset-0` with `pointerEvents: none`. All content sits above it via `relative z-10`:

```tsx
<main className="relative min-h-screen bg-background">
  <MagneticDots
    dotSize={2}
    dotSpacing={35}
    attractionRadius={180}
    attractionStrength={0.3}
    springStrength={0.05}
    damping={0.85}
    dotColor="rgba(100, 100, 100, 0.5)"
  />
  <div className="relative z-10 flex min-h-screen flex-col items-center justify-center p-8">
    {/* content here */}
  </div>
</main>
```

Note: `page.tsx` uses gentler props (`attractionStrength={0.3}`) than the component defaults (`attractionStrength=300`). The defaults in the component source are the dramatic/v0-demo values. The page overrides dial it back for subtle use.

---

## Props Reference

| Prop | Default | Effect |
|---|---|---|
| `dotSize` | `2` | Dot radius in px |
| `dotSpacing` | `15` | Grid cell size in px — lower = denser |
| `attractionRadius` | `1000` | Mouse attraction reach in px |
| `attractionStrength` | `300` | Pull force magnitude |
| `springStrength` | `0.003` | Return-to-base spring force |
| `damping` | `0.96` | Velocity decay per frame (0-1, higher = slower decay) |
| `dotColor` | `rgba(100,100,100,0.5)` | Light mode dot color only |
| `flowAngle` | `25` | Grid angle in degrees |
| `flowSpeed` | `0.02` | Ambient animation speed |
| `flowAmplitude` | `15` | Ambient drift range in px |
| `rippleSpeed` | `600` | How fast ripple ring expands (px/sec equivalent) |
| `rippleStrength` | `80` | Ripple displacement force |
| `rippleDuration` | `1500` | How long each ripple lives (ms) |

**Subtle preset (production-ready):**
```tsx
dotSize={2} dotSpacing={35} attractionRadius={180}
attractionStrength={0.3} springStrength={0.05} damping={0.85}
```

**Dramatic preset (demo/hero):**
```tsx
dotSize={2} dotSpacing={15} attractionRadius={1000}
attractionStrength={300} springStrength={0.003} damping={0.96}
```

---

## CSS Setup (`globals.css`)

Uses Tailwind v4 with `@import 'tailwindcss'` (no config file):

```css
@import 'tailwindcss';
@import 'tw-animate-css';

@custom-variant dark (&:is(.dark *));

/* paste full :root and .dark blocks from design system above */

@theme inline {
  --font-sans: 'Geist', 'Geist Fallback';
  --font-mono: 'Geist Mono', 'Geist Mono Fallback';
  --font-serif: 'Source Serif 4', 'Source Serif 4 Fallback';
  /* map all color, radius, shadow tokens */
}

@layer base {
  * { @apply border-border outline-ring/50; }
  body { @apply bg-background text-foreground; }
}
```

---

## Tailwind v4 Dependencies

```json
{
  "devDependencies": {
    "@tailwindcss/postcss": "^4.1.9",
    "tailwindcss": "^4.1.9",
    "tw-animate-css": "1.3.3"
  }
}
```

`postcss.config.mjs`:
```js
export default { plugins: { '@tailwindcss/postcss': {} } }
```

---

## Theme Toggle (manual, no next-themes)

This project uses a hand-rolled toggle, not `next-themes` in the layout. It directly adds/removes the `.dark` class on `<html>`:

```tsx
"use client"
import { Moon, Sun } from "lucide-react"
import { useEffect, useState } from "react"

export function ThemeToggle() {
  const [theme, setTheme] = useState<"light" | "dark">("light")
  useEffect(() => {
    setTheme(document.documentElement.classList.contains("dark") ? "dark" : "light")
  }, [])
  const toggle = () => {
    const next = theme === "light" ? "dark" : "light"
    setTheme(next)
    document.documentElement.classList.toggle("dark", next === "dark")
  }
  return (
    <button
      onClick={toggle}
      className="inline-flex items-center gap-2 rounded-lg border border-border bg-background px-4 py-2 text-sm font-mono transition-colors hover:bg-accent hover:text-accent-foreground"
    >
      {theme === "light" ? <><Moon className="size-4" /><span>Dark Mode</span></> : <><Sun className="size-4" /><span>Light Mode</span></>}
    </button>
  )
}
```

---

## Integration Checklist

1. Add fonts to `layout.tsx` via `next/font/google`: Geist, Geist_Mono, Source_Serif_4
2. Copy `globals.css` token system exactly — `oklch` values, shadow system, `@theme inline` block
3. Drop `magnetic-dots.tsx` into `components/`
4. Wrap page: `<main className="relative min-h-screen bg-background">` + `<MagneticDots .../>` + `<div className="relative z-10 ...">`
5. Choose subtle vs dramatic prop preset based on context
6. Use `font-mono` for all display text — that's the aesthetic voice

---

## Aesthetic Rules

- Canvas background is the art. Keep content minimal above it.
- All color is achromatic. No hue. Tension comes from movement and contrast.
- `font-mono font-light` for headlines. Not bold. Not serif.
- Dark mode is the primary experience. Light is optional.
- Spacing is generous — the breathing room is intentional.
- No decorative borders, shadows, or gradients. The motion surface provides all visual richness.
