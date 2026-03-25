---
name: carousel-creator
description: Design and produce high-engagement social media carousels as HTML slides rendered to images. No external CLI dependencies. Uses local HTML rendering + canvas/browser screenshot tooling. Baked-in laniameda positioning rules for creative brand audiences.
---

# Carousel Creator

Produce publish-ready social media carousel slides as rendered images from HTML. No external services. No inference.sh dependency.

## Stack
- **HTML/CSS per slide** → rendered to image via `ocscreenshot` or browser screenshot tooling available on this VPS
- **Dimensions** → 1080×1350px (4:5, Instagram/LinkedIn default; takes more feed real estate than square)
- **Output** → PNG per slide, numbered `slide_01.png`, `slide_02.png`, etc.
- **Delivery** → send to Michael via Telegram file upload (never just report the path)

## Platform Specs

| Platform   | Dimensions          | Slides  | Best Ratio |
|------------|---------------------|---------|------------|
| Instagram  | 1080×1350px         | Up to 20 | 4:5 ✅    |
| LinkedIn   | 1080×1350px         | Up to 20 | 4:5 ✅    |
| Twitter/X  | 1080×1080px         | Up to 4  | 1:1        |
| Facebook   | 1080×1350px         | Up to 10 | 4:5 ✅    |

Default to **1080×1350** (4:5) unless X-only is explicitly requested.

---

## Rendering Method

### Primary: ocscreenshot

```bash
# Render a single slide HTML file to PNG
ocscreenshot --width 1080 --height 1350 --output slide_01.png slide_01.html
```

### Fallback: Python + Playwright/Chrome headless

```python
import subprocess

def render_slide(html_path, out_path, width=1080, height=1350):
    subprocess.run([
        'chromium-browser', '--headless=new',
        '--disable-gpu',
        '--no-sandbox',
        f'--screenshot={out_path}',
        f'--window-size={width},{height}',
        html_path
    ], check=True)
```

### Fallback 2: browser tool (screenshot action)

If running inside an OpenClaw session with browser tool access:
- Open the HTML file in browser
- Use `browser(action="screenshot", fullPage=False)` at 1080×1350 viewport

---

## Carousel Structure

### Standard 7-Slide Framework

| Slide | Purpose | Goal |
|-------|---------|------|
| 1 | Hook | Stop the scroll |
| 2 | Context | Set up the problem/promise |
| 3–6 | Value | One point per slide |
| 7 | CTA | Save / follow / share |

### Minimum viable: 5 slides
Hook → Context → 2 value slides → CTA

### Maximum engagement: 8–10 slides
Use only if topic genuinely needs depth. Every slide must earn its place.

---

## laniameda Positioning Rules (Non-Negotiable)

These apply to all carousels unless Michael explicitly overrides:

### Audience
**Creative brands and creative studios.** Not engineers. Not enterprise buyers.
People who think in campaigns, content calendars, and creative output — not runtimes.

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

---

## Slide Templates

### Slide 1 — Hook

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    width: 1080px; height: 1350px; overflow: hidden;
    background: linear-gradient(160deg, #0f0f0f 0%, #1a1a1a 100%);
    display: flex; align-items: center; justify-content: center;
    padding: 80px;
    font-family: 'Inter', system-ui, -apple-system, sans-serif;
  }
  .inner { text-align: center; max-width: 900px; }
  .eyebrow {
    font-size: 22px; font-weight: 500; color: #888;
    text-transform: uppercase; letter-spacing: 4px; margin-bottom: 32px;
  }
  h1 {
    font-size: 72px; font-weight: 900; color: #fff;
    line-height: 1.1; margin-bottom: 40px;
  }
  h1 em { color: [ACCENT_COLOR]; font-style: normal; }
  .swipe {
    font-size: 22px; color: #555; letter-spacing: 2px;
    text-transform: uppercase;
  }
</style>
</head>
<body>
  <div class="inner">
    <p class="eyebrow">[TOPIC TAG]</p>
    <h1>[HOOK HEADLINE with <em>accent word</em>]</h1>
    <p class="swipe">Swipe →</p>
  </div>
</body>
</html>
```

### Slide 2–6 — Content Slide

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    width: 1080px; height: 1350px; overflow: hidden;
    background: #111;
    padding: 80px;
    font-family: 'Inter', system-ui, -apple-system, sans-serif;
    display: flex; flex-direction: column; justify-content: center;
  }
  .slide-num {
    font-size: 120px; font-weight: 900;
    color: [ACCENT_COLOR]; opacity: 0.15;
    line-height: 1; margin-bottom: 24px;
  }
  h2 {
    font-size: 52px; font-weight: 800; color: #fff;
    line-height: 1.15; margin-bottom: 28px;
  }
  p {
    font-size: 28px; color: #aaa;
    line-height: 1.6; max-width: 880px;
  }
  p em { color: #fff; font-style: normal; }
</style>
</head>
<body>
  <div class="slide-num">0[N]</div>
  <h2>[SLIDE HEADING]</h2>
  <p>[Body copy. Max 30–40 words. One idea only. Use <em>emphasis</em> for the key phrase.]</p>
</body>
</html>
```

