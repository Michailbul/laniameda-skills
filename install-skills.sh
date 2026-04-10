#!/bin/bash
# install-skills.sh — Sync laniameda skills to ~/.agents/skills/, ~/.claude/skills/, and optional workspace skill dirs
#
# Copies all skill folders from this repo (including nested skills/<category>/<skill>/)
# into ~/.agents/skills/<skill-name>/ and ~/.claude/skills/<skill-name>/ as real
# directories (no symlinks). Optionally also syncs into one or more workspace skill
# directories so local agent workspaces stay aligned with the canonical repo.
#
# Usage:
#   ./install-skills.sh                          # sync all skills to default targets
#   ./install-skills.sh supadata                 # sync one skill to default targets
#   WORKSPACE_SKILLS_DIRS="/root/.openclaw/workspace-crea/skills" ./install-skills.sh
#   WORKSPACE_SKILLS_DIRS="/path/a:/path/b" ./install-skills.sh parallel-web-search

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
AGENTS_DIR="$HOME/.agents/skills"
CLAUDE_DIR="$HOME/.claude/skills"
TARGET_SKILL="${1:-}"
WORKSPACE_SKILLS_DIRS="${WORKSPACE_SKILLS_DIRS:-}"

mkdir -p "$AGENTS_DIR" "$CLAUDE_DIR"

IFS=':' read -r -a WORKSPACE_DIR_ARRAY <<< "$WORKSPACE_SKILLS_DIRS"
for workspace_dir in "${WORKSPACE_DIR_ARRAY[@]}"; do
  [[ -n "$workspace_dir" ]] && mkdir -p "$workspace_dir"
done

updated=0
created=0
skipped=0

sync_dir() {
  local src="$1"
  local dest_root="$2"
  local name="$3"

  if [[ -L "$dest_root/$name" ]]; then
    rm "$dest_root/$name"
  elif [[ -d "$dest_root/$name" ]]; then
    rm -rf "$dest_root/$name"
  fi

  rsync -a --safe-links "$src/" "$dest_root/$name/"
}

sync_skill() {
  local src="$1"
  local name=$(basename "$src")

  sync_dir "$src" "$AGENTS_DIR" "$name"

  if [[ -L "$CLAUDE_DIR/$name" ]]; then
    sync_dir "$src" "$CLAUDE_DIR" "$name"
    updated=$((updated + 1))
    echo "  updated: $name (replaced symlink with real dir)"
  elif [[ -d "$CLAUDE_DIR/$name" ]]; then
    sync_dir "$src" "$CLAUDE_DIR" "$name"
    updated=$((updated + 1))
    echo "  updated: $name"
  else
    sync_dir "$src" "$CLAUDE_DIR" "$name"
    created=$((created + 1))
    echo "  new:     $name"
  fi

  for workspace_dir in "${WORKSPACE_DIR_ARRAY[@]}"; do
    [[ -z "$workspace_dir" ]] && continue
    sync_dir "$src" "$workspace_dir" "$name"
    echo "           ↳ workspace: $workspace_dir/$name"
  done
}

echo "Syncing laniameda skills..."
echo ""

# Collect all skill paths
declare -a skill_paths=()

# Root-level skills (e.g. design-thinking-partner)
for dir in "$SCRIPT_DIR"/*/; do
  name=$(basename "$dir")
  [[ "$name" == "skills" || "$name" == "design-system" ]] && continue
  [[ -f "$dir/SKILL.md" ]] && skill_paths+=("$dir")
done

# Nested skills/<category>/<skill>/
if [[ -d "$SCRIPT_DIR/skills" ]]; then
  for category_dir in "$SCRIPT_DIR/skills"/*/; do
    category=$(basename "$category_dir")
    [[ "$category" == "deprecated" ]] && continue
    for skill_dir in "$category_dir"*/; do
      [[ -f "$skill_dir/SKILL.md" ]] && skill_paths+=("$skill_dir")
    done
  done
fi

# Sync
for skill_path in "${skill_paths[@]}"; do
  name=$(basename "$skill_path")
  if [[ -n "$TARGET_SKILL" && "$name" != "$TARGET_SKILL" ]]; then
    skipped=$((skipped + 1))
    continue
  fi
  sync_skill "$skill_path"
done

echo ""
echo "Done. $updated updated, $created new, $skipped skipped."
