---
layout: post
title: "Thirty-Five Years On: The Acorn A5000, First Machine to Ship with RISC OS 3"
date: 2026-11-09 07:50:00 +0000
summary: "The Acorn A5000 arrived in 1991 as the first computer to ship with RISC OS 3, and it is reaching its 35th anniversary this year."
tags: [history, hardware]
source_url: "https://chrisacorns.computinghistory.org.uk/Computers/A5000.html"
source_name: "Chris's Acorns"
image: /assets/images/acorn-a5000.jpg
image_alt: "An Acorn A5000 pizza-box computer with keyboard and mouse, running RISC OS on a CRT monitor"
---

The Acorn A5000 arrived in 1991 as the first machine to ship with RISC OS 3, and it is reaching its 35th anniversary this year.

The machine is documented on [Chris's Acorns](https://chrisacorns.computinghistory.org.uk/Computers/A5000.html), which also hosts Acorn's press release [Acorn Unveils its Newest Computer – Welcome to the A5000!!](https://chrisacorns.computinghistory.org.uk/docs/Acorn/PR/Welcome_to_the_A5000.txt). Further accounts appear on Wikipedia's [Acorn Archimedes](https://en.wikipedia.org/wiki/Acorn_Archimedes) page and in [McMordie's Technical history of Acorn](https://www.mcmordie.co.uk/acornhistory/) and its [A5000 article](https://www.mcmordie.co.uk/acornhistory/a5khist.shtml).

[![An Acorn A5000 pizza-box computer with keyboard and mouse, running RISC OS on a CRT monitor]({{ '/assets/images/acorn-a5000.jpg' | relative_url }}){: width="960" height="1280" loading="lazy"}]({{ '/assets/images/acorn-a5000.jpg' | relative_url }})

*An Acorn A5000 with keyboard and mouse, running RISC OS. Photo: [Blake Patterson](https://commons.wikimedia.org/wiki/File:My_Acorn_Archimedes_A5000_(2379176314).jpg) / Wikimedia Commons, [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/).*

## A desktop ARM3 machine with RISC OS 3.00

The A5000 used an ARM3 processor, initially clocked at 25 MHz — slower than the 33 MHz ARM3 in the earlier A540. Acorn's announcement described two launch models: a 1 MB base machine, and a 2 MB model with a 40 MB IDE hard disc and a 14-inch Acorn multiscan monitor. The press release priced them at £999 and £1,499 excluding VAT respectively.

The A5000 used a redesigned desktop case in a style similar to the PCs of the day. Other changes from the A400 range included a 15-pin VGA monitor connector, a PC-style serial port, a bi-directional parallel port, an on-board IDE controller in place of ST506, and a high-density floppy drive. That drive handled Acorn's 1.6 MB "F" format as well as 1.44 MB DOS discs.

Chris's Acorns notes that the first A5000s (codes ALB10, ALB12 and ALB14) shipped with RISC OS 3.00. The OS ROMs grew from 512 KB on RISC OS 2 to 2 MB. Applications such as Draw, Edit and Paint, together with commonly used fonts, moved into ROM. McMordie highlights the multitasking filer: disc operations no longer froze the rest of the desktop. RISC OS 3.00 had a serious bug in ADFSBuffers that could corrupt discs; Acorn later shipped 3.10 and 3.11 as the usual RISC OS 3 versions.

## The 1993 alpha variant

In September 1993 Acorn released an improved A5000, sometimes called the alpha version, with a 33 MHz ARM3 and a motherboard that made it practical to expand memory beyond 4 MB. Chris's Acorns and McMordie's timeline both give that date. Wikipedia records later A5000s with the faster ARM3 and larger hard discs. At launch the A5000 sat below the A540 in Acorn's range; McMordie describes it as fitting above the A440/1, which it effectively superseded.
