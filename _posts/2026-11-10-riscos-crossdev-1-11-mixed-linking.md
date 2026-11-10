---
layout: post
title: "riscos-crossdev 1.11 Adds Mixed Linking for Shared Libraries"
date: 2026-11-10 23:16:00 +0000
summary: "Andrew Youll has released riscos-crossdev 1.11, adding mixed linking so programs can share libraries through !SharedLibs while keeping UnixLib, libstdc++ and libgcc static, together with UnixLib 5.0.3.7."
tags: [development, software]
source_url: "https://www.riscosopen.org/forum/forums/1/topics/20589"
source_name: "RISC OS Open Forums"
---

Andrew Youll has released riscos-crossdev 1.11, his kit for building and testing RISC OS software on Linux with GCCSDK's GCC 10. The announcement on the [RISC OS Open forums](https://www.riscosopen.org/forum/forums/1/topics/20589) on 10 November 2026 highlights mixed (or hybrid) programs, which share libraries with other programs, and UnixLib 5.0.3.7.

## Mixed programs

Until now, every program built with the kit was fully static: UnixLib, the C++ library and every other library were linked into the program. That remains the default, and still works as before.

A mixed program still links UnixLib, libstdc++ and libgcc into itself, but its other libraries are shared objects loaded by !SharedLibs when it starts. Programs that use the same library file then share one copy in memory, and each program file is much smaller.

Youll used riscos-gtk as the test case. On a Raspberry Pi 4 under RISC OS 5, mixed Geany and L3afpad ran side by side from one 20 MB copy of GTK's 26 libraries, held in a `!GTKLibs` pack in `!Boot.Resources`. Opening the second program did not load GTK again. Each program still keeps its own UnixLib.

If a library tries to bring in a second UnixLib, the program stops with a message rather than running with two C libraries. Libraries built by GCCSDK for fully shared programs can still be used: the kit supplies empty stand-ins for shared UnixLib so those libraries use the program's own copy. Fully shared programs and static programs can run alongside mixed ones; Youll reports Iris running at the same time as mixed Geany and L3afpad on a Pi, all three using !SharedLibs.

To run a mixed program, users need a `!SharedLibs` with `ld-riscos/so/2` (GCCSDK 8 or later; Iris ships one) in `!Boot.Resources`. The older SharedLibs 4.0 package has only `ld-riscos/so/1` and will not run them. SharedUnixLibrary 1.16 or later and ARMEABISupport are still required.

Developers link the program with `-rdynamic` instead of `-static`, build each library with `-fPIC` then `-shared -nostdlib`, and can check the results with new kit checks. `docs/MIXED.md` describes the scheme, and `examples/mixed` is a small working example.

Youll notes that mixed programs are new. They have run on RISC OS 5 on his Pi 4 and on RISC OS on Linux, but not yet on other machines, so reports are welcome.

## Also in 1.11

UnixLib 5.0.3.7 comes from riscos-unixlib, Youll's unofficial fork of GCCSDK's UnixLib, with PThreadTicker 0.04. Shared memory works with ARMEABISupport 1.08 as well as 1.05, and the library can start mixed programs. There are no struct or argument changes, so existing programs relink to pick the update up. `-pthread` is accepted, as on Linux, so meson, CMake and many configure scripts that pass it work as they are.

The riscos-mesa development kit in this release is 20.3.5-18. The container image is `ghcr.io/adyoull/riscos-crossdev:1.11`.

riscos-crossdev 1.11 is on [GitHub](https://github.com/adyoull/riscos-crossdev) at tag v1.11. Discussion is in the [forum thread](https://www.riscosopen.org/forum/forums/1/topics/20589).
