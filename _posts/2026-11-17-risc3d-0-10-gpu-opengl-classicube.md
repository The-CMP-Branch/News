---
layout: post
title: "RISC3D 0.10 Brings GPU-Accelerated OpenGL to RISC OS, with ClassiCube as First Showcase"
date: 2026-11-17 08:10:00 +0000
summary: "Andrew Youll has released RISC3D 0.10, a module that lets OpenGL and OpenGL ES programs use the GPU on RISC OS on Linux and native RISC OS on the Raspberry Pi 4, with ClassiCube 1.3.9 the first game to ship as a RISC OS showcase."
tags: [software, graphics, games]
source_url: "https://www.riscosopen.org/forum/forums/1/topics/20678"
source_name: "RISC OS Open Forums"
image: /assets/images/torcs-pi4-gpu.png
image_alt: "TORCS running on a Raspberry Pi 4 with GPU acceleration through RISC3D"
---

Andrew Youll has released RISC3D 0.10, a first release that lets RISC OS programs drawing with OpenGL or OpenGL ES use the GPU. He announced it on 16 November 2026 in the RISC OS Open Announcements topic [RISC3D: 3D acceleration for RISC OS on Linux and RISC OS on the Pi 4](https://www.riscosopen.org/forum/forums/1/topics/20678). Source is in the [riscos-risc3d](https://github.com/adyoull/riscos-risc3d) GitHub repository; the GitHub tag is v0.10.

The same day he posted a companion first release of [ClassiCube 1.3.9 for RISC OS](https://www.riscosopen.org/forum/forums/1/topics/20679), a Minecraft Classic-compatible game that uses RISC3D when it is installed.

## How RISC3D sits between Mesa and the GPU

RISC3D is a module between [riscos-mesa](https://github.com/adyoull/riscos-mesa)'s `!MesaLibs` and the GPU. Programs keep drawing through Mesa as they do now. Where RISC3D has a driver, Mesa hands the drawing to the GPU; where it has none, Mesa draws in software as before. Programs do not need changing.

It ships as `!RISC3D` in `!Boot.Resources`, with the module and a `GPU` folder of drivers. At start-up it tries each driver until one starts. Each driver refuses machines it is not for, so the same `!RISC3D` can be used on every system.

There are two drivers:

- **Linux3D**, for RISC OS on Linux. OpenGL calls are written as commands in shared memory, with no SWI per call. On the Linux side, **rol-3d** plays them back with Linux's Mesa. The riscos-risc3d package installs Mesa 26.1.6 from Debian's backports for this.
- **V3DRender**, a new native driver for Raspberry Pi 4, 400 and Compute Module 4. There is no command stream here: the program runs Mesa's own v3d driver, the same code Linux uses for this GPU, and V3DRender does the kernel driver's part.

The release covers OpenGL 1.x to 3.1 and OpenGL ES 1.1 to 3.1. On Youll's Pi 4, ClassiCube, Warzone 2100, YSFlight and TORCS draw on the GPU through it.

[![TORCS running on a Raspberry Pi 4 with GPU acceleration through RISC3D]({{ '/assets/images/torcs-pi4-gpu.png' | relative_url }}){: width="864" height="540" loading="lazy"}]({{ '/assets/images/torcs-pi4-gpu.png' | relative_url }})

*TORCS on a Raspberry Pi 4, drawn on the GPU through RISC3D. Image: Andrew Youll / riscos-risc3d.*

## Installing

RISC3D is installed through PackMan from Youll's package source, `https://adyoull.github.io/riscos-packages/pkg/index`. Because the source is on https, PackMan needs **CaCertificates** first. After adding the source and updating lists, RISC3D is in the System section.

RISC OS on Linux images from riscos-harddisc 1.0.0058 onwards already include `!RISC3D`. Native use on a Pi 4 also needs riscos-mesa 20.3.5-20 (or later) so that `!MesaLibs` carries the GPU library.

This is a first release. The SWI chunk (`&C3D00`) and error numbers are provisional. `*Set RISC3D$Disable 1` turns RISC3D off for programs started afterwards, which then draw in software.

RISC3D is under the MIT licence; V3DRender is GPL-2.0-or-later. Youll credits Rob Heaton, whose V3DDriver showed how to power up the Pi 4 GPU from RISC OS, and notes that the code, build scripts and documentation were written with Anthropic's Claude as a coding assistant.

Later posts in the same thread say RISC3D should also work, untested, on RISC OS on Linux on the Pinebook Pro, the Pinebook, and the Windows Dev Kit 2023, because Linux3D hands drawing to whatever GPU Linux already drives.

## ClassiCube 1.3.9 for RISC OS

ClassiCube is a free, open source game compatible with Minecraft Classic, by UnknownShadow200 and the ClassiCube team. Youll's RISC OS port is its first release for RISC OS 5 on ARMv7: Raspberry Pi 2 and later, and other Cortex-A boards.

GitHub carries two tags dated 16 November 2026: [v1.3.9-riscos1](https://github.com/adyoull/riscos-classicube/releases/tag/v1.3.9-riscos1) and [v1.3.9-riscos2](https://github.com/adyoull/riscos-classicube/releases/tag/v1.3.9-riscos2). The second is the same program with riscos-mesa's released `!MesaLibs` 20.3.5-21 (riscos1 had a test build) and PackMan packaging.

The game can be played in single-player or online, signing in to classicube.net through AcornSSL. Mouse look works in a window: the game holds the pointer while you play. With `!RISC3D` in `!Boot.Resources` it is drawn on the GPU; without it, the game draws in software. Youll says the software path is faster than upstream's: caves that cannot be seen are not drawn, and the music is decoded with NEON.

It needs `!MesaLibs` 20.3.5-21 via `!SharedLibs`, SharedUnixLibrary 1.16 or later, and ARMEABISupport. In PackMan it is under Games, from the same package source as RISC3D. The first time it runs, it offers to download textures, sounds and music from classicube.net, about 20 MB.

Youll has tested the release on RISC OS on Linux in software, but not yet on a Pi as a release. In the forum thread, Norman Lawrence reports 56 fps on an Argon One laptop.

[![ClassiCube running on RISC OS]({{ '/assets/images/classicube-riscos-game.png' | relative_url }}){: width="1280" height="800" loading="lazy"}]({{ '/assets/images/classicube-riscos-game.png' | relative_url }})

*ClassiCube on RISC OS. Image: Andrew Youll / riscos-classicube.*

Discussion continues in the [RISC3D](https://www.riscosopen.org/forum/forums/1/topics/20678) and [ClassiCube](https://www.riscosopen.org/forum/forums/1/topics/20679) forum threads.
