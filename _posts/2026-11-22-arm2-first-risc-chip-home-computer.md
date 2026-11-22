---
layout: post
title: "All About Circuits on the ARM2, the First RISC Chip Cheap Enough for a Home Computer"
date: 2026-11-22 16:50:00 +0000
summary: "Luke James's All About Circuits article traces the ARM2 from Wilson and Furber's Acorn design to the Archimedes A305, the VLSI chipset, and the founding of Advanced RISC Machines."
tags: [history, arm, hardware]
source_url: "https://www.allaboutcircuits.com/news/the-arm2-the-first-risc-chip-cheap-enough-for-a-home-computer/"
source_name: "All About Circuits"
---

[All About Circuits](https://www.allaboutcircuits.com/news/the-arm2-the-first-risc-chip-cheap-enough-for-a-home-computer/) has published a history of the ARM2 by Luke James, dated 20 November 2026, under the title *The ARM2: The First RISC Chip Cheap Enough for a Home Computer*. The article says Acorn Computers launched the Archimedes in June 1987, with the entry-level A305 at £799, built around Acorn's own 32-bit RISC processor.

## The chip in the Archimedes

According to the article, the ARM2 inside ran at 8 MHz, had roughly 30,000 transistors, and delivered 4,901 Dhrystones per second in *Byte*'s October 1987 preview — 31% ahead of a 16 MHz Compaq Deskpro 386. The article says Sophie Wilson and Steve Furber designed it as a replacement for the 6502 in Acorn's BBC Micro, after the company evaluated and rejected leading 16-bit CPUs: the Motorola 68000, National Semiconductor 32016 and Intel 80286. Neither designer had built a microprocessor before, it says. *Byte*'s Dick Pountain, quoted in the piece, called the Archimedes "the first RISC machine inexpensive enough for home use".

## From Phoenix to first silicon

The article describes an October 1983 visit by Wilson and Furber to the Western Design Center in Phoenix, Arizona. It says Wilson wrote the instruction set and Furber the three-stage microarchitecture, and that the whole reference model and development environment ran in about 850 lines of BBC BASIC on a BBC Micro.

ARM1 first silicon, the article says, arrived from VLSI Technology on 26 April 1985, fabricated on a 3 µm process. The ARM2 followed as VLSI part VL86C010 on a 2 µm process. Over ARM1 it added multiply and multiply-accumulate (MLA) instructions and a coprocessor interface.

## Chipset and power

James describes Acorn's four-chip set as the ARM2 plus the MEMC memory controller, VIDC video controller and IOC I/O controller, all fabricated by VLSI. The ARM2 had no cache; the article says the ARM3 added one in 1989. On power, it cites VLSI's data book at about 0.1 W (20 mA typical at 10 MHz), with Furber's team coming in under a tenth of a watt.

## After Acorn

Advanced RISC Machines Ltd. was founded in November 1990 by Acorn, Apple and VLSI Technology, the article says, after Apple looked for a processor for its Newton handheld. James writes that Wilson and Furber shared the 2022 Draper Prize with John Hennessy and David Patterson.

Steve Furber discussed the BBC Micro and the ARM design in a [Peterman Pod interview]({{ '/2026/11/17/steve-furber-peterman-pod-bbc-micro-arm/' | relative_url }}) covered earlier on this site. The All About Circuits article is [The ARM2: The First RISC Chip Cheap Enough for a Home Computer](https://www.allaboutcircuits.com/news/the-arm2-the-first-risc-chip-cheap-enough-for-a-home-computer/).
