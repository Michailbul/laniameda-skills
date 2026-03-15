---
name: youtube-digest
description: YouTube video digestion for learning and content repurposing. Extracts specific, tactical details from videos (prompts, workflows, tool mappings) and structures them for reuse in marketing and product development. Updated with save-and-repurpose workflow.
metadata:
  laniameda:
    departments: ['Marketing', 'Operations']
    purposes: ['Ingestion', 'PM']
    tags: ['instagram', 'marketing', 'operations', 'youtube']
    status: active
    depends_on: []
    replaces: []
---

# YouTube Digest Skill

**Purpose:** Deep video digestion for tactical learning + content repurposing  
**For:** All agents (Lani, Meda, Persey)  
**Last updated:** 2026-03-05

---

## Trigger Phrases

- "digest this video"
- "save this video for content"
- "extract from this video"
- "learn from this"
- "what's useful in this video"
- Any YouTube URL paste

## Output Standard (Michael)

When asked to digest a video, optimize for **time saved**:
- Return **specifics only** (tools, workflows, prompts, skill/plugin names, implementation steps).
- Explicitly map findings to relevant pillar(s) and interests.
- If video is mostly generic, say so fast and label it low value.

Default answer shape must be **concise + expandable**:
1. **Fast verdict (3–6 bullets)** — what matters / what doesn't
2. **Specifics extracted** — concrete tools, steps, frameworks, commands
3. **Useful for us?** — yes/no + exactly where it applies
4. **Deep dive (optional)** — only when there is genuinely high-leverage detail

---

## Michael's Research Interests (Priority Order)

When digesting videos, prioritize content matching these interests:

### 1. AI Design for Marketing
**What to extract:**
- How to generate carousels with AI
- How to generate PDFs with AI
- AI-assisted design workflows
- Branded system creation with AI

**Specifics needed:**
- Exact prompts for design generation
- Tool names and when to use them
- Step-by-step: prompt → design output
- Design system keywords (tokens, components, etc.)

### 2. Agent Orchestration / Agent Decoding
**What to extract:**
- Workflow architectures (Step 1, Step 2, etc.)
- "If X then Y" tool mappings
- MCP usage patterns
- Skill plugin utilization
- Claude Code life hacks and advanced usage

**Specifics needed:**
- Specific skill names and what they do
- How to chain agents together
- Error handling patterns
- State management between agents

### 3. Prompt Engineering (All Types)
**What to extract:**
- UI design prompts
- Marketing content prompts
- Agent control prompts
- Framework names and structures

**Specifics needed:**
- Copy-pasteable templates with [BLANKS]
- Prompt construction workflows
- Specific keywords that change outputs

### 4. AI Creatorship (Images/Video)
**What to extract:**
- Tool-specific workflows
- Exact prompts with all parameters
- Advanced techniques (ControlNet, inpainting, etc.)

**Specifics needed:**
- "If I need [effect], use [tool]" mappings
- Complete prompt texts
- Settings and parameters

---

## Digestion Workflow

### Default Engine (MANDATORY)

**Always use Supadata first whenever Michael asks to digest a video.**

Rule:
1. Use Supadata transcript/metadata endpoints as the primary ingestion path.
2. Do **not** start with `yt-dlp`, YouTube web scraping, or random transcript sites.
3. Only fallback away from Supadata if API/auth fails — and clearly state fallback was used.

### Supadata Under-the-Hood Reference (embedded)

**Auth:** `x-api-key: $SUPADATA_API_KEY`

**Primary endpoints for this skill:**
- Transcript (default): `GET /v1/youtube/transcript?url=<URL>&text=true&lang=en`
- Transcript (timestamped): `GET /v1/youtube/transcript?url=<URL>&text=false&lang=en`
- Video metadata: `GET /v1/youtube/video?id=<VIDEO_ID>`
- Cross-platform metadata: `GET /v1/metadata?url=<URL>`
- Search (when needed): `GET /v1/youtube/search?query=<QUERY>&type=video&sortBy=views`

