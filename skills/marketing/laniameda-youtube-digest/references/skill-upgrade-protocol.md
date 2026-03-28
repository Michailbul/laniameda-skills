# Skill Upgrade Protocol

When a video teaches something worth encoding into studio skills, use this decision tree.

---

## Decision Tree

### 1. Does the video introduce a technique, rule, or finding that isn't already in our skills?

**Check relevant skill files first:**
- `nano-banana-pro/SKILL.md` — Nano Banana Pro prompting rules
- `crea-cinematic-prompts/SKILL.md` — cinematic direction formula
- `ai-video-prompting/SKILL.md` — video prompt construction
- `image-to-prompt/SKILL.md` — reference image → prompt extraction

Skills live in `~/.claude/skills/` (Mac) or `/root/.openclaw/workspace-crea/skills/` (VPS).

If the technique is already documented and the video adds nothing new → **KB only, no skill update needed.**

---

### 2. If new knowledge exists — what kind is it?

#### A) Refines an existing skill
The video adds a new rule, technique variant, model-specific finding, or negative result to something we already have a skill for.

**Action:**
1. Identify the exact section of the relevant SKILL.md to update
2. Draft the addition (new bullet, new table row, updated verdict)
3. Present the proposed change to Michael: *"I'd add this to [skill name] — approve?"*
4. On approval: write to the SKILL.md in laniameda-skills source, symlink picks it up

**Example:** Video shows that Kling v2.5 handles slow-motion prompts differently than v2.0 → patch `ai-video-prompting/SKILL.md`

#### B) Warrants a new skill
The video covers a domain or tool that has no existing skill, AND there's enough actionable depth to write useful instructions.

**Threshold for new skill — all three must be true:**
- The topic is clearly in scope for the studio (AI creatorship, agent workflows, design systems, etc.)
- The video provides at least 3 specific, actionable techniques/rules (not just tool overview)
- The studio would realistically use this in future sessions

**Action:**
1. Propose to Michael: skill name + one-line purpose + 2-3 bullet preview of what it would contain
2. On approval: use `skill-creator` to build it
3. New skill lives in: `~/work/laniameda/laniameda-hq/laniameda-skills/skills/<category>/<skill-name>/`
4. Run `install-skills.sh` to sync to `~/.agents/skills/` and `~/.claude/skills/`

#### C) Only useful as reference, not as agent instructions
The video teaches background knowledge (why a model works a certain way, history, comparisons) but not actionable rules to apply during a session.

**Action:** Save to KB only. Optionally update `MEMORY.md` if it's model landscape knowledge worth remembering long-term.

---

## What goes in SKILL.md vs references/ vs KB

| Content type | Where it goes |
|---|---|
| Agent instructions — what to do, when, how | `SKILL.md` body |
| Technique tables, model-specific rules, prompt templates | `references/<topic>.md` inside skill folder |
| Raw extracted content from a specific video | `content-kb/sources/youtube/` |
| Long-term model/tool verdicts | `MEMORY.md` |
| One-off prompts worth keeping | `laniameda-gallery-ingest` → gallery vault |

---

## Skill source of truth

All laniameda skills live in:
```
~/work/laniameda/laniameda-hq/laniameda-skills/skills/<category>/<skill-name>/
```

Install/sync:
```bash
cd ~/work/laniameda/laniameda-hq/laniameda-skills
./install-skills.sh
```

When updating a skill: always edit the source in laniameda-hq. Never edit the symlink target directly. Always `git add -A && git commit && git push` after changes.

---

## Approval gate (non-negotiable)

**Always ask Michael before:**
- Writing to any SKILL.md
- Creating a new skill folder
- Updating MEMORY.md with model verdicts

**Never ask for approval to:**
- Save to content-kb (that's automatic)
- Read existing skill files to check for overlap
