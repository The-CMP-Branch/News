---
layout: post
title: "The Really Small Software Company Updates SampleEd, Markdown, Mermaid and Sourcery"
date: 2026-11-07 07:25:00 +0000
summary: "Richard Windley has released updates to his audio, documentation and project management tools, including rebuilt SampleEd with LADSPA plugins, enhanced Mermaid with in-place editing, and Sourcery 1.25 with improved git integration and mass export."
tags: [software, development, multimedia]
source_url: "https://www.riscosopen.org/forum/forums/1/topics/20629"
source_name: "RISC OS Open Forums"
---

Richard Windley of The Really Small Software Company has released a second batch of software updates, covering audio editing, documentation tools and project management. The releases continue his return to RISC OS development after a break, and he acknowledges they are coming out quickly and should be considered alpha or beta quality.

SampleEd, the sound sample editor, has been rebuilt along with related tools including LADSPA, which manages audio plugins. New ports of LADSPA plugins and libsndfile, the library for reading and writing sound files, are also available.

The Markdown and Mermaid tools have been updated, with Mermaid gaining the ability to edit its diagram source in place. Mermaid produces diagrams from text descriptions, supporting flowcharts, sequence diagrams, Gantt charts and other technical documentation formats.

Sourcery, Windley's tool for making RISC OS development easier, has been updated to version 1.25 with several major features. A new export window enables mass export of projects for distribution, with consistent and templated naming of archive files. The software also includes the beginnings of integration with ROBE (RISC OS Build Environment), allowing 64-bit versions of projects to be built from within Sourcery itself.

The most significant change in Sourcery 1.25 is improved git integration. According to the upgrade instructions, some settings have changed and existing users should read them carefully. The manual has been updated, though Windley notes the documentation was written quickly. He reports that git integration works well on RISC OS 5 based on his testing, but he has been unable to get the git client to function on RISC OS 6, which may be a documented limitation he is unaware of. Steve Pampling suggested this could be related to SSL setup changes, noting that SSL3 is deprecated and modern systems require TLS 1.2 or 1.3, whereas RISC OS 6 was developed when SSL3 was still current.

Windley's previous announcement covered Grimoire, his programmer's editor with syntax colouring and code completion for over twenty languages, which [received a significant update to version 1.15](https://www.riscosopen.org/forum/forums/1/topics/20650) on 6th November. Sourcery works best with Grimoire when editing C or C++ files, pulling completion and parameter hinting from include files associated with the project.

The updated software is available from [The Really Small Software Company](https://www.reallysmall.co.uk/), with discussion in the [forum announcement thread](https://www.riscosopen.org/forum/forums/1/topics/20629).
