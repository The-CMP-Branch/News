---
layout: post
title: "ReelEdit 0.3 Beta Brings Non-Linear Video Editing to RISC OS"
date: 2026-11-07 07:00:00 +0000
summary: "Andrew Youll has released ReelEdit, a non-linear video editor for RISC OS 5 on the Raspberry Pi, built on MLT and FFmpeg with features including multi-track editing, effects, titles, and hardware-accelerated export."
tags: [software, multimedia]
source_url: "https://www.riscosopen.org/forum/forums/1/topics/20631"
source_name: "RISC OS Open Forums"
---

Andrew Youll has released ReelEdit 0.3 Beta, a non-linear video editor for RISC OS 5 on the Raspberry Pi. Built on the MLT framework (which powers Shotcut and Kdenlive) and FFmpeg, ReelEdit uses the Pi's VideoCore to decode H.264 video and encode when exporting. The software was developed with Anthropic's Claude as a coding assistant.

The editor provides cut, trim, move, split and roll operations for clips, with marks, extract and lift, copy and paste, and 100 levels of undo. Audio can be muted, faded or adjusted per clip, with separate music and sound effects tracks that stack as needed. An overlay track supports logos, pictures and picture-in-picture, while titles use RISC OS fonts on their own track and can overlay other visual elements.

ReelEdit supports slow motion, fast motion and reverse playback, along with fades, dissolves and wipes including circle, barn doors, diagonal, box and clock patterns with soft edges. A Clips window enables three-point editing with insert and overwrite operations. The Inspector panel provides colour adjustment (brightness, contrast, saturation, warmth, midtones, or preset looks including Vivid, Warm, Cool, Faded, Black and white, Sepia and Night), pan and zoom, special effects (Negative, Sketch and Posterise), sound clean-up with rumble cut and clearer voices, and keyframes for animated overlay movement and growth. Green screen compositing is also supported.

To handle demanding projects and HEVC clips, the editor offers render previews and automatic proxies, ensuring smooth playback. Autosave with crash recovery is built in. Export produces MP4 files (H.264 and AAC) using the Pi's VideoCore encoder, with fallback to ARM encoding if the hardware encoder fails. Exported files receive the AVI filetype (&FB2) so Reel and the Filer recognise them as videos, while keeping the `/mp4` extension for other systems.

The current release, Beta 3, improves performance when jumping into MKV files without an index. Some MKV files lack Cues (an index structure), which previously forced FFmpeg to read large portions of the file to locate a specific position. The editor now reads approximately one megabyte at the target position, finds the nearest keyframe, and starts from there, reducing delays from minutes to seconds when working with files on network shares.

The software requires RISC OS 5 on a Raspberry Pi 2, 3 or 4, SharedUnixLibrary 1.16 or later, ARMEABISupport, SharedSoundBuffer and StreamManager for audio, and `gpu_mem=128` in config.txt for 1080p editing. An illustrated user guide opens in NetSurf by pressing F1 or choosing User guide from the icon bar menu.

ReelEdit is free software under the GNU GPL and is available from PackMan (via the source `https://adyoull.github.io/riscos-packages/pkg/index`) or as a direct download from the [GitHub releases page](https://github.com/adyoull/riscos-reeledit/releases/tag/v0.3-beta3). The [forum announcement thread](https://www.riscosopen.org/forum/forums/1/topics/20631) is open for discussion, and logging can be enabled from the icon bar menu for problem reports.
