# Convex Interface Reference

**Source of truth — always read these files before modifying the ingest script if the schema may have changed:**

- Action: `/Users/michael/work/wannasay-ai/prompt-storager/prompt-storager/convex/ingest.ts`
- Schema: `/Users/michael/work/wannasay-ai/prompt-storager/prompt-storager/convex/schema.ts`
- Folders: `/Users/michael/work/wannasay-ai/prompt-storager/prompt-storager/convex/folders.ts`
- Tags: `/Users/michael/work/wannasay-ai/prompt-storager/prompt-storager/convex/tags.ts`

## Current `ingestFromApi` action args (as of Feb 2026)

```ts
{
  ownerUserId: string          // required — use Telegram sender_id
  promptText?: string          // prompt or text content
  url?: string                 // remote image/video URL to fetch and store
  file?: {                     // inline file upload
    base64: string
    fileName?: string
    contentType?: string
  }
  tagNames?: string[]          // tags to apply (auto-guessed from content too)
  folderId?: string            // Convex folder ID (Id<"folders">)
  ingestKey?: string           // dedup key for the asset record — same key = returns existing record
  promptIngestKey?: string     // separate dedup key for the prompt record only
                               // KEY INSIGHT: pass the same promptIngestKey + promptText in multiple
                               // calls to link multiple assets to ONE prompt (variations pattern).
                               // createPrompt checks by_owner_ingestKey index and returns existing
                               // promptId if found — no duplicate prompt is created.
}
```

Returns: `{ assetId?: Id<"assets">, promptId?: Id<"prompts"> }`

## Schema tables (summary)

| Table       | Key fields |
|-------------|-----------|
| `prompts`   | `ownerUserId`, `text`, `tagIds[]`, `folderId`, `ingestKey`, `createdAt` |
| `assets`    | `ownerUserId`, `kind` (image/video), `storageId`, `promptId`, `tagIds[]`, `folderId`, `ingestKey` |
| `tags`      | `name`, `normalized`, `usageCount` |
| `folders`   | `name`, `description` |

## Convex deployment
- URL: `https://perfect-buffalo-375.convex.cloud`
- Mode: dev (no auth required for HTTP API calls)
- Endpoint: `POST /api/action` with `{ path, args }`

## Batch ingestion (skill-side)
The skill script handles batching client-side — pass a JSON array to ingest multiple items in one call.
Each item maps to one `ingestFromApi` call. Convex `ingest.ts` is NOT modified — it stays single-item.
Do NOT use `agent_ingest.ts` / `ingestFromAgentPayload` — that requires a `runId` from the runs table (agent-worker flow).

## When schema changes
1. Read the source files above
2. Update `scripts/ingest.ts` args accordingly
3. Update this file's "Current args" section
