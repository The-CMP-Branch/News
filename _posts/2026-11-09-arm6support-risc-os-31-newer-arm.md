---
layout: post
title: "ARM6Support Gains Cache Flushing and ARM710 Work for RISC OS 3.1"
date: 2026-11-09 07:45:00 +0000
summary: "Sarah Walker and Ian Jeffray have updated ARM6Support to improve cache handling, write buffering and processor detection for RISC OS 3.1 on newer ARM CPUs."
tags: [community, hardware, development]
source_url: "https://github.com/sarah-walker-pcem/ARM6Support"
source_name: "GitHub"
---

Sarah Walker's [ARM6Support](https://github.com/sarah-walker-pcem/ARM6Support) module adds ARM610 and ARM710 support under RISC OS 3.1 on Archimedes machines with experimental CPU boards. [The Icon Bar's open source round-up](https://www.iconbar.com/articles/RISC_OS_Open_source_developments_weekly_update_7th_November_2026/index2421.html) on 7 November, by Charles Ferguson, covered recent updates to the module.

The README describes a module that initialises the MMU for those newer ARM processors. Walker has added cache flushing when memory mappings change, enabled the write buffer (required for original ARM710), and extended caching and write buffering to more of memory, including module, sprite and system heap areas, ROM, and video memory. Ian Jeffray contributed ARM710 support, with corrections to processor identification, page-table alignment and caching of the first 16 MB, plus CPU detection that ignores revision differences. Walker has also implemented permissions for static areas at or above 32 MB, covering ROM, I/O and physical RAM.

Source and version history are in the [ARM6Support GitHub repository](https://github.com/sarah-walker-pcem/ARM6Support).
