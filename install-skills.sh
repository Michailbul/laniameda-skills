#!/bin/bash
# install-skills.sh — Sync laniameda skills directly to ~/.agents/skills/
#
# Copies all skill folders from this repo (including nested skills/<category>/<skill>/)
# into ~/.agents/skills/<skill-name>/. Claude Code and other agents pick them up
# via existing symlinks from ~/.claude/skills/ → ~/.agents/skills/.
#
# For new skills that don't have symlinks yet, creates them.
#
# Usage:
#   ./install-skills.sh          # sync all skills
#   ./install-skills.sh supadata # sync one skill

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
AGENTS_DIR="$HOME/.agents/skills"
CLAUDE_DIR="$HOME/.claude/skills"
TARGET_SKILL="${1:-}"

mkdir -p "$AGENTS_DIR" "$CLAUDE_DIR"

updated=0
created=0
skipped=0

sync_skill() {
  local src="$1"
  local name=$(basename "$src")

  # Copy to ~/.agents/skills/
  if [[ -d "$AGENTS_DIR/$name" ]]; then
    rm -rf "$AGENTS_DIR/$name"
  fi
  cp -r "$src" "$AGENTS_DIR/$name"

  # Ensure symlink exists in ~/.claude/skills/
  if [[ -L "$CLAUDE_DIR/$name" ]]; then
    ((updated++))
    echo "  updated: $name"
  elif [[ -d "$CLAUDE_DIR/$name" ]]; then
    # Real dir exists (not symlink) — replace with symlink
    rm -rf "$CLAUDE_DIR/$name"
    ln -s "../../.agents/skills/$name" "$CLAUDE_DIR/$name"
    ((updated++))
    echo "  updated: $name (relinked)"
  else
    ln -s "../../.agents/skills/$name" "$CLAUDE_DIR/$name"
    ((created++))
    echo "  new:     $name"
  fi
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
    ((skipped++))
    continue
  fi
  sync_skill "$skill_path"
done

echo ""
echo "Done. $updated updated, $created new, $skipped skipped."
