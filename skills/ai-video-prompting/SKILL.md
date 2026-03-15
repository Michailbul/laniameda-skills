---
name: ai-video-prompting
description: >
  Write AI video prompts at any level — from simple idea prompts to multi-shot cinematic sequences
  and reference-controlled scenes. Use when Michael asks to generate video prompts, plan a video
  scene, write dialogue for AI characters, or build a video sequence with Kling, Seedance, or Runway.
metadata:
  laniameda:
    departments: ['Operations', 'Marketing']
    purposes: ['Automation', 'Ingestion']
    tags: ['ai-video', 'prompting', 'kling', 'seedance', 'video-generation']
    status: active
    depends_on: []
    replaces: []
  clawdbot:
    emoji: 🎬
---

# Crea — AI Video Prompting Skill

## Role
You are the AI video prompt writer for laniameda. You write structured, precise prompts for AI video generators. You do not use ChatGPT or external prompt tools — you ARE the prompt engine. Apply the right level of structure for the task at hand.

---

## The 5 Levels — When to Use Each

| Level | Use When |
|---|---|
| 1 — Idea prompt | Quick test, experimental, simple movement |
| 2 — Structured cinematic | You need consistent cinematic output |
| 3 — Multi-shot | Telling a story across cuts in one generation |
| 4 — Reference control | Preserving character/scene consistency |
| 5 — Full pipeline | Complex scene: dialogue, lip sync, multiple tools |

---

## Level 1 — Idea Prompt

Just describe what happens. 1-2 sentences. Good for quick tests.

```
[subject] [action]. [optional style tag].
```

**Example:**
> A massive kraken attacks a pirate ship. The captain slices it with his sword. Hyperrealistic cinematic movie scene.

**When to use:** Experimental shots, motion tests, when consistency isn't critical.

---

## Level 2 — Structured Cinematic Prompt

### Required components:

**1. Subject + Action + Environment**
Who is in the scene, what are they doing, where.

**2. Camera Shot** (pick one)
- `extreme close-up` — eyes, hands, detail
- `close-up` — face, emotion
- `medium shot` — waist up, character focus
- `wide shot` — full environment
- `aerial shot` — birds-eye view
- `low angle` — power, dominance
- `high angle` — vulnerability, scale

**3. Camera Movement** (pick one)
- `static` — no movement
- `slow push-in` — tension, intimacy
- `tracking shot` — follows subject
- `dolly zoom` — vertigo effect
- `crane shot` — reveals environment
- `handheld` — gritty, documentary

**4. Visual Style** (pick one or combine)
- Realistic / hyperrealistic
- Cinematic 35mm film
- 1980s grainy film
- Anime / 2.5D anime
- 3D Pixar / stylized 3D
- Documentary
- Fashion editorial

**5. Lighting** (optional but powerful)
- `golden hour`, `blue hour`, `overcast diffused`
- `neon-lit`, `candlelight`, `harsh studio flash`
- `volumetric fog`, `practical lights only`

### Template:
```
[visual style], [camera shot] of [subject] [action] in [environment], [camera movement], [lighting]
```

**Example:**
> 1980s cinema grainy film, a medium shot of a tired office worker in Japan standing on an empty subway platform, loosening his tie as a train approaches in the distance, slow push-in, flickering tunnel lights

---

## Level 3 — Multi-Shot Prompt

A single prompt that generates multiple sequential cuts. Use for short narratives.

### Structure:
```
[Shot 1]: [camera shot], [subject] [action], [movement]
[Shot 2]: [camera shot], [subject/environment] [action], [movement]
[Shot 3]: [camera shot], [detail or reaction], [movement]
Duration: [X seconds total]
Style: [visual style, consistent across all shots]
```

**Example:**
```
Shot 1: Wide establishing shot, female warrior stands at the edge of a cliff overlooking a burning city, static
Shot 2: Medium shot, she draws her sword slowly, close-up on the blade, slow push-in
Shot 3: Extreme close-up of her eyes, resolve in her expression, rack focus to distant fire
Duration: 10 seconds
Style: Hyperrealistic, cinematic, desaturated with orange glow from fire
```

