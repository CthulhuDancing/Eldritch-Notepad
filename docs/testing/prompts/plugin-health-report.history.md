# Runtime Test History

## 1.3.0

### Claude 

#### Dev notes

Soft failure. Skills appeared but plugin was not discoverable. Refine prompting.

#### Raw Response

`project-workflow-tools` is identifiable only through its two skills in the runtime; it has no catalog entry, and I can't inspect its tools or connections.

| Plugin Name | Plugin Discoverable | Available Skills | Available Tools | Available Connections |
|---|---|---|---|---|
| project-workflow-tools | Partially: not found in the plugin catalog search, but two skills are exposed under its namespace | `project-workflow-tools:adaptive-workflow`, `project-workflow-tools:structured-handoff` | None | Not discoverable |

- **Catalog search:** it returned ten similarly themed plugins, such as `agent-handoff`, `workflow-toolkit` and `handoff`, but none named `project-workflow-tools`.
- **Skills:** the two listed are the only ones in the runtime's skill list carrying that prefix.
- **Tools:** none of the callable tools in this session are tied to the plugin.
- **Connections:** nothing in the runtime lets me inspect connections per plugin, so I can't say whether it has any.

### Codex

#### Dev notes
Codex can see the skills and its in a format that is expected. Perhaps the problem with visibility of plugin is the marketplace.json or plugin.json for claude.

#### Raw Response

| Plugin Name | Plugin Discoverable | Available Skills | Available Tools | Available Connections |
|---|---|---|---|---|
| project-workflow-tools | Yes | `adaptive-workflow`, `structured-handoff` | None | Not discoverable |

### ChatGPT

#### Dev Notes
I'm gonna blow a gasket. This has been plaguing me and I think it's an openai problem at this point so we will see if it improves later. For now, I will install the skills directly to test them in ChatGPT

#### Raw Response

| Plugin Name | Plugin Discoverable | Available Skills | Available Tools | Available Connections |
|---|---|---|---|---|
| `project-workflow-tools` | Yes | None | None | Not discoverable |
