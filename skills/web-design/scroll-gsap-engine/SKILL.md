---
name: scroll-gsap-engine
description: "GSAP ScrollTrigger master skill for building award-winning scroll-driven websites. Covers GSAP ScrollTrigger, Lenis smooth scroll, CSS scroll-driven animations, pinned sections, horizontal scroll, parallax, image sequences, text split reveals, and section transitions. Enforces performance rules, accessibility, and mobile-first architecture. Use when: GSAP, ScrollTrigger, Lenis, pinned scroll, scroll hijack, image sequence, SplitText, cinematic website, Apple-style scroll, dreamy scroll, scroll animation with GSAP. For React-only scroll with Framer Motion, use scroll-motion skill instead."
---

# Scroll Experience Architect

You build scroll-driven websites that feel like cinematic experiences — not just pages with animations bolted on. You treat scrolling as a narrative device. Every transition has purpose. Every animation serves the story.

**Your standard:** Awwwards Site of the Year quality. If it doesn't feel like a controlled movie, it's not done.

---

## Stack Decision Matrix

Choose tools based on the complexity of the scroll experience:

| Complexity | Smooth Scroll | Scroll Engine | 3D | Text Effects |
|---|---|---|---|---|
| **Simple** (reveals, progress bars) | CSS `scroll-behavior: smooth` | CSS `animation-timeline: view()` | None | CSS transitions |
| **Medium** (parallax, sticky sections) | Lenis | GSAP ScrollTrigger | None | GSAP SplitText |
| **Complex** (pinned timelines, horizontal scroll, image sequences) | Lenis | GSAP ScrollTrigger + timeline | Optional Three.js | GSAP SplitText |
| **Cinematic** (3D camera, shader effects, frame scrubbing) | Lenis | GSAP ScrollTrigger | Three.js / Theatre.js | GSAP SplitText |

**Default stack for most projects:** Lenis + GSAP ScrollTrigger + SplitText. This covers 90% of scroll experiences.

**React-only alternative:** Use the `scroll-motion` skill for Framer Motion / Motion-based scroll experiences.

---

## Architecture: How to Structure the Page

### HTML Pattern for Scroll Sections

Every scroll section follows this pattern: **tall outer wrapper** (provides scroll distance) + **sticky inner viewport** (provides the visual frame).

```html
<!-- Section height = 100vh * (phases + 1) -->
<section class="scroll-section" style="height: 400vh;">
  <div class="viewport" style="position: sticky; top: 0; height: 100vh; overflow: hidden;">
    <!-- All animated content lives inside the viewport -->
    <div class="phase phase-1">...</div>
    <div class="phase phase-2">...</div>
    <div class="phase phase-3">...</div>
  </div>
</section>
```

**Height calculation rule:** `section height = 100vh * (number_of_content_phases + 1)`

- 3 phases that each transition over 1 viewport = `400vh`
- 5 phases = `600vh`
- The "+1" accounts for the first phase being visible on entry

### Lenis + GSAP + Next.js Setup (Canonical)

```tsx
// app/providers/SmoothScroll.tsx
'use client';
import { useEffect, useRef } from 'react';
import Lenis from 'lenis';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

export function SmoothScrollProvider({ children }: { children: React.ReactNode }) {
  const lenisRef = useRef<Lenis | null>(null);

  useEffect(() => {
    const lenis = new Lenis({ autoRaf: false });
    lenisRef.current = lenis;

    lenis.on('scroll', ScrollTrigger.update);
    gsap.ticker.add((time) => lenis.raf(time * 1000));
    gsap.ticker.lagSmoothing(0);

    return () => {
      lenis.destroy();
      ScrollTrigger.getAll().forEach(t => t.kill());
    };
  }, []);

  return <>{children}</>;
}
```

### GSAP in React — useGSAP Hook (Preferred)

Use `useGSAP()` from `@gsap/react` instead of raw `useEffect`/`useLayoutEffect`. It handles cleanup automatically and scopes selectors to the container.

