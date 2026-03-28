---
name: scroll-framer-motion
description: "Framer Motion / Motion scroll animation skill for React projects. Covers useScroll, useTransform, useSpring, whileInView, parallax, horizontal scroll, sticky sections, text reveals, and staggered animations — all without GSAP. React-idiomatic scroll experiences using Motion + CSS sticky + Lenis. Use when: Framer Motion scroll, Motion scroll, React scroll animation, useScroll, whileInView, React parallax, scroll animation without GSAP. For GSAP-based scroll with ScrollTrigger/pinning/image sequences, use scroll-experience skill instead."
---

# Scroll Motion Architect (React + Framer Motion)

You build scroll-driven experiences using **Motion (Framer Motion)** — the React-native approach. No GSAP dependency. You leverage React's component model, hooks, and CSS sticky positioning to create scroll animations that feel natural and ship fast.

**Your standard:** Smooth, purposeful scroll interactions. Every animation serves the content. Ship quality over complexity.

**When this skill applies vs `scroll-experience`:**

| Use this skill (scroll-motion) | Use scroll-experience (GSAP) |
|---|---|
| React-only project, want simplicity | Need pinning, image sequences, scrub smoothing |
| Team knows React well but not GSAP | Complex multi-phase scroll timelines |
| Simple-to-medium parallax + reveal animations | Need `ScrollTrigger.batch()` for 10+ elements |
| Prototyping / shipping fast | Award-winning cinematic scroll (Awwwards level) |
| Don't need snap behavior or frame scrubbing | Need snap points, horizontal scroll conversion |

**Bottom line:** Motion gets you 60% of scroll effects with 20% of the complexity. GSAP gets you 100% but requires more knowledge.

---

## Stack

| Layer | Tool | Why |
|---|---|---|
| Scroll animations | **Motion** (`motion/react`) | React-native, declarative, spring physics |
| Smooth scroll | **Lenis** (optional) | Buttery scroll feel, works with Motion |
| Sticky sections | **CSS `position: sticky`** | No JS needed, performant |
| Text splitting | **Manual word/char split** | No SplitText dependency needed |
| Snap | **CSS `scroll-snap-type`** | Native browser snap |

**Install:**
```bash
npm install motion lenis
```

---

## Core Hooks

### useScroll — Track Scroll Progress

Two modes: **page-level** and **element-level**.

```tsx
import { useScroll, useTransform, motion } from 'motion/react';

// Page-level: track overall scroll progress
function PageProgress() {
  const { scrollYProgress } = useScroll();
  return <motion.div style={{ scaleX: scrollYProgress }} className="fixed top-0 left-0 right-0 h-1 bg-blue-500 origin-left" />;
}

// Element-level: track element's position relative to viewport
function TrackedSection() {
  const ref = useRef(null);
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ['start end', 'end start']  // when element enters → when it leaves
  });
  // scrollYProgress: 0 = element entering bottom, 1 = element leaving top
}
```

**Offset syntax:** `['<target> <viewport>', '<target> <viewport>']`
- `start end` = element's top reaches viewport bottom
- `end start` = element's bottom reaches viewport top
- `start start` = element's top reaches viewport top
- `center center` = element centered in viewport

### useTransform — Map Scroll to Values

```tsx
const { scrollYProgress } = useScroll({ target: ref, offset: ['start end', 'end start'] });

// Linear mapping
const y = useTransform(scrollYProgress, [0, 1], ['0%', '-50%']);
const opacity = useTransform(scrollYProgress, [0, 0.3, 0.7, 1], [0, 1, 1, 0]);
const scale = useTransform(scrollYProgress, [0, 0.5], [0.8, 1]);

// Multi-point mapping (non-linear)
const rotate = useTransform(scrollYProgress, [0, 0.25, 0.5, 0.75, 1], [0, 90, 180, 270, 360]);

// Custom transform function
const custom = useTransform(scrollYProgress, (v) => Math.round(v * 100));
```

### useSpring — Smooth Out Jitter

Wraps any motion value with spring physics for smoother feel.

```tsx
const { scrollYProgress } = useScroll({ target: ref });
const y = useTransform(scrollYProgress, [0, 1], ['0%', '50%']);

// Add spring smoothing
const smoothY = useSpring(y, {
  stiffness: 100,   // higher = faster response
  damping: 30,       // higher = less oscillation
  restDelta: 0.001   // precision threshold
});

return <motion.div style={{ y: smoothY }} />;
```

**When to use useSpring:** Always on parallax layers and scroll-linked transforms. Prevents the "stuttery" feeling from discrete scroll events.

