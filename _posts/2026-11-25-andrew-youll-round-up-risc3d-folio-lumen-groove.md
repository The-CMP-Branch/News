---
layout: post
title: "Andrew Youll round-up: RISC3D 0.18, Folio test77, Lumen 0.0.42, Groove 0.4.4 and GTK updates"
date: 2026-11-25 08:05:00 +0000
summary: "A combined round-up of Andrew Youll's RISC OS releases from 22–25 November 2026, covering RISC3D's Configure page, Folio's Measure tool, Lumen rotate and flip, Groove score layout, GTK saving, and RISC OS on Linux audio."
tags: [andrew-youll, round-up, software, development]
source_url: "https://www.riscosopen.org/forum/forums/1"
source_name: "RISC OS Open Announcements"
---

This is a combined round-up of Andrew Youll's updates from 22–25 November 2026, grouped by project. The announcements were posted in the RISC OS Open Announcements forum, with matching GitHub releases. It follows this site's [earlier round-up of 17–21 November]({{ '/2026/11/22/andrew-youll-round-up-risc3d-gtk-lumen-groove/' | relative_url }}).

## RISC3D / V3DRender

Youll posted these in [RISC3D: 3D acceleration for RISC OS on Linux and RISC OS on the Pi 4](https://www.riscosopen.org/forum/forums/1/topics/20678).

[RISC3D 0.16](https://github.com/adyoull/riscos-risc3d/releases/tag/v0.16) (22 November) adds a RISC3D page in Configure (`!RISC3DSetup` in `!Boot.Resources.Configure`). The page can turn GPU drawing off so that programs draw in software, with no 3D driver loaded. The choice is kept in `Choices:RISC3D.Settings`. The RISC3D module 0.08 loads no driver while `RISC3D$Off` is set.

[RISC3D 0.17](https://github.com/adyoull/riscos-risc3d/releases/tag/v0.17) (22 November) expands that page: it shows which driver is in use, the renderer, OpenGL and OpenGL ES versions, the largest texture and the extensions. On native RISC OS the OpenGL figures need [`!MesaLibs` 20.3.5-23](https://github.com/adyoull/riscos-mesa). A Hardware section from V3DRender reports the GPU, its clock, GPU memory in use, and whether desktop 2D is on. Programs can share textures and buffers between OpenGL contexts, and use a context per thread.

[V3DRender 0.26](https://github.com/adyoull/riscos-v3drender/releases/tag/v0.26) (22 November, bundled with RISC3D 0.17) powers the GPU up before touching it, which Youll described as a likely fix for start-up aborts on some boards, including a CM4. Desktop rectangle copies and fills can run on the GPU (`*V3DRender 2D on`); this is off by default. Youll's timings on a Pi 4 at 1920×1200, 32 bits a pixel, include a 512×320 copy in 266 µs on the GPU against 566 µs on the CPU.

[RISC3D 0.18](https://github.com/adyoull/riscos-risc3d/releases/tag/v0.18) (23 November) fixes Configure's RISC3D page. Opening it stopped with "SWI &59D01 not known" where ARMEABISupport was not already loaded (reported by Doug Webb and Chris Hughes on CM4 machines). `!RISC3DSetup` now loads SharedUnixLibrary and ARMEABISupport from `System:Modules`, or says which to install from PackMan. Nothing else changed from 0.17. In PackMan the matching package is RISC3D 0.09.0.2-1.

## RISC OS on Linux

These updates were posted in [Updated RISC OS on Linux](https://www.riscosopen.org/forum/forums/1/topics/20657).

On 24 November Youll told George T. Greenfield that audio on the Pi 4 should be working. The problem was how `rol-snd` (the Linux-to-RISC OS sound interface) read some monitors' ELD data; Youll reproduced it on a monitor of his own.

A kernel update had been clearing modules from the FAT partition to make space for the new kernel, and not copying them back when space ran out. Youll pushed a fix that copies the modules out, updates the kernel, then copies them back. Norman Lawrence, whose Argon One battery icon had disappeared, needed to run Updates twice, with a restart after each, and then the icon returned to the icon bar.

## GTK apps

Posted in the [GTK 3.24.41](https://www.riscosopen.org/forum/forums/1/topics/20588) topic on 22 November, after this site's earlier note of [AbiWord 3.0.8-riscos9 and Gnumeric 1.12.62-riscos23]({{ '/2026/11/22/andrew-youll-round-up-risc3d-gtk-lumen-groove/' | relative_url }}).

[`!GTKLibs` 3.24.52-27](https://github.com/adyoull/riscos-gtk/releases/tag/gtklibs-3.24.52-27) and [Gnumeric 1.12.62-riscos24](https://github.com/adyoull/riscos-gtk/releases/tag/gnumeric-1.12.62-riscos24) follow more of Doug Webb's testing. Gnumeric's `.xls` files no longer give Fireworkz black cells: unfilled cells had been written with a black pattern colour that Excel ignores but Fireworkz used as the background.

The File type menu in a Save box opened from Menu > File > Save As no longer closes that box (which could leave the program waiting, and crash Gnumeric if Save As was chosen again). After the first GTK program of a session, later ones start faster because the desktop's fonts are checked only once. Gnumeric riscos24 needs !GTKLibs 3.24.52-25 or later.

## Folio

Posted in [Folio: a PDF and ebook reader for the desktop](https://www.riscosopen.org/forum/forums/1/topics/20590), after this site's note of [test76]({{ '/2026/11/13/folio-test76-user-guide-riscpc/' | relative_url }}).

[0.0.1-test77](https://github.com/adyoull/riscos-folio/releases/tag/v0.0.1-test77) (23 November) takes most of Matthew Phillips' suggestions. Measure moves from Edit onto the document menu under Find, with a ruler button on the toolbar. Add to page writes the figures on the page in red. You can type a scale ratio, or draw a line over a scale bar and type its real length. Pages > Arrange pages fills the window with thumbnails so pages can be selected, moved and deleted. There is a matching RiscPC zip.

## Lumen

Posted in [Lumen: a photo library and non-destructive editor for RISC OS](https://www.riscosopen.org/forum/forums/1/topics/20646), after this site's note of [0.0.40]({{ '/2026/11/22/andrew-youll-round-up-risc3d-gtk-lumen-groove/' | relative_url }}).

[0.0.41](https://github.com/adyoull/riscos-lumen/releases/tag/v0.0.41) (23 November) adds Rotate and flip on the Selection menu and the Viewer's Photo menu. Left and Right turn photos a quarter (`[` and `]` in the Browser too); Flip horizontally and Flip vertically mirror them. The file is not changed. FITS files typed FITS are imported without a `/fits` name. When a FITS header has a sky position, Lumen uses it to show the picture as the sky looks, so DWARF stacks that had come out upside down now have north up. Very smooth stacks, such as Chris Terran's star-removed M45, are stretched so the nebulosity shows.

[0.0.42](https://github.com/adyoull/riscos-lumen/releases/tag/v0.0.42) (24 November) puts a Stretch group on FITS pictures: Amount (100% is the auto-stretch as before) and Black point. The stretch is applied as the file is read and kept with the photo. H flips horizontally and U vertically. The Rotate and flip menus now show their keys.

## Groove

Posted in [Groove: a music studio for RISC OS](https://www.riscosopen.org/forum/forums/1/topics/20638), after this site's note of [0.4.2]({{ '/2026/11/22/andrew-youll-round-up-risc3d-gtk-lumen-groove/' | relative_url }}).

[0.4.3](https://github.com/adyoull/riscos-groove/releases/tag/v0.4.3) (23 November) writes MuseScore and MusicXML scores the way the score itself does: each note in its own voice and on its own staff, with the score's written values, spelling, clefs, ties, rests, beams, tuplets, lyrics, tempo words, dynamics, slurs and pedalling. Repeats, endings, D.C. and D.S. play in the same order as in MuseScore. Youll checked it bar by bar against MuseScore 4 on OpenScore's 1,352 Lieder and 121 string quartets: 99% of the songs' bars and 99.6% of the quartets' bars come out as MuseScore writes them, up from about 22%. It also starts on a Raspberry Pi with alignment exceptions turned on (Geofrey Baxendale's report). Groove is in PackMan as 0.4.3.0.1-1 under Audio.

[0.4.4](https://github.com/adyoull/riscos-groove/releases/tag/v0.4.4) (24 November) lets the Score window zoom to 25%, 30%, 40%, 50%, 60%, 80%, 100%, 130% and 160% (it previously stopped at 60%), after Paul Sprangers asked to read orchestral scores. Ctrl with the scroll wheel, and + and −, zoom as well. At 25%, about 25 bars of a string quartet fit across the window. PackMan has it as 0.4.4.0.1-1.

## riscos-crossdev / UnixLib

These were GitHub releases on 22 November; there was no new Youll post in the [riscos-crossdev](https://www.riscosopen.org/forum/forums/1/topics/20589) forum topic in this window.

[riscos-unixlib 5.0.3.9](https://github.com/adyoull/riscos-unixlib/releases/tag/v5.0.3.9): `lseek` past the end of a file no longer extends it, which had made SQLite say "file is not a database" for new databases on FileCore discs.

[riscos-unixlib 5.0.3.10](https://github.com/adyoull/riscos-unixlib/releases/tag/v5.0.3.10): a bad file descriptor below 1000 returns EBADF without a SWI. TORCS had been trying a bad fd about 13,500 times a second under RISC OS on Linux, and track loading stalled.

[riscos-crossdev 1.11.3](https://github.com/adyoull/riscos-crossdev/releases/tag/v1.11.3) takes in mixed-program findings: several library directories separated with `;` in `LD_LIBRARY_PATH`, a `WimpSlot` in `!Run`, and shared libraries as ARM code.

[riscos-crossdev 1.12](https://github.com/adyoull/riscos-crossdev/releases/tag/v1.12) ships UnixLib 5.0.3.9 and links the whole of UnixLib into mixed programs, so a newer library pack can use UnixLib functions without the program being relinked.

[riscos-crossdev 1.13](https://github.com/adyoull/riscos-crossdev/releases/tag/v1.13) ships UnixLib 5.0.3.10 and aligns UnixLib's assembler data. Programs built with 1.12 and earlier could abort at start-up on a Pi with alignment exceptions on (Groove and YTDL were affected). Rebuild with 1.13. An optional GCC 16 toolchain is attached for ports that need C++23.

Andrew is speaking at WROCC on 2 December 2026, "Andrew Youll – Building Blocks" ([WROCC meetings](https://www.wrocc.org.uk/meetings)).
