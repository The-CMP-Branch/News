---
layout: post
title: "Updated RISC OS on Linux Brings RISC OS 5.31 to Raspberry Pi and Macs"
date: 2026-11-08 07:30:00 +0000
summary: "Andrew Youll has released the first update and expansion of Timothy Baldwin's Linux port of RISC OS, brought up to RISC OS 5.31 and packaged as complete images that boot straight into the desktop on Debian 13."
tags: [software, emulation, linux, raspberry-pi]
source_url: "https://www.riscosopen.org/forum/forums/1/topics/20657"
source_name: "RISC OS Open Forums"
image: /assets/images/risc-os-on-linux-desktop.png
image_alt: "The RISC OS on Linux desktop"
---

Andrew Youll has announced the first release of his update and expansion of Timothy Baldwin's Linux port of RISC OS. Baldwin's port made it possible to run RISC OS as a Linux program; Youll's work brings it up to date with RISC OS Open's current sources (RISC OS 5.31, with 19 builds since) and packages it as complete images that boot straight into the RISC OS desktop on Debian 13.

[![The RISC OS on Linux desktop]({{ '/assets/images/risc-os-on-linux-desktop.png' | relative_url }}){: width="1280" height="800" loading="lazy"}]({{ '/assets/images/risc-os-on-linux-desktop.png' | relative_url }})

*The RISC OS on Linux desktop. Screenshot: Andrew Youll / RISCOSonLinux on GitHub.*

The images can be written to an SD card, or added as a ready-made UTM machine on Apple Silicon Macs. They run on Raspberry Pi 3, Zero 2 W, 4/400, 5/500 and Compute Modules; on Apple Silicon Macs via UTM and QEMU; and experimentally on the Windows Dev Kit 2023, UEFI machines and VMs, and Pinebooks. On 32-bit-capable ARM CPUs RISC OS runs natively; on Apple chips it runs under QEMU.

Youll reports that the release completes most of Baldwin's to-do list. Sound output now plays through Linux. VFPSupport covers VFP and NEON. Physical memory pool (PMP) dynamic areas are implemented in the kernel, so ARMEABISupport and Iris work. IXFS error handling has been improved. A new front end drives video, keyboard and mouse through Linux's KMS. Linux commands can be run from RISC OS with `*Linux`, `*LinuxUser` and `*IXRun`. Binary releases include a signed package repository.

On performance, Youll states that SWIs are about three times faster on a Raspberry Pi 4, and FPA instructions about 4.5 times faster, than before his changes.

The images are presented as a complete system: wired networking and Wi-Fi are configured in Configure, USB discs appear with FAT, exFAT, NTFS and ext4 support, and updates and rollback are available from Configure. NetSurf, RDPServer and Folio are preinstalled, and PackMan is set up.

Youll describes this as a test release and asks users to report problems, including the LOGS folder from the card's FAT partition. He credits Timothy Baldwin for the port the work is built on, and Chris Gransden for testing.

Images, release notes and full history are on the [RISCOSonLinux GitHub repository](https://github.com/adyoull/RISCOSonLinux). Discussion is in the [forum announcement thread](https://www.riscosopen.org/forum/forums/1/topics/20657).