**Fallback rule inside this skill:**
- If `/youtube/video` fails due to ID/param mismatch, derive `VIDEO_ID` from URL and retry with `id`.
- If transcript unavailable in `lang=en`, retry without `lang` to use first available language.

### Step 1: Fetch Video Metadata + Description

```bash
curl -s "https://api.supadata.ai/v1/youtube/video?id=<VIDEO_ID>" \
  -H "x-api-key: $SUPADATA_API_KEY"
```

**Check description for:**
- Links to prompts, templates, resources
- "Link in description" mentions
- Free downloads, swipe files

**If external links found:**
- Fetch with `web_fetch`
- Extract prompts, frameworks, templates
- Save to `resources/` folder immediately

### Step 2: Fetch Transcript

```bash
curl -s "https://api.supadata.ai/v1/youtube/transcript?url=<URL>&text=true" \
  -H "x-api-key: $SUPADATA_API_KEY"
```

### Step 3: Fast Verdict

**No-fluff filter:** if you cannot extract copy-pasteable tactics, clearly mark video as low tactical value.

**Reply to Michael in this format:**

```
**[VIDEO TITLE]** — [Channel] (~Xmin)

**What it is:** [One sentence - what they make/show + tools used]

**Verdict:** USEFUL / PARTIAL / SKIP

**Why:**
• [Specific reason - what's non-obvious]
• [What's genuinely new]
• [What's missing/re-chewed]

**Interest Match:** [Which of Michael's interests this serves]
**Novelty:** High / Medium / Low
**Repurposable:** Yes / No — [why]

**Specific findings preview:**
• [Tool name]: [what it does]
• [Prompt/Workflow]: [brief description]
• [Technique]: [brief description]

Digest and save? (yes / skip / partial)
```

### Step 4: Deep Digestion (if approved)

**Extract ONLY:**
- Specific tool names and versions
- Exact prompts (copy-paste ready)
- Step-by-step workflows
- "If X then Y" mappings
- Code snippets
- Command examples

**Format:**

```markdown
## [Video Title] — Deep Digest

### Tools Mentioned
| Tool | Use Case | When to Use |
|------|----------|-------------|
| [name] | [what it does] | [specific scenario] |

### Prompts / Templates
```
[Exact prompt text with [BLANKS]]
```
**Context:** [when to use this]
**Key ingredients:** [what makes it work]

### Workflows
**[Workflow name]:**
1. [Step 1 - specific action]
2. [Step 2 - specific action]
3. [Step 3 - specific action]

### "If X Then Y" Mappings
| If you need... | Then use... | Steps |
|----------------|-------------|-------|
| [specific task] | [specific tool] | [brief steps] |

### Code / Commands
```bash
[exact commands shown]
```

### Key Insights
- [Specific insight 1]
- [Specific insight 2]

### Gaps / What's Missing
- [What wasn't covered]
- [What doesn't work]
```

### Step 5: Save to Learning Repository

**Location:** `~/work/laniameda/laniameda-hq/knowledge-base/sources/youtube/YYYY-MM-DD-slug/`

**Files to create:**

1. **meta.json**
```json
{
  "title": "...",
  "url": "...",
  "channel": "...",
  "date_processed": "YYYY-MM-DD",
  "interests": ["ai-design", "agent-orchestration", "prompt-engineering"],
  "verdict": "useful|partial|skip",
  "tools_mentioned": ["tool1", "tool2"],
  "repurposable": true,
  "marketing_angle": "brief description",
  "tags": []
}
```

2. **digest.md** — Full deep digestion
3. **prompts.md** — Extracted prompts/templates only
4. **workflows.md** — Step-by-step workflows only
5. **tools.md** — Tool mappings and comparisons

### Step 6: Flag for Repurposing

**If content is marketing-ready:**

Create: `~/work/laniameda/laniameda-hq/knowledge-base/marketing-ready/YYYY-MM-DD-slug.md`

