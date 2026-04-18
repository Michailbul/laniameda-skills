# 3D Template + Brand Texture Swap

**Use when:** you have a generic 3D product render (e.g. from Freepik, Envato, or self-generated) and want to apply a specific brand's packaging, texture, or logo. Fast way to produce product-forward ads without a real product photo shoot.

**Inputs required:**
- Video 1: generic 3D template (unbranded package, bottle, box, etc.)
- Image 1: brand texture / packaging design / label art
- Optional image 2: hero product composite (if you've already generated one via Nano Banana Pro)

---

## Template

```
Multi-input video generation, Seedance V2.

SOURCE TEMPLATE: Use video 1 as the motion, camera, and lighting reference.
Preserve all motion exactly — rotation speed, camera movement, product position,
any background animation. Do not alter the timing or framing.

TEXTURE SWAP: Apply the branding from image 1 onto the product in video 1.
Preserve the 3D geometry of the product exactly — do not change shape, size,
or proportions. Only the surface texture, colors, logo, and label design
change to match image 1.

Specifically:
- Main label / wrap: matches image 1 exactly
- Logo placement: matches image 1 positioning and size
- Color palette: matches image 1 — primary, secondary, and accent colors
- Typography on product: matches image 1 — preserve font, weight, and layout
- Material finish: [GLOSSY / MATTE / METALLIC / SOFT-TOUCH] — match image 1 if shown

BACKGROUND: Preserve the background from video 1 exactly — do not regenerate
or alter. If background is a studio color, keep the exact color. If background
is a scene, preserve all elements.

LIGHTING: Match video 1 exactly — same direction, intensity, color temperature.
Reflections on the product should match the lighting from video 1 as if the
branded product were actually in that lighting.

CONSISTENCY: Product geometry identical to video 1 throughout. Branding from
image 1 remains consistent through all rotations and camera moves — text stays
legible, logo does not morph, colors stay true.

DURATION: Match video 1 exactly.
```

---

## Swap points per brand

- Image 1 (brand texture/label)
- Material finish (glossy / matte / metallic / soft-touch)
- Optional: background color if brand requires it

Keep constant:
- Source template video
- Camera, motion, lighting reference

---

## When this beats a photoshoot

- Evergreen ads that need quick brand swaps
- Multi-SKU testing (same product shape, different flavors/variants)
- Pre-launch mockups before packaging is physically produced
- A/B testing label designs before committing to print
- Localized packaging variants (different text per market, same shape)

---

## When NOT to use this

- First impression of a product to press or investors → use real photography
- Texture needs to show physical material quality (fabric, leather, wood grain) — 3D renders still struggle with these
- Product has complex transparent or refractive elements (glass bottles with liquid, crystalline textures) — real photos + Nano Banana Pro compositing works better

---

## Failure watchouts

- **Logo distortion** — brand logo warps during rotation. Fix: use a higher-res image 1 with the logo isolated, add `"logo from image 1 remains sharp and undistorted through all rotations"`.
- **Color shift** — brand color temperature changes. Fix: add `"exact color values from image 1 preserved — do not shift hue, saturation, or lightness"`.
- **Geometry morph** — product shape changes to match image 1's implied shape. Fix: add `"product geometry is the shape from video 1, not image 1 — only surface texture changes"`.
- **Label text re-rendered with wrong characters** — common failure mode. Fix: increase image 1 resolution, add `"preserve exact text characters from image 1, do not regenerate or misread letters"`.

---

## Finding templates

Sirio's mention — Freepik has 3D product templates (bottles, boxes, tubes, tubs, pouches). Also:
- Envato Elements
- Motion Array
- Storyblocks
- Self-generate via Nano Banana Pro (prompt a generic unbranded product, then extend to video via Seedance V2)

Build a library of 10-20 template shapes you reuse across brands. Each template = one source video + one catalog entry with what brand types fit it.

---

## Variation axes

**Brand A/B:** same template video, same motion, swap image 1 for different brands. Fastest multi-client production.

**Flavor/variant A/B:** same brand, different SKUs — swap image 1 for each variant of the same product line.

**Shape A/B:** same branding, different template (tube vs bottle vs jar) — see which packaging shape converts for the same product.

---

## Example — Sirio's package template demo

Setup:
- Video 1: generic 3D package rotation (unbranded, evergreen template)
- Image 1: branded package design (yellow background, specific logo + text)
- Target: replace the package in the template with the branded version

Result:
- Logo applied correctly, stayed consistent through rotation
- Yellow background from brand image preserved
- 3D geometry from template preserved
- Motion and camera unchanged from source

Why it worked: multi-input preserved the expensive part (3D animation) and only swapped the surface layer. Production cost: one prompt, ~60 seconds of generation.
