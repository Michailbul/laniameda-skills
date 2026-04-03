---
name: carousel-designer
description: >
  Design and produce high-engagement social media carousels as self-contained HTML,
  rendered to PDF + PNGs via Playwright.

  Use when asked to build, generate, design, or iterate on a carousel, social media slides,
  Instagram carousel, LinkedIn carousel, slide deck, swipe post, or branded content slides.

  Supports Instagram, LinkedIn, Twitter/X, and Stories. Supports three modes: SHOWCASE
  (AI art / prompt shares), EDUCATE (tutorials, how-tos, listicles), and THINK (thought
  leadership / raw ideas). Also use for comparison carousels (tool-vs-tool, before-vs-after,
  model-vs-model) where each compared output should get its own full-width slide rather than a cramped split layout.
---

# Carousel Designer

Generate publish-ready social media carousels as a single self-contained HTML file. Export to PDF + PNGs via Playwright.

## Output structure

```
<project>/
  src/slides.html      <- single file, all slides
  dist/carousel.pdf
  dist/slides/01.png ... NN.png
  package.json         <- { "type": "module", "dependencies": { "playwright": "^1.52" } }
```

---

## Phase 0: Parse the Request

Before designing anything, extract from the user's message:

| Field | Default |
|-------|---------|
| **Topic** | (required) |
| **Key points** | Extract or infer from topic |
| **CTA** | "Save + follow" |
| **Tone** | brand-system-aligned |
| **Platform** | Instagram + LinkedIn (1080x1350) |
| **Mode** | EDUCATE |
| **Slide count** | 7 (min 5, max 10) |
| **Carousel type** | Educational |
| **Brand system** | Use the active brand guidelines when available |
| **Comparison format** | If comparing outputs, default to one output per slide (full-width), not side-by-side unless the user explicitly asks for a split |

If topic is unclear, ask one question only: *"What's the main idea you want to get across?"*

---

## Platform Specs

| Platform | Dimensions | Max Slides | Aspect Ratio |
|----------|-----------|------------|--------------|
| **Instagram** | 1080x1350px | 20 | 4:5 |
| **LinkedIn** | 1080x1350px | 20 | 4:5 |
| **Twitter/X** | 1080x1080px | 4 | 1:1 |
| **Story** | 1080x1920px | 7 | 9:16 |

Default to **1080x1350** (4:5) unless X-only or Story is explicitly requested. 4:5 takes more feed real estate than square.

---

## Carousel Modes

### SHOWCASE -- Prompt Shares / AI Art
The image IS the content. The design system provides a premium dark frame.
- **CSS**: `assets/styles/mode-showcase.css`
- **Template**: `assets/templates/showcase-template.html`
- **Key components**: `.showcase-frame`, `.showcase-prompt`, `.showcase-param-tag`, `.showcase-model-badge`
- **Slides**: Image hook -> Prompt detail -> CTA
- **Rule**: Minimal text. The art speaks.

### EDUCATE -- Tutorials, How-Tos, Listicles
Structured content with clear hierarchy and progressive disclosure.
- **CSS**: `assets/styles/mode-educate.css`
- **Template**: `assets/templates/educate-template.html`
- **Key components**: `.step-number`, `.edu-card`, `.edu-list`, `.edu-callout`, `.edu-progress`
- **Slides**: Hook -> Step slides -> List slides -> Stats -> CTA
- **Rule**: One idea per slide. Max 30 words.

### THINK -- Thought Leadership / Raw Ideas
Pure text, maximum negative space, dramatic typography.
- **CSS**: `assets/styles/mode-think.css`
- **Template**: `assets/templates/think-template.html`
- **Key components**: `.think-hero`, `.think-body-lg`, `.think-accent`, `.think-gradient`, `.think-counter`
- **Slides**: Statement -> Emphasis -> CTA
- **Rule**: NO glass cards, NO code blocks, NO accent chips. Typography does ALL the work.

