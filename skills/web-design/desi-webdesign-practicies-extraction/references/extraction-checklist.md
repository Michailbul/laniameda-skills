# Extraction Checklist

Use this checklist to inspect a reference and convert it into reusable practices.

## A. Source Capture

- Record the original reference URL first.
- Record the input type: repo, component, code block, screenshot, or live URL.
- Record whether the analysis is source-backed or inferred.
- If code exists, record the framework, runtime, styling system, and key files.

## B. Visual Grammar

Extract:

- base mood
- density level
- composition style
- viewport usage
- color ownership
- typography hierarchy
- surface language
- spacing rhythm
- section structure

Ask:

- Is the page document-like or stage-like?
- Is it symmetric or intentionally off-balance?
- Does color live in the UI or mainly in the atmosphere?
- Are there repeated modules, or is each section composed differently?

## C. On-Screen Elements

List all visible element types:

- nav
- hero
- CTA blocks
- lists
- cards
- stat rows
- form fields
- captions
- decorative layers
- cursor overlays
- scroll hints

Describe each in screen terms:

- fixed or scrolling
- filled or transparent
- sharp or blurred
- text-heavy or sparse
- inline or floating

## D. Motion And Interaction

Extract the motion system precisely:

- what animates on load
- what animates on scroll
- what animates on hover
- what animates on section entry
- what follows pointer movement
- what changes on touch

Ask:

- Is scroll direction remapped?
- Is motion mostly opacity and translation, or something more physical?
- Are reveals directional?
- Are sections independent scenes or one continuous scroll field?

## E. Frontend Implementation

If code exists, identify:

- refs and DOM measurement
- state that tracks section, loading, pointer, or scroll
- event listeners for wheel, touch, mousemove, resize, scroll
- `IntersectionObserver`
- animation loops with `requestAnimationFrame`
- math for translation, index detection, or gesture thresholds
- theme tokens and CSS variables
- fixed-position layering and z-index strategy

## F. Complex Patterns That Need Snippets

Include code when the behavior depends on exact implementation.

Typical cases:

- scroll remapping
- snap logic
- shader/canvas load gating
- custom cursor loops
- magnetic buttons
- custom hooks
- stagger orchestration
- layout calculations

## G. Transferable Practices

At the end, separate:

- universal design practices
- reference-specific techniques
- stack-specific implementation details

This keeps the output useful in a different codebase.
