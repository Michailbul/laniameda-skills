---
name: laniameda-youtube-digest
description: >
  Watch a YouTube video so Michael doesn't have to. Extract what's actionable — tools, prompts,
  workflows, "if X then Y" mappings — and save to KB. Uses Supadata API for transcripts.
  Keywords: digest video, watch this, youtube extract, video summary, youtube transcript.
version: 2.0.0
status: active
created: 2026-02-01
updated: 2026-03-25
owner: Lani
agents: [Lani, Meda]
departments: [Marketing, Operations]
purposes: [Ingestion, Research, Content Repurposing, Knowledge Base]
tags:
  - youtube
  - video
  - digest
  - transcript
  - knowledge-base
  - content-repurposing
  - supadata
depends_on: [supadata]
replaces: [youtube-digest]
---

# laniameda-youtube-digest

**Purpose:** Watch a YouTube video so Michael doesn't have to. Extract what's actionable — tools, prompts, workflows, "if X then Y" mappings — and save to KB.

**Engine:** Supadata API (`supadata` skill).

---

## Triggers

- YouTube URL pasted
- "digest this video"
- "watch this for me"
- "extract from this video"
- "what's useful in this"
- "learn from this"

---

## Extraction Priority (what matters to Michael)

- Agent orchestration — specific workflow architectures, "if X then Y" tool mappings
- Prompt engineering — templates with [BLANKS], copy-pasteable
- AI design systems — design tokens, UI generation prompts, exact tool names
- AI creatorship — exact prompts with parameters, generation workflows, modern techniques
- Tool workflows — "If I need X, use Y" with steps

**Golden rule:** If Michael can't copy-paste and use it immediately, it's not specific enough. Generics = skip.

---

## Workflow

### Step 1 — Metadata
```bash
curl -s "https://api.supadata.ai/v1/youtube/video?id=<VIDEO_ID>" \
  -H "x-api-key: $SUPADATA_API_KEY"
```
Check description for linked prompts, swipe files, "link in bio" resources → fetch with `web_fetch`.

### Step 2 — Transcript
```bash
curl -s "https://api.supadata.ai/v1/youtube/transcript?url=<URL>&text=true" \
  -H "x-api-key: $SUPADATA_API_KEY"
```
If language fails → retry without `lang` param.

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
• [Tool]: [what it does]
• [Prompt/workflow]: [brief]

Digest and save? (yes / skip / partial)
```

### Step 4 — Deep digest (on approval)

Extract ONLY:
- Specific tool names
- Exact prompts (copy-paste ready)
- Step-by-step workflows
- "If X then Y" mappings
- Code snippets / commands

### Step 5 — Save to KB

Location: `~/work/laniameda/laniameda-hq/content-kb/sources/youtube/YYYY-MM-DD-<slug>/`

Files:
- `meta.json` — title, url, channel, date, verdict, tools_mentioned, tags
- `digest.md` — full extraction
- `prompts.md` — prompts/templates only
- `workflows.md` — step-by-step workflows only

If marketing-ready → also save to `content-kb/marketing-ready/YYYY-MM-DD-<slug>.md`

---

## Hard Rules

- Deliver fast verdict first, always — don't dump full transcript unprompted
- If video is mostly generic motivation/inspiration → SKIP, say why in one line
- Never summarize in vague terms — specifics or nothing
- Save the actual content, not a paraphrase of what the video "is about"
