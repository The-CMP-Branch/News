---
layout: post
title: "RISC OS Open Publishes RISC OS Coding Guidelines, Including AI-Assisted Contributions"
date: 2026-11-21 17:00:00 +0000
summary: "RISC OS Open has published coding guidelines for contributors to its source tree, covering style, licensing, allocated names and numbers, and how AI-assisted code should be declared and reviewed."
tags: [rool, development, guidelines]
source_url: "https://www.riscosopen.org/content/documents/risc-os-coding-guidelines"
source_name: "RISC OS Open"
---

RISC OS Open has published a set of [RISC OS Coding Guidelines](https://www.riscosopen.org/content/documents/risc-os-coding-guidelines) for developers changing or submitting components to its source tree, and for anyone else who wants their RISC OS code to read the same way. Steve Revill announced them on 21 November 2026 in the Code review forum topic [ROOL coding guidelines](https://www.riscosopen.org/forum/forums/3/topics/20682). He said the guidelines are meant to help developers engage with RISC OS Open and get their work through review, to give advice on how things are normally done in the RISC OS codebase, and to set out ROOL's guidance on using AI tools when developing RISC OS components. Constructive feedback is welcome.

The main page is a short set of requirements, marked *must* and *must not*, that merge requests are typically rejected for. A [good practice](https://www.riscosopen.org/content/documents/risc-os-coding-guidelines/good-practice) guide then covers recommendations for any language, and there are separate pages per language. A component's own established conventions take precedence over the good-practice and language guides. A small fix often needs little more than following the requirements and matching the style of the file being edited.

## Requirements

Changes must follow the conventions of the component they touch (indentation, braces, naming, comment form, layout), or of the file being edited where the component is inconsistent. They must not reformat code they do not otherwise change: a reformat hides the real work and breaks `git blame` and open merge requests. A wholesale reformat of an old component is sometimes appropriate, but it must be agreed with RISC OS Open first and committed on its own, changing nothing but the formatting, so a reviewer can check that the result is binary identical.

Every source file must start with a licence header, either in full or as an SPDX identifier. Files delivered to the user, typically those in `Resources`, are excepted. The licence and copyright line of a file the contributor did not write must not be changed.

Code imported from elsewhere must be under a licence the tree can carry. Permissive licences such as Apache 2.0, MIT, BSD and zlib can; so can the LGPL where its relinking terms are met. GPL code must not go into the OS, because anyone redistributing the image would then have to do so under the GPL, which the rest of the image's licences do not allow. Code of unknown licence is also excluded. The vendor's licence text, copyright notices, any `NOTICE` file, and the vendor's formatting must be left intact.

[SWI chunks, error blocks, service calls, filetypes and other quantities that RISC OS Open allocates](https://www.riscosopen.org/content/allocate) must be registered before the software is released. Placeholders are fine during development. `VersionNum` and `VersionASM` must not be edited by hand; RISC OS Open's tooling maintains them when changes are merged. A password, key or token must not be printed, logged, written to a file or committed, including in debug output.

## AI-assisted contributions

AI-assisted code is welcome on the same terms as any other, with four extra conditions that a reviewer cannot check from the diff alone:

1. The merge request must declare which parts an AI tool wrote, and which tool.
2. A named person must be accountable: they understand the code well enough to answer for it in review, as they would for their own work, and will maintain it afterwards or say who will.
3. The code must have been tested on RISC OS, on hardware or in emulation, and the merge request must say what was tested and how.
4. Imports must be declared, and other people's software must not be reproduced. Using a tool to reverse-engineer or replicate a specific third-party program is not acceptable. If a merge request is "like X but for RISC OS", it should say so and say what of X was used.

## Good practice and language guides

The good-practice page follows the order a contributor usually meets the work: asking early in the Code review forum, working in a GitLab fork, matching an existing component, laying out a new one as the rest of the tree does, importing third-party code in its own directory, layout (spaces rather than tabs, LF line endings, no trailing whitespace), licence headers and comments, functions, portability, testing, documentation, extra checks when an AI tool has helped, committing, and submitting a merge request.

Separate guides cover [C and C++](https://www.riscosopen.org/content/documents/risc-os-coding-guidelines/c), [Assembler](https://www.riscosopen.org/content/documents/risc-os-coding-guidelines/assembler), [BBC BASIC](https://www.riscosopen.org/content/documents/risc-os-coding-guidelines/basic), [Fortran](https://www.riscosopen.org/content/documents/risc-os-coding-guidelines/fortran), and [Makefiles, Obey and TaskObey files](https://www.riscosopen.org/content/documents/risc-os-coding-guidelines/makefiles).

The guidelines are on [RISC OS Open](https://www.riscosopen.org/content/documents/risc-os-coding-guidelines). Discussion is in the [forum topic](https://www.riscosopen.org/forum/forums/3/topics/20682).
