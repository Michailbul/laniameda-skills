---
name: laniameda-carousel-copy
description: >
  Write slide-by-slide carousel copy for Laniameda social media posts.
  Handles the CONTENT side — what goes on each slide, hook writing, copy frameworks,
  CTA strategy — not the visual design or rendering.

  Triggers: "write a carousel", "carousel copy", "what should the slides say",
  "write slides for", "carousel about [topic]", "draft a carousel", "carousel script",
  "slide copy for", or any request to write the text content for a carousel post.

  Does NOT trigger for: rendering/exporting carousels (use carousel-designer),
  building design systems (use carousel-brand-system), or general social posts
  without carousel format (use social-content).
version: 0.1.0
---

# Laniameda Carousel Copy

Write publish-ready slide-by-slide copy for social media carousels. This skill produces the TEXT — what each slide says, in what order, with what tone. Hand the output to `carousel-designer` or Canva for visual production.

---

## Before writing: Read these

1. `human-copy-standards` — every line must pass. No AI-speak, no filler, no inflation words.
2. `brand/voice.md` — Laniameda voice: direct, specific, earned confidence.
3. `brand/content-standards.md` — which pillar does this carousel serve?

If copy doesn't pass `human-copy-standards`, rewrite before delivering. No exceptions.

---

## Step 1: Parse the Request

Extract from the user's message or ask one question:

| Field | Default |
|-------|---------|
| **Topic** | (required) |
| **Pillar** | Infer from topic. One of: Art, AI Creatorship, Cinematic Frames, Web/AI Design, Gen AI/Tools, Building in Public, Marketing-First, AI Engineering |
| **Carousel type** | Infer from topic (see types below) |
| **Platform** | Instagram + LinkedIn |
| **Slide count** | 7 (min 5, max 10) |
| **CTA goal** | Save + Follow (default) |
| **Tone override** | None (use default Laniameda voice) |

If the topic is too vague to write specific copy, ask: *"What's the one thing someone should walk away knowing?"*

---

## Step 2: Pick the Carousel Type

### Prompt Share
For sharing AI generation prompts, workflows, or creation processes.

```
Slide 1 (HOOK):     Provocative claim about the prompt or result
Slide 2 (CONTEXT):  Why this prompt matters / what makes it different
Slide 3 (PROMPT):   The actual prompt — monospace, full text, no cuts
Slide 4 (BREAKDOWN): 3-4 key elements that make it work, with WHY
Slide 5 (RESULT):   The output — image placeholder + brief caption
Slide 6 (INSIGHT):  The transferable lesson (not just "use good prompts")
Slide 7 (CTA):      Save + follow
```

### Educational / Tips
For teaching techniques, sharing knowledge, listicles.

```
Slide 1 (HOOK):       Bold claim or number + promise
Slide 2 (TRANSITION): Why this matters / what most people get wrong
Slides 3-6 (TEASE):   One tip per slide, numbered. Example + explanation.
Slide 7 (CTA):        Save + follow + optional comment trigger
```

### Storytelling / Case Study
For process stories, behind-the-scenes, lessons learned.

```
Slide 1 (HOOK):     Outcome hook ("How I went from X to Y")
Slide 2 (CONTEXT):  The starting situation — make it relatable
Slide 3 (PROBLEM):  The challenge or pain point
Slide 4 (ATTEMPT):  What was tried and failed (builds credibility)
Slide 5 (SOLVE):    What actually worked
Slide 6 (RESULT):   Numbers, proof, transformation
Slide 7 (CTA):      Key takeaway + follow
```

### Tool Review / Comparison
For AI tools, workflows, model comparisons.

```
Slide 1 (HOOK):     "I tested X so you don't have to" / "X vs Y: honest take"
Slide 2 (CONTEXT):  What problem this tool solves
Slides 3-5 (TEASE): One feature/finding per slide with real example
Slide 6 (VERDICT):  Honest recommendation — who should use it, who shouldn't
Slide 7 (CTA):      Save + follow + "Comment [KEYWORD] for my full setup"
```

### Thought Piece
For opinions, takes, philosophy. Pure text, maximum impact.

```
Slide 1 (HOOK):     Contrarian statement or uncomfortable truth
Slide 2 (TENSION):  Why the common belief is wrong
Slides 3-5 (BUILD): Build the argument — one point per slide
Slide 6 (RESOLVE):  The reframe — new way of thinking
Slide 7 (CTA):      "Agree or not?" + follow
```

### Before / After
For transformations, redesigns, prompt iterations.

