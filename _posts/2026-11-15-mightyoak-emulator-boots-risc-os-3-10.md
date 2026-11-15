---
layout: post
title: "MightyOak Archimedes and RiscPC Emulator Boots RISC OS 3.10"
date: 2026-11-15 07:50:00 +0000
summary: "Nick Arkell has brought MightyOak, an early-stage Acorn Archimedes and RiscPC emulator, to the point of booting RISC OS 3.10, with Claude used to help implement hardware emulation, tests and debugging tools."
tags: [software, emulation]
source_url: "https://www.iconbar.com/articles/RISC_OS_open_source_developments_weekly_update_14th_November_2026/index2424.html"
source_name: "The Icon Bar"
---

Nick Arkell has brought MightyOak, an Archimedes and RiscPC emulator, to the point of booting RISC OS 3.10. Charles Ferguson reported the milestone in [The Icon Bar's open source round-up](https://www.iconbar.com/articles/RISC_OS_open_source_developments_weekly_update_14th_November_2026/index2424.html) of 14 November 2026.

Arkell used Claude to help implement hardware emulation, tests and debugging tools, then refined the results and corrected faults uncovered during booting. Further work improved video handling, repaired keyboard and mouse input, and fixed memory-controller register decoding. The [MightyOak](https://github.com/GiantRobotLemur/MightyOak) repository records this in the 7 November 2026 commit [Claude's initial additions to allow RISC OS boot (#30)](https://github.com/GiantRobotLemur/MightyOak/commit/b46d7285cf982b242ab564bfdb4239ebe1183ab3).

The README describes MightyOak as an Acorn Archimedes and RiscPC emulator. Its main components are written in C++, and MightyOakLib depends on SDL3. The documented build currently supports Visual Studio 2022 and gcc 11, both on x64.

This is early work in progress, not a release. Source is in the [MightyOak GitHub repository](https://github.com/GiantRobotLemur/MightyOak).
