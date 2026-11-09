---
layout: post
title: "ARM6Support Gains Cache Flushing and ARM710 Work for RISC OS 3.1"
date: 2026-11-09 07:45:00 +0000
summary: "Sarah Walker and Ian Jeffray have pushed a run of ARM6Support updates that improve cache handling, write buffering and processor detection for RISC OS 3.1 on newer ARM CPUs."
tags: [community, hardware, development]
source_url: "https://github.com/sarah-walker-pcem/ARM6Support"
source_name: "GitHub"
---

Sarah Walker's [ARM6Support](https://github.com/sarah-walker-pcem/ARM6Support) module, which adds ARM610 and ARM710 support under RISC OS 3.1 on Archimedes machines with experimental CPU boards, has seen a burst of commits in early November 2026. [The Icon Bar's open source round-up](https://www.iconbar.com/articles/RISC_OS_Open_source_developments_weekly_update_7th_November_2026/index2421.html) on 7 November, by Charles Ferguson, listed the same stretch of work.

The README describes a module that initialises the MMU for those newer ARM processors. Walker's commits of 1–2 November match the round-up's account of cache flushing when memory mappings change, and of caching and write buffering across more memory regions:

- version 0.06 traps `OS_SetMemMapEntries` and flushes the cache
- 0.07 enables the write buffer, which the commit message says is required for original ARM710 (not ARM710a) because of a CPU bug
- 0.08 enables caching in module, sprite and system heap areas
- 0.09 enables caching of ROM and reworks CPU type detection
- 0.10 marks video memory as bufferable

## ARM710 support and processor detection

Ian Jeffray's ARM710 work was merged into Walker's repository on 1 November 2026 ([pull request #3](https://github.com/sarah-walker-pcem/ARM6Support/pull/3)). The commits themselves are older — ARM710 support, a control-register correction, page-table alignment handling and caching over the first 16 MB date from June 2025, with corrected ARM710 identifiers in April 2026 — and are now in the canonical tree as versions 0.02 to 0.05. That is the ARM710 support, identifier and alignment work The Icon Bar summarised.

On 4 November Jeffray added version 0.11, which masks the revision field before comparing CPU IDs so processor detection ignores revision differences. Walker followed on 8 November with 0.12, implementing permissions for static areas at or above 32 MB, including ROM, I/O and physical RAM. That last change landed after The Icon Bar's 7 November round-up.

The module's source, version history and recent commits are in the [ARM6Support GitHub repository](https://github.com/sarah-walker-pcem/ARM6Support).