```tsx
import { useGSAP } from '@gsap/react';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(useGSAP, ScrollTrigger);

function ScrollSection() {
  const containerRef = useRef<HTMLDivElement>(null);

  useGSAP(() => {
    // Selectors like '.element' are automatically scoped to containerRef
    gsap.to('.element', {
      scrollTrigger: { trigger: '.section', scrub: 1 },
      y: -100
    });
  }, { scope: containerRef }); // scope = auto-cleanup + scoped selectors

  // For event handlers created outside the hook, use contextSafe:
  const { contextSafe } = useGSAP({ scope: containerRef });
  const handleClick = contextSafe(() => {
    gsap.to('.element', { rotation: 360 });
  });

  return <div ref={containerRef}>...</div>;
}
```

**Fallback (no @gsap/react):** Use `gsap.context()` manually:

```tsx
useLayoutEffect(() => {
  const ctx = gsap.context(() => {
    // All GSAP/ScrollTrigger code here
  }, containerRef);
  return () => ctx.revert();
}, []);
```

**SSR rule:** Never run GSAP during server-side rendering. The `useGSAP` hook handles this automatically.

---

## GSAP ScrollTrigger Rules (Non-Negotiable)

These are the rules that separate working code from broken scroll experiences:

### 1. Register once, at the top level
```javascript
gsap.registerPlugin(ScrollTrigger);
// Do this ONCE. Not in components. Not in effects.
```

### 2. ScrollTrigger goes on the TIMELINE, not child tweens
```javascript
// CORRECT
const tl = gsap.timeline({
  scrollTrigger: {
    trigger: '.section',
    start: 'top top',
    end: 'bottom bottom',
    scrub: 1,
    pin: true
  }
});
tl.to('.box1', { x: 200 })
  .to('.box2', { scale: 1.5 }, '<');  // simultaneous with previous

// WRONG — never put scrollTrigger on a child tween inside a timeline
tl.to('.box', { x: 100, scrollTrigger: {...} }); // BREAKS
```

### 3. Never combine scrub + toggleActions
They are **mutually exclusive** approaches. Pick one:
- `scrub` = animation progress tied to scroll position (cinematic)
- `toggleActions` = animation plays/reverses at trigger points (event-based)

### 4. When pinning, animate CHILDREN — never the pinned element itself
```javascript
// CORRECT — pin the section, animate its children
gsap.timeline({
  scrollTrigger: { trigger: '.section', pin: true, scrub: 1 }
})
.to('.section .child', { x: 200 });

// WRONG — animating the pinned element
gsap.to('.section', {
  x: 200,
  scrollTrigger: { trigger: '.section', pin: true } // BREAKS
});
```

### 5. Create ScrollTriggers in top-to-bottom page order
Or use `refreshPriority` to override. Call `ScrollTrigger.refresh()` after:
- DOM changes (dynamic content loaded)
- Font loads completing
- Layout shifts
- Route changes in SPAs

### 6. Use ScrollTrigger.batch() for 10+ elements
Individual triggers for each card/item = performance disaster:
```javascript
// CORRECT — batch for many elements
ScrollTrigger.batch('.card', {
  onEnter: (elements) => {
    gsap.to(elements, {
      opacity: 1, y: 0, duration: 0.6,
      stagger: 0.15, ease: 'power2.out'
    });
  },
  start: 'top 90%',
  once: true
});

// WRONG — individual triggers for 50 cards
document.querySelectorAll('.card').forEach(card => {
  gsap.to(card, { scrollTrigger: { trigger: card } }); // 50 ScrollTriggers!
});
```

### 7. Kill on unmount (SPAs)
```javascript
// In cleanup
ScrollTrigger.getAll().forEach(t => t.kill());
// Or better: use useGSAP() / gsap.context() which handles this automatically
```

### 8. Use autoAlpha instead of opacity
```javascript
// BETTER — autoAlpha sets visibility:hidden when opacity reaches 0
// This removes the element from accessibility tree and click targets
gsap.from('.element', { autoAlpha: 0, duration: 0.6 });

// Instead of just opacity which leaves an invisible but interactive element
gsap.from('.element', { opacity: 0, duration: 0.6 }); // still clickable at 0!
```

### 9. Never leave markers in production
```javascript
scrollTrigger: {
  markers: true  // DEBUG ONLY — remove before shipping
}
```

---

## Section Transition Patterns

### Pattern 1: Pinned Section with Phase Transitions

The most common award-winning pattern. Section stays fixed, content phases in/out.

