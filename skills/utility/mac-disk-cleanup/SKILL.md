---
name: mac-disk-cleanup
description: >
  Audit and clean up disk space on macOS. Scans all major space consumers — apps, caches,
  dev tools, audio plugins, sample libraries, node_modules, Docker, and system data.
  Produces a ranked report and executes removals on confirmation. Trigger when the user
  says "clean up space", "disk is full", "free up storage", "what's taking space", or
  "audit my disk".
metadata:
  laniameda:
    departments: ['Operations']
    purposes: ['Maintenance', 'System']
    tags: ['macos', 'disk', 'cleanup', 'storage', 'maintenance', 'devtools', 'audio']
    status: active
    depends_on: []
    replaces: []
---

# Mac Disk Cleanup

## Purpose

Systematically find and reclaim disk space on macOS without losing important data. Covers the full spectrum — from obvious caches to deep audio plugin libraries and orphaned dev dependencies that silently eat storage.

## When to Use

- User says "clean up space", "disk full", "free up storage", "what's using space"
- Disk free drops below 15% of total
- Before large installs or project work that needs headroom
- Periodic maintenance (monthly recommended)

## What This Skill Produces

1. **Disk audit report** — ranked table of all major consumers
2. **Actionable cleanup plan** — categorized by risk (safe cache / recoverable deps / permanent removal)
3. **Executed removals** — with before/after space comparison
4. **Sudo command block** — for system-level removals that need Terminal

## Inputs

- No inputs required — skill auto-discovers everything
- Optional: user can specify areas to focus on (e.g. "just audio", "just dev tools")

## Core Workflow

### Phase 1 — Snapshot & Scan

Start with the baseline:
```bash
df -h / | tail -1
```

Run all scans in parallel for speed. Never use `find` with `-uall` on large dirs.

**Scan targets (run in parallel):**

| Category | What to scan |
|---|---|
| **Overview** | `df -h /` for total/free |
| **User folders** | `~/Downloads`, `~/Documents`, `~/Desktop`, `~/Movies`, `~/Music`, `~/Pictures`, `~/work`, `~/.Trash` |
| **Library caches** | `~/Library/Caches/*` sorted by size |
| **App Support** | `~/Library/Application Support/*` sorted by size |
| **Containers** | `~/Library/Containers/*` sorted by size |
| **Group Containers** | `~/Library/Group Containers/*` sorted by size |
| **System audio** | `/Library/Audio/Plug-Ins/VST3/*`, `/Library/Audio/Plug-Ins/Components/*`, `/Library/Audio/Plug-Ins/VST/*` |
| **Audio vendors** | `/Library/Arturia`, `/Library/Application Support/Native Instruments`, `/Library/Application Support/iZotope`, `/Library/Application Support/XLN Audio`, `/Library/Application Support/Toontrack`, `/Library/Application Support/Waves`, `/Library/Application Support/Splice` |
| **User audio** | `~/Library/Audio/Presets`, `~/Music/*` |
| **Dev tools** | `/opt/homebrew`, `~/.npm`, `~/.bun`, `~/.cargo`, `~/.rustup`, `~/.nvm`, `~/.volta`, `~/.pyenv`, `~/.conda` |
| **node_modules** | `find ~/work -name "node_modules" -type d -maxdepth 4` |
| **Applications** | `du -sh /Applications/* \| sort -hr` |
| **Docker** | `docker system df` (if running) |
| **Logs** | `~/Library/Logs` |

### Phase 2 — Report

Present findings as a **single ranked table**, descending by size. Group into categories:

```
## Disk Audit — [date]

**Total:** XXX GB | **Used:** XXX GB | **Free:** XXX GB

### Top consumers (>500 MB)

| # | Item | Size | Category | Safe to remove? |
|---|---|---|---|---|
| 1 | ... | ... | ... | ... |
```

Categories: `cache`, `dev-deps`, `audio-plugin`, `sample-library`, `app`, `app-data`, `media`, `system`

For each item, note:
- Whether it's **safe** (cache, regenerates), **recoverable** (reinstallable), or **permanent** (unique data)
- Whether it needs `sudo`

