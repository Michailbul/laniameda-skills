# Output Template

Use this exact structure when handing the extraction to another agent.

```md
# Reference Extraction

## Source Reference
- Original reference URL: <url or "No original reference URL provided">
- Reference type: <repo | component | code block | screenshot | live URL>
- Artifact scope: <landing page | section | component | layout | interaction pattern>
- Evidence level: <source-backed | mixed | inferred>

## What This Reference Is
<1 short paragraph describing the artifact and why it matters>

## Design Language
- <precise design language terms>
- <precise design language terms>
- <precise design language terms>

## On-Screen Elements
- <hero / nav / cards / overlays / forms / etc.>
- <how each element behaves visually>

## Behavior And Motion
- <scrolling pattern>
- <loading behavior>
- <hover and pointer response>
- <reveal choreography>
- <mobile or touch behavior>

## Frontend Logic
- <state model>
- <event listeners>
- <measurement or scroll math>
- <hooks or utilities>
- <layering strategy>

## Complex Patterns To Teach With Code
### <pattern name>
Why it matters:
<short explanation>

Source snippet:
```tsx
<short snippet>
```

Explanation:
<how it works and what must be preserved>

## Recreation Instructions For Another Agent
- <what to preserve>
- <what to rebuild first>
- <what not to simplify away>

## Prompt Template
```text
<prompt that another agent can use>
```

## Things Not To Lose
- <non-negotiable design trait>
- <non-negotiable interaction trait>
- <non-negotiable implementation trait>
```

## Rule For Image-Only References

If the user only provides an image, keep the same structure but explicitly label:

- visible facts
- inferred behaviors
- unknown implementation details

Do not present inferred implementation as certain.
