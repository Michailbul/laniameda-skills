---
name: laniameda-x-post
description: >
  Digest and learn from an X/Twitter post about AI creatorship, AI image/video generation,
  prompting, filmography, or creative workflows. Fetches the tweet, follows every linked
  resource autonomously, extracts all actionable techniques, saves to KB, optionally ingests
  to gallery, and encodes new knowledge into skills if warranted.
  Use when Michael pastes an X or Twitter URL about AI tools, prompting, Midjourney, FLUX,
  Kling, Runway, Seedance, ComfyUI, Stable Diffusion, AI filmmaking, or any AI creative workflow.
  Keywords: digest this tweet, learn from this tweet, extract from this post, what does this
  thread teach, ai prompts from tweet, follow this x link, upgrade skills from tweet, mine this,
  grab the prompts from this, digest this x post.
version: 1.0.0
status: active
created: 2026-03-28
updated: 2026-03-28
owner: Crea
agents: [Crea, Lani]
departments: [AI Creatorship, Marketing]
purposes: [Learning, Ingestion, Research, Prompt Vault, Skill Upgrade, Knowledge Base]
tags:
  - x
  - twitter
  - digest
  - learning
  - ai-creatorship
  - skill-upgrade
  - prompting
  - image-gen
  - video-gen
  - knowledge-base
depends_on: [x-tweet-fetcher, supadata, browser-use-cloud, laniameda-gallery-ingest]
---

# laniameda-x-post

**Purpose:** Mine an X/Twitter post for actionable AI creatorship knowledge. Follow every linked resource — autonomously, in parallel where possible. Extract what's specific and reusable. Save to KB. Optionally ingest strong prompts to gallery. Encode into skills if it clears the bar.

---

## Triggers

- X/Twitter URL pasted (x.com or twitter.com)
- "digest this tweet/post/thread"
- "learn from this tweet/post/thread"
- "what does this thread teach"
- "extract from this x post"
- "follow this link and learn"
- "digest this AI tweet"
- "upgrade your skills from this"
- "grab the prompts from this"
- "mine this"

---

## Topic Filter

**Proceed if the post is about:**
- AI image generation (Midjourney, FLUX, Nano Banana, Stable Diffusion, Ideogram, etc.)
- AI video generation (Kling, Runway, Seedance, LTX, Sora, Pika, Hailuo, etc.)
- Prompt engineering / prompting techniques
- Visual storytelling / cinematography with AI
- AI creative workflows (ComfyUI, ControlNet, img2img, inpainting, LoRA training, etc.)
- AI tools for creators — anything producing visual/audio/video output
- Creative OS / systems (prompt vaults, gallery setups, creative pipelines)

**Skip if:** pure tech/dev with no creative application, finance/crypto, generic motivation with no specifics.
If skipping: one line — what it is and why it's not worth digesting.

---

## Workflow

### Step 1 — Fetch the Tweet

Use `x-tweet-fetcher` — full reference: `references/x-tweet-fetcher.md`.
```bash
python3 ~/.agents/skills/x-tweet-fetcher/scripts/fetch_tweet.py \
  --url "<TWEET_URL>" --pretty
```

Collect:
- Full tweet text (including X Articles / long-form)
- Author + handle
- Stats (likes, views, bookmarks, retweets)
- Quoted tweets — fetch those too
- **All links in the tweet body** — catalogue every one

### Step 2 — Fast Verdict (deliver before going deep)

```
[AUTHOR @handle] — [date]
[Post preview — first 120 chars]

Topic: [ai image / ai video / prompts / filmography / creative workflow / tool]
Relevant: YES / NO / PARTIAL

Verdict: JUICE / WORTH SAVING / SKIP

Why:
* [what's specific and useful]
* [tools / techniques mentioned]
* [linked resources found: list URLs]

Proceed with full extraction? (yes / skip)
```

### Step 3 — Follow All Links (parallel, with subagents)

This is mandatory. Tweets are often teasers — the real technique is in what they link to.

**Spawn subagents in parallel for independent external resources.** Don't wait for one to finish before starting the next — fire them all at once when links are independent.

| Link type | How to handle |
|-----------|--------------|
| YouTube video | Spawn subagent: run `laniameda-youtube-digest` on the URL (uses `references/supadata.md`) |
| Another tweet / thread | Spawn subagent: run `laniameda-x-post` recursively, depth max 2 |
| Instagram reel | Spawn subagent: run `laniameda-instagram-reel-digest` |
| Instagram carousel | Spawn subagent: run `laniameda-instagram-carousel-extract` |
| PDF / Google Doc / Notion / Slides | `web_fetch` first; if gated -> spawn subagent with `browser-use-cloud` |
| External article / blog / Substack | `web_fetch` |
| GitHub / Gist | `web_fetch` -> extract code, prompts, README |
| Linktree / bio link | `web_fetch` -> follow sub-links to prompts/resources |
| ComfyUI workflow JSON | `web_fetch` or download -> save to KB |

**Rule:** Never leave a link unfollowed if it could contain prompts, workflows, or tools. Keep going until all resources are exhausted or confirmed empty.

**When to use a subagent vs inline:**
- Use subagent when: the linked resource is a full video, a long thread, or a gated page that needs browser-use-cloud
- Handle inline when: simple web page, short article, direct PDF — `web_fetch` is sufficient

Collect all subagent results before proceeding to Step 4.

### Step 4 — Full Extraction

Extract ONLY what's specific and actionable. Read `references/extraction-standards.md` for the full field-by-field guide.

