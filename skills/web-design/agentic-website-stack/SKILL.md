---
name: Agentic Website Stack
description: >-
  Build websites with a full agentic layer — not just frontend, but autonomous
  content publishing, backend dashboard (Kanban CMS), brand corpus as AI brain,
  block-based generative UI, hero image generation, trend scanning, and Convex
  cron-driven agents that write + publish on autopilot. Use when the user says
  "build an agentic website", "website that publishes itself", "autonomous
  content site", "agentic stack", "website with AI agents", "self-publishing
  blog", "SEO autopilot site", or wants to add an agentic content layer to any
  web project.
version: 0.2.0
---

# Agentic Website Stack

Build websites that are more than frontend — they have an autonomous agentic layer that creates, manages, and publishes content without human intervention. The AI writes structured blocks from your brand corpus, generates hero images, scans trends, publishes on schedule, and the site grows on its own.

**Key distinction:** The agent writes *data* (structured content blocks), not *code*. The frontend is a template that renders blocks as real React components. The agent decides *what* content and *which* blocks to use — the frontend decides *how* they look.

---

## Architecture Overview

```
┌─────────────────────────────────────────────────┐
│                   FRONTEND                       │
│   Public site. Renders content blocks as React   │
│   components. Reads from Convex reactively.      │
└────────────────────┬────────────────────────────┘
                     │ reactive queries
┌────────────────────▼────────────────────────────┐
│                    CONVEX                        │
│     Database + Functions + Cron scheduler        │
│     Single source of truth. Everything here.     │
└──────┬─────────────────────────────┬────────────┘
       │ mutations/queries           │ actions (AI calls)
┌──────▼──────────┐          ┌──────▼──────────────┐
│    DASHBOARD    │          │      AGENTS          │
│  Kanban CMS.    │          │  articleWriter       │
│  Human control. │          │  trendScanner        │
│  Auth-gated.    │          │  heroImageGen        │
│  @dnd-kit board │          │  socialPoster        │
└─────────────────┘          └─────────────────────┘
```

**Why Convex (not Supabase + GitHub Actions):**
- Reactive queries = dashboard and frontend update in real-time when agents write. No polling, no refresh.
- Cron jobs are native — no external CI/CD needed for scheduling
- `internalAction` = server-side agent functions. No API auth, no HTTP hops between services.
- Schema is code-first, type-safe, version-controlled
- Single Convex project shared by frontend and dashboard. No sync issues.
- File storage built in — hero images stored alongside content

---

## Stack

| Layer | Tech | Purpose |
|-------|------|---------|
| Frontend + Dashboard | Next.js or Vite + React | Single app, `/admin` routes auth-gated |
| Database + agents | Convex | Shared DB, cron jobs, AI agent actions, file storage |
| AI writing | Anthropic SDK (Claude) | Article generation from brand corpus |
| Image generation | Nano Banana Pro / DALL-E / Flux | Hero images per article |
| Styling | Tailwind CSS | Both public and admin |
| Kanban DnD | `@dnd-kit/core` | Drag-and-drop content pipeline |

---

## Phase 1 — Schema & Database

### Convex Schema

