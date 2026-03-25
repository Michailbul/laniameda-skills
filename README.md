# @laniameda/skills

Private agent skills for the Laniameda studio. Install to Claude Code, OpenClaw, Codex, Cursor, and other AI agents.

```bash
npx skills add Michailbul/laniameda-skills
```

## Update

```bash
npx skills update Michailbul/laniameda-skills
```

---

## Skill Folders

### utility/
General-purpose tools. No domain opinion — used by other skills as engines.

| Skill | What it does |
|---|---|
| `supadata` | Transcript + metadata from any video URL (YouTube, Instagram, TikTok, X, Facebook) |
| `browser-use-cloud` | Cloud browser automation — authenticated sites, CAPTCHA bypass, visual extraction |
| `deepgram-transcribe` | Audio file → text via Deepgram Nova-2 |
| `notion-sync` | Sync tasks to laniameda Notion kanban board |
| `repo-kanban-pm` | Install PM workflow (kanban, ROADMAP, cron review) into any repo |
| `andromeda-messages` | CRUD for Andromeda Galaxy page nodes |
| `x-tweet-fetcher` | Fetch tweets, reply threads, and user timelines from X/Twitter — no login, no API key. Includes X-Tracker for viral growth monitoring. |
| `parallel-deep-research` | Deep multi-source web research via Parallel AI — parallel query execution, synthesis across sources. |
| `parallel-web-search` | Fast web search via Parallel AI — multiple queries in parallel, structured results. |

### ai-creatorship/
Skills for generating and creating with AI — images, video, prompts, knowledge base.

| Skill | What it does |
|---|---|
| `nano-banana-pro` | Generate/edit images with Nano Banana 2 (Gemini 3 Pro Image) |
| `image-to-prompt` | Reverse-engineer any image into a structured cinematic prompt |
| `ai-video-prompting` | Write AI video prompts (Kling, Seedance, Runway) |
| `frame-vfx-stylizer` | Stylize video frame-by-frame with AI graphic effects |
| `laniameda-kb` | Save prompts, images, tutorials to the laniameda.gallery vault |
| `laniameda-x-post-digest` | Digest X/Twitter posts about AI creatorship — extract prompts, workflows, tools. Follows all linked resources (PDFs, videos, threads). Offers skill conversion. |
| `crea-cinematic-prompts` | Turn a concept into cinematic AI still + video prompts using structured semantic control (subject, scene, composition, lighting, style, constraints). |
| `laniameda-storage` | Save pillar-tagged prompts + references to storage |

### web-design/
Design, visual output, and branded content production.

| Skill | What it does |
|---|---|
| `laniameda-brand-design` | Full laniameda design system + Pencil workflow for marketing pages |
| `product-visual-generator` | AI product photography pipeline (Nano Banana 2 + Claude Code) |
| `carousel-designer` | Generate branded LinkedIn carousel slides (HTML → PDF/PNG) |
| `carousel-orchestrator` | End-to-end carousel pipeline: brief → Codex → review → deliver |
| `social-media-carousels` | Design and produce high-engagement social media carousel slides as rendered HTML images. No external dependencies. |

### marketing/
Content intelligence, digestion, creation, and standards.

| Skill | What it does |
|---|---|
| `laniameda-youtube-digest` | Watch YouTube video → extract tools/prompts/workflows → save to KB |
| `laniameda-instagram-reel-digest` | Watch Instagram reel → extract what's actionable → save to KB |
| `laniameda-instagram-carousel-extract` | Extract text/prompts from Instagram carousel slides → save to KB |
| `viral-psychology-hooks` | Content ideation using neuroscience-backed viral triggers |
| `human-copy-standards` | Copy quality gate — kills AI-speak, inflation words, filler |
| `laniameda-hq-update` | Update studio ground truth docs when Michael shares decisions |

### ai-development/
Dev infrastructure skills. *(empty — ready for new skills)*

### general/
Anything that doesn't fit cleanly elsewhere. *(empty — ready)*

### deprecated/
Superseded skills kept for reference only. Do not install.

| Skill | Replaced by |
|---|---|
| `instagram-extract` | `laniameda-instagram-reel-digest` + `laniameda-instagram-carousel-extract` |
| `youtube-digest` | `laniameda-youtube-digest` |

---

## Adding a new skill

1. Pick the right folder based on the skill's purpose
2. Create `skills/<folder>/<skill-name>/SKILL.md`
3. **`description:` frontmatter is required** — `npx skills` silently skips skills without it
4. Update `AGENTS.md` with what changed and which agents need to act
5. `git commit + push`
6. Copy/symlink to relevant agent workspace(s)

---

Built by [Laniameda](https://github.com/Michailbul)
