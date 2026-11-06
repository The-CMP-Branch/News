---
layout: post
title: "ROOL GitLab Server Upgraded Following Security Vulnerability"
date: 2026-11-06 08:15:00 +0000
summary: "RISC OS Open Ltd accelerated a planned GitLab upgrade after disclosure of a maximum-severity remote code execution vulnerability affecting twelve years of releases."
tags: [security, community]
source_url: "https://www.riscosopen.org/forum/forums/1/topics/20625"
source_name: "RISC OS Open Forums"
---

RISC OS Open Ltd (ROOL) brought forward a planned upgrade of its GitLab server following the disclosure of a maximum-severity remote code execution vulnerability. James Byrne announced on 25 October 2026 that the existing server was exposed to automated attacks due to the security flaw.

The vulnerability, identified as CVE-2026-110264, was reported by The Register on 22 October 2026 in an article detailing its impact across [more than twelve years of GitLab releases](https://www.theregister.com/security/2026/10/22/max-severity-gitlab-bug-allows-remote-code-execution-over-12-years-of-releases/5304854). To address the exposure, ROOL temporarily restricted access to the server while performing the upgrade, which was expected to require two to three days. Users requiring access during the maintenance window were directed to contact ROOL via the Code Submissions email address.

## Upgrade Completed

The server returned to service on 30 October running the latest GitLab version. The upgrade introduced significant changes to the user interface. Continuous integration jobs were temporarily suspended while the CI infrastructure was restored.

## Access Changes

The updated GitLab installation no longer accepts SHA1-based RSA SSH keys. Users with older accounts who experience difficulties fetching or pushing over SSH need to generate and register a new key. Problems should be reported to ROOL's Code Submissions email address or posted in the Community Support forum.

## Git Client Update

On 4 November, the RISC OS Git Client was updated to version 0.13, available as a [direct download](https://www.riscosopen.org/zipfiles/platform/common/GitClient.0.13.zip). This update resolves SSH fetch problems when connecting to the upgraded server. The same issue may affect older versions of TortoiseGit on Windows systems, which may also require updating.

The upgrade ensures that ROOL's development infrastructure remains secure for the RISC OS development community while maintaining access to the source code repositories.
