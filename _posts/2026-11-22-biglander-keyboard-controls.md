---
layout: post
title: "BigLander Adds Keyboard Controls to David Braben's Archimedes Lander"
date: 2026-11-22 08:00:00 +0000
summary: "Mark Moxon's BigLander, a larger-landscape version of the 1987 Archimedes demo game Lander, now offers Elite-style and RISC OS keyboard layouts as well as the original mouse controls."
tags: [software, games]
source_url: "https://lander.bbcelite.com/hacks/big_lander/downloads.html"
source_name: "Mark Moxon, lander.bbcelite.com"
image: /assets/images/big-lander-landscape.png
image_alt: "BigLander showing a large chequered landscape of trees, houses and a hovering ship"
---

Mark Moxon has added keyboard controls to BigLander, his "gently hacked" version of David Braben's 1987 Lander — the Archimedes' original demo game — with bigger landscapes. He posted on [StarDot](https://stardot.org.uk/forums/viewtopic.php?t=33971) on 19 November 2026, and updated the post on 20 November. Downloads, key maps and browser links are on [lander.bbcelite.com](https://lander.bbcelite.com/hacks/big_lander/downloads.html).

BigLander stretches the original 12×10-tile landscape up to 121×121 tiles and runs on all versions of RISC OS. The first release was 1 March 2024. On 12 November 2026 the four landscape sizes were combined on one ADFS disc image.

[![BigLander showing a large chequered landscape of trees, houses and a hovering ship]({{ '/assets/images/big-lander-landscape.png' | relative_url }}){: width="330" height="266" loading="lazy"}]({{ '/assets/images/big-lander-landscape.png' | relative_url }})

*BigLander in play. Image: Mark Moxon, lander.bbcelite.com.*

## Elite-style keys (19 November)

The 19 November update adds an Elite-style key layout, chosen by pressing K on the launchpad:

- **S** pitch down
- **X** pull up
- **<** and **>** rotate
- **A** fire
- **Space** thrust
- **?** hover

**J** returns to mouse control.

Moxon wrote that the motivation came from ABUG South, where people found the BBC Master key controls of the ARM Evaluation System version of Lander easy to use, so he brought that code into the original.

## RISC OS layout (20 November)

The 20 November update, requested by Ian Jeffray, adds a more typical RISC OS layout chosen with **L**:

- **"** pitch down
- **?** pull up
- **Z** and **X** rotate
- **Return** fire
- **Space** thrust
- **Left Shift** hover

**Y** inverts the y-axis and **U** restores it. Option keys now beep to confirm. The disc also gains a `!ReadMe`.

## Playing it

The game can be played in the browser on Archimedes Live at 12×10 (ARM2), 19×19 (ARM3), 64×64 (Risc PC) or 121×121 (Pi) settings. The two largest run slowly because the fastest Archimedes Live machine is an A5000. Alternatively, download the ADFS disc image, or build from the [`big-landscape` branch](https://github.com/markmoxon/lander-source-code-acorn-archimedes/tree/big-landscape) of the source repository.
