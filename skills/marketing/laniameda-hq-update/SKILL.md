---
name: laniameda-hq-update
description: Update the Laniameda HQ ground truth docs at ~/work/laniameda/laniameda-hq/ when Michael shares thoughts, ideas, decisions, or direction about the studio — including brand, vision, values, design aesthetic, content standards, agency positioning, projects, or agent protocols. Trigger when: Michael says "add this to the docs", "update the HQ", "lock this in", "write this down for the studio", shares brand or aesthetic opinions, clarifies what we do/don't do, shares new content rules, describes a project change, or expresses any opinion that should become ground truth for the studio and all agents.
---

# laniameda-hq-update

Ground truth for the studio lives at `~/work/laniameda/laniameda-hq/`. This skill tells you exactly which file to update, how to write it, and what to commit.

## HQ Structure → What Lives Where

```
laniameda-hq/
  company/
    identity.md       ← studio name, stage, founder, core differentiator, mantras
    vision.md         ← north star, 12-month goals, phase arc, what we're NOT building
    values.md         ← core values (numbered), working principles for agents
    manifesto.md      ← full positioning statement (the "feeling" doc — edit rarely)
  agency/
    what-we-do.md     ← service areas: creative + engineering
    how-we-work.md    ← process, philosophy, collaboration model
    clients.md        ← who we work with, who we don't, the filter
  brand/
    visual.md         ← color system, typography, shape, motion, component rules
    voice.md          ← brand voice, tone by surface, vocabulary, what we don't say
    content-standards.md ← content types + specs, quality bar, what gets killed
  departments/
    marketing.md      ← Marketing First principle, content pillars, content engine
    engineering.md    ← tech stack, agent systems, infrastructure, key decisions
    creative.md       ← AI tools in use, prompt vault standards, creative standards
  projects/
    index.md          ← all active projects + repos + status + next steps
  agents/
    roster.md         ← Lani/Meda/Persey roles, domain boundaries, shared rules
```

Read `references/routing.md` for a quick routing guide: which topic → which file.

## How to Update

### 1. Classify what Michael shared

Ask: what category does this belong to?
- **Who we are / what stage / core identity** → `company/identity.md`
- **North star / goals / what we're building toward** → `company/vision.md`
- **How we work / principles / what we care about** → `company/values.md`
- **The brand statement / why we exist** → `company/manifesto.md` (edit rarely)
- **What services we offer** → `agency/what-we-do.md`
- **Process / how we operate** → `agency/how-we-work.md`
- **Client types / who we do/don't work with** → `agency/clients.md`
- **Visual design / colors / typography / aesthetic** → `brand/visual.md`
- **Voice / tone / content quality bar** → `brand/voice.md`
- **Content types / what we post / what we kill** → `brand/content-standards.md`
- **Marketing strategy / content pillars** → `departments/marketing.md`
- **Tech stack / engineering decisions** → `departments/engineering.md`
- **Creative tools / prompt vault / AI models in use** → `departments/creative.md`
- **Project status / new project / repo change** → `projects/index.md`
- **Agent role / domain / rule** → `agents/roster.md`

When in doubt: prefer the most specific file. If it touches multiple files, update all of them.

### 2. Write it in

**Style rules:**
- Match the voice of the existing file — direct, no filler, specific
- Preserve existing structure; add to the right section rather than appending at the bottom
- For "what we don't do" items → add to the relevant ❌ list
- For new values → add as a numbered section with a title + 2–3 sentence description
- For color tokens or design rules → use the table format already in `brand/visual.md`
- For content pillar changes → update the table in both `departments/marketing.md` AND `brand/content-standards.md`
- Update `_Last updated:` date at the bottom of any file you touch

### 3. Commit

```bash
cd ~/work/laniameda/laniameda-hq
git add -A
git commit -m "hq: <short description of what changed>"
```

Good commit messages:
- `hq: lock in warm-dark visual identity, no cold tones`
- `hq: add content standard — no generic AI tips`
- `hq: update vision 12-month goals`
- `hq: add client filter — no clients without a point of view`

## Conversational Capture Pattern

When Michael is talking and drops something that should be locked in — even mid-conversation — capture it immediately. Don't wait until the end.

**Signals to listen for:**
- "we should always..." / "we never..." / "I hate when..."
- "our thing is..." / "that's not us" / "this is exactly what we're about"
- "I want to add this to the docs" / "write this down"
- Strong opinion about a visual, a piece of content, a client type, a way of working
- A description of the aesthetic, the vibe, the feeling

**What to do:**
1. Write it down in the right file immediately
2. Confirm what you captured in 1–2 sentences
3. Commit
4. Keep the conversation going — don't make it a big deal

## Multi-Item Sessions

If Michael shares multiple things across a conversation, batch the writes but commit after each logical group — not all at once at the end. Intermediate commits create better history.

## Content KB — Raw Voice & Source Material

When Michael shares thoughts, ideas, or external content worth reusing for marketing:

→ Save to `~/work/laniameda/laniameda-hq/content-kb/raw-voice/YYYY-MM-DD-slug.md`

**Never** save raw voice or content material to agent workspaces (`workspace-meda/kb/`, etc.) — those are agent-local only and not shared ground truth.

Structure of a raw voice file:
- The raw thought preserved verbatim
- Content angles extracted
- Direct quotes pulled out
- Tone note for Meda

After saving, add a todo to Meda's backlog at `~/.openclaw/workspace-meda/pm/backlog.md` pointing at the file.

## Do Not

- Do not paraphrase or soften strong opinions — preserve the directness
- Do not put content in `company/manifesto.md` unless Michael says something is a manifesto-level statement
- Do not create new files outside the HQ structure without discussing it
- Do not update agent AGENTS.md files — that's a separate operation (ask first)
- Do not store niche project-specific technical details here — those stay in the project repo
- Do not save content/marketing material to agent workspace KB folders — always use `laniameda-hq/content-kb/`

## Verification

After writing, read back the changed section to Michael in 2–4 lines so he can confirm or correct before commit.
