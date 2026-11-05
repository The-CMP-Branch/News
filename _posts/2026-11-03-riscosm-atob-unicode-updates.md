---
layout: post
title: "RiscOSM and AtoB Receive Unicode Improvements"
date: 2026-11-03 15:00:00 +0000
summary: "Sine Nomine Software's mapping and route-planning applications gain enhanced Unicode character handling alongside bug fixes and updated OpenStreetMap data."
tags: [software, mapping]
source_url: "https://www.riscosopen.org/forum/forums/1/topics/20644"
source_name: "RISC OS Open Forums"
---

Matthew Phillips has announced updates to Sine Nomine Software's mapping applications, with RiscOSM reaching version 2.35 and AtoB updated to version 1.05. Both releases focus on improved Unicode character handling, while RiscOSM addresses several bugs and adds new features.

RiscOSM has progressed through three releases over the past two months, accumulating fixes for obscure bugs alongside user-visible enhancements. Version 2.35 corrects Unicode text display in the Features window and resolves a memory leak that could affect long-running sessions.

## Map Pin Enhancements

A new circular map pin style displays pins with areas proportional to numerical values. This feature proves particularly useful when displaying multiple data-driven pins simultaneously, with the pin's value serving as its default label. The style editor provides immediate visual feedback, previewing edited styles at the current zoom level before updating the map.

The update fixes a "zero page" error that occurred when double-clicking on previously hidden pins in the Pins & Tracks window or when unhiding them. A separate redraw bug affecting certain RISC OS versions when opening folders or plotting pins has also been corrected.

## Service Integration Update

RiscOSM's bus stop "next departures" lookup now queries traveline.info using ATCO codes rather than the previous nextbuses.mobi service with NAPTAN codes. The change reflects the latter site's redirection to the former, ensuring the feature continues functioning correctly.

## AtoB Route Planning

AtoB version 1.05's primary update brings enhanced Unicode character handling, matching the improvements made to RiscOSM. The route-planning application can be used standalone or integrated with RiscOSM for combined mapping and navigation.

## Map Data Refresh

All map data has been reconverted using October 2026 downloads from OpenStreetMap, ensuring users have access to the latest road layouts, place names, and geographic features. Updated map data is available for download from the Sine Nomine Software website alongside the application updates.

RiscOSM 2.35 is a free upgrade for users of version 2.30 or later, with a patch download available on the [downloads page](https://sinenomine.co.uk/software/riscosm/downloads.php). Users of earlier versions may purchase upgrades through the Sine Nomine website. AtoB 1.05 is a free update for all registered users. Complete version history and detailed change notes are available on the [RiscOSM version history page](https://www.sinenomine.co.uk/software/riscosm/history.html).
