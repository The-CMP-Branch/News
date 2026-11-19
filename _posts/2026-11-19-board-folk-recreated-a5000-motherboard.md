---
layout: post
title: "The Board Folk's Re-created Acorn A5000 Motherboard Has Been Built and Tested"
date: 2026-11-19 07:50:00 +0000
summary: "Ian Jeffray has built and tested a fully re-created Acorn A5000 motherboard from The Board Folk, a faithful issue 1 (PALs) board with small tweaks. There is no plan, schedule or availability yet."
tags: [hardware, retro]
source_url: "https://stardot.org.uk/forums/viewtopic.php?t=33952"
source_name: "StarDot"
---

The Board Folk have produced a fully re-created Acorn A5000 motherboard, and Ian Jeffray (IanJeffray) is the first to build and test one. He posted about it on 17 November 2026 in the StarDot thread [Re-created A5000 - The Board Folk have done it again!](https://stardot.org.uk/forums/viewtopic.php?t=33952).

He first showed the board at ABUG Scotland in September, and showed it again at ABUG South on the weekend before that post.

## A faithful issue 1 re-creation

Jeffray describes it as a very faithful re-creation of an issue 1 (PALs) board, with a few small tweaks, such as a link allowing unfiltered, line-level-only audio. Along the way the team found that the bill of materials in the Technical Reference Manual does not match the schematic: the schematics are essentially for the issue 1 (IOEB) version, while the BOM is for the issue 1.

He populated the 8051, which was never fitted on original A5000 boards. That lets the A5000 use a PS/2 keyboard, as the A4 does.

In a reply, he said both board revisions are essentially functionally identical. The main difference is that the cluster of PALs in the centre of the board became a single IOEB ASIC in the later revision. An A5000 Alpha is just a -35FC ARM3 on the board, and the next board he is building has that. He hopes The Board Folk will also do the IOEB version.

## Not available yet

There is no plan, schedule or availability for the boards yet. Jeffray writes that there are tweaks to make to correct some small errors from the first spin. He has a few prototype boards to build up, and will create a build guide as he builds further boards.

Forum members welcomed the work. Some noted that a replacement motherboard could help when an original A5000 is lost to battery damage.

The Board Folk's earlier Acorn work includes a reproduction [Acorn A3010](https://github.com/Board-Folk/Acorn_A3010) board.
