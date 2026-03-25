# Carousel Brief Template

Use this template when spawning Codex for carousel generation.
Fill every field from the user's request before sending.

---

```
Create a 7-slide LinkedIn carousel using the carousel-designer skill.

## Brief
Topic: {{TOPIC}}
Angle/hook: {{HOOK — the one contrarian or surprising take}}
Target audience: {{WHO IS THIS FOR}}
Tone: {{brutalist-tech | warm-professional | bold-statement}}

## Key points (one per content slide, slides 2–6)
1. {{POINT_1 — include any real stat or number if available}}
2. {{POINT_2}}
3. {{POINT_3}}
4. {{POINT_4}}
5. {{POINT_5}}

## CTA
Keyword: {{COMMENT_KEYWORD e.g. "THROUGHPUT", "SYSTEM", "FRAMEWORK"}}
What they get: {{what you'll send them}}

## Output
Save to: {{PROJECT_PATH e.g. ~/work/carousels/YYYY-MM-DD-topic/}}
When done print: RENDER_COMPLETE
```

---

## Notes on filling the brief
- **Angle/hook**: This is slide 1's headline energy. Should be a tension or inversion. 
  Bad: "AI tools are useful"  
  Good: "The bottleneck isn't prompts. It's throughput."
- **Key points**: Each one should be self-contained and worth a full slide. If a point needs 2 sentences to explain, it IS 2 slides.
- **Real numbers**: If the user provided stats, include them verbatim. Codex should not invent numbers.
- **CTA keyword**: Short (1–2 words), all caps, easy to type in a comment.