---

## Section Transition Patterns

### Pattern 1: Parallax Hero

```tsx
function ParallaxHero() {
  const ref = useRef(null);
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ['start start', 'end start']
  });

  const bgY = useTransform(scrollYProgress, [0, 1], ['0%', '50%']);
  const textY = useTransform(scrollYProgress, [0, 1], ['0%', '150%']);
  const opacity = useTransform(scrollYProgress, [0, 0.5], [1, 0]);

  const smoothBgY = useSpring(bgY, { stiffness: 100, damping: 30 });

  return (
    <section ref={ref} className="relative h-screen overflow-hidden">
      <motion.div style={{ y: smoothBgY }} className="absolute inset-0">
        <img src="/hero.jpg" alt="" className="w-full h-full object-cover" />
      </motion.div>
      <motion.div style={{ y: textY, opacity }} className="relative z-10 flex items-center justify-center h-full">
        <h1 className="text-6xl font-bold text-white">Welcome</h1>
      </motion.div>
    </section>
  );
}
```

### Pattern 2: Reveal on Scroll (whileInView)

The simplest scroll animation — no hooks needed.

```tsx
// Single element reveal
<motion.div
  initial={{ opacity: 0, y: 50 }}
  whileInView={{ opacity: 1, y: 0 }}
  viewport={{ once: true, margin: '-100px' }}
  transition={{ duration: 0.6, ease: 'easeOut' }}
>
  Content reveals on scroll
</motion.div>
```

**`viewport` options:**
- `once: true` — animate only first time (most common)
- `once: false` — re-animate every time element enters/exits
- `margin: '-100px'` — trigger 100px before element reaches viewport edge
- `amount: 0.5` — trigger when 50% of element is visible

### Pattern 3: Staggered List Reveal

```tsx
const container = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: { staggerChildren: 0.1, delayChildren: 0.2 }
  }
};

const item = {
  hidden: { opacity: 0, y: 20 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.4, ease: 'easeOut' } }
};

function StaggeredList({ items }) {
  return (
    <motion.ul
      variants={container}
      initial="hidden"
      whileInView="visible"
      viewport={{ once: true, margin: '-50px' }}
      className="space-y-4"
    >
      {items.map((item, i) => (
        <motion.li key={i} variants={item} className="p-6 bg-white rounded-lg shadow">
          {item}
        </motion.li>
      ))}
    </motion.ul>
  );
}
```

### Pattern 4: Horizontal Scroll Section

Uses CSS `position: sticky` + `useScroll` to convert vertical scroll into horizontal movement.

```tsx
function HorizontalScroll({ items }) {
  const containerRef = useRef(null);
  const { scrollYProgress } = useScroll({
    target: containerRef,
    offset: ['start start', 'end end']
  });

  const x = useTransform(
    scrollYProgress,
    [0, 1],
    ['0%', `-${(items.length - 1) * 100}%`]
  );

  return (
    <section ref={containerRef} style={{ height: `${items.length * 100}vh` }}>
      <div className="sticky top-0 h-screen overflow-hidden">
        <motion.div style={{ x }} className="flex h-full">
          {items.map((item, i) => (
            <div key={i} className="flex-shrink-0 w-screen h-full flex items-center justify-center p-16">
              {item}
            </div>
          ))}
        </motion.div>
      </div>
    </section>
  );
}
```

**Height formula:** `container height = items.length * 100vh`

### Pattern 5: Sticky Section with Fade Swap

```tsx
function StickySection({ title, content, image }) {
  const ref = useRef(null);
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ['start start', 'end start']
  });

  const opacity = useTransform(scrollYProgress, [0, 0.5, 1], [1, 1, 0]);
  const scale = useTransform(scrollYProgress, [0, 0.5, 1], [1, 1, 0.85]);

  return (
    <section ref={ref} className="relative h-[200vh]">
      <motion.div
        style={{ opacity, scale }}
        className="sticky top-0 h-screen flex items-center"
      >
        <div className="grid grid-cols-2 gap-16 container mx-auto px-8">
          <div>
            <h2 className="text-5xl font-bold">{title}</h2>
            <p className="mt-6 text-lg text-gray-600">{content}</p>
          </div>
          <img src={image} alt="" className="rounded-2xl shadow-xl" />
        </div>
      </motion.div>
    </section>
  );
}
```

### Pattern 6: Multi-Phase Sticky (Content Swap)

Multiple content phases within a single pinned viewport.

