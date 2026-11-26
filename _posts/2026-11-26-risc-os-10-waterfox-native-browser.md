---
layout: post
title: "RISC OS 10 Gains Native Waterfox Browser"
date: 2026-11-26 17:00:00 +0000
summary: "Martin Eastwood reports that the RISC OS 10 64-bit alpha now has Waterfox as a native web browser, with RISC OS Technologies also showing a LibreOffice development build on Raspberry Pi 5 and CM5."
tags: [software, raspberry-pi, risc-os-10, risc-os-64]
source_url: "https://www.riscosopen.org/forum/forums/13/topics/20621"
source_name: "RISC OS Open Forums"
image: /assets/images/riscos10-waterfox.png
image_alt: "Waterfox running as a native browser on the RISC OS 10 desktop"
---

Martin Eastwood posted on 26 November 2026 in the RISC OS Open 64-bit forum topic [RISC OS 64](https://www.riscosopen.org/forum/forums/13/topics/20621) that RISC OS 10 now has Waterfox as a native browser, along with other new applications. He thanked the community testers who have joined the alpha to help develop it.

RISC OS Technologies presents RISC OS 10 on its [home page](https://www.riscostechnologies.co.uk/) as a native 64-bit RISC OS for Raspberry Pi 5 and Compute Module 5. This site's earlier coverage was a [ROUGOL November meeting report]({{ '/2026/11/17/rougol-november-meeting-risc-os-10/' | relative_url }}) on RISC OS Developments' first deep dive into the system.

## Waterfox and LibreOffice

RISC OS Technologies now has a "Waterfox on RISC OS 10" section showing the browser running on the RISC OS 10 desktop. A neighbouring "LibreOffice on RISC OS 10" section shows a development build; LibreOffice is being brought to the system rather than presented as a finished port.

[![Waterfox running as a native browser on the RISC OS 10 desktop]({{ '/assets/images/riscos10-waterfox.png' | relative_url }}){: width="2560" height="1440" loading="lazy"}]({{ '/assets/images/riscos10-waterfox.png' | relative_url }})

*Waterfox running on the RISC OS 10 desktop. Image: RISC OS Technologies.*

## Still an alpha

The system remains an alpha, with community testers helping to develop it. Alongside the browser and office work, RISC OS Technologies lists 32-bit applications running in EL0 user space, selected 26-bit applications through JIT translation, preemptive multitasking still in development, four-core support, V3D and Mesa64 graphics, UFS2 storage, the Shield desktop theme, 64-bit ports of PipeDream, Fireworkz and Ovation Pro, and developer tools including GCC 16 and LLVM 22.
