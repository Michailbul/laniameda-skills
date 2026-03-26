# Extraction Standards — AI Creatorship Content

What to pull and how. Apply to any source: tweet, thread, video, article, PDF.

---

## Prompts

| What to capture | What to skip |
|----------------|-------------|
| Full prompt text — verbatim, every word | Paraphrased or summarized versions |
| Model name it was used with | "works in AI image tools" |
| Parameters, aspect ratios, style keywords | Parameter mentions without values |
| Negative prompt (if given) | Generic style descriptions |
| [BLANK] template structure (keep intact) | "just describe what you want" |

**Format:**
```
Model: [Midjourney v6 / FLUX / Nano Banana Pro / Kling v2.5 / etc.]
Prompt: [exact text verbatim]
Parameters: [--ar 16:9 --stylize 750 / cfg: 7 / etc.]
Negative: [if present]
Notes: [what the result looked like, any specific conditions]
```

---

## Workflows

Capture:
- Numbered step-by-step processes
- "If you want [effect] → use [tool] + [setting]" mappings
- Tool chains: what feeds into what
- Exact settings, values, slider positions
- Platform-specific nuances ("in Kling, X causes Y")

Skip:
- "and then you refine it" vagueness
- Steps without tools named

---

## Tools & Models

| What to capture | What to skip |
|----------------|-------------|
| Exact tool/model name | "an AI tool" |
| Version number if mentioned | Outdated versions (flag as deprecated) |
| Specific capability or use case | "can do many things" |
| Pricing tier or limitation noted | "it's expensive" |
| Comparison advantage over alternatives | "better than X" without specifics |

---

## Techniques

Capture named techniques specifically:
- ComfyUI node setups: which nodes, what connections, workflow logic
- ControlNet: which model, conditioning type, weight
- Inpainting / outpainting: which tool, mask approach, prompt strategy
- Motion control (video): camera movement language, speed descriptors
- Style transfer: source → target approach
- LoRA: trigger word, strength, training context

Always tag the model the technique applies to. A technique that works in FLUX may not work in Midjourney.

---

## Negative Findings

Equally valuable as positive findings. Capture:
- "X doesn't work in [model]"
- "Y produces worse results than Z"
- "Avoid [technique] because [reason]"
- Hyped approaches that underperform in practice

These often prevent wasted time and are worth encoding into skills as explicit warnings.

---

## Quality Gate

Before saving anything, ask: **can Michael copy-paste this and use it immediately?**

| Content | Save it? |
|---------|---------|
| Exact prompt with model tag | ✅ Yes |
| "Describe your scene in detail" | ❌ No |
| Step-by-step workflow with tool names | ✅ Yes |
| "Iterate until it looks right" | ❌ No |
| "[Model] handles X better than Y because Z" | ✅ Yes |
| "AI is changing creativity" | ❌ No |
| Named technique with settings | ✅ Yes |
| "Use good lighting" | ❌ No |

If a post is 90% hype and 10% specific — save the 10%, skip the rest. Don't pad output with noise.
