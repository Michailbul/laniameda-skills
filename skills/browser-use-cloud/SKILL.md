---
name: browser-use-cloud
version: 1.0.0
status: active
created: 2026-02-01
updated: 2026-03-24
owner: Lani
agents: [Lani]
departments: [Operations]
purposes: [Web Automation, Content Extraction]
tags:
  - browser-automation
  - instagram
  - web-scraping
  - authenticated-sites
  - captcha
  - browser-use
  - cloud-browser
description: >
  Cloud browser automation for navigating authenticated websites, extracting content from dynamic pages,
  scrolling carousels, filling forms. Uses Browser-Use Cloud with stealth browsers, CAPTCHA solving,
  and residential proxies. Use when Supadata fails for video/social content, or when authenticated
  multi-step web tasks are needed (Instagram feed, LinkedIn, X). Do NOT use for simple public URLs or
  video transcripts — try supadata first.
allowed-tools: Bash(browser-use-cloud:*)
---

# Browser-Use Cloud: AI Browser Automation

**Use AFTER `supadata` fails** for video/social content. Use FIRST for authenticated multi-step web tasks.

## Pre-Flight

```bash
echo "${BROWSER_USE_API_KEY:+OK}" || echo "MISSING"
echo "${BROWSER_USE_PROFILE_ID:+OK}" || echo "MISSING (needed for authenticated sites)"
```

## SDK Quick Reference

```typescript
import { BrowserUse } from "browser-use-sdk/v3";
const client = new BrowserUse();

const result = await client.run(
  "Go to <URL>. VISUALLY READ any text shown in each image and transcribe it exactly. " +
  "Scroll through EVERY carousel slide one by one. Extract image URLs, caption, hashtags.",
  {
    model: "bu-mini",       // bu-mini ($0.002/step) or bu-max ($0.03/step)
    proxyCountryCode: "us",
    maxCostUsd: 0.50,
    profileId: process.env.BROWSER_USE_PROFILE_ID,
  }
);
```

## Task Prompting Rules

1. **Tell it to USE VISION** — "VISUALLY READ any text shown in the image and transcribe it exactly"
2. **Tell it how to navigate** — "Scroll through EVERY carousel slide one by one"
3. **Default to bu-mini** — only use bu-max if bu-mini fails

## Fallback Chain

```
supadata → browser-use-cloud → manual
```
