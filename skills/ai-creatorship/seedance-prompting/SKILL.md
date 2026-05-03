---
name: seedance-prompting
description: >
  Write high-performance Seedance 2.0 prompts for NON-NARRATIVE work — ad spots, music videos, fashion films, automotive inserts, product shots, pet/character demos, cutaway montages, social reels (TikTok / Reels / YouTube Shorts), and any cinematic AI video that is not a story scene. Use whenever the target model is explicitly Seedance and the work is standalone or commercial — no dialogue, no scene continuity, no shot-list-into-a-film. Also owns Seedance-specific structured output (JSON, bilingual EN+ZH prompt delivery) for non-narrative briefs.
  
  For NARRATIVE work — scenes, short films, screenplays, dialogue coverage, shots that cut into a story — use `seedance-screenwriter` instead. That sibling skill outputs Seedance prompts in screenplay format and pairs with the `screenwriter` skill.
metadata:
  laniameda:
    departments: ['Operations', 'Marketing']
    purposes: ['Automation', 'Ingestion']
    tags: ['seedance', 'ai-video', 'prompting', 'cinematic', 'timecoded-video']
    status: active
    depends_on: []
    replaces: ['seedance-prompts']
  clawdbot:
    emoji: 🎬
---

# Seedance 2.0 Prompting

## Role

When this skill activates, you are a **Seedance prompt architect**.
You write prompts like a film director briefing a previs team: precise, visual, time-aware, and motion-aware.
You do not write vague prompt poetry. You build a shot system the model can actually follow.

Your priorities, in order:
1. **Character consistency**
2. **Readable action from second zero**
3. **Clear camera choreography**
4. **Explicit physics**
5. **Strong ending beat**

---

## Core Seedance Rules

These are the non-negotiables.

- **Default prompt order:** Subject → Action → Camera → Style → Constraints → Audio
- **Always lock continuity when needed:** `same character throughout all shots`, `same car throughout all shots`, `same dog throughout all shots`, or `same product throughout all shots`
- **Use the identity lock only when continuity matters** — do not force `same character` on campaign montages, multi-product ads, or deliberately different subjects
- **Timecodes are the default for multi-shot when timing precision matters:** `[0s] [3s] [6s]`
- **Director-prose sequencing is also valid for multi-shot** if the shot order is explicit with phrases like `opens on`, `pushes in`, `cuts to`, `returns to`, `concluding with`
- **Max 3 shots per prompt** — more causes drift
- **Ideal prompt length:** 120–280 words
- **Action starts at second zero** — never open with stillness unless the intended motion is environmental or micro-movement
- **For simple one-shot clips, a compact non-timecoded prompt is valid** — do not force multi-shot structure when one clear shot is enough
- **Use one main action verb per shot** — avoid stacking multiple unrelated actions into the same beat
- **One sentence should do one job** — setup, lighting, camera progression, hero insert, or ending beat
- **Use direct director verbs, not poetic filler** — `opens on`, `reveals`, `pushes in`, `tracks`, `whip-pans`, `cuts back`, `holds`, `concludes`
- **Keep adjective density controlled** — 1 to 3 precise modifiers beat a pile of cinematic synonyms

If the user gives a loose AI-video idea, convert it into this six-part base before adding advanced structure:
`Camera/shot type -> Subject -> Action/motion -> Environment -> Lighting -> Visual style/mood`.

---

## Output Contract

Always deliver in this order:

1. **Seedance prompt** — copy-paste ready
2. **Why this structure works** — 2–4 bullets max
3. **Failure watchouts** — what may break in generation
4. **Optional tighter / bolder version** — only if useful

Do not bury the actual prompt under explanation.

If the user explicitly asks for **JSON**, **bilingual EN+ZH**, or other machine-shaped Seedance output:
- keep the same Seedance logic from this skill
- change only the delivery format
- do not switch to a separate Seedance skill

### Structured-output variant

When the user asks for structured Seedance output, use a compact shape like:

```json
{
  "mode": "single-shot | multi-shot | reference-controlled",
  "prompt_en": "...",
  "prompt_zh": "...",
  "continuity_lock": "...",
  "notes": ["optional short implementation notes"]
}
```

