---
layout: post
title: "Bluetooth for RISC OS 1.03 Adds Built-in Radio Support on Raspberry Pi 4 and CM4"
date: 2026-11-18 16:55:00 +0000
summary: "RISC OS Technologies has released Bluetooth for RISC OS 1.03, adding support for the Raspberry Pi 4, Pi 400 and CM4 built-in Bluetooth radios so a USB dongle is no longer required on those boards, and refreshing the USB drivers used on Titanium."
tags: [software, hardware, raspberry-pi]
source_url: "https://www.riscosopen.org/forum/forums/5/topics/14934"
source_name: "RISC OS Open Forums"
---

RISC OS Technologies has released Bluetooth for RISC OS 1.03, a Bluetooth host stack for 32-bit RISC OS 5. Martin Eastwood posted on 18 November 2026 in the RISC OS Open [Bluetooth](https://www.riscosopen.org/forum/forums/5/topics/14934) topic that it had received a version bump adding Pi 4 and CM4 radio support, and updated USB drivers for the Titanium.

The current version in the [Bluetooth-RISCOS32](https://github.com/riscostechnologies/Bluetooth-RISCOS32) GitHub repository, and as a zip on the RISC OS Technologies [miscellaneous downloads](https://www.riscostechnologies.co.uk/content/downloads/miscellaneous) page, is 1.03, dated 18 November 2026.

## Raspberry Pi built-in radio

Version 1.02 adds a RISC OS 5 backend for the Raspberry Pi's own Bluetooth radio, so a USB dongle is no longer required on the boards that have one. The README lists Raspberry Pi 4, Pi 400 and Compute Module 4, using the built-in Broadcom BCM4345C0 on PL011 UART0. When no USB adapter is present, the stack can use that radio instead.

The Pi controller needs a legally obtained `BCM4345C0` HCD patch in `!Bluetooth.Firmware`. That file is not included in the source or the installer. The README also notes that this new transport still needs hardware smoke testing.

The Pi backend (`port/c/ro5_bridge`) is adapted from the Phoenix RISC OS project's BluetoothVoice-ro5 contribution, under the MIT licence.

## Titanium USB drivers

Version 1.03 refreshes the USB path used with a passed-through USB adapter on Titanium. That setup needs USBDriver 1.35 or later. `!Bluetooth` detects an insufficient driver and offers the bundled update. Accepting it restarts USBDriver and XHCIDriver, so keyboards, mice and USB storage may be unavailable briefly.

## What the stack already does

The stack plays the computer's sound through Bluetooth speakers and headphones (A2DP, SBC) and works with Bluetooth mice and keyboards, both classic HID and Low Energy (HID over GATT, with LE Secure Connections pairing). Paired devices reconnect at start-up and when they wake.

USB adapters such as the TP-Link UB400 (CSR8510) and the UB4A or UB500 (RTL8761B) remain supported; Realtek firmware is included. The Pinebook Pro's built-in Bluetooth, added in [Bluetooth 0.94](https://www.riscostechnologies.co.uk/news/articles/2026/10/27/bluetooth-0-94-adds-pinebook-pro-internal-bluetooth-support) on 27 October 2026, is still listed. RISC OS Technologies [open-sourced the stack](https://www.riscostechnologies.co.uk/news/articles/2026/10/26/bluetooth-stack-for-risc-os-5-is-open-source) on 26 October 2026.

Headset microphones (HFP) are not supported in this version. The installer ReadMe reports testing on a Raspberry Pi CM4 under RISC OS 5.31 with a TP-Link UB400. SharedUnixLibrary 1.16 or later is required; a copy is included.

## Installing

[Bluetooth-1.03.zip](https://www.riscostechnologies.co.uk/downloads/Bluetooth-1.03.zip) (533 KB) is on the RISC OS Technologies miscellaneous downloads page. Unpack it on RISC OS, double-click `!Install` and click Install. Source is in the [Bluetooth-RISCOS32](https://github.com/riscostechnologies/Bluetooth-RISCOS32) repository, under a BSD 2-Clause licence.

Discussion continues in the [forum thread](https://www.riscosopen.org/forum/forums/5/topics/14934).
