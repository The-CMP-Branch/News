---
layout: post
title: "Groove Music Studio Adds MIDI Support"
date: 2026-11-03 09:00:00 +0000
summary: "The recently released RISC OS music creation app gains MIDI input and output capabilities just two days after its initial launch, allowing integration with external keyboards and sound modules."
tags: [software, multimedia]
source_url: "https://www.riscosopen.org/forum/forums/1/topics/20638"
source_name: "RISC OS Open Forums"
---

Andrew Youll has released version 0.2.2 of Groove, adding MIDI input and output capabilities to the music creation application that launched on 1st November. The rapid update, developed in response to user feedback, enables Groove to communicate with external MIDI keyboards and sound modules.

With Pete Everett's MIDI Support module loaded, Groove registers as a MIDI driver visible in the MIDI Manager's routing interface. Users can connect MIDI keyboards or software instruments directly to Groove, with velocity and sustain pedal controls working as expected. Recording from a MIDI keyboard functions identically to recording from the computer keyboard, with notes automatically quantised to the nearest sixteenth note.

## External Sound Modules

The Track menu's new "Play on MIDI out" option sends individual tracks to external MIDI hardware or software synthesizers rather than using Groove's internal synthesis. Each instrument track receives its own MIDI channel, with drums assigned to channel 10 following General MIDI conventions. Notes are sent in synchronisation with the rest of the song, maintaining proper timing across all tracks.

Groove supports both the MIDI Support module's routing system and direct USBMIDI port connections. When MIDI Support is unavailable, Groove accesses USBMIDI module ports directly while the application has input focus.

## Keyboard Shortcuts

Version 0.2.3, released shortly after 0.2.2, adds keyboard shortcuts for MIDI output management. F10 cycles through available MIDI output destinations including MIDI Support and USB ports 1 through 4, while F11 toggles MIDI output for the selected track. Shift+F11 enables MIDI output for all drum and instrument tracks simultaneously, allowing entire songs to play through external hardware.

The song window's title bar displays the current MIDI output destination, such as "MIDI out: Support", providing immediate feedback about routing configuration.

## Testing and Compatibility

Andrew Youll has tested both MIDI input and output using Pete Everett's MIDI Support, MIDIKeyboard, and MidiSynth applications. Community member Jean-Michel BRÜCK successfully tested the software with USB-to-MIDI interfaces, a Roland Sound Canvas expander, and an M-Audio Keystation Mini 32 keyboard, confirming compatibility with external hardware.

Groove 0.2.3 is available from the [GitHub releases page](https://github.com/adyoull/riscos-groove/releases/tag/v0.2.3). The software requires RISC OS 5 on an ARMv7 machine with VFP, such as a Raspberry Pi 2 or later. Pete Everett's MIDI Support module can be obtained from [Forever.onmypc.net](http://www.forever.onmypc.net/).
