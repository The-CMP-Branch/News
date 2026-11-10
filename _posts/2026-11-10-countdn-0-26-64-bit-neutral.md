---
layout: post
title: "!CountDn 0.26 is 64-bit Neutral"
date: 2026-11-10 23:10:00 +0000
summary: "Chris Hall has released !CountDn 0.26, the Countdown numbers game for RISC OS, now 64-bit neutral after replacing ArmSort with a BASIC quicksort."
tags: [software, games]
source_url: "https://www.riscosopen.org/forum/forums/1/topics/20636"
source_name: "RISC OS Open Forums"
---

Chris Hall has released !CountDn version 0.26 on !Store. Announced on the [RISC OS Open forums](https://www.riscosopen.org/forum/forums/1/topics/20636) on 31 October 2026, the program implements the Countdown numbers game.

Hall describes the update as 64-bit neutral. Because the application is written in BASIC, the change was limited: he replaced the `ArmSort:sort` command, which does not yet run correctly on RISC OS 64, with a quicksort written in BASIC. The sort is used so that a difficulty spectrum can be shown once the tiles have been selected.

The 32-bit ARM code produced by the BASIC assembler — which works out how easy each of the 900 possible targets might be for the chosen tiles — is emulated on RISC OS 64. Hall says that takes a few more centiseconds than running natively on a CM4.

!CountDn 0.26 is available from !Store. Discussion is in the [forum announcement](https://www.riscosopen.org/forum/forums/1/topics/20636).
