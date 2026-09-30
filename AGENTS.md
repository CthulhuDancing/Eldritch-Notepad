# Repository Instructions

## Purpose

Eldritch Notepad is a provider-portable plugin marketplace for non-technical
users. Keep shared plugin and skill content useful across ChatGPT, Codex,
Claude, and Claude Code.

## Important Files

- `.agents/plugins/marketplace.json`: agent plugin marketplace catalog.
- `.claude-plugin/marketplace.json`: Claude plugin marketplace catalog.
- `plugins/*/plugin.json`: portable agent plugin manifests.
- `plugins/*/.claude-plugin/plugin.json`: Claude plugin manifests.
- `plugins/*/skills/*/SKILL.md`: user-facing skill instructions.

## Development

- Use Python 3.12. The repository currently has no third-party dependencies.
- Run `make check` after changing marketplace or plugin manifests, test code,
  or skill directories.
- Keep user-facing instructions concise, human-readable, and
  provider-agnostic.
- Keep skill frontmatter descriptions focused on when the skill should be
  invoked; do not put rules or checklists in descriptions.

## Releases and Documentation

- Keep both marketplace formats and both plugin manifest formats synchronized.
- Keep plugin versions valid semantic versions and synchronized across each
  plugin's portable and Claude manifests.
- Update `docs/VersionHistory.md` for releases.
- Record durable architectural decisions in `docs/Decisions.md`.

