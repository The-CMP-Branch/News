#!/usr/bin/env python3
"""Crop RISC OS News logos to remove excess white margins."""

from PIL import Image
import sys

def find_crop_bounds(img, padding=10):
    """Find the bounding box of non-white content with padding."""
    # Convert to RGB if necessary
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    pixels = img.load()
    width, height = img.size
    
    # Find bounds of non-white content (allowing for slight variations)
    min_x, min_y = width, height
    max_x, max_y = 0, 0
    
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Consider pixels that aren't pure white (with some tolerance)
            if not (r > 250 and g > 250 and b > 250):
                min_x = min(min_x, x)
                min_y = min(min_y, y)
                max_x = max(max_x, x)
                max_y = max(max_y, y)
    
    # Add padding
    min_x = max(0, min_x - padding)
    min_y = max(0, min_y - padding)
    max_x = min(width, max_x + padding + 1)
    max_y = min(height, max_y + padding + 1)
    
    return (min_x, min_y, max_x, max_y)

def crop_and_save(input_path, output_path, padding=10, scale=1):
    """Crop image and optionally scale it."""
    img = Image.open(input_path)
    bounds = find_crop_bounds(img, padding)
    
    cropped = img.crop(bounds)
    
    if scale != 1:
        new_size = (int(cropped.width * scale), int(cropped.height * scale))
        cropped = cropped.resize(new_size, Image.Resampling.LANCZOS)
    
    # Save as PNG
    if output_path.endswith('.png'):
        cropped.save(output_path, 'PNG', optimize=True)
    # Save as WebP
    elif output_path.endswith('.webp'):
        cropped.save(output_path, 'WEBP', quality=95, method=6)
    
    return cropped.size

if __name__ == '__main__':
    import os
    
    os.chdir('/agent/repos/News')
    
    print("Analyzing logo-full.png...")
    img = Image.open('assets/logo-full.png')
    print(f"Original size: {img.size}")
    bounds = find_crop_bounds(img, 10)
    print(f"Crop bounds: {bounds}")
    print(f"Content size: {bounds[2]-bounds[0]} x {bounds[3]-bounds[1]}")
    
    print("\nAnalyzing logo-icon.png...")
    img2 = Image.open('assets/logo-icon.png')
    print(f"Original size: {img2.size}")
    bounds2 = find_crop_bounds(img2, 10)
    print(f"Crop bounds: {bounds2}")
    print(f"Content size: {bounds2[2]-bounds2[0]} x {bounds2[3]-bounds2[1]}")
    
    print("\nCropping and generating files...")
    
    # Logo full - 1x
    size = crop_and_save('assets/logo-full.png', 'assets/logo-full.png', padding=10, scale=1)
    print(f"logo-full.png: {size}")
    
    # Logo full - 2x
    size = crop_and_save('assets/logo-full.png', 'assets/logo-full@2x.png', padding=10, scale=2)
    print(f"logo-full@2x.png: {size}")
    
    # Logo full - WebP 1x
    size = crop_and_save('assets/logo-full.png', 'assets/logo-full.webp', padding=10, scale=1)
    print(f"logo-full.webp: {size}")
    
    # Logo full - WebP 2x
    size = crop_and_save('assets/logo-full.png', 'assets/logo-full@2x.webp', padding=10, scale=2)
    print(f"logo-full@2x.webp: {size}")
    
    # Logo icon - 1x
    size = crop_and_save('assets/logo-icon.png', 'assets/logo-icon.png', padding=10, scale=1)
    print(f"logo-icon.png: {size}")
    
    # Logo icon - 2x
    size = crop_and_save('assets/logo-icon.png', 'assets/logo-icon@2x.png', padding=10, scale=2)
    print(f"logo-icon@2x.png: {size}")
    
    # Logo icon - WebP 1x
    size = crop_and_save('assets/logo-icon.png', 'assets/logo-icon.webp', padding=10, scale=1)
    print(f"logo-icon.webp: {size}")
    
    # Logo icon - WebP 2x
    size = crop_and_save('assets/logo-icon.png', 'assets/logo-icon@2x.webp', padding=10, scale=2)
    print(f"logo-icon@2x.webp: {size}")
    
    print("\nDone!")
