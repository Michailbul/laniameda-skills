---
name: laniameda-x-post-digest
description: >
  Digest an X/Twitter post about AI creatorship, AI video, prompts, filmography, or creative
  workflows. Extracts the juice — prompts, techniques, tool mappings — then follows any linked
  resources (PDFs, threads, external pages) to mine the full picture. Delivers a fast verdict,
  saves findings, and offers to turn it into a skill if it's worth keeping.
  Keywords: x post digest, twitter extract, ai prompts from tweet, digest this tweet, follow this link.
version: 1.0.0
status: active
created: 2026-03-25
updated: 2026-03-25
owner: Crea
agents: [Crea, Lani]
departments: [AI Creatorship, Marketing]
purposes: [Ingestion, Research, Prompt Vault, Skill Building]
tags:
  - x
  - twitter
  - digest
  - prompts
  - ai-creatorship
  - knowledge-base
  - skill-building
depends_on: [x-tweet-fetcher, supadata, browser-use-cloud, laniameda-gallery-ingest]
---

# laniameda-x-post-digest

**Purpose:** Mine an X/Twitter post for actionable AI creatorship value. Follow every linked resource. Save the full extracted output. Offer to convert it into a reusable skill.

---

## Triggers

- X/Twitter URL pasted (x.com or twitter.com)
- "digest this tweet"
- "extract from this post"
- "what's in this thread"
- "grab the prompts from this"
- "follow this link and extract"
- "mine this"

---

## Topic Filter — Only Digest If Relevant

**Proceed if the post is about:**
- AI image generation (Midjourney, FLUX, Nano Banana, Stable Diffusion, etc.)
- AI video generation (Kling, Runway, Seedance, LTX, Sora, Pika, etc.)
- Prompt engineering / prompting techniques
- Filmography / cinematography / visual storytelling with AI
- AI creative workflows (ComfyUI, ControlNet, inpainting, img2img, etc.)
- AI tools for creators (any tool that produces visual/audio/video output)
- Creative OS / systems (prompt vaults, gallery setups, creative pipelines)

**Skip if:**
- Pure tech/dev content with no creative application
- Finance, crypto, business only
- Generic motivation / "AI is the future" takes with no specifics

If skipping: say one clear line — what it is and why it's not worth digesting.

---

## Workflow

### Step 1 — Fetch the Tweet

Use `x-tweet-fetcher`:

```bash
python3 ~/.agents/skills/x-tweet-fetcher/scripts/fetch_tweet.py \
  --url "<TWEET_URL>" --pretty
```

Extract:
- Full tweet text (including long-form / X Articles)
- Author + handle
- Stats (likes, views, bookmarks, retweets)
- Quoted tweets — fetch those too
- All links in tweet body

### Step 2 — Follow All Links

This is mandatory. A tweet is often just a teaser. The real value is in what it links to.

For every link found in the tweet or thread:

| Link type | Tool to use |
|-----------|------------|
| YouTube video | `laniameda-youtube-digest` skill |
| Instagram reel | `laniameda-instagram-reel-digest` skill |
| Instagram carousel | `laniameda-instagram-carousel-extract` skill |
| PDF / Google Doc / Notion | `web_fetch` → if gated, `browser-use-cloud` |
| External article / blog | `web_fetch` |
| Another tweet / thread | `x-tweet-fetcher` recursively |
| Linktree / bio link | `web_fetch` → follow sub-links to prompts/PDFs |
| GitHub / Gist | `web_fetch` → extract code, prompts, README |
| Typefully / Beehiiv / Substack | `web_fetch` |

**Rule:** Never leave a link unfollowed if it could contain prompts, workflows, or tools. Keep going until all resources are exhausted or confirmed empty.

### Step 3 — Topic Check + Fast Verdict

Before deep-digesting, deliver:

```
[AUTHOR @handle] — [date]
[X post preview — first 100 chars]

Topic: [ai image / ai video / prompts / filmography / creative workflow / tool / other]
Relevant: YES / NO / PARTIAL

Verdict: JUICE / WORTH SAVING / SKIP

Why:
• [what's in here]
• [specific tools/prompts mentioned]
• [linked resources found: X YouTube links, X PDFs, X threads]

Proceed with full extraction? (yes / skip)
```

### Step 4 — Full Extraction

