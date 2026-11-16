---
layout: post
title: "Archimedes Live Adds Touch Input for Phones and Tablets"
date: 2026-11-16 08:00:00 +0000
summary: "Paul Stone has restructured Archimedes Live, the browser-based Archimedes emulator, restoring the BASIC editor and disc insertion, adding touch input for phones and tablets, and improving audio, fast-forward and resume behaviour."
tags: [software, emulation]
source_url: "https://www.iconbar.com/articles/RISC_OS_open_source_developments_weekly_update_14th_November_2026/index2424.html"
source_name: "The Icon Bar"
---

Paul Stone has continued restructuring Archimedes Live, a browser-based Acorn Archimedes emulator at [archi.medes.live](https://archi.medes.live). Charles Ferguson reported the week's work in [The Icon Bar's open source round-up](https://www.iconbar.com/articles/RISC_OS_open_source_developments_weekly_update_14th_November_2026/index2424.html) of 14 November 2026.

The [archimedes-live](https://github.com/pdjstone/archimedes-live) repository from 7 to 13 November 2026 matches that account. Communication with the background worker was rebuilt, including an RPC proxy in place of hand-written worker messages, and the worker, audio worklet and shared code were given their own directories.

That work restored features that had broken during the refactor. The BASIC editor again runs and reloads programs in the emulator ([Make the BASIC editor work with the worker](https://github.com/pdjstone/archimedes-live/commit/3b4657a6dc91518063ecfcd05d48aa2becae85d1)). Inserting a disc after boot, by drag and drop or the upload button, works again ([Fix inserting a disc after boot](https://github.com/pdjstone/archimedes-live/commit/acb07d21cfe12188bfa5f7538ee77aa6ed23029e)).

Touch input was added for phones and tablets: tap for Select, a long press for Menu, a two-finger tap for Adjust, and drag, or a touchpad-style move when a program wants relative mouse input ([Update emulator: touch input for phones and tablets](https://github.com/pdjstone/archimedes-live/commit/e21e9c27bd88bdfe8d2228d390bd01d83bea6f06)). Audio now starts on the first tap. While the page is hidden, the audio worklet keeps a larger buffer so background stalls are less likely to underrun. A progress bar is shown during fast-forward, notices appear as toasts over the display, and the emulator resumes more reliably after loading software or changing machines.

The public site at [archi.medes.live](https://archi.medes.live) is serving a frontend built on 13 November 2026. That page includes the BASIC editor, disc-insertion controls and the fast-forward progress overlay from this week's work.

The README describes the project as a work in progress: a web frontend for [Arculator WASM](https://github.com/pdjstone/arculator-wasm). Source is on GitHub.