```javascript
const tl = gsap.timeline({
  scrollTrigger: {
    trigger: '.pinned-section',
    start: 'top top',
    end: 'bottom bottom',
    scrub: 1,
    pin: false  // using CSS sticky instead for simpler DOM
  }
});

tl.to('.phase-1', { opacity: 0, y: -50, duration: 1 })
  .from('.phase-2', { opacity: 0, y: 50, duration: 1 })
  .to('.phase-2', { opacity: 0, y: -50, duration: 1 })
  .from('.phase-3', { opacity: 0, y: 50, duration: 1 });
```

**When to use:** Product feature walkthroughs, storytelling sections, before/after reveals.

### Pattern 2: Horizontal Scroll Gallery

Vertical scrolling converts to horizontal panel movement.

```javascript
const panels = gsap.utils.toArray('.panel');

gsap.to(panels, {
  xPercent: -100 * (panels.length - 1),
  ease: 'none',
  scrollTrigger: {
    trigger: '.horizontal-container',
    pin: true,
    scrub: 1,
    snap: 1 / (panels.length - 1),
    end: () => '+=' + document.querySelector('.horizontal-container').offsetWidth
  }
});
```

**When to use:** Image galleries, portfolio showcases, step-by-step processes.
**Mobile consideration:** Add swipe affordance. Consider disabling horizontal scroll on mobile and stacking vertically instead.

### Pattern 3: Parallax Depth Layers

Multiple layers moving at different speeds create depth.

```javascript
document.querySelectorAll('.parallax-layer').forEach((layer) => {
  const speed = parseFloat(layer.dataset.speed) || 0.5;
  gsap.to(layer, {
    y: () => window.innerHeight * speed,
    ease: 'none',
    scrollTrigger: {
      trigger: layer.closest('.parallax-section'),
      start: 'top bottom',
      end: 'bottom top',
      scrub: true
    }
  });
});
```

**Layer speed guide:**
| Layer | Speed | Effect |
|---|---|---|
| Far background | 0.1-0.2 | Almost static, deep |
| Mid background | 0.3-0.5 | Gentle movement |
| Foreground content | 1.0 | Normal scroll speed |
| Floating accents | 1.2-1.5 | Pops forward |

### Pattern 4: Apple-Style Image Sequence (Canvas Frame Scrubbing)

```javascript
function imageSequence({ urls, canvas, scrollTrigger }) {
  const ctx = canvas.getContext('2d');
  const playhead = { frame: 0 };
  const images = urls.map((url, i) => {
    const img = new Image();
    img.src = url;
    if (i === 0) img.onload = () => ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
    return img;
  });

  return gsap.to(playhead, {
    frame: images.length - 1,
    ease: 'none',
    snap: 'frame',
    onUpdate: () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.drawImage(images[Math.round(playhead.frame)], 0, 0, canvas.width, canvas.height);
    },
    scrollTrigger
  });
}

// Usage
const frameCount = 148;
const urls = Array.from({ length: frameCount }, (_, i) =>
  `/frames/frame_${String(i + 1).padStart(4, '0')}.webp`
);

imageSequence({
  urls,
  canvas: document.querySelector('#sequence-canvas'),
  scrollTrigger: {
    trigger: '#sequence-section',
    start: 'top top',
    end: '+=4000',
    scrub: true,
    pin: true
  }
});
```

**Performance rules for image sequences:**
- Use WebP format, never PNG
- Resize frames to display dimensions (not source resolution)
- Preload first 10 frames explicitly for instant first paint
- On mobile (<768px): substitute a short autoplay video or static image

### Pattern 5: Text Split Reveals (SplitText)

```javascript
gsap.registerPlugin(SplitText, ScrollTrigger);

// Character reveal with mask (cinematic look)
const split = SplitText.create('.headline', {
  type: 'chars',
  mask: 'chars',    // overflow:hidden wrappers for upward reveal
  autoSplit: true   // re-splits on resize
});

gsap.from(split.chars, {
  y: '100%',
  stagger: 0.03,
  duration: 0.5,
  ease: 'power2.out',
  scrollTrigger: {
    trigger: '.headline',
    start: 'top 80%'
  }
});

// Line-by-line body text reveal
const lineSplit = SplitText.create('.body-text', {
  type: 'lines',
  mask: 'lines',
  autoSplit: true
});

gsap.from(lineSplit.lines, {
  y: '100%',
  stagger: 0.08,
  duration: 0.6,
  scrollTrigger: {
    trigger: '.body-text',
    start: 'top 80%'
  }
});
```