```typescript
// convex/schema.ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

// ── Block types for structured content ──
const blockValidator = v.union(
  v.object({ type: v.literal("paragraph"), content: v.string() }),
  v.object({ type: v.literal("heading"), level: v.union(v.literal(2), v.literal(3)), content: v.string() }),
  v.object({ type: v.literal("image"), src: v.string(), alt: v.string(), caption: v.optional(v.string()) }),
  v.object({ type: v.literal("callout"), variant: v.union(v.literal("tip"), v.literal("warning"), v.literal("note")), content: v.string() }),
  v.object({ type: v.literal("quote"), content: v.string(), attribution: v.optional(v.string()) }),
  v.object({ type: v.literal("list"), ordered: v.boolean(), items: v.array(v.string()) }),
  v.object({ type: v.literal("code"), language: v.string(), code: v.string() }),
  v.object({ type: v.literal("table"), headers: v.array(v.string()), rows: v.array(v.array(v.string())) }),
  v.object({ type: v.literal("cta"), heading: v.string(), body: v.string(), buttonText: v.string(), href: v.string() }),
  v.object({ type: v.literal("faq"), items: v.array(v.object({ question: v.string(), answer: v.string() })) }),
  v.object({ type: v.literal("carousel"), images: v.array(v.object({ src: v.string(), alt: v.string(), caption: v.optional(v.string()) })) }),
  v.object({ type: v.literal("embed"), url: v.string(), embedType: v.union(v.literal("youtube"), v.literal("twitter"), v.literal("generic")) }),
);

export default defineSchema({
  // ── Content Pipeline ──
  articles: defineTable({
    title: v.string(),
    slug: v.string(),
    status: v.union(
      v.literal("planned"),
      v.literal("approved"),
      v.literal("writing"),
      v.literal("published"),
      v.literal("draft"),
      v.literal("archived")
    ),
    pillar: v.string(),
    subtopic: v.optional(v.string()),
    targetKeyword: v.optional(v.string()),
    keywordCluster: v.optional(v.string()),
    intentType: v.optional(v.string()),       // informational, commercial, navigational
    priority: v.optional(v.union(v.literal("high"), v.literal("medium"), v.literal("low"))),

    // ── Content (block-based) ──
    blocks: v.optional(v.array(blockValidator)),
    // Fallback: raw HTML/markdown for simple articles or migration
    rawContent: v.optional(v.string()),

    // ── SEO & Meta ──
    excerpt: v.optional(v.string()),
    metaTitle: v.optional(v.string()),
    metaDescription: v.optional(v.string()),
    keywords: v.optional(v.array(v.string())),
    semanticTags: v.optional(v.array(v.string())),
    interlinks: v.optional(v.array(v.string())),
    faqs: v.optional(v.array(v.object({ question: v.string(), answer: v.string() }))),

    // ── Hero Image ──
    heroImageId: v.optional(v.id("_storage")),
    heroImageUrl: v.optional(v.string()),

    // ── Publishing ──
    authorName: v.optional(v.string()),
    publishedAt: v.optional(v.number()),
    createdAt: v.number(),
    updatedAt: v.number(),
    isAutoMode: v.boolean(),
  })
    .index("by_status", ["status"])
    .index("by_pillar", ["pillar"])
    .index("by_slug", ["slug"])
    .index("by_published", ["publishedAt"]),

  // ── Brand Corpus (the AI brain) ──
  // Uses category/key pattern for organized, queryable corpus entries
  brandCorpus: defineTable({
    category: v.string(),  // e.g. "voice", "positioning", "content", "identity", "cta"
    key: v.string(),       // e.g. "guide", "banned_phrases", "offers", "author"
    content: v.string(),
    updatedAt: v.number(),
  })
    .index("by_category", ["category"])
    .index("by_category_key", ["category", "key"]),

  // ── Content Strategy ──
  topicClusters: defineTable({
    pillar: v.string(),
    subtopics: v.array(v.string()),
    keywords: v.array(v.string()),
    priority: v.number(),
    articlesPlanned: v.number(),
  }).index("by_priority", ["priority"]),

  // ── Agent Logs ──
  agentLogs: defineTable({
    agent: v.string(),         // "article_writer", "trend_scanner", "image_gen"
    action: v.string(),        // "write_article", "scan_trends", "generate_hero"
    description: v.string(),
    status: v.union(v.literal("completed"), v.literal("failed"), v.literal("skipped")),
    targetTable: v.optional(v.string()),
    targetId: v.optional(v.string()),
    inputData: v.optional(v.any()),
    outputData: v.optional(v.any()),
    createdAt: v.number(),
  }).index("by_agent", ["agent"]),

  // ── Settings ──
  settings: defineTable({
    key: v.string(),
    value: v.string(),
  }).index("by_key", ["key"]),
});
```

---

## Phase 2 — Brand Corpus

The corpus is what separates AI that writes like *you* from AI that writes generic slop. Uses `category/key` pattern for organized, queryable entries.

### Required corpus entries

| Category | Key | What goes in it |
|----------|-----|----------------|
| `positioning` | `core` | Who you are, what you do, for whom, why it matters |
| `voice` | `guide` | Tone, style rules, energy level. Include 3-5 example paragraphs that nail the voice. |
| `voice` | `banned_phrases` | Kill list — AI-speak, inflation words, industry cliches |
| `voice` | `hooks` | Proven hooks, headlines, openers that performed well |
| `voice` | `tone_examples` | 3-5 paragraphs of actual copy that sounds right |
| `content` | `offers` | Products/services with descriptions, pricing context, target audience per offer |
| `content` | `competitive_landscape` | Key competitors, how you differentiate |
| `content` | `testimonials` | Real quotes from real customers. Names, companies, specifics. |
| `content` | `keyword_clusters` | SEO keyword groups organized by topic pillar |
| `content` | `image_style` | Hero image aesthetic — composition, palette, lighting, mood, what to avoid |
| `cta` | `links` | The actual CTA links the AI should use in articles, with descriptions of when to use each |
| `identity` | `author` | Byline name for articles |

### Convex functions for corpus

