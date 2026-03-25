---
name: youtube-digest
description: >
  DEPRECATED — use laniameda-youtube-digest instead. Old YouTube video digestion skill kept for
  backwards compatibility.
version: 1.1.0
status: deprecated
created: 2026-02-01
updated: 2026-03-24
owner: Lani
agents: [Lani, Meda]
departments: [Marketing, Operations]
purposes: [Ingestion, Research, Content Repurposing, Knowledge Base]
tags:
  - youtube
  - transcript
  - digest
  - knowledge-base
  - content-repurposing
  - supadata
  - video-research
  - workflows
  - prompts
depends_on: [supadata]
replaces: []
superseded_by: laniameda-youtube-digest
---

# YouTube Digest Skill

**Purpose:** Deep video digestion for tactical learning + content repurposing.
Extracts: tools, prompts, workflows, "if X then Y" mappings, implementation steps.
Saves structured output to laniameda-hq knowledge base.

**Primary engine:** Supadata API (see `supadata` skill).
**Use for:** YouTube first. Also works for Instagram reels, TikTok via Supadata.

---

## Trigger Phrases

- "digest this video"
- "save this video for content"
- "extract from this video"
- "learn from this"
- "what's useful in this video"
- Any YouTube URL paste
- Any social video URL when user wants structured digestion

---

## Output Standard

Optimize for **time saved**. Return specifics only:
- Tools, workflows, prompts, skill/plugin names, implementation steps
- Map findings to Michael's pillars
- If video is mostly generic: say so fast and label it low value

**Default shape:**
1. Fast verdict (3–6 bullets)
2. Specifics extracted
3. Useful for us? yes/no + where it applies
4. Deep dive — only when there's genuinely high-leverage detail

---

## Michael's Research Interests (Priority Order)

### 1. AI Design for Marketing
Extract: carousel/PDF generation, branded systems, AI-assisted design workflows
Specifics: exact prompts, tool names, step-by-step from prompt → design output

### 2. Agent Orchestration
Extract: workflow architectures, "if X then Y" tool mappings, MCP usage, Claude Code hacks
Specifics: skill names, chaining logic, error handling patterns

### 3. Prompt Engineering
Extract: specific templates with [BLANKS], framework names, structured patterns
Specifics: copy-pasteable templates, prompt construction workflows

### 4. AI Creatorship (Images/Video)
Extract: tool-specific workflows, exact prompts, advanced techniques (ControlNet, inpainting)
Specifics: "If I need [effect], use [tool]" mappings, complete prompt texts with settings

### Golden Rule
> If Michael can't copy-paste and use it immediately, it's not specific enough.

---

## Digestion Workflow

### Step 1 — Metadata
```bash
# YouTube
curl -s "https://api.supadata.ai/v1/youtube/video?id=<VIDEO_ID>" \
  -H "x-api-key: $SUPADATA_API_KEY"
```
Check description for: prompt links, "link in description" mentions, free downloads, swipe files.
If external links found → fetch with `web_fetch`, extract prompts/templates, save to `resources/`.

### Step 2 — Transcript
```bash
curl -s "https://api.supadata.ai/v1/youtube/transcript?url=<URL>&text=true" \
  -H "x-api-key: $SUPADATA_API_KEY"
```
- Fallback: remove `lang` param if language-specific fetch fails
- For non-YouTube: use `/v1/transcript?url=<URL>&text=true`

### Step 3 — Fast Verdict

Reply to Michael in this format:
```
**[VIDEO TITLE]** — [Channel] (~Xmin)

**What it is:** [One sentence — what they make/show + tools used]

**Verdict:** USEFUL / PARTIAL / SKIP

**Why:**
• [Specific reason]
• [What's genuinely new]
• [What's missing/re-chewed]

**Interest Match:** [Which of Michael's interests]
**Novelty:** High / Medium / Low
**Repurposable:** Yes / No — [why]

**Specific findings preview:**
• [Tool name]: [what it does]
• [Prompt/Workflow]: [brief description]

Digest and save? (yes / skip / partial)
```

### Step 4 — Deep Digestion (if approved)

Extract ONLY:
- Specific tool names and versions
- Exact prompts (copy-paste ready)
- Step-by-step workflows
- "If X then Y" mappings
- Code snippets / command examples

### Step 5 — Save to KB

**Location:** `~/work/laniameda/laniameda-hq/content-kb/sources/videos/YYYY-MM-DD-slug/`

Files:
- `meta.json` — title, url, channel, date, interests, verdict, tools_mentioned, repurposable, tags
- `digest.md` — full deep digestion
- `prompts.md` — extracted prompts/templates only
- `workflows.md` — step-by-step workflows only
- `tools.md` — tool mappings and comparisons

### Step 6 — Flag for Repurposing

If content is marketing-ready, create:
`~/work/laniameda/laniameda-hq/content-kb/marketing-ready/YYYY-MM-DD-slug.md`

Include: our angle, key takeaways to share, content formats (X thread / carousel / PDF).

---

## Source Fidelity Rule

When saving ingested media: save the **actual source artifact** (video, frame, linked doc, slide image). Never silently replace with summary text or thumbnail and present as complete.

---

## Repurposing Rules

1. Extract thesis, not creator's products — use their insight, not their branding
2. Reframe for laniameda voice — art + engineering + systems, taste-driven
3. Add our proof points — our agent examples, our workflows, our results
4. Never copy-paste — digest → understand → re-express

---

## Checklist Before Delivering

- [ ] Specific tool names mentioned (not "AI tools")?
- [ ] Exact prompts extracted with [BLANKS]?
- [ ] Step-by-step workflows documented?
- [ ] "If X then Y" mappings created?
- [ ] Saved to KB with proper structure?
- [ ] Flagged for repurposing if marketing-ready?