```markdown
# Marketing Angle: [Video Title]

**Source:** [URL]
**Original Pillar:** [Michael's content pillar]

## Our Angle
[How to reframe this for laniameda's voice/positioning]

## Key Takeaways to Share
- [Point 1]
- [Point 2]

## Content Formats
- [ ] X thread
- [ ] LinkedIn post
- [ ] Carousel
- [ ] PDF guide

## Original vs Our Version
| Element | Original | Our Version |
|---------|----------|-------------|
| [aspect] | [their approach] | [our approach] |
```

### Step 7: Update This Skill

**If new tools/workflows discovered:**

1. Add tool to "Tools Reference" section below
2. Add workflow pattern to "Common Patterns"
3. Update "Michael's Research Interests" if new category discovered
4. Git commit with message: "skill: add [tool/workflow] from [video]"

---

## Tools Reference (Update as Discovered)

### For Design/Marketing
| Tool | Purpose | Best For |
|------|---------|----------|
| v0.dev | UI generation | React components, landing pages |
| Tempo | AI design | Marketing materials, brand assets |
| Lovable | App prototyping | Quick mockups, demos |
| Claude Artifacts | Component building | Interactive UI elements |
| Canva AI | Design automation | Social posts, presentations |

### For Agent Orchestration
| Tool | Purpose | Best For |
|------|---------|----------|
| OpenClaw | Agent framework | Multi-agent workflows |
| Claude Code | Coding agent | Frontend, full-stack |
| n8n | Workflow automation | Connecting tools |
| Make.com | Automation | Visual workflow building |

### For MCPs (Model Context Protocols)
| MCP | Purpose | Best For |
|-----|---------|----------|
| Browser Use | Web automation | Scraping, form filling |
| GitHub | Code management | Repo operations |
| Supadata | Video/data extraction | YouTube, social content |
| Sequential Thinking | Reasoning | Complex problem solving |

### For Content/Research
| Tool | Purpose | Best For |
|------|---------|----------|
| x-tweet-fetcher | X post extraction | Social research |
| instagram-extract | IG content extraction | Visual research |
| supadata | Video transcripts | YouTube digestion |
| web_fetch | Page extraction | Article research |

---

## Common Patterns (Update as Discovered)

### Pattern: AI Design Workflow
1. Start with prompt in [tool]
2. Iterate on output (2-3 rounds)
3. Export to [format]
4. Refine in [secondary tool]

### Pattern: Agent Chaining
1. Agent 1: [task] → outputs [format]
2. Agent 2: takes [format] → does [task]
3. Agent 3: reviews → final output

### Pattern: Content Repurposing
1. Extract from video → digest.md
2. Identify angle → marketing-ready/
3. Reframe for brand → content draft
4. Create asset → carousel/PDF/post

---

## Repurposing Rules

1. **Extract thesis, not creator's products**
   - Don't name-drop their tools
   - Use their insight, not their branding

2. **Reframe for laniameda voice**
   - Art + engineering + systems
   - Taste-driven, not volume-driven
   - Specific, not generic

3. **Add our proof points**
   - Use our agent examples
   - Reference our workflows
   - Show our results

4. **Never copy-paste**
   - Digest → understand → re-express
   - Our angle, their insight

---

## Checklist Before Delivering

- [ ] Specific tool names mentioned (not "AI tools")?
- [ ] Exact prompts extracted with [BLANKS]?
- [ ] Step-by-step workflows documented?
- [ ] "If X then Y" mappings created?
- [ ] Saved to KB with proper structure?
- [ ] Flagged for repurposing if marketing-ready?
- [ ] Skill updated with new tools/patterns?

---

## Readaptivity

**Log feedback to:** `~/work/laniameda/laniameda-hq/knowledge-base/profile/feedback-log.md`

Format:
```
YYYY-MM-DD | [video slug] | [what was wrong] | [how to fix]
```

**Update this skill** after 3+ similar feedback patterns.

---

*This skill ensures: Every video becomes reusable IP for product and marketing.*
