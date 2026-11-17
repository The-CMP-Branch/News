---
layout: post
title: "PiArcBoot Offers One-Click Archimedes Games on Raspberry Pi OS, Linux and Windows"
date: 2026-11-17 08:00:00 +0000
summary: "James Hansen has released PiArcBoot, a free ArcEm-based launcher that installs JASPP Archimedes games and boots each one as its own app on Raspberry Pi OS, Linux and Windows, using a ROM built from RISC OS Open sources so no commercial ROM is required."
tags: [software, emulation, games]
source_url: "https://github.com/jameshansen/PiArcBoot"
source_name: "PiArcBoot on GitHub"
image: /assets/images/piarcboot-launcher.png
image_alt: "PiArcBoot launcher listing Archimedes games on the JASPP tab"
---

James Hansen (Stardot username Qjimbo) has released PiArcBoot, a launcher that installs Acorn Archimedes games from [JASPP](https://www.jaspp.org.uk), the Archimedes Software Preservation Project, and boots each one straight into the game. He posted about it on [Stardot](https://stardot.org.uk/forums/viewtopic.php?t=33945) on 16 November 2026. The first release, [v1.0.0](https://github.com/jameshansen/PiArcBoot/releases/tag/v1.0.0), was published on 14 November 2026; the latest at the time of writing is [v1.1.4](https://github.com/jameshansen/PiArcBoot/releases/tag/v1.1.4) on 17 November.

It runs on Raspberry Pi OS, Linux and Windows. There is no RISC OS-hosted version. The project is based on [ArcEm](https://github.com/ArcEm-emu/ArcEm). It needs no commercial ROM: it uses [ROO311](https://github.com/jameshansen/ROO311), a "3.11 compatible" ROM built from RISC OS Open sources.

[![PiArcBoot launcher listing Archimedes games on the JASPP tab]({{ '/assets/images/piarcboot-launcher.png' | relative_url }}){: width="660" height="582" loading="lazy"}]({{ '/assets/images/piarcboot-launcher.png' | relative_url }})

*PiArcBoot's launcher. Image: James Hansen / PiArcBoot.*

## Games, saves and extras

The launcher lists 120 JASPP games and 16 Classics, among them Elite, Star Fighter 3000 and Asylum, plus PackMan desktop games. PiArcBoot bundles none of the games: Install downloads each title's floppy images from JASPP, and an installed game then plays offline.

Each game runs as its own application, with its own window, icon and shortcuts. Every game has three save-state slots, one of which is written automatically every 30 seconds of play. CRT-Royale shaders (an optimised CRT-Royale-Pi, from TroggleMonkey's CRT-Royale) are available, with a lighter CRT-Pi filter as well.

The My Games tab loads your own JFD, ADF, ADL and HFE disc images, or a zip of them, and also Spark and ArcFS archives of RISC OS applications. A Slower Mode runs a game at the speed of an A3000's 8 MHz ARM2 rather than a 25 MHz ARM3.

## Licence and credits

PiArcBoot is unofficial and is not affiliated with JASPP or RISC OS Open. It is free software under GPL-3.0. Hansen says it was written with AI help, using Claude Code (and, on Stardot, he names Opus 5.5 and some Fable 5.2 for optimisation); he says the key design decisions were his own.

Downloads, installers and the README are on the [PiArcBoot GitHub repository](https://github.com/jameshansen/PiArcBoot).
