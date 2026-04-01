---
name: desi-webdesign-practicies-extraction
description: Extract reusable web-design practices, interaction patterns, layout grammar, motion systems, and implementation techniques from a reference repo, component, code block, screenshot, or live URL. Use when Codex needs to study an existing design or frontend implementation and teach another agent how to recreate the same component, landing page, layout, or behavior in a different project, especially when complex patterns should be explained with source-backed code snippets rather than natural-language summary alone.
---

# Desi Webdesign Practicies Extraction

## Overview

Use this skill to turn a reference into a reusable reconstruction brief for another agent.

The input may be:

- a repo
- a component
- a code block
- a screenshot
- a live URL

The output is not a vague style description. It is a structured extraction of:

- what the design is doing visually
- how the screen is composed
- how motion and interaction behave
- which frontend mechanisms create those behaviors
- which exact source snippets should be carried forward when the logic is too complex to summarize loosely

## Non-Negotiable Rule

Always store the original reference URL when one exists.

- If the user provides a live URL, store it verbatim.
- If the user provides a repo or component and a corresponding source URL is discoverable, store it.
- If no URL exists, record `No original reference URL provided`.

Put this near the top of the output under `Source Reference`.

## Workflow

1. Identify the input type.
2. Capture source metadata.
3. Extract visible design language.
4. Extract behavior and motion patterns.
5. Extract frontend implementation patterns.
6. Decide which mechanisms require code-backed teaching.
7. Produce a reconstruction brief for another agent.

## 1. Identify The Input Type

Choose the extraction mode based on the strongest artifact available:

- Repo or full codebase: prioritize real implementation patterns and file-backed evidence.
- Component or code block: prioritize local logic, state, event handling, CSS structure, and rendering strategy.
- Screenshot or reference image: prioritize visual grammar and interaction hypotheses, but clearly mark inferred behaviors.
- Live URL: inspect rendered behavior first, then inspect code if available.

Prefer source-backed evidence over inference whenever code is available.

## 2. Capture Source Metadata

Start every extraction with:

- `Source Reference:` original URL or `No original reference URL provided`
- `Reference Type:` repo, component, code block, screenshot, live URL
- `Artifact Scope:` full landing page, section, component, layout, interaction pattern
- `Evidence Level:` source-backed, mixed, or inferred

When code is provided, also record:

- framework and stack
- key files
- component names
- relevant hooks or utilities

## 3. Extract Visible Design Language

Describe the page in precise screen-language terms, not generic adjectives.

Extract:

- atmosphere and vibe
- layout model
- layering system
- typography system
- surface treatment
- spacing rhythm
- color ownership
- information density
- asymmetry vs symmetry

Use concrete phrasing such as:

- full-screen horizontal chapter layout
- fixed atmospheric background
- glass instrumentation
- editorial typography over generative motion
- asymmetric list rhythm
- bottom-weighted hero composition

## 4. Extract Behavior And Motion

Explain what the user experiences:

- scrolling pattern
- navigation behavior
- section changes
- hover response
- cursor behavior
- reveal choreography
- loading sequence
- mobile gesture mapping

Focus on actual motion grammar:

- opacity plus translation
- stagger timing
- directional entry
- parallax or fixed layers
- scroll remapping
- pointer-follow physics

Avoid fuzzy phrases like "smooth animations" without saying what actually moves, when, and why.

## 5. Extract Frontend Implementation Patterns

For code-backed references, identify the mechanics that produce the design:

- state model
- refs
- event listeners
- scroll math
- gesture thresholds
- layout containers
- z-index and fixed-position strategy
- CSS variables and theme tokens
- reveal hooks
- animation loops
- pointer interpolation
- responsive layout branching

When useful, explain the relationship between structure and effect:

- fixed background plus moving content track
- hidden native cursor plus custom rendered cursor
- `IntersectionObserver` plus transition classes for reveal-on-enter
- pointer offset math plus `translate3d` for magnetic buttons

## 6. Use Code-Backed Teaching For Complex Patterns

Do not rely on natural-language summary alone when the behavior depends on implementation detail.

Include short source-backed snippets when the pattern involves:

- custom scroll remapping
- section index math
- shader or canvas readiness gating
- animation loops
- custom cursor interpolation
- magnetic button math
- gesture handling
- custom hooks
- stateful motion coordination
- layout calculations

For each snippet:

- keep it short and focused
- include file path or source location when available
- explain what the snippet is doing in plain language
- explain why the mechanism matters for recreating the effect

## 7. Mark Evidence Correctly

When the reference is image-only:

- separate what is visible from what is inferred
- label interaction and logic guesses as inferred
- avoid pretending you know the exact implementation

When the reference includes code:

- ground behavioral claims in the source
- cite files
- carry forward implementation patterns rather than only describing the result

## Output Contract

Produce the extraction in this order:

1. `Source Reference`
2. `What This Reference Is`
3. `Design Language`
4. `On-Screen Elements`
5. `Behavior And Motion`
6. `Frontend Logic`
7. `Complex Patterns To Teach With Code`
8. `Recreation Instructions For Another Agent`
9. `Prompt Template`
10. `Things Not To Lose`

## References

Read [references/extraction-checklist.md](references/extraction-checklist.md) for the concrete extraction checklist.

Read [references/output-template.md](references/output-template.md) for the exact shape of the reconstruction brief.