### Phase 3 — Confirm & Execute

**Never delete without explicit user confirmation.** Present the plan, get approval per category or per item.

Execution order:
1. **Caches first** — zero risk, immediate wins
2. **Dev dependencies** (node_modules) — recoverable via `npm install`
3. **App data** for removed/unused apps
4. **Audio plugins/samples** — only on explicit confirmation per vendor
5. **Apps** — only on explicit confirmation

For system-level paths (`/Library/*`, `/Applications/*`), collect all removals into a single sudo block the user can paste in Terminal.

### Phase 4 — Verify

```bash
df -h / | tail -1
```

Report: **Before:** X GB free | **After:** Y GB free | **Recovered:** Z GB

## Scan Commands Reference

### Quick cache scan
```bash
du -sh ~/Library/Caches/* 2>/dev/null | sort -hr | head -20
```

### node_modules audit
```bash
find ~/work -name "node_modules" -type d -maxdepth 4 -exec du -sh {} \; 2>/dev/null | sort -hr
```

### Audio plugins (VST3) full list
```bash
du -sh /Library/Audio/Plug-Ins/VST3/*.vst3 2>/dev/null | sort -hr
```

### App Support deep scan
```bash
ls -d ~/Library/"Application Support"/*/ 2>/dev/null | while read d; do du -sh "$d" 2>/dev/null; done | sort -hr | head -30
```

### Applications ranked
```bash
du -sh /Applications/* 2>/dev/null | sort -hr | head -30
```

### Electron app cache pattern
For Electron apps (Claude, Cursor, Windsurf, Slack, Discord, Notion, etc.):
```bash
# Check these subfolders — all are safe to clear:
Cache/  Code Cache/  GPUCache/  Service Worker/CacheStorage/
```

### Homebrew cleanup
```bash
brew cleanup --prune=0  # removes all cached downloads
brew autoremove         # removes unused dependencies
```

### NVM unused versions
```bash
nvm ls                  # list installed versions
nvm uninstall <version> # remove unused ones
```

## Known Large Consumers on macOS

| App/Tool | Where it hides | Typical size |
|---|---|---|
| Claude Desktop | `~/Library/Application Support/Claude/vm_bundles/` | 9-10 GB (VM image) |
| Xcode / Swift | `~/Library/Developer/`, `~/Library/Caches/org.swift.swiftpm` | 5-50 GB |
| Docker | `~/Library/Containers/com.docker.docker/` | 5-60 GB |
| Arturia V Collection | `/Library/Arturia/Samples/` | 10-20 GB |
| iZotope (Ozone/RX/Neutron) | `/Library/Application Support/iZotope/` | 10-15 GB |
| XLN Addictive Drums | `/Library/Application Support/XLN Audio/` | 10-15 GB |
| Native Instruments | `/Library/Application Support/Native Instruments/` | 3-50 GB |
| Adobe Creative Suite | `/Library/Application Support/Adobe/` + apps | 10-30 GB |
| Spotify offline | `~/Library/Application Support/Spotify/PersistentCache/` | 1-5 GB |
| Playwright browsers | `~/Library/Caches/ms-playwright/` | 1-2 GB |
| Homebrew | `/opt/homebrew/` | 3-10 GB |
| node_modules (scattered) | `~/work/**/node_modules/` | 5-30 GB |
| Apple Music downloads | `~/Music/Music/` | 1-10 GB |
| CoreML cache | `~/Library/Application Support/coreMLCache/` | 0.5-2 GB |

## Hard Rules

1. **Never delete without confirmation.** Always show what will be removed and the size.
2. **Research first, remove second.** Full audit before any deletion.
3. **Separate user-level from system-level.** Anything under `/Library/` needs sudo — collect into a pasteable block.
4. **Always report before/after.** Run `df -h /` at start and end.
5. **Flag permanent deletions.** Caches regenerate. Sample libraries don't. Make the distinction clear.
6. **Don't touch active project dependencies** without asking which projects are active.
7. **Audio plugins: confirm per vendor.** Musicians are particular about their tools. Never batch-delete audio without per-vendor approval.
8. **Check if apps are running** before deleting their caches (browser caches especially).