```tsx
function MultiPhaseSticky({ phases }) {
  const containerRef = useRef(null);
  const { scrollYProgress } = useScroll({
    target: containerRef,
    offset: ['start start', 'end end']
  });

  return (
    <section ref={containerRef} style={{ height: `${(phases.length + 1) * 100}vh` }}>
      <div className="sticky top-0 h-screen flex items-center justify-center overflow-hidden">
        {phases.map((phase, i) => {
          const start = i / phases.length;
          const peak = (i + 0.5) / phases.length;
          const end = (i + 1) / phases.length;

          const opacity = useTransform(scrollYProgress, [start, peak, end], [0, 1, 0]);
          const y = useTransform(scrollYProgress, [start, peak, end], [60, 0, -60]);

          return (
            <motion.div
              key={i}
              style={{ opacity, y }}
              className="absolute inset-0 flex items-center justify-center p-16"
            >
              {phase}
            </motion.div>
          );
        })}
      </div>
    </section>
  );
}
```

### Pattern 7: Text Reveal (Word-by-Word)

No SplitText library needed — split manually in React.

```tsx
function TextReveal({ text, className }) {
  const words = text.split(' ');
  return (
    <p className={className}>
      {words.map((word, i) => (
        <motion.span
          key={i}
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ delay: i * 0.04, duration: 0.3, ease: 'easeOut' }}
          className="inline-block mr-[0.25em]"
        >
          {word}
        </motion.span>
      ))}
    </p>
  );
}

// Character-level reveal
function CharReveal({ text, className }) {
  const chars = text.split('');
  return (
    <p className={className} aria-label={text}>
      {chars.map((char, i) => (
        <motion.span
          key={i}
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ delay: i * 0.02, duration: 0.3 }}
          className="inline-block"
          aria-hidden="true"
        >
          {char === ' ' ? '\u00A0' : char}
        </motion.span>
      ))}
    </p>
  );
}
```

### Pattern 8: Scroll-Linked Color Transition

```tsx
function ColorSection({ sections }) {
  const { scrollYProgress } = useScroll();

  const backgroundColor = useTransform(
    scrollYProgress,
    sections.map((_, i) => i / sections.length),
    sections.map(s => s.bgColor)
  );

  return (
    <motion.main style={{ backgroundColor }} className="transition-colors">
      {sections.map((section, i) => (
        <section key={i} className="min-h-screen flex items-center justify-center">
          {section.content}
        </section>
      ))}
    </motion.main>
  );
}
```

### Pattern 9: Card Stack (Parallax Cards)

```tsx
function CardStack({ cards }) {
  const containerRef = useRef(null);
  const { scrollYProgress } = useScroll({
    target: containerRef,
    offset: ['start start', 'end end']
  });

  return (
    <section ref={containerRef} style={{ height: `${cards.length * 100}vh` }}>
      <div className="sticky top-0 h-screen flex items-center justify-center">
        {cards.map((card, i) => {
          const progress = useTransform(
            scrollYProgress,
            [i / cards.length, (i + 1) / cards.length],
            [0, 1]
          );
          const scale = useTransform(progress, [0, 1], [1, 0.9]);
          const y = useTransform(progress, [0, 1], [0, -40]);

          return (
            <motion.div
              key={i}
              style={{ scale, y, zIndex: cards.length - i }}
              className="absolute w-[80vw] max-w-2xl bg-white rounded-2xl shadow-xl p-8"
            >
              {card}
            </motion.div>
          );
        })}
      </div>
    </section>
  );
}
```

---

## Lenis Integration (Optional Smooth Scroll)

Lenis adds buttery smooth scroll feel. Works with Motion without any special setup.

```tsx
// app/providers/SmoothScroll.tsx
'use client';
import { useEffect } from 'react';
import Lenis from 'lenis';

export function SmoothScrollProvider({ children }: { children: React.ReactNode }) {
  useEffect(() => {
    const lenis = new Lenis({
      duration: 1.2,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      smoothWheel: true,
    });

    function raf(time: number) {
      lenis.raf(time);
      requestAnimationFrame(raf);
    }
    requestAnimationFrame(raf);

    return () => lenis.destroy();
  }, []);

  return <>{children}</>;
}

// app/layout.tsx
import { SmoothScrollProvider } from './providers/SmoothScroll';

export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        <SmoothScrollProvider>{children}</SmoothScrollProvider>
      </body>
    </html>
  );
}
```

**Disable on specific elements:**
```html
<div data-lenis-prevent>This scrolls natively (e.g., modals, dropdowns)</div>
```

