---
layout: post
title: "RISC OS Open Publishes a Continuous Integration Guide for Contributors"
date: 2026-11-24 17:00:00 +0000
summary: "RISC OS Open has added a Continuous Integration page to its coding guidelines, explaining how GitLab CI checks each change before a person reviews it. Steve Revill notes that the page is a working draft and may change."
tags: [rool, development, guidelines]
source_url: "https://www.riscosopen.org/content/documents/risc-os-coding-guidelines/ci"
source_name: "RISC OS Open"
---

RISC OS Open has added a [Continuous Integration](https://www.riscosopen.org/content/documents/risc-os-coding-guidelines/ci) page to its RISC OS Coding Guidelines. Steve Revill announced it on 24 November 2026 in the Code review forum topic [ROOL coding guidelines](https://www.riscosopen.org/forum/forums/3/topics/20682): "We now have a CI page – but note that this is a working draft and subject to change!" Earlier in that topic he had said ROOL would look at putting a little more in around merge requests and CI. This site covered the [coding guidelines]({{ '/2026/11/21/rool-coding-guidelines/' | relative_url }}) when they were published on 21 November 2026.

## How the CI works

ROOL's GitLab CI checks each change to a component before a person reviews it. It runs on a contributor's fork whenever they push, and again on the merge request. In both places the results appear under Build, then Pipelines. Many components already use it.

Enabling it on a typical component already in the tree needs one small `.gitlab-ci.yml` file at the component's root. That file includes the component's jobs from the Support/CI project, from a file named after the last part of the component's GitLab path. For FileSwitch, whose path is `RiscOS/Sources/FileSys/FileSwitch`, the example includes `/FileSwitch.yml` from Support/CI.

The page then lists four steps:

1. Add a `.gitlab-ci.yml` file of that form at the component's root.
2. Commit the file and push the branch to the fork. A pipeline starts immediately.
3. Correct whatever the pipeline reports, in the same commit or an earlier one. In a component that has not used CI before, the jobs usually report a missing `.gitattributes` file, `.gitignore` file or licence file.
4. Submit the merge request once the pipeline passes.

The jobs are generated centrally from the build system's ModuleDB and components files, and held in Support/CI. Each component's `.gitlab-ci.yml` refers to them indirectly, so RISC OS Open can change the jobs across the whole tree without a commit to every component. Most jobs check only the changes a branch makes, not the component's files as a whole, so a component with existing problems can enable CI without first correcting them. The included jobs should be left as they are. A change to them can be proposed on the Support/CI_Source project. RISC OS Open configures any exemption that applies to a whole component, such as disabling a job.

## Why the jobs exist

The jobs a component receives depend on its ModuleDB entry and change over time, so the guide explains what they are for rather than listing every check:

- **Real names.** Commits must carry the author's and committer's real names so that each change can be audited. A merge request page shows GitLab usernames instead, so the CI reads the names from the commits before the merge.
- **Version numbers.** A component normally keeps its version in a standard `VersionNum` file, which RISC OS Open's tools increment when a merge request is accepted. If that file is missing or non-standard, each commit message must say how the change is to be tagged.
- **Copyright notices and licence files.** Every source file must show the terms it can be distributed under. The CI looks for a copyright notice, and a licence file at the component's root, such as `LICENSE` or `COPYING`, covers the component as a whole.
- **Language attributes.** RISC OS source files have no extensions, so GitLab cannot guess the language from a name. A `.gitattributes` file records the language of each source directory and typed file so that highlighting works.
- **Ignored files.** A `.gitignore` file lists the object files, binaries and dependency files a build leaves behind, so they cannot be committed by mistake.
- **Makefiles.** Recipe lines must start with a tab: GNU make on Linux does not accept the spaces that the DDE's amu allows, so the cross-build would fail. Makefiles must also omit the dynamic dependencies amu appends, which record paths on the machine that built the component and mean nothing elsewhere.
- **Whitespace and cppcheck.** The CI flags whitespace errors of the kind `git diff --check` finds, and any new diagnostics from cppcheck, a static analyser for C.
- **Imported source.** Code brought in from another project is left as its authors wrote it, whitespace errors included, so later versions from that project can still be merged easily.
- **Building.** The component is built against an overnight copy of the whole tree, and the result is attached to the pipeline so reviewers and testers can try the change from the merge request page.

The page also covers what to do when a job fails, including how to correct a commit message or a name and how to exempt a file from the whitespace or cppcheck job where there is good reason. A component can add jobs of its own after the `include` — regression tests in particular are welcome — though until RISC OS Open has GitLab runners on RISC OS machines those jobs are limited to what can be built and run on Linux. A further section explains how to try most of the same jobs on a new component that is not yet in the build, by generating them from Support/CI_Source for the time being.

## Early feedback

In the same forum topic on 24 November, Marc Warne said he enabled CI on the Serial component on a scratch branch and the pipeline ran first time, with eight of ten jobs green. The softload job caught a case-sensitivity problem (`Hdr:OSBytes` versus the exported `OsBytes`) that one of his open merge requests already fixes.

The CI page is a working draft and is subject to change. It is on [RISC OS Open](https://www.riscosopen.org/content/documents/risc-os-coding-guidelines/ci). Discussion is in the [forum topic](https://www.riscosopen.org/forum/forums/3/topics/20682).
