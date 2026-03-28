# Full Reference Implementation

Complete source from the [codrops async page transitions demo](https://github.com/blenkcode/codrops-demo) by Valentin Mor.

## Table of Contents

1. [Entry Point](#entry-point)
2. [Router](#router)
3. [Transition Engine](#transition-engine)
4. [Transition Animations](#transition-animations)
5. [Transition Registry](#transition-registry)
6. [GSAP Library Setup](#gsap-library-setup)
7. [Enter Animations](#enter-animations)
8. [SplitText Helpers](#splittext-helpers)
9. [Page Modules](#page-modules)
10. [Web Components](#web-components)
11. [CSS](#css)
12. [Without SplitText](#without-splittext)

---

## Entry Point

`src/main.js`

```js
import "./components/index.js";
import "./style.css";
import { initRouter } from "./router.js";

initRouter();
```

## Router

`src/router.js`

```js
import { executeTransition } from "./transitions/pageTransition.js";

let isTransitioning = false;
let currentPage = null;
let currentNamespace = null;

const routes = {
  "/": {
    namespace: "home",
    loader: () => import("./pages/home/home.js"),
  },
  "/alternative-page": {
    namespace: "about",
    loader: () => import("./pages/about/about.js"),
  },
};

export function initRouter() {
  // Event delegation — works even when links are dynamically injected
  document.addEventListener("click", (e) => {
    const link = e.target.closest("a");
    if (!link) return;

    const url = new URL(link.href, window.location.origin);
    if (url.origin !== window.location.origin) return;

    e.preventDefault();

    if (url.pathname === window.location.pathname) return;

    navigate(url.pathname);
  });

  window.addEventListener("popstate", () => {
    performTransition(window.location.pathname);
  });

  // Initial page load
  const initialPath = window.location.pathname;
  const route = routes[initialPath] || routes["/"];

  route.loader().then((mod) => {
    currentPage = mod;
    currentNamespace = route.namespace;

    const container = document.querySelector('[data-transition="container"]');
    if (container) {
      container.setAttribute("data-namespace", route.namespace);
    }

    if (mod.init) {
      mod.init({ container });
    }
  });
}

async function navigate(path) {
  if (isTransitioning) return;

  window.history.pushState({}, "", path);
  await performTransition(path);
}

async function performTransition(path) {
  if (isTransitioning) return;
  isTransitioning = true;

  try {
    if (currentPage?.cleanup) {
      currentPage.cleanup();
    }

    const route = routes[path] || routes["/"];
    const nextModule = await route.loader();
    const nextHTML = nextModule.default();

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

## Transition Engine

`src/transitions/pageTransition.js`

```js
import gsap from "gsap";
import { getTransition } from "./registry.js";

export async function executeTransition({
  currentNamespace,
  nextNamespace,
  nextHTML,
  nextModule,
}) {
  const currentContainer = document.querySelector(
    '[data-transition="container"]'
  );
  const wrapper = document.querySelector('[data-transition="wrapper"]');

  // Shallow clone — preserves data attributes, not children
  const nextContainer = currentContainer.cloneNode(false);
  nextContainer.setAttribute("data-namespace", nextNamespace);

  // Create and inject content
  const main = document.createElement("main");
  main.id = "page_content";
  main.innerHTML = nextHTML;
  nextContainer.appendChild(main);

  // Both pages now coexist in DOM
  wrapper.appendChild(nextContainer);

  // Wait for all images to load
  const images = nextContainer.querySelectorAll("img");
  if (images.length > 0) {
    await Promise.all(
      Array.from(images).map(
        (img) =>
          new Promise((resolve) => {
            if (img.complete) {
              resolve();
            } else {
              img.onload = resolve;
              img.onerror = resolve;
            }
          })
      )
    );
  }

  // Init enter animations on the next page
  if (nextModule.init) {
    nextModule.init({ container: nextContainer });
  }

  // Get and run the transition
  const transitionFn = getTransition(currentNamespace, nextNamespace);
  const timeline = await transitionFn(currentContainer, nextContainer);

  // Wait for animation to complete
  await timeline.then();

  // Cleanup: remove old, clear inline styles on new
  currentContainer.remove();
  gsap.set(nextContainer, { clearProps: "all" });
}
```

## Transition Animations

### Default — Clip-Path Bottom Reveal

`src/transitions/animations/default.js`

```js
import { gsap, customEases } from "../../lib/index.js";

export function defaultTransition(currentContainer, nextContainer) {
  gsap.set(nextContainer, {
    clipPath: "inset(100% 0% 0% 0%)",
    opacity: 1,
    position: "fixed",
    top: 0,
    left: 0,
    width: "100%",
    height: "100vh",
    zIndex: 10,
  });

  const tl = gsap.timeline({ defaults: { lazy: false } });

  tl.to(
    currentContainer,
    {
      y: "-30vh",
      opacity: 0.4,
      scale: 0.8,
      duration: 0.7,
      force3D: true,
      ease: customEases.pageTransition,
    },
    0
  ).to(
    nextContainer,
    {
      clipPath: "inset(0% 0% 0% 0%)",
      duration: 0.7,
      force3D: true,
      ease: customEases.pageTransition,
    },
    0
  );

  return tl;
}
```

### Alternative — Horizontal Slide

`src/transitions/animations/alternative.js`

```js
import { gsap, customEases } from "../../lib/index.js";

export function alternativeTransition(currentContainer, nextContainer) {
  gsap.set(nextContainer, {
    opacity: 1,
    position: "fixed",
    top: 0,
    left: 0,
    width: "100%",
    height: "100vh",
    x: "100%",
    zIndex: 10,
  });

  const tl = gsap.timeline({ defaults: { lazy: false } });

  tl.to(
    currentContainer,
    {
      x: "-50%",
      scale: 0.8,
      opacity: 0.4,
      duration: 1.5,
      force3D: true,
      ease: customEases.pageTransition2,
    },
    0
  ).to(
    nextContainer,
    {
      x: 0,
      duration: 1.5,
      force3D: true,
      ease: customEases.pageTransition2,
    },
    0
  );

  return tl;
}
```

## Transition Registry

`src/transitions/registry.js`

```js
import { defaultTransition } from "./animations/default.js";
import { alternativeTransition } from "./animations/alternative.js";

const transitionRegistry = {
  "home-to-about": defaultTransition,
  "about-to-home": defaultTransition,
  default: defaultTransition,
};

export function getTransition(currentNamespace, nextNamespace) {
  const key = `${currentNamespace}-to-${nextNamespace}`;
  return transitionRegistry[key] || transitionRegistry.default;
}
```

## GSAP Library Setup

`src/lib/index.js`

```js
import gsap from "gsap";
import { CustomEase } from "gsap/CustomEase";
import { SplitText } from "gsap/SplitText";

gsap.registerPlugin(CustomEase, SplitText);

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

export { gsap, SplitText, CustomEase, customEases };
```

## Enter Animations

`src/animations/Enter.js`

```js
import { gsap, SplitText } from "../lib/index.js";
import { wrap_lines, wrap_chars } from "../helpers/wrap.js";

let charSplits = [];
let lineSplits = [];

export function Enter(container) {
  const tl = gsap.timeline({ delay: 0.32 });

  // Character animation on h1
  const h1 = container.querySelector("h1");
  if (h1) {
    const charSplit = new SplitText(h1, {
      type: "chars",
      charsClass: "char",
    });
    charSplits.push(charSplit);
    wrap_chars(charSplit.chars);

    tl.to(
      charSplit.chars,
      {
        y: 0,
        rotateX: 0,
        duration: 2.1,
        stagger: 0.035,
        ease: "expo.out",
      },
      0
    );
  }

  // Line animation on paragraphs
  const paragraphs = container.querySelectorAll(".anim_p");
  paragraphs.forEach((p) => {
    const lineSplit = new SplitText(p, {
      type: "lines",
      linesClass: "line",
    });
    lineSplits.push(lineSplit);
    wrap_lines(lineSplit.lines);
  });

  tl.to(
    container.querySelectorAll(".anim_p .line"),
    {
      y: 0,
      duration: 1.65,
      stagger: { each: 0.08, from: "end" },
      ease: "power3.out",
    },
    0.32
  );

  // Secondary paragraphs
  const paragraphs2 = container.querySelectorAll(".anim_p2");
  paragraphs2.forEach((p) => {
    const lineSplit = new SplitText(p, {
      type: "lines",
      linesClass: "line",
    });
    lineSplits.push(lineSplit);
    wrap_lines(lineSplit.lines);
  });

  tl.to(
    container.querySelectorAll(".anim_p2 .line"),
    {
      y: 0,
      duration: 1.65,
      stagger: { each: 0.08, from: "end" },
      ease: "power3.out",
    },
    0.32
  );

  // Horizontal rules
  tl.to(
    container.querySelectorAll(".inner_linesright"),
    {
      x: 0,
      duration: 1.2,
      stagger: 0.25,
      ease: "power2.inOut",
    },
    0.32
  );

  tl.to(
    container.querySelectorAll(".inner_linesleft"),
    {
      x: 0,
      duration: 1.2,
      stagger: 0.25,
      ease: "power2.inOut",
    },
    0.32
  );

  // Fade in hero
  tl.to(
    container.querySelector(".hero_content"),
    {
      opacity: 1,
      duration: 0.01,
    },
    0
  );

  return tl;
}

export function cleanupEnter() {
  charSplits.forEach((s) => s.revert());
  lineSplits.forEach((s) => s.revert());
  charSplits = [];
  lineSplits = [];
}
```

## SplitText Helpers

`src/helpers/wrap.js`

```js
import gsap from "gsap";

export function wrap_chars(chars) {
  chars.forEach((char) => {
    gsap.set(char, {
      y: "100%",
      rotateX: 60,
      force3D: true,
    });
  });
}

export function wrap_lines(lines) {
  lines.forEach((line) => {
    const wrapper = document.createElement("div");
    wrapper.style.overflow = "hidden";
    line.parentNode.insertBefore(wrapper, line);
    wrapper.appendChild(line);
    gsap.set(line, { y: "100%" });
  });
}
```

## Page Modules

### Home Page

`src/pages/home/home.js`

```js
import pageContent from "./home.html?raw";
import { Enter, cleanupEnter } from "../../animations/Enter.js";

export default function () {
  return pageContent;
}

export function init({ container }) {
  Enter(container);
}

export function cleanup() {
  cleanupEnter();
}
```

`src/pages/home/home.html`

```html
<section class="hero">
  <div class="hero_content">
    <div class="hero_titlecontainer">
      <h1>Async Transitions</h1>
    </div>
    <div class="hero_subcontent">
      <div class="hero_subcontentleft">
        <div class="hero_subcontentleft_lines">
          <div class="lines">
            <div class="inner_linesright"></div>
          </div>
          <div class="lines">
            <div class="inner_linesleft"></div>
          </div>
        </div>
        <p class="anim_p">
          A silky transition demo, powered by GSAP 3 and vanilla JavaScript.
        </p>
      </div>
      <div class="hero_subcontentright">
        <ul>
          <li class="anim_p2">GSAP 3</li>
          <li class="anim_p2">SplitText</li>
          <li class="anim_p2">Custom Ease</li>
          <li class="anim_p2">Vanilla JS</li>
        </ul>
      </div>
    </div>
  </div>
</section>
```

### About Page

`src/pages/about/about.js`

```js
import pageContent from "./about.html?raw";
import { Enter, cleanupEnter } from "../../animations/Enter.js";

export default function () {
  return pageContent;
}

export function init({ container }) {
  Enter(container);
}

export function cleanup() {
  cleanupEnter();
}
```

## Web Components

### Header Component

`src/components/header-c.js`

```js
class HeaderComponent extends HTMLElement {
  constructor() {
    super();
    this._rendered = false;
  }

  connectedCallback() {
    if (this._rendered) return;
    this._rendered = true;

    this.innerHTML = `
      <nav class="nav">
        <div class="nav_left">
          <link-c href="/" text="Home"></link-c>
        </div>
        <div class="nav_right">
          <link-c href="/alternative-page" text="Alternative"></link-c>
        </div>
      </nav>
    `;
  }
}

customElements.define("header-c", HeaderComponent);
```

### Link Component (with hover animation)

`src/components/link-c.js`

```js
import gsap from "gsap";

class LinkComponent extends HTMLElement {
  constructor() {
    super();
    this.handleHoverIn = this.handleHoverIn.bind(this);
    this.handleHoverOut = this.handleHoverOut.bind(this);
    this.handleClick = this.handleClick.bind(this);
  }

  connectedCallback() {
    this.render();
    const link = this.querySelector("a");
    link.addEventListener("mouseenter", this.handleHoverIn);
    link.addEventListener("mouseleave", this.handleHoverOut);
    link.addEventListener("click", this.handleClick);
  }

  disconnectedCallback() {
    const link = this.querySelector("a");
    if (link) {
      link.removeEventListener("mouseenter", this.handleHoverIn);
      link.removeEventListener("mouseleave", this.handleHoverOut);
      link.removeEventListener("click", this.handleClick);
    }
  }

  isSamePage() {
    const href = this.getAttribute("href");
    const normalize = (p) => (p === "/" ? "/" : p.replace(/\/$/, ""));
    return normalize(href) === normalize(window.location.pathname);
  }

  handleHoverIn() {
    if (this.isSamePage()) return;
    const line = this.querySelector(".line_a_inner");
    gsap.set(line, { x: "-101%" });
    gsap.to(line, { x: 0, duration: 0.8, ease: "power3.out" });
  }

  handleHoverOut() {
    const line = this.querySelector(".line_a_inner");
    gsap.to(line, { x: "101%", duration: 0.5, ease: "power3.out" });
  }

  handleClick(e) {
    if (this.isSamePage()) {
      e.preventDefault();
      e.stopPropagation();
    }
  }

  render() {
    const href = this.getAttribute("href");
    const text = this.getAttribute("text");

    this.innerHTML = `
      <a href="${href}" class="nav_link">
        <div class="overflow">
          <span>${text}</span>
        </div>
        <div class="line_a">
          <div class="line_a_inner"></div>
        </div>
      </a>
    `;
  }
}

customElements.define("link-c", LinkComponent);
```

## CSS

### Variables & Typography

```css
:root {
  --title-size: clamp(3rem, 8vw, 8rem);
}

h1 {
  font-size: var(--title-size);
  font-weight: 400;
  line-height: 1.1;
  overflow: hidden;
  text-transform: uppercase;
}
```

### Page Layout

```css
.hero {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.hero_content {
  opacity: 0; /* hidden until Enter animation */
  width: 100%;
  max-width: 1200px;
}

.hero_subcontent {
  display: flex;
  justify-content: space-between;
  margin-top: 2rem;
}
```

### Horizontal Rules

```css
.lines {
  overflow: hidden;
  position: relative;
  height: 1px;
  width: 100%;
  margin: 0.5rem 0;
}

.inner_linesright,
.inner_linesleft {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: currentColor;
}

.inner_linesright {
  transform: translateX(-100%);
}

.inner_linesleft {
  transform: translateX(100%);
}
```

### Navigation

```css
.nav {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: space-between;
  padding: 1.5rem 2rem;
  z-index: 50;
  mix-blend-mode: difference;
  color: white;
}

.nav_link {
  text-decoration: none;
  color: inherit;
  position: relative;
}

.overflow {
  overflow: hidden;
}

.line_a {
  position: relative;
  height: 1px;
  width: 100%;
  overflow: hidden;
  margin-top: 2px;
}

.line_a_inner {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: currentColor;
  transform: translateX(-101%);
}
```

### Transition Container

```css
body {
  background-color: #000000;
  color: #1a1a1a;
  font-family: "Helvetica Neue", sans-serif;
  margin: 0;
  overflow-x: hidden;
}

main {
  background-color: #ffffff;
  width: 100%;
  min-height: 100vh;
}

[data-transition="container"] {
  transform: translateZ(0);
  backface-visibility: hidden;
  will-change: transform;
}
```

## Without SplitText

If GSAP SplitText (Club plugin) is unavailable, you can achieve similar effects:

### Option 1: Manual character splitting

```js
function splitChars(element) {
  const text = element.textContent;
  element.innerHTML = "";
  element.style.overflow = "hidden";

  return [...text].map((char) => {
    const span = document.createElement("span");
    span.textContent = char === " " ? "\u00A0" : char;
    span.style.display = "inline-block";
    element.appendChild(span);
    return span;
  });
}

// Usage
const chars = splitChars(h1);
gsap.set(chars, { y: "100%", rotateX: 60 });
gsap.to(chars, { y: 0, rotateX: 0, duration: 2.1, stagger: 0.035, ease: "expo.out" });
```

### Option 2: Simpler fade-up without splitting

```js
// No splitting needed — just animate the whole element
gsap.from(container.querySelector("h1"), {
  y: 60,
  opacity: 0,
  duration: 1.2,
  ease: "expo.out",
  delay: 0.32,
});

gsap.from(container.querySelectorAll("p"), {
  y: 40,
  opacity: 0,
  duration: 1,
  stagger: 0.1,
  ease: "power3.out",
  delay: 0.5,
});
```

This is simpler but still looks great. The key premium feel comes from the page transition itself (clip-path reveal), not necessarily the text splitting.
