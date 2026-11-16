---
layout: post
title: "SSHd Brings a Native SSH Server to RISC OS 5"
date: 2026-11-16 08:05:00 +0000
summary: "Christiane Ruetten has announced SSHd, a native SSH server for RISC OS 5 built on libssh and mbedTLS, aimed at cross development, scripting and AI agent integration, and installable through PackMan."
tags: [software, networking]
source_url: "https://www.riscosopen.org/forum/forums/1/topics/20675"
source_name: "RISC OS Open Forums"
---

Christiane Ruetten has announced SSHd, a native SSH server for RISC OS 5. The announcement appeared on 15 November 2026 in the RISC OS Open Announcements forum topic [SSHd for RISC OS](https://www.riscosopen.org/forum/forums/1/topics/20675). Source is in the [riscosshd](https://github.com/cr/riscosshd) GitHub repository, under an MIT licence.

Ruetten describes the project as something that began as an experiment and became convenient for cross development, scripting and AI agent integration on RISC OS 5 systems, and asks for feedback.

## Desktop SSH and SFTP

The README presents SSHd as a Wimp task with an icon-bar icon, built on [libssh](https://www.libssh.org/) and [mbedTLS](https://github.com/Mbed-TLS/mbedtls) and cross-compiled with GCCSDK. It accepts public-key logins only, apart from a one-time pairing code for `ssh-copy-id`. From another machine, `ssh host '*Cat'` runs a command, `ssh host` opens an interactive `*` command line in a TaskWindow, and `sftp` and `scp` copy files. Keys are managed in a desktop window, including an import that logs in to another machine and fetches its public keys.

The current documented version is 0.3.1. It has been tested on RISC OS 5.27 in RPCEmu and RISC OS 5.31 on a Raspberry Pi (RISC OS Direct). It needs a configured network and the CryptRandom module, which the PackMan package pulls in. The server listens on TCP port 22.

## Installation and PackMan

SSHd can be installed by adding its PackMan source, `https://cr.github.io/riscosshd/pkg/index`, then installing **SSHd** from the Network section. Zip downloads are also on the [releases page](https://github.com/cr/riscosshd/releases).

Ruetten asks who to talk to about getting the package into the official PackMan index and autobuilder. The binary currently statically links UnixLib, libmbedcrypto and a patched libssh, and the build system may need changes for autobuilder. The README's roadmap likewise lists getting the package into the riscos.info autobuilder index so that an extra PackMan source is not required.

Discussion continues in the [forum thread](https://www.riscosopen.org/forum/forums/1/topics/20675).
