#!/bin/bash
# install-skills.sh — Install all laniameda skills globally via npx skills
# Handles the nested skills/<category>/<skill>/ structure that npx skills can't discover.
# Creates a temp flattened copy, installs from there, cleans up.
#
# Usage: ./install-skills.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TMP_DIR=$(mktemp -d)

echo "📦 Preparing laniameda skills for installation..."

# Copy root-level skills (e.g. design-thinking-partner)
for dir in "$SCRIPT_DIR"/*/; do
  skill_name=$(basename "$dir")
  # Skip non-skill directories
  [[ "$skill_name" == "skills" || "$skill_name" == "design-system" || "$skill_name" == "deprecated" ]] && continue
  # Only copy if it contains SKILL.md
  if [[ -f "$dir/SKILL.md" ]]; then
    cp -r "$dir" "$TMP_DIR/$skill_name"
  fi
done

# Flatten nested skills/<category>/<skill>/ to root level
if [[ -d "$SCRIPT_DIR/skills" ]]; then
  for category_dir in "$SCRIPT_DIR/skills"/*/; do
    category=$(basename "$category_dir")
    # Skip deprecated skills
    [[ "$category" == "deprecated" ]] && continue
    for skill_dir in "$category_dir"*/; do
      skill_name=$(basename "$skill_dir")
      if [[ -f "$skill_dir/SKILL.md" ]]; then
        cp -r "$skill_dir" "$TMP_DIR/$skill_name"
      fi
    done
  done
fi

# Count what we found
skill_count=$(find "$TMP_DIR" -maxdepth 2 -name "SKILL.md" | wc -l | tr -d ' ')
echo "Found $skill_count skills to install."

if [[ "$skill_count" -eq 0 ]]; then
  echo "No skills found. Exiting."
  rm -rf "$TMP_DIR"
  exit 1
fi

# List them
echo ""
for skill_dir in "$TMP_DIR"/*/; do
  if [[ -f "$skill_dir/SKILL.md" ]]; then
    echo "  $(basename "$skill_dir")"
  fi
done
echo ""

# Install globally
echo "Installing to all agents..."
npx skills add "$TMP_DIR" --all --global

# Clean up
rm -rf "$TMP_DIR"
echo "Done. Temp files cleaned up."
