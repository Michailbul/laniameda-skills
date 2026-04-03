# Visual Review Checklist

Run this on every PNG set before approving or giving feedback to Codex.

## Per-slide checks
For each of the 7 PNGs, verify:

### Layout
- [ ] No text clipping at edges (right side is the most common failure point)
- [ ] No overflow below the slide boundary
- [ ] Black border visible on all 4 sides
- [ ] Grid overlay present but subtle

### Hierarchy
- [ ] Kicker visible top-left on every slide
- [ ] One dominant headline per slide
- [ ] Supporting copy is smaller, secondary
- [ ] Visual element (metric/equation/list/grid) is distinct from body text

### Brand
- [ ] Active brand-system palette respected for this carousel context
- [ ] No purple-adjacent or blue-grey backgrounds if working in Laniameda brand mode
- [ ] Coral / accent used on ≤1 emphasis element per slide
- [ ] Light backgrounds use dark text in the prompt/content area
- [ ] Bottom-of-image labels/chrome remain light over image gradients

### Content
- [ ] Slide 1: cover — big headline, no body text walls
- [ ] Slides 2–6: one key idea each, not a list of everything
- [ ] Slide 7: CTA — has a clear keyword to comment
- [ ] No Lorem Ipsum or placeholder text anywhere
- [ ] Numbers/stats match the brief

## Common failures from Codex → feedback phrases
| Issue | Feedback to give Codex |
|-------|------------------------|
| Text clips right edge | "slide_N.headline: reduce font-size from 108px to 88px — clips at right edge" |
| Too many ideas on one slide | "slide_N: split into 2 slides — currently has 3 unrelated points" |
| Accent overused | "slide_N: accent color on 3 elements — keep to 1 maximum" |
| Placeholder text | "slide_N: remove placeholder text '[insert stat]' — use real content from brief" |
| No CTA keyword | "slide_7.closing: preserve the exact CTA offer from the brief — don't genericize it" |
| Metric card missing shadow | "slide_N.metric-card: missing box-shadow — add the intended depth treatment" |
| Grid not visible | "global: grid overlay too faint or missing — ensure ::before opacity ~0.07" |
| Comparison slide is half-width split | "slide_N: comparison outputs are cramped — give each compared output its own full-width slide" |
| Hero text unreadable over image | "slide_1: increase contrast with gradient + text-shadow, not an opaque container" |