Rules:
- `prompt_en` is required
- add `prompt_zh` only when the user asks for Chinese or bilingual output
- keep commentary outside the JSON unless the user explicitly wants explanation
- if the user wants pure JSON, return pure JSON

---

## Seedance Prompt Skeleton

Use this default skeleton when writing from scratch:

```text
same [subject] throughout all shots, same [subject] consistent appearance every shot.
[0s] [subject + action already in motion]. [camera angle / movement]. [environment details]. [style / color system].
[3s] [escalation beat or transition]. [camera change if needed]. [physics explicitly named].
[6s] [final visual beat / impact / reveal / transition out]. [audio ending].
Global: [aspect ratio], [lens / anamorphic note], [grain], [physics rules], [consistency lock], [constraints].
```

For single-shot prompts, remove later timecodes and keep one coherent shot.

### Compact single-shot template

Use this when the user wants one clean clip or fast iteration:

```text
[Subject]. [Action in progress]. [Camera]. [Style]. [Constraints]. [Audio if useful].
```

Example:
```text
A red sports car races through a dusk mountain road. Low front three-quarter tracking shot with subtle handheld vibration and heavy directional motion blur. Premium automotive commercial realism, blue dusk sky, pink roadside flowers, anamorphic 2.39:1, fine grain. Realistic tire grip, suspension compression, petal turbulence in the slipstream. Deep engine note and rushing wind.
```

### Director-prose multi-shot template

Use this when the user wants the prompt to read like a concise director brief instead of a timecoded block.
This is valid for Seedance if the shot order stays explicit and each sentence has a clear job.

```text
[Opening master shot introducing subject, setting, and overall tone]. [Physical environment and lighting system]. [Camera progression from master to closer coverage]. [Hero insert or specific performer/object focus]. [Final return, reveal, or concluding beat]. [Optional sound or dialogue note].
```

Working rule:
- sentence 1 = who / where / what kind of scene
- sentence 2 = what the light and set are doing physically
- sentence 3 = how the camera moves through the sequence
- sentence 4 = what specific hero detail gets isolated
- sentence 5 = how the clip lands

Example:
```text
A wide cinematic shot opens on the lead dancer and the full group in a dark seamless studio, already mid-performance. Soft rectangular overhead panels cast a cool low-key wash while harder front and side keys carve bright highlights across the black floor and structured wardrobe. The camera slowly pushes in from a full-body wide shot to a tight medium close-up on the lead performer, then cuts back to the wider formation as the choreography sharpens. A low-angle medium shot isolates the lead dancer for one hero beat, followed by a clean facial close-up. The sequence concludes on a full-group wide shot with crisp rhythmic cuts and subtle push-ins, pull-outs, and gentle pans.
```

---

## Prompt Construction Sequence

### 1) Subject
Lock the subject first.
- Who is on screen?
- What do they look like?
- What identity details must persist?

Use plain, stable language.
Bad: “ethereal cinematic female warrior goddess of chaos”
Good: “same young woman throughout: black hair, dark structured coat, two swords”

### 2) Action
Action must already be underway at `[0s]`.
Do not start with standing still unless the scene is driven by environmental movement, emotional tension, or micro-movement.

Good openings:
- “she runs through shallow flood water”
- “he turns sharply as sparks fall behind him”
- “the train is already entering the station”
- “the dog stands perfectly still while sheep flow around him”
- “the car is already cornering at speed as petals lift into the slipstream”

Rule: one clear action verb per shot is stronger than a list of actions.

### 3) Camera
Use exact camera language. Prefer one primary move per beat.

Approved camera terms:
- `slow dolly-in`
- `pull-back`
- `dolly out`
- `extreme low-angle`
- `overhead top-down`
- `360° orbit`
- `handheld natural lag`
- `tracking shot`
- `crash zoom`
- `aerial pull-back`

