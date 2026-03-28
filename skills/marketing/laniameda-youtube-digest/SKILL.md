---
name: laniameda-youtube-digest
description: >
  Watch a YouTube video so Michael doesn't have to. Extract what's actionable — tools, prompts,
  workflows, "if X then Y" mappings, model-specific techniques — and save to KB. Uses Supadata API
  for transcripts and vision extraction (on-screen content like ComfyUI node graphs, prompts not
  spoken aloud). Also handles learning-oriented triggers for AI creatorship tutorials.
  Keywords: digest video, watch this, youtube extract, video summary, youtube transcript,
  learn from this, what does this teach, upgrade your skills, ai tutorial, prompting tutorial.
version: 3.0.0
status: active
created: 2026-02-01
updated: 2026-03-28
owner: Lani
agents: [Lani, Meda, Crea]
departments: [Marketing, Operations, AI Creatorship]
purposes: [Ingestion, Research, Content Repurposing, Knowledge Base, Learning, Skill Upgrade]
tags:
  - youtube
  - video
  - digest
  - transcript
  - knowledge-base
  - content-repurposing
  - supadata
  - learning
  - ai-creatorship
  - skill-upgrade
  - prompting
  - image-gen
  - video-gen
depends_on: [supadata]
replaces: [youtube-digest, crea-youtube-learn]
---

# laniameda-youtube-digest

**Purpose:** Watch a YouTube video so Michael doesn't have to. Extract what's actionable — tools, prompts, workflows, "if X then Y" mappings — and save to KB. For AI creatorship tutorials: extract model-specific techniques, prompt structures, and optionally encode new knowledge into studio skills.

**Engine:** Supadata API (`supadata` skill). Full API reference: `references/supadata.md`. Key decision: use **Transcript** for narrated content; use **Extract** (vision) when prompts/settings are shown on screen but not spoken aloud (e.g. ComfyUI node graphs, Midjourney UI, on-screen prompt text).

**Cross-reference:** This is the skill that `laniameda-x-post-digest` calls when it encounters YouTube links in X posts.

---

## Triggers

- YouTube URL pasted
- "digest this video"
- "watch this for me"
- "extract from this video"
- "what's useful in this"
- "learn from this"
- "what does this teach"
- "does this have good prompting technique"
- "upgrade your skills from this"
- "digest this AI tutorial"

---

## Extraction Priority (what matters to Michael)

- **Agent orchestration** — specific workflow architectures, "if X then Y" tool mappings, MCP names, Claude Code patterns
- **Prompt engineering** — templates with [BLANKS], copy-pasteable structures, named frameworks
- **AI design systems** — design tokens, UI generation prompts, exact tool names + use cases
- **AI creatorship** — exact prompts with parameters, generation workflows, modern techniques
- **Model-specific craft** — what works/doesn't in Midjourney, FLUX, Nano Banana, Kling, Runway, Seedance, etc.
- **Tool workflows** — "If I need X, use Y" with steps
- **Visual direction craft** — lighting language, camera language, composition rules that translate to prompts
- **Negative findings** — techniques that are hyped but don't work (equally valuable)

**Golden rule:** If Michael can't copy-paste and use it immediately, it's not specific enough. Generics = skip. Inspiration without technique = skip.

---

## Workflow

### Step 1 — Metadata
```bash
curl -s "https://api.supadata.ai/v1/youtube/video?id=<VIDEO_ID>" \
  -H "x-api-key: $SUPADATA_API_KEY"
```
Check description for linked prompts, swipe files, preset downloads, "link in bio" resources → fetch with `web_fetch` if relevant.

### Step 2 — Transcript or Extract

See `references/supadata.md` for full API reference and curl commands.

**Choose based on content type:**
- **Narrated content** → `/youtube/transcript?url=<URL>&text=true` (native captions, 1 credit)
- **Visual-heavy tutorial** (prompts on screen, UI demos, ComfyUI graphs, settings panels) → `/extract` with vision schema. Use when important technique content is shown but not spoken.
- If transcript returns no content → retry without `lang` param, or fall back to Extract.

```bash
# Transcript (default)
curl -s "https://api.supadata.ai/v1/youtube/transcript?url=<URL>&text=true" \
  -H "x-api-key: $SUPADATA_API_KEY"

# Extract (for visual content — async, returns jobId)
curl -X POST "https://api.supadata.ai/v1/extract" \
  -H "x-api-key: $SUPADATA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "<URL>",
    "prompt": "Extract all AI image prompts shown on screen. Include exact text, tool/platform visible, and parameter settings.",
    "schema": { ... }
  }'
```

### Step 3 — Fast verdict (always deliver this first)

```
[VIDEO TITLE] — [Channel] (~Xmin)

What it is: [one sentence — what they show + tools used]

Verdict: USEFUL / PARTIAL / SKIP

Why:
• [specific reason]
• [what's new]
• [what's missing]

Interest match: [which of Michael's interests]
Repurposable: Yes / No

Preview:
• [Tool/Technique]: [what it does / one line]
• [Prompt/workflow]: [brief]

Skill impact: [which existing skill this would update, or "new skill warranted", or "none"]

Digest and save? (yes / skip / partial)
```

### Step 4 — Deep digest (on approval)

Extract ONLY:
- Specific tool names
- Exact prompts shown or described (copy-paste ready)
- Step-by-step workflows
- "If X then Y" mappings
- Code snippets / commands
- Model-specific rules ("in Kling v2.5, X causes Y")
- Tool settings, parameters, version numbers
- Technique verdicts (works / doesn't work / when to use)
- Direct quotes if they capture a principle cleanly

**Skip:** channel intros, sponsor segments, generic motivation, "AI is amazing" takes, vague inspiration.

### Step 5 — Save to KB

Location: `~/work/laniameda/laniameda-hq/content-kb/sources/youtube/YYYY-MM-DD-<slug>/`

Files:
- `meta.json` — title, url, channel, date, verdict, tools_mentioned, models_mentioned, techniques, tags
- `digest.md` — full extraction
- `prompts.md` — prompts/templates only
- `workflows.md` — step-by-step workflows only
- `techniques.md` — model-specific rules, technique verdicts, what works vs what doesn't

If marketing-ready → also save to `content-kb/marketing-ready/YYYY-MM-DD-<slug>.md`

### Step 6 — Skill encoding check

Read `references/skill-upgrade-protocol.md` for the full decision tree.

**Short version:**
After saving to KB, ask: *does this video teach something that isn't already in our skills?*

- **Yes, it refines an existing skill** → propose a patch to the relevant SKILL.md, ask Michael to approve before writing
- **Yes, it warrants a new skill** → propose skill name + one-line purpose, ask Michael to approve, then build it using skill-creator
- **No, KB save is enough** → done

Always ask before writing to any SKILL.md or creating a new skill folder.

---

## Hard Rules

- Deliver fast verdict first, always — don't dump full transcript unprompted
- If video is mostly generic motivation/inspiration → SKIP, say why in one line
- SKIP verdict if video is: generic AI hype, tool demos with no technique depth, "10 prompts you need" lists with no explanation of why they work
- Never summarize in vague terms — specifics or nothing
- Save the actual content, not a paraphrase of what the video "is about"
- Never paraphrase technique — extract the actual rule, the actual prompt, the actual finding
- Model specificity matters — "works in Midjourney" ≠ "works in FLUX" — always tag the model
