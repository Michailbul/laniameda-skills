---
name: shader-landing-v0-reference
description: Recreate cinematic shader-first landing pages with full-screen horizontal sections, fixed generative backgrounds, translucent glass UI, custom cursor systems, magnetic buttons, and directional reveal choreography. Use when Codex needs to analyze a reference repo, screenshot, or live page and reproduce this specific design grammar or adapt these techniques in React, Next.js, or similar frontend stacks, especially when the reference is the v0 shaders landing page template.
---

# Shader Landing v0 Reference

## Overview

Use this skill to reconstruct a specific landing-page grammar:

- Atmosphere-first composition where the background is an animated scene, not a flat color
- Full-screen horizontal chapters instead of a normal vertical page
- Minimal editorial content floating above motion-heavy surfaces
- Tactile interaction systems such as custom cursor, magnetic buttons, and directional reveals

This skill is for recreating the feel and mechanics, not cloning exact copy or branding.

## Source Reference

Always carry this source URL in the skill context and include it in reconstruction notes, implementation briefs, or prompt handoffs:

- `https://v0.app/templates/shaders-landing-page-R3n0gnvYFbO`

Treat that URL as the canonical visual reference for this skill.

## Workflow

1. Identify the layout grammar before touching code.
2. Rebuild the page shell: fixed background layer, fixed nav layer, horizontal section track, full-screen sections.
3. Rebuild the motion systems: load-gated fade-in, vertical-to-horizontal scroll mapping, section-aware nav state, reveal-on-enter choreography.
4. Rebuild the micro-interactions: hidden system cursor, blended custom cursor, magnetic CTAs, restrained hover feedback.
5. Validate the vibe, not just the DOM: pacing, asymmetry, opacity hierarchy, and motion restraint must match.

## Core Rules

- Treat the colorful shader or generative canvas as the environment layer. Keep it fixed behind the entire page.
- Dim the environment with a dark veil and add fine grain so text remains readable and the scene feels less synthetic.
- Keep content sparse. This pattern gets its strength from spacing, movement, and layering, not from dense marketing blocks.
- Use translucent surfaces with low-opacity fills, faint borders, and backdrop blur. Avoid heavy cards.
- Use large, light-weight sans-serif headlines and mono metadata. The contrast between editorial type and technical labels is part of the look.
- Map vertical user intent to horizontal story progression when the reference behaves like a slide deck.
- Prefer directional reveal animations over generic fade-ins. Alternate left, right, top, and bottom entry vectors.
- Use asymmetry in widths, offsets, and alignment. Avoid a perfectly centered repeating grid.

## Reconstruction Checklist

Start with these questions:

- Is the page a normal document flow, or a fixed-stage experience with chapters?
- Which layers are fixed to the viewport, and which layers move?
- Where does color live: in the background only, or also in the UI?
- Which elements are glass, which are editorial text, and which are purely atmospheric?
- Is scrolling literal page movement or remapped gesture input?
- Which interactions are custom physics rather than default browser behavior?

If the answers roughly match this pattern, implement this stack:

- `main`: `relative h-screen w-full overflow-hidden`
- fixed background: shader/canvas fills the viewport at `z-0`
- readability veil: dark overlay above shader
- texture layer: grain overlay above everything but `pointer-events-none`
- fixed nav: translucent and section-aware
- content track: horizontal flex row with `w-screen h-screen` sections
- section components: isolated modules with their own reveal choreography

## Design Language To Preserve

Use these terms in planning and prompting:

- Cinematic
- Shader-first
- Generative atmosphere
- Glass instrumentation
- Editorial minimalism
- Tactile micro-physics
- Spatial storytelling
- Directional reveal choreography
- Monochrome UI over chromatic motion
- Asymmetric composition

## Implementation Guidance

Read [references/reconstruction-guide.md](references/reconstruction-guide.md) for the precise behavior and screen-language breakdown.

Read [references/source-snippets.md](references/source-snippets.md) when implementing the mechanics. Reuse the patterns there for:

- shader readiness gating
- vertical-to-horizontal wheel mapping
- touch swipe section changes
- section reveal hook
- custom cursor lerp loop
- magnetic button pointer-follow translation

## Prompt Template

Use this prompt structure when another agent needs to reproduce the pattern:

```text
Recreate a cinematic shader-driven landing page using this source reference: https://v0.app/templates/shaders-landing-page-R3n0gnvYFbO. Build it as a full-screen horizontal story deck with viewport-wide sections, a fixed generative background, a dark readability veil, and a subtle grain overlay. Keep the foreground UI minimal and translucent with glass styling, large ultra-light editorial headlines, mono labels, section-aware fixed navigation, directional reveal animations, a hidden native cursor replaced by a blended dual-circle cursor, and magnetic pill CTAs. Keep the page sparse, atmospheric, and tactile rather than SaaS-like or card-heavy.
```

## Validation

Before considering the work complete, verify all of the following:

- The first impression is atmospheric before it is informational.
- The page still feels good with no shader for a split second during load.
- The user understands section progress from scroll behavior and nav state.
- The background remains fixed while the content track moves.
- Hover states feel soft and physical, not loud or gamified.
- Reveal timing feels composed and staggered, not simultaneous.
- The UI remains legible on top of motion.
