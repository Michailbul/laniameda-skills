# Localization Playbook

**The bet:** Most DTC brands don't localize creative because it's too expensive to reshoot per market. That's the arbitrage. Take one ad that's working in English → ship 10 language variants overnight → capture traffic the brand was already paying for but not converting.

---

## When Localization Wins

- Brand has paid traffic from multiple countries but conversion only works in one language
- Product has no regulatory/compliance translation blockers
- The hook in the original ad is translatable (some idioms don't carry — skip these)
- Creator persona is market-neutral OR you're willing to swap persona per market

## When It Doesn't

- Brand has strict legal review per market (pharma, finance, supplements) — translation delay kills the ROI
- Original ad leans on cultural references — not translatable without rewriting
- Market-specific creators are non-negotiable for the brand

---

## Language Tier Map (Start Here)

Prioritize by market size × ease of translation. Start with 3-5 languages, not 20.

**Tier 1 — highest ROI per translation:**
- Spanish (neutral Latam or Castilian — pick one based on target market)
- Portuguese (Brazilian)
- German
- French (Parisian)
- Italian

**Tier 2 — high value, more translation nuance:**
- Japanese
- Korean
- Mandarin (simplified, mainland)
- Arabic (MSA for pan-Arab, or dialect if single market)

**Tier 3 — worth it for the right brand:**
- Dutch
- Polish
- Turkish
- Indonesian
- Hindi (with English code-switch — common in urban India ads)

---

## The Workflow

### 1. Pick the source ad

Use only ads that are already converting in their original language. Don't localize duds.

### 2. Lock the persona

Two strategies:

**Strategy A — Single global persona:** one AI creator, all languages. Simpler production. Less authentic per market. Good for brands with a "global" feel.

**Strategy B — Persona per market:** each language gets a demographic match. More authentic. More production overhead (more personas to maintain).

Default: Strategy A for tier 1 markets, Strategy B for tier 2-3.

### 3. Translate the script

Use Claude Opus 4.6 with this exact instruction:

```
Translate this UGC ad line to [TARGET_LANGUAGE].

Rules:
- Match syllable count within ±20% of original
- Keep conversational register — this is a casual spoken ad
- Use fillers natural in [TARGET_LANGUAGE] (don't carry over English fillers)
- Preserve the hook structure — if the original opens with surprise,
  the translation opens with a surprise-equivalent in [TARGET_LANGUAGE]
- Do not translate brand names, product names, or proper nouns
- Return only the translation, no commentary

Original: [paste original dialogue]
```

Always get a native speaker to review tier 1 languages before shipping. LLM translations are ~90% there — the last 10% is where authenticity lives.

### 4. Build the prompt using `prompt-templates/translation.md`

Source video carries the motion. New persona image + translated dialogue are the only swap axes.

### 5. Generate and QA

Generate all language variants. Run through quality gates (see SKILL.md). Native-speaker review for tier 1.

### 6. Deploy and measure

Ship to the same ad platforms as the original. Measure CVR per language variant vs. the original English ad.

---

## Common Translation Traps

**Literal translation of idioms.**
- English: "This is a total game-changer."
- Literal Spanish: "Esto es un cambio total del juego." (Bad — nobody says this.)
- Localized Spanish: "Esto cambia todo." (Right.)

**Register mismatch.**
- English casual UGC: "Okay so I just tried this..."
- Over-formal Japanese: 「先ほどこちらを試してみたのですが…」(too formal — sounds like a business report)
- Right casual Japanese: 「これ試してみたんだけど…」

**Syllable drift breaking lip sync.**
- English: "Not bad." (2 syllables, ~1s)
- Bad French: "Ce n'est pas mal du tout." (7 syllables — mouth runs out of time)
- Good French: "Pas mal." (2 syllables — matches)

**Filler word mistakes.**
- English: "uh", "like", "you know"
- German: "äh", "halt", "ne?"
- Don't leave English fillers in a German script.

---

## Market-Specific Notes

**Spanish (Latam vs Castilian):**
Pick one. Castilian uses "vosotros" and lisped "c" — Latam uses "ustedes" and hard "c". Mixing them feels wrong to natives.

**Portuguese (Brazilian vs European):**
Brazilian is much bigger market. Cadence is slower, vowels are more open. European Portuguese is faster and clipped — sounds different to the ear, not just different accent.

**Arabic (MSA vs dialect):**
MSA (Modern Standard) works pan-Arab but sounds formal. Dialects (Egyptian, Levantine, Gulf) feel authentic per market but don't carry across.

**Japanese:**
Register matters more than in most languages. Default to casual informal (です・ます form feels salesy in a UGC ad — too polite for a friend recommending something).

**Chinese (Mainland vs Taiwan):**
Simplified vs Traditional characters. Mandarin pronunciation differs. Don't use a Taiwanese persona for mainland ads or vice versa.

---

## Economic Model

Rough math for why this works:

**Traditional localization:** Reshoot per market.
- 1 ad × 5 markets = 5 shoots × $5-15k = $25-75k
- 2-4 week timeline per market
- Creative consistency suffers (different creators, different shoots)

**Seedance V2 localization:** One source, N language variants.
- 1 persona + 1 source ad + 5 translations + 5 Seedance generations
- ~$50-200 in generation cost + 1 day of production
- Creative consistency preserved (same motion, same framing, same energy)

Savings: ~99%. Time-to-market: ~95% faster.

The question isn't "should we localize" — it's "how many markets do we run by Friday?"

---

## Attribution / Measurement

Tag each variant with language code in filename and meta:
- `v1-en-reaction` (control)
- `v2-es-la-reaction` (Spanish Latam)
- `v3-pt-br-reaction` (Portuguese Brazilian)
- `v4-de-reaction` (German)
- etc.

Run as separate ad sets in the ad platform to isolate CVR per language.

Benchmark: expect 2-4× CVR lift on localized vs. default English in non-English markets. If you see less than 1.5× lift, the translation probably needs a native-speaker pass.
