---
name: design-poster-prompts
description: >
  Write graphic design poster prompts in 9 proven style families: ASCII glitch art,
  Asian chic graphic, classic advertising, whimsical moody, visual kei, scrapbook collage,
  Y2K collage, dreamcore, and Y2K glossy chrome. Use whenever the user wants a designed
  poster, typographic art print, collage graphic, or asks for one of these aesthetics by
  name. Built for ChatGPT Image 2.0 / GPT-Image-2 (Higgsfield); the formula transfers to
  Nano Banana Pro and other design-literate image models.
metadata:
  laniameda:
    departments: ['Operations', 'Marketing']
    purposes: ['Prompting', 'Design']
    tags: ['poster', 'graphic-design', 'gpt-image-2', 'higgsfield', 'typography', 'collage', 'y2k', 'ascii', 'prompting']
    status: active
    depends_on: []
    replaces: []
  clawdbot:
    emoji: 🖼️
---

# Design Poster Prompts

## Role

You are writing a brief for a design-literate image model. Every prompt describes a finished poster the way an art director would spec it: one hero subject, a disciplined palette, a typography layer with real placement, and micro-copy in quotes. The model executes layout — your job is to leave it zero ambiguity about what sits where.

Reference results: all 25 source posters live in laniameda.gallery under tags `design` + `poster`. Full source prompts: `references/prompt-library.md`.

## The formula

Every prompt in the library follows the same skeleton, in this order:

```
[STYLE FAMILY] poster,
[HERO SUBJECT + rendering technique],
[background / support layer],
[texture overlay + named color palette].
[HEADLINE: type style + weight + placement],
[MICRO-COPY: captions, badges, fine print — sample text in quotes],
[layout descriptor + format].
```

Rules that make it work:

1. **Open with the style declaration.** `ASCII glitch art poster,` / `Visual kei style poster,` — the first phrase sets the whole rendering mode. Never bury it.
2. **One hero subject, and say how it's rendered.** Not "a deer" but "a deer head silhouette built entirely from dense monospace ASCII text and code fragments". The rendering technique is the style.
3. **Name the palette, cap it at 2–3 colors.** "deep royal blue and bright yellow linework on vibrant magenta-pink" beats any adjective. Every strong result in the pack has a named, limited palette.
4. **Declare a physical texture.** Halftone grain, fine woven canvas, film grain, vintage newsprint, torn paper. This is what separates "designed poster" from "AI render".
5. **Sentence break before typography.** The period between scene and type layer matters — it tells the model these are separate layers.
6. **Type gets style + placement, always.** "Large bold serif headline stacked and overlapping slightly at the top", "cursive script word stacked vertically along the right edge". Placement words the pack uses: lower left, top corners, along the left edge, arcing above, curving diagonally, filling the upper right.
7. **Micro-copy in quotes.** Small labels sell the design: `"○ Warsaw, 2019"`, `"Developed in the dark, remembered in color"`. Quoted strings render as actual legible text; unquoted "some caption text" renders as gibberish. Give 2–4 small text elements per poster.
8. **Fill negative space with scatter.** Tick marks, data points, firework icons, star stickers, badges — every family has its own scatter vocabulary.
9. **Close with format.** "clean editorial poster layout, vertical format" or equivalent.
10. **Variations = one variable swap.** To make a series, lock the composition and swap only the palette (library indexes 22/23: sunset-orange chrome → violet-magenta chrome, everything else identical).

## The 9 style families

Signature ingredients per family — combine with the formula above. Full worked prompts in `references/prompt-library.md`.

**ASCII glitch art** — subject built from monospace characters and code fragments; blue/indigo/black, white-on-black, or glowing white overlaid on a sepia photograph; edges fade into scattered character noise; thin italic data-point captions with `○` bullets.

**Asian chic graphic** — one bold animal (koi, dragon, crane) in duotone or woodblock-print linework; checkerboard, wave-pattern, or solid saturated background; East Asian characters stacked vertically or filling a corner; circular emblem badges; hard 2-color clashes (indigo/off-white, royal blue/yellow on magenta).

**Classic advertising** — single product hero on a solid cream or deep-color background; dramatic side lighting; oversized cursive script word arcing over the product; small oval badge; faint vertical ingredient-list fine print; vintage print feel.

**Whimsical moody** — atmospheric storybook scene (crown on a pedestal, submerged library, lighthouse at dusk); high contrast with one undertone (faint blue, emerald, warm cream on dark green); grain or canvas texture across the whole image; elegant serif + cursive headline mix.

**Visual kei** — androgynous figures in baroque decay: melting candle wax, torn lace, cracked mirrors, frozen greenhouses; chiaroscuro or B&W with newsprint texture; heavy film grain; elegant cursive script text.

**Scrapbook collage** — a photo base (beach, 2000s suburban snapshot) or bold solid background, then layered ephemera: washi tape, paper clips, torn notebook pages, postmark stamps, film-strip borders, cut-out word tiles spelling a sentence, confetti stickers. Maximalist variant: solid red background, unrelated cutouts (vinyl label, mesh bag of oranges, chrome sphere, cat photo).

**Y2K collage** — grainy B&W street photo or bright blue-sky snapshot base; halftone-dot silhouette portrait or oversized cutout illustration; bubble-graffiti logo with drop shadow; floating cartoon stickers, retro video-player window overlay; handwritten lyric fragments.

**Dreamcore** — oversaturated hyper-green landscape under deep blue sky; details deliberately wrong: paths that split and never arrive, identical cottages at mismatched proportions, shadows pointing the wrong way. The unease is the style — always include at least two "wrong" details.

**Y2K glossy chrome** — chrome ribbon or liquid-metal bubble 3D typography as the hero; chromatic-aberration edges in a named accent color; solid gradient background; sparkle lens flares at letter tips; editorial fashion figure in a glossy metallic outfit; glass-shard or crack textures.

## Workflow

1. Ask which family (or pick from the user's description — "make it feel like a zine" → Y2K collage).
2. Draft using the formula skeleton. Pull the family's worked examples from `references/prompt-library.md` as the pattern.
3. Write real micro-copy for the user's subject — never leave placeholder text unquoted.
4. For a series: lock composition, swap one variable per variant.
5. Generate on Higgsfield ChatGPT Image 2.0 (GPT-Image-2). Vertical format unless asked otherwise.
6. Save keepers to laniameda.gallery via `laniameda-gallery-ingest` with tags `design` + `poster` + the family tag.

## Gallery references

The 25 source posters are queryable via `laniameda-gallery-query`:
- tag filter: `design` + `poster`, plus family tags `ascii-glitch`, `asian-chic`, `classic-advertising`, `whimsical-moody`, `visual-kei`, `scrapbook-collage`, `y2k-collage`, `dreamcore`, `y2k-chrome`
- ingest keys: `design:notion-design-prompt-pack:00:v1` … `:24:v1`