```
Slide 1 (HOOK):     Transformation hook — show the gap
Slide 2 (BEFORE):   The "before" state
Slide 3 (PROBLEM):  What made it broken / weak
Slide 4 (AFTER):    The "after" state
Slide 5 (HOW):      What changed + why it worked
Slide 6 (PROOF):    Result or comparison
Slide 7 (CTA):      Save + follow
```

---

## Step 3: Write the Copy

### Anatomy rules (every carousel, no exceptions)

| Position | Role | Rule |
|----------|------|------|
| Slide 1 | **THE HOOK** | Stop the scroll. 5-8 words max. Biggest text. No branding clutter. |
| Slide 2 | **THE TRANSITION** | What will the reader gain / avoid / why you're qualified |
| Slides 3 to N-1 | **THE TEASE** | Reveal bit by bit. One idea per slide. Keep swiping. |
| Last slide | **THE ACTION** | One clear CTA. Do not dilute. |

### Per-slide copy limits

| Element | Limit |
|---------|-------|
| Hook headline | 5-8 words |
| Body text per slide | 30 words max |
| Lines of body text | 4-5 max |
| CTA | One action only |

### Chrome copy (same on every slide)

```
Header:  ● LANIAMEDA   [PILLAR TAG in accent]
Footer:  @michael.bul                    ●●●●●●●
```

Pillar tags: `AI CREATORSHIP` · `BUILDING IN PUBLIC` · `TOOLS` · `ART` · `WEB DESIGN` · `MARKETING`

Optional metadata: date (`APR 2026`), pack label (`VOL.01`), tool tag (`MIDJOURNEY V6.1`)

---

## Hook Formulas

### By psychology trigger

| Trigger | Formula | Example |
|---------|---------|---------|
| **Curiosity gap** | "[Specific claim] — here's why" | "This prompt took me 47 tries to get right" |
| **Pattern interrupt** | "Stop doing [common thing]" | "Stop using 'high quality' in your prompts" |
| **Social proof** | "[Number] [people] [did thing]" | "1.2M people saw this image. Here's the prompt." |
| **Specificity** | "[Exact number] [things] that [outcome]" | "3 words that changed every image I generate" |
| **Contrarian** | "[Popular belief] is wrong" | "Your prompt isn't too short. It's too generic." |
| **Transformation** | "From [bad state] to [good state]" | "From generic renders to editorial photography — one prompt change" |
| **FOMO** | "[Thing] most people don't know" | "The Midjourney parameter nobody talks about" |

### By carousel type

| Type | Best hooks |
|------|-----------|
| Prompt Share | Curiosity gap, Specificity, Social proof |
| Educational | Specificity, Pattern interrupt, FOMO |
| Storytelling | Transformation, Social proof |
| Tool Review | Contrarian, Specificity |
| Thought Piece | Contrarian, Pattern interrupt |

---

## CTA Strategies

| Goal | CTA copy | When to use |
|------|----------|-------------|
| **Save** | "Save this for your next session." | Prompt shares, tools, tips |
| **Follow** | "Follow @michael.bul for prompts that work." | Always (combine with another) |
| **Comment** | "Comment [KEYWORD] and I'll send you the full prompt." | Lead gen, DM automation |
| **Share** | "Send this to someone who needs it." | Relatable content, hot takes |
| **Link** | "Full breakdown in bio." | Long-form content, articles |

Default CTA: **Save + Follow**. Never use more than 2 actions per CTA slide.

---

## Voice Rules (Laniameda-specific)

### DO
- State things. Don't ask permission to have an opinion.
- Use specific references (model names, exact settings, real numbers).
- Write like someone who's done the thing, not read about it.
- One idea per slide. If it needs a comma and "also", split the slide.
- Short sentences. Varied length. Let a line breathe.

### DON'T
- "Top 5 AI tools that will blow your mind" — commodity angle, zero taste
- "Leverage AI to enhance your creative workflow" — corporate death
- "In this carousel, I'll share..." — we can see it's a carousel
- "Let's dive in" / "Without further ado" — just start
- "Game-changing" / "Revolutionary" / "Must-have" — inflation kills trust
- Hashtag soup on slides (save for caption)
- Lorem ipsum or placeholder text anywhere

### Tone calibration by pillar

| Pillar | Tone | Example |
|--------|------|---------|
| AI Creatorship | Craft-focused, specific, workshop energy | "The film stock matters. Portra 800 gives you grain structure that Velvia can't." |
| Building in Public | Honest, vulnerable, no polish | "I broke the deploy at 2am. Here's what I learned." |
| Tools | Direct verdict, no hedging | "Midjourney v6 is better for portraits. Flux wins on text rendering. That's it." |
| Art | Philosophical, feeling-first | "The best images come from prompts that describe feelings, not objects." |
| Marketing | Strategy-forward, numbers when possible | "One carousel, six platforms, zero extra effort. Here's how." |

