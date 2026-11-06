---
layout: post
title: "Lumen Photo Library and Editor Released for RISC OS"
date: 2026-11-06 08:00:00 +0000
summary: "New photo management and editing application brings non-destructive editing, smart albums, camera raw support, and professional-grade adjustments to RISC OS 5."
tags: [software, multimedia]
source_url: "https://www.riscosopen.org/forum/forums/1/topics/20646"
source_name: "RISC OS Open Forums"
image: /assets/images/lumen-all-photos.png
image_alt: "Lumen's browser window showing a library of photos"
---

Andrew Youll has announced the first public release of Lumen, a photo library and non-destructive editor for RISC OS 5. Released on 4 November 2026 as version 0.0.36, the application provides comprehensive tools for organising and editing photographs without altering the original files.

Lumen combines browsing, viewing, split view, and full screen capabilities in a single window, with an inspector panel alongside. The application maintains photos in a library structure while leaving original files unchanged. It automatically tracks when files are moved, locating them again, and can monitor folders to detect newly added photos.

[![Lumen's browser window showing a library of photos]({{ '/assets/images/lumen-all-photos.png' | relative_url }}){: width="1100" height="679" loading="lazy"}]({{ '/assets/images/lumen-all-photos.png' | relative_url }})

*Lumen's browser window showing a library of photos. Screenshot from the [Lumen user guide](https://raw.githubusercontent.com/adyoull/riscos-lumen/v0.0.36/docs/guide/images/all-photos.png); the photos are the author's own.*

## Organisation and Workflow

The software supports multiple organisation methods including projects (one per imported folder), albums, smart albums, and stacks. Photos can be marked with stars, flags, reject markers, colour labels, captions, keywords, and ratings. A search function and rating filter help locate specific images quickly.

The viewer displays individual photos at full size or at 100 percent magnification, with a round loupe tool available for detailed inspection. All image adjustments are processed in 16-bit linear light, preserving image quality throughout the editing workflow.

## Editing Capabilities

Lumen provides an extensive set of adjustment tools including white balance with an eyedropper tool, exposure, highlights and shadows, levels, curves, contrast, saturation, and vibrancy controls. Colour can be adjusted by individual hue, and split toning is supported. Technical enhancements include noise reduction, sharpening, vignette, and glow effects.

Geometric corrections include crop, straighten, and perspective adjustments. Retouching tools and brushes allow for detailed corrections. The software includes undo and redo functions, before and after comparison, an Auto adjustment feature, presets, versions support, and fifteen built-in styles.

## Export and Format Support

Photos can be exported as JPEG or PNG at any size, with colour space options including sRGB, Adobe RGB, and Display P3. Camera metadata, captions, and keywords are preserved during export. The application supports printing to any RISC OS printer and can export, import, check, and repair complete photo libraries.

Camera raw file support is available through the optional LumenRaw plug-in, which uses LibRaw to support over a thousand camera models. Lumen maintains a working-size preview of each raw file for immediate loading. On the same day as the initial release, version 0.0.37 introduced a formalised and versioned plug-in API, documented in the repository. This update also included LumenHEIF 1.1, the first format plug-in, which reads HEIF photos from iPhones and many Android phones, as well as AVIF images.

## Requirements and Availability

Lumen requires RISC OS 5.30 or later and has been tested on RISC OS 5.31 running on Raspberry Pi 4, as well as RISC OS running on Linux. Other ARMv7 machines with VFPv3 should be compatible but remain untested. The application depends on SharedUnixLibrary 1.16 or later and ARMEABISupport, both of which PackMan can install automatically.

The software is available through PackMan as separate Lumen and LumenRaw packages, or as a zip file of approximately 22 megabytes including the user guide from the [GitHub release page](https://github.com/adyoull/riscos-lumen/releases/tag/v0.0.36). Source code is available at the [GitHub repository](https://github.com/adyoull/riscos-lumen) under the MIT licence. Version 0.0.37 can be found at its [release page](https://github.com/adyoull/riscos-lumen/releases/tag/v0.0.37).

Youll notes that the code, build scripts, and documentation were written with Anthropic's Claude as a coding assistant. He cites his interest in photography and inspiration from Apple Aperture as influences on the project. Forum reaction has been positive, with Andrew Rawnsley describing it as one of his desired RISC OS applications.

Current limitations include the absence of slideshow functionality and IPTC metadata support, and raw file export remains relatively slow.
