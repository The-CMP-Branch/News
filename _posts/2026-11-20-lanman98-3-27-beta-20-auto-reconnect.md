---
layout: post
title: "LanMan98 3.27 (Beta 20) Adds Auto-Reconnect and Per-Share Icon Mappings"
date: 2026-11-20 08:05:00 +0000
summary: "RISC OS Developments has released LanMan98 3.27 (beta 20), a 32-bit build backported from the 64-bit RISC OS 10 code, with optional auto-reconnect at startup, share definitions stored in Choices, and per-share iconbar icons."
tags: [software, networking]
source_url: "https://www.riscosopen.org/forum/forums/1/topics/20545?page=3"
source_name: "RISC OS Open Forums"
---

RISC OS Developments has released LanMan98 3.27 (beta 20). Andrew Rawnsley posted on the evening of 19 November 2026 in the RISC OS Open Announcements topic [LanMan98 v3 public beta now available](https://www.riscosopen.org/forum/forums/1/topics/20545?page=3) that the build is on the [download site](https://www.riscosdev.com/lanman98/). The file there is `LM98-v327-beta20.zip`, last modified 19 November 2026.

LanMan98 is RISC OS Developments' network sharing client. It is a separate product from RISC OS Open's LanManFS, whose SMB2/3 beta this site [covered on 22 October]({{ '/2026/10/22/lanmanfs-smb2-smb3-support-beta/' | relative_url }}).

The 32-bit release is backported from the 64-bit (RISC OS 10) code. POSIX multi-threading and hardware AES instructions are disabled to suit 32-bit RISC OS on ARMv7/8 CPUs. The version number jumps from 3.08 to 3.27.

## What is new for users

Rawnsley lists three main user-facing features:

1. Optional auto-reconnect to shares at startup, turned on from an iconbar menu option.
2. Share definitions have moved from `!LanMan98.Discs` to `<Choices$Write>.LanMan98.Discs` (that is, `!Boot.Choices.LanMan98.Discs` or `!Choices.LanMan98.Discs`). Existing shares should migrate automatically.
3. Per-share iconbar icon mappings, set inside `!LanMan98` for now (Rawnsley notes they probably ought to live in Choices in a later build), so a NAS can use a different icon from Windows or Mac shares.

On the technical side, the SecureSockets2 module has updated security. Performance may be improved; speeds over 110 MB/s have been observed on 64-bit RISC OS. There are also zero page fixes, following a report from Martin A.

## The v3 public beta

RISC OS Developments first announced the LanMan98 v3 public beta on 14 September 2026 in the same topic. That release added SMB 2 and 3 support, including SMB 3.1.1 (and also 2.0.2, 2.1, 3.0 and 3.02), while keeping the older SMB 1 path. WebDAV support arrived in later betas; beta 18, posted on 23 September, improved WebDAV and pCloud access and included a pCloud guide. pCloud currently needs RISC OS 5 on ARMv6 or later. Beta 19, posted on 26 September, added WebDAV proxy support.

## pCloud login on 19 November

On the afternoon of 19 November, before 3.27 was posted, David Pitt reported a WebDAV authentication error with pCloud on beta 19a. Rawnsley confirmed it as an open issue that was being looked into, and also noted recent reports of problems with pCloud's WebDAV service. Later that afternoon Pitt wrote that it was fixed, and Rawnsley said it was working for him in 3.08 while further updates were still being tested. The 3.27 announcement does not mention pCloud.

## Download

[LM98-v327-beta20.zip](https://www.riscosdev.com/lanman98/LM98-v327-beta20.zip) (4.8 MB) is on the RISC OS Developments [LanMan98 download page](https://www.riscosdev.com/lanman98/). The original v3 announcement says source is provided under the CDDL licence.

Discussion continues in the [forum thread](https://www.riscosopen.org/forum/forums/1/topics/20545).
