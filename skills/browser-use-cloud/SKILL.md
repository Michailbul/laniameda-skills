---
name: browser-use-cloud
description: >
  Cloud browser automation for authenticated websites, dynamic pages, and multi-step web tasks.
  Use when supadata fails for video/social content, or when you need to log in, scroll carousels,
  fill forms, solve CAPTCHAs, or extract from pages that require a real browser session.
  Keywords: browser automation, scrape authenticated site, instagram scroll, extract dynamic page.
version: 1.0.0
status: active
created: 2026-02-01
updated: 2026-03-24
owner: Lani
agents: [Lani]
departments: [Operations]
purposes: [Web Automation, Content Extraction, Browser Automation]
tags:
  - browser-automation
  - instagram
  - web-scraping
  - authenticated-sites
  - captcha
  - browser-use
  - cloud-browser
depends_on: []
replaces: []
allowed-tools: Bash(browser-use-cloud:*)
---

# Browser-Use Cloud: AI Browser Automation

**Purpose:** Browse authenticated websites, extract content from dynamic pages, scroll carousels, fill forms, and perform computer-use tasks using cloud stealth browsers.

**Use AFTER `supadata` fails** for video/social content. Use FIRST for authenticated multi-step web tasks.

---

## What This Skill Does

Runs a real Chromium browser in the cloud with:
- Anti-fingerprinting + CAPTCHA solving
- Cloudflare bypass
- Residential proxies (195+ countries)
- Persistent login profiles (reuse your sessions)

---

## Trigger Conditions

Use when:
- Supadata fails to extract transcript/metadata from social video
- Extracting from an authenticated site (Instagram feed, LinkedIn, X)
- Scrolling through carousels, infinite scroll, paginated content
- Filling forms or clicking through multi-step flows
- Taking screenshots of live authenticated pages

**Do NOT use for:**
- Simple public URL extraction (use `web_fetch`)
- Video transcript (try `supadata` first)
- Web search

---

## Pre-Flight Checks

```bash
# API key
echo "${BROWSER_USE_API_KEY:+OK}" || echo "MISSING"

# Profile (for authenticated sites)
echo "${BROWSER_USE_PROFILE_ID:+OK}" || echo "MISSING"

# SDK
npm list -g browser-use-sdk 2>/dev/null | grep browser-use-sdk || echo "NOT INSTALLED"
```

**Auth:** `BROWSER_USE_API_KEY`
**Base URL:** `https://api.browser-use.com`

---

## SDK Quick Reference (TypeScript)

```typescript
import { BrowserUse } from "browser-use-sdk/v3";
import { z } from "zod";

const client = new BrowserUse(); // uses BROWSER_USE_API_KEY env var

const result = await client.run(
  "Go to <URL>, scroll through all carousel slides. " +
  "VISUALLY READ any text shown in each image and transcribe it exactly. " +
  "Extract image URLs, caption, likes, and hashtags.",
  {
    schema: z.object({ /* your schema */ }),
    model: "bu-mini",       // bu-mini ($0.002/step) or bu-max ($0.03/step)
    proxyCountryCode: "us",
    maxCostUsd: 0.50,
    profileId: process.env.BROWSER_USE_PROFILE_ID,
  }
);
```

---

## Task Prompting Rules

1. **Tell it to USE VISION** — "VISUALLY READ any text shown in the image and transcribe it exactly"
2. **Be specific about what's valuable** — don't say "extract everything"
3. **Tell it how to navigate** — "Scroll through EVERY carousel slide one by one"
4. **Default to bu-mini** — only use bu-max if bu-mini fails

---

## Fallback Chain (for video/social content)

```
supadata → browser-use-cloud → manual
```

Always try supadata first. Only use this skill when Supadata fails or when authenticated browsing is needed.

---

## Models

| Model | Cost/step | Use for |
|---|---|---|
| `bu-mini` | $0.002 | Simple extraction, navigation |
| `bu-max` | $0.03 | Complex visual tasks, multi-step reasoning |

---

## Common Pattern: Instagram Carousel

```typescript
const result = await client.run(
  `Go to ${url}. Scroll through EVERY carousel slide. ` +
  `For EACH slide: VISUALLY READ any text shown in the image. ` +
  `Transcribe the EXACT text. Extract image URL, caption, engagement, hashtags.`,
  {
    schema: CarouselSchema,
    model: "bu-mini",
    proxyCountryCode: "us",
    maxCostUsd: 0.50,
    profileId: process.env.BROWSER_USE_PROFILE_ID,
  }
);
```
