# Testing Inventory

# Prompt Tests

### Plugin Health Report
**ID:** plugin-health-report

`prompts/plugin-health-report.prompt.md` Tests basic reachability of plugins and skills. Add each new plugin directly to the prompt file as they are built.

**Current plugins**
1. project-workflow-tools

**Outcomes**
- **Pass:** chat runtime sees the plugins and their bundled skills, tools, and connectors.
- **Fail:** plugins or skills fail to load in the chat runtime.


## Deterministic Tests



## Marketplace Tests

### Marketplace Integrity
**ID:** marketplace-integrity

`tests/test-marketplace.py` validates both marketplace formats, their local
plugin sources, portable and Claude plugin manifests, semantic versions, and
skill entry points. It also checks that corresponding plugin names, source
directories, and versions remain synchronized.

**Outcomes**
- **Pass:** both marketplace formats describe the same valid local plugins.
- **Fail:** a marketplace, manifest, source directory, version, or skill entry
  point is missing, invalid, unsafe, or inconsistent.
