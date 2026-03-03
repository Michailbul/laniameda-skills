# Landing Page Section Examples

Concrete batch_design operations for building each section of a laniameda landing page.

---

## Screen Frame

Create the main screen frame first:

```javascript
screen=I(document, {
  type: "frame",
  name: "Landing Page",
  layout: "vertical",
  width: 1200,
  height: "fit_content",
  fill: "#fffaf5"
})
```

---

## 1. Hero Section

The most important section — eyebrow, headline, sub, CTA, and terminal preview.

```javascript
// Hero container
hero=I(screen, {
  type: "frame",
  layout: "vertical",
  gap: 32,
  padding: [80, 64, 80, 64],
  width: "fill_container",
  height: "fit_content",
  fill: "#fffaf5"
})

// Eyebrow label
eyebrow=I(hero, { type: "ref", ref: "sectionLabelId" })
U(eyebrow+"/labelTextId", { content: "// v0.2.0 · Open Source · MIT" })

// Main headline (Inter 800)
headline=I(hero, {
  type: "text",
  content: "Your agents are only as good as their context.",
  fontSize: 56,
  fontWeight: "800",
  fontFamily: "Inter",
  fill: "#201710",
  letterSpacing: -0.04,
  lineHeight: 1.1,
  width: 700
})

// Subheadline
sub=I(hero, {
  type: "text",
  content: "Self-hosted editor for the files that make your AI agents smart.",
  fontSize: 18,
  fontFamily: "Inter",
  fontWeight: "400",
  fill: "#4c3a2d",
  lineHeight: 1.6,
  width: 600
})

// CTA row
ctaRow=I(hero, {
  type: "frame",
  layout: "horizontal",
  gap: 16,
  alignItems: "center"
})
cta=I(ctaRow, { type: "ref", ref: "ctaPillId" })
ghost=I(ctaRow, { type: "ref", ref: "ghostBtnId" })
U(ghost+"/labelId", { content: "View on GitHub →" })
```

### Hero Terminal Block

Add a terminal window next to or below the headline:

```javascript
// Terminal with install output
terminal=I(hero, { type: "ref", ref: "macWindowId", width: 560 })
U(terminal+"/titleId", { content: "terminal" })

// Terminal content (dark bg code lines)
line1=I(terminal+"/bodyId", {
  type: "text",
  content: "$ npx @laniameda/agent-hub",
  fontFamily: "JetBrains Mono",
  fontSize: 13,
  fill: "#e0e0e0"
})
line2=I(terminal+"/bodyId", {
  type: "text",
  content: "✓ Found: Persey ⚙️  (CTO)",
  fontFamily: "JetBrains Mono",
  fontSize: 13,
  fill: "#27c93f"
})
line3=I(terminal+"/bodyId", {
  type: "text",
  content: "→ 42 skills loaded",
  fontFamily: "JetBrains Mono",
  fontSize: 13,
  fill: "#ff7a64"
})
```

---

## 2. Problems Section

Three pain points — works with brutalist or soft cards.

```javascript
// Section container
problems=I(screen, {
  type: "frame",
  layout: "vertical",
  gap: 32,
  padding: [64, 64, 64, 64],
  width: "fill_container",
  height: "fit_content",
  fill: "#fff4ea"
})

// Section label
plabel=I(problems, { type: "ref", ref: "sectionLabelId" })
U(plabel+"/labelTextId", { content: "// problems" })

// Section heading
pheading=I(problems, {
  type: "text",
  content: "Agent context is a mess.",
  fontSize: 36,
  fontWeight: "800",
  fontFamily: "Inter",
  fill: "#201710"
})

// Card grid (3 columns)
pgrid=I(problems, {
  type: "frame",
  layout: "horizontal",
  gap: 20,
  wrap: true,
  width: "fill_container"
})

// Problem cards
p1=I(pgrid, { type: "ref", ref: "brutalCardId", width: 350 })
U(p1+"/iconId", { content: "📁" })
U(p1+"/titleId", { content: "Files scattered everywhere" })
U(p1+"/descId", { content: "SOUL.md in one dir, skills in another, MEMORY.md somewhere else." })

p2=I(pgrid, { type: "ref", ref: "brutalCardId", width: 350 })
U(p2+"/iconId", { content: "🔧" })
U(p2+"/titleId", { content: "Wrong tool for the job" })
U(p2+"/descId", { content: "Editing agent personalities in VS Code. These aren't code files." })

p3=I(pgrid, { type: "ref", ref: "brutalCardId", width: 350 })
U(p3+"/iconId", { content: "🌀" })
U(p3+"/titleId", { content: "No overview of capabilities" })
U(p3+"/descId", { content: "Which agent has which skills? Nobody knows without digging." })
```

