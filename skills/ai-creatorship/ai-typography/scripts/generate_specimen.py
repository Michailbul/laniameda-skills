#!/usr/bin/env python3
"""
Generate font specimen PNG for AI typography reference injection.
Downloads font from Google Fonts and renders a clean specimen image.
Used as --input-image reference in Nano Banana Pro for font consistency.

Usage:
  python3 generate_specimen.py --font "Manrope" --weight "SemiBold" --output specimens/manrope-semibold.png
  python3 generate_specimen.py --all  # Generate all 10 presets
"""

import argparse
import os
import sys
import urllib.request
import re
from pathlib import Path

# Try PIL, fallback instructions if missing
try:
    from PIL import Image, ImageDraw, ImageFont
    import io
except ImportError:
    print("ERROR: Pillow required. Run: pip install Pillow")
    sys.exit(1)


FONT_PRESETS = [
    {"font": "Manrope",        "weight": "600",   "slug": "manrope-semibold",      "css_weight": "600"},
    {"font": "Fraunces",       "weight": "400",   "slug": "fraunces-regular",      "css_weight": "400"},
    {"font": "Syne",           "weight": "800",   "slug": "syne-extrabold",        "css_weight": "800"},
    {"font": "Inter",          "weight": "600",   "slug": "inter-semibold",        "css_weight": "600"},
    {"font": "Albert Sans",    "weight": "600",   "slug": "albert-sans-semibold",  "css_weight": "600"},
    {"font": "Merriweather",   "weight": "700",   "slug": "merriweather-bold",     "css_weight": "700"},
    {"font": "Tenor Sans",     "weight": "400",   "slug": "tenor-sans-regular",    "css_weight": "400"},
    {"font": "Space Grotesk",  "weight": "700",   "slug": "space-grotesk-bold",    "css_weight": "700"},
    {"font": "Google Sans",    "weight": "700",   "slug": "google-sans-bold",      "css_weight": "700"},
    {"font": "IBM Plex Sans",  "weight": "600",   "slug": "ibm-plex-sans-semibold","css_weight": "600"},
]

SPECIMEN_TEXT = [
    "Aa Bb Cc Dd Ee Ff",
    "Gg Hh Ii Jj Kk Ll",
    "Mm Nn Oo Pp Qq Rr",
    "Ss Tt Uu Vv Ww Xx Yy Zz",
    "0 1 2 3 4 5 6 7 8 9",
    "The quick brown fox",
    "jumps over the lazy dog",
]


def download_google_font(font_name: str, weight: str) -> bytes | None:
    """Download font TTF from Google Fonts API."""
    font_encoded = font_name.replace(" ", "+")
    # Try Google Fonts CSS2 API to get font URL
    url = f"https://fonts.googleapis.com/css2?family={font_encoded}:wght@{weight}&display=swap"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            css = resp.read().decode("utf-8")
        
        # Extract font URL from CSS
        urls = re.findall(r'url\((https://fonts\.gstatic\.com/[^)]+\.ttf)\)', css)
        if not urls:
            # Try woff2
            urls = re.findall(r'url\((https://fonts\.gstatic\.com/[^)]+)\)', css)
        
        if not urls:
            print(f"  WARNING: Could not find font URL in CSS for {font_name}")
            return None
        
        font_url = urls[0]
        print(f"  Downloading: {font_url}")
        
        req2 = urllib.request.Request(font_url, headers=headers)
        with urllib.request.urlopen(req2, timeout=15) as resp:
            return resp.read()
            
    except Exception as e:
        print(f"  WARNING: Failed to download {font_name}: {e}")
        return None


def generate_specimen(font_name: str, weight: str, output_path: str) -> bool:
    """Generate a font specimen PNG."""
    
    print(f"Generating specimen: {font_name} {weight} → {output_path}")
    
    # Image settings
    width, height = 1200, 800
    bg_color = (15, 15, 15)       # Dark background
    text_color = (240, 240, 240)  # Near-white text
    accent_color = (180, 180, 180) # Gray for labels
    
    img = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Try to download and use the actual font
    font_data = download_google_font(font_name, weight)
    
    display_font = None
    body_font = None
    label_font = None
    
    if font_data:
        try:
            font_io = io.BytesIO(font_data)
            display_font = ImageFont.truetype(font_io, size=72)
            font_io.seek(0)
            body_font = ImageFont.truetype(font_io, size=36)
            font_io.seek(0)
            label_font = ImageFont.truetype(font_io, size=22)
        except Exception as e:
            print(f"  WARNING: Could not load font data: {e}. Using default.")
    
    if not display_font:
        # Fallback to default font
        display_font = ImageFont.load_default()
        body_font = display_font
        label_font = display_font
    
    # Header label
    draw.text((60, 40), f"{font_name.upper()}  ·  WEIGHT {weight}", 
              font=label_font, fill=accent_color)
    
    # Divider
    draw.line([(60, 90), (width - 60, 90)], fill=(60, 60, 60), width=1)
    
    # Large display sample
    draw.text((60, 110), font_name, font=display_font, fill=text_color)
    
    # Second divider
    draw.line([(60, 210), (width - 60, 210)], fill=(60, 60, 60), width=1)
    
    # Specimen text lines
    y = 230
    for line in SPECIMEN_TEXT:
        draw.text((60, y), line, font=body_font, fill=text_color)
        y += 70
    
    # Footer metadata
    draw.line([(60, height - 80), (width - 60, height - 80)], fill=(60, 60, 60), width=1)
    meta = f"Font specimen for AI reference injection  ·  laniameda.gallery  ·  Nano Banana Pro compatible"
    draw.text((60, height - 55), meta, font=label_font, fill=accent_color)
    
    # Save
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    img.save(output_path, "PNG", optimize=True)
    print(f"  ✅ Saved: {output_path} ({os.path.getsize(output_path) // 1024}KB)")
    return True


def main():
    parser = argparse.ArgumentParser(description="Generate font specimens for AI typography reference")
    parser.add_argument("--font", help="Font name (e.g. 'Manrope')")
    parser.add_argument("--weight", help="CSS weight (e.g. '600')")
    parser.add_argument("--output", help="Output PNG path")
    parser.add_argument("--all", action="store_true", help="Generate all 10 presets")
    parser.add_argument("--specimens-dir", default=str(Path(__file__).parent.parent / "specimens"),
                        help="Directory for specimens when using --all")
    
    args = parser.parse_args()
    
    if args.all:
        print(f"Generating all {len(FONT_PRESETS)} font specimens → {args.specimens_dir}\n")
        success = 0
        for preset in FONT_PRESETS:
            out = os.path.join(args.specimens_dir, f"{preset['slug']}.png")
            if generate_specimen(preset["font"], preset["css_weight"], out):
                success += 1
            print()
        print(f"\n✅ Done: {success}/{len(FONT_PRESETS)} specimens generated")
        
    elif args.font and args.weight and args.output:
        generate_specimen(args.font, args.weight, args.output)
        
    else:
        print("Usage:")
        print("  python3 generate_specimen.py --font 'Space Grotesk' --weight '700' --output specimens/space-grotesk-bold.png")
        print("  python3 generate_specimen.py --all")
        sys.exit(1)


if __name__ == "__main__":
    main()