```typescript
// convex/brandCorpus.ts
import { mutation, query } from "./_generated/server";
import { v } from "convex/values";

export const set = mutation({
  args: { category: v.string(), key: v.string(), content: v.string() },
  handler: async (ctx, { category, key, content }) => {
    const existing = await ctx.db
      .query("brandCorpus")
      .withIndex("by_category_key", (q) => q.eq("category", category).eq("key", key))
      .first();
    if (existing) {
      await ctx.db.patch(existing._id, { content, updatedAt: Date.now() });
    } else {
      await ctx.db.insert("brandCorpus", { category, key, content, updatedAt: Date.now() });
    }
  },
});

export const get = query({
  args: { category: v.string(), key: v.string() },
  handler: async (ctx, { category, key }) => {
    return await ctx.db
      .query("brandCorpus")
      .withIndex("by_category_key", (q) => q.eq("category", category).eq("key", key))
      .first();
  },
});

export const getAll = query({
  handler: async (ctx) => {
    return await ctx.db.query("brandCorpus").collect();
  },
});

// Build the full context string for agent prompts
export const getFullContext = query({
  handler: async (ctx) => {
    const rows = await ctx.db.query("brandCorpus").collect();
    return rows
      .map((row) => `# ${row.category}/${row.key}\n\n${row.content}`)
      .join("\n\n---\n\n");
  },
});
```

### How to populate

If the user has brand material (Notion export, markdown, JSON) — parse it and split into category/key pairs.

If not, guide through these questions:
1. What does your brand/product do? Who is it for?
2. What's your tone? (casual, authoritative, technical, warm, edgy?)
3. Give me 3-5 paragraphs that sound like you at your best
4. What words/phrases should we never use?
5. What are your products/services?
6. Who are your competitors? How are you different?
7. What are your best customer testimonials?
8. What should hero images look like? (style, palette, mood)
9. What CTAs should articles end with? (links + when to use each)

---

## Phase 3 — Content Strategy

### Convex action to generate strategy

```typescript
// convex/contentStrategy.ts
import { action } from "./_generated/server";
import { api } from "./_generated/api";
import { callAI } from "./lib/ai";

export const generateStrategy = action({
  handler: async (ctx) => {
    const corpus = await ctx.runQuery(api.brandCorpus.getAll);
    const corpusMap: Record<string, string> = {};
    for (const row of corpus) {
      corpusMap[`${row.category}/${row.key}`] = row.content;
    }

    const result = await callAI({
      system: "You are a content strategist specializing in SEO and GEO (generative engine optimization).",
      user: `Based on this brand corpus, generate:
1. 5-8 topic pillars (broad themes the brand should own)
2. 4-6 subtopics per pillar
3. Target keywords per subtopic
4. 30 article ideas distributed across pillars, prioritized by SEO potential

Focus on topic clusters — groups of semantically related content that reinforce each other through interlinking. Each pillar should form a cluster that signals topical authority to both traditional search and LLM discovery.

Brand positioning: ${corpusMap["positioning/core"] || "Not provided"}
Offers: ${corpusMap["content/offers"] || "Not provided"}
Competitive landscape: ${corpusMap["content/competitive_landscape"] || "Not provided"}
Keywords: ${corpusMap["content/keyword_clusters"] || "Not provided"}

Return as JSON:
{
  "clusters": [{ "pillar": "", "subtopics": [], "keywords": [], "priority": 1, "articlesPlanned": 0 }],
  "articles": [{ "title": "", "slug": "", "pillar": "", "subtopic": "", "targetKeyword": "", "keywordCluster": "", "intentType": "informational", "priority": "medium" }]
}`,
    });

    // Save topic clusters
    for (const cluster of result.clusters) {
      await ctx.runMutation(api.topicClusters.create, cluster);
    }

    // Save article ideas as "planned"
    for (const article of result.articles) {
      await ctx.runMutation(api.articles.create, {
        ...article,
        status: "planned",
        isAutoMode: false,
        createdAt: Date.now(),
        updatedAt: Date.now(),
      });
    }

    return { clusters: result.clusters.length, articles: result.articles.length };
  },
});
```

---

## Phase 4 — AI Article Writer Agent

The core agent. Takes an approved article topic, writes structured content blocks, generates a hero image, and publishes.

### Article writer action

```typescript
// convex/agents/articleWriter.ts
import { internalAction } from "../_generated/server";
import { internal, api } from "../_generated/api";
import { v } from "convex/values";
import { callAI } from "../lib/ai";

