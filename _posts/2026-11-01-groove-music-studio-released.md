---
layout: post
title: "Groove Music Studio Brings Song Creation to RISC OS"
date: 2026-11-01 17:00:00 +0000
summary: "New music application enables RISC OS users to create songs using loops, drum grids, and piano rolls without needing to read traditional musical notation."
tags: [software, multimedia]
source_url: "https://www.riscosopen.org/forum/forums/1/topics/20638"
source_name: "RISC OS Open Forums"
image: /assets/images/groove-loops-dropped.png
image_alt: "Groove music studio interface showing loops being arranged"
---

Andrew Youll has released Groove, a music creation application for RISC OS 5 that allows users to compose songs without requiring knowledge of traditional music notation. The software provides an accessible approach to music making through ready-made loops, visual drum grids, and piano roll editing.

Groove enables users to drag pre-made loops into songs, draw drum beats on a grid, and sketch notes using a piano roll interface. The application includes a musical typing feature that turns the computer keyboard into a playable piano, supporting chord input. A recording mode provides a bar of count-in before capturing played notes, automatically quantizing them to the nearest sixteenth note.

[![Groove music studio interface showing loops being arranged]({{ '/assets/images/groove-loops-dropped.png' | relative_url }}){: width="1600" height="330" loading="lazy"}]({{ '/assets/images/groove-loops-dropped.png' | relative_url }})

*Groove's interface showing ready-made loops being arranged into a song. Screenshot from the [Groove user guide](https://raw.githubusercontent.com/adyoull/riscos-groove/v0.2/docs/guide/images/loops-dropped.png).*

## Sound Generation

The application synthesizes its built-in instruments and drums as they play, eliminating the need for large sample libraries and keeping song files compact as small text documents. When SoftMIDI is installed, each track can access the full range of 128 General MIDI instruments and eight drum kits from SoftMIDI's SoundFont library.

Groove also plays Maestro files, treating each channel as a separate track and rendering them with the same playback engine used for Maestro. This provides compatibility with the music files included in RISC OS's standard Documents folder.

## Features

The software supports arranging through moving, stretching, splitting, copying, and pasting regions across up to 16 tracks. Mixing capabilities include per-track volume, pan, mute, and solo controls, along with master volume and reverb effects. Undo and redo functions allow experimentation without risk.

Time signatures can be set to any value, including 3/4 and 6/8, and can change within a song. File format support includes song saving and loading, WAV export, MIDI import and export, WAV import, and Maestro music file playback.

## Requirements

Groove has been tested on Raspberry Pi 4 running RISC OS 5.31. It requires SharedUnixLibrary 1.16 or later and ARMEABISupport, both available through PackMan. SoftMIDI support is optional and also available via PackMan.

The application includes a user guide with illustrations, written for people new to computer-based music creation. It can be accessed from the menu on Groove's icon bar icon.
