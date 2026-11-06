---
layout: post
title: "RISC OS Developments Releases Enhanced Paint and Draw Test Versions"
date: 2026-11-06 08:20:00 +0000
summary: "New test releases bring SVG support to Draw, additional file formats and undo capability to Paint, as part of preparation for 64-bit RISC OS."
tags: [software, development]
source_url: "https://www.riscosopen.org/forum/forums/1/topics/20602"
source_name: "RISC OS Open Forums"
---

RISC OS Developments has announced new test versions of Paint and Draw, developed as part of the Renaissance Project with consideration for future 64-bit compatibility. Announced on 16 October 2026, these releases incorporate new features and elements from previous bounty submissions, and the company describes them as Director's Cuts. Testing on 32-bit systems is invited before the applications move forward.

This site previously covered the [announcement of the Renaissance Project](/News/2026/10/17/risc-os-renaissance-project-announced.html) on 17 October 2026.

## Paint Enhancements

The updated Paint application adds direct saving of screenshots as JPEG and PNG files. Screenshot capture can now grab a window's contents, matching functionality available in RISC OS Adjust. Additional import and export formats are supported, with files automatically loading on double-click when Paint is running.

File extensions now display when saving in non-sprite formats. An undo facility has been implemented. Previous behaviour that caused imported sprites to overwrite a selected sprite without warning when dragged in has been corrected. Multiple sprite files can now be imported simultaneously without issues.

## Draw Improvements

The headline feature for Draw is SVG import and export capability, enabling Draw files to be used on PC, Mac, and Linux systems. On 17 October, Andrew Rawnsley noted that Draw now employs a more intelligent naming convention for exported SVG files and appends /svg to filenames, allowing files to be transferred to other platforms without modification.

## Availability

Both applications are available for download from the [RISC OS Developments website](https://www.riscosdev.com/apps). Source code is included with the releases, and contributor credits appear in the ReadMe files.
