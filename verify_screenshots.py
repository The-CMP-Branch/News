#!/usr/bin/env python3
"""Verify screenshots show no overlap or horizontal overflow."""

from PIL import Image
import os

def analyze_screenshot(path, width):
    """Analyze a screenshot for issues."""
    print(f"\n{'='*60}")
    print(f"Analyzing {width}px screenshot...")
    print(f"{'='*60}")
    
    img = Image.open(path)
    print(f"Image size: {img.size[0]}x{img.size[1]}")
    
    if img.size[0] != width:
        print(f"⚠️  WARNING: Expected width {width}px but got {img.size[0]}px")
    else:
        print(f"✓ Width matches expected {width}px")
    
    # Get pixel data
    pixels = img.load()
    
    # Check header area (first ~150 pixels) for white background
    header_white_count = 0
    header_cream_count = 0
    header_total = 0
    
    for y in range(min(150, img.size[1])):
        for x in range(img.size[0]):
            r, g, b = pixels[x, y][:3]
            header_total += 1
            
            # Check if pixel is white (header background)
            if r > 250 and g > 250 and b > 250:
                header_white_count += 1
            # Check if pixel is cream (old background)
            elif 240 < r < 250 and 235 < g < 245 and 220 < b < 230:
                header_cream_count += 1
    
    white_pct = (header_white_count / header_total) * 100
    cream_pct = (header_cream_count / header_total) * 100
    
    print(f"Header background: {white_pct:.1f}% white, {cream_pct:.1f}% cream")
    
    if white_pct > 30:
        print("✓ Header appears to have white background")
    else:
        print("⚠️  Header may not have white background")
    
    # Check for green border at bottom of header (around y=100-110)
    green_border_found = False
    for y in range(80, 120):
        for x in range(0, min(200, img.size[0])):
            r, g, b = pixels[x, y][:3]
            # Check for Acorn green (#00A651)
            if r < 20 and 150 < g < 180 and 70 < b < 100:
                green_border_found = True
                print(f"✓ Green border found at y={y}")
                break
        if green_border_found:
            break
    
    if not green_border_found:
        print("⚠️  Green border not clearly visible")
    
    return True

if __name__ == '__main__':
    widths = [1280, 768, 390, 320]
    
    print("Screenshot Verification")
    print("="*60)
    
    all_good = True
    for width in widths:
        path = f'/agent/repos/News/screenshots/header-{width}px.png'
        if os.path.exists(path):
            analyze_screenshot(path, width)
        else:
            print(f"⚠️  Screenshot not found: {path}")
            all_good = False
    
    print("\n" + "="*60)
    if all_good:
        print("✓ All screenshots captured and analyzed")
    else:
        print("⚠️  Some issues found")
    print("="*60)
