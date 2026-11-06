---
layout: post
title: "WROCC November Meeting Explores Package Managers for RISC OS"
date: 2026-11-06 08:25:00 +0000
summary: "Chris Hughes presents Store and PackMan options for installing RISC OS software, demonstrating dependency resolution and package management from an end-user perspective."
tags: [community, events]
source_url: "https://www.iconbar.com/articles/WROCC_November_2026_meeting_-_Package_managers_with_Chris_Hughes/index2420.html"
source_name: "The Icon Bar"
---

Wakefield RISC OS Computer Club held its November meeting on Wednesday 4 November 2026 at 7.45pm via Zoom, with Chris Hughes presenting on package managers for RISC OS from an end-user perspective. The presentation slides were created in Ovation Pro as an experiment.

Hughes explained that software packaging is commonplace on other platforms, simplifying software installation and automatically resolving dependencies. For RISC OS users, two main options exist: Store and PackMan. Each has distinct characteristics, with PackMan limited to non-commercial software while Store also handles commercial software sales with card payment processing.

## PackMan Overview

PackMan remains technically in beta status. Users not running version 0.9.8 should update, and PackMan includes the capability to update itself. The system creates a Packages directory in Resources and retrieves package lists from configurable sources. Paths determine installation locations.

A substantial collection of free software is accessible through PackMan, including games, browsers, utilities, and fonts. The information window displays package details, installation location, and potential conflicts. Some packages can be installed in any location, while others have fixed paths. PackMan also provides facilities for updating and removing installed software.

Hughes demonstrated installing Iris, which requires numerous dependencies that PackMan handles automatically. He also provided a preview of next month's meeting topic by installing TubeSearch.

## Store and PackMan Comparison

Both systems offer advantages and limitations. Store's support for commercial software with payment processing makes it suitable for paid applications, while PackMan focuses on freely available software with a broader selection in that category.

The meeting was documented in a report by Mark Stephens published on The Icon Bar on 5 November 2026. WROCC had also [posted a public meeting notice](https://www.riscosopen.org/forum/forums/1/topics/20637) on 4 November on the RISC OS Open forum, titled Software Packaging from an end-user's perspective.

A video recording of the presentation is expected to be published on the [WROCC meetings page](https://www.wrocc.org.uk/meetings).
