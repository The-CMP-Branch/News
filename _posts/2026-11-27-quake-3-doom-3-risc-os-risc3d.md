---
layout: post
title: "Quake III Arena and Doom 3 Ported to RISC OS with GPU Acceleration via RISC3D"
date: 2026-11-27 08:00:00 +0000
summary: "David Sharp has ported ioquake3 (Quake III Arena) and dhewm3 (Doom 3) to RISC OS, with GPU drawing through Andrew Youll's RISC3D on a Raspberry Pi 4. Each port can download id Software's free demo, or use data from a copy of the full game."
tags: [software, games, graphics]
source_url: "https://www.riscosopen.org/forum/forums/1/topics/20687"
source_name: "RISC OS Open Forums"
image: /assets/images/quake3-pi4-rocket-fight.jpg
image_alt: "A Quake III Arena bot match on a Raspberry Pi 4, drawn by the GPU through RISC3D"
---

David Sharp announced on 27 November 2026, in the RISC OS Open Announcements topic [Quake 3 and Doom 3 on RISC OS with GPU acceleration via RISC3D](https://www.riscosopen.org/forum/forums/1/topics/20687), that he has ported two of id Software's engines to RISC OS: [ioquake3](https://davidsharp.com/riscos/quake3/) (Quake III Arena, id Tech 3, 1999) and [dhewm3](https://davidsharp.com/riscos/doom3/) (Doom 3, id Tech 4, 2004). He states that the ports were made with the help of Claude AI.

On a Raspberry Pi 4 with Andrew Youll's [RISC3D]({{ '/2026/11/17/risc3d-0-10-gpu-opengl-classicube/' | relative_url }}), both games are drawn by the GPU, in a window on the desktop or full screen. Neither package includes game data. Each one can download id Software's free demo, or use data from a copy of the full game that you already own.

## Quake III Arena

The [Quake III Arena home page](https://davidsharp.com/riscos/quake3/) lists version 0.2.1 as an 8.8 MB zip. It has the game's own menus, single player against bots, and LAN and internet play. Alt+Enter switches between full screen and a window.

On a Pi 4 with RISC3D, Sharp reports about 70 frames a second in a 1024×768 window and about 45 full screen at 1680×1050. Without RISC3D it also runs on a Pi 2, 3 or 4, drawn in software at a lower resolution and scaled up to fill the screen.

It needs RISC OS 5 (tested on 5.30), SharedUnixLibrary 1.16 or later, and ARMEABISupport 1.03 or later. GPU drawing needs RISC3D 0.22 or later on a Pi 4. Sound is through SharedSoundBuffer or DigitalRenderer. Source is in the [riscos-quake3](https://github.com/davidpsharp/riscos-quake3) GitHub repository.

[![A bot firing rockets down a corridor in q3dm7, from a Quake III Arena bot match on a Raspberry Pi 4]({{ '/assets/images/quake3-pi4-rocket-fight.jpg' | relative_url }}){: width="640" height="480" loading="lazy"}]({{ '/assets/images/quake3-pi4-rocket-fight.jpg' | relative_url }})

*A bot match on a Raspberry Pi 4, drawn by its GPU through RISC3D. Image: [davidsharp.com](https://davidsharp.com/riscos/quake3/).*

## Doom 3

The [Doom 3 home page](https://davidsharp.com/riscos/doom3/) lists version 0.2.3 as a 10.6 MB zip. It plays the single-player campaign with sound. This port is for the Pi 4 only, with RISC3D. It runs in an 800×600 window on the desktop, or full screen. From version 0.2.2 it can play the full game as well as the demo.

Sharp reports about 10 to 15 frames a second in Mars City with shadows on, and about half as fast again with them off (the default). A tick in the icon bar menu turns shadows on, including mid-game.

The full game needs a Pi 4 with 2 GB or more, and the original DOOM 3 data from Steam or GOG — not the BFG Edition, whose data the engine cannot read. It has been tested on RISC OS 5.30 on a 4 GB Pi 4, and also needs RISC3D 0.22 or later, SharedUnixLibrary 1.16 or later, and ARMEABISupport 1.03 or later. Source is in the [riscos-dhewm3](https://github.com/davidpsharp/riscos-dhewm3) GitHub repository.

[![The Mars City hangar in Doom 3 in an 800×600 window on a Raspberry Pi 4]({{ '/assets/images/doom3-pi4-hangar.png' | relative_url }}){: width="640" height="400" loading="lazy"}]({{ '/assets/images/doom3-pi4-hangar.png' | relative_url }})

*The Mars City hangar on a Raspberry Pi 4, drawn by its GPU through RISC3D. Image: [davidsharp.com](https://davidsharp.com/riscos/doom3/).*

## Installing

The announcement gives PackMan as the easiest route, which will also offer updates:

1. In PackMan's Choices, under Sources, add `https://davidsharp.com/riscos/pkg`
2. For the GPU, also add Youll's source, which has RISC3D: `https://adyoull.github.io/riscos-packages/pkg/index`
3. Update the lists and install ioquake3 or dhewm3 from the Games section

Plain zip downloads are on each home page.

Sharp thanks id Software for releasing the source, the ioquake3 and dhewm3 developers, Andrew Youll for RISC3D and riscos-mesa, and the GCCSDK team for UnixLib and SDL. Bug reports are welcome on the forum thread, on GitHub, or through [davidsharp.com/contact](https://davidsharp.com/contact/).
