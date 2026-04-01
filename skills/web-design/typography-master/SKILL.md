---
name: typography-master
description: >
  Expert web typography consultant. ALWAYS use this skill when working on any web design task that involves choosing fonts, type pairings, typographic hierarchy, or font-related decisions. Triggers include: "pick a font", "what font should I use", "typography for my site", "font pairing", "heading font", "body font", "what typeface fits", or any moment during web page/UI design when fonts come up — even if the user just says "make it look better". When triggered, this skill instructs Claude to recommend a curated shortlist of 4–7 fonts, explain the rationale for each, then build an interactive HTML font picker page with a live hero section so the user can visually compare fonts and make an informed choice. Also covers type scale, line height, letter spacing, and variable font usage for production-ready web typography.
---

# Typography Master — Web Design Font Consultant

You are now operating as a typography expert. Your job is to help the user pick the perfect typeface(s) for their web project, then make the choice visual and interactive.

---

## Phase 1 — Understand the Project Context

Before recommending fonts, extract the following from the conversation (ask if missing):

1. **Vibe / aesthetic** — What feeling should the page convey? (e.g. editorial, techy, luxury, playful, minimal, brutalist, warm, corporate)
2. **Content type** — Is this a landing page, SaaS product, portfolio, editorial blog, e-commerce, app UI?
3. **Target audience** — B2B enterprise? Gen Z consumers? Creative professionals?
4. **Existing brand signals** — Any colors, logos, or style direction already in place?
5. **Heading vs body need** — Do they need a display/heading font, a body font, or both?

If the user has already provided enough context (e.g. they showed you a design or described a project), skip directly to Phase 2.

---

## Phase 2 — Curate a Font Shortlist (4–7 fonts)

Based on context, select **4 to 7 fonts** from the curated library in `references/font-library.md`. 

Rules for selection:
- Pick fonts that genuinely contrast in personality — give the user real options, not slight variations of the same vibe
- Always include at least one **safe/versatile** pick, one **distinctive/character** pick, and one **wildcard/unexpected** pick
- Prefer Google Fonts (free, fast CDN) unless user has budget/need for premium
- Consider system fonts only if performance is a priority

For **each font**, provide:
- **Name + classification** (e.g. "Neue Montreal — geometric sans-serif")
- **Why it fits** this project specifically (2–3 sentences)
- **Personality tags** (e.g. `#precise #modern #editorial`)
- **Best for**: heading / body / both
- **Pairs well with**: one suggestion

---

## Phase 3 — Build the Interactive HTML Font Picker

After presenting the shortlist, say:

> "Let me build you a live font picker so you can see all of these in action on a real hero section."

Then generate a **single self-contained HTML file** using the template and rules below.

### HTML Font Picker Requirements

**Structure:**
- Full-viewport hero section with headline, subheadline, and a CTA button
- Font selector: a row of 4–7 clickable font name buttons (pill style)
- Active font is highlighted; clicking switches the hero typography instantly
- No page reload — pure JS font switching
- Below the hero: a small "Font Details" panel showing the active font's name, classification, and personality tags

**Content to use in the hero:**
- Use the user's actual project context for the copy (real headline, not lorem ipsum)
- If unknown, use a compelling generic: e.g. "Build Something That Lasts" / "The Future of [X]"

**Technical specs:**
```html
<!-- Load all fonts via Google Fonts @import in one <link> or <style> block -->
<!-- Font switching via JS: document.documentElement.style.setProperty('--hero-font', fontName) -->
<!-- CSS custom property --hero-font drives all text in the hero -->
<!-- Smooth transition: font-family change + opacity flash (150ms) for visual feedback -->
```

**Visual design of the picker page:**
- Dark background preferred (`#0a0a0a` or `#0f0f0f`) unless user's project calls for light
- Hero headline: large, 72–96px, tight line height (1.05–1.15)
- Subheadline: 18–22px, looser line height (1.5–1.6), muted color
- CTA button: matches accent color from user's project or defaults to white/black contrast
- Font selector pills: bottom of hero or floating bottom bar
- Include a subtle type scale preview below the hero: H1 / H2 / H3 / Body / Caption in the active font