export const writeArticle = internalAction({
  args: { articleId: v.id("articles") },
  handler: async (ctx, { articleId }) => {
    // 1. Get the article stub
    const article = await ctx.runQuery(api.articles.get, { id: articleId });
    if (!article || article.status !== "approved") return;

    // 2. Mark as writing
    await ctx.runMutation(api.articles.updateStatus, { id: articleId, status: "writing" });

    try {
      // 3. Load brand context + existing articles for interlinking
      const [fullContext, published, ctaRow, authorRow] = await Promise.all([
        ctx.runQuery(api.brandCorpus.getFullContext),
        ctx.runQuery(api.articles.listPublished),
        ctx.runQuery(api.brandCorpus.get, { category: "cta", key: "links" }),
        ctx.runQuery(api.brandCorpus.get, { category: "identity", key: "author" }),
      ]);

      const existingArticles = published.map((a) => `- /blog/${a.slug} — "${a.title}"`).join("\n");
      const ctaLinks = ctaRow?.content || "";
      const authorName = authorRow?.content?.trim() || "Content Agent";

      // 4. Build prompt — request structured blocks, not raw HTML
      const result = await callAI({
        system: `You are a Content Agent. You write articles as structured content blocks optimized for human readers and AI systems.

${fullContext}

${existingArticles ? `\nExisting articles for internal linking:\n${existingArticles}` : ""}

IMPORTANT RULES:
- Write in the brand voice defined above. Follow the voice guide, tone examples, and banned phrases strictly.
- Reading level: 9th grade. Short sentences. Plain words. No jargon.
- Article length: MINIMUM 1,500 words, target 2,000-2,500 words.
- Every paragraph should be a dense, contextually complete semantic unit.
- Output ONLY valid JSON — no markdown code fences, no commentary.`,

        user: `Write a full article for this topic:

Title: ${article.title}
Target keyword: ${article.targetKeyword || "not specified"}
Keyword cluster: ${article.keywordCluster || "not specified"}
Intent type: ${article.intentType || "informational"}

Return the article as structured BLOCKS. Each block has a "type" and type-specific fields.

Available block types:
- paragraph: { type: "paragraph", content: "text with <a href>, <strong>, <em> inline HTML" }
- heading: { type: "heading", level: 2 or 3, content: "heading text" }
- image: { type: "image", src: "PLACEHOLDER", alt: "description", caption: "optional" }
- callout: { type: "callout", variant: "tip" | "warning" | "note", content: "text" }
- quote: { type: "quote", content: "text", attribution: "optional source" }
- list: { type: "list", ordered: true/false, items: ["item1", "item2"] }
- code: { type: "code", language: "typescript", code: "..." }
- table: { type: "table", headers: [...], rows: [[...], [...]] }
- cta: { type: "cta", heading: "...", body: "...", buttonText: "...", href: "..." }
- faq: { type: "faq", items: [{ question: "...", answer: "..." }] }

Article structure:
1. Hook paragraph — provocative statement, vivid anecdote, or counterintuitive claim
2. Problem — name the specific pain
3. Failed solutions — why what they've tried hasn't worked
4. The reframe — shift perspective
5. The framework/solution — systematic approach
6. Proof — reference case studies/testimonials from brand context
7. CTA block — use one of these links (pick most relevant): ${ctaLinks}
8. FAQ block — 4-6 questions a reader would ask after reading

SEO requirements:
- Use heading blocks with level 2 as questions (good for GEO/featured snippets)
- Target keyword in first paragraph and at least one heading
- 2-3 internal links as <a href="/blog/slug"> in paragraph content
- Target keyword 3-5 times naturally across paragraphs

For image blocks, set src to "PLACEHOLDER" — hero image will be generated separately.

Return as JSON:
{
  "title": "article title",
  "slug": "url-safe-slug",
  "blocks": [ ...block objects... ],
  "excerpt": "150-200 char excerpt",
  "metaTitle": "SEO title under 60 chars",
  "metaDescription": "meta description under 160 chars",
  "semanticTags": ["tag1", "tag2"],
  "keywords": ["kw1", "kw2"],
  "faqs": [{ "question": "Q?", "answer": "A" }],
  "interlinks": ["slug1", "slug2"]
}`,
      });

      // 5. Generate hero image (non-blocking — article saves even if this fails)
      let heroImageUrl: string | undefined;
      let heroImageId: string | undefined;
      try {
        const imageResult = await ctx.runAction(internal.agents.heroImageGen.generate, {
          title: article.title,
          keyword: article.targetKeyword || result.semanticTags?.[0] || "",
          slug: result.slug,
        });
        heroImageUrl = imageResult?.url;
        heroImageId = imageResult?.storageId;
      } catch {
        // Image gen failed — article still publishes without hero
      }

      // 6. Determine target status
      const publishMode = await ctx.runQuery(api.settings.get, { key: "publish_mode" });
      const targetStatus = article.isAutoMode || publishMode?.value === "autonomous"
        ? "published" : "draft";

      // 7. Save the article
      await ctx.runMutation(api.articles.update, {
        id: articleId,
        blocks: result.blocks,
        excerpt: result.excerpt,
        metaTitle: result.metaTitle,
        metaDescription: result.metaDescription,
        semanticTags: result.semanticTags,
        keywords: result.keywords,
        faqs: result.faqs,
        interlinks: result.interlinks,
        heroImageUrl,
        heroImageId,
        authorName,
        status: targetStatus,
        publishedAt: targetStatus === "published" ? Date.now() : undefined,
        updatedAt: Date.now(),
      });

      // 8. Log the action
      await ctx.runMutation(api.agentLogs.insert, {
        agent: "article_writer",
        action: "write_article",
        description: `Wrote article: ${article.title}`,
        status: "completed",
        targetTable: "articles",
        targetId: articleId,
        inputData: { articleId, targetKeyword: article.targetKeyword },
        outputData: {
          slug: result.slug,
          blockCount: result.blocks.length,
          wordCount: result.blocks
            .filter((b: any) => b.type === "paragraph")
            .reduce((sum: number, b: any) => sum + b.content.split(/\s+/).length, 0),
          publishMode: targetStatus,
          hasHeroImage: !!heroImageUrl,
        },
        createdAt: Date.now(),
      });

      return { status: targetStatus, title: article.title };
    } catch (error) {
      // Revert status on failure
      await ctx.runMutation(api.articles.updateStatus, { id: articleId, status: "approved" });

      await ctx.runMutation(api.agentLogs.insert, {
        agent: "article_writer",
        action: "write_article",
        description: `Failed: ${article.title} — ${error instanceof Error ? error.message : "unknown"}`,
        status: "failed",
        targetTable: "articles",
        targetId: articleId,
        createdAt: Date.now(),
      });

      throw error;
    }
  },
});
```

### AI helper with JSON repair

```typescript
// convex/lib/ai.ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