---

## Output Format

Deliver copy as a structured slide deck:

```
CAROUSEL: [Title]
TYPE: [Carousel type]
PILLAR: [Content pillar]
PLATFORM: [Instagram / LinkedIn / Both]
SLIDES: [count]

---

SLIDE 1 — HOOK
[Headline text]
[Subheadline if needed — max 1 line]

SLIDE 2 — TRANSITION
[Body text — max 30 words]

SLIDE 3 — [SLIDE TYPE]
[Number or label if applicable]
[Headline]
[Body text]

...

SLIDE 7 — CTA
[CTA headline]
[CTA body]
[Handle: @michael.bul]

---

CHROME:
Header: ● LANIAMEDA   [PILLAR TAG]
Footer: @michael.bul   ●●●●●●●
Optional: [date/pack/tool tag]

CAPTION DRAFT:
[Instagram/LinkedIn caption — separate from slide copy]
```

---

## Caption Writing (post body, not on slides)

Write a short caption to accompany the carousel post:

- **Line 1:** Hook that mirrors slide 1 (slightly different wording)
- **Line 2-3:** Context or personal angle
- **Last line:** CTA (save, follow, comment keyword)
- **Hashtags:** 5-8 relevant, after a line break. Mix niche + broad.

Example:
```
This prompt changed how I think about AI photography.

Not because it's complicated — because every word has a job.
The film stock controls grain. The photographer reference sets composition.
The fabric choice gives the AI something to render light through.

Save this. Try it. Then follow @michael.bul for more prompts that actually teach you something.

#AICreatorship #Midjourney #PromptEngineering #AIPhotography #CreativeAI
```

---

## Quality Checklist (run before delivering)

- [ ] Every slide passes `human-copy-standards` (no AI-speak, no filler)
- [ ] Hook slide: 5-8 words, stops the scroll, no branding clutter
- [ ] One idea per slide, max 30 words per slide
- [ ] Pillar is identified and tone matches
- [ ] Chrome copy is specified (header + footer)
- [ ] CTA is one clear action (not three)
- [ ] Caption draft included
- [ ] No "let's dive in", "game-changing", "leverage", "without further ado"
- [ ] Specific references over generic adjectives
- [ ] If prompt share: full prompt included, not truncated

---

## Example: Prompt Share Carousel

```
CAROUSEL: The Prompt Behind This Shot
TYPE: Prompt Share
PILLAR: AI Creatorship
PLATFORM: Instagram + LinkedIn
SLIDES: 7

---

SLIDE 1 — HOOK
This prompt took me 47 tries to get right

SLIDE 2 — TRANSITION
Most people copy prompts.
The ones who understand WHY each word is there
get 10x better results.

SLIDE 3 — THE PROMPT
Editorial portrait of a woman in layered silk fabrics,
Kodak Portra 800, golden hour sidelight,
shallow depth of field, film grain, 85mm lens,
slightly overexposed highlights
— shot by Annie Leibovitz for Vanity Fair

SLIDE 4 — BREAKDOWN
Why this works:

01 — "Annie Leibovitz for Vanity Fair"
Sets composition, lighting mood, and editorial framing in 5 words.

02 — "Kodak Portra 800"
Controls grain structure and color response. Velvia would give you different skin tones.

03 — "layered silk fabrics"
Gives the AI something to render light THROUGH. Texture + translucency = depth.

SLIDE 5 — THE RESULT
[IMAGE PLACEHOLDER]
The output speaks for itself.

SLIDE 6 — INSIGHT
Specific references beat generic adjectives.
"Annie Leibovitz for Vanity Fair" does more work
than "professional, high quality, stunning" ever will.

SLIDE 7 — CTA
Save this prompt.
Follow @michael.bul for prompts that teach you something.

---

CHROME:
Header: ● LANIAMEDA   AI CREATORSHIP
Footer: @michael.bul   ●●●●●●●
Optional: MIDJOURNEY V6.1

CAPTION DRAFT:
This prompt changed how I approach AI portraits.

Not because it's long — because every word has a job.
Film stock controls grain. Photographer reference sets composition.
Fabric choice gives the model something to render light through.

47 iterations to figure that out. Sharing so you don't have to.

Save this. Follow @michael.bul for more.

#AICreatorship #Midjourney #PromptEngineering #AIPhotography #CreativeAI #LaniAMeda
```
