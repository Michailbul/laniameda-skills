---
name: sync-plugin-skills
description: >
  Sync skills from the laniameda-skills GitHub repo into the Cowork plugin. Use when Michael says
  "update the plugin", "sync the skills", "pull latest skills", "update plugin from GitHub", or
  "rebuild the plugin". This skill pulls the latest from github.com/Michailbul/laniameda-skills
  and rebuilds the laniameda AI creatorship .plugin file so Cowork picks up the changes.
version: 1.0.0
status: active
created: 2026-04-12
updated: 2026-04-12
owner: Claude
agents: [Claude, Lani]
departments: [Operations]
purposes: [Maintenance, Automation]
tags:
  - plugin
  - sync
  - github
  - laniameda-skills
  - cowork
  - maintenance
---

# Sync Plugin Skills — laniameda-skills → Cowork Plugin

Keep the Cowork plugin in sync with the canonical laniameda-skills GitHub repo.

---

## Why This Exists

The laniameda AI creatorship plugin installed in Cowork is a `.plugin` ZIP file.
When skills in the GitHub repo (`Michailbul/laniameda-skills`) are updated, the plugin doesn't auto-update.
This skill rebuilds and reinstalls the plugin so Cowork picks up the latest versions.

---

## Architecture

```
github.com/Michailbul/laniameda-skills
  └── skills/ai-creatorship/           ← source of truth
        ├── seedance-prompting/
        ├── nano-banana-pro/
        ├── crea-cinematic-prompts/
        └── ... (all 14 skills)
              ↓
        [this skill: build + install]
              ↓
  ~/.claude/skills/laniameda-ai-creatorship/  ← local symlinks (install-skills.sh)
  ~/work/laniameda/laniameda-hq/*.plugin      ← rebuilt plugin file for Cowork
```

**Remote plugin files at `.remote-plugins/` are read-only** — they're served by Cowork's registry.
The update path is to rebuild the `.plugin` ZIP and reinstall it via Cowork.

---

## Step 1 — Pull Latest from GitHub

```bash
cd ~/work/laniameda/laniameda-hq/laniameda-skills
git pull origin main
```

Check what changed:
```bash
git log --oneline -5
git diff HEAD~1 HEAD --name-only
```

---

## Step 2 — Run install-skills.sh (local sync)

This syncs all skills to `~/.agents/skills/` and `~/.claude/skills/`:

```bash
cd ~/work/laniameda/laniameda-hq/laniameda-skills
./install-skills.sh
```

To sync a single skill only:
```bash
./install-skills.sh seedance-prompting
```

---

## Step 3 — Identify What Changed (ai-creatorship scope)

Scope the diff to only ai-creatorship skills:

```bash
git diff HEAD~1 HEAD -- skills/ai-creatorship/
```

Check for:
- **Updated SKILL.md files** → need to be reflected in plugin
- **New skill folders** → need to be added to plugin
- **Deleted skill folders** → need to be removed from plugin
- **Renamed folders** → update plugin folder name + SKILL.md name field

---

## Step 4 — Rebuild the Plugin File

The plugin is a ZIP file with this structure:
```
plugin_name.plugin (ZIP)
  ├── README.md
  └── skills/
        ├── skill-name-1/
        │     └── SKILL.md
        ├── skill-name-2/
        │     └── SKILL.md
        └── ...
```

### Build script

