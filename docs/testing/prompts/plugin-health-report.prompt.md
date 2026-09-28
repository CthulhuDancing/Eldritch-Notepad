---
id: plugin-health-report
title: Plugin Health Report
description: Tests whether each of the marketplace's plugins is available in the current chat runtime and reports its exposed capabilities.
category: plugin-discovery
tags:
  - plugin
  - skills
  - tools
  - availability
version: 1
status: active
---

Attempt to access the following plugins in the current chat runtime:

- `project-workflow-tools`

For each plugin, report its current runtime availability using exactly this table structure:

| Plugin Name | Plugin Discoverable | Available Skills | Available Tools | Available Connections |
|---|---|---|---|---|

Use the following rules:

- `Plugin Discoverable` indicates whether the plugin itself can be identified by the current chat runtime.
- List only skills, tools, and connections that are actually exposed to the current runtime.
- Do not infer capabilities from documentation, prior knowledge, expected repository structure, or plugin naming.
- If a category is discoverable but empty, report `None`.
- If a category cannot be inspected, report `Not discoverable`.
- Do not perform any task using the plugin beyond what is necessary to determine and report its availability.
