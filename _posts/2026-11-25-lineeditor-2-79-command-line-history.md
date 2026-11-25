---
layout: post
title: "LineEditor 2.79 Released for RISC OS 3.1x to 5.x"
date: 2026-11-25 17:00:00 +0000
summary: "Jon Abbott of JASPP has released LineEditor 2.79, a 26/32-bit neutral command-line history module that runs on RISC OS 3.1x to RISC OS 5.x, available from PackMan and the JASPP forum."
tags: [software]
source_url: "https://stardot.org.uk/forums/viewtopic.php?t=34021"
source_name: "StarDot"
---

Jon Abbott of the Archimedes Software Preservation Project ([JASPP](https://www.jaspp.org.uk)), who posts on StarDot as sirbod, has released LineEditor 2.79. He announced it on [StarDot](https://stardot.org.uk/forums/viewtopic.php?t=34021) on 25 November 2026. The download was posted the day before in the JASPP forum topic [LineEditor 2.79](https://forums.jaspp.org.uk/forum/viewtopic.php?p=6257).

LineEditor is a command-line history module originally written by Olly Betts, with further contributors since 2003. Abbott's 2.79 build is 26/32-bit neutral and runs on RISC OS 3.1x to RISC OS 5.x. On the JASPP forum he notes that it supplies history at command prompts such as Supervisor and BASIC.

Abbott says he has been quietly maintaining the module since 2015 and is not sure he ever released it. He has fixed obvious bugs, made it backward compatible with RISC OS 3.1x, and made it ROM-safe, though he does not recall testing it in a ROM.

The JASPP release notes for 2.79 list three changes: commented-out code has been removed and the help tidied, the module flags have been moved to after the code, and the special character in the dictionary is now `^`.

## Installing

LineEditor can be installed through PackMan using the [JASPP source](https://www.jaspp.org.uk/packages/release). The index lists package LineEditor 2.79-1. It can also be downloaded from the [JASPP forum post](https://forums.jaspp.org.uk/forum/viewtopic.php?p=6257), which attaches `LineEditor279.zip` (the module and `!Help`) and `LineEditor279_src.zip` (the BASICTxt source). To load it at boot, that post says to copy the module to `!Boot.Choices.Boot.Tasks`.
