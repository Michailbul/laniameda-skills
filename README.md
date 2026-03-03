# @laniameda/skills

Private agent skills for the Laniameda ecosystem. Install to Claude Code, OpenClaw, Codex, Cursor, and 40+ AI coding agents.

```bash
npx skills add Michailbul/laniameda-skills
```

---

## Install

```bash
# Interactive — pick skills + agents + scope
npx skills add Michailbul/laniameda-skills

# Everything, everywhere, globally
npx skills add Michailbul/laniameda-skills --all --global

# One skill, specific agents
npx skills add Michailbul/laniameda-skills --skill laniameda-brand-design -a claude-code -a openclaw

# Project-local only (.claude/skills/, .agents/skills/ in cwd)
npx skills add Michailbul/laniameda-skills --all --local

# List what's available without installing
npx skills add Michailbul/laniameda-skills --list
```

## Update

Skills are **copied** on install. The `~/skills-lock.json` tracks source + hash per skill. To pull latest:

```bash
npx skills update                               # all skills from all sources
npx skills update Michailbul/laniameda-skills   # just this repo
```

**Workflow**: edit SKILL.md → `git push` → `npx skills update` on each machine.

---

## Skills

### Design & Brand

| Skill | Triggers | What it does |
|-------|----------|-------------|
| **[laniameda-brand-design](./skills/laniameda-brand-design/)** | "design a landing page", "follow the laniameda design system", "build a page in Pencil", "use our brand colors" | Full laniameda design system (colors, typography, shadows, components) + Pencil MCP workflow for building marketing pages. Warm editorial + brutalist hybrid aesthetic. |

### Content & Knowledge

| Skill | Triggers | What it does |
|-------|----------|-------------|
| **[laniameda-kb](./skills/laniameda-kb/)** | "save this", "store this", "add to KB", "save to vault" | Save prompts, images, tutorials, links, and ideas to the laniameda.gallery Convex knowledge base. Auto-classifies into pillars (creators / cars / designs / dump). |
| **[laniameda-storage](./skills/laniameda-storage/)** | "save this", "store this", "add to vault", shares a prompt or reference media | Save pillar-tagged prompts + reference assets from Instagram or any source into the Lania Meta Prompt Storage dashboard (Convex KB). |

### Social Media & Carousels

| Skill | Triggers | What it does |
|-------|----------|-------------|
| **[carousel-designer](./skills/carousel-designer/)** | "build a carousel", "generate slides", "LinkedIn carousel" | Generate branded LinkedIn carousel slides as a single HTML file (Tailwind, 1080x1350px, 7 slides) + PDF/PNG export via Playwright. |
| **[carousel-orchestrator](./skills/carousel-orchestrator/)** | "create a LinkedIn carousel", "generate branded slides" | End-to-end carousel pipeline: parse request → brief Codex → visual review → iteration feedback → deliver PDF via Telegram. |

### Personal & Utility

| Skill | Triggers | What it does |
|-------|----------|-------------|
| **[andromeda-messages](./skills/andromeda-messages/)** | "add to andromeda", "save to galaxy", "add to dreams", "unlock your life" | CRUD for the Andromeda Galaxy page (mishabuloichyk.com). Add/edit/delete nodes across galaxies (Dreams, Life, Partner, Family, Antidreams). Lock/unlock galaxies. |
| **[deepgram-transcribe](./skills/deepgram-transcribe/)** | sends a voice message, "transcribe this audio" | Transcribe audio files (ogg, mp3, wav, m4a, webm) using the Deepgram Nova-2 API. |

### Developer Workflow

| Skill | Triggers | What it does |
|-------|----------|-------------|
| **[repo-kanban-pm](./skills/repo-kanban-pm/)** | starting a new project, "set up kanban", "add PM workflow" | Install a lightweight product-management workflow inside any repo: feature kanban boards, ROADMAP status tracking, branch/PR conventions, optional daily OpenClaw cron PM review. |

---

## Design System

The repo also ships a portable **design system export** in [`design-system/`](./design-system/):

```bash
# Drop into any project
cp -r design-system/ your-project/design-system/
```

Then in your CSS:
```css
@import "./design-system/tokens.css";
```

**What's inside:**

| File | Purpose |
|------|---------|
| `tokens.css` | Drop-in CSS custom properties (all colors, type, shadows, timing) |
| `brand.md` | Voice, tone, audience, design principles |
| `colors.md` | Paper stack, ink scale, 12-step coral ramp, terminal colors |
| `typography.md` | 3 font families, 7-tier scale, weights, letter spacing |
| `shadows-elevation.md` | Dual shadow system (soft editorial + brutalist offset) |
| `spacing-layout.md` | 4px base spacing, radius scale, grid, breakpoints |
| `components.md` | Buttons, cards, badges, window chrome, tags, nav patterns |
| `motion.md` | Animation tokens, easing curves, transition patterns |

### Brand at a glance

| Element | Value |
|---------|-------|
| Background | `#fffaf5` (warm parchment) |
| Text | `#201710` (volcanic ink) |
| Accent | `#ff7a64` (ember coral — use sparingly) |
| Display font | Instrument Serif italic |
| Body font | Geist Sans |
| Label font | Geist Mono (uppercase, tracked) |
| Brutalist shadow | `4px 4px 0 #201710` (never blur) |
| Button shape | Pill (always) |
| Base radius | 20px |

---

## How skills work

A skill is a `SKILL.md` file with YAML frontmatter that your AI agent reads at session start. The `description` field controls **when** the skill activates — the agent pattern-matches your request against it.

```
skills/
└── my-skill/
    ├── SKILL.md          ← required (name + description)
    ├── references/       ← loaded on demand (detailed docs)
    ├── examples/         ← code examples
    ├── scripts/          ← executable utilities
    └── assets/           ← templates, images, fonts
```

### Where skills get installed

The `npx skills` CLI copies files to agent-specific directories:

| Agent | Global path | Project path |
|-------|-------------|-------------|
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |
| OpenClaw | `~/.openclaw/skills/` | `.openclaw/skills/` |
| Generic agents | `~/.agents/skills/` | `.agents/skills/` |
| Codex, Cursor, etc. | Symlinked from `~/.agents/skills/` | — |

### Manual install (no CLI)

```bash
# Clone and copy specific skills
git clone https://github.com/Michailbul/laniameda-skills.git /tmp/laniameda-skills

# Copy to all agent dirs
for dir in ~/.claude/skills ~/.openclaw/skills ~/.agents/skills; do
  cp -r /tmp/laniameda-skills/skills/laniameda-brand-design "$dir/"
done
```

---

## Adding a new skill

1. Create `skills/your-skill/SKILL.md`:
   ```yaml
   ---
   name: your-skill
   description: >-
     What triggers this skill. Use phrases users would actually say.
     "save this", "do that", "build X".
   ---

   # Your Skill

   Instructions for the agent here...
   ```

2. Add optional `references/`, `examples/`, `scripts/` dirs

3. Commit and push:
   ```bash
   git add skills/your-skill && git commit -m "feat: add your-skill" && git push
   ```

4. On any machine: `npx skills update Michailbul/laniameda-skills`

---

## Third-party skills we use

These are NOT in this repo — install separately:

```bash
# Marketing (32 skills — CRO, SEO, copywriting, growth)
npx skills add coreyhaines31/marketingskills --all --global

# Behavioral product design
npx skills add refoundai/lenny-skills --all --global
```

---

Built by [Laniameda](https://github.com/Michailbul)
