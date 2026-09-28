---
id: plugin-health-report
title: Plugin Health Report
description: Tests whether each of the marketplace's plugins are available in the current chat runtime and reports their exposed capabilities.
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

For each plugin, produce the following tabular output:
Plugin Name | Directory Discoverable | available skills | available tools | available connections

Do not perform any task using the plugin beyond what is necessary to determine and report its availability.
If the plugin, its skills, or its tools cannot be discovered, state that explicitly rather than inferring that they exist.