---

## 3. Features Section

8-item grid — 2x4 layout with feature cards.

```javascript
// Section
features=I(screen, {
  type: "frame",
  layout: "vertical",
  gap: 32,
  padding: [64, 64, 64, 64],
  width: "fill_container",
  height: "fit_content",
  fill: "#fffaf5"
})

flabel=I(features, { type: "ref", ref: "sectionLabelId" })
U(flabel+"/labelTextId", { content: "// features" })

fheading=I(features, {
  type: "text",
  content: "Everything you need. Nothing you don't.",
  fontSize: 36,
  fontWeight: "800",
  fontFamily: "Inter",
  fill: "#201710"
})

// 2-column grid
fgrid=I(features, {
  type: "frame",
  layout: "horizontal",
  gap: 16,
  wrap: true,
  width: "fill_container"
})

// Feature cards (repeat pattern for all 8)
f1=I(fgrid, { type: "ref", ref: "brutalCardId", width: 530 })
U(f1+"/iconId", { content: "⬜" })
U(f1+"/titleId", { content: "Multi-pane editor" })
U(f1+"/descId", { content: "VSCode-style up to 4 panes. Compare agent files side by side." })

// ... repeat for f2-f8 with FEATURES content from content.ts
```

---

## 4. Setup Section

Tabbed terminal blocks showing Install / Configure / Docker.

```javascript
// Section (dark variant for contrast)
setup=I(screen, {
  type: "frame",
  layout: "vertical",
  gap: 32,
  padding: [64, 64, 64, 64],
  width: "fill_container",
  height: "fit_content",
  fill: "#0f0f0f"
})

slabel=I(setup, {
  type: "text",
  content: "// setup",
  fontSize: 11,
  fontFamily: "JetBrains Mono",
  fontWeight: "500",
  fill: "#ff7a64",
  letterSpacing: 0.12
})

sheading=I(setup, {
  type: "text",
  content: "One command. That's it.",
  fontSize: 36,
  fontWeight: "800",
  fontFamily: "Inter",
  fill: "#fafafa"
})

// Tab labels
tabs=I(setup, {
  type: "frame",
  layout: "horizontal",
  gap: 8
})
tab1=I(tabs, { type: "ref", ref: "badgeCoralId" })
U(tab1+"/labelId", { content: "INSTALL" })
tab2=I(tabs, { type: "ref", ref: "badgeInkId" })
U(tab2+"/labelId", { content: "CONFIGURE" })
tab3=I(tabs, { type: "ref", ref: "badgeInkId" })
U(tab3+"/labelId", { content: "DOCKER" })

// Terminal window with install content
sterminal=I(setup, { type: "ref", ref: "macWindowId", width: "fill_container" })
U(sterminal+"/titleId", { content: "terminal" })
// Add code content to terminal body...
```

---

## 5. Compatibility Section

Badge grid showing supported frameworks and platforms.

```javascript
compat=I(screen, {
  type: "frame",
  layout: "vertical",
  gap: 24,
  padding: [48, 64, 48, 64],
  width: "fill_container",
  fill: "#f7ede2"
})

clabel=I(compat, { type: "ref", ref: "sectionLabelId" })
U(clabel+"/labelTextId", { content: "// compatible" })

// Agent badges row
agentRow=I(compat, {
  type: "frame",
  layout: "horizontal",
  gap: 8,
  wrap: true
})
a1=I(agentRow, { type: "ref", ref: "badgeInkId" })
U(a1+"/labelId", { content: "OPENCLAW" })
a2=I(agentRow, { type: "ref", ref: "badgeInkId" })
U(a2+"/labelId", { content: "CLAUDE CODE" })
// ... more badges

// Platform badges row
platRow=I(compat, {
  type: "frame",
  layout: "horizontal",
  gap: 8,
  wrap: true
})
// ... platform badges
```

