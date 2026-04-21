#!/bin/bash
# install-skills.sh — Sync laniameda skills to ~/.agents/skills/, ~/.claude/skills/, ~/.codex/skills/, and optional workspace skill dirs
#
# Copies all skill folders from this repo (including nested skills/<category>/<skill>/)
# into ~/.agents/skills/<skill-name>/ and ~/.claude/skills/<skill-name>/ as real
# directories. Creates ~/.codex/skills/<skill-name> symlinks pointing to the
# ~/.agents/skills copies so Codex sees the same canonical install without duplicate
# directory copies. Optionally also syncs into one or more workspace skill directories
# so local agent workspaces stay aligned with the canonical repo.
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
CODEX_DIR="$HOME/.codex/skills"
TARGET_SKILL="${1:-}"
WORKSPACE_SKILLS_DIRS="${WORKSPACE_SKILLS_DIRS:-}"
SKIP_EXTERNAL_SYNC="${SKIP_EXTERNAL_SYNC:-}"

mkdir -p "$AGENTS_DIR" "$CLAUDE_DIR" "$CODEX_DIR"

# External-origin skills. Each entry: "<origin-repo-path>:<origin-skill-subdir>:<local-category>"
# Before installing, pull the origin repo and rsync the skill into this repo so
# downstream agents always get the latest version from ground truth.
EXTERNAL_ORIGINS=(
  "$HOME/work/laniameda/laniameda.gallery:skills/laniameda-gallery-ingest:ai-creatorship"
  "$HOME/work/laniameda/laniameda.gallery:skills/laniameda-gallery-query:utility"
)

sync_external_origins() {
  [[ -n "$SKIP_EXTERNAL_SYNC" ]] && { echo "Skipping external origin sync (SKIP_EXTERNAL_SYNC set)."; echo ""; return; }

  echo "Refreshing skills from external origins..."
  local pulled_repos=()
  for entry in "${EXTERNAL_ORIGINS[@]}"; do
    IFS=':' read -r repo_path skill_subdir category <<< "$entry"
    local skill_name
    skill_name=$(basename "$skill_subdir")

    if [[ ! -d "$repo_path/.git" ]]; then
      echo "  skipped: $skill_name (origin repo not found at $repo_path)"
      continue
    fi

    # Pull each origin repo once even if it hosts multiple skills
    if [[ ! " ${pulled_repos[*]:-} " =~ " $repo_path " ]]; then
      if (cd "$repo_path" && git pull --ff-only --quiet 2>/dev/null); then
        echo "  pulled:  $(basename "$repo_path")"
      else
        echo "  warn:    could not fast-forward $(basename "$repo_path") — using current checkout"
      fi
      pulled_repos+=("$repo_path")
    fi

    local src="$repo_path/$skill_subdir"
    local dst="$SCRIPT_DIR/skills/$category/$skill_name"
    if [[ ! -d "$src" ]]; then
      echo "  skipped: $skill_name (origin path missing: $src)"
      continue
    fi
    mkdir -p "$dst"
    # Preserve the local README.md pointer (it documents the origin relationship)
    rsync -a --delete --exclude='.DS_Store' --exclude='README.md' "$src/" "$dst/"
    echo "  synced:  $skill_name ← $(basename "$repo_path")/$skill_subdir"
  done
  echo ""
}

sync_external_origins

WORKSPACE_DIR_ARRAY=()
if [[ -n "$WORKSPACE_SKILLS_DIRS" ]]; then
  IFS=':' read -r -a WORKSPACE_DIR_ARRAY <<< "$WORKSPACE_SKILLS_DIRS"
  for workspace_dir in "${WORKSPACE_DIR_ARRAY[@]}"; do
    [[ -n "$workspace_dir" ]] && mkdir -p "$workspace_dir"
  done
fi

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

link_codex_skill() {
  local name="$1"
  local target="$AGENTS_DIR/$name"
  local link="$CODEX_DIR/$name"

  if [[ -L "$link" ]]; then
    rm "$link"
  elif [[ -e "$link" ]]; then
    rm -rf "$link"
  fi

  ln -s "$target" "$link"
}

sync_skill() {
  local src="$1"
  local name=$(basename "$src")

  sync_dir "$src" "$AGENTS_DIR" "$name"
  link_codex_skill "$name"

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

  if [[ ${#WORKSPACE_DIR_ARRAY[@]} -gt 0 ]]; then
    for workspace_dir in "${WORKSPACE_DIR_ARRAY[@]}"; do
      [[ -z "$workspace_dir" ]] && continue
      sync_dir "$src" "$workspace_dir" "$name"
      echo "           ↳ workspace: $workspace_dir/$name"
    done
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
    skipped=$((skipped + 1))
    continue
  fi
  sync_skill "$skill_path"
done

echo ""
echo "Done. $updated updated, $created new, $skipped skipped."
