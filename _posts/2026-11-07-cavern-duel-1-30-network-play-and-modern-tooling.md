---
layout: post
title: "Cavern Duel 1.30 Adds Network Play and Modern Development Tooling"
date: 2026-11-07 07:15:00 +0000
summary: "Stephen Scott has resurrected the two-player Cavern Duel game with network multiplayer, an improved level editor, and a comprehensive Mac-based cross-development environment built with AI assistance."
tags: [software, games]
source_url: "https://www.riscosopen.org/forum/forums/1/topics/20642"
source_name: "RISC OS Open Forums"
---

Stephen Scott has released Cavern Duel version 1.30, reviving a two-player game originally written by his brother Graeme Scott in 1993 and 1994. Players roam a cavern collecting food and weapons before facing their opponent. The game saw updates in 1997 and between 2007 and 2011, with the most recent work attempting to support newer RISC OS versions before development stalled.

The new release adds network-enabled play, allowing two players on separate computers to compete without crowding around a single keyboard. The game includes instructions for setting up network matches. Various code changes throughout the game facilitate this multiplayer mode, though Stephen notes his testing has been limited and welcomes feedback, especially from users with physical hardware rather than emulators.

The accompanying Cavern Duel editor has been updated to version 1.38. Both the game and editor now use DrWimp 5.04 for their Wimp front ends, which cleaned out buggy Wimp code and fixed a long-standing problem where windows rendered partially offscreen. The editor also gains a significant usability improvement: users can now hold down the Select mouse button to draw levels continuously, replacing the previous approach of clicking countless times to create each level element.

Stephen developed these updates using a modern toolchain based on an Apple Studio Mac running macOS 27 and Visual Studio Code. The repository includes comprehensive documentation on this setup, which uses RPCEmu Enhanced with multiple instances for testing network play. The VS Code `tasks.json` file provides shortcuts for building the game targeting RISC OS 3.71, 5.37 and 5.30. While he has not yet created an equivalent Windows environment, he uses Parallels and intends to explore that option.

The project was made possible with AI assistance from Anthropic's Claude. Stephen notes that while he has reviewed the output to the best of his knowledge, it appears sound. His ultimate aim is to enable online play and move to graphics mode independence, as the sprites remain configured for mode 12. He hopes the tooling approach offers value to other RISC OS developers looking to scratch their creative itch.

Cavern Duel 1.30 is available from the [GitHub repository](https://github.com/sassquad/cavern-duel), with discussion in the [forum announcement thread](https://www.riscosopen.org/forum/forums/1/topics/20642). The original [Cavern Duel website](https://www.sassquad.net/cavernduel) has not yet been updated to reflect the new releases.