---

## CSS Scroll Snap (Native Snap Without JS)

When you need snap-to-section behavior without GSAP:

```css
/* Parent scroller */
.snap-container {
  scroll-snap-type: y mandatory;  /* or 'proximity' for softer snap */
  overflow-y: scroll;
  height: 100vh;
}

/* Each section */
.snap-section {
  scroll-snap-align: start;
  height: 100vh;
}
```

```tsx
function SnapSections({ sections }) {
  return (
    <div className="snap-y snap-mandatory overflow-y-scroll h-screen">
      {sections.map((section, i) => (
        <motion.section
          key={i}
          className="snap-start h-screen flex items-center justify-center"
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true }}
        >
          {section}
        </motion.section>
      ))}
    </div>
  );
}
```

---

## Performance Rules

1. **Only animate `transform` and `opacity`** — Motion does this by default with `x`, `y`, `scale`, `rotate`, `opacity`
2. **Use `useSpring`** on scroll-linked values to prevent jitter
3. **`viewport={{ once: true }}`** — for reveal animations, don't re-trigger
4. **Avoid mounting hundreds of `motion.div`** — for large lists, use CSS animations or virtualization
5. **`will-change: transform`** — Motion adds this automatically for animated elements
6. **Lazy mount heavy sections** — don't render below-fold content until near viewport

---

## Accessibility

```tsx
// Respect prefers-reduced-motion
import { useReducedMotion } from 'motion/react';

function AnimatedSection({ children }) {
  const prefersReduced = useReducedMotion();

  return (
    <motion.div
      initial={prefersReduced ? false : { opacity: 0, y: 50 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true }}
    >
      {children}
    </motion.div>
  );
}
```

- Always add `aria-label` to text elements **before** splitting into spans
- `aria-hidden="true"` on individual character/word spans
- Content must be readable without animations (progressive enhancement)
- Keyboard navigation must not be blocked by sticky sections

---

## Responsive Design

```tsx
// Use CSS breakpoints for layout, Motion for animation
// Motion animations work the same across breakpoints

// For different animation behavior per breakpoint, use a hook:
function useIsMobile() {
  const [isMobile, setIsMobile] = useState(false);
  useEffect(() => {
    const mq = window.matchMedia('(max-width: 768px)');
    setIsMobile(mq.matches);
    const handler = (e: MediaQueryListEvent) => setIsMobile(e.matches);
    mq.addEventListener('change', handler);
    return () => mq.removeEventListener('change', handler);
  }, []);
  return isMobile;
}

function ResponsiveParallax() {
  const isMobile = useIsMobile();
  const ref = useRef(null);
  const { scrollYProgress } = useScroll({ target: ref });

  // Reduce parallax intensity on mobile
  const y = useTransform(scrollYProgress, [0, 1], isMobile ? ['0%', '10%'] : ['0%', '50%']);

  return <motion.div ref={ref} style={{ y }} />;
}
```

**Mobile rules:**
- Reduce parallax intensity (10-20% vs 50% on desktop)
- Skip horizontal scroll sections on mobile — use vertical stacking instead
- Fewer stagger children (max 5-6 visible at once)
- Shorter transition durations (0.3s instead of 0.6s)

---

## Limitations (vs GSAP scroll-experience)

Things you **cannot** do with Motion alone:

- **No pinning** — use CSS `position: sticky` (works fine, just manual)
- **No snap with scrub** — CSS `scroll-snap-type` is the fallback
- **No batch** — no equivalent to `ScrollTrigger.batch()` for coordinating many elements entering at once
- **No scrub smoothing** — `useSpring` helps but isn't as tunable as GSAP `scrub: 1`
- **No image sequences** — no canvas frame scrubbing helper (use GSAP for Apple-style frame scrub)
- **No SplitText** — character-level text animations require manual splitting (shown above)
- **No timeline orchestration** — multi-step sequences need manual progress mapping

**If you hit these limits:** switch to the `scroll-experience` skill (GSAP ScrollTrigger).

---

## References

- [Motion scroll animations docs](https://motion.dev/docs/react-scroll-animations)
- [useScroll hook docs](https://motion.dev/docs/react-use-scroll)
- [useTransform docs](https://motion.dev/docs/react-use-transform)
- [whileInView docs](https://motion.dev/docs/react-animation#whileinview)
- [Lenis smooth scroll](https://github.com/darkroomengineering/lenis)
- [Cards Parallax with Framer Motion — Olivier Larose](https://blog.olivierlarose.com/tutorials/cards-parallax)
