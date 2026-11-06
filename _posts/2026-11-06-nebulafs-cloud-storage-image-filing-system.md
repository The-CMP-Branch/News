---
layout: post
title: "NebulaFS Brings Cloud Storage Access to RISC OS"
date: 2026-11-06 08:10:00 +0000
summary: "Image filing system provides access to WebDAV, S3, SFTP, and FTP cloud services as local folders, with folder synchronisation support."
tags: [software, filesystems]
source_url: "https://www.riscosopen.org/forum/forums/1/topics/20645"
source_name: "RISC OS Open Forums"
---

Rob Kendrick has announced NebulaFS, an image file system that provides access to cloud storage services as if they were local folders on RISC OS. Announced on 3 November 2026, the software revives a project that was half-finished approximately 20 years ago, made more practical now that RISC OS sources are publicly available.

Inspired by ImageNFS and by extension Sunfish, NebulaFS supports multiple cloud storage protocols including WebDAV services such as Nextcloud, Owncloud, and pCloud, S3-compatible services including AWS S3, Minio, and Backblaze, SFTP connections to any modern UNIX server, and traditional FTP.

## Access Method

Rather than using a conventional mounting process, NebulaFS uses a distinctive approach where users create a small text configuration file or use the graphical interface to generate one. This file can then be entered like a directory, providing access to the remote storage. The system includes rudimentary support for synchronising a local folder with cloud storage.

## Current Status

A formal release is awaiting completion of work on certain allocations. In the interim, a pre-release demonstration version with some limitations is available on the [KiwiSoft website](https://www.kiwisoft.co.uk/software.html).

## Alternative Solutions

In the announcement thread, George T. Greenfield noted that Steve Revill's revamped LanManFS provides access to pCloud through a Windows, Mac, or Linux machine on the local network. Andrew Rawnsley highlighted that LanMan98 from RISC OS Developments offers native pCloud access via secure WebDAV and is available as a free download from the [RISC OS Developments website](http://www.riscosdev.com/lanman98).

This site previously covered LanManFS's addition of SMB2 and SMB3 support in the [22 October 2026 article](/News/2026/10/22/lanmanfs-smb2-smb3-support-beta.html).