export async function callAI({ system, user }: { system: string; user: string }): Promise<any> {
  const response = await client.messages.create({
    model: "claude-sonnet-4-6-20250514",
    max_tokens: 8192,
    system,
    messages: [{ role: "user", content: user }],
  });

  const text = response.content[0].type === "text" ? response.content[0].text : "";

  // Parse JSON — handle code fences, control chars, unescaped quotes
  const sanitized = text.replace(/[\x00-\x1F\x7F]/g, " ");
  const repaired = repairJsonQuotes(sanitized);

  // Try direct parse, then fence extraction, then bracket matching
  try { return JSON.parse(repaired.trim()); } catch {}

  const fenceMatch = repaired.match(/```(?:json)?\s*(\{[\s\S]*?\})\s*```/);
  if (fenceMatch) {
    try { return JSON.parse(fenceMatch[1]); } catch {}
  }

  // Bracket matching fallback
  const start = repaired.indexOf("{");
  if (start === -1) throw new Error("No JSON found in AI response");
  let depth = 0, end = -1, inStr = false, esc = false;
  for (let i = start; i < repaired.length; i++) {
    const c = repaired[i];
    if (esc) { esc = false; continue; }
    if (c === "\\") { esc = true; continue; }
    if (c === '"') { inStr = !inStr; continue; }
    if (inStr) continue;
    if (c === "{") depth++;
    if (c === "}") { depth--; if (depth === 0) { end = i; break; } }
  }
  if (end === -1) throw new Error("Incomplete JSON in AI response");
  return JSON.parse(repaired.slice(start, end + 1));
}

// Fix unescaped double quotes inside JSON string values
function repairJsonQuotes(text: string): string {
  const result: string[] = [];
  let inString = false, escapeNext = false;
  for (let i = 0; i < text.length; i++) {
    const char = text[i];
    if (escapeNext) { result.push(char); escapeNext = false; continue; }
    if (char === "\\") { result.push(char); escapeNext = true; continue; }
    if (char === '"') {
      if (!inString) { inString = true; result.push(char); }
      else {
        let j = i + 1;
        while (j < text.length && text[j] === " ") j++;
        const next = text[j];
        if (next === ":" || next === "," || next === "}" || next === "]" || next === undefined) {
          inString = false; result.push(char);
        } else {
          result.push("\\"); result.push(char);
        }
      }
      continue;
    }
    result.push(char);
  }
  return result.join("");
}
```

### Hero image generator

```typescript
// convex/agents/heroImageGen.ts
import { internalAction } from "../_generated/server";
import { api } from "../_generated/api";
import { v } from "convex/values";