Extract ONLY what's specific and actionable:

**Prompts:**
- Copy the full prompt text verbatim — no paraphrasing
- Note the model it was used with
- Note any parameters, aspect ratios, style keywords, negative prompts
- If a prompt template has [BLANKS] — keep the structure intact

**Workflows:**
- Step-by-step processes ("Step 1: generate base image in X, Step 2: upscale in Y...")
- "If you want [effect], use [tool] with [setting]" mappings
- Tool chains — what connects to what

**Tools:**
- Exact tool/model names + version if mentioned
- What they're used for specifically
- Any pricing, limitations, or special capabilities noted

**Techniques:**
- Named techniques (ControlNet, inpainting, motion brush, etc.)
- Parameters, settings, numerical values
- Comparisons between tools

**Ignore:**
- "AI is amazing" commentary
- Generic tips with no specifics
- Hype without substance

### Step 5 — Compile Output File

Save to: `~/work/laniameda/laniameda-hq/content-kb/sources/x-posts/YYYY-MM-DD-<author>-<slug>/`

Files:
```
meta.json         — tweet url, author, date, topic, verdict, tools_mentioned, tags
digest.md         — full extraction (main deliverable)
prompts.md        — all prompts verbatim, model-tagged
workflows.md      — step-by-step workflows and tool mappings
linked-sources/   — extracted content from each followed link (one file per source)
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
Found a strong prompt → save to gallery?
• Prompt: [preview]
• Model: [model]
• Suggested pillar: [creators / cars / designs / dump]
```

Use `laniameda-gallery-ingest` skill to save on approval.

### Step 7 — Skill Conversion Offer

After saving, evaluate: is this a repeatable workflow worth encoding as a skill?

Criteria for suggesting skill creation:
- 3+ step workflow that will be used again
- A specific tool combination that's reusable
- A named technique that other agents should know about

If yes, ask:

```
This contains a repeatable workflow: [workflow name]
Worth turning into a skill? (yes / no)

If yes → I'll draft a SKILL.md for it and save to laniameda-skills for your review.
```

If approved: use `skill-creator` skill or write SKILL.md directly following the laniameda-skills format. Save to appropriate category folder, update README + AGENTS.md.

---

## Extraction Standard — Michael's Priorities

| Interest | What to extract | What to skip |
|----------|----------------|--------------|
| AI image gen | Exact prompts, model name, parameters, style keywords | "Midjourney is great" |
| AI video gen | Prompt structure, motion descriptors, tool + settings | "Kling can do this" |
| Filmography | Camera angles, lighting setups, color grading keywords | "Cinema looks good" |
| Prompt engineering | Templates with [BLANKS], named frameworks | "Be descriptive" |
| Tool workflows | "If X → use Y with Z setting" | Tool lists without use cases |
| ComfyUI / pipelines | Node connections, workflow JSON, named pipelines | "ComfyUI is powerful" |

**Golden rule:** If Michael can't copy-paste and use it immediately, it's not specific enough. Generics = skip.

---

## Hard Rules

1. **Follow every link.** A tweet without following its links is an incomplete extraction. Non-negotiable.
2. **Verbatim prompts.** Never paraphrase a prompt. Copy it exactly — every word, every comma matters.
3. **Fast verdict first.** Don't dump everything at once. Give the verdict, wait for approval, then go deep.
4. **Don't invent specifics.** If the tweet is vague, say it's vague. Don't fill gaps with assumptions.
5. **Save before offering skills.** Always save the digest file first. Skill conversion is secondary.
6. **Quality gate.** If the content is generic inspiration with no extractable juice — say SKIP clearly. Don't manufacture value from noise.

---

## Tool Belt Reference

| Need | Tool |
|------|------|
| Fetch tweet + links | `x-tweet-fetcher` scripts/fetch_tweet.py |
| Video in linked resources | `laniameda-youtube-digest`, `supadata` |
| Instagram reel in links | `laniameda-instagram-reel-digest` |
| Instagram carousel in links | `laniameda-instagram-carousel-extract` |
| Web pages, articles, PDFs | `web_fetch` |
| Authenticated / gated pages | `browser-use-cloud` |
| Save prompt to gallery | `laniameda-gallery-ingest` |
| Convert to skill | `skill-creator` or write SKILL.md directly |
| Log task to Notion | `notion-sync` |
