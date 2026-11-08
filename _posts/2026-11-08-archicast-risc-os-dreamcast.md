---
layout: post
title: "Archicast Runs RISC OS 3.11 Natively on the Sega Dreamcast"
date: 2026-11-08 07:05:00 +0000
summary: "Richard Stokes has published Archicast, a KallistiOS project that recompiles RISC OS 3.11 ahead of time for the Sega Dreamcast. Builders must supply their own RISC OS ROM; it is never included in the repository."
tags: [software, hardware]
source_url: "https://github.com/richstokes/Archicast"
source_name: "GitHub"
---

Richard Stokes has published Archicast, a project that runs RISC OS 3.11 natively on the Sega Dreamcast. The GitHub repository was created on 31 October 2026, first appearing under the name DreamRISC3, and [The Icon Bar's open source round-up](https://www.iconbar.com/articles/RISC_OS_Open_source_developments_weekly_update_7th_November_2026/index2421.html) on 7 November included it among the week's RISC OS developments.

Archicast is built on KallistiOS. RISC OS itself is not emulated, and there is no just-in-time compiler. The Acorn ROM is ARM code with no public source, so a tool recompiles it ahead of time into C and then into SH-4. The operating system and bundled applications run as native SH-4. Original Archimedes binaries that have no recompiled block drop into a built-in ARM interpreter, with nothing extra for the user to launch. Those binaries run unmodified from disc images, and their RISC OS calls still land in the native ROM.

The project's archive disc carries 261 Archimedes titles drawn from archive.org. Stokes reports that about a dozen have been tested, including Lemmings, Elite, Populous and Maestro, and that the rest are untested. Software that needs its original floppy or checks copy protection will not run.

## Own RISC OS ROM required

Archicast does not include RISC OS. RISC OS 3.11 remains Acorn's copyrighted ROM, and builders must supply their own copy. The documented build expects four 512KB chip dumps; the ROM is never committed to the repository. There is no redistributable disc image on GitHub for that reason: the public tree is source, and a build with a locally held ROM produces the Dreamcast image. The README also describes running that image in the Flycast emulator.

## Current status

On a real Dreamcast, Stokes reports a boot to the desktop in about 20 seconds. The desktop runs in mode 27, a true 640×480 display in 16 colours, with lower-resolution modes stretched to fit. Sound plays through the console's AICA, covering beeps, BASIC `SOUND` and other use of the RISC OS sound system. An SD card on the serial port adapter can appear as an ADFS hard disc.

The current tree includes networking, a small text web browser with HTTP and HTTPS (encrypted, but certificates are not verified), network printing to AirPrint printers, a Dreambox network drive, and a network time application. The Icon Bar round-up summarised the same stretch of work, including native networking, the text browser, AirPrint, Dreambox and clock-related fixes, together with the mix of native execution and the ARM interpreter for software that has not been recompiled.

Source, build instructions and architecture notes are in the [Archicast GitHub repository](https://github.com/richstokes/Archicast).
