#!/usr/bin/env bun
/**
 * ingest.ts — Save content to Convex prompt-storager KB
 *
 * Usage:
 *   bun run ~/.agents/skills/laniameda-storage/scripts/ingest.ts '<json>'
 *
 * Input: single item object OR array of items.
 * ownerUserId is always read from KB_OWNER_USER_ID env var — never pass it in input.
 *
 * Item fields (see references/convex-interface.md for full schema):
 *   promptText    string   — text/prompt content
 *   tagNames      string[] — tags to apply
 *   folderId      string   — Convex folder ID (optional)
 *   ingestKey     string   — dedup key (auto-generated if omitted)
 *   imagePath     string   — local file path to read and upload
 *   imageBase64   string   — inline base64 image
 *   imageUrl      string   — remote URL to fetch and store
 *   fileName      string   — filename hint
 *   contentType   string   — MIME type hint
 *
 * Output: JSON array of results [{ promptId?, assetId? }, ...]
 */

import { readFileSync, existsSync } from "fs";
import { basename } from "path";
import { createHash } from "crypto";

const CONVEX_URL = "https://perfect-buffalo-375.convex.cloud";

type IngestItem = {
  // ownerUserId intentionally excluded — always read from KB_OWNER_USER_ID env var
  promptText?: string;
  tagNames?: string[];
  folderId?: string;
  ingestKey?: string;
  promptIngestKey?: string;  // shared dedup key for prompt — use same value across variations to link all images to one prompt
  imagePath?: string;
  imageBase64?: string;
  imageUrl?: string;
  fileName?: string;
  contentType?: string;
  // New fields (schema v2)
  modelName?: string;         // e.g. "Midjourney", "FLUX", "Nano Banana Pro", "Runway", "Kling"
  generationType?: "image_gen" | "video_gen" | "ui_design" | "other";
  promptType?: "image_gen" | "video_gen" | "ui_design" | "cinematic" | "ugc_ad" | "other";
  domain?: string;            // freeform: "product photography", "portrait", "architecture", etc.
};

type IngestResult = {
  promptId?: string;
  assetId?: string;
  error?: string;
  input?: string; // short label for context
};

function guessMime(filename: string): string {
  const ext = filename.split(".").pop()?.toLowerCase();
  const map: Record<string, string> = {
    jpg: "image/jpeg", jpeg: "image/jpeg",
    png: "image/png", gif: "image/gif", webp: "image/webp",
  };
  return map[ext ?? ""] ?? "application/octet-stream";
}

function buildArgs(item: IngestItem, ownerUserId: string): Record<string, unknown> {
  const args: Record<string, unknown> = {
    ownerUserId,
    tagNames: item.tagNames ?? [],
  };

  if (item.promptText)       args.promptText = item.promptText.trim();
  if (item.folderId)         args.folderId = item.folderId;
  if (item.promptIngestKey)  args.promptIngestKey = item.promptIngestKey;
  if (item.modelName)        args.modelName = item.modelName;
  if (item.generationType)   args.generationType = item.generationType;
  if (item.promptType)       args.promptType = item.promptType;
  if (item.domain)           args.domain = item.domain;

  // Auto-generate dedup key from content hash
  if (item.ingestKey) {
    args.ingestKey = item.ingestKey;
  } else {
    const raw = [item.promptText ?? "", item.imageUrl ?? "", item.imagePath ?? ""].join("|");
    args.ingestKey = createHash("sha256").update(raw).digest("hex").slice(0, 24);
  }

  // Image: local path > inline base64 > remote url
  if (item.imagePath && existsSync(item.imagePath)) {
    const buf = readFileSync(item.imagePath);
    const fn = item.fileName ?? basename(item.imagePath);
    args.file = {
      base64: buf.toString("base64"),
      fileName: fn,
      contentType: item.contentType ?? guessMime(fn),
    };
  } else if (item.imageBase64) {
    args.file = {
      base64: item.imageBase64,
      fileName: item.fileName ?? "image.jpg",
      contentType: item.contentType ?? "image/jpeg",
    };
  } else if (item.imageUrl) {
    args.url = item.imageUrl;
  }

  return args;
}

async function ingestOne(item: IngestItem, ownerUserId: string): Promise<IngestResult> {
  const args = buildArgs(item, ownerUserId);
  const response = await fetch(`${CONVEX_URL}/api/action`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ path: "ingest:ingestFromApi", args }),
  });

  const result = await response.json() as { status: string; value?: unknown; errorMessage?: string };

  if (result.status === "success") {
    return result.value as IngestResult;
  } else {
    return {
      error: result.errorMessage ?? JSON.stringify(result),
      input: item.promptText?.slice(0, 60) ?? item.imagePath ?? item.imageUrl ?? "unknown",
    };
  }
}

// --- Main ---

const rawArg = process.argv[2];
if (!rawArg) {
  console.error("Usage: bun run ingest.ts '<json>'  (single item or array)");
  process.exit(1);
}

let input: IngestItem | IngestItem[];
try {
  input = JSON.parse(rawArg);
} catch (e) {
  console.error("Invalid JSON:", (e as Error).message);
  process.exit(1);
}

const ownerUserId = (process.env.KB_OWNER_USER_ID ?? "278674008").trim();
const items: IngestItem[] = Array.isArray(input) ? input : [input];

if (items.length === 0) {
  console.error("No items to ingest.");
  process.exit(1);
}

const results: IngestResult[] = [];
for (const item of items) {
  const result = await ingestOne(item, ownerUserId);
  results.push(result);
}

// Single item → single object output. Batch → array.
if (items.length === 1) {
  console.log(JSON.stringify(results[0]));
} else {
  console.log(JSON.stringify(results, null, 2));
}

// Exit with error code if any item failed
const hasErrors = results.some(r => r.error);
if (hasErrors) process.exit(1);
