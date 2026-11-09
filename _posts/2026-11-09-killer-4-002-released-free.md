---
layout: post
title: "Killer 4.002 Released Free for the RISC OS Community"
date: 2026-11-09 07:40:00 +0000
summary: "Phil Pemberton has released Killer 4.002 free of charge for the community, the version of Pineapple Software's virus killer that he worked on before handing it back."
tags: [software, security]
source_url: "https://www.riscosopen.org/forum/forums/1/topics/20662"
source_name: "RISC OS Open Forums"
---

Phil Pemberton has released Killer 4.002 free of charge for the RISC OS community. He announced it on 9 November 2026 in the [RISC OS Open Announcements forum](https://www.riscosopen.org/forum/forums/1/topics/20662), describing it as the version he worked on before handing the software back. He says the intention agreed with the IP owners was always to release it free of charge for the community.

Killer is Pineapple Software's virus killer, maintained for many years by Alan Glover. An [earlier discussion on the RISC OS Open forums](https://www.riscosopen.org/forum/forums/2/topics/20114) noted that Killer and VProtect originated with Glover and Pineapple, and that their sources had been placed in RISC OS Developments' git, where they are not publicly visible.

On [StarDot](https://stardot.org.uk/forums/viewtopic.php?t=33887), Pemberton posted the download as a development beta with 32-bit fixes. He writes that it should run on RISC OS 3.11 through RISC OS 6, that RISC OS 5 support is untested, and that on RISC OS 4 it passed the test suite Glover had made for it. The changes he lists are removing the copy protection and finishing the 32-bit work Glover started. He notes that disinfection has not been tested much.

Pemberton warns that this version may not work on Raspberry Pi, because Killer's self-verification periodically checks whether its code has been modified and also checks zero page. He says it might work with some way of emulating zero page, and asks testers to report back. It can be installed on a read-only network share and run from any machine on the network.

For Pi users who cannot get this release running, he says Rob Kendrick (Rjek) is working on Slayer as an alternative, with Pemberton helping to test.

Pemberton writes that he disagreed with a decision by others to rework the software using AI and wanted the community to have a choice of versions. He thanks Alan Glover for many years of maintaining Killer, and describes this release as preserving Glover's work with the changes needed to run on more recent systems.

The download is attached to the [StarDot thread](https://stardot.org.uk/forums/viewtopic.php?t=33887). Discussion is open there and in the [forum announcement](https://www.riscosopen.org/forum/forums/1/topics/20662).
