#!/bin/bash
# install-skills.sh — Sync laniameda skills to ~/.agents/skills/ and ~/.claude/skills/
#
# Copies all skill folders from this repo (including nested skills/<category>/<skill>/)
# into both ~/.agents/skills/<skill-name>/ and ~/.claude/skills/<skill-name>/ as real
# directories (no symlinks). This ensures compatibility with tools like Cowork that
# cannot resolve symlinks through mounted filesystems.
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
  # Use rsync to skip broken symlinks (some reference VPS paths)
  rsync -a --safe-links "$src/" "$AGENTS_DIR/$name/"

  # Copy to ~/.claude/skills/ as a real directory (no symlinks — required for Cowork)
  if [[ -L "$CLAUDE_DIR/$name" ]]; then
    # Was a symlink before — remove and replace with real copy
    rm "$CLAUDE_DIR/$name"
    rsync -a --safe-links "$src/" "$CLAUDE_DIR/$name/"
    ((updated++))
    echo "  updated: $name (replaced symlink with real dir)"
  elif [[ -d "$CLAUDE_DIR/$name" ]]; then
    rm -rf "$CLAUDE_DIR/$name"
    rsync -a --safe-links "$src/" "$CLAUDE_DIR/$name/"
    ((updated++))
    echo "  updated: $name"
  else
    rsync -a --safe-links "$src/" "$CLAUDE_DIR/$name/"
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