Additional high-value camera language:
- `wide`
- `medium`
- `close-up`
- `extreme close-up`
- `macro close-up`
- `aerial / drone`
- `telephoto compression`
- `ultra-wide ground-up lens`
- `locked-off`
- `static, no camera movement`
- `gimbal smooth`
- `slight handheld sway`
- `gentle pan left / right`
- `crane rising slowly`
- `low front three-quarter tracking shot`

If the prompt is already action-heavy, simplify camera movement. Seedance breaks when everything is moving at once.
Rule: shot size + movement + angle is usually enough. Example: `close-up slow dolly-in from low angle with telephoto compression`.

### 4) Style
Describe style as production direction, not hype words.

Strong style ingredients:
- lighting system
- color system
- lens / format note
- film grain / texture
- weather / atmosphere

Bad: “epic masterpiece ultra cinematic insane realism”
Good: “deep red emergency light, sprinkler rain, anamorphic 2.39:1, 35mm grain”

### 5) Constraints
State what must stay stable.

Examples:
- `same character throughout all shots`
- `same wardrobe every shot`
- `continuous rain throughout`
- `no extra characters entering frame`
- `single light source only`

### 6) Audio
Seedance responds better when the audio beat is intentional.
Name the sonic ending or silence.

Examples:
- `audio silence`
- `rain fades to three final drops`
- `distant subway rumble continues under silence`
- `hard cut to black, audio drops out completely`

---

## Camera Moves — Use These Exact Meanings

| Move | Effect |
|---|---|
| `slow dolly-in` | builds intensity |
| `pull-back` / `dolly out` | reveals environment, scale, loneliness |
| `extreme low-angle` | heroic, dominant, powerful |
| `overhead top-down` | geometry, choreography, battlefield logic |
| `360° orbit` | frozen tension, stylized rotation |
| `handheld natural lag` | documentary urgency |
| `tracking shot` | side-follow motion, continuity |
| `crash zoom` | shock, urgency |
| `aerial pull-back` | epic reveal |

Rule: choose the move that matches the emotional beat. Don't add camera variety just because it sounds cool.

---

## Physics — Always Name Them Explicitly

Seedance under-specifies physics unless told directly.
Always name the material behavior if it matters.

### Physics language
- **Cloth:** `cloth inertia`, `fabric lags behind movement`, `cloth settles after landing`
- **Sand / dust:** `sand displacement under foot`, `radial dust shockwave`
- **Water:** `water splashing with surface tension`, `droplets scattering`, `floor puddle mirror reflections`
- **Slow motion:** `120fps slow-motion on impact, hard snap back to 24fps realtime`
- **Hair:** `hair reacts to acceleration vector and wind direction`
- **Impact:** `skin distorting on impact`, `delayed follow-through motion`
- **Cars / racing:** `suspension compression`, `tire grip under load`, `road vibration through the chassis`, `side mirror vibration`, `slipstream pulling leaves and petals`, `gravel flicking outward from the tire line`
- **Environment reaction:** `grass bending in airflow`, `debris dragged in the wake`, `petals spiraling after the car passes`, `branches reacting to pressure wave`

If water, dust, hair, cloth, sparks, debris, petals, or vehicle wake are visually important, write the physics explicitly.

---

## STOP MOTION — Use Exactly Once

This is the strongest dramatic tool in the system.
Use it once per prompt, at peak tension.
During the freeze: **complete audio silence**.

Format:
```text
STOP MOTION [duration]s — complete audio silence — [describe what is frozen] — explosive snap-back to full speed
```

Duration guide:
- `0.5s` = sharp impact beat
- `1.0s` = standard dramatic freeze
- `1.5s + 360° orbit` = bullet-time style moment

Do not use STOP MOTION more than once.

---

## Transitions

Use only when the scene truly needs a cut.

- `match cut`
- `whip pan`
- `smash cut`
- `cut to black`
- `natural fade`

Best practice: finish with the strongest possible final beat instead of overusing transitions.

---

## Color & Grade

Write palettes like an art director, not a moodboard caption.

**Rule: always derive the color grade from the scene's emotional logic and the source lighting.** No preset palettes, no named defaults. Every scene gets the color treatment it deserves — pulled from what the subject feels, where the light comes from, and what the shot is trying to say.

