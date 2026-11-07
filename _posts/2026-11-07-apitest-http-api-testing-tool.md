---
layout: post
title: "APITest Brings HTTP API Testing to RISC OS"
date: 2026-11-07 07:10:00 +0000
summary: "Richard Windley has released APITest, an early-release tool for testing HTTP APIs that supports all common methods, request bodies, syntax-coloured responses and reusable collections with shared variables."
tags: [software, development, networking]
source_url: "https://www.riscosopen.org/forum/forums/1/topics/20643"
source_name: "RISC OS Open Forums"
---

Richard Windley of The Really Small Software Company has released APITest, a tool for testing HTTP API endpoints from RISC OS. Describing it as an early release with some rough edges, Windley likens it to a simple version of Postman for those familiar with that application.

APITest allows developers to call API endpoints using all common HTTP methods, including GET, POST, PUT, DELETE and others. Users can specify a request body and visualise responses, with syntax colouring applied where appropriate to make JSON, XML and other structured formats easier to read.

The tool supports collections, which group related API calls together with shared variables and settings. These collections can be reused across individual requests, making it easier to test a complete API or maintain different environments (development, staging, production) with their own base URLs, authentication tokens and other parameters.

Matthew Phillips responded to the announcement with "Nice!", suggesting developer interest in the tool. The software is available from [The Really Small Software Company's APITest page](https://www.reallysmall.co.uk/Pages/categories/riscos/development/apitest.php), with discussion in the [forum announcement thread](https://www.riscosopen.org/forum/forums/1/topics/20643).
