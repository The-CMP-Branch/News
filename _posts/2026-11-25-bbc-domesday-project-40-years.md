---
layout: post
title: "Forty Years On: The BBC Domesday Project, Published 25 November 1986"
date: 2026-11-25 08:00:00 +0000
summary: "Today is 40 years since the BBC Domesday Project was published: a 1986 laserdisc survey of Britain on Acorn BBC Master AIV hardware, later a textbook case of digital obsolescence."
tags: [history, hardware]
source_url: "https://en.wikipedia.org/wiki/BBC_Domesday_Project"
source_name: "Wikipedia"
image: /assets/images/bbc-domesday-system.jpg
image_alt: "A BBC Domesday system: Acorn BBC Master AIV, Philips VP415 LaserDisc player and Marconi RB2 trackerball"
---

Today, 25 November 2026, is 40 years since the BBC Domesday Project was published. [BeebMaster](http://www.beebmaster.co.uk/Domesday/DDiscs.html) records that the National and Community discs were published by the BBC on 25 November 1986, as the first Advanced Interactive Video laserdiscs for the BBC Master AIV system.

The *Radio Times* for 22–28 November 1986 described the discs as "out this week" and said they would make their public debut on *Tomorrow's World* on Thursday at 8pm on BBC1 — 27 November 1986.

## A survey for the 900th anniversary of the Domesday Book

The project was a partnership between Acorn Computers, Philips, Logica and the BBC, with some funding from the European Commission's ESPRIT programme, to mark the 900th anniversary of the original Domesday Book of 1086. Wikipedia, drawing on contemporary reporting, says it was compiled between 1984 and 1986 and that over a million people took part, including children from more than 9,000 schools. The Centre for Computing History gives the same "over 1 million people" figure and a higher school count of 14,000; this article uses Wikipedia's more conservative school figure.

Contributors, mostly schoolchildren, wrote about geography, history or social issues in their local area, or about daily life. That material was linked with maps, colour photographs, statistical data, video and "virtual walks", together with professionally prepared footage, tours of landmarks, and datasets such as the 1981 census.

The results were stored on two 12-inch LaserVision Read Only Memory (LV-ROM) discs, which held analogue video and still pictures as well as digital data:

- The **Community Disc** is map-based and shows Britain as seen by the people who lived there. The country was divided into 4 km × 3 km blocks based on Ordnance Survey grid references. It is double-sided, with a Southern and a Northern side.
- The **National Disc** is topic-based, with census data, professional photographs and walkarounds. Side 2 held video material.

[Chris's Acorns](https://chrisacorns.computinghistory.org.uk/Computers/Domesday.html) notes that each disc contains 108,000 pictures and 648 megabytes of data.

[![A BBC Domesday system: Acorn BBC Master AIV, Philips VP415 LaserDisc player and Marconi RB2 trackerball]({{ '/assets/images/bbc-domesday-system.jpg' | relative_url }}){: width="1280" height="853" loading="lazy"}]({{ '/assets/images/bbc-domesday-system.jpg' | relative_url }})

*A BBC Domesday system: Acorn BBC Master AIV, Philips VP415 LaserDisc player and Marconi RB2 trackerball. Photo: [simon.inns](https://commons.wikimedia.org/wiki/File:BBC_Master_AIV_(Domesday_System)_(1).jpg) / Wikimedia Commons, [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/).*

## The Acorn hardware

Viewing the discs needed a BBC Master AIV: an Acorn BBC Master expanded with a SCSI controller and the 65C102 "Turbo" co-processor, controlling a Philips VP415 LaserVision player. Chris's Acorns describes the SCSI bus as the data link to the player, which appeared to the Master as a large, slow read-only SCSI disc. The Video Filing System (VFS) ROM was a read-only version of ADFS with extra commands for the VP415. The pointer was an Acorn trackerball — a rebadged Marconi RB2 — on the Master's User Port.

The application software was written in BCPL, mainly by Logica.

## Cost, and why few were bought

Chris's Acorns and the Centre for Computing History both give the launch price of the complete BBC AIV system as £5,156.75 including VAT. Acorn's September 1987 retail price list lists AVC11, the BBC AIV System, at that figure: the Domesday disc set, BBC Master AIV with trackerball, BBC AIV LaserVision player, and a colour monitor.

Andy Finney, who worked on the project, later wrote that the package was around £5,000 — "the cost of a small family car" — and "a little expensive for many schools". Wikipedia, citing *Acorn User* in May 1988, says that by early 1988 fewer than 2,000 Domesday systems had been sold, with a voucher scheme reducing the price to £3,000.

## Digital obsolescence, and later rescue

By 2002 the project was widely cited as an example of digital obsolescence: the original Domesday Book could still be read after nine centuries, while the 1986 discs already needed rare hardware. The still images had been stored as single-frame analogue video, overlaid by the computer's graphics, years before JPEG and truecolour video cards were common.

In 2002 the CAMiLEON project (Creative Archiving at Michigan and Leeds: Emulating the Old on the New), a partnership between the University of Leeds and the University of Michigan, developed emulation that could access the discs. BBC News reported that work on 2 December 2002. CAMiLEON transferred the digital files over SCSI and digitised the still-frame video, then used a modified BeebEm emulator with Turbo, SCSI and laserdisc support.

In May 2011 BBC Learning republished much of the Community Disc on the Domesday Reloaded website. That site went offline in June 2018; a snapshot is held by The National Archives.

The [Domesday86](https://www.domesday86.com/) project has since worked on preserving both the laserdiscs and the hardware needed to use them, with the aim of running the system without the original rare player. The Centre for Computing History in Cambridge keeps a working Domesday system on public display, as does The National Museum of Computing at Bletchley Park.

## On show in the RISC OS community

RISC OS Open's news post [Laser focused on London](https://www.riscosopen.org/news/articles/2026/10/15/laser-focused-on-london) (15 October 2026) noted that it had also been forty years since the launch of the Domesday laserdisc system, and that a still-working system would be available at the London Show on 24 October 2026. Bryan Hogan wrote on the show's forum topic that visitors could look up their hometown as it was around 1986.

## Sources

- [BeebMaster, The Domesday Discs](http://www.beebmaster.co.uk/Domesday/DDiscs.html)
- [Wikipedia, BBC Domesday Project](https://en.wikipedia.org/wiki/BBC_Domesday_Project)
- [Chris's Acorns, BBC Master AIV & Domesday Project](https://chrisacorns.computinghistory.org.uk/Computers/Domesday.html)
- [Centre for Computing History, Domesday System – BBC Domesday Discs](https://www.computinghistory.org.uk/det/55515/Domesday%20System%20-%20BBC%20Domesday%20Discs/)
- [Andy Finney, The BBC Domesday Project](https://www.atsf.co.uk/dottext/domesday.html)
- [*Radio Times*, 22–28 November 1986](https://www.domesday86.com/wp-content/uploads/2018/02/Radio-Times-Domesday-Nov-1986.pdf) (scan hosted by Domesday86)
- [BBC News, Digital Domesday book unlocked, 2 December 2002](http://news.bbc.co.uk/2/hi/technology/2534391.stm)
- [RISC OS Open, Laser focused on London, 15 October 2026](https://www.riscosopen.org/news/articles/2026/10/15/laser-focused-on-london)
- [Domesday86](https://www.domesday86.com/)
