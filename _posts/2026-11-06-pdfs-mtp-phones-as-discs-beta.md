---
layout: post
title: "PDFS Beta Brings MTP Devices to RISC OS as Filer Discs"
date: 2026-11-06 08:05:00 +0000
summary: "New filing system allows Android phones, tablets, and MTP cameras to appear as regular disc drives in the RISC OS Filer, enabling drag-and-drop file transfers."
tags: [software, filesystems]
source_url: "https://www.riscosopen.org/forum/forums/1/topics/20633"
source_name: "RISC OS Open Forums"
image: /assets/images/pdfs-devices.png
image_alt: "PDFS showing a device's storages on the icon bar with Filer windows open"
---

Andrew Youll has announced the beta release of PDFS (Portable Device Filing System), a new filing system for RISC OS 5 that enables MTP devices to appear in the Filer as standard disc drives. Released on 29 October 2026 as version 0.14 beta, the software supports Android phones and tablets, along with many cameras and media players.

When an MTP device is connected and configured for file transfer, each of its storage volumes receives an icon bar drive icon. Users can open these icons to view the contents in standard Filer windows and drag files in both directions. An Eject option in the icon menu safely disconnects individual devices, and an Eject All option is also provided. Devices should be ejected before physical disconnection.

[![PDFS showing a device's storages on the icon bar with Filer windows open]({{ '/assets/images/pdfs-devices.png' | relative_url }}){: width="1024" height="768" loading="lazy"}]({{ '/assets/images/pdfs-devices.png' | relative_url }})

*PDFS showing a device's two storages on the icon bar with Filer windows open. Screenshot from the [PDFS documentation](https://raw.githubusercontent.com/adyoull/riscos-pdfs/pdfs-0.14-beta/docs/images/devices.png), taken on RISC OS running under Linux with a simulated device.*

## Integration and Compatibility

Each storage volume appears as a disc named `PDFS::<Model>-<Storage>.$` and functions through the standard FileSwitch interface. This means the storage works with the Filer, the Copy command, BASIC programs, and any application that uses FileSwitch for file operations.

File copy operations run through Filer_Action, providing progress displays and allowing operations to be aborted while keeping the desktop responsive. The system preserves RISC OS file types by incorporating them into filenames on the device. A Text file named Letter appears as Letter.txt on the device, while files with types lacking a standard extension receive a comma-xxx suffix.

## Command Set and Testing

PDFS provides several star commands including PDFSDevices, PDFSMount, PDFSEject, PDFSUSB, and PDFSLog. The software requires RISC OS 5 with the native USB stack and has been tested using a Raspberry Pi connected to a Pixel phone.

As a beta release, the developer advises users to back up data before use. The software is distributed under the Apache 2.0 licence with no warranty. Testing with iPhones (which provide photos-only, read-only access), cameras, and media players had not been completed at the time of the initial announcement.

## Rapid Updates

Following user feedback, two quick updates followed. Version 0.15 beta, released on 30 October, addressed an issue where a phone set to Charging Only mode could delay system boot. It also fixed a USBDriver crash that occurred when switching to file transfer mode and resolved a problem where certain folders, such as DCIM, appeared nested inside themselves on some Android phones' SD cards.

Version 0.16 beta arrived on 31 October with automatic mounting support for Amazon Fire tablets and Motorola phones in File Transfer mode, which use vendor-specific MTP interfaces. This version now waits appropriately for Android's device access permission prompt, recovers from failed incoming USB transfers, and processes large Android folders one object at a time to improve responsiveness. Transfer speed information was added to the PDFSDevices command, and trace logging capability was added to PDFSLog.

## Availability

PDFS is available for installation through PackMan from the [author's package source](https://adyoull.github.io/riscos-packages/pkg/index), or as a zip download from the [GitHub release page for version 0.16 beta](https://github.com/adyoull/riscos-pdfs/releases/tag/pdfs-0.16-beta). Source code is available at the [GitHub repository](https://github.com/adyoull/riscos-pdfs).

The author notes that the code was written with Claude as a coding assistant.
