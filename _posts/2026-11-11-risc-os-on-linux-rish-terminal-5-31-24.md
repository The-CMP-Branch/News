---
layout: post
title: "RISC OS on Linux Adds RiSH Terminal, Interactive Commands and RISC OS 5.31-24"
date: 2026-11-11 16:40:00 +0000
summary: "Andrew Youll has followed the RISC OS on Linux updated release with RiSH, a Linux terminal for the desktop, interactive Linux commands, and a RISC OS 5.31-24 ROM, all arriving through Configure's Updates."
tags: [software, emulation, linux, raspberry-pi]
source_url: "https://www.riscosopen.org/forum/forums/1/topics/20657?page=2"
source_name: "RISC OS Open Forums"
image: /assets/images/risc-os-on-linux-rish-terminals.png
image_alt: "Two RiSH terminal windows on the RISC OS on Linux desktop"
---

Andrew Youll has posted a substantial follow-up to [the RISC OS on Linux updated release this site covered on 8 November]({{ '/2026/11/08/risc-os-on-linux-updated-release/' | relative_url }}). The new features, announced on 11 November 2026 in the [RISC OS Open forums](https://www.riscosopen.org/forum/forums/1/topics/20657?page=2), arrive through Configure → Updates, so a new image does not need to be written to a card. Youll asks users to restart after installing.

## RiSH, the RISC Shell

RiSH is a Linux terminal for the RISC OS desktop, placed in Apps. Each window is a Linux shell and can run full-screen Linux programs — editors, `top`, and anything written for an xterm — in 256 colours with line drawing. Resize the window and the program inside is told. A scroll bar keeps the last 1000 lines. A Large text option doubles the text for 4K screens.

[![Two RiSH terminal windows on the RISC OS on Linux desktop]({{ '/assets/images/risc-os-on-linux-rish-terminals.png' | relative_url }}){: width="1280" height="800" loading="lazy"}]({{ '/assets/images/risc-os-on-linux-rish-terminals.png' | relative_url }})

*RiSH running Linux terminals on the RISC OS desktop. Screenshot: Andrew Youll / RISCOSonLinux on GitHub.*

A root terminal is available from the icon bar menu (or Adjust on the icon). It asks for the root password, and is marked so it cannot be mistaken for an ordinary shell: a red title bar, a red cursor, and a warning in bold.

Copy and paste works with other RISC OS applications in both directions. Drag to select, then use Copy and Paste on the menu, or Ctrl-Shift-C and Ctrl-Shift-V. Youll notes that the mouse is not yet supported inside programs.

## Interactive Linux commands

`*IXRun`, `*LinuxUser` and `*Linux` are now interactive: they pass what you type to the Linux program, so prompts such as apt-get's `[Y/n]` and `passwd` can be answered. With no command they start a shell — `*IXRun` as RISC OS's own Linux user (no password, no privileges), `*Linux` as root after the root password. Escape is treated as Ctrl-C; Escape twice in quick succession stops the command outright. The commands remain line-by-line; for full-screen programs, Youll points users to RiSH.

## RISC OS 5.31-24 ROM

The `riscos-rom` 5.31-24 update changes how dynamic areas are placed. New areas are now allocated from the lowest free address upwards, as on native RISC OS. Previously Linux chose the addresses from the top down, so a program that ran a byte past the end of an area could quietly read or write its neighbour — behaviour that would stop with a data abort on a real machine. Youll reports a test run line-for-line against native RISC OS 5.31 on the same Raspberry Pi 4, with matching results. Areas also no longer sit at addresses with the top bit set.

The RAM disc can now be as large as 2 GB, up from 128 MB, matching native RISC OS 5.3×. Youll credits Chris Gransden for the report.

A pointer that has been turned off now disappears properly. A program that hides the pointer — Youll's example is !RDPClient over its window — no longer leaves the last one frozen on screen.

## NativeSupport 0.45

`riscos-support` 1.0.0041-1 includes NativeSupport 0.45. The busiest SWI calls in the ROM now go straight to RISC OS's SWI handler without trapping out to Linux and back. `*NativeSupport SWIStubs Off` turns that path off for comparison; it needs the 5.31-24 ROM as well. Youll also reports fewer traps on a Pi 4 from instructions that never actually run.

Modules and programs saved from memory are written as they were, without NativeSupport's patch markers in the file. A Filer_Action abort when copying from LanMan98 is fixed. HDMI sound is chosen only when the screen reports that it supports audio; otherwise the headphone socket is used.

## PackMan and Iris

`riscos-harddisc` 1.0.0040-1 no longer hits a file-conflict error when Iris is installed with PackMan. The images shipped their own `!CaCertificates` in `!Boot.Resources`, which PackMan did not know about. The update replaces it with PackMan's CaCertificates 1.00-6 and records it, so PackMan owns it from then on. Youll thanks Ralph Barrett for the report.

## Raspberry Pi hardware

The headphone socket on a Pi 3 or 4 had no Linux headphone device, because `dtparam=audio=on` in `config.txt` was in the wrong place: it has to come before the overlays. The update moves the line and keeps the old file as `config.txt.old`. Youll thanks Ralph Barrett for the report and the log.

The official Raspberry Pi 5 Active Cooler fan never started, because Linux's fan driver was missing from the Pi kernel. It is now included in `riscos-kernel-pi` 6.6.78-7.

## Source and testing

The public source is up to date with these changes, including RISC OS 5.31-24, in the [riscos-linux](https://github.com/adyoull/riscos-linux) repository. Images and further RiSH notes remain on [RISCOSonLinux](https://github.com/adyoull/RISCOSonLinux).

Youll notes that RiSH and the interactive commands were tested under QEMU, not yet on a Pi or a 4K screen; he has no Pi 5, so the fan is untested; and the headphone fix is not yet confirmed on a Pi. He invites testers to report how it goes, including the LOGS folder from the boot partition if something goes wrong.

Discussion continues in the [forum thread](https://www.riscosopen.org/forum/forums/1/topics/20657?page=2).