**Prompts:**
- Copy the full prompt text verbatim — no paraphrasing
- Note the model it was used with
- Note any parameters, aspect ratios, style keywords, negative prompts
- If a prompt template has [BLANKS] — keep the structure intact

**Workflows:**
- Step-by-step processes ("Step 1: generate base image in X, Step 2: upscale in Y...")
- "If you want [effect], use [tool] with [setting]" mappings
- Tool chains — what connects to what
- Exact settings, values, slider positions
- Platform-specific nuances ("in Kling, X causes Y")

**Tools:**
- Exact tool/model names + version if mentioned
- What they're used for specifically
- Any pricing, limitations, or special capabilities noted
- Comparison advantage over alternatives

**Techniques:**
- Named techniques (ControlNet, inpainting, motion brush, etc.)
- Parameters, settings, numerical values
- Comparisons between tools

**Negative findings** — what doesn't work is as valuable as what does:
- "X doesn't work in [model]"
- "Avoid [technique] because [reason]"
- Hyped approaches that underperform in practice

**Ignore:** "AI is amazing" commentary, generic tips with no specifics, hype without substance.

### Step 5 — Save to KB

Location: `~/work/laniameda/laniameda-hq/content-kb/sources/x-posts/YYYY-MM-DD-<author>-<slug>/`

Files:
```
meta.json           — tweet url, author, date, topic, verdict, tools_mentioned, tags
digest.md           — full extraction (main deliverable)
prompts.md          — all prompts verbatim, model-tagged
techniques.md       — technique verdicts and tool-specific rules
workflows.md        — step-by-step workflows and tool mappings
linked-sources/     — extracted content from each followed link (one file per source)
```

`digest.md` structure:
```markdown
# [Author @handle] — [Date]
Source: [tweet URL]
Topic: [topic]
Tools mentioned: [list]

## The Juice

### Prompts
[verbatim prompts, model-tagged]

### Workflows
[step-by-step]

### Tools + Techniques
[specific, copy-pasteable]

### From Linked Resources
[extracted content from each link — label each source]

## Raw Notes
[anything useful that didn't fit above]
```

### Step 6 — Gallery Ingest (Optional)

If the post contains a strong standalone prompt (especially with a reference image), offer to save it to laniameda.gallery:

```
Found a strong prompt -> save to gallery?
* Prompt: [preview]
* Model: [model]
* Suggested pillar: [creators / cars / designs / dump]
```

Use `laniameda-gallery-ingest` skill to save on approval.

### Step 7 — Skill Encoding Check

Read `references/skill-upgrade-protocol.md` for the full decision tree (if available).

After saving to KB, ask: *does this content teach something we don't already know?*

- **Refines an existing skill** -> propose the patch, wait for Michael's approval, then write
- **Warrants a new skill** -> propose name + purpose + 3-bullet preview, wait for approval, then build with `skill-creator`
- **KB-only** -> done, nothing to encode

Criteria for suggesting skill creation:
- 3+ step workflow that will be used again
- A specific tool combination that's reusable
- A named technique that other agents should know about

New skills go in: `~/work/laniameda/laniameda-hq/laniameda-skills/skills/ai-creatorship/<skill-name>/`

**Always ask before writing to any SKILL.md or creating any new skill folder.**

---

## Extraction Standard — Michael's Priorities

| Interest | What to extract | What to skip |
|----------|----------------|--------------|
| AI image gen | Exact prompts, model name, parameters, style keywords | "Midjourney is great" |
| AI video gen | Prompt structure, motion descriptors, tool + settings | "Kling can do this" |
| Filmography | Camera angles, lighting setups, color grading keywords | "Cinema looks good" |
| Prompt engineering | Templates with [BLANKS], named frameworks | "Be descriptive" |
| Tool workflows | "If X -> use Y with Z setting" | Tool lists without use cases |
| ComfyUI / pipelines | Node connections, workflow JSON, named pipelines | "ComfyUI is powerful" |

**Golden rule:** If Michael can't copy-paste and use it immediately, it's not specific enough. Generics = skip.

---

## Hard Rules

1. **Follow every link.** Incomplete extraction = no value delivered.
2. **Parallel subagents for heavy resources.** Don't serialize what can run in parallel.
3. **Verbatim prompts.** Never paraphrase. Every word and comma matters.
4. **Verdict first.** Don't dump everything upfront. Give verdict -> wait -> go deep.
5. **Never invent specifics.** Vague post = say it's vague. Don't fill gaps.
6. **Save before encoding.** KB save always happens first. Skill conversion is secondary.
7. **Quality gate.** Generic inspiration with no extractable technique = SKIP. Don't manufacture value.

---

## Tool Belt

| Need | Tool | Reference |
|------|------|-----------|
| Fetch tweet + extract text | `x-tweet-fetcher` — `scripts/fetch_tweet.py` | `references/x-tweet-fetcher.md` |
| YouTube in linked resources | spawn subagent -> `laniameda-youtube-digest` | `references/supadata.md` |
| Nested tweet / thread | spawn subagent -> `laniameda-x-post` (max depth 2) | `references/x-tweet-fetcher.md` |
| Instagram reel in links | spawn subagent -> `laniameda-instagram-reel-digest` | — |
| Instagram carousel in links | spawn subagent -> `laniameda-instagram-carousel-extract` | — |
| Web pages, articles, PDFs | `web_fetch` | — |
| Gated / authenticated pages | `browser-use-cloud` | — |
| Save prompt to gallery | `laniameda-gallery-ingest` | — |
| Convert to skill | `skill-creator` (after Michael approves) | — |
| Log task to Notion | `notion-sync` | — |
