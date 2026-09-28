# Testing Criteria

## Prompt Tests

### Plugin Health Report

This test should report all plugins available, with all of each plugin's skills visible. Ensure that runtime / environment / account problems are not the problem. Skill testing should only confirm availability of each plugin and its related resources for it to pass.

**Fail:** plugins or skills fail to load.

**Pass:** chat runtime sees the plugins and their bundled skills, tools, and connectors.

**Current plugins:**
- project-workflow-tools
