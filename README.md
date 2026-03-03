# laniameda/skills

Agent skills for the laniameda ecosystem. Works with Claude Code, OpenClaw, Codex, Cursor, and 40+ other AI coding agents.

## Install

```bash
# Interactive — pick which skills + which agents
npx skills add Michailbul/laniameda-skills

# Install one skill to specific agents
npx skills add Michailbul/laniameda-skills --skill laniameda-brand-design -a claude-code -a openclaw

# Install everything, globally (home dir — all your projects)
npx skills add Michailbul/laniameda-skills --all --global

# Install everything, project-local (this repo only)
npx skills add Michailbul/laniameda-skills --all --local
```

## Update installed skills

```bash
npx skills update                               # update all skills from their lock sources
npx skills update Michailbul/laniameda-skills   # update only skills from this repo
```

Skills are **copied** on install. The `skills-lock.json` in your home dir tracks source + hash. Running `update` re-fetches from GitHub and replaces the local copy.

## Available skills

| Skill | What it does |
|-------|-------------|
| [`laniameda-brand-design`](./skills/laniameda-brand-design/SKILL.md) | Full laniameda design system + Pencil MCP workflow. Warm editorial + brutalist hybrid. Triggered by: "design a landing page", "follow the laniameda design system", "build a page in Pencil" |
| [`laniameda-kb`](./skills/laniameda-kb/SKILL.md) | Save prompts, images, and ideas to the laniameda.gallery Convex knowledge base. Auto-classifies into pillars (creators/cars/designs/dump) |
| [`laniameda-storage`](./skills/laniameda-storage/SKILL.md) | Save pillar-tagged prompts and reference assets into the Lania Meta Prompt Storage dashboard |
| [`andromeda-messages`](./skills/andromeda-messages/SKILL.md) | Add, update, delete, or list nodes in the Andromeda Galaxy page. Lock/unlock galaxies programmatically |
| [`carousel-designer`](./skills/carousel-designer/SKILL.md) | Generate branded LinkedIn carousel slides as a single HTML file + PDF export (Tailwind, 7 slides, 1080×1350px) |
| [`carousel-orchestrator`](./skills/carousel-orchestrator/SKILL.md) | Orchestrate the end-to-end carousel pipeline: brief → Codex generation → visual review → iteration → Telegram delivery |
| [`repo-kanban-pm`](./skills/repo-kanban-pm/SKILL.md) | Install a lightweight kanban PM workflow inside any repo: ROADMAP tracking, branch/PR conventions, optional daily PM cron |
| [`deepgram-transcribe`](./skills/deepgram-transcribe/SKILL.md) | Transcribe audio files (ogg, mp3, wav, m4a) via the Deepgram Nova-2 API |

## How skills work

Skills are `SKILL.md` files with YAML frontmatter (`name`, `description`) that your agent reads at the start of a session. The description controls **when** the skill loads — the agent pattern-matches your request against the description to decide which skills to pull into context.

```
skills/
└── my-skill/
    ├── SKILL.md          ← required (name + description frontmatter)
    ├── references/       ← loaded on demand (detailed docs, tokens, patterns)
    └── examples/         ← concrete code examples
```

## Manual install (no CLI)

```bash
# Claude Code (global)
cp -r skills/laniameda-brand-design ~/.claude/skills/

# OpenClaw (global)
cp -r skills/laniameda-brand-design ~/.openclaw/skills/

# Generic agents (global)
cp -r skills/laniameda-brand-design ~/.agents/skills/

# Project-local
cp -r skills/laniameda-brand-design ./.claude/skills/
```

## Adding a new skill

1. Create `skills/your-skill-name/SKILL.md` with frontmatter:
   ```yaml
   ---
   name: your-skill-name
   description: >-
     Describe exactly when this skill should trigger.
     Use phrases the user would actually say.
   ---
   ```
2. Add `references/` and `examples/` as needed
3. Commit and push
4. Run `npx skills update` on any machine where it's installed

---

Built by [Laniameda](https://github.com/Michailbul) · MIT