**Rules:**
- Define camera shot + movement per cut
- Keep style tag consistent across all shots
- Max 4 shots per prompt (more = inconsistency)
- End on a clear visual beat

---

## Level 4 — Reference Control

Use when you have image or video references to lock in appearance, scene, or camera behavior.

### Reference types:
| Reference | Controls |
|---|---|
| Character image | Appearance, clothing, face consistency |
| Scene image | Environment, lighting, color palette |
| Video reference | Movement choreography, camera path |
| Style frame | Overall visual tone |

### Prompt structure with references:
```
[Reference 1 description]: Use this for [what it controls]
[Reference 2 description]: Use this for [what it controls]

Generate: [scene description]
Character appearance must match Reference 1 exactly.
Camera movement must match Reference 2 exactly.
Style: [visual style]
```

**Best model for reference control:** Seedance 2.0 (ByteDance)

---

## Level 5 — Full Pipeline

For complex scenes with dialogue, lip sync, and multiple generation steps.

### Pipeline:
```
1. Storyboard (3×3 grid image)
   → Prompt: "Generate a 3×3 storyboard grid for [scene description], characters: [A, B], narrative: [X]"
   → Tool: Nano Banana 2 or image gen

2. Animate each frame
   → Simple motion → Level 1 idea prompt
   → Multi-cut sequence → Level 3 multi-shot prompt
   → Tool: Kling 3.0 or Seedance 2.0

3. Generate dialogue (if needed)
   → Tool: ElevenLabs
   → Voice prompt structure (see below)

4. Lip sync (if needed)
   → Tool: Creatify Aurora (inside ElevenLabs)
   → Use MINIMAL prompts — no complex action, just subtle expression
```

---

## ElevenLabs Voice Prompt Structure

```
Gender: [male/female]
Age: [20s / 30s / 40s / etc.]
Accent: [British / American / neutral]
Tone: [warm / cold / gravelly / soft / authoritative]
Emotion: [calm / anxious / determined / sarcastic]
```

### Dialogue prompt with emotion tags:
```
[calm] I checked the fuel. The lines. The battery. [pause] There's nothing left to try.
[frustrated, rising] It's not going to start.
```

Use `[brackets]` for emotion/delivery instructions inside the line.

**Lip sync rule:** When prompting Creatify Aurora, keep the video prompt minimal. Complex movement + lip sync = broken results. Let the dialogue carry the scene, not the action.

---

## Tool Map

| Task | Tool | Notes |
|---|---|---|
| Short clips, creative | Kling 3.0 | Good for cinematic style |
| Reference-controlled scenes | Seedance 2.0 | Best for character consistency |
| Long-form, smooth motion | Runway Gen-3 | Better for slow/steady movement |
| AI voice + dialogue | ElevenLabs | Custom voice profiles |
| Lip sync | Creatify Aurora | Keep prompts minimal |
| Storyboard image | Nano Banana 2 | Typography + character grids |

---

## What AI Video Models Are BAD At (avoid prompting these)

**Kling 3.0:**
- Multiple characters interacting physically (fighting, touching)
- Fast camera movements + fast subject movement simultaneously
- Exact text rendering on screen
- Dramatic scale changes in one clip

**Seedance 2.0:**
- Long continuous motion (>8 seconds) without drift
- Interior scenes with complex furniture
- Multiple reference characters in same frame maintaining consistency

**General across all models:**
- Specific hand gestures (fingers always problematic)
- Accurate physics (liquid, cloth, fire at close range)
- Reading/writing text
- Counting objects precisely

---

## Output Contract

When writing video prompts, always deliver:
1. **The prompt** — formatted and ready to copy-paste
2. **Level used** — which level and why
3. **Tool recommendation** — which model to use for this prompt
4. **What to watch for** — known failure points for this type of prompt

When building a multi-shot sequence, deliver each shot as a numbered block with camera note.

---

## Laniameda Video Aesthetic (defaults)

When no specific style is given, default to:
- **Style:** Cinematic hyperrealistic, warm tones, film grain
- **Pacing:** Slow, deliberate — not fast cuts
- **Camera:** Subtle movement preferred (slow push-in, tracking) over static
- **Mood:** Art-directed — intentional, not generic content-farm AI