### Slide 7 — CTA

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    width: 1080px; height: 1350px; overflow: hidden;
    background: linear-gradient(160deg, #0f0f0f 0%, #1a1a1a 100%);
    display: flex; align-items: center; justify-content: center;
    padding: 80px;
    font-family: 'Inter', system-ui, -apple-system, sans-serif;
  }
  .inner { text-align: center; max-width: 900px; }
  h2 {
    font-size: 60px; font-weight: 900; color: #fff;
    line-height: 1.15; margin-bottom: 32px;
  }
  .actions {
    font-size: 28px; color: #888;
    line-height: 1.8; margin-bottom: 56px;
  }
  .handle { font-size: 24px; color: #444; letter-spacing: 2px; }
</style>
</head>
<body>
  <div class="inner">
    <h2>[CTA HEADLINE — what they get from following/saving]</h2>
    <p class="actions">
      Save this post 🔖<br>
      Follow for more →
    </p>
    <p class="handle">@[HANDLE]</p>
  </div>
</body>
</html>
```

---

## Design System

### Typography Scale (at 1080px width)

| Element | Size | Weight |
|---------|------|--------|
| Slide number (decorative) | 96–120px | 900 |
| Hook headline | 64–80px | 900 |
| Content heading | 48–60px | 800 |
| Body text | 26–30px | 400 |
| Eyebrow / caption | 18–22px | 500 |

### Readability Rules

| Rule | Value |
|------|-------|
| Max words per slide | 30–40 |
| Max body lines | 4–5 |
| Line height | 1.5–1.6 |
| Font | Inter, Montserrat, or system-ui |
| Text contrast | 4.5:1 minimum (WCAG AA) |

### Consistency Rules (all slides must share)
- Same background palette (exact hex, slight gradient variation OK)
- Same font family
- Same text alignment (left or center, not mixed)
- Same padding/margin (80px safe zone)
- Same accent color
- Same numbering format (01, 02, 03)

---

## Accent Color Palette Presets

| Mood | Background | Accent | Body text |
|------|-----------|--------|-----------|
| Dark premium | `#0f0f0f` | `#c8ff57` (lime) | `#aaa` |
| Dark electric | `#0a0a0a` | `#7c6ef5` (purple) | `#999` |
| Dark warm | `#111` | `#ff6b35` (orange) | `#bbb` |
| Dark editorial | `#0d0d0d` | `#e8d5b7` (cream) | `#888` |
| Light editorial | `#f5f3f0` | `#1a1a1a` | `#555` |

Default: **dark premium** unless brand direction is specified.

---

## Hook Types Quick Reference

| Type | Formula | Example |
|------|---------|---------|
| Bold claim | "[X]% of [audience] [painful truth]" | "90% of content strategies skip this" |
| Question | "Why does [common thing] [not work]?" | "Why does posting daily still not grow you?" |
| Number + promise | "[N] [things] you [outcome verb]" | "5 tools that replaced my whole production team" |
| Contrarian | "Stop doing [popular thing]. Do [this]." | "Stop making content. Build a content engine." |
| Before/After | State the transformation in one line | "I went from 3 posts/month to 30 posts/week — same effort" |

---

## Carousel Type Templates

### Educational / Tips
```
Slide 1: Bold claim hook
Slide 2: Why this matters (context)
Slides 3–6: One tip each, numbered
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
Slide 3: Problem 1 — what made it broken
Slide 4: The "after" state
Slide 5: What changed + why it worked
Slide 6: Result proof
Slide 7: Offer to help / CTA
```

### Tools / Listicle
```
Slide 1: Number hook ("7 tools that changed how I create")
Slide 2: Context — why tools matter / what was missing
Slides 3–6: 1–2 tools per slide, name + one-liner use case
Slide 7: Save + follow CTA
```

---

## Swipe Psychology (bake into slide design)

| Principle | How to apply |
|-----------|-------------|
| Curiosity gap | Hook promises value that requires swiping to unlock |
| Numbered progress | Show "3/7" in corner or progress dots to create completion drive |
| Visual continuity | Consistent design signals "there's more" |
| Increasing value | Best insight last — rewards completing the whole carousel |
| Swipe cue | Arrow or "Swipe →" text on slide 1 |

---

## Workflow

### Step 1: Brief
Collect from Michael or extract from source material:
- Topic / angle
- Platform (default: Instagram + LinkedIn)
- Number of slides (default: 7)
- Carousel type (tips / story / before-after / listicle)
- Any brand color preference (default: dark premium preset)
- Handle / watermark

### Step 2: Copy
Write all slide copy first. Get it tight before building HTML.
Apply laniameda positioning rules:
- outcome-first
- creative brand language
- max 30–40 words per slide

### Step 3: Build HTML files
One `.html` file per slide. Name: `slide_01.html`, `slide_02.html`, etc.
Use templates above. Swap in copy.

### Step 4: Render to PNG
```bash
# Primary method
for i in $(seq -w 1 7); do
  ocscreenshot --width 1080 --height 1350 --output slide_${i}.png slide_${i}.html
done
```

### Step 5: Deliver
- Send all PNGs to Michael via Telegram file uploads (message tool with filePath)
- Also send copy doc separately if useful

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Weak hook | Lead with bold claim, number, or transformation — not a soft question |
| Too much text per slide | Max 30–40 words, hard limit |
| No visual consistency | Same color + font system across all slides |
| No swipe indicator on slide 1 | Always include "Swipe →" |
| No CTA on last slide | Ask for save, follow, or share |
| Cramming 2+ ideas per slide | One point only, always |
| Square format on Instagram | Default to 1080×1350 (4:5) |
| Leading with technical language | Lead with outcome; audience is creative brands |

---

## Anti-Patterns (laniameda specific)

- Do not lead with "AI tools can help you..." — that's a commodity angle
- Do not use "leverage AI to..." — weak and overused
- Do not explain the tech before explaining the outcome
- Do not let the tool be the hero — the creator's output/life is the hero