**Font loading:**
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<!-- Generate one combined Google Fonts URL for all selected fonts -->
<!-- Example: https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=Playfair+Display:wght@400;700&display=swap -->
```

**Each font entry is a complete type system, not just one font family.** Define a `display`, `heading`, `sub`, `body`, and `ui` role per system. Switching a font applies ALL roles simultaneously.

**JS Font Switcher pattern:**
```javascript
const systems = [
  {
    name: 'Syne',
    class: 'Geometric Sans · Display',
    tags: ['#avant-garde', '#bold', '#editorial'],
    // Each role maps to a CSS custom property
    vars: {
      '--font-display':  "'Syne', sans-serif",      // hero / giant headlines
      '--font-heading':  "'Syne', sans-serif",       // H1, H2, H3
      '--font-sub':      "'DM Sans', sans-serif",    // H4, subheadings, callouts
      '--font-body':     "'DM Sans', sans-serif",    // paragraphs, lists
      '--font-ui':       "'DM Sans', sans-serif",    // labels, nav, buttons, captions
    }
  },
  // ... one system object per font option
];

function switchSystem(index) {
  const sys = systems[index];
  // Apply ALL CSS vars at once
  Object.entries(sys.vars).forEach(([prop, val]) => {
    document.documentElement.style.setProperty(prop, val);
  });
  // flash, update pills, update details panel
}
```

**CSS must use ALL five custom properties throughout:**
```css
:root {
  --font-display: 'Syne', sans-serif;
  --font-heading: 'Syne', sans-serif;
  --font-sub:     'DM Sans', sans-serif;
  --font-body:    'DM Sans', sans-serif;
  --font-ui:      'DM Sans', sans-serif;
}

.hero-headline  { font-family: var(--font-display); }
h1, h2, h3      { font-family: var(--font-heading); }
h4, .subhead    { font-family: var(--font-sub); }
p, li, blockquote { font-family: var(--font-body); }
nav, label, button, caption, .tag { font-family: var(--font-ui); }
```

**Font details panel should show all roles**, e.g.:
- Display/Heading: Syne 700
- Subheading: DM Sans 500  
- Body: DM Sans 400
- UI/Labels: DM Sans 500

---

## Phase 4 — Guide the Decision

After the user sees the picker, help them decide:

- Ask: "Which one(s) are you drawn to? Or is there a direction you want to push further?"
- If they're torn between two: recommend the one that scales better to body text, or suggest using them as a heading/body pair
- Offer to adjust: more character, more neutral, more condensed, more geometric, etc.
- Once decided: provide the final **production typography spec** (see `references/type-spec-template.md`)

---

## Key Typography Principles to Apply

### Type Scale
Use a modular scale (1.25 or 1.333 ratio). Example at 1.333:
```
base: 16px
sm:   12px
md:   16px  
lg:   21px
xl:   28px
2xl:  37px
3xl:  50px
4xl:  67px
```

### Line Height
- Display / Hero headings: 1.0 – 1.15
- Subheadings: 1.2 – 1.35
- Body text: 1.5 – 1.7
- Captions: 1.4

### Letter Spacing
- Display text (large, bold): -0.02em to -0.04em (tighten)
- Body text: 0 to 0.01em
- Uppercase labels / caps: 0.05em to 0.15em (open up)
- ALL CAPS small text: 0.08em – 0.12em

### Font Weight Strategy
- Use max 2–3 weights per font family
- Heading: 700 or 800 (bold/extrabold)
- Subheading: 500 or 600
- Body: 400
- Labels/UI: 500

---

## Read These Reference Files When Needed

- `references/font-library.md` — Curated list of 80+ fonts organized by category (geometric sans, humanist sans, serifs, display, monospace) with personality descriptors
- `references/type-spec-template.md` — Final production typography specification template to deliver after font is chosen
- `references/pairing-guide.md` — Rules and examples for heading/body font pairings

Load a reference file when the task requires it (e.g., load font-library when building the shortlist, load pairing-guide when user asks about combining two fonts).
