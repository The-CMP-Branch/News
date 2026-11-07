---
layout: post
title: "ODBC Database Tools Updated with New Drivers and Enhanced SQLTool"
date: 2026-11-07 07:05:00 +0000
summary: "Richard Windley has released updates to RISC OS ODBC tools including new driver manager and database drivers, plus SQLTool gains an editable results grid, syntax colouring, and entity relationship diagram generator."
tags: [software, database, development]
source_url: "https://www.riscosopen.org/forum/forums/1/topics/20640"
source_name: "RISC OS Open Forums"
---

Richard Windley of The Really Small Software Company has released a major update to the ODBC database tools for RISC OS, completing his recent software updates. The release includes a new version of the ODBC driver manager, updated drivers for PostgreSQL, MySQL, SQLite and FreeTDS (Microsoft SQL Server), and a recent port of the SQLite database itself to support the SQLite ODBC driver.

The headline improvements come to SQLTool, which provides a graphical interface for running SQL queries against any ODBC-compatible database. The results grid is now editable, the SQL editor gains syntax colouring and completion, and the tool can display keys and indexes. A new entity relationship diagram generator visualises database structure.

The ODBC (Open Database Connectivity) system allows RISC OS applications to connect to both local and remote databases using a standard API. Once a datasource is configured through ODBCMan, any ODBC-compliant application can access the database transparently, whether it runs on the local machine or a remote server. The ODBCLib library is available for developers writing C code that needs database access.

In a forum exchange, Richard confirmed that users can employ SQLTool as a front end for SQLite or MySQL databases running entirely on RISC OS, or query remote servers such as PostgreSQL. He noted that performance is modest and datasource setup can require some care, with security settings sometimes needing adjustment to simpler authentication methods. His own website uses a templating application written in RISC OS that stores templates and content in a PostgreSQL database.

The ODBC tools are available from [The Really Small Software Company's ODBC page](https://www.reallysmall.co.uk/Pages/categories/riscos/database/odbc.php), which also provides documentation on the driver manager, ODBCMan, SQLTool and the available drivers. Discussion continues in the [forum announcement thread](https://www.riscosopen.org/forum/forums/1/topics/20640).
