# AGENTS.md — Skills Changelog & Agent Actions

This file tracks skill changes that agents need to act on: new skills to install, deprecated skills to remove, updates to sync.

**Every agent reads this file at session start.**
**Every agent updates this file when they add, remove, or change a skill.**

---

## How to Update This File

When you make a skill change, add an entry under the relevant section:

- **Added** — new skill created, list which agents should install it
- **Updated** — existing skill changed, list what changed
- **Deprecated** — skill superseded, list what replaces it and which agents should remove it
- **Removed** — skill deleted from repo, agents must manually delete from their workspace

Format:
```
### YYYY-MM-DD — <skill-name>
**Change:** Added / Updated / Deprecated / Removed
**Agents:** [Lani, Meda, ...] or "all"
**Action:** what the agent needs to do
**Notes:** any context
```

---

## Pending Agent Actions

> Agents: check this section every session. Do the action, then move the entry to the changelog below.

_Nothing pending._

---

## Special Rules

### laniameda-kb — canonical source is laniameda.gallery repo
**NOT** managed in this package. Canonical skill lives at:
`~/work/laniameda/laniameda.gallery/skills/laniameda-kb/SKILL.md`

When the gallery ingest contract changes, the skill is updated there and pushed to agent workspaces via:
```bash
cd ~/work/laniameda/laniameda.gallery && git pull && bun run skills:update
```

Installed agents: Lani, Meda, Crea (symlinked from `/root/.agents/skills/laniameda-kb`)

---

## Changelog

### 2026-03-25 — instagram-extract
**Change:** Deprecated + removed from workspaces  
**Agents:** Lani, Meda — removed  
**Replaced by:** `laniameda-instagram-carousel-extract` + `laniameda-instagram-reel-digest` (installed)

### 2026-03-25 — youtube-digest (old)
**Change:** Deprecated + removed from workspaces  
**Agents:** Lani, Meda — removed  
**Replaced by:** `laniameda-youtube-digest` (installed)



### 2026-03-25 — laniameda-skills reorganization
**Change:** Structural refactor  
**Summary:**
- All skills consolidated into `laniameda-skills/skills/` (single source of truth)
- Top-level duplicate `skills/` folder removed from laniameda-hq
- Submodule moved from `skills/laniameda-skills` → `laniameda-skills/`
- 9 skills had missing `description:` frontmatter — fixed (skills were silently skipped by `npx skills`)
- `skill-creator` updated with hard rule: `description:` is always required

### 2026-03-25 — laniameda-instagram-carousel-extract
**Change:** Added  
**Agents:** Lani, Meda  
**Replaces:** instagram-extract (for carousel posts)

### 2026-03-25 — laniameda-instagram-reel-digest
**Change:** Added  
**Agents:** Lani, Meda  
**Replaces:** instagram-extract (for reels/video)

### 2026-03-25 — laniameda-youtube-digest (v2)
**Change:** Added (v2 replaces old youtube-digest)  
**Agents:** Lani, Meda
