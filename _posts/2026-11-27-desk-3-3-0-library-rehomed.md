---
layout: post
title: "Desk C Library Updated to 3.3.0 and Rehomed"
date: 2026-11-27 17:00:00 +0000
summary: "The Desk C library for RISC OS has been updated to 3.3.0 and moved to Philip Ludlam's GitLab project, with sources and pre-built binaries available under the MIT licence."
tags: [software, development]
source_url: "https://www.riscository.com/2026/desk-updated-rehomed/"
source_name: "RISCOSitory"
---

The Desk library for RISC OS C programs has been updated to version 3.3.0 and published from a new home. [RISCOSitory reported the news](https://www.riscository.com/2026/desk-updated-rehomed/) on 27 November 2026, in VinceH's article [Desk updated and rehomed](https://www.riscository.com/2026/desk-updated-rehomed/). The sources now live in Philip Ludlam's [Desk project on GitLab](https://gitlab.com/philipnet/desk).

Desk dates back to the early 1990s and has had many contributors over the years. RISCOSitory describes it as a library of functions for C programs, covering debugging, the desktop, file and memory management, sprites, internationalisation, graphics and sound, and fonts.

The server that hosted its sources went offline a few years ago. It has since been updated and made available from the GitLab project. Sources and [pre-built binaries](https://gitlab.com/philipnet/desk/-/releases) are covered by the MIT licence and can be downloaded for linking with modules or applications.

## Getting Desk 3.3.0

The GitLab [tags](https://gitlab.com/philipnet/desk/-/tags) list `Desk-3.3.0`, with the associated release titled "Desk 3.3.0 for RISC OS". The previous tag is `Desk-3.2.5`. The [3.3.0 release page](https://gitlab.com/philipnet/desk/-/releases/Desk-3.3.0) includes a pre-built zip, `Desk-Release-3_3_0.zip`, along with source archives.

RISC OS Open's [64-bit Moonshot technical page](https://www.riscosopen.org/content/documents/risc-os-moonshots/64-bit-moonshot-technical) had listed a job "Desk sources are lost", noting that some otherwise C-based components could not be rebuilt for 64-bit platforms without the library, and that this Desk is not the same as DeskLib. Later notes on that page say the maintainer located the sources, an OSS-recognised licence was selected, and the sources were rebuilt using contemporary tools.
