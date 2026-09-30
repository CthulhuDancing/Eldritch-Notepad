# Eldritch-Notepad
a collection of plugins for non-technical users engaging in agentic workflows.

### Current Version - 0.2.0
This version initializes a simple test for marketplace plugin validation.

version history is [here](docs/VersionHistory.md)

## Development environment

Development and CI use Python 3.12. The repository currently has no
third-party dependencies, required environment variables, or secrets.

Run the complete local validation suite with:

```sh
make check
```


# Plugin Directory

## Project Workflow Tools
The purpose of this plugin is to help agents adapt plans as new information changes the problem. It helps agents better understand things like implicit intent, long horizon tasks, and navigating complex objectives. It also instructs them to produce a more consistent output.

**Skills:** 
- `adaptive-workflow` - Structure complex, uncertain, or multi-step work as an adaptive workflow.
- `structured-handoff` - Produce a concise, structured handoff that preserves the context needed for another actor or chat.
