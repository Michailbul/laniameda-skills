#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "google-genai>=1.0.0",
#     "pillow>=10.0.0",
# ]
# ///
"""
Color Grade Transfer via Nano Banana 2 (Gemini 2.0 Flash Image)

Transfers the color grade and tonal treatment from a reference image onto a source image,
preserving composition, pose, focus, and camera perspective.

Usage:
    uv run color_grade_transfer.py \
        --source path/to/source.jpg \
        --reference path/to/reference.jpg \
        --filename output.png \
        [--resolution 1K|2K|4K] \
        [--api-key KEY]
"""

import argparse
import os
import sys
from pathlib import Path


TRANSFER_PROMPT = (
    "Transfer the exact color correction and tonal treatment from Image 2 onto Image 1. "
    "Preserve the frame composition completely: framing, focus, and lighting direction must remain unchanged. "
    "Do not alter the subject's pose, depth of field, or camera perspective."
)


def get_api_key(provided_key: str | None) -> str | None:
    if provided_key:
        return provided_key
    return os.environ.get("GEMINI_API_KEY")


def main():
    parser = argparse.ArgumentParser(
        description="Transfer color grade from a reference image onto a source image using Nano Banana 2"
    )
    parser.add_argument("--source", "-s", required=True, help="Source image path (Image 1 — your photo)")
    parser.add_argument("--reference", "-r", required=True, help="Reference image path (Image 2 — color grade donor)")
    parser.add_argument("--filename", "-f", required=True, help="Output filename (e.g., graded-portrait.png)")
    parser.add_argument("--resolution", choices=["1K", "2K", "4K"], default="2K",
                        help="Output resolution: 1K, 2K (default), or 4K")
    parser.add_argument("--api-key", "-k", help="Gemini API key (overrides GEMINI_API_KEY env var)")
    parser.add_argument("--extra-prompt", help="Optional: append extra instructions to the base prompt")

    args = parser.parse_args()

    api_key = get_api_key(args.api_key)
    if not api_key:
        print("Error: No API key provided.", file=sys.stderr)
        print("  Set GEMINI_API_KEY env var or pass --api-key", file=sys.stderr)
        sys.exit(1)

    from google import genai
    from google.genai import types
    from PIL import Image as PILImage

    client = genai.Client(api_key=api_key)
    output_path = Path(args.filename)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Load both images
    try:
        source_img = PILImage.open(args.source)
        print(f"Source loaded:    {args.source} ({source_img.width}x{source_img.height})")
    except Exception as e:
        print(f"Error loading source image: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        reference_img = PILImage.open(args.reference)
        print(f"Reference loaded: {args.reference} ({reference_img.width}x{reference_img.height})")
    except Exception as e:
        print(f"Error loading reference image: {e}", file=sys.stderr)
        sys.exit(1)

    # Build prompt
    prompt = TRANSFER_PROMPT
    if args.extra_prompt:
        prompt = f"{prompt} {args.extra_prompt}"

    # Contents: [source (Image 1), reference (Image 2), prompt]
    # Model sees them in order — prompt references Image 1 and Image 2 accordingly
    contents = [
        "Image 1:",
        source_img,
        "Image 2:",
        reference_img,
        prompt,
    ]

    print(f"\nRunning color grade transfer at {args.resolution}...")
    print(f"Prompt: {prompt}\n")

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-preview-image-generation",
            contents=contents,
            config=types.GenerateContentConfig(
                response_modalities=["TEXT", "IMAGE"],
                image_config=types.ImageConfig(image_size=args.resolution)
            )
        )

        image_saved = False
        for part in response.parts:
            if part.text:
                print(f"Model: {part.text}")
            elif part.inline_data:
                from io import BytesIO
                import base64

                image_data = part.inline_data.data
                if isinstance(image_data, str):
                    image_data = base64.b64decode(image_data)

                image = PILImage.open(BytesIO(image_data))

                if image.mode == "RGBA":
                    rgb = PILImage.new("RGB", image.size, (255, 255, 255))
                    rgb.paste(image, mask=image.split()[3])
                    rgb.save(str(output_path), "PNG")
                else:
                    image.convert("RGB").save(str(output_path), "PNG")

                image_saved = True

        if image_saved:
            print(f"\n✓ Saved: {output_path.resolve()}")
        else:
            print("Error: No image in response.", file=sys.stderr)
            sys.exit(1)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
