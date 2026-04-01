# Picker Export Format

The picker HTML page generates a structured text summary when the user clicks "Export Picks". This format is designed to be parseable by the agent in the next phase.

## Format

```
=== [BRAND NAME] BRAND PICKS ===

## Base (locked)
[Color Name] [Hex] | [Color Name] [Hex] | ...

## Accent Colors I Like
- [Name] [Hex]
- [Name] [Hex]

## Font Pairings I Like
- [Headline Font Weight] + [Body Font Weight]
- [Headline Font Weight] + [Body Font Weight]

## Combo Cards I Like
- [Tag] [Background] bg + [Headline color] head / [Headline font]+[Body font]
- [Tag] [Background] bg + [Headline color] head / [Headline font]+[Body font]

## Gradients I Like
- [Color A] → [Color B]
- [Color A] → [Color B]

--- Paste this to Claude to proceed ---
```

## How to analyze

### Frequency counting
For each unique color, count how many times it appears across all combo card picks (as bg, headline, or accent). Rank by frequency:
- 3+ appearances → **Primary Accent**
- 1-2 appearances → **Supporting**
- 1 appearance, only as situational → **Situational**

### Pattern detection
- Which backgrounds were picked most? → These are the user's preferred dark/light surfaces
- Which headline colors repeat? → These are the go-to accent colors
- Which font pairings appear with which colors? → These become the cheatsheet recipes

### Cuts
Colors that appear 0 times across all picks get dropped entirely. Don't propose keeping them "just in case."

## Tags in combo cards

Combo cards may be tagged with their origin direction:
- `[B]` — from direction B
- `[C]` — from direction C
- No tag — hybrid or new combination

This helps trace which direction the user gravitates toward when multiple were proposed.
