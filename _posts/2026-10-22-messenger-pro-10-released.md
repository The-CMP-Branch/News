---
layout: post
title: "Messenger Pro 10 Released with HTML Email Display"
date: 2026-10-22 15:00:00 +0000
summary: "R-Comp's email client reaches double digits with native HTML rendering, improved Unicode support, and a beta 64-bit version for future RISC OS releases."
tags: [software, email]
source_url: "https://www.riscository.com/2026/messenger-pro-10-available/"
source_name: "RISCOSitory"
---

R-Comp has released Messenger Pro 10, marking the first major update to the RISC OS email client in four years. The release introduces native HTML email display, expanded Unicode support, and several interface improvements requested by users.

The new version can now display HTML emails with embedded images, providing a more modern viewing experience. For security, Messenger Pro will only automatically fetch images for contacts in the address book, with other images requiring user confirmation. The HTML rendering supports standard operations like copy and paste, while ignoring JavaScript for security reasons.

## Interface Enhancements

Messenger Pro 10 introduces an optional three-column mode for users accustomed to multi-column layouts in other email clients. This mode, designed for monitors with 1080p resolution or higher, presents a revised toolbar layout and unified interface without requiring manual window positioning.

Unicode support has been significantly expanded throughout the application. Translation between RISC OS's Latin alphabet and UTF-8 Unicode now works seamlessly across copy and paste operations, drag and drop, and message loading and saving. The improvements particularly benefit users working with messages in languages beyond the standard Latin character set.

## Modern Email Protocols

A beta email fetcher is included with version 10, offering expanded options for secure email connections. The new fetcher addresses Microsoft's OAuth2 requirements for Hotmail and Outlook addresses and supports Gmail access. It handles SMTP, POP, and IMAP protocols and originates from work on 64-bit email transport.

## Looking Ahead

Messenger Pro 10 includes a 64-bit version developed for testing purposes. While not yet available for general release, it will be offered as part of the version 10 upgrade program as RISC OS continues its progress toward 64-bit support.

The software is available now through !Store with upgrades priced at £20. Note that HTML email display requires RISC OS 5 or newer due to technical requirements and Unicode font support, though RISC OS 4 users retain access to fallback modes and browser-based HTML display options.
