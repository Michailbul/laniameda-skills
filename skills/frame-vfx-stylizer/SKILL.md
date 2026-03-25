---
name: frame-vfx-stylizer
version: 1.0.0
status: draft
created: 2026-03-24
updated: 2026-03-24
owner: Lani
source: https://www.instagram.com/reel/DWPEdC_AWOR/
credit: "@lewis_carrot (Саида | Съемка & Монтаж & Ai | Казань)"
agents: [Lani, Persey]
departments: [Marketing, Dev]
purposes: [Content Creation, AI Creatorship, Visual Workflow]
tags:
  - frame-by-frame
  - video-stylization
  - stop-motion
  - mixed-media
  - ai-image-editing
  - cinematic
  - reels
  - vfx
description: >
  Convert source video into stylized frame-by-frame mixed-media animation using AI image editing.
  Three presets: white marker outline, painted background strokes, selective graphic fill.
  Use when asked to: "add hand-drawn overlay", "stop-motion effect", "stylize this video frame by frame",
  "painted brush effect on this clip", "make this look like animated sketch".
---

# Frame VFX Stylizer

**Purpose:** Convert a source video into a stylized frame-by-frame mixed-media animation using AI image editing.

## What This Skill Does

Takes a video → explodes it into frames → runs an AI graphic effect on each frame → reassembles into a stylized clip.

Three effect presets:
1. **White marker outline** — hand-drawn contour lines over subjects
2. **Painted background** — expressive brush strokes in negative space
3. **Selective graphic fill** — partial paint-fill over the hero object

## Required Inputs

| Input | Type | Notes |
|---|---|---|
| `video` | file path or URL | source clip to stylize |
| `preset` | enum | `white-marker-outline` / `painted-background-strokes` / `selective-graphic-fill` |
| `timing_mode` | enum | `stop-motion` (0.2s/frame) or `smooth` (0.04s/frame) |

## Timing Reference

| Mode | Frame duration | fps | Vibe |
|---|---|---|---|
| `stop-motion` | 0.2s | ~5fps | Chunky, stylized, old-school stop-motion |
| `smooth` | 0.04s | ~25fps | Fluid, closer to normal motion |

## Effect Presets

### `white-marker-outline`
```
Preserve the original composition, camera angle, subject identity, pose, clothing,
lighting, and scene structure. Add rough imperfect white hand-drawn marker lines that
trace only selected contours of the main subject and key shapes in the frame. The lines
should feel handmade, slightly torn, expressive, and editorial. Do not redraw the whole
image. Do not replace the subject. Keep the underlying footage visible.
```

### `painted-background-strokes`
```
Preserve the original composition, subject identity, pose, foreground objects, lighting,
and framing. Add expressive painted brush strokes only into the background and
negative-space areas behind the subject. The brush strokes should feel gestural,
cinematic, textured, and emotionally charged. Do not cover the face unless explicitly
requested. Keep the subject readable and realistic.
```

### `selective-graphic-fill`
```
Preserve the original composition, subject identity, pose, lighting, and environment.
Add a selective hand-painted graphic fill over the main subject or chosen object only,
as if part of the hero object is briefly painted over by hand. Keep the effect partial,
deliberate, and editorial. Do not fully repaint the full frame.
```

## Execution Protocol

```bash
# Step 1: Extract frames
ffmpeg -i input.mp4 -vf fps=5 frames/frame_%04d.png   # stop-motion
ffmpeg -i input.mp4 -vf fps=25 frames/frame_%04d.png  # smooth

# Step 2: Apply preset to each frame via image edit model

# Step 3: Rebuild video
ffmpeg -framerate 5 -i frames/processed_frame_%04d.png -c:v libx264 -pix_fmt yuv420p output.mp4
ffmpeg -framerate 25 -i frames/processed_frame_%04d.png -c:v libx264 -pix_fmt yuv420p output.mp4

# Step 4: Add audio back
ffmpeg -i output_video.mp4 -i original.mp4 -c:v copy -c:a aac output_final.mp4
```

## "If X Then Y"

| If you need... | Then use... |
|---|---|
| Rough indie / music video sketch | `white-marker-outline` + `stop-motion` |
| Moody cinematic without touching subject | `painted-background-strokes` |
| Hero-object emphasis hit | `selective-graphic-fill` |
| Too much flicker | Tighten preservation prompt / lower denoise |
