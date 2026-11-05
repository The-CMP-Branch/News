---
layout: post
title: "riscos-gtk RC15 Brings Security Updates and GTK 3.24.52"
date: 2026-11-03 17:00:00 +0000
summary: "The GTK 3 port for RISC OS receives a major update with two years of upstream fixes, 154 Ubuntu security patches, and updated Gnumeric spreadsheet application."
tags: [software, security]
source_url: "https://www.riscosopen.org/forum/forums/1/topics/20588"
source_name: "RISC OS Open Forums"
---

Andrew Youll has released riscos-gtk public beta RC15, updating the GTK 3 framework from version 3.24.41 to 3.24.52 and incorporating 154 security fixes from Ubuntu's long-term support packages. All GTK applications in the distribution have been rebuilt against the updated libraries.

The release brings two years of upstream bug and crash fixes from the GTK project. Rather than tracking individual library versions, riscos-gtk adopts Ubuntu 24.04 LTS's tested and verified library combinations, ensuring compatibility between components. This approach provides a stable foundation for the port while maintaining access to security updates.

## Security Patches

RC15 introduces Ubuntu's downstream security patches for the first time in the riscos-gtk project. Previous releases built from Ubuntu's original upstream tarballs without applying Ubuntu's additional patches. The 154 security fixes span multiple libraries:

- GLib: 49 patches
- libxml2: 32 patches
- Expat: 27 patches
- libpng: 23 patches
- Additional fixes in FreeType, gdk-pixbuf, libxslt, zlib, libcroco, libgsf, and libetpan

These updates primarily benefit ClawsMail, which handles network data from email, RSS feeds, and calendar services, as well as AbiWord and Gnumeric when opening documents from untrusted sources.

## Application Updates

Gnumeric has been updated from version 1.12.57 to 1.12.62, incorporating upstream bug fixes and crash repairs. The new release adds several spreadsheet functions including XLOOKUP, XMATCH, TEXTBEFORE, TEXTAFTER, and TEXTSPLIT. All 43 built-in plugins remain available.

The office suite components—AbiWord, Gnumeric, ClawsMail, Geany, L3afpad, and mtPaint—have been rebuilt against the updated GTK framework and now include the security patches.

## Filename Handling

A long-standing limitation preventing GTK applications from opening files with RISC OS-style names has been resolved. Files named using RISC OS conventions, such as `hello/c`, `foo/h`, or `notes/s`, previously failed to open because the C library attempted to find `c.hello` instead. Both naming styles now work correctly, with Geany opening `hello/c` and `c.hello` as C source files and building `c.hello` files as GCC expects.

An UnixLib update (version 5.0.3.5) addresses a related issue where files with RISC OS types differing from their extension's usual type—such as a Text file named `something.xml`—could not be renamed or overwritten. ClawsMail previously could not save its folder list in such cases.

ClawsMail's `--subscribe` command-line option, used for RSS feed and calendar subscriptions, now correctly opens new folders rather than exiting unexpectedly as in upstream version 4.4.0.

## Requirements and Testing

The software requires RISC OS 5 on ARMv7 hardware with VFP support, such as a Raspberry Pi 2 or later. RC15 has been tested on RISC OS 5.31 and passes 576 automated checks in the test suite.

riscos-gtk RC15 is available from the [GitHub releases page](https://github.com/adyoull/riscos-gtk/releases/tag/v3.24.52-riscos1.0-rc15). The package includes full source code, and security patches are documented with their Ubuntu package versions for verification and future updates.