export const generate = internalAction({
  args: { title: v.string(), keyword: v.string(), slug: v.string() },
  handler: async (ctx, { title, keyword, slug }) => {
    // Load image style from brand corpus
    const styleRow = await ctx.runQuery(api.brandCorpus.get, {
      category: "content", key: "image_style",
    });

    const defaultStyle = `Editorial photography style. Clean, modern, professional.
Composition: Minimal, intentional. One clear subject or metaphor.
Color palette: Muted, sophisticated tones with one accent color.
Lighting: Natural, cinematic. Soft shadows, depth of field.
Mood: Confident, authoritative.`;

    const styleGuide = styleRow?.content || defaultStyle;

    const imagePrompt = `Create a hero image for a blog article titled "${title}" (topic: ${keyword}).

${styleGuide}

RULES:
- Visually relate to "${keyword}" — not generic
- ABSOLUTELY NO TEXT, letters, numbers, logos, watermarks
- No stock photo cliches (handshakes, people pointing at screens)`;

    // Use whatever image gen API is available — DALL-E, Nano Banana, Flux
    // This is a placeholder — swap the implementation based on available API
    const imageBuffer = await generateImage(imagePrompt);
    if (!imageBuffer) return null;

    // Upload to Convex file storage
    const storageId = await ctx.storage.store(new Blob([imageBuffer], { type: "image/png" }));
    const url = await ctx.storage.getUrl(storageId);

    return { storageId, url };
  },
});
```

---

## Phase 5 — Trend Scanner Agent

Automatically discovers new content opportunities by scanning Google News RSS.

```typescript
// convex/agents/trendScanner.ts
import { internalAction } from "../_generated/server";
import { api } from "../_generated/api";
import { callAI } from "../lib/ai";

export const scan = internalAction({
  handler: async (ctx) => {
    // 1. Load keyword clusters from corpus
    const keywordsRow = await ctx.runQuery(api.brandCorpus.get, {
      category: "content", key: "keyword_clusters",
    });
    const searchDomains = extractSearchDomains(keywordsRow?.content || "");

    // 2. Fetch headlines from Google News RSS
    const headlines: string[] = [];
    for (const domain of searchDomains) {
      const rssUrl = `https://news.google.com/rss/search?q=${encodeURIComponent(domain)}&hl=en`;
      const res = await fetch(rssUrl);
      const xml = await res.text();
      // Parse XML for <title> tags (simplified — use proper XML parser in production)
      const titles = [...xml.matchAll(/<title>(.*?)<\/title>/g)].map((m) => m[1]).slice(1, 11);
      headlines.push(...titles);
    }

    // 3. Feed to Claude — generate content opportunities
    const corpus = await ctx.runQuery(api.brandCorpus.getFullContext);
    const existing = await ctx.runQuery(api.articles.listAll);
    const existingTitles = existing.map((a) => a.title.toLowerCase());

    const result = await callAI({
      system: `You are a content trend analyst. Given recent headlines and a brand's positioning, suggest article topics that are timely, relevant, and align with the brand.`,
      user: `Recent headlines:\n${headlines.join("\n")}\n\nBrand context:\n${corpus}\n\nExisting articles (don't duplicate):\n${existingTitles.join("\n")}\n\nSuggest 5-10 article ideas. Return as JSON:\n{ "articles": [{ "title": "", "slug": "", "pillar": "", "targetKeyword": "", "priority": "high" | "medium", "intentType": "informational" }] }`,
    });

    // 4. Deduplicate and insert as planned
    let added = 0;
    for (const article of result.articles) {
      const normalized = article.title.toLowerCase();
      if (existingTitles.some((t) => similarity(t, normalized) > 0.8)) continue;

      await ctx.runMutation(api.articles.create, {
        ...article,
        status: "planned",
        isAutoMode: false,
        createdAt: Date.now(),
        updatedAt: Date.now(),
      });
      added++;
    }

    // 5. Log
    await ctx.runMutation(api.agentLogs.insert, {
      agent: "trend_scanner",
      action: "scan_trends",
      description: `Scanned ${headlines.length} headlines, added ${added} new topics`,
      status: "completed",
      outputData: { headlinesScanned: headlines.length, topicsAdded: added },
      createdAt: Date.now(),
    });

    return { headlinesScanned: headlines.length, topicsAdded: added };
  },
});
```

---

## Phase 6 — Cron Jobs

```typescript
// convex/crons.ts
import { cronJobs } from "convex/server";
import { internal } from "./_generated/api";

const crons = cronJobs();

// Write one approved article every day at 8:00 AM UTC
crons.daily(
  "daily-article-writer",
  { hourUTC: 8, minuteUTC: 0 },
  internal.agents.dailyPublish.run
);

// Scan for trending topics every Monday at 9:00 AM UTC
crons.weekly(
  "weekly-trend-scan",
  { dayOfWeek: "monday", hourUTC: 9, minuteUTC: 0 },
  internal.agents.trendScanner.scan
);