---

## Workflow -- follow in order, skip nothing

### Phase 1: Design Intelligence (before writing any HTML)
1. Read `references/REFERENCES.md` -- extract layout patterns, type choices, color moments, spacing ratios from listed references. Note which patterns apply to each slide type.
2. Read `references/layout-rules.md` -- internalize all 12 rules. These override any general instincts about layout.
3. Read `references/design-standards.md` -- lock in the typography scale + quality checklist.
4. Read the brief -- map each key point to a slide type and select the right primitive or mode component.

### Phase 2: Build
5. **LinkedIn / brutalist-tech mode**: Read `assets/linkedin-base.html` -- use as skeleton (fonts, tokens, grid/grain, slide counter all pre-wired). Read `assets/components/primitives.html` -- copy-paste the right building block per slide.
6. **Dark Tech mode (SHOWCASE / EDUCATE / THINK)**: Load `assets/styles/carousel-base.css` first, then the mode-specific CSS. Use the corresponding template from `assets/templates/` as a starting point.
7. Build `src/slides.html`:
   - Start from chosen base template, fill all slides
   - Apply layout-rules.md constraints (alignment, scale contrast, negative space)
   - Apply patterns extracted from REFERENCES.md
   - Every element left-aligned unless explicitly specified otherwise
   - Slide counter or progress indicator on every slide
   - Adjust slide count dynamically (min 5, default 7, max 10)

### Phase 3: Render & QA
8. Run `npm install` then `node scripts/render.mjs`
9. Run full quality checklist (see Design Audit below)
10. If any check fails: fix and re-render (do not skip)
11. Print: `RENDER_COMPLETE: dist/carousel.pdf + dist/slides/01-NN.png`

### Phase 4: Visual Review & Feedback Loop (max 3 iterations)
12. Review each rendered PNG against the quality checklist.
13. **Decision:**
    - All checks pass -> deliver
    - 1-3 issues -> fix with structured feedback diffs, re-render
    - Major structural issues -> rebuild from Phase 2
14. Format feedback as structured diffs, never prose:
    ```
    slide_1.headline: clips right edge -- reduce font-size 148px -> 120px
    slide_3.metric-card: missing shadow
    slide_7.closing: no CTA keyword -- add "Comment THROUGHPUT and I'll send it"
    ```
15. After 3 iterations, deliver best available and note remaining issues.

---

## Carousel Anatomy (every carousel follows this)

Every carousel maps to four functional zones. No exceptions.

| Position | Role | Job |
|----------|------|-----|
| Slide 1 | **THE HOOK** | Stop the scroll. Bold, visual, provocative. Biggest text. |
| Slide 2 | **THE TRANSITION** | What will the user gain / what will the user avoid / what makes you qualified |
| Slides 3–N-1 | **THE TEASE** | Reveal info bit by bit. Examples, statistics, captivating visuals. Keep swiping. |
| Last slide | **THE ACTION** | Make the next step obvious. One clear CTA. |

**Typography minimums at carousel scale (1080x1350):**
- Headlines: **50pt minimum** (55pt+ preferred)
- Body copy: **14pt minimum** — smaller sizes cause drop-off

---

## Phase 5: Deliver

### Option A — Telegram delivery (default)
```bash
# Send PDF
message(send, filePath: $PROJECT/dist/carousel.pdf)

# Send cover preview
message(send, filePath: $PROJECT/dist/slides/01.png,
        caption: "Carousel ready. N slides. Reply with any tweaks.")
```

### Option B — Schedule to LinkedIn via Publora

If Michael asks to schedule or post, use the Publora REST API.

**Prerequisite:** Publora API key must be in env as `PUBLORA_API_KEY`. Account must be on Pro plan ($2.99/mo/account).

**1. List connected accounts (find the LinkedIn platform ID):**
```bash
curl -s https://api.publora.com/api/v1/platform-connections \
  -H "x-publora-key: $PUBLORA_API_KEY" | jq '.connections'
# Returns: [{platformId: "linkedin-ABC123", username: "...", displayName: "..."}]
```

