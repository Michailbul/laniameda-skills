# Instagram Extract — classification + save rules

## Buckets (pillars)

### 1) Prompts — image creation (Convex via prompt-kb)
Use prompt-kb when the content contains copy-pastable image-gen instructions:
- explicit prompts / prompt recipes / parameter blocks
- negative prompts
- “use this prompt template” style content

Tagging defaults:
- `prompts` + `ai-image` (or `image_gen`) + tool/model tags when known

### 2) Tutorials/knowledge — marketing workflows (local KB)
Save locally when the content is primarily:
- growth/marketing strategy, content frameworks, swipe files
- hooks, positioning, content systems, carousel structure heuristics
- step-by-step tutorials (non-prompt)

Default path:
- `kb/tutorials/instagram/<YYYY-MM-DD>-<short-slug>.md`

### 3) Design systems / design inspiration (local KB)
Save locally when it’s UI/UX patterns and inspiration:
- components, layout patterns, typography, spacing systems
- design audits, “why this UI works”, reference breakdowns

Default path:
- `kb/design/instagram/<YYYY-MM-DD>-<short-slug>.md`

### 4) Prompts — web design / development (Convex via prompt-kb)
Use prompt-kb when it’s promptable UI generation instructions:
- landing page / component prompts
- “generate a design system” prompts
- design-to-code prompts

Tagging defaults:
- `prompts` + `ui_design` + tool/model tags when known

## Local KB note contents (keep it useful)
Include:
- source URL
- short summary + key takeaways
- links
- only include extracted text if it adds value (don’t dump everything)

## Ambiguity rule
If it’s partly strategy and partly prompt:
- prefer saving BOTH:
  1) local KB doc with the strategic summary
  2) prompt-kb ingest for the reusable prompt text + example images

If the user wants one: ask which one.