export default crons;
```

### Daily publish orchestrator

```typescript
// convex/agents/dailyPublish.ts
import { internalAction } from "../_generated/server";
import { api, internal } from "../_generated/api";

export const run = internalAction({
  handler: async (ctx) => {
    const approved = await ctx.runQuery(api.articles.getNextApproved);
    if (!approved) return { status: "no_articles_approved" };
    return await ctx.runAction(internal.agents.articleWriter.writeArticle, {
      articleId: approved._id,
    });
  },
});
```

---

## Phase 7 — Block-Based Content Rendering

The frontend renders structured blocks as real React components. This is the key architectural choice — the agent writes data, the frontend owns the design.

### Block renderer

```tsx
// src/components/BlockRenderer.tsx
import { ArticleBlock } from "@/types";

export function BlockRenderer({ blocks }: { blocks: ArticleBlock[] }) {
  return (
    <div className="prose prose-lg max-w-none">
      {blocks.map((block, i) => {
        switch (block.type) {
          case "paragraph":
            return <p key={i} dangerouslySetInnerHTML={{ __html: block.content }} />;
          case "heading":
            const Tag = `h${block.level}` as "h2" | "h3";
            return <Tag key={i}>{block.content}</Tag>;
          case "image":
            return (
              <figure key={i}>
                <img src={block.src} alt={block.alt} className="rounded-lg w-full" />
                {block.caption && <figcaption>{block.caption}</figcaption>}
              </figure>
            );
          case "callout":
            return (
              <aside key={i} className={`callout callout-${block.variant}`}>
                {block.content}
              </aside>
            );
          case "quote":
            return (
              <blockquote key={i}>
                <p>{block.content}</p>
                {block.attribution && <cite>— {block.attribution}</cite>}
              </blockquote>
            );
          case "list":
            const ListTag = block.ordered ? "ol" : "ul";
            return (
              <ListTag key={i}>
                {block.items.map((item, j) => <li key={j}>{item}</li>)}
              </ListTag>
            );
          case "code":
            return (
              <pre key={i}><code className={`language-${block.language}`}>{block.code}</code></pre>
            );
          case "table":
            return (
              <table key={i}>
                <thead><tr>{block.headers.map((h, j) => <th key={j}>{h}</th>)}</tr></thead>
                <tbody>
                  {block.rows.map((row, j) => (
                    <tr key={j}>{row.map((cell, k) => <td key={k}>{cell}</td>)}</tr>
                  ))}
                </tbody>
              </table>
            );
          case "cta":
            return (
              <section key={i} className="cta-block">
                <h3>{block.heading}</h3>
                <p>{block.body}</p>
                <a href={block.href} className="cta-button">{block.buttonText}</a>
              </section>
            );
          case "faq":
            return (
              <section key={i} className="faq-block">
                <h2>Frequently Asked Questions</h2>
                {block.items.map((item, j) => (
                  <details key={j}>
                    <summary>{item.question}</summary>
                    <p>{item.answer}</p>
                  </details>
                ))}
              </section>
            );
          case "carousel":
            return (
              <div key={i} className="carousel">
                {block.images.map((img, j) => (
                  <figure key={j}>
                    <img src={img.src} alt={img.alt} />
                    {img.caption && <figcaption>{img.caption}</figcaption>}
                  </figure>
                ))}
              </div>
            );
          case "embed":
            return <div key={i} className="embed-wrapper">{/* render iframe based on embedType */}</div>;
          default:
            return null;
        }
      })}
    </div>
  );
}
```

### Article page using blocks

```tsx
// src/pages/blog/[slug].tsx
import { useQuery } from "convex/react";
import { api } from "@/convex/_generated/api";
import { BlockRenderer } from "@/components/BlockRenderer";