**2. Schedule the carousel:**

> Publora accepts LinkedIn carousels as a PDF document upload. Use the presigned upload URL flow.

```bash
# Step 1: get presigned S3 upload URL
curl -s -X POST https://api.publora.com/api/v1/get-upload-url \
  -H "Content-Type: application/json" \
  -H "x-publora-key: $PUBLORA_API_KEY" \
  -d '{"filename": "carousel.pdf", "contentType": "application/pdf"}'
# Returns: { uploadUrl, fileKey }

# Step 2: upload PDF to S3
curl -s -X PUT "$UPLOAD_URL" \
  -H "Content-Type: application/pdf" \
  --data-binary @$PROJECT/dist/carousel.pdf

# Step 3: create post with fileKey
curl -s -X POST https://api.publora.com/api/v1/create-post \
  -H "Content-Type: application/json" \
  -H "x-publora-key: $PUBLORA_API_KEY" \
  -d "{
    \"content\": \"$POST_CAPTION\",
    \"platforms\": [\"$LINKEDIN_PLATFORM_ID\"],
    \"scheduledTime\": \"$ISO_DATETIME\",
    \"mediaKey\": \"$FILE_KEY\"
  }"
```

**When to use Publora vs. manual delivery:**
- Michael says "schedule this for tomorrow" or "post to LinkedIn" → use Publora
- Michael wants to review first → deliver to Telegram, wait for approval
- No Publora key → deliver to Telegram only, note that Publora integration is available

---

## Slide Map (default 7-slide LinkedIn)

| # | Type | Components to use |
|---|------|-------------------|
| 1 | Cover | kicker, hero-headline, subtitle, badge-row |
| 2 | Problem | kicker, section-headline, subtitle |
| 3 | Stat / Math | kicker, section-headline, metric-card OR equation-block |
| 4 | Stat / Math | kicker, section-headline, metric-card OR equation-block |
| 5 | System | kicker, section-headline, checklist |
| 6 | Solution | kicker, section-headline, stack-grid |
| 7 | CTA | kicker, section-headline, ordered-list, closing-line |

## Slide Archetypes (for flexible builds)

Use these as building blocks for any carousel type:

- **Hook Slide** (Slide 1 -- always required): Bold headline (5-8 words max), optional subheadline. Largest text. No logos, no branding clutter.
- **Context Slide**: Set up the problem. 1-2 sentences max.
- **Content Slide**: Deliver the value. One idea per slide. Max 30 words.
- **Stats/Data Slide**: One hero number (huge), supporting context (small).
- **Quote Slide**: Social proof. Generous whitespace.
- **Before/After Slide**: Split layout with clear labels.
- **CTA Slide** (final -- always required): ONE clear call to action. Do not dilute.

---

## Carousel Type Templates

### Educational / Tips
```
Slide 1: Bold claim hook
Slide 2: Why this matters (context)
Slides 3-6: One tip each, numbered
Slide 7: CTA (save + follow)
```

### Storytelling / Case Study
```
Slide 1: Outcome hook ("How I went from X to Y")
Slide 2: The starting situation
Slide 3: The challenge / pain
Slide 4: What we tried (failed)
Slide 5: What actually worked
Slide 6: The result (numbers/proof)
Slide 7: Key takeaway + CTA
```

### Before / After
```
Slide 1: Transformation hook
Slide 2: The "before" state (problem framed)
Slide 3: Problem 1 -- what made it broken
Slide 4: The "after" state
Slide 5: What changed + why it worked
Slide 6: Result proof
Slide 7: Offer to help / CTA
```

