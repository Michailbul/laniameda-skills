---
name: crea-x-learn
description: >
  Learn from an X/Twitter post about AI creative tools, prompting, image gen, video gen,
  or creative workflows. Fetches the tweet, follows every linked resource autonomously,
  extracts all actionable technique, and encodes new knowledge into skills if warranted.
  Use when Michael pastes an X or Twitter URL about AI tools, prompting, Midjourney, FLUX,
  Kling, Runway, Seedance, ComfyUI, Stable Diffusion, AI filmmaking, or any AI creative workflow.
  Keywords: learn from this tweet, extract from this post, what does this thread teach,
  digest this x post, ai prompts from tweet, follow this x link, upgrade skills from tweet.
version: 1.0.0
status: active
created: 2026-03-26
updated: 2026-03-26
owner: Crea
agents: [Crea]
departments: [AI Creatorship]
purposes: [Learning, Skill Upgrade, Knowledge Base]
tags:
  - x
  - twitter
  - learning
  - ai-creatorship
  - skill-upgrade
  - prompting
  - image-gen
  - video-gen
depends_on: [x-tweet-fetcher, supadata, browser-use-cloud]
---

# crea-x-learn

**Purpose:** Mine an X/Twitter post for actionable AI creatorship knowledge. Follow every linked resource — autonomously, in parallel where possible. Extract what's specific and reusable. Encode into skills if it clears the bar.

---

## Triggers

- X/Twitter URL pasted (x.com or twitter.com)
- "learn from this tweet/post/thread"
- "what does this thread teach"
- "extract from this x post"
- "follow this link and learn"
- "digest this AI tweet"
- "upgrade your skills from this"

---

## Topic Filter

**Proceed if the post is about:**
- AI image generation (Midjourney, FLUX, Nano Banana, Stable Diffusion, Ideogram, etc.)
- AI video generation (Kling, Runway, Seedance, LTX, Sora, Pika, Hailuo, etc.)
- Prompt engineering / prompting techniques
- Visual storytelling / cinematography with AI
- AI creative workflows (ComfyUI, ControlNet, img2img, inpainting, LoRA training, etc.)
- AI tools for creators — anything producing visual/audio/video output
- Creative systems and pipelines

**Skip if:** pure tech/dev with no creative application, finance/crypto, generic motivation with no specifics.
If skipping: one line — what it is and why it's not worth digesting.

---

## Workflow

### Step 1 — Fetch the Tweet

Use `x-tweet-fetcher`:
```bash
python3 ~/.agents/skills/x-tweet-fetcher/scripts/fetch_tweet.py \
  --url "<TWEET_URL>" --pretty
```

Collect:
- Full tweet text (including X Articles / long-form)
- Author + handle
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
• [what's specific and useful]
• [tools / techniques mentioned]
• [linked resources found: list URLs]

Proceed with full extraction? (yes / skip)
```

### Step 3 — Follow All Links (parallel, with subagents)

This is mandatory. Tweets are often teasers — the real technique is in what they link to.

**Spawn subagents in parallel for independent external resources.** Don't wait for one to finish before starting the next — fire them all at once when links are independent.

| Link type | How to handle |
|-----------|--------------|
| YouTube video | Spawn subagent: run `crea-youtube-learn` on the URL |
| Another tweet / thread | Spawn subagent: run `crea-x-learn` recursively, depth max 2 |
| Instagram reel | Spawn subagent: run `laniameda-instagram-reel-digest` |
| Instagram carousel | Spawn subagent: run `laniameda-instagram-carousel-extract` |
| PDF / Google Doc / Notion / Slides | `web_fetch` first; if gated → spawn subagent with `browser-use-cloud` |
| External article / blog / Substack | `web_fetch` |
| GitHub / Gist | `web_fetch` → extract code, prompts, README |
| Linktree / bio link | `web_fetch` → follow sub-links to prompts/resources |
| ComfyUI workflow JSON | `web_fetch` or download → save to KB |

**Rule:** Never leave a link unfollowed if it could contain prompts, workflows, or tools. Keep going until all resources are exhausted or confirmed empty.

**When to use a subagent vs inline:**
- Use subagent when: the linked resource is a full video, a long thread, or a gated page that needs browser-use-cloud
- Handle inline when: simple web page, short article, direct PDF — `web_fetch` is sufficient

Collect all subagent results before proceeding to Step 4.

### Step 4 — Full Extraction

Extract ONLY what's specific and actionable. Read `references/extraction-standards.md` for the full field-by-field guide.

**Short version:**
- **Prompts** — verbatim, never paraphrased, model-tagged, parameters included
- **Workflows** — step-by-step, "If X → use Y with Z" mappings, tool chains
- **Tools** — exact names + versions + what they do specifically
- **Techniques** — named techniques, settings, numerical values, comparisons
- **Negative findings** — what doesn't work is as valuable as what does

**Ignore:** generic commentary, "AI is amazing" takes, tool mentions without use cases.

### Step 5 — Save to KB

Location: `~/work/laniameda/laniameda-hq/content-kb/sources/x-posts/YYYY-MM-DD-<author>-<slug>/`

```
meta.json           — tweet url, author, date, topic, verdict, tools_mentioned, tags
digest.md           — full extraction (main deliverable)
prompts.md          — all prompts verbatim, model-tagged
techniques.md       — technique verdicts and tool-specific rules
linked-sources/     — extracted content from each followed link (one file per source)
```

### Step 6 — Skill encoding check

Read `references/skill-upgrade-protocol.md` for the full decision tree.

**Short version:**
After saving to KB, ask: *does this content teach something Crea doesn't already know?*

- **Refines an existing skill** → propose the patch, wait for Michael's approval, then write
- **Warrants a new skill** → propose name + purpose + 3-bullet preview, wait for approval, then build with `skill-creator`
- **KB-only** → done, nothing to encode

New skills go in: `~/work/laniameda/laniameda-hq/laniameda-skills/skills/ai-creatorship/<skill-name>/`
Symlinked to: `/root/.openclaw/workspace-crea/skills/<skill-name>`

**Always ask before writing to any SKILL.md or creating any new skill folder.**

---

## Hard Rules

1. **Follow every link.** Incomplete extraction = no value delivered.
2. **Parallel subagents for heavy resources.** Don't serialize what can run in parallel.
3. **Verbatim prompts.** Never paraphrase. Every word and comma matters.
4. **Verdict first.** Don't dump everything upfront. Give verdict → wait → go deep.
5. **Never invent specifics.** Vague post = say it's vague. Don't fill gaps.
6. **Save before encoding.** KB save always happens first. Skill conversion is secondary.
7. **Quality gate.** Generic inspiration with no extractable technique = SKIP. Don't manufacture value.

---

## Tool Belt

| Need | Tool |
|------|------|
| Fetch tweet + extract text | `x-tweet-fetcher` — `scripts/fetch_tweet.py` |
| YouTube in linked resources | spawn subagent → `crea-youtube-learn` |
| Nested tweet / thread | spawn subagent → `crea-x-learn` (max depth 2) |
| Instagram reel in links | spawn subagent → `laniameda-instagram-reel-digest` |
| Instagram carousel in links | spawn subagent → `laniameda-instagram-carousel-extract` |
| Web pages, articles, PDFs | `web_fetch` |
| Gated / authenticated pages | `browser-use-cloud` |
| Convert to skill | `skill-creator` (after Michael approves) |