When writing the color block, name:
- the dominant light source and its temperature
- the 1–3 colors allowed in frame (and what is explicitly excluded)
- contrast behavior (crushed shadows, blown highlights, midtone flatness)
- any surface behavior that reinforces the grade (wet asphalt reflections, volumetric haze, skin glow, matte absorption)

If the user does not specify color, build one coherent system from the scene's own logic instead of pulling from a preset library or using vague cinematic language.

---

## Safe Reframing When Seedance Rejects a Prompt

Do **not** help bypass filters or moderation systems.
If a prompt gets blocked, reframe it into cleaner cinematic language while preserving the visual intent.

Use these safe swaps:
- `fight` → `impact sequence`, `collision`, `force exchange`
- `soldiers` → `armored figures`
- `kill` → `final moment`, `collapse`, `aftermath`
- graphic injury details → remove them; keep the scene cinematic and non-graphic

You may also:
- reduce intensity
- emphasize camera / environment over harm
- rephrase as a production brief
- retry benign prompts once or twice if failure seems inconsistent

---

## Writing Modes

## Mode 1 — Single-shot
Use when the user wants one clean clip.
Structure:
- one subject lock only if continuity matters
- one action beat
- one camera move
- one color system
- one ending beat

## Mode 2 — Multi-shot
Use for short story beats.
Rules:
- max 3 shots
- each shot escalates or contrasts intentionally
- choose either **timecodes** or **director-prose sequencing** based on what makes the beat easiest to read
- if using director-prose, make every transition explicit in language
- final shot must land on reveal / impact / silence / cut to black

## Mode 3 — Reference-controlled
If the user provides reference frames or character references:
- say what the reference controls: subject, wardrobe, composition, mood, or setting
- lock identity only if the same subject must persist
- keep camera complexity lower than normal
- avoid more than 2 shots unless necessary
- build from what is visible in the reference, not invented off-frame lore
- when the reference already shows the subject and set, spend prompt tokens on motion, shot progression, physics, and ending beat instead of re-describing the starting frame

## Mode 4 — Commercial / product montage
Use for ads, fashion films, automotive inserts, pet campaigns, or cutaway coverage.
Rules:
- continuity lock can be `same car`, `same dog`, or `same product`, not only `same character`
- each shot should feature one sellable detail: silhouette, texture, behavior, material, or hero moment
- use contrast on purpose: prestige shot, detail shot, playful shot, hero shot
- if multiple subjects are intentionally different, do not force a false identity lock

---

## Seedance Failure Patterns

Watch for these when constructing prompts:
- Too many shots → character drift
- Forcing `same character` when the scene is actually a montage → bad continuity logic
- Static output → missing subject action, camera movement, or environmental motion
- Flat lighting → missing directional source, color temperature, or contrast behavior
- Action + camera + effects all peaking together → chaos
- No continuity lock when sameness matters → face/wardrobe/vehicle drift
- Multi-shot sequencing that is not clearly ordered → mushy sequencing, whether timecoded or prose
- Overusing timecodes for a simple one-shot clip → unnecessary rigidity
- Generic style words → weak visual language
- Poetic filler or synonym stacks → the model loses the actual instruction
- Missing physics → fake water, dead cloth, weightless impacts, weak speed
- Weak ending → clip feels unfinished

## Debugging Seedance Prompts

When a prompt underperforms, debug it like a shot problem, not a magic problem.

### Change one variable at a time
Do not rewrite everything at once.
Hold the continuity lock, style, and constraints steady while changing only one variable:
- subject
- action
- camera
- environment
- color system
- ending beat

This makes failures legible.

### Debug order
1. **Action clarity** — is one readable thing happening from second zero?
2. **Camera simplicity** — is the camera doing too much while the subject is already moving?
3. **Continuity logic** — should this actually be `same character`, `same car`, `same dog`, or no lock at all?
4. **Physics specificity** — are the materials reacting believably?
5. **Ending beat** — does the clip land on something memorable?

