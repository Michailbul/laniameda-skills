---
name: brand-guidelines-builder
description: >
  Builds a complete, reusable brand guidelines document for any company, product,
  startup, creative project, or idea — from scratch or from a brief. Use this skill
  whenever a user wants to define, create, or document a brand identity. Triggers
  include: "create brand guidelines for X", "define our brand", "build a brand identity",
  "what should our brand look like", "brand colors for my startup", "brand kit", "brand
  system", "visual identity", "brand document", "style guide", or any request to
  establish or formalize a brand. Always use this skill when a new project needs a
  brand foundation before design work begins. Once guidelines are generated, they can
  be saved as a project-specific skill and reused across all future artifacts.
---

# Brand Guidelines Builder

A reusable system for creating complete brand guidelines for any company, product,
or idea. Run this skill once per project, then save the output as a project-specific
brand skill to apply consistently across all future artifacts.

---

## WHEN TO USE THIS SKILL

- User wants to define or formalize a brand for a new or existing project
- User has a rough idea but no structured brand identity yet
- User wants a reusable brand system they can apply to decks, docs, websites, etc.
- A new client project is starting and needs a brand foundation

---

## STEP 1 — GATHER BRAND INPUTS

Start by collecting what the user already has. Ask only what you don't already know from context. Categories to cover:

### A. Identity basics
- **Name** of the brand / product / company
- **One-line description**: what it is, who it's for
- **Industry / category**: tech, wellness, fashion, B2B SaaS, creative studio, etc.
- **Stage**: early idea, startup, established brand, rebrand

### B. Personality & tone
Ask the user to pick 3–5 words that describe the brand's personality. Offer examples if they're stuck:
> "Bold, minimal, warm, playful, authoritative, experimental, luxury, accessible, technical, human, dark, vibrant, clean, raw, cinematic"

### C. Visual references
- Any existing logos, colors, or assets?
- Any brands they admire visually? (doesn't have to be same industry)
- Dark or light aesthetic preference?
- Any colors they definitely want or want to avoid?

### D. Audience
- Who is the target customer / user?
- What's the emotional experience they should have with this brand?

### E. Outputs needed
- What will this brand be applied to? (website, decks, social, product UI, docs, video)

If the user provides a URL, website, or existing doc — read it first and extract as much as possible before asking questions. Only ask for what's missing.

---

## STEP 2 — GENERATE THE BRAND SYSTEM

Once you have enough input (aim for at least A + B + C), generate a complete brand guidelines document using the structure below. Use creative judgment to fill gaps — make opinionated, coherent decisions rather than leaving things open.

### OUTPUT STRUCTURE

Produce a markdown document with the following sections:

---

### 1. Brand Overview
- Name
- Tagline (generate one if none exists)
- One-paragraph brand story / positioning
- Brand archetype (choose one: Creator, Hero, Sage, Explorer, Rebel, Magician, Ruler, Caregiver, Jester, Lover, Innocent, Everyman)

### 2. Personality & Voice
- 5 personality adjectives
- Tone of voice: how the brand speaks (formal/casual, warm/cool, etc.)
- 3 "we are / we are not" pairs (e.g. "We are bold. We are not aggressive.")
- Sample copy: write 2–3 example sentences in brand voice

### 3. Color System
Define a complete palette with hex codes and usage rules:

```
PRIMARY
#XXXXXX — [name] — Main brand color, dominant in UI and print

SECONDARY
#XXXXXX — [name] — Supporting color, used for accents and CTAs

NEUTRAL DARK
#XXXXXX — [name] — Text, dark backgrounds

NEUTRAL LIGHT
#XXXXXX — [name] — Light backgrounds, cards, whitespace

ACCENT (optional)
#XXXXXX — [name] — Highlight color, use sparingly
```

Rules to include:
- Which color is dominant vs. supporting
- Dark mode vs. light mode defaults
- What never to combine (contrast violations)

### 4. Typography
Define heading and body fonts. Choose from Google Fonts for maximum compatibility.

```
HEADING FONT: [Font Name]
  Weight: Bold (700) for H1, Semibold (600) for H2–H3
  Use for: all headings, display text, hero sections

BODY FONT: [Font Name]
  Weight: Regular (400) for body, Medium (500) for labels/captions
  Use for: paragraphs, UI text, documentation

MONO FONT (if needed): [Font Name]
  Use for: code, technical data, timestamps
```

Type scale (px, desktop):
- H1: 56px / H2: 40px / H3: 28px / H4: 20px / Body: 16px / Caption: 13px

### 5. Logo & Mark Usage
Even without a logo file, document rules:
- Preferred logo format (wordmark / icon + wordmark / monogram)
- Clear space rule: minimum padding = X height of logo
- Background rules: approved backgrounds for logo placement
- What NOT to do: stretch, recolor, add effects

### 6. Imagery & Photography Style
Describe the visual language for photos, illustrations, and video:
- Photography mood (e.g. "candid and natural, never stock-photo polished")
- Color grading direction (warm/cool, high/low contrast, saturated/muted)
- Illustration style if applicable
- What to avoid

### 7. UI & Layout Principles (if digital product)
- Border radius: sharp (0px) / soft (4–8px) / rounded (12–16px+)
- Shadow style: none / subtle / dramatic
- Spacing system: 8px base grid
- Component feel: dense vs. airy

### 8. Quick-Reference Card
End with a compact summary:

```
BRAND: [Name]
TAGLINE: [Tagline]
ARCHETYPE: [Archetype]
PERSONALITY: [5 words]

COLORS
Primary: #XXXXXX
Secondary: #XXXXXX
Dark: #XXXXXX
Light: #XXXXXX

FONTS
Heading: [Font], Bold
Body: [Font], Regular

VOICE: [2-sentence summary]
```

---

## STEP 3 — DELIVER & OFFER TO SAVE

After generating the brand guidelines:

1. **Present the full document** in the chat as formatted markdown
2. **Offer to create a downloadable .docx** if the user wants a shareable file
3. **Offer to save as a project skill** — say:

> "Want me to save this as a `[brand-name]-brand` skill in your Laniameda skills library? That way I'll automatically apply these guidelines to any artifact I create for this project."

If they say yes, package the brand system into a minimal SKILL.md using this template:

```markdown
---
name: [brand-name]-brand
description: >
  Applies [Brand Name] brand guidelines to any artifact. Use whenever creating
  docs, decks, websites, social assets, or any visual output for [Brand Name].
  Triggers on any mention of [brand name] or requests to style something
  "for [brand name]".
---

# [Brand Name] Brand Guidelines

[Paste the Quick-Reference Card here]

[Paste the full Color System here]

[Paste the full Typography section here]

[Paste the Personality & Voice section here]

[Paste the Imagery Style section here]
```

Then install it to `/mnt/skills/user/[brand-name]-brand/SKILL.md`.

---

## NOTES FOR THE AGENT

- Be opinionated. Don't leave color palettes or font choices as "TBD" — make a strong, coherent decision and explain the reasoning briefly.
- If the user gives a vague brief (e.g. "a tech startup for Gen Z"), use industry knowledge to infer what would work. You can offer alternatives.
- Prioritize coherence over novelty — the brand system should feel like one unified thing, not a collection of random choices.
- Reference the `design-inspiration` skill if you need to check saved visual references before making aesthetic decisions.
- Reference the `typography-master` skill if the user wants an interactive font comparison before locking in typography choices.