export default function ArticlePage({ slug }: { slug: string }) {
  const article = useQuery(api.articles.getBySlug, { slug });
  if (!article) return <div>Loading...</div>;

  return (
    <article>
      {article.heroImageUrl && (
        <img src={article.heroImageUrl} alt={article.title} className="w-full rounded-xl" />
      )}
      <h1>{article.title}</h1>
      <p className="text-muted">{article.authorName} · {formatDate(article.publishedAt)}</p>

      {article.blocks ? (
        <BlockRenderer blocks={article.blocks} />
      ) : article.rawContent ? (
        <div dangerouslySetInnerHTML={{ __html: article.rawContent }} />
      ) : null}

      {/* FAQ schema.org structured data */}
      {article.faqs && article.faqs.length > 0 && (
        <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": article.faqs.map((faq) => ({
            "@type": "Question",
            "name": faq.question,
            "acceptedAnswer": { "@type": "Answer", "text": faq.answer },
          })),
        })}} />
      )}
    </article>
  );
}
```

---

## Phase 8 — Dashboard (Kanban CMS)

### Key implementation details

**Kanban with `@dnd-kit/core`:**
- 6 columns: Planned → Approved → Writing → Draft → Published → Archived
- Valid move constraints — can't drag out of "writing" (only the agent moves that)
- Optimistic updates — card moves instantly, syncs to Convex in background (Convex reactive queries handle reconciliation automatically)

**Valid drag transitions:**
```typescript
const VALID_MOVES: Record<string, string[]> = {
  planned:   ["approved", "archived"],
  approved:  ["planned", "writing", "archived"],  // drag to writing = trigger AI write
  writing:   [],                                   // only the agent moves out of writing
  draft:     ["published", "archived"],
  published: ["draft", "archived"],
  archived:  ["planned"],
};
```

**Special transitions:**
- Drag Approved → Writing = triggers `writeArticle` action immediately
- Drag Draft → Published = publishes the article
- "Write Now" button on approved cards = same as dragging to Writing

**Auto/Safe mode toggle:**
- Safe mode (default): articles go to Draft for human review
- Autonomous: articles publish directly. Requires confirmation modal.
- Stored in `settings` table, read by agents.

**Dashboard views:**
1. **Kanban board** — pipeline overview, drag-and-drop management
2. **Article editor** — preview rendered blocks + edit individual blocks + publish
3. **Brand corpus editor** — update voice, positioning, banned phrases
4. **Agent logs** — see what agents have done, success/failure, token usage
5. **Settings** — auto/safe mode, cron schedule visibility

**Writing state indicator:**
- Cards in "writing" column show a pulsing green dot + "Agent writing..." text
- "Reset" button appears on cards stuck in writing (for error recovery)

---

## Phase 9 — Frontend Blog

### Blog list page

```tsx
import { useQuery } from "convex/react";
import { api } from "@/convex/_generated/api";

export default function BlogPage() {
  const articles = useQuery(api.articles.listPublished);
  return (
    <div>
      {articles?.map((article) => (
        <a key={article._id} href={`/blog/${article.slug}`}>
          {article.heroImageUrl && <img src={article.heroImageUrl} alt={article.title} />}
          <h2>{article.title}</h2>
          <p>{article.excerpt}</p>
        </a>
      ))}
    </div>
  );
}
```

**SEO for each article:**
- `<title>` from `metaTitle`
- `<meta name="description">` from `metaDescription`
- FAQPage JSON-LD from `faqs`
- Article JSON-LD with author, date, keywords
- For SSR/SSG: use Convex `fetchQuery` in server components

---

## Build Order

1. **Convex schema + functions** — the foundation everything plugs into
2. **Brand corpus** — populate before any agent runs. Garbage in, garbage out.
3. **Content strategy agent** — generates the pipeline of topics
4. **Article writer agent** — test with 3-5 articles manually, verify quality
5. **Hero image gen** — wire up after article quality is confirmed
6. **Trend scanner** — weekly discovery of new topics
7. **Block renderer** — the frontend component library
8. **Dashboard** — Kanban + editor + corpus management
9. **Frontend blog** — public pages wired to Convex
10. **Crons** — enable autonomous mode only after everything is validated

---

## Extending with More Agents

Each agent = one `internalAction` + one trigger (cron, manual, or event).

| Agent | Trigger | What it does |
|-------|---------|-------------|
| Article Writer | Cron daily / manual | Writes structured article blocks from corpus |
| Trend Scanner | Cron weekly | Google News RSS → new planned articles |
| Hero Image Gen | Called by Article Writer | Generates branded hero image per article |
| Social Poster | On publish | Creates X/LinkedIn posts from published articles |
| Email Agent | On publish / on lead | Sends email via Resend when articles publish |
| Lead Processor | On form submit | Scores and stores leads from contact forms |
| Analytics Agent | Cron daily | Aggregates page views, article performance |
| Internal Linker | Cron weekly | Scans published articles, suggests new interlinks |

---

## Hard Rules

- **Brand corpus before automation.** Never start writing without a populated corpus.
- **Test one article manually first.** Before enabling crons, manually trigger one article and review.
- **Safe mode by default.** Start with articles going to draft. Switch to autonomous only after confirming quality.
- **Block-based content.** Agent returns structured blocks, not raw HTML. Frontend owns the design.
- **Log every agent action.** Every write, scan, and generation gets logged with input/output data.
- **Revert on failure.** If article writing fails, revert status to "approved" so the cron can retry.
- **No hosting in this skill.** Deployment is a separate concern.
- **Convex is the single source of truth.** No API bridges between frontend and dashboard.