---

## 6. FAQ Section

Accordion-style questions with coral left border.

```javascript
faq=I(screen, {
  type: "frame",
  layout: "vertical",
  gap: 24,
  padding: [64, 64, 64, 64],
  width: "fill_container",
  fill: "#fffaf5"
})

fqlabel=I(faq, { type: "ref", ref: "sectionLabelId" })
U(fqlabel+"/labelTextId", { content: "// faq" })

fqheading=I(faq, {
  type: "text",
  content: "Common questions.",
  fontSize: 36,
  fontWeight: "800",
  fontFamily: "Inter",
  fill: "#201710"
})

// FAQ item (repeat for each Q&A)
q1=I(faq, {
  type: "frame",
  layout: "vertical",
  gap: 8,
  padding: [16, 0, 16, 20],
  width: "fill_container",
  strokeLeft: 3,
  stroke: "#ff7a64"
})
q1title=I(q1, {
  type: "text",
  content: "What agent frameworks does it support?",
  fontSize: 16,
  fontWeight: "600",
  fontFamily: "Inter",
  fill: "#201710"
})
q1answer=I(q1, {
  type: "text",
  content: "Any markdown-based agent setup. Works with OpenClaw, Claude Code, Codex...",
  fontSize: 14,
  fontFamily: "Inter",
  fill: "#4c3a2d",
  lineHeight: 1.6,
  width: "fill_container"
})
```

---

## 7. Footer

Minimal footer with brand and links.

```javascript
footer=I(screen, {
  type: "frame",
  layout: "horizontal",
  justifyContent: "space-between",
  alignItems: "center",
  padding: [32, 64, 32, 64],
  width: "fill_container",
  fill: "#f7ede2"
})

brand=I(footer, {
  type: "text",
  content: "laniameda",
  fontSize: 14,
  fontFamily: "Playfair Display",
  fontStyle: "italic",
  fill: "#201710"
})

links=I(footer, {
  type: "frame",
  layout: "horizontal",
  gap: 24
})
link1=I(links, {
  type: "text",
  content: "GitHub",
  fontSize: 12,
  fontFamily: "JetBrains Mono",
  fill: "#7d6755"
})
link2=I(links, {
  type: "text",
  content: "Demo",
  fontSize: 12,
  fontFamily: "JetBrains Mono",
  fill: "#7d6755"
})
link3=I(links, {
  type: "text",
  content: "MIT License",
  fontSize: 12,
  fontFamily: "JetBrains Mono",
  fill: "#7d6755"
})
```

---

## Full-Bleed Dark Section Pattern

For dramatic chapter breaks (Paper Press style):

```javascript
darkSection=I(screen, {
  type: "frame",
  layout: "vertical",
  gap: 32,
  padding: [80, 64, 80, 64],
  width: "fill_container",
  fill: "#201710"
})
// All text inside uses fill: "#fafafa" or "#e0e0e0"
// Section labels use fill: "#ff7a64" (coral pops on dark)
```

## Spotlight CTA Pattern (Window Stack style)

A search-bar-style CTA that mimics macOS Spotlight:

```javascript
spotlight=I(screen, {
  type: "frame",
  layout: "horizontal",
  gap: 0,
  alignItems: "center",
  padding: [0, 0, 0, 24],
  width: 600,
  height: 56,
  fill: "#ffffff",
  cornerRadius: 9999,
  stroke: "rgba(32,23,16,0.16)",
  shadow: "0 4px 12px rgba(32,23,16,0.08)"
})
prompt=I(spotlight, {
  type: "text",
  content: "npx @laniameda/agent-hub",
  fontSize: 15,
  fontFamily: "JetBrains Mono",
  fill: "#7d6755",
  width: "fill_container"
})
runBtn=I(spotlight, {
  type: "frame",
  layout: "horizontal",
  alignItems: "center",
  justifyContent: "center",
  padding: [12, 24, 12, 24],
  fill: "#ff7a64",
  cornerRadius: 9999,
  height: "fill_container"
})
runLabel=I(runBtn, {
  type: "text",
  content: "RUN",
  fontSize: 12,
  fontFamily: "JetBrains Mono",
  fontWeight: "700",
  fill: "#ffffff",
  letterSpacing: 0.12
})
```
