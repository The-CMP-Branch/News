---
layout: post
title: "Folio 0.0.1-test76 Gets a User Guide and First Risc PC Build"
date: 2026-11-13 16:40:00 +0000
summary: "Andrew Youll's Folio PDF and ebook reader for the RISC OS desktop now has an illustrated user guide, and a first Risc PC build for StrongARM machines, in test release 0.0.1-test76."
tags: [software, documentation]
source_url: "https://www.riscosopen.org/forum/forums/1/topics/20590?page=3"
source_name: "RISC OS Open Forums"
image: /assets/images/folio-test76-user-guide.png
image_alt: "The Folio User Guide open in a RISC OS web browser, showing the contents for Folio 0.0.1-test76"
---

Andrew Youll has released Folio 0.0.1-test76, a test build of his PDF and ebook reader for the RISC OS desktop. He posted the news on 13 November 2026 in the RISC OS Open Announcements forum topic [Folio: a PDF and ebook reader for the desktop](https://www.riscosopen.org/forum/forums/1/topics/20590?page=3). The build adds a full user guide and a first version for a Risc PC with a StrongARM card.

Folio was first announced in that topic on 11 October 2026. This site has not previously given it a dedicated article; it was mentioned as preinstalled in the [RISC OS on Linux images]({{ '/2026/11/08/risc-os-on-linux-updated-release/' | relative_url }}).

## User guide

The guide is in the same style as Youll's Groove, Lumen and EDT guides: everything Folio does, step by step, with pictures, Tips and Warnings, Try it exercises, a Part of Tens (keys to learn first, things for experienced users, problems and what to do), and every key and menu on one page at the end. Choosing User guide from the menu on Folio's icon bar icon opens it in a web browser. It is also available as a separate download, to read elsewhere or print: [Folio-User-Guide-0.0.1-test76.zip](https://github.com/adyoull/riscos-folio/releases/download/v0.0.1-test76/Folio-User-Guide-0.0.1-test76.zip).

[![The Folio User Guide open in a RISC OS web browser, showing the contents for Folio 0.0.1-test76]({{ '/assets/images/folio-test76-user-guide.png' | relative_url }}){: width="824" height="644" loading="lazy"}]({{ '/assets/images/folio-test76-user-guide.png' | relative_url }})

*The Folio User Guide open in a web browser. Screenshot: Andrew Youll / riscos-folio on GitHub.*

## Bugs found while taking the pictures

Producing the guide's pictures turned up four bugs, now fixed:

- The Annotations window could stop the desktop once its list was complete.
- Clicking a signature Folio had just made said it couldn't find it.
- The date on a signature's appearance came out as "FT11:39:07z".
- The Measure window's paper-size line overlapped the Area row.

## First Risc PC version

There is also a first Risc PC version, for a Risc PC with a StrongARM card: [Folio-RiscPC-0.0.1-test76.zip](https://github.com/adyoull/riscos-folio/releases/download/v0.0.1-test76/Folio-RiscPC-0.0.1-test76.zip). It is the same Folio, built to run without floating-point hardware, but without the plugins — no reading aloud or text recognition, which rely heavily on NEON. It needs a 32 thousand colour mode (1024x768 fits in 2 MB of VRAM), and SharedUnixLibrary comes inside `!Folio`.

[![Folio's Risc PC build running under RPCEmu, with an ebook open]({{ '/assets/images/folio-test76-riscpc.png' | relative_url }}){: width="1024" height="768" loading="lazy"}]({{ '/assets/images/folio-test76-riscpc.png' | relative_url }})

*The Risc PC build of Folio running under RPCEmu, with an ebook open. Screenshot: Andrew Youll / riscos-folio on GitHub.*

Youll has tested it under RPCEmu with RISC OS 5.30, where PDFs, ebooks and a 47 MB magazine all open and draw correctly, but not yet on a real machine. He would like to know how fast it is on a StrongARM Risc PC: a page of text should take about a second. It will not run on an ARM610 or ARM710.

Earlier in the thread, Colin Ferris asked whether Folio could work on older Risc PC emulators. Youll replied that he could look at making the core app work, though the plugins would not, as they use NEON.

## Availability

The main build is [Folio-0.0.1-test76.zip](https://github.com/adyoull/riscos-folio/releases/download/v0.0.1-test76/Folio-0.0.1-test76.zip). Through PackMan, Folio updates from the usual source (`https://adyoull.github.io/riscos-packages/pkg/index`) once the package is updated. The Risc PC version is a direct download only for now.

This is a test build. Source and the [release page](https://github.com/adyoull/riscos-folio/releases/tag/v0.0.1-test76) are on the [riscos-folio](https://github.com/adyoull/riscos-folio) GitHub repository. Youll notes that the code, build scripts and documentation were written with Anthropic's Claude as a coding assistant.

Discussion continues in the [forum thread](https://www.riscosopen.org/forum/forums/1/topics/20590?page=3).
