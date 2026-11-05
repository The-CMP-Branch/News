#!/usr/bin/env python3
"""Capture screenshots of the header at different viewport widths."""

import asyncio
import sys
from pathlib import Path
from playwright.async_api import async_playwright

async def capture_screenshots():
    """Capture screenshots at specified widths."""
    widths = [1280, 768, 390, 320]
    height = 1200  # Tall enough to capture full header and some content
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        
        for width in widths:
            print(f"Capturing screenshot at {width}px width...")
            page = await browser.new_page(viewport={'width': width, 'height': height})
            
            # Navigate to test page
            await page.goto('file:///agent/repos/News/test_header.html')
            
            # Wait for fonts to load
            await page.wait_for_timeout(1000)
            
            # Take screenshot
            output_path = f'/agent/repos/News/screenshots/header-{width}px.png'
            await page.screenshot(path=output_path, full_page=False)
            print(f"  Saved: {output_path}")
            
            await page.close()
        
        await browser.close()
        print("\nAll screenshots captured!")

if __name__ == '__main__':
    import os
    os.makedirs('/agent/repos/News/screenshots', exist_ok=True)
    asyncio.run(capture_screenshots())
