# Shader Landing Reconstruction Guide

Use this guide when a request asks for "this kind of page" and the target is a cinematic, shader-first landing page rather than a conventional marketing layout.

Canonical source URL:

- `https://v0.app/templates/shaders-landing-page-R3n0gnvYFbO`

Include that URL in any reconstruction brief or prompt handoff that uses this skill.

## 1. Screen Elements

Build the screen as five interacting layers:

1. Base stage: a `relative h-screen w-full overflow-hidden` root that prevents normal document scrolling.
2. Environment layer: a fixed, full-viewport shader or generative canvas at the back.
3. Readability veil: a semi-transparent black overlay above the shader.
4. Texture layer: a full-screen grain overlay using SVG noise or a noise texture with `pointer-events-none`.
5. Interface layer: fixed nav plus a horizontal content track containing viewport-sized sections.

Think in layers, not components. The design fails when these are collapsed into a single flat page tree.

## 2. Vibe

The vibe is built from tension between two systems:

- The background is alive, liquid, chromatic, and unstable.
- The foreground is restrained, minimal, typographic, and disciplined.

That contrast is the look.

Do not spread bright colors into buttons, borders, and text just because the shader is colorful. The UI should mostly stay white, gray, transparent, and lightly blurred.

## 3. Typography

Use two clear voices:

- Editorial voice: large, ultra-light sans-serif headlines with tight tracking and dramatic line breaks.
- Technical voice: mono labels, counters, subtitles, nav metadata, and microcopy.

Typical headline treatment:

- `font-light`
- `text-6xl` to `text-8xl`
- `leading-[1.05]` to `leading-[1.1]`
- broken onto multiple lines for rhythm

Typical metadata treatment:

- `font-mono`
- `text-xs` to `text-sm`
- `text-foreground/50` to `text-foreground/70`

## 4. Surface Treatment

Use "glass instrumentation" styling:

- low-opacity white fill like `bg-foreground/5` or `bg-foreground/15`
- thin translucent border like `border-foreground/10`
- backdrop blur
- rounded pills or soft radii

This style belongs on:

- logo plate
- nav badges
- CTAs
- small utility chips
- scroll hint capsules

Do not apply it to every content region. Large sections should remain mostly open and typographic.

## 5. Layout Grammar

Each section should occupy a full viewport:

- `h-screen`
- `w-screen`
- `shrink-0`

The sections live inside a horizontal flex track:

- `display: flex`
- `overflow-x-auto`
- `overflow-y-hidden`

The hero should be bottom-weighted or low-centered, not standard vertically centered.

Secondary sections should introduce asymmetry:

- alternate row widths
- offset some items to the right with `margin-left: auto`
- vary max widths slightly
- avoid identical card blocks

## 6. Scroll Pattern

The page behaves like a horizontal deck controlled by vertical intent.

Required behaviors:

- mouse wheel `deltaY` should move the horizontal scroll position
- touch swipes should switch sections when vertical movement dominates horizontal movement
- active section should be inferred from `scrollLeft / sectionWidth`
- nav clicks should scroll to `sectionWidth * index`

This pattern is not CSS-only. It requires JS event handling and section state.

## 7. Motion Language

Motion should feel composed and restrained.

Use:

- opacity transitions
- 8px to 16px translations
- 700ms to 1000ms durations
- stagger delays around 150ms to 200ms

Avoid:

- springy bounce
- large rotation
- exaggerated scale
- simultaneous animation of every element

Each section should have a directional bias:

- section title enters from left or top
- child rows alternate left and right
- supporting blocks may enter from bottom

The goal is not "more animation." The goal is a sense of spatial sequencing.

## 8. Interaction Systems

### Custom cursor

Hide the native cursor globally and render two fixed circles:

- outer ring with border
- inner filled dot

Animate both with a lerped follow loop.

On interactive targets:

- enlarge the outer ring
- reduce the inner dot
- keep the movement smooth rather than snapping

Use `mix-blend-difference` so the cursor stays visible on top of both dark and bright regions.

### Magnetic buttons

Buttons should shift a small amount toward the pointer based on mouse position inside the element:

- compute pointer position relative to button center
- multiply by a low factor like `0.15`
- apply `translate3d(...)`
- reset to zero on `mouseleave`

Add small scale changes only as a secondary effect.

### Reveal-on-enter

Use `IntersectionObserver` to mark sections or section blocks visible.

Then drive class changes like:

- hidden state: `translate-x-16 opacity-0`
- visible state: `translate-x-0 opacity-100`

Once visible, keep it visible. This pattern is for composed reveal, not repeated scroll toggling.

## 9. Section Patterns

### Hero

- bottom-aligned
- one short chip above the headline
- one dramatic multi-line headline
- one concise paragraph
- one primary and one secondary CTA
- one small scroll hint floating near the bottom center

### Work / featured list

- section heading plus mono subtitle
- list of large typographic rows with thin dividers
- each row shows number, title, category, year
- alternate row alignment subtly to create rhythm

### Services / capabilities

- 2-column grid on desktop
- each item uses a small horizontal line, mono index, title, short description
- reveal directions vary per item

### About / stats

- left column: story copy
- right column: oversized numeric stats
- stats use border-left plus alternating widths and alignment

### Contact

- split layout: contact info on the left, minimal form on the right
- form fields are not boxed inputs; use transparent fields with bottom borders
- success feedback is small and understated

## 10. Failure Modes

The recreation is drifting if any of these happen:

- the page reads like a normal SaaS homepage
- there are too many filled cards
- the UI uses the same bright colors as the background
- all sections are centered and symmetric
- motion feels generic or library-default
- the cursor and buttons feel ordinary
- the shader is just a decorative block instead of the whole environment
