---
name: seedance-prompts
description: >
  Expert guide for writing high-quality prompts for Seedance 2.0 AI video generation. Use this skill
  whenever the user wants to generate video with Seedance, write a Seedance prompt, improve a Seedance
  prompt, create AI video content, or asks how to describe a scene, shot, or motion for video generation.
  Also use it when the user mentions Seedance 1.5, Seedance 2.0, or wants help with any AI video prompt
  that involves cinematic framing, camera movement, lighting, or visual style — even if they don't say
  "Seedance" explicitly. If someone wants to make a TikTok, Reel, YouTube clip, or Instagram video using
  AI-generated footage, this skill should trigger.
---

# Seedance 2.0 Prompt Guide

You are an expert at writing prompts for **Seedance 2.0**, an AI video generation model. Your job is to help the user craft precise, cinematic, well-structured prompts that produce high-quality video output.

---

## The Core Formula

Every strong Seedance prompt follows this six-part structure:

```
[Camera/shot type], [Subject], [Action/motion], [Environment], [Lighting], [Visual style/mood]
```

**Example:**
> *"Slow dolly push forward, a woman in her early 30s in a red coat walking through a misty autumn forest, leaves falling gently around her, golden diffused morning light, cinematic color grade, shallow depth of field"*

Not every prompt needs all six components — but including most of them consistently produces better results than vague, short descriptions.

---

## 1. Shot Types

Choose the right framing for the content:

| Shot | Best for |
|------|----------|
| Extreme close-up | Texture, detail, emotion in eyes/hands |
| Close-up | Facial expressions, small objects |
| Medium shot | People and action |
| Wide shot | Landscapes, establishing context |
| Aerial / drone | Scale, geography, epic establishing |
| Tracking / dolly | Following subjects, momentum |
| Static / locked-down | Atmosphere, stillness, contemplation |

---

## 2. Camera Movement Language

Use specific motion language — vague prompts produce static or drifting shots:

- `slow dolly forward / back`
- `gentle pan left / right`
- `subtle zoom in / out`
- `orbit around subject`
- `handheld slight camera shake` (naturalism, documentary feel)
- `crane rising slowly`
- `static, no camera movement` (when you explicitly want stillness)

---

## 3. Subject Description

Be concrete. Instead of "businesswoman," describe what the camera actually sees:

> *"woman in her early 30s, dark navy blazer, dark hair in a loose bun, serious expression, carrying a leather briefcase"*

For consistency across multiple clips, keep the exact same subject description in every prompt — only change the shot type and action.

---

## 4. Action & Motion

If you don't describe motion, the video may look static. Always include what's moving:

- Subject actions: *walking, turning her head, pouring coffee, typing slowly*
- Environmental motion: *leaves falling, rain streaking the window, smoke curling upward*
- Combined: *she looks up from her desk as snow begins to fall outside the window*

---

## 5. Environment

Ground the scene with specific place details:

- `cobblestone alley in a rainy European city`
- `brutalist concrete office interior, late evening`
- `dense pine forest, mist hanging low between trees`
- `rooftop terrace overlooking a neon-lit city at night`

---

## 6. Lighting

Lighting is one of the highest-leverage elements in the prompt. Be specific:

| Type | Description |
|------|-------------|
| Golden hour sunlight | Warm, low-angle, long shadows |
| Soft diffused cloud light | Flattering, neutral, even |
| Blue twilight tones | Cool, cinematic, moody |
| Hard chiaroscuro | Dramatic shadows, noir feel |
| Neon reflections | Urban night, colourful ambient |
| Natural window light | Interior realism, soft directional |
| Studio softbox | Clean, controlled, professional |

You can also specify color temperature directly: `color temperature: warm` or `color temperature: cool/blue`.

---

## 7. Visual Style & Mood

Add one or two style modifiers to lock in the aesthetic:

**Film references:**
- `35mm film grain, Kodak palette`
- `anamorphic lens flares`
- `shallow depth of field, bokeh background`

**Mood/atmosphere:**
- `moody`, `ethereal`, `gritty`, `cinematic`, `documentary`, `dreamlike`, `clean and minimal`

**Era/aesthetic:**
- `1970s muted tones`, `noir black-and-white`, `contemporary clean`, `vintage 8mm`

---

## Platform Formatting

Match the prompt to where the content will live:

| Platform | Format to add |
|----------|--------------|
| TikTok / Reels | `vertical format, 9:16`, favor close-ups, `dynamic energy` |
| YouTube | Keep default 16:9, add `cinematic widescreen` |
| Instagram | `1:1 square format`, center compositions |

---

## Multi-Clip Consistency

When generating a sequence of clips that need to feel like the same shoot:

1. Keep **identical subject descriptions** across all prompts
2. Keep **consistent lighting character** (same source, same temperature)
3. Keep **unified visual style** modifiers
4. Only vary **shot type** and **specific action**

This is the most reliable way to achieve visual coherence without a ControlNet-style reference.

---

## Common Problems & Fixes

| Problem | Solution |
|---------|----------|
| Video looks static | Add specific motion: dolly, pan, or subject action |
| Lighting looks flat | Include directional light source and temperature |
| Subject looks inconsistent across clips | Use identical, detailed subject description in all prompts |
| Output quality feels low | Use the full six-part formula, not a one-liner |
| Multiple subjects causing confusion | Simplify to one primary subject per clip |

---

## Credit Efficiency Tips

- **Narrow close-ups** cost the same as complex wide shots but are easier for the model to generate consistently
- **Reuse winning elements** — once you find lighting and style that works, copy those phrases across all prompts
- **Iterate on Seedance 1.5 first**, then finalize on Seedance 2.0 for quality
- **4–5 second clips** often outperform stretched longer ones — generate multiple short clips rather than one long one

---

## Model Selection

| Model | Best for |
|-------|----------|
| **Seedance 2.0** | Cinematic quality, complex scenes, hero shots |
| **Seedance 1.5** | Fast iteration, exploring concepts cheaply |
| Kling 3.0 | Character motion and performance |
| Veo 3.1 | Detailed environmental scenes |

---

## How to Help the User

When a user asks for a Seedance prompt (or help improving one), do this:

1. **Understand the scene** — ask what they're making if it's unclear (subject, mood, setting, purpose)
2. **Apply the formula** — build the prompt using the six components
3. **Add motion** — make sure there's always movement somewhere
4. **Tune for platform** — add format guidance if they mention where it'll be used
5. **Offer variations** — give 2–3 prompt options with different shot types or moods
6. **If improving an existing prompt** — identify what's missing (usually: motion, lighting specificity, or subject detail) and explain why you changed it

Keep prompts to **1–3 sentences**. Detailed but not overwhelming.