**Accessibility rule:** Add `aria-label` to text elements BEFORE SplitText splits them. Screen readers need the original text.

### Pattern 6: Card Stack / Deck Transitions

```javascript
const cards = gsap.utils.toArray('.stack-card');

cards.forEach((card, i) => {
  ScrollTrigger.create({
    trigger: card,
    start: 'top 50%',
    end: 'top 10%',
    scrub: true,
    animation: gsap.to(card, {
      scale: 1 - (cards.length - i) * 0.05,
      y: -30 * (cards.length - i)
    })
  });
});
```

### Pattern 7: Scroll-Linked Color/Theme Transitions

```javascript
const sections = gsap.utils.toArray('.themed-section');

sections.forEach((section) => {
  const bg = section.dataset.bg;
  const text = section.dataset.text;

  ScrollTrigger.create({
    trigger: section,
    start: 'top center',
    end: 'bottom center',
    onEnter: () => gsap.to('body', { backgroundColor: bg, color: text, duration: 0.5 }),
    onEnterBack: () => gsap.to('body', { backgroundColor: bg, color: text, duration: 0.5 })
  });
});
```

### Pattern 8: Clip-Path Morphing Reveals

```javascript
gsap.from('.reveal-section', {
  clipPath: 'inset(100% 0 0 0)',  // hidden from bottom
  scrollTrigger: {
    trigger: '.reveal-section',
    start: 'top 80%',
    end: 'top 20%',
    scrub: 1
  }
});

// Circle reveal from center
gsap.from('.circle-reveal', {
  clipPath: 'circle(0% at 50% 50%)',
  scrollTrigger: {
    trigger: '.circle-reveal',
    start: 'top center',
    end: 'bottom center',
    scrub: true
  }
});
```

---

## CSS Scroll-Driven Animations (No JS)

For simple reveals and progress effects, native CSS is now viable and runs on the compositor thread (zero main thread cost).

### Reveal on Scroll (CSS Only)

```css
@keyframes reveal {
  from { opacity: 0; transform: translateY(50px); }
  to { opacity: 1; transform: translateY(0); }
}

.reveal-element {
  animation: reveal linear both;
  animation-timeline: view();
  animation-range: entry 0% cover 40%;
}
```

### Scroll Progress Bar (CSS Only)

```css
.progress-bar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 3px;
  background: var(--accent);
  transform-origin: left;
  animation: scaleX linear;
  animation-timeline: scroll();
}

@keyframes scaleX {
  from { transform: scaleX(0); }
  to { transform: scaleX(1); }
}
```

### Progressive Enhancement Wrapper

```css
/* Always wrap in @supports — Firefox still partial */
@supports (animation-timeline: view()) {
  .element {
    animation: fadeIn linear both;
    animation-timeline: view();
    animation-range: entry 25% cover 50%;
  }
}
```

### When CSS vs GSAP

| Use CSS | Use GSAP |
|---|---|
| Simple fade/slide reveals | Multi-step timeline sequences |
| Progress bars | Pinning sections |
| Single-property parallax | Horizontal scroll conversion |
| Performance-critical (compositor thread) | Snap behavior |
| Progressive enhancement OK | Cross-browser consistency required |
| No Firefox support needed | Image sequences on canvas |

---

## Responsive Scroll Design

### gsap.matchMedia() — Different Animations Per Breakpoint

```javascript
gsap.matchMedia().add(
  {
    isDesktop: '(min-width: 1024px)',
    isTablet: '(min-width: 768px) and (max-width: 1023px)',
    isMobile: '(max-width: 767px)'
  },
  (context) => {
    const { isDesktop, isMobile } = context.conditions;

    if (isDesktop) {
      // Full cinematic experience
      gsap.timeline({
        scrollTrigger: { trigger: '.section', pin: true, scrub: 1, end: '+=2000' }
      })
      .to('.content', { x: '-100vw' });
    }

    if (isMobile) {
      // Simplified — no pinning, shorter animations
      gsap.from('.content', {
        opacity: 0, y: 30,
        scrollTrigger: { trigger: '.content', start: 'top 80%' }
      });
    }

    // Cleanup is automatic when breakpoint changes
  }
);
```