### Comparison / Model Battle
```
Slide 1: Hook — what is being compared and why it matters
Slide 2: Comparison item 1 — output A (full-width)
Slide 3: Comparison item 1 — output B (full-width)
Slide 4: Comparison item 2 — output A
Slide 5: Comparison item 2 — output B
...
Final slide: Exact value-exchange CTA
```
Rules:
- one compared output per slide by default
- full-width image beats half-width split in almost every Instagram case
- prompt/context box at top, image as hero below
- use side-by-side only when the brief explicitly prioritizes simultaneous visual comparison over image quality

### Tools / Listicle
```
Slide 1: Number hook ("7 tools that changed how I create")
Slide 2: Context -- why tools matter / what was missing
Slides 3-6: 1-2 tools per slide, name + one-liner use case
Slide 7: Save + follow CTA
```

### Narrative Arc Templates (Dark Tech modes)
**Educational (5-8 slides):** Hook -> Context -> Content -> Content -> Content -> Stats -> CTA
**Storytelling (6-8 slides):** Hook -> Context -> Content -> Content -> Quote -> Content -> CTA
**Listicle (5-10 slides):** Hook -> Content -> Content -> Content -> Content -> ... -> CTA
**Comparison (5-7 slides):** Hook -> Before/After -> Content -> Content -> Stats -> CTA
**Single Concept Deep Dive (4-6 slides):** Hook -> Context -> Content -> Content -> CTA

---

## Hook Types

The most important slide. If this fails, nobody swipes.

| Type | Formula | Example |
|------|---------|---------|
| Bold claim | "[X]% of [audience] [painful truth]" | "90% of content strategies skip this" |
| Question | "Why does [common thing] [not work]?" | "Why does posting daily still not grow you?" |
| Number + promise | "[N] [things] you [outcome verb]" | "5 tools that replaced my whole production team" |
| Contrarian | "Stop doing [popular thing]. Do [this]." | "Stop making content. Build a content engine." |
| Before/After | State the transformation in one line | "I went from 3 posts/month to 30 posts/week -- same effort" |

---

## Swipe Psychology (bake into slide design)

| Principle | How to apply |
|-----------|-------------|
| Curiosity gap | Hook promises value that requires swiping to unlock |
| Numbered progress | Show "3/7" or progress dots to create completion drive |
| Visual continuity | Consistent design signals "there's more" |
| Increasing value | Best insight last -- rewards completing the whole carousel |
| Swipe cue | Arrow or "Swipe ->" text on slide 1 |

---

## Color Presets

| Mood | Background | Accent | Body text |
|------|-----------|--------|-----------|
| Obsidian editorial | `#0A0805` | `#F26157` (coral) | `rgba(240,235,232,0.60+)` |
| Carbon system | `#191919` | `#F26157` / `#79B791` | `rgba(240,235,232,0.60+)` |
| Graphite utility | `#3A3A3A` | `#F26157` | `rgba(240,235,232,0.60+)` |
| Linen light | `#FFF4EA` | `#F26157` | `#1A1008` |
| Amber signal | `#E8A838` | `#1A1008` / `#F26157` | `#1A1008` |

Validated rejects for carousel backgrounds:
- `#3D2E42` / purple-adjacent Charcoal Violet
- `#4A5E7A` / blue-grey Slate Blue
- pure black `#000000`
- pure white `#FFFFFF`

Default to the brand-system palette above unless the user explicitly asks for a different visual language.

---

## Fonts

