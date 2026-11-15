---
layout: post
title: "RISC OS on Linux Adds Drivers for Plug-in Wi-Fi, Ethernet and Mobile Broadband Adapters"
date: 2026-11-15 07:55:00 +0000
summary: "Andrew Youll's latest RISC OS on Linux update, through Configure's Updates, adds drivers for plug-in USB and PCI Express Wi-Fi, Ethernet and mobile broadband adapters, plus Compute Module USB and Photodesk fixes."
tags: [software, emulation, linux, raspberry-pi]
source_url: "https://www.riscosopen.org/forum/forums/1/topics/20657?page=4"
source_name: "RISC OS Open Forums"
---

Andrew Youll has posted a further RISC OS on Linux update, adding drivers for plug-in Wi-Fi, Ethernet and mobile broadband adapters. He announced it on the evening of 14 November 2026 in the RISC OS Open Announcements topic [Updated RISC OS on Linux](https://www.riscosopen.org/forum/forums/1/topics/20657?page=4). It follows [the updated release this site covered on 8 November]({{ '/2026/11/08/risc-os-on-linux-updated-release/' | relative_url }}) and [the RiSH, interactive commands and RISC OS 5.31-24 follow-up of 11 November]({{ '/2026/11/11/risc-os-on-linux-rish-terminal-5-31-24/' | relative_url }}). The new work arrives through Configure → Updates (Check for updates, then Install).

## Plug-in adapters

Until now only each machine's own Wi-Fi and network worked. Adapters that are plugged in or fitted now have drivers:

- USB Wi-Fi adapters (Realtek, MediaTek/Ralink and Atheros chips)
- USB Ethernet adapters
- phone and mobile broadband sticks
- PCI Express Wi-Fi and Ethernet cards (Intel, Realtek, MediaTek and Qualcomm Atheros, including the Windows Dev Kit 2023's own Wi-Fi)

Youll's instructions are to plug the adapter in, then set it up as usual in Configure → Linux network.

Which connection is used: a cable with a link first; a USB Wi-Fi adapter before built-in Wi-Fi.

Huawei mobile broadband sticks that first show up as a CD drive are switched to network mode. Youll credits Raik's report.

## Compute Module USB and Photodesk

Compute Modules whose USB sockets did not work — no keyboard or mouse, USB drives ignored, and a black screen when started from USB, as on Chris Hall's CM5 Lite — are listed as fixed by the update. If a keyboard is not available to run Updates, Youll points to [manual instructions](https://github.com/adyoull/RISCOSonLinux/blob/main/docs/install-raspberry-pi.md) that can be followed from another computer.

Follow-up posts on 15 November show Hall's CM5 keyboard and mouse still not working, with Youll investigating. Compute Module testing is ongoing.

Photodesk Image → Rotate on a large picture no longer fails. Youll credits George's report.

## A larger test update

This update is bigger and slower than usual. The adapters' firmware comes from Debian's own firmware packages, a download of a hundred megabytes or more, and Updates goes through its steps twice. Youll asks users to let it finish, then restart.

Please treat it as a test release. If the machine does not start afterwards, an empty file called `ROLLBACK` on the card's FAT partition reverts to the previous version.

Youll welcomes reports, working or not: the adapter's make and model, and `kernel-log.txt` from the card's `LOGS` folder (it names the driver in lines starting `rol-modd`).

Not addressed yet: the slow Wi-Fi George and Raik have seen, and OvationPro from HardDisc4.

Versions: `riscos-kernel-pi` 6.6.78-13, `riscos-kernel-generic` and `riscos-kernel-wdk2023` 7.2.0-6, `riscos-support` 1.0.0055-1, `riscos-harddisc` 1.0.0054-1.

Images and notes remain on the [RISCOSonLinux](https://github.com/adyoull/RISCOSonLinux) GitHub repository. Discussion continues in the [forum thread](https://www.riscosopen.org/forum/forums/1/topics/20657?page=4).