### Mobile Rules

- **Disable pinning** when viewport < 768px — too much scroll for too little content
- **Reduce parallax layers** to max 2 on mobile (background + content)
- **Skip image sequences** under 768px — use static image or short autoplay video
- **Lower scrub values** on mobile: `scrub: 0.5` instead of `scrub: 1` (touch scroll is more sensitive)
- **Lenis touchMultiplier:** reduce to 1.5 from default 2 if scroll feels too fast
- **Test on real devices** — Chrome DevTools throttling is not the same as actual mobile

---

## Performance (The Hard Rules)

### Only Animate Transform and Opacity

| Property | Layout | Paint | Composite | Use? |
|---|---|---|---|---|
| `transform` (x, y, scale, rotate) | No | No | Yes | **ALWAYS** |
| `opacity` | No | No | Yes | **ALWAYS** |
| `filter` (blur, brightness) | No | Yes | No | Sparingly |
| `clipPath` | No | Yes | No | OK for reveals |
| `width`, `height`, `top`, `left` | Yes | Yes | No | **NEVER animate** |
| `margin`, `padding` | Yes | Yes | No | **NEVER animate** |
| `background-color` | No | Yes | No | OK for theme transitions |

### will-change

```css
/* Apply to elements ABOUT to animate — max 10-20 elements */
.will-animate {
  will-change: transform, opacity;
}

/* NEVER apply globally */
* { will-change: transform; }  /* GPU memory explosion */
```

### Avoid Layout Thrashing

```javascript
// BAD — read/write interleaving forces layout recalculation
elements.forEach(el => {
  const height = el.offsetHeight;  // READ (forces layout)
  el.style.transform = `translateY(${height}px)`;  // WRITE
});

// GOOD — batch reads, then batch writes
const heights = elements.map(el => el.offsetHeight);  // All reads
elements.forEach((el, i) => {
  el.style.transform = `translateY(${heights[i]}px)`;  // All writes
});
```

### Lazy-Load Heavy Sections

```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      initHeavyAnimation(entry.target);
      observer.unobserve(entry.target);
    }
  });
}, { rootMargin: '200px' });

document.querySelectorAll('.heavy-section').forEach(el => observer.observe(el));
```

---

## Accessibility (Non-Negotiable)

### Reduced Motion

```javascript
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (prefersReducedMotion) {
  // Show all content immediately, skip animations
  gsap.set('.animated', { clearProps: 'all' });
  // Do NOT initialize ScrollTrigger animations
} else {
  initScrollAnimations();
}
```

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

### Content Rules

- All content must be in the DOM on page load (not injected by scroll)
- Pinned sections must not trap keyboard focus
- `aria-label` on text elements BEFORE SplitText splits them
- Semantic HTML: `<section>`, `<article>`, heading hierarchy
- Tall spacer sections should contain real content, not empty divs
- Content must be readable and navigable without JS

---

## Anti-Patterns (What NOT to Do)

### Scroll Hijacking

**Never alter default scroll speed or direction globally.** Users hate losing scroll control.

Acceptable exceptions:
- Full-page snap sections (with clear visual affordance that more content exists)
- Horizontal scroll galleries (with visible scroll/swipe indicator)
- Image sequence scrubbing (users expect this on product pages)

**Never acceptable:**
- Slowing down scroll globally
- Changing scroll speed arbitrarily between sections
- Any scroll hijacking on mobile
- Scroll hijacking without a way to skip/escape

### Animation Overload

- Less is more. Animate **key moments**, not every element
- Static content is OK — guide attention, don't overwhelm
- Max 3-4 active animations visible at any time
- If the user notices the animation more than the content, you've gone too far

### Desktop-Only Experiences

- Mobile is 60%+ of traffic. Design mobile-first
- A beautiful desktop experience that breaks on mobile = failure
- Every scroll pattern must have a mobile strategy (simplified, stacked, or disabled)

### Forgetting Cleanup

- Every ScrollTrigger created must be killed on route change
- Use `gsap.context()` in React — it handles cleanup automatically
- Memory leaks from orphaned ScrollTriggers are the #1 cause of SPA scroll bugs

---

## Snap Points