### Brutalist / LinkedIn mode
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
```
Display: Bebas Neue. Body: Space Grotesk. Mono: JetBrains Mono. **Never use Arial/Inter/Roboto as display.**

### Dark Tech modes
Font stack: Space Grotesk (headlines) + Inter (body) + JetBrains Mono (code/labels). Loaded via `carousel-base.css`.

---

## Brand tokens (Brutalist / LinkedIn mode -- inline in `<script>` block)

```js
tailwind.config = {
  theme: { extend: {
    colors: { primary:'#8566AF', secondary:'#BA943B', accent:'#EA3F2C', 'accent-alt':'#FF552E', brand:'#09090B' },
    fontFamily: {
      display: ['"Bebas Neue"', 'Impact', 'sans-serif'],
      body:    ['"Space Grotesk"', '"Helvetica Neue"', 'sans-serif'],
      mono:    ['"JetBrains Mono"', '"SF Mono"', 'monospace'],
    },
  }},
}
```

---

## Laniameda Positioning Rules (Non-Negotiable)

These apply to all carousels unless Michael explicitly overrides:

### Audience
**Creative brands and creative studios.** Not engineers. Not enterprise buyers. People who think in campaigns, content calendars, and creative output -- not runtimes.

### Default tone
- Outcome-first. Lead with what they get, feel, or achieve.
- Crisp. No padding, no hedging, no corporate speak.
- Confident. State things. Don't ask.
- Creative. Slide design should feel intentional, not templated.

### Language to avoid
- runtime, orchestration, sub-agent, spawn, inference, async, parallel workloads
- "leverage", "utilize", "synergy", "ecosystem"
- DevOps / backend engineering framing as the lead

### Language to lean into
- content engine, production pipeline, creative OS, creative leverage
- on-brand, consistent, more output same team, stay creative director
- transformation vocabulary: "from X to Y", "now you can...", "what used to take..."

### Exception
For **OpenClaw architecture / agent infrastructure** topics, technical framing is acceptable and intentional. The audience there is technical-curious builders, not default creative brand audience.

### Anti-patterns
- Do not lead with "AI tools can help you..." -- commodity angle
- Do not use "leverage AI to..." -- weak and overused
- Do not explain the tech before explaining the outcome
- Do not let the tool be the hero -- the creator's output/life is the hero

---

## Hard rules

- Every slide: class `slide`, id `slide-0N`, fixed dimensions via CSS
- **Brutalist mode**: Black border (12px sides, 14px top/bottom, #09090B). Grid overlay via `::before`, grain via `::after`. `chrome` div: `position:relative; z-index:1; padding:78px 76px; display:flex; flex-direction:column`. Slide counter `"0N / 07"` on every slide.
- **Dark Tech modes**: `.slide` is 1080x1350 with grid background and vignette built in. `.safe-zone` has 80px inset with 48px bottom padding for footer. `.slide-footer` with handle + progress dots on every slide.
- **The Unforgettable Rule**: slide 1 must pass -- one element works as a standalone viral image
- **1 idea per slide** -- no walls of text
- Max 30-40 words per content slide
- Accent color on <=1 element per slide
- No placeholder text -- real content from brief only
- If the slide is image-led, do not put opaque containers/cards on top of the image; solve contrast with gradients and text shadows first
- For comparison carousels, default to one output per slide; do not crush images into side-by-side half-width frames unless explicitly requested
- CTA copy should preserve the exact value exchange from the brief; do not rewrite it into a generic "save/follow" hook if the user supplied a concrete offer
- Print `RENDER_COMPLETE` only after PDF + all PNGs verified to exist

---

## Design Audit (run before delivering)

### Layout
- [ ] No text clipping at edges (right side is the most common failure)
- [ ] No overflow below slide boundary
- [ ] Borders/grid/vignette visible and correct for chosen mode
- [ ] All text within safe zone with footer clearance

### Typography
- [ ] Fonts loading correctly (condensed display, not generic fallback)
- [ ] Font sizes are phone-readable (nothing under 18px)
- [ ] Max 30 words per content slide
- [ ] 3 typographic levels max per slide

### Hierarchy
- [ ] One dominant headline per slide
- [ ] One focal point per slide -- eye lands in one place
- [ ] Using correct mode CSS (showcase/educate/think/brutalist)
- [ ] Clear narrative arc from slide 1 to final

### Brand
- [ ] Accent color used on <=1 element per slide
- [ ] Consistent spacing using correct base unit (24px or 54px grid)
- [ ] Color palette consistent with chosen preset

### Content
- [ ] Slide 1: cover -- bold hook, passes the unforgettable test
- [ ] Content slides: one key idea each
- [ ] CTA slide has exactly ONE clear action
- [ ] No Lorem Ipsum or placeholder text anywhere
- [ ] Numbers/stats match the brief

### Mode-specific
- [ ] SHOWCASE: Minimal text, art is the hero, showcase-frame has visible depth
- [ ] EDUCATE: Glass cards have depth (inset highlight + outer shadows), grid at 60px cells
- [ ] THINK: NO cards/chips/code blocks -- text only
- [ ] BRUTALIST: Black border on all 4 sides, slide counter bottom-right

### Export
- [ ] PNGs are exactly the target dimensions
- [ ] Footer (handle + progress OR slide counter) present on every slide
- [ ] Exported PNGs match what was designed

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Weak hook (slide 1) | Bold claim, question, or number + promise |
| Too much text per slide | Max 30-40 words, hard limit |
| No visual consistency | Same colors, fonts, margins throughout |
| No swipe indicator on slide 1 | Add "Swipe ->" or arrow |
| No CTA on last slide | Ask to save, follow, share, or comment |
| Cramming 2+ ideas per slide | One point per slide, always |
| Square format on Instagram | Default to 1080x1350 (4:5) |
| Leading with technical language | Lead with outcome; audience is creative brands |
| Center-aligned body text | Left-align everything (see layout-rules.md rule 1) |

---

## Reference files -- read ALL in Phase 1 before writing HTML

| File | What it contains | When to use |
|------|-----------------|-------------|
| `references/REFERENCES.md` | Design inspiration + brand DNA | Extract layout/type/color patterns before designing |
| `references/layout-rules.md` | 12 explicit design rules | Alignment, scale contrast, spacing, card style, narrative arc |
| `references/design-standards.md` | Typography scale, color rules, quality checklist | Type sizes, color assignments, QA after render |
| `references/brief-template.md` | Brief template for structured requests | Fill before building when topic needs structuring |
| `references/quality-checklist.md` | Per-slide visual review checklist | Run on every PNG set before approving |

## Asset files -- copy-paste when building

| File | What it contains |
|------|-----------------|
| `assets/linkedin-base.html` | Brutalist skeleton: fonts, Tailwind config, grid/grain, slide counter |
| `assets/components/primitives.html` | All brutalist primitives: kicker, headlines, metric-card, equation, terminal, checklist, stack-grid, badge-row, closing-line |
| `assets/brand-tokens.js` | Tailwind color + font config |
| `assets/styles/carousel-base.css` | Dark Tech design tokens + shared components (ALWAYS load for modes) |
| `assets/styles/mode-showcase.css` | Showcase-specific styles |
| `assets/styles/mode-educate.css` | Educate-specific styles |
| `assets/styles/mode-think.css` | Think-specific styles |
| `assets/templates/showcase-template.html` | 3-slide showcase starter (image hook, prompt detail, CTA) |
| `assets/templates/educate-template.html` | 5-slide educate starter (hook, step, list, stats, CTA) |
| `assets/templates/think-template.html` | 3-slide think starter (statement, emphasis, CTA) |
| `scripts/render.mjs` | Playwright render -> PDF + PNGs (copy to project root) |

---

## Usage Examples

**LinkedIn carousel (brutalist, default):**
```
/carousel-designer 5 ways to increase throughput
```

**Instagram educate mode:**
```
/carousel-designer educate: how to use Claude Code skills, 7 slides, platform:instagram
```

**Showcase mode (AI art):**
```
/carousel-designer showcase: my latest Midjourney garden scene
```

**Think mode (thought leadership):**
```
/carousel-designer think: taste is the last moat in AI
```

**With specific slide count:**
```
/carousel-designer 10 tools every designer needs, 10 slides
```

**Twitter/X format:**
```
/carousel-designer 3 things about X, platform:x
```
