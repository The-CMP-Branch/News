---
layout: post
title: "Andrew Youll round-up: OpenTTD 15.3, RISC OS on Linux 1.0.0093 images, RISC3D, GTK and Folio updates"
date: 2026-11-28 08:00:00 +0000
summary: "A combined round-up of Andrew Youll's RISC OS releases from 25–27 November 2026, covering OpenTTD 15.3, RISC OS on Linux 1.0.0093 images, RISC3D, GTK start-up, Folio's Draw export, and Reel."
tags: [andrew-youll, round-up, software, development]
source_url: "https://www.riscosopen.org/forum/forums/1"
source_name: "RISC OS Open Announcements"
---

This is a combined round-up of Andrew Youll's updates from 25–27 November 2026, grouped by project. The announcements were posted in the RISC OS Open Announcements forum, with matching GitHub releases. It follows this site's [round-up of 22–25 November]({{ '/2026/11/25/andrew-youll-round-up-risc3d-folio-lumen-groove/' | relative_url }}).

## OpenTTD

Posted on 27 November in [!OpenTTD 14.1 Port](https://www.riscosopen.org/forum/forums/1/topics/20560), with the GitHub release [OpenTTD 15.3 for RISC OS](https://github.com/adyoull/riscos-openttd/releases/tag/15.3.1).

The RISC OS port moves from 14.1 to 15.3, the current OpenTTD stable. That brings the upstream 15.0–15.3 work, including maps with water beyond their edges, bridges over stations, waypoint improvements, and many interface changes.

The window and icon bar icon now appear within a few seconds, with a small "Loading OpenTTD, please wait…" box until the title screen is ready. The desktop keeps running while the game loads.

OpenTTD 15 needs newer C++ than GCC 10 had, so this build uses GCC 16.2 from the optional toolchain in riscos-crossdev 1.14, with UnixLib 5.0.3.12. The window is the right size in alpha-channel desktop modes, and it works in desktops of fewer than 32 bits per pixel.

Through Youll's PackMan source (`https://adyoull.github.io/riscos-packages/pkg/index`) it shows as OpenTTD 15.3.0.1-1. The OpenTTD-OpenSFX and OpenTTD-OpenMSX packages are unchanged. 15.3 loads games saved by 14.1, but 14.1 cannot load 15.3 saves, so keep a copy of any save you might want to take back. Network games need the same version.

As before, you need ARMEABISupport and SharedUnixLibrary from PackMan. For sound, StreamManager and SharedSoundBuffer (John Duffell's freeware) are required.

## RISC OS on Linux

These updates were posted in [Updated RISC OS on Linux](https://www.riscosopen.org/forum/forums/1/topics/20657).

On 25 November afternoon, Configure > Updates brought printing through Linux's CUPS (Configure > Linux printing), faster downloads, a working Ping, ShareFS and Freeway, USB joysticks and gamepads, RISC3D 0.10 and MesaLibs 20.3.5-23 on the disc, and riscos-rom 5.31-32.

That evening, ShareFS's Discs icon was fixed when the network comes up after the desktop — as it can on a Pi 5 starting from NVMe, or on Wi-Fi (riscos-harddisc 1.0.0076-1). Configure > Linux printing now shows ink and toner levels, and the printer you choose stays in CUPS's own web pages.

On 26 November, Updates no longer runs out of memory on a large first update (riscos-harddisc 1.0.0078-1, thanks to David Pitt). It now has 1 MB. If an older Updates stops with "No room for function/procedure call" or "Too many nested structures", raise its WimpSlot once: Shift-double-click !Boot, open Resources then Configure, Shift-double-click !ROLUpdate, and change the `WimpSlot` line in `!Run` to `WimpSlot -min 1024k -max 1024k`. That update brings the fixed Updates, so you only need to do this once. Updates 1.04 (riscos-harddisc 1.0.0079-1) then updates itself and the Linux side first, restarts where it was, and installs the rest. Printing is no longer removed by a later update (riscos-support 1.0.0091-1).

On 27 November Youll published new [1.0.0093 images](https://github.com/adyoull/RISCOSonLinux/releases/tag/1.0.0093): generic (Pi 3/4/5, 400/500, Compute Modules, Zero 2 W, UEFI machines and Pinebooks), UTM for Apple Silicon Macs, and the Windows Dev Kit 2023. They include RISC OS 5.31-33, CUPS printing and RISC3D 0.25. Existing installs reach the same through Configure > Updates. They have only been tried under emulation so far; reports from real machines are welcome.

From David Sharp's testing: Dismount hands a RISC OS-format USB stick or card back to Linux so it is safe to remove; a small Pi card image written to a larger card is now seen as RISC OS's; abort handlers can restore DFAR, DFSR, IFAR and IFSR (which had left GCC 10 programs stopping with an EMT trap); and a file whose RISC OS type cannot be read no longer breaks its directory (RISC OS 5.31-33).

## RISC3D

Posted in [RISC3D: 3D acceleration for RISC OS on Linux and RISC OS on the Pi 4](https://www.riscosopen.org/forum/forums/1/topics/20678).

[RISC3D 0.22](https://github.com/adyoull/riscos-risc3d/releases/tag/v0.22) (25 November evening; 0.19–0.21 were unpublished) adds a tick box on Configure's RISC3D page to draw the desktop's copies and fills on the GPU. It is applied at once and kept; it remains off by default.

[RISC3D 0.25](https://github.com/adyoull/riscos-risc3d/releases/tag/v0.25) (`!RISC3D` 0.11-5), announced in the RISC OS on Linux topic on 27 November: a program's 3D contexts last until it ends, so one that runs a `*command` keeps them. Configure's RISC3D page shows the driver's version. The Linux side (0.23-1) lets contexts share their objects, one per thread, for programs such as web browsers.

## GTK

Posted in the [GTK 3.24.41](https://www.riscosopen.org/forum/forums/1/topics/20588) topic on 25 November evening.

[`!GTKLibs` 3.24.52-33](https://github.com/adyoull/riscos-gtk/releases/tag/gtklibs-3.24.52-33) is for every GTK program; none of them needs updating for it. Youll profiled it on a Pi 4 under RISC OS itself. Fonts are given to fontconfig as one cached folder instead of being re-read one by one at every start, and GTK draws straight into each window's off-screen picture. A test window went from 3.7 s to 0.4 s from the second start on, and scrolling from 70 to 80 steps a second. The first start after installing still builds the caches.

## Folio

Posted in [Folio: a PDF and ebook reader for the desktop](https://www.riscosopen.org/forum/forums/1/topics/20590) on 25 November evening.

[0.0.1-test78](https://github.com/adyoull/riscos-folio/releases/tag/v0.0.1-test78) adds a Pictures choice to Export as Draw: As in the PDF, 150 dpi, or 90 dpi. The lower settings shrink finer scans by averaging pixels, so thin lines stay whole in Draw. Download [Folio-0.0.1-test78.zip](https://github.com/adyoull/riscos-folio/releases/download/v0.0.1-test78/Folio-0.0.1-test78.zip). There is a matching RiscPC zip.

## Reel / FFmpeg

Posted on 26 November in [!FFmpeg 5.1.10 LTS & New Video Player !Reel & !ReelEGL](https://www.riscosopen.org/forum/forums/1/topics/20565).

[Reel 0.1.32](https://github.com/adyoull/riscos-ffmpeg/releases/tag/reel-0.1.32) and [FFmpeg 5.1.10 riscos25](https://github.com/adyoull/riscos-ffmpeg/releases/tag/v5.1.10-riscos25) are rebuilt with UnixLib 5.0.3.12. RISC OS Open had already allocated `!FFmpeg` and `*ffmpeg`, so the application is now `!FFmpeg5` (`*ffmpeg5`). A fix covers files that stop short of their end: a large MKV on a NAS through LanMan98 could stop part-way through, because LanMan98 cannot read past 2 GB. In PackMan they are Reel 0.1.32.0.1-1 (with `!ReelEGL`) and FFmpeg 5.1.10.0.25-1.
