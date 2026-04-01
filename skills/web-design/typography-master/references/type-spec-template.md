# Production Typography Specification Template

Use this template to deliver a final, implementable typography spec to the user once a font decision has been made.

---

## Typography Specification: [Project Name]

### Primary Typeface
**[Font Name]**
- Source: Google Fonts / Fontshare / Adobe Fonts
- Load URL: `https://fonts.googleapis.com/css2?family=...`
- Weights to load: 400, 600, 700 (only load what you use)

### Secondary Typeface (if using a pair)
**[Font Name]**
- Source: ...
- Weights to load: 400, 500

---

### Type Scale (CSS Custom Properties)

```css
:root {
  /* Font families */
  --font-display: '[Heading Font]', sans-serif;
  --font-body: '[Body Font]', sans-serif;
  --font-mono: 'JetBrains Mono', monospace; /* only if needed */

  /* Size scale (1.333 ratio from 16px base) */
  --text-xs:   0.75rem;   /* 12px */
  --text-sm:   0.875rem;  /* 14px */
  --text-base: 1rem;      /* 16px */
  --text-lg:   1.125rem;  /* 18px */
  --text-xl:   1.25rem;   /* 20px */
  --text-2xl:  1.5rem;    /* 24px */
  --text-3xl:  1.875rem;  /* 30px */
  --text-4xl:  2.25rem;   /* 36px */
  --text-5xl:  3rem;      /* 48px */
  --text-6xl:  3.75rem;   /* 60px */
  --text-7xl:  4.5rem;    /* 72px */
  --text-8xl:  6rem;      /* 96px */

  /* Line heights */
  --leading-tight:   1.1;
  --leading-snug:    1.25;
  --leading-normal:  1.5;
  --leading-relaxed: 1.625;
  --leading-loose:   1.75;

  /* Letter spacing */
  --tracking-tight:  -0.025em;
  --tracking-normal:  0em;
  --tracking-wide:    0.025em;
  --tracking-wider:   0.05em;
  --tracking-widest:  0.1em;

  /* Font weights */
  --font-normal:    400;
  --font-medium:    500;
  --font-semibold:  600;
  --font-bold:      700;
  --font-extrabold: 800;
}
```

---

### Typographic Roles

| Role | Font | Size | Weight | Line Height | Tracking |
|------|------|------|--------|-------------|----------|
| Hero / Display | Display | 72–96px | 700–800 | 1.05 | -0.03em |
| H1 | Display | 48–60px | 700 | 1.1 | -0.02em |
| H2 | Display | 36–42px | 600–700 | 1.15 | -0.01em |
| H3 | Display | 24–30px | 600 | 1.25 | 0 |
| H4 | Body | 18–22px | 600 | 1.35 | 0 |
| Body Large | Body | 18–20px | 400 | 1.6 | 0 |
| Body | Body | 16px | 400 | 1.65 | 0 |
| Body Small | Body | 14px | 400 | 1.5 | 0.01em |
| Label / UI | Body | 12–13px | 500 | 1.4 | 0.05em |
| Caption | Body | 11–12px | 400 | 1.4 | 0.03em |
| Code | Mono | 14px | 400 | 1.6 | 0 |

---

### Google Fonts Implementation

```html
<!-- In <head> — optimize with preconnect -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=[FONT1]:wght@400;600;700&family=[FONT2]:wght@400;500&display=swap" rel="stylesheet">
```

**Performance notes:**
- Use `display=swap` to prevent invisible text during load
- Only load the weights you actually use
- Consider `font-display: optional` for above-the-fold text to avoid layout shift
- Self-host fonts for best performance (use google-webfonts-helper.herokuapp.com)

---

### CSS Base Styles

```css
body {
  font-family: var(--font-body);
  font-size: var(--text-base);
  line-height: var(--leading-normal);
  font-weight: var(--font-normal);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-rendering: optimizeLegibility;
}

h1, h2, h3, h4 {
  font-family: var(--font-display);
  font-weight: var(--font-bold);
  line-height: var(--leading-tight);
  letter-spacing: var(--tracking-tight);
}

/* Prevent orphans in headings */
h1, h2 {
  text-wrap: balance;
}

/* Better reading width */
p, li {
  max-width: 65ch;
}
```

---

### Responsive Type Scale

```css
/* Fluid typography for hero headings */
.hero-headline {
  font-size: clamp(2.5rem, 5vw + 1rem, 6rem);
  line-height: 1.05;
  letter-spacing: -0.03em;
}

.hero-subheadline {
  font-size: clamp(1rem, 1.5vw + 0.5rem, 1.375rem);
  line-height: 1.6;
}
```