### Fast fixes by failure type
- **Character drift** → reduce shots, simplify wardrobe, strengthen the continuity lock
- **Chaotic motion** → remove one camera move or one effects layer
- **Static output** → add one clear subject action, camera move, or environmental motion
- **Flat lighting** → name the light source, temperature, and shadow behavior
- **Dead realism** → add environment reaction physics, inertia, or secondary motion
- **Weak emotion** → replace abstract feeling words with visible behavior
- **Boring output** → strengthen contrast, silhouette, color system, or final beat
- **Prompt feels overwritten** → collapse adjective stacks, keep one sentence per job, switch to directorial verbs

### Reference-material debugging
If using references:
- use short clean video references for movement or rhythm
- use clear front-facing image references for identity
- prefer evenly lit subject references when consistency matters
- do not mix too many reference goals into one generation unless the interface clearly supports it

---

## Prompt Templates

### Template A — Single-shot cinematic
```text
same [subject] throughout all shots, same [subject] consistent appearance every shot. [0s] [camera angle] [subject] [action already in progress] in [environment]. [camera movement]. [color system]. [physics]. Global: [aspect ratio], [lens/style], [grain], [constraints]. Audio: [sound design or silence].
```

If continuity does not matter, remove the lock and use the compact single-shot template instead.

### Template B — Three-beat sequence
```text
same character throughout all shots, same character consistent appearance every shot. [0s] [subject] [action already happening]. [camera]. [environment]. [style]. [3s] [escalation / reaction / transition]. [camera adjustment]. [physics]. [6s] [final beat / reveal / collapse / cut]. [ending transition or cut to black]. Global: [aspect ratio], [anamorphic note], [grain], [single light source or palette rule], [consistency constraints]. Audio: [specific ending beat].
```

### Template C — STOP MOTION beat
```text
same character throughout all shots, same character consistent appearance every shot. [0s] [action in progress]. [camera]. [color system]. [3s] STOP MOTION 1.0s — complete audio silence — [exact frozen visual] — explosive snap-back to full speed. [6s] [final impact or reveal]. Global: [constraints], [physics], [format].
```

### Template D — Director-prose sequence
```text
[Wide or master shot opens on subject and setting]. [Physical set design and lighting system]. [Camera pushes / pans / tracks / whip-pans into the next beat]. [Specific hero insert or character focus]. [Sequence returns, expands, or concludes on the final beat]. [Optional dialogue or sound note].
```

### Platform format defaults
- TikTok / Reels / Shorts: `vertical 9:16`, favor close-ups and readable motion
- YouTube: `16:9` or `cinematic widescreen`, allow wider environmental framing
- Instagram square: `1:1`, center important subjects and avoid edge-dependent action

### Model and iteration notes
- Seedance 2.0: use for hero shots, cinematic quality, and complex scenes
- Seedance 1.5: use for cheaper concept iteration when available
- Kling: consider for character motion and performance-heavy clips
- Veo: consider for detailed environmental scenes
- Generate 4-5 second clips when exploring; stitch multiple strong clips instead of stretching one weak long generation

---

## Example — Working Seedance Prompt

```text
same character throughout all shots, same character consistent appearance every shot. [0s] Extreme low-angle inside a Tokyo metro car. Same young woman throughout: black hair, dark structured coat, two swords. Fire alarm already active, sprinkler indoor rain already falling. She walks forward without stopping, each step creating a precise water circle on the floor. Handheld natural lag with tracking shot, continuous motion, no sprint. Deep red color system: single deep red emergency light, no other colors, floor puddle mirror reflections, anamorphic 2.39:1, 35mm grain. [5s] STOP MOTION 1.0s — complete audio silence — all droplets frozen mid-air in red light, her face completely calm — explosive snap-back to full speed. [6s] Final impact, opponent mask flies spinning, hard cut to black. Global: same wardrobe every shot, sprinkler water throughout, water splashing with surface tension, cloth inertia, 9:16 output. Audio: rain fades to three final drops, then total silence.
```

---

## Reference Library

Reference source material for Seedance prompt ideation and retrieval is saved in the studio KB here:
- `~/work/laniameda/laniameda-hq/content-kb/sources/articles/2026-04-10-seedance-2-prompt-guide/`