```javascript
scrollTrigger: {
  scrub: 1,
  snap: {
    snapTo: 1 / (sections.length - 1),  // evenly spaced
    duration: { min: 0.2, max: 0.5 },
    delay: 0,
    ease: 'power1.inOut'
  }
}

// Or snap to specific positions
snap: [0, 0.25, 0.5, 0.75, 1]

// Or snap to labels
snap: 'labelsDirectional'
```

**When to snap:** Full-page sections, step-by-step walkthroughs, image sequence keyframes.
**When NOT to snap:** Long-form content, editorial pages, anything where users need free-scroll control.

---

## Trigger Positioning Reference

Format: `"triggerPosition viewportPosition"`

```
start: "top center"    → trigger's top hits viewport center
start: "top 80%"       → trigger's top hits 80% from viewport top
start: "center center"  → trigger's center hits viewport center
end: "bottom top"       → trigger's bottom hits viewport top
end: "+=2000"           → 2000px after the start position
```

Visual: the first value is **where on the trigger element**, the second is **where on the viewport**.

---

## Easing Reference

| Ease | Feel | Use For |
|---|---|---|
| `"none"` | Linear, mechanical | Scrub animations (scroll-linked) |
| `"power1.out"` | Gentle deceleration | Subtle reveals |
| `"power2.out"` | Medium deceleration | Standard entrance animations |
| `"power3.out"` | Strong deceleration | Dramatic entrances |
| `"back.out(1.7)"` | Overshoot + settle | Playful, bouncy reveals |
| `"elastic.out(1, 0.3)"` | Spring bounce | Attention-grabbing elements |
| `"expo.out"` | Sharp deceleration | Hero text reveals |

**Rule:** Scrub animations should almost always use `ease: "none"` — the scroll IS the easing.

---

## Delivery Checklist

Before declaring a scroll experience complete:

- [ ] **60fps on desktop** — no jank during any scroll animation (test in Chrome DevTools Performance tab)
- [ ] **Smooth on mobile** — tested on real iPhone and Android device, not just DevTools
- [ ] **Reduced motion respected** — all animations skip gracefully with `prefers-reduced-motion: reduce`
- [ ] **Content accessible without JS** — page is readable with JavaScript disabled
- [ ] **Keyboard navigable** — pinned sections don't trap focus, tab order is logical
- [ ] **ScrollTriggers cleaned up** — no orphaned triggers on route change (check with `ScrollTrigger.getAll()`)
- [ ] **Responsive breakpoints handled** — `gsap.matchMedia()` used for mobile/tablet/desktop differences
- [ ] **No layout property animations** — only `transform` and `opacity` used for scroll-linked movement
- [ ] **Lenis + GSAP synced** — if using Lenis, the canonical integration pattern is followed
- [ ] **Image sequences optimized** — WebP format, display-size frames, preloaded first frames
- [ ] **Semantic HTML** — sections use proper `<section>`, `<article>`, heading hierarchy
- [ ] **Scroll indicators** — horizontal scroll and snap sections have visible affordances

---

## Reference Sites to Study

| Site | Pattern | Why Study It |
|---|---|---|
| Apple product pages | Image sequence scrubbing, pinned reveals | The benchmark for scroll-driven product storytelling |
| Zentry (Awwwards SOTM) | Geometric transitions, video storytelling | Cinematic scroll done right |
| Stripe Sessions | Clean scroll animations + light design | Purposeful, not overdone |
| Frame.io | GSAP + React + Next.js long-scroll | Production-grade architecture |

**Directories:** [Awwwards Scrolling](https://www.awwwards.com/websites/scrolling/), [Godly Scrolling Animation](https://godly.website/websites/scrolling-animation), [Made With GSAP](https://madewithgsap.com/)

---

## Key Facts

- **GSAP is now free** — Webflow acquired GreenSock in 2024. All plugins including ScrollTrigger, SplitText, ScrollSmoother are free for commercial use.
- **Lenis replaced Locomotive Scroll** — Locomotive v5 essentially became Lenis. Use Lenis for new projects.
- **CSS scroll-driven animations** — Chrome/Edge/Safari stable, Firefox partial. Use with `@supports` fallback.
- **ScrollSmoother vs Lenis:** ScrollSmoother requires rigid wrapper DOM (`#smooth-wrapper > #smooth-content`), breaks with fixed positioning inside. Lenis works with native DOM. **Default to Lenis.**
