---
name: async-page-transitions
description: |
  GSAP-powered async page transitions with dual-container DOM pattern, clip-path reveals, scale-down crossfades, and SplitText enter animations. Use this skill whenever the user wants smooth page transitions, route-based animations, cinematic page reveals, SPA transitions without a framework, GSAP page animations, clip-path transition effects, or any "page transition" / "route transition" / "page reveal" / "crossfade between pages" request in a web project. Also trigger when user mentions "codrops transitions", "async transitions", or wants to add premium-feeling navigation animations to a site. Works with vanilla JS, React, Next.js, or any frontend stack — adapt the pattern to the framework.
---

# Async Page Transitions with GSAP

A premium page transition system inspired by [Aristide Benoist's Watson website](https://watson.la/) and the [Codrops tutorial by Valentin Mor](https://tympanus.net/codrops/2026/02/26/building-async-page-transitions-in-vanilla-javascript/).

The core innovation: **both the current and next page coexist in the DOM simultaneously**, enabling true crossfade/overlay transitions impossible with simple CSS transitions.

## When to use this

- Adding route transitions to an SPA
- Building a portfolio, agency site, or editorial site that needs cinematic navigation
- Any request for "smooth page transitions", "page reveals", "crossfade between routes"
- Upgrading a basic router with visual transitions
- Building marketing/landing pages with premium feel

## Architecture Overview

```
[Click link] → intercept → clone container → inject next page HTML
→ both pages coexist in DOM → run GSAP transition animation
→ remove old page → cleanup
```

### The Dual-Container Pattern

This is the key concept. Instead of unmounting one page and mounting another, you:

1. Keep the current page in the DOM
2. Clone the transition container (shallow — no children)
3. Inject the next page's HTML into the clone
4. Append the clone to the wrapper — **both pages now live in the DOM**
5. Animate: current page scales down/fades, next page reveals via clip-path
6. Remove the old container after animation completes
7. Clear GSAP inline styles on the new container

This enables effects that are impossible when only one page exists at a time — parallax crossfades, scale-down reveals, horizontal slides, etc.

## Required HTML Structure

```html
<body>
  <!-- Persistent elements (nav, header) — OUTSIDE the transition container -->
  <nav class="nav">...</nav>

  <!-- Transition wrapper — contains the swappable containers -->
  <div data-transition="wrapper">
    <div data-transition="container" data-namespace="home">
      <main id="page_content">
        <!-- Page content here -->
      </main>
    </div>
  </div>
</body>
```

Key rules:
- `data-transition="wrapper"` — the parent that holds page containers
- `data-transition="container"` — the swappable page unit (gets cloned/removed)
- `data-namespace` — identifies which page is active (used for transition routing)
- Persistent elements (nav, footer) live **outside** the wrapper
- `body` background should be dark (`#000`) — it shows through during scale-down transitions

### Critical CSS for containers

```css
[data-transition="container"] {
  transform: translateZ(0);
  backface-visibility: hidden;
  will-change: transform;
}

main {
  background-color: #ffffff;
  width: 100%;
}

body {
  background-color: #000000;
}
```

The GPU-acceleration properties (`translateZ(0)`, `backface-visibility: hidden`) prevent flicker during 3D transforms. The dark body background creates the cinematic "reveal" effect when the current page scales down.

## GSAP Setup

### Dependencies

```bash
npm install gsap
```

### Plugin Registration

```js
import gsap from "gsap";
import { CustomEase } from "gsap/CustomEase";
import { SplitText } from "gsap/SplitText";

gsap.registerPlugin(CustomEase, SplitText);
```

SplitText requires a GSAP Club membership. If unavailable, see the "Without SplitText" section in the reference file.

### Custom Eases (what makes it feel premium)

```js
const customEases = {
  pageTransition: CustomEase.create(
    "pageTransition",
    "M0,0 C0.38,0.05 0.48,0.58 0.65,0.82 0.82,1 1,1 1,1"
  ),
  pageTransition2: CustomEase.create(
    "pageTransition2",
    "M0,0 C0.178,0.031 0.279,0.802 0.345,0.856 0.421,0.918 0.374,1 1,1"
  ),
};
```

These SVG cubic bezier curves give the transitions a non-generic, premium feel. `pageTransition` is a smooth accelerate-decelerate. `pageTransition2` has more aggressive initial acceleration — better for horizontal slides.

If CustomEase is unavailable, use `"power3.inOut"` as a solid fallback.

## Transition Animations

### 1. Default: Clip-Path Reveal from Bottom

The signature transition. Current page scales down and fades while the next page reveals from bottom via clip-path.

```js
function defaultTransition(currentContainer, nextContainer) {
  // Position next container on top, fully clipped
  gsap.set(nextContainer, {
    clipPath: "inset(100% 0% 0% 0%)",   // fully hidden (clipped from bottom)
    opacity: 1,
    position: "fixed",
    top: 0,
    left: 0,
    width: "100%",
    height: "100vh",
    zIndex: 10,
  });

  const tl = gsap.timeline({ defaults: { lazy: false } });

  // Both animations run simultaneously (position 0)
  tl.to(currentContainer, {
    y: "-30vh",
    opacity: 0.4,
    scale: 0.8,
    duration: 0.7,
    force3D: true,
    ease: customEases.pageTransition,
  }, 0)
  .to(nextContainer, {
    clipPath: "inset(0% 0% 0% 0%)",      // fully revealed
    duration: 0.7,
    force3D: true,
    ease: customEases.pageTransition,
  }, 0);

  return tl;
}
```

How it works:
- `clipPath: "inset(100% 0% 0% 0%)"` clips the entire element from the bottom — invisible
- Animating to `"inset(0% 0% 0% 0%)"` reveals it bottom-to-top
- Current page simultaneously moves up (`y: -30vh`), shrinks (`scale: 0.8`), and fades (`opacity: 0.4`)
- The dark body background peeks through the gaps as the current page shrinks
- `position: fixed` + `zIndex: 10` ensures the next page layers on top

### 2. Alternative: Horizontal Slide

Current page slides left while next page enters from the right.

```js
function alternativeTransition(currentContainer, nextContainer) {
  gsap.set(nextContainer, {
    opacity: 1,
    position: "fixed",
    top: 0,
    left: 0,
    width: "100%",
    height: "100vh",
    x: "100%",          // offscreen right
    zIndex: 10,
  });

  const tl = gsap.timeline({ defaults: { lazy: false } });

  tl.to(currentContainer, {
    x: "-50%",
    scale: 0.8,
    opacity: 0.4,
    duration: 1.5,
    force3D: true,
    ease: customEases.pageTransition2,
  }, 0)
  .to(nextContainer, {
    x: 0,
    duration: 1.5,
    force3D: true,
    ease: customEases.pageTransition2,
  }, 0);

  return tl;
}
```

### 3. Custom Variations You Can Build

Mix and match these properties for new transitions:

| Effect | Current Page | Next Page Initial | Next Page Final |
|---|---|---|---|
| **Bottom reveal** | `y: "-30vh", scale: 0.8` | `clipPath: "inset(100% 0% 0% 0%)"` | `clipPath: "inset(0%)"` |
| **Top reveal** | `y: "30vh", scale: 0.8` | `clipPath: "inset(0% 0% 100% 0%)"` | `clipPath: "inset(0%)"` |
| **Left reveal** | `x: "50%", scale: 0.8` | `clipPath: "inset(0% 100% 0% 0%)"` | `clipPath: "inset(0%)"` |
| **Circle reveal** | `scale: 0.9, opacity: 0` | `clipPath: "circle(0% at 50% 50%)"` | `clipPath: "circle(100% at 50% 50%)"` |
| **Diagonal wipe** | `scale: 0.8, opacity: 0.3` | `clipPath: "polygon(100% 0, 100% 0, 100% 100%, 100% 100%)"` | `clipPath: "polygon(0 0, 100% 0, 100% 100%, 0 100%)"` |

## Enter Animations (SplitText)

These run on the incoming page content during the transition, creating a staggered text reveal.

### Character-by-Character Title Reveal

```js
function enterAnimation(container) {
  const tl = gsap.timeline({ delay: 0.32 });  // sync with transition

  // Split heading into characters
  const h1 = container.querySelector("h1");
  const split = new SplitText(h1, {
    type: "chars",
    charsClass: "char",
  });

  // Wrap each char for overflow clipping
  h1.style.overflow = "hidden";

  // Set initial state
  gsap.set(split.chars, {
    y: "100%",
    rotateX: 60,
    force3D: true,
  });

  // Animate in
  tl.to(split.chars, {
    y: 0,
    rotateX: 0,
    duration: 2.1,
    stagger: 0.035,
    ease: "expo.out",
  });

  return { tl, split };  // return split for cleanup
}
```

### Line-by-Line Paragraph Reveal

```js
function revealLines(container, selector) {
  const elements = container.querySelectorAll(selector);
  const splits = [];

  elements.forEach((el) => {
    const split = new SplitText(el, { type: "lines", linesClass: "line" });
    splits.push(split);

    // Wrap each line in overflow-hidden div
    split.lines.forEach((line) => {
      const wrapper = document.createElement("div");
      wrapper.style.overflow = "hidden";
      line.parentNode.insertBefore(wrapper, line);
      wrapper.appendChild(line);
      gsap.set(line, { y: "100%" });
    });
  });

  return splits;
}

// In the timeline:
tl.to(container.querySelectorAll(".line"), {
  y: 0,
  duration: 1.65,
  stagger: { each: 0.08, from: "end" },
  ease: "power3.out",
}, 0.32);
```

### Horizontal Rule Slide-In

```js
// CSS: .lines { overflow: hidden; } .inner_line { transform: translateX(-100%); }

tl.to(container.querySelectorAll(".inner_line"), {
  x: 0,
  duration: 1.2,
  stagger: 0.25,
  ease: "power2.inOut",
}, 0.32);
```

## The Router

### Vanilla JS (minimal SPA router)

```js
let isTransitioning = false;
let currentPage = null;
let currentNamespace = null;

const routes = {
  "/": { namespace: "home", loader: () => import("./pages/home.js") },
  "/about": { namespace: "about", loader: () => import("./pages/about.js") },
};

// Intercept all internal link clicks via event delegation
document.addEventListener("click", (e) => {
  const link = e.target.closest("a");
  if (!link) return;

  const url = new URL(link.href, window.location.origin);
  if (url.origin !== window.location.origin) return;  // external link
  if (url.pathname === window.location.pathname) return; // same page

  e.preventDefault();
  navigate(url.pathname);
});

// Browser back/forward
window.addEventListener("popstate", () => {
  performTransition(window.location.pathname);
});

async function navigate(path) {
  if (isTransitioning) return;
  window.history.pushState({}, "", path);
  await performTransition(path);
}

async function performTransition(path) {
  if (isTransitioning) return;
  isTransitioning = true;

  try {
    // Cleanup current page
    if (currentPage?.cleanup) currentPage.cleanup();

    // Load next page
    const route = routes[path] || routes["/"];
    const nextModule = await route.loader();
    const nextHTML = nextModule.default();

    // Execute the transition
    await executeTransition({
      currentNamespace,
      nextNamespace: route.namespace,
      nextHTML,
      nextModule,
    });

    currentPage = nextModule;
    currentNamespace = route.namespace;
  } finally {
    isTransitioning = false;
  }
}
```

### The Transition Engine

```js
async function executeTransition({ currentNamespace, nextNamespace, nextHTML, nextModule }) {
  const wrapper = document.querySelector('[data-transition="wrapper"]');
  const currentContainer = document.querySelector('[data-transition="container"]');

  // 1. Create next container (shallow clone preserves data attributes)
  const nextContainer = currentContainer.cloneNode(false);
  nextContainer.setAttribute("data-namespace", nextNamespace);

  // 2. Inject content
  const main = document.createElement("main");
  main.id = "page_content";
  main.innerHTML = nextHTML;
  nextContainer.appendChild(main);

  // 3. Add to DOM — both pages now coexist
  wrapper.appendChild(nextContainer);

  // 4. Wait for images to load (prevents layout shift)
  const images = nextContainer.querySelectorAll("img");
  await Promise.all(
    Array.from(images).map(
      (img) => new Promise((resolve) => {
        if (img.complete) resolve();
        else {
          img.onload = resolve;
          img.onerror = resolve;
        }
      })
    )
  );

  // 5. Init enter animations on next page
  if (nextModule.init) nextModule.init({ container: nextContainer });

  // 6. Get and run transition animation
  const transitionFn = getTransition(currentNamespace, nextNamespace);
  const timeline = await transitionFn(currentContainer, nextContainer);
  await timeline.then();

  // 7. Cleanup
  currentContainer.remove();
  gsap.set(nextContainer, { clearProps: "all" });
}
```

### Transition Registry

Map specific route pairs to different animations:

```js
const transitionRegistry = {
  "home-to-about": defaultTransition,
  "about-to-home": alternativeTransition,
  default: defaultTransition,
};

function getTransition(from, to) {
  return transitionRegistry[`${from}-to-${to}`] || transitionRegistry.default;
}
```

## Adapting to Frameworks

### React / Next.js

The dual-container pattern translates to React by using refs and portals:

```jsx
// Conceptual approach — adapt to your routing setup
function PageTransition({ children, routeKey }) {
  const wrapperRef = useRef();
  const [pages, setPages] = useState([{ key: routeKey, content: children }]);

  useEffect(() => {
    if (pages.length === 2) {
      const [oldPage, newPage] = wrapperRef.current.children;
      const tl = defaultTransition(oldPage, newPage);
      tl.then(() => {
        setPages((p) => [p[1]]); // remove old page
        gsap.set(newPage, { clearProps: "all" });
      });
    }
  }, [pages]);

  // When route changes, add new page
  useEffect(() => {
    setPages((prev) => [...prev, { key: routeKey, content: children }]);
  }, [routeKey]);

  return (
    <div ref={wrapperRef} data-transition="wrapper">
      {pages.map((page) => (
        <div key={page.key} data-transition="container">
          {page.content}
        </div>
      ))}
    </div>
  );
}
```

For Next.js App Router, wrap this around `{children}` in your root layout, using `usePathname()` as the route key.

### Astro / Multi-Page

Use the View Transitions API with GSAP as enhancement:

```js
document.addEventListener("astro:before-swap", (e) => {
  // Animate out current page before swap
});
document.addEventListener("astro:after-swap", () => {
  // Animate in new page after swap
});
```

## Performance Checklist

- `force3D: true` on all GSAP tweens — forces GPU-accelerated transforms
- `backface-visibility: hidden` on containers — prevents render artifacts
- `will-change: transform` on elements about to animate
- `transform: translateZ(0)` on transition containers — creates GPU compositing layer
- `clearProps: "all"` after transition — removes inline styles to prevent accumulation
- Preload images with `Promise.all` before starting transition
- `lazy: false` on timeline defaults — ensures tweens render immediately
- Use `position: fixed` for the incoming page — prevents scroll interference

## Cleanup Pattern

Always clean up SplitText instances and GSAP properties when leaving a page:

```js
// In page module
let splits = [];

export function init({ container }) {
  const split = new SplitText(container.querySelector("h1"), { type: "chars" });
  splits.push(split);
  // ... animate
}

export function cleanup() {
  splits.forEach((s) => s.revert());  // restores original DOM
  splits = [];
}
```

This prevents memory leaks and DOM pollution across navigations.

## Common Pitfalls

1. **Querying the wrong container** — During transition, both pages exist. Always scope queries to the specific container: `nextContainer.querySelector(".title")`, never `document.querySelector(".title")`.

2. **Scroll position** — Reset scroll on navigation: `window.scrollTo(0, 0)` after transition completes.

3. **Missing `isTransitioning` guard** — Without it, rapid clicks cause race conditions with multiple containers in the DOM.

4. **Forgetting `clearProps`** — GSAP inline styles accumulate. Always clear after transition.

5. **Images causing layout shift** — Always wait for images before starting the transition animation.

For the complete reference implementation with all file contents, read `references/full-implementation.md`.
