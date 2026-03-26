---
name: crea-youtube-learn
description: >
  Learn from a YouTube video about AI creative tools, image gen, video gen, prompting techniques,
  or AI workflows. Watches the video, extracts what's worth knowing, judges if it upgrades Crea's
  skills, and encodes new knowledge into skill files. Use when Michael pastes a YouTube URL about
  AI tools, prompting, image generation, video generation, Midjourney, FLUX, Kling, Runway,
  Seedance, ComfyUI, Stable Diffusion, or any AI creative workflow. Keywords: learn from this,
  watch this, what does this teach, upgrade your skills, digest this video, ai tutorial, prompting
  tutorial, youtube ai.
version: 1.0.0
status: active
created: 2026-03-26
updated: 2026-03-26
owner: Crea
agents: [Crea]
departments: [AI Creatorship]
purposes: [Learning, Skill Upgrade, Knowledge Base]
tags:
  - youtube
  - learning
  - ai-creatorship
  - skill-upgrade
  - prompting
  - image-gen
  - video-gen
  - supadata
depends_on: [supadata]
---

# crea-youtube-learn

**Purpose:** Watch a YouTube video about AI creative tools or techniques. Extract what actually upgrades Crea's craft. If the video teaches something worth encoding — update or create a skill.

**Engine:** `supadata` skill handles all transcript and metadata fetching. Read `supadata/SKILL.md` for full API reference. Key decision: use **Transcript** for narrated content; use **Extract** (vision) when prompts/settings are shown on screen but not spoken aloud (e.g. ComfyUI node graphs, Midjourney UI, on-screen prompt text).

---

## Triggers

- YouTube URL pasted (AI creative / prompting / tool tutorial context)
- "learn from this"
- "watch this"
- "what does this teach"
- "does this have good prompting technique"
- "upgrade your skills from this"
- "digest this AI tutorial"

---

## Extraction Priority — AI Creatorship Only

What Crea is hunting for:

- **Prompting techniques** — exact prompt structures, templates with [BLANKS], model-specific rules
- **Model-specific craft** — what works/doesn't in Midjourney, FLUX, Nano Banana, Kling, Runway, Seedance, etc.
- **Generation workflows** — "If I need X, do Y → Z" pipelines
- **Tool discoveries** — new models, new features, new techniques circulating in the community
- **Visual direction craft** — lighting language, camera language, composition rules that translate to prompts
- **Negative findings** — techniques that are hyped but don't work (equally valuable)

**Not in scope for this skill:** marketing strategy, content repurposing, copywriting, SEO, social media tactics → use `laniameda-youtube-digest` instead.

**Golden rule:** If it can't be applied to a prompt or workflow immediately — it's not specific enough. Inspiration without technique = skip.

---

## Workflow

### Step 1 — Fetch metadata
Use `supadata` skill → `/youtube/video` endpoint. Check description for linked prompts, swipe files, preset downloads, "link in bio" resources → fetch with `web_fetch` if relevant.

### Step 2 — Fetch transcript or extract
Use `supadata` skill:
- **Narrated content** → `/youtube/transcript?url=<URL>&text=true` (native captions, 1 credit)
- **Visual-heavy tutorial** (prompts on screen, UI demos, ComfyUI graphs) → `/extract` with vision (see supadata skill for schema). Use when important technique content is shown but not spoken.
- If transcript returns no content → retry without `lang` param, or fall back to Extract.

### Step 3 — Fast verdict (deliver this first, always)

```
[VIDEO TITLE] — [Channel] (~Xmin)

What it is: [one sentence — what technique/tool/workflow they demonstrate]

Verdict: LEARN / PARTIAL / SKIP

Why:
• [specific reason — what's new or useful]
• [what model(s) this applies to]
• [what's missing or weak]

Skill impact: [which existing skill this would update, or "new skill warranted"]

Preview:
• [Technique/finding 1]: [one line]
• [Technique/finding 2]: [one line]
• [Prompt example if shown]: [exact or close]

Deep digest? (yes / skip / partial)
```

### Step 4 — Deep digest (on approval)

Extract ONLY:
- Exact prompts shown or described (copy-paste ready)
- Model-specific rules ("in Kling v2.5, X causes Y")
- Step-by-step generation workflows
- Tool settings, parameters, version numbers
- Technique verdicts (works / doesn't work / when to use)
- Direct quotes if they capture a principle cleanly

Skip: channel intros, sponsor segments, generic motivation, vague "AI is amazing" takes.

### Step 5 — Save to KB

Location: `~/work/laniameda/laniameda-hq/content-kb/sources/youtube/YYYY-MM-DD-<slug>/`

Files:
- `meta.json` — title, url, channel, date, verdict, models_mentioned, techniques, tags
- `digest.md` — full extraction
- `prompts.md` — exact prompts/templates only
- `techniques.md` — technique verdicts and model-specific rules

### Step 6 — Skill encoding check

Read `references/skill-upgrade-protocol.md` for the full decision tree.

**Short version:**
After saving to KB, ask: *does this video teach something Crea doesn't already know?*

- **Yes, it refines an existing skill** → propose a patch to the relevant SKILL.md, ask Michael to approve before writing
- **Yes, it warrants a new skill** → propose skill name + one-line purpose, ask Michael to approve, then build it using skill-creator
- **No, KB save is enough** → done

Always ask before writing to any SKILL.md or creating a new skill folder.

---

## Hard Rules

- Verdict first, always — never dump transcript unprompted
- SKIP verdict if video is: generic AI hype, tool demos with no technique depth, "10 prompts you need" lists with no explanation of why they work
- Never paraphrase technique — extract the actual rule, the actual prompt, the actual finding
- Model specificity matters — "works in Midjourney" ≠ "works in FLUX" — always tag the model
