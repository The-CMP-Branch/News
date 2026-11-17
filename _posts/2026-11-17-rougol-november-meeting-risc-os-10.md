---
layout: post
title: "ROUGOL November Meeting Reports a First Deep Dive into 64-bit RISC OS 10"
date: 2026-11-17 08:05:00 +0000
summary: "Mark Stephens reports from the RISC OS User Group of London's 16 November meeting, where Andrew Rawnsley and Richard Brown of RISC OS Developments gave a first deep dive into 64-bit RISC OS 10."
tags: [community, events, user-groups, risc-os-64]
source_url: "https://www.iconbar.com/articles/ROUGOL_November_2026_meeting_-_RISC_OS_10/index2426.html"
source_name: "The Icon Bar"
---

The RISC OS User Group of London's 16 November 2026 meeting was a first deep dive into 64-bit RISC OS 10. Mark Stephens reports the evening in [The Icon Bar](https://www.iconbar.com/articles/ROUGOL_November_2026_meeting_-_RISC_OS_10/index2426.html), posted on 17 November 2026. Forty-two people attended.

This site [previewed the meeting on 11 November]({{ '/2026/11/11/rougol-november-risc-os-10-deep-dive/' | relative_url }}), when ROUGOL had confirmed Andrew Rawnsley of RISC OS Developments (ROD) as the speaker after the 64-bit system's London Show reveal.

## RISC OS 10

The speakers were Andrew Rawnsley and Richard Brown of RISC OS Developments. Stephens describes RISC OS 10 as a 64-bit RISC OS rewritten in C, compiled with GCC, and building on the framework laid out by Gerph. It has been about six to nine months of work so far, and is open to anyone who wants to get involved. Development has been iterative with AI tools — Codex, Claude and Gemini — mixed with conventional coding; Rawnsley spent some time explaining that you cannot simply ask AI to do it all.

## What was shown

The evening was an interactive demonstration. It started with HForm, which can format drives and uses UFS2 as its recommended format. Stephens says this was much slicker than the version shown at the London Show, with a Make Boot option and a range of recovery options. They are looking to backport some of this to 32-bit RISC OS.

The Task Manager has more detail than before and showed other cores in use (thumbnailing was demonstrated), with pthreads. Hardware OpenGL was shown with a fishtank and Quake 3. The desktop now uses SVG files, and themes have gained a dark mode. PinBoard is based on ROD's enhanced PinBoard 2, and the TCP/IP stack is also ROD's version.

Streaming video and YouTube were shown, as were LanMan98 access to WebDAV and pCloud, Bluetooth, and support for OTF fonts. Several applications ran, including Ovation Pro. An old version of TechWriter ran with no issues, and a 26-bit Impression ran as well. A 32-bit ImpressionX caused the only crash of the evening.

Stephens notes that there were plenty of questions afterwards. Meeting details remain on the [ROUGOL website](https://www.rougol.jellybaby.net).