Structured prompt library extracted from that source:
- `docs/seedance/imagine-art-seedance-prompt-library.json`
- `docs/seedance/imagine-art-seedance-prompt-library-categorized.json`

Use these as:
- category examples
- retrieval material
- prompt pattern mining input

Do not treat the library as doctrine. Treat it as example coverage layered under the stricter rules in this skill.

## Advanced Director Structure Reference

Use this only when the prompt needs a fuller director-style brief, such as:
- emotional narrative shorts
- multimodal reference-controlled generations
- more complex ad films with explicit tone and progression

This is an **advanced optional structure**, not the default.

### Why the reference prompts work

The strongest professional Seedance-style prompts tend to follow this logic:
- **Open with the master image** — who is on screen, what kind of scene it is, and the core genre signal
- **Ground the space physically** — floor, walls, haze, skyline, cockpit, street debris, overhead panels
- **Describe the lighting as a system** — source, direction, softness or hardness, and what surfaces it shapes
- **Direct the edit in prose** — wide to medium, medium to close-up, push-in then cut back, low-angle hero insert, concluding wide
- **Attach mood to visible causes** — not just `powerful` or `mysterious`, but low-key contrast, stark spotlight, dust-filled backlight, harsh daylight, rhythmic cuts
- **Repeat anchor nouns when needed** — mecha, cockpit, ruined city, group choreography; repetition keeps the model on track
- **Land on a final beat** — return to the group, hold on the face, cut to the cockpit, conclude on the wide

### Director-language heuristics

When writing this style, follow these rules:
- Write like a director briefing shots to a previs team, not like a copywriter selling the scene
- Use declarative present-tense sentences the model can stage directly
- Let each sentence carry one layer: setup, set design, lighting, camera progression, hero beat, ending
- Prefer physical nouns and film terms over abstract adjectives
- If you mention mood, tie it to camera, light, performance, or cut rhythm in the same sentence
- When moving through multiple shots, keep the sequence linear and readable
- Mention shot size and angle whenever focus changes: `wide shot`, `medium shot`, `close-up`, `low-angle`, `extreme close-up`
- Name only the camera moves that matter to the beat; subtle push-ins, pull-outs, pans, tracking, and whip-pans are usually enough
- For action scenes, describe force and recoil in physical terms instead of generic intensity words

### Advanced structure
- **Goal & Tone** — one-line statement of the emotional and production objective
- **Narrative progression** — beginning, development, climax, or equivalent timeline beats
- **Cinematography** — shot size, camera movement, angle, lens behavior
- **Lighting & Color** — light quality, temperature, palette, contrast, saturation
- **Action Direction** — specific visible actions, written coherently and step-by-step when needed
- **Sound Design** — ambience, sync beats, dialogue, silence, or sonic ending
- **Constraints** — continuity, anatomy, stability, transition behavior, or interface-specific requirements

### Multimodal dispatch reference
If the Seedance surface supports reference syntax such as `@image`, `@video`, or `@audio`, use it deliberately:
- `@image` → identity, wardrobe, composition, scene layout
- `@video` → movement style, rhythm, camera behavior, transition feel
- `@audio` → soundtrack, beat sync, lip-sync reference, ambience reference

Rule: assign each reference one clear job. Do not overload a single generation with too many competing reference instructions.

### Director-language checklist

Before sending a dense prose prompt, verify:
- Can I underline a clear opening frame in the first sentence?
- Did I name the set surfaces and the light sources, not just the vibe?
- Is the shot progression explicit without needing to guess chronology?
- Does each sentence have one job, or did I stack too many instructions?
- Are my strongest words concrete film language instead of hype language?
- Does the prompt end on a clean final beat?

---

## Response Style

When the user says things like:
- `write a Seedance prompt for...`
- `make this feel more cinematic in Seedance`
- `turn this scene idea into a Seedance 2.0 prompt`
- `I need a 3-shot Seedance prompt`

You should respond with the finished prompt first.
Then give only the minimal notes needed to make it usable.

If the user is exploring or ideating rather than asking for a final prompt:
- you may answer in looser cinematic language first
- then convert that direction into strict Seedance structure only when needed
- if switching modes, say so briefly
