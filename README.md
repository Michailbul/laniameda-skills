# laniameda/skills

Agent skills for the laniameda brand and design system. Works with Claude Code, OpenClaw, Codex, Cursor, and 40+ other AI coding agents.

## Install

```bash
# Install all skills (interactive — picks agents + scope)
npx skills add Michailbul/laniameda-skills

# Install a specific skill
npx skills add Michailbul/laniameda-skills --skill laniameda-brand-design

# Install to specific agents
npx skills add Michailbul/laniameda-skills --skill laniameda-brand-design -a claude-code -a openclaw

# Install globally (all your projects)
npx skills add Michailbul/laniameda-skills --global

# Install project-local (this repo only)
npx skills add Michailbul/laniameda-skills --local
```

## Available Skills

| Skill | Description |
|-------|-------------|
| [`laniameda-brand-design`](./skills/laniameda-brand-design/SKILL.md) | Full laniameda design system + Pencil MCP workflow for building landing pages. Warm editorial + brutalist hybrid. |

## What is a skill?

Skills are reusable instruction sets that extend your AI coding agent's capabilities. They load into your agent's context when you ask for something relevant — like "design a landing page" or "follow the laniameda design system".

Each skill is a `SKILL.md` file with YAML frontmatter and markdown instructions, plus optional `references/` and `examples/` folders for progressive context loading.

## Manual install

If you prefer not to use the CLI, copy any skill folder into your agent's skills directory:

```bash
# Claude Code (global)
cp -r skills/laniameda-brand-design ~/.claude/skills/

# Claude Code (project)
cp -r skills/laniameda-brand-design .claude/skills/

# OpenClaw
cp -r skills/laniameda-brand-design ~/.openclaw/skills/

# Generic agents
cp -r skills/laniameda-brand-design ~/.agents/skills/
```

## Design system

The `laniameda-brand-design` skill encodes the full laniameda visual identity:

- **Colors** — warm paper stack (`#fffaf5`), volcanic ink (`#201710`), ember coral (`#ff7a64`)
- **Typography** — Instrument Serif (display, italic), Geist Sans (body), Geist Mono (labels/code)
- **Shadows** — dual system: soft editorial + brutalist offset (`4px 4px 0 #201710`)
- **Components** — macOS window chrome, CTA pill, brutalist/soft cards, badges, section labels
- **Workflow** — full Pencil MCP design tool patterns for building marketing pages

Triggering phrases: _"design a landing page"_, _"follow the laniameda design system"_, _"build a page in Pencil"_, _"use our brand colors"_

---

Built by [Laniameda](https://github.com/Michailbul) · MIT
