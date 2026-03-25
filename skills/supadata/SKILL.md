---
name: supadata
version: 1.0.0
status: active
created: 2026-03-24
updated: 2026-03-24
owner: Lani
agents: [Lani, Meda, Persey]
departments: [Operations, Marketing]
purposes: [Ingestion, Research, Transcription]
tags:
  - transcript
  - metadata
  - instagram
  - tiktok
  - youtube
  - twitter
  - facebook
  - video-extraction
  - supadata
  - social-media
depends_on: []
replaces: []
---

# Supadata — Platform-Agnostic Video Transcript & Metadata

**Purpose:** Extract transcripts and metadata from any supported social video URL — Instagram, TikTok, YouTube, Twitter/X, Facebook — without opening a browser.

**Always use this BEFORE browser-use-cloud for any video URL.**

---

## What This Skill Does

Calls the Supadata API to:
1. Fetch transcript (spoken audio → text) from social videos
2. Fetch metadata (title, author, description, engagement, duration)
3. AI-extract structured data from a video (tools, prompts, workflows)

Supports: YouTube, Instagram, TikTok, Twitter/X, Facebook, direct video file URLs.

---

## Trigger Conditions

Use this skill whenever:
- User shares a video URL (Instagram reel, TikTok, YouTube, X video, Facebook)
- User asks to "transcript", "transcribe", "watch", "digest", "summarize", "what does she say"
- User asks "what's in this video" or "extract from this reel"
- Any content ingestion task starting from a video link

**Priority: Always try Supadata before browser-use-cloud.**

---

## Pre-Flight Check

```bash
echo "${SUPADATA_API_KEY:+SET}" || echo "MISSING"
```

If missing:
> "I need `SUPADATA_API_KEY`. Add it to `/root/.openclaw/.env` and restart the gateway."

**Auth header:** `x-api-key: $SUPADATA_API_KEY`
**Base URL:** `https://api.supadata.ai/v1`

---

## Endpoints Reference

### Transcript (primary — all platforms)
```bash
curl -s "https://api.supadata.ai/v1/transcript?url=<VIDEO_URL>&text=true" \
  -H "x-api-key: $SUPADATA_API_KEY"
```
- `text=true` → plain text (use by default)
- `text=false` → timestamped segments
- `lang=en` → optional language hint

**If response has `jobId`** (async):
```bash
curl -s "https://api.supadata.ai/v1/transcript/<jobId>" \
  -H "x-api-key: $SUPADATA_API_KEY"
```
Poll until `status = done`. Wait 3–5s between polls.

### Metadata (all platforms)
```bash
curl -s "https://api.supadata.ai/v1/metadata?url=<VIDEO_URL>" \
  -H "x-api-key: $SUPADATA_API_KEY"
```
Returns: title, author, description, engagement metrics, thumbnail, duration.

### AI Extract (structured data from video)
Use when you need structured output — extract tools, prompts, workflows:
```bash
curl -s "https://api.supadata.ai/v1/extract" \
  -X POST \
  -H "x-api-key: $SUPADATA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "<VIDEO_URL>",
    "prompt": "Extract all prompts, workflows, and tool names shown or mentioned in this video."
  }'
# Returns jobId → poll /v1/extract/<jobId>
```

### YouTube-specific (better quality for YouTube)
```bash
curl -s "https://api.supadata.ai/v1/youtube/transcript?url=<YOUTUBE_URL>&text=true" \
  -H "x-api-key: $SUPADATA_API_KEY"
```

---

## Platform Routing

| URL pattern | Transcript endpoint | Metadata endpoint |
|---|---|---|
| `youtube.com` / `youtu.be` | `/v1/youtube/transcript` | `/v1/youtube/video` |
| `instagram.com` | `/v1/transcript` | `/v1/metadata` |
| `tiktok.com` | `/v1/transcript` | `/v1/metadata` |
| `twitter.com` / `x.com` | `/v1/transcript` | `/v1/metadata` |
| `facebook.com` / `fb.com` | `/v1/transcript` | `/v1/metadata` |

---

## Execution Protocol

1. **Check API key** — fail fast if missing
2. **Detect platform** from URL
3. **Fetch metadata first** — fast, often has description with full workflow text
4. **Fetch transcript** — plain text, async if jobId returned
5. **If transcript fails** → try `/v1/extract` with descriptive prompt
6. **Deliver output** → combine metadata + transcript
7. **If user said "digest"** → hand off to `youtube-digest` skill at Step 3

---

## Fallback Chain

```
Supadata transcript → Supadata AI extract → browser-use-cloud → manual
```

Never skip to browser-use-cloud while Supadata paths are viable.

---

## Output Format

```
**[Title]** — @[author] ([platform])

**Transcript:**
[full plain-text transcript]

**Metadata:**
- Duration: Xs
- Description: [text]
- Tags: [list]
```

---

## Hard Rules

- Always Supadata first. Never browser for video URLs without trying this.
- If transcript unavailable → use `/v1/extract` before giving up.
- If video is non-English → return as-is, optionally translate.
- If `jobId` returned → poll to completion, don't return empty result.
- Always report which path was used (transcript / extract / fallback).
