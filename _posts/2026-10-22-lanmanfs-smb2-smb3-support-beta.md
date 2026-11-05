---
layout: post
title: "LanManFS Gains SMB2 and SMB3 Support in Beta Release"
date: 2026-10-22 13:00:00 +0000
summary: "RISC OS Open releases updated network file sharing that reconnects RISC OS computers to modern Windows, macOS, and NAS systems after years of compatibility issues."
tags: [software, networking]
source_url: "https://www.riscosopen.org/news/articles/2026/10/22/two-samba-or-not-two-samba-smb2-lands-in-the-nightly-builds"
source_name: "RISC OS Open"
---

RISC OS Open has released a beta version of LanManFS with support for SMB2 and SMB3 protocols, addressing years of connectivity problems with modern networks. The update allows RISC OS computers to once again access file shares on Windows, macOS, Linux, and network storage devices.

The original SMB protocol, which RISC OS has supported through OmniClient's LanManFS since the 1990s, was disabled by default in Windows 10 and many NAS systems due to security concerns. This left RISC OS users staring at empty file server windows when attempting to browse network shares.

![LanManFS mounting a Windows 11 share]({{ '/assets/images/lanmanfs-win11-mount.png' | relative_url }}){: width="626" height="270" loading="lazy"}

*LanManFS successfully mounting and browsing a Windows 11 network share. Screenshot from [RISC OS Open](https://www.riscosopen.org/news/articles/2026/10/22/two-samba-or-not-two-samba-smb2-lands-in-the-nightly-builds).*

## Modern Protocol Support

The new LanManFS supports SMB protocols up to version 3.0.2, while maintaining the original dialect as a fallback for older servers. Modern authentication using NTLMv2 is now supported, with message signing whenever requested by the server to prevent tampering.

Server discovery has been improved to use DNS lookups in addition to traditional NetBIOS broadcasts. Long filenames are now standard, with support for names containing characters from Greek, Russian, Chinese, and even emoji, all accessible from the Filer. File types are automatically determined from extensions, so files like Report.txt and Photo.jpg are correctly identified without renaming.

## Performance Improvements

Speed has received considerable attention during development. A per-mount cache reduces redundant server queries, while reads and writes now transfer data in larger blocks. One tester reported that browsing over 4,000 albums on a Synology NAS now completes in under a minute.

The updated software includes automatic reconnection when server connections are lost, eliminating the need to manually dismount and remount shares. Directory displays in the Filer automatically refresh when files change on the server.

## Beta Testing

The new LanManFS completed 26 alpha releases with volunteer testers using a variety of servers including Windows, macOS, Samba on Linux, and various NAS devices. The software is now available in RISC OS Open's nightly beta builds and can be downloaded via PackMan or directly from ROOL's package index.

RISC OS Open is particularly interested in feedback regarding servers that refuse login attempts, missing or misnamed files and folders, and performance issues. Users are encouraged to check the known issues list before reporting problems on the forums.
