---
layout: post
title: "riscos-gtk RC18 Shares One GTK Through !GTKLibs"
date: 2026-11-10 23:22:00 +0000
summary: "Andrew Youll's riscos-gtk public beta RC18 moves GTK 3.24.52 and its supporting libraries into a shared !GTKLibs pack, cutting program sizes sharply and letting several GTK applications share one copy in memory."
tags: [software, development]
source_url: "https://www.riscosopen.org/forum/forums/1/topics/20588"
source_name: "RISC OS Open Forums"
image: /assets/images/riscos-gtk-rc18-all-programs.jpg
image_alt: "Eight riscos-gtk programs running together on the RISC OS desktop from one shared !GTKLibs"
---

Andrew Youll has released riscos-gtk public beta RC18, a substantial change from the [RC15 build this site covered on 3 November]({{ '/2026/11/03/riscos-gtk-rc15-released/' | relative_url }}). Until this release, each GTK program shipped its own complete copy of GTK and the libraries underneath it. RC18 instead installs one shared set, `!GTKLibs`, in `!Boot.Resources`, using mixed linking from riscos-crossdev 1.11.

Youll announced the release on the [RISC OS Open forums](https://www.riscosopen.org/forum/forums/1/topics/20588) on 10 November 2026. The [GitHub release](https://github.com/adyoull/riscos-gtk/releases/tag/v3.24.52-riscos1.0-rc18) carries the same notes, the downloads and screenshots.

## One shared GTK

Mixed linking keeps UnixLib and each program's own libraries inside the application. GTK 3.24.52, riscos-gtk's RISC OS backend, and the libraries under it — Youll lists GLib, cairo, pango, harfbuzz, FreeType, fontconfig, pixman, libpng and libjpeg among them — become 26 shared libraries in `!GTKLibs`, loaded by !SharedLibs.

Programs that run together then share that copy. On a Raspberry Pi with Geany and L3afpad both open, Youll reports the shared libraries used 20 MB, the same as with Geany alone. Against RC17, the program files themselves shrink:

- L3afpad: 17.2 MB to 0.75 MB
- mtPaint: 18.0 MB to 1.5 MB
- Geany: 22.6 MB to 6.7 MB
- ClawsMail: 25.1 MB to 9.6 MB
- Gnumeric: 27 MB to 11.1 MB
- AbiWord: 32.8 MB to 18.8 MB
- `!GTKLibs`, installed once: 20.5 MB

[![Eight riscos-gtk programs running together on the RISC OS desktop from one shared !GTKLibs]({{ '/assets/images/riscos-gtk-rc18-all-programs.jpg' | relative_url }}){: width="1280" height="1024" loading="lazy"}]({{ '/assets/images/riscos-gtk-rc18-all-programs.jpg' | relative_url }})

*All eight bundled programs running together from one !GTKLibs, on RISC OS 5.31 on Linux. Screenshot from Andrew Youll's [riscos-gtk RC18 GitHub release](https://github.com/adyoull/riscos-gtk/releases/tag/v3.24.52-riscos1.0-rc18).*

## Installing !GTKLibs

Installation has changed. The programs need `!GTKLibs` in `!Boot.Resources` alongside `!SharedLibs`. They also need the newer `ld-riscos/so/2` loader and SOManager 3.x, which PackMan's SharedLibs 4.0 does not include. `!GTKLibs` carries those and adds them to the existing `!SharedLibs` when it boots: the loader only if it is missing, SOManager only if the installed copy is older.

The steps given in the forum post are:

1. Download `GTKLibs-3.24.52-19.zip`.
2. Shift-double-click `!Boot` and open `Resources`.
3. Copy `Resources.!GTKLibs` from the zip into that folder. If there is no `!SharedLibs` yet, install PackMan's SharedLibs first.
4. Restart, or run a program: its `!Run` boots the libraries and reports what is missing if it cannot start.

Youll says PackMan packages of GTKLibs and the updated programs are on their way, after which PackMan will handle the install.

## Faster drawing

pixman (used for cairo's drawing), libjpeg-turbo and libpng now use NEON on machines that have it. The GitHub release notes add that those paths are chosen at start-up, so machines without NEON still run.

## Requirements and testing

The software needs RISC OS 5 on ARMv7 or later hardware, such as a Raspberry Pi 2 or later, in a 16 or 32 bpp screen mode, plus SharedUnixLibrary 1.16 or later, ARMEABISupport and Iconv from PackMan, and both `!GTKLibs` and PackMan's SharedLibs. ClawsMail still needs RISC OS 5.28 or later for AcornSSL.

Youll has tried Geany and L3afpad on a Pi, sharing GTK, and all eight programs at once on RISC OS 5.31 on Linux, plus the automatic tests. The other six programs have not yet been run on a Pi in this form, so reports from real machines are particularly welcome.

The bundled applications in this release are Gnumeric 1.12.62-riscos21, AbiWord 3.0.8-riscos7, ClawsMail 4.4.0-riscos28, L3afpad 0.8.18.1.11-riscos37, Geany 2.1-riscos16 and mtPaint 3.50.14-riscos16, with an optional colour emoji font unchanged from earlier releases. The development kit, source and checksums are on the [RC18 GitHub release](https://github.com/adyoull/riscos-gtk/releases/tag/v3.24.52-riscos1.0-rc18). Discussion continues in the [forum thread](https://www.riscosopen.org/forum/forums/1/topics/20588).
