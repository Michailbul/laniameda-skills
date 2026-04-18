# Emotion → Muscle Movement Library

**The rule:** Seedance V2 (and every vision model) fails when you write "sad" or "happy." It has no idea which of the thousand ways to be sad you meant. Describe the muscles. The model renders what you describe.

**Source:** Sirio Berati, Enhancor AI founder, from Seedance V2 walkthrough 2026-04-17.

---

## Translation Table

| Don't write | Write instead |
|---|---|
| "She is happy" | "Corners of the mouth lift into a closed-lip smile, eyes crinkle slightly at the outer edges, chin tilts up half an inch." |
| "She is surprised" | "Eyebrows lift, eyes widen for half a second, mouth opens a beat before she speaks." |
| "She is sad" | "Eyebrows draw together and down at the inner corners, lower lip comes up slightly, gaze drops to the mid-distance." |
| "She is excited" | "Eyes widen, cheeks lift, small exhale through an open mouth, slight forward lean toward camera." |
| "She is confused" | "One eyebrow lifts half a beat before the other, head tilts right by 10 degrees, corner of the mouth pulls sideways." |
| "She is skeptical" | "Chin lowers slightly, one eyebrow rises, lips press together into a thin neutral line, eyes narrow just at the outer corners." |
| "She is impressed" | "Eyebrows lift, mouth opens into a soft 'oh' shape, head nods once slowly, shoulders rise a quarter inch." |
| "She is enjoying it" | "Eyes close briefly, a small satisfied exhale through the nose, corners of the mouth turn up with the lips still closed." |
| "She is confident" | "Chin level, shoulders relaxed and open, steady eye contact with camera, slight half-smile on one side of the mouth." |
| "She is thoughtful" | "Gaze drifts up and to the left, lips press together loosely, one hand touches the jaw or chin lightly." |
| "She is laughing" | "Head tips back half an inch, shoulders lift with a single breath, mouth opens wide with teeth visible, eyes nearly close." |
| "She is disappointed" | "Shoulders drop a quarter inch, a slow exhale, corners of the mouth pull down and back, eyes lower to the product." |

---

## Emotional Transitions

UGC authenticity lives in *transitions*. A single held expression reads as AI. A shift from one expression to another reads as human.

**Always describe the transition, not the endpoint.** Format:

```
[Starting expression] → [transition beat] → [ending expression]
```

Worked examples:

- **Skeptical → pleasantly surprised** (taste test):
  "She starts with lips pressed together and one eyebrow slightly raised. As the first sip hits, her eyebrows lift, eyes widen for half a beat, and the corners of her mouth pull up into a small closed-lip smile."

- **Neutral → delighted** (unboxing):
  "Her face holds a soft neutral expression as she lifts the lid. Her eyes widen the instant she sees the contents, her mouth opens into a small 'oh,' and a real smile spreads a beat later with her cheeks lifting."

- **Excited → genuine** (product hold):
  "She starts with a wide rehearsed smile that softens within the first second as her eyes settle on the camera. The smile drops to a relaxed half-smile, her gaze steadies, and her shoulders release a quarter inch."

---

## Micro-Gestures That Sell Authenticity

Add at least one per clip. These are the tells that separate AI from human.

- Blink mid-sentence, not between sentences
- Brief glance down or sideways before answering
- Hair touch or tuck behind ear
- Quick lip-press or lip-wet before speaking
- Hand enters frame to adjust hair, collar, glasses
- Small shoulder shift or weight redistribution
- Half-laugh or soundless exhale between phrases
- Eyes tracking something moving in the scene (Sirio's bear demo)
- Hand gesture that doesn't perfectly match the rhythm of speech
- A beat of silence where the mouth is closed but the eyes are alive

---

## Breathing + Pacing Cues

Real people breathe. AI people don't.

- "Takes a short breath before saying..."
- "Pauses for half a beat, then..."
- "Exhales softly as she finishes the sentence."
- "Mid-sentence pause, continues..."
- "Closes mouth between sentences."

Put these in the prompt alongside the dialogue:

```
She takes a short breath, then says "Okay so I just tried this...",
pauses for half a beat as she looks at the bottle, then continues "...huh, that's actually nice."
```

---

## What Breaks

- **Rehearsed-smile syndrome** — avoid. Always soften the opening expression within 1 second.
- **Over-animation** — too many micro-gestures in a 5-second clip reads as AI trying too hard. Pick 2.
- **Mismatched emotion + dialogue** — if the script is casual, don't write cinematic muscle choreography. Match the register.
- **Emotion labels smuggled in via adjectives** — "her genuinely happy smile" defeats the whole rule. Describe the smile.

---

_Build your own additions below when you discover new emotion-to-muscle mappings in production. Cite the model and use case._