```bash
#!/bin/bash
# Run from laniameda-hq/

PLUGIN_NAME="laniameda-ai-creatorship"
SOURCE_DIR="laniameda-skills/skills/ai-creatorship"
OUTPUT="$PLUGIN_NAME.plugin"
STAGING="/tmp/$PLUGIN_NAME-staging"

# Clean staging
rm -rf "$STAGING"
mkdir -p "$STAGING/skills"

# Copy README
cp "$SOURCE_DIR/../../../README.md" "$STAGING/README.md" 2>/dev/null || \
  echo "# $PLUGIN_NAME Plugin" > "$STAGING/README.md"

# Copy all skill folders
for skill_dir in "$SOURCE_DIR"/*/; do
  skill_name=$(basename "$skill_dir")
  mkdir -p "$STAGING/skills/$skill_name"
  cp "$skill_dir/SKILL.md" "$STAGING/skills/$skill_name/SKILL.md"
  # Copy any reference dirs if present
  [ -d "$skill_dir/references" ] && cp -r "$skill_dir/references" "$STAGING/skills/$skill_name/"
  [ -d "$skill_dir/scripts" ] && cp -r "$skill_dir/scripts" "$STAGING/skills/$skill_name/"
done

# Build the ZIP
rm -f "$OUTPUT"
cd "$STAGING" && zip -r "$OLDPWD/$OUTPUT" . && cd "$OLDPWD"
echo "Built: $OUTPUT"
```

Save this as `laniameda-hq/scripts/build-plugin.sh` and run:
```bash
cd ~/work/laniameda/laniameda-hq
bash scripts/build-plugin.sh
```

---

## Step 5 — Reinstall in Cowork

After rebuilding, the `.plugin` file needs to be installed in Cowork:

1. Open Cowork settings → Plugins
2. Remove the old `laniameda-ai-creatorship` plugin
3. Install the new `.plugin` file from `~/work/laniameda/laniameda-hq/laniameda-ai-creatorship.plugin`

OR if Cowork supports auto-reload from a local path, point it to the rebuilt file.

---

## Skill Sync Checklist

When syncing, verify these specific cases:

| Change type | Action |
|---|---|
| SKILL.md content updated | Overwrite file in plugin staging |
| New skill folder added | Add folder + SKILL.md to staging |
| Skill folder deleted | Remove from staging |
| Skill folder renamed | Rename in staging, update `name:` field in SKILL.md |
| references/ or scripts/ added | Copy alongside SKILL.md |

---

## Current Skill Manifest (ai-creatorship)

As of 2026-04-12, the canonical repo contains these skills:

| Folder | Status |
|---|---|
| `ai-avatar-realistic` | ✅ active |
| `ai-typography` | ✅ active |
| `ai-video-prompting` | ✅ active |
| `character-consistency-character-sheet` | ✅ active (was: `character-consistency`) |
| `color-grade-transfer` | ✅ active |
| `crea-cinematic-prompts` | ✅ active |
| `frame-vfx-stylizer` | ✅ active |
| `image-to-prompt` | ✅ active |
| `laniameda-gallery-ingest` | ✅ active |
| `laniameda-x-post` | ✅ active |
| `mj-nb2-pipeline` | ✅ active |
| `nano-banana-pro` | ✅ active |
| `seedance-prompting` | ✅ active (major update 2026-04-12) |
| `visual-style-replicator` | ✅ active |

**Removed from repo (remove from plugin):**
- `laniameda-gallery` — deleted (commit: "remove duplicate laniameda-gallery skill")

---

## Quick Reference — What Changed in This Sync (2026-04-12)

From commit `439b473 → 4d1bb7f`:

1. **`seedance-prompting/SKILL.md`** — major rewrite: added Mode 4 (commercial montage), compact single-shot template, reference library pointers, advanced director structure, multimodal dispatch reference, full debugging guide
2. **`laniameda-gallery/`** — DELETED from repo (was duplicate of `laniameda-gallery-ingest`)
3. **`character-consistency/`** — RENAMED to `character-consistency-character-sheet` + content updated
4. **`install-skills.sh`** — updated install script (pull this too)

---

## Notes

- Never edit files directly in `.remote-plugins/` — they're read-only (served by Cowork registry)
- The source of truth is always `github.com/Michailbul/laniameda-skills`
- After a plugin rebuild + reinstall, restart the Cowork session to pick up new skill descriptions
- The plugin README.md should be updated to reflect the current skill manifest after each sync
