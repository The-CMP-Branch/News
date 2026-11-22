---
layout: post
title: "Andrew Youll round-up: RISC3D 0.11, GTK app saving fixes, Lumen 0.0.40 astro stacking, Groove 0.4.2 and RISC OS on Linux updates"
date: 2026-11-22 08:05:00 +0000
summary: "A combined round-up of Andrew Youll's RISC OS releases from 17–21 November 2026, covering RISC3D's allocated SWIs, RISC OS on Linux, GTK save-format fixes, Lumen's FITS stacking, and Groove 0.4.2."
tags: [andrew-youll, round-up, software, development]
source_url: "https://www.riscosopen.org/forum/forums/1"
source_name: "RISC OS Open Announcements"
image: /assets/images/lumen-stack-frames.png
image_alt: "Lumen 0.0.40's Stack frames window after stacking six FITS frames"
---

This is a combined round-up of Andrew Youll's updates from 17–21 November 2026, grouped by project. The announcements were posted in the RISC OS Open Announcements forum, with matching GitHub releases.

## RISC3D / riscos-mesa / V3DRender

Youll announced these on 18 November in the topic [RISC3D: 3D acceleration for RISC OS on Linux and RISC OS on the Pi 4](https://www.riscosopen.org/forum/forums/1/topics/20678), following this site's earlier note of [RISC3D 0.10]({{ '/2026/11/17/risc3d-0-10-gpu-opengl-classicube/' | relative_url }}).

[RISC3D 0.11](https://github.com/adyoull/riscos-risc3d/releases/tag/v0.11) now uses its own ROOL-allocated SWI chunks and error blocks: RISC3D SWIs `&5AF80` and errors `&823D00`; Linux3D errors `&823C00`; V3DRender SWIs `&5AFC0` and errors `&823E00`. It is a clean break. RISC3D and `!MesaLibs` must be updated together; programs need [riscos-mesa 20.3.5-22](https://github.com/adyoull/riscos-mesa/releases/tag/v20.3.5-22)'s `!MesaLibs` or they fall back to software rendering. In PackMan the matching packages are RISC3D 0.05 and MesaLibs 20.3.5-22. Programs that must have RISC3D should use `RMEnsure RISC3D 0.05`.

The Windows Dev Kit 2023 is the first GPU other than the Pi 4's confirmed working. Chris Gransden's Quakespasm went from 5 fps at 640×480 in software to 98 fps at 1920×1080.

riscos-mesa 20.3.5-22's RISC3D client 0.11 uses the new SWIs. Statically linked programs need relinking.

[V3DRender 0.16](https://github.com/adyoull/riscos-v3drender/releases/tag/v0.16) has the allocated SWIs and errors, and needs RISC3D 0.05.

On 20 November, after a Compute Module 4 user reported an "Internal abort" at boot, Youll said Rob Heaton's V3DDriver must not be loaded alongside RISC3D, as both claim the GPU.

## RISC OS on Linux

These updates were posted in [Updated RISC OS on Linux](https://www.riscosopen.org/forum/forums/1/topics/20657), after this site's [earlier RISC OS on Linux coverage]({{ '/2026/11/08/risc-os-on-linux-updated-release/' | relative_url }}).

**riscos-harddisc.** 1.0.0068-1 (17 November): RiscOSM starts again (a cut-down test Iconv was replaced by ROOL's Iconv 0.12). 1.0.0070-1 (17 November): HardDisc4's icon bar menu replaces Dismount with Close windows. 1.0.0071-1, with riscos-support 1.0.0077-1 (18 November): 4K-sector USB discs are refused with a clear message. 1.0.0072-1 (18 November): the current directory is HardDisc4 at start-up, so crash dumps and similar saves work.

**riscos-support.** 1.0.0078-1 (18 November) removes a once-a-second pause in 3D games (TORCS, ClassiCube, Warzone 2100, YSFlight); gives a steadier pointer when RISC OS is busy, mainly under UTM; and makes riscos-risc3d part of RISC OS on Linux. 1.0.0079-1 (19 November) restores PackMan 0.9.8 to `Apps.Admin` if it is missing. 1.0.0080-1 (19 November) checks and repairs the FAT boot partition at every start-up using dosfstools, logging to `fat-check.txt` in LOGS, which addresses "Read-only file system" update failures.

**riscos-kernel-pi.** 6.6.78-17 and -18 (19 November) build in Linux's HEVC (H.265) decoder driver, for ReelHWAccel under RISC OS on Linux. On a Pi 4, all test clips (8-bit and 10-bit, 1080p and 4K) decoded correctly at 85–90% of native speed. The driver also covers the Pi 5 and CM5. The ReelHWAccel build that uses it is to come separately and has not been released yet.

## GTK apps

These were posted in the [riscos-gtk](https://www.riscosopen.org/forum/forums/1/topics/20588) topic, after this site's note of [RC18 and shared `!GTKLibs`]({{ '/2026/11/10/riscos-gtk-rc18-shared-gtklibs/' | relative_url }}).

`!GTKLibs` 3.24.52-22 (18 November, GitHub and PackMan) lets Shift and Ctrl with function keys, and Print Scrn, reach programs. F12 stays with the desktop.

[AbiWord 3.0.8-riscos9](https://github.com/adyoull/riscos-gtk/releases/tag/abiword-3.0.8-riscos9) and [`!GTKLibs` 3.24.52-24](https://github.com/adyoull/riscos-gtk/releases/tag/gtklibs-3.24.52-24) (20 November) put the program's format menu in the Save box; choosing a format changes the extension. A name typed as, for example, `Report/docx`, `/rtf` or `/odt` saves in that format. AbiWord's ".doc" is actually RTF; use `/rtf` for EasiWriter and `/docx` for Word 2007 or later.

[Gnumeric 1.12.62-riscos23](https://github.com/adyoull/riscos-gtk/releases/tag/gnumeric-1.12.62-riscos23) (21 November) makes `Book1/xlsx`, `/xls` and `/ods` produce real Excel 2007, Excel 97 and OpenDocument files. It needs `!GTKLibs` 3.24.52-24.

[mtPaint 3.50.14-riscos18](https://github.com/adyoull/riscos-gtk/releases/tag/mtpaint-3.50.14-riscos18) (21 November) opens the directory browser from Browse…, and a typed extension (`jpg`, `gif`, `bmp` or `png`) sets the format.

## Lumen

Posted in [Lumen](https://www.riscosopen.org/forum/forums/1/topics/20646), after this site's [first-release report]({{ '/2026/11/06/lumen-photo-library-editor-first-release/' | relative_url }}).

[0.0.39.1](https://github.com/adyoull/riscos-lumen/releases/tag/v0.0.39.1) (17 November) adds Filer-style photo selection: a drag box, Shift-click, and blue shading. RiscOSM now shows heights correctly.

[0.0.39.2](https://github.com/adyoull/riscos-lumen/releases/tag/v0.0.39.2) (18 November) stops the browser scrolling sideways, makes Adjust-drag toggle like the Filer, and starts RiscOSM properly from "Show on map" (reported by Matthew Phillips).

[0.0.40](https://github.com/adyoull/riscos-lumen/releases/tag/v0.0.40) (21 November) reads FITS astronomy images (`.fits`, `.fit` and `.fts`; mono, RGB or colour mosaic), auto-stretched, with the header in the Info tab. Selection > Stack frames… subtracts a master dark, aligns frames by their stars (including across a meridian flip) and averages with sigma clipping so satellite and aircraft trails disappear. The result is a 32-bit FITS in the library. Raw frames can be stacked through the new LumenRaw 1.5. A new LumenWebP 1.0 plug-in reads WebP using libwebp, with NEON where available. Flat and bias frames are not yet used.

[![Lumen 0.0.40's Stack frames window after stacking six FITS frames]({{ '/assets/images/lumen-stack-frames.png' | relative_url }}){: width="880" height="550" loading="lazy"}]({{ '/assets/images/lumen-stack-frames.png' | relative_url }})

*Lumen 0.0.40's Stack frames window. Credit: Andrew Youll, riscos-lumen user guide.*

## Groove

Posted in [Groove: a music studio for RISC OS](https://www.riscosopen.org/forum/forums/1/topics/20638), after this site's note of [Groove 0.4]({{ '/2026/11/19/groove-0-4-musescore-musicxml-scores/' | relative_url }}).

[0.4.1](https://github.com/adyoull/riscos-groove/releases/tag/v0.4.1) (19 November) opens scores saved by MuseScore 4.2 and later; brass and strings no longer play as piano; and full scores are no longer capped at 16 parts.

[0.4.2](https://github.com/adyoull/riscos-groove/releases/tag/v0.4.2) (21 November) reads a score's own dynamics, hairpins, slurs, staccato, accents and 8va/15ma lines; tempo changes are read and played; arpeggios are drawn and played spread. Playback uses about half the CPU time (a 26-part score takes about 5% of a Pi 4), and notes start sample-accurately. Fixes from Paul Sprangers' report: no freeze choosing Score with no track selected, a close icon on the Score window, and no empty leading bars on a dropped score.

Andrew is speaking at WROCC's meeting on 2 December 2026, "Andrew Youll – Building Blocks", about his ports, his own software, his use of AI and RISC OS on Linux ([WROCC meetings](https://www.wrocc.org.uk/meetings)).
