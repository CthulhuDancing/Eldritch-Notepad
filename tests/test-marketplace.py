import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AGENTS_MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"
CLAUDE_MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"

SEMVER = re.compile(
    r"^(0|[1-9]\d*)\."
    r"(0|[1-9]\d*)\."
    r"(0|[1-9]\d*)"
    r"(?:-[0-9A-Za-z.-]+)?"
    r"(?:\+[0-9A-Za-z.-]+)?$"
)

errors = []


def fail(message):
    """Hard stop when validation cannot continue."""
    print(f"FAIL: {message}")
    sys.exit(1)


def error(message):
    """Record a validation failure and continue checking."""
    errors.append(message)


def display_path(path):
    return path.relative_to(ROOT)


def load_json(path):
    if not path.is_file():
        raise ValueError(f"Missing file: {display_path(path)}")

    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {display_path(path)}: {exc}")


def load_marketplace(path):
    try:
        marketplace = load_json(path)
    except ValueError as exc:
        fail(str(exc))

    label = str(display_path(path))
    if not isinstance(marketplace, dict):
        fail(f"{label}: marketplace must contain an object")

    plugins = marketplace.get("plugins")
    if not isinstance(plugins, list):
        fail(f"{label}: marketplace must contain a plugins array")
    if not plugins:
        fail(f"{label}: marketplace contains no plugins")

    return plugins


def resolve_plugin_dir(relative_path, label):
    if not isinstance(relative_path, str) or not relative_path.startswith("./"):
        error(f"{label}: source path must begin with './'")
        return None

    plugin_dir = (ROOT / relative_path).resolve()
    try:
        plugin_dir.relative_to(ROOT)
    except ValueError:
        error(f"{label}: source path escapes repository root")
        return None

    if not plugin_dir.is_dir():
        error(f"{label}: plugin directory does not exist: {relative_path}")
        return None

    return plugin_dir


def load_manifest(path, label):
    try:
        manifest = load_json(path)
    except ValueError as exc:
        error(f"{label}: {exc}")
        return None

    if not isinstance(manifest, dict):
        error(f"{label}: {display_path(path)} must contain an object")
        return None

    return manifest


def check_name(entry, index, seen_names, marketplace_label):
    label = f"{marketplace_label} plugins[{index}]"
    if not isinstance(entry, dict):
        error(f"{label}: entry must be an object, got {type(entry).__name__}")
        return None

    name = entry.get("name")
    if not isinstance(name, str) or not name:
        error(f"{label}: missing a valid name")
        return None

    if name in seen_names:
        error(f"{marketplace_label} {name}: duplicate plugin name")
    seen_names.add(name)
    return name


def check_skills(plugin_dir, label):
    skills_dir = plugin_dir / "skills"
    if not skills_dir.exists():
        return
    if not skills_dir.is_dir():
        error(f"{label}: skills exists but is not a directory")
        return

    for skill_dir in sorted(skills_dir.iterdir()):
        if skill_dir.is_dir() and not (skill_dir / "SKILL.md").is_file():
            error(f"{label}: skill '{skill_dir.name}' does not contain SKILL.md")


def check_agents_plugins(entries):
    seen_names = set()
    plugins = {}
    marketplace_label = str(display_path(AGENTS_MARKETPLACE))

    for index, entry in enumerate(entries):
        name = check_name(entry, index, seen_names, marketplace_label)
        if name is None:
            continue

        label = f"{marketplace_label} {name}"
        source = entry.get("source")
        if not isinstance(source, dict):
            error(f"{label}: missing source configuration")
            continue
        if source.get("source") != "local":
            error(f"{label}: expected local source")
            continue

        plugin_dir = resolve_plugin_dir(source.get("path"), label)
        if plugin_dir is None:
            continue

        manifest = load_manifest(plugin_dir / "plugin.json", label)
        if manifest is None:
            continue

        if manifest.get("name") != name:
            error(
                f"{label}: marketplace name does not match plugin.json name "
                f"'{manifest.get('name')}'"
            )
        if not isinstance(manifest.get("$schema"), str) or not manifest["$schema"]:
            error(f"{label}: plugin.json is missing $schema")

        version = manifest.get("version")
        if not isinstance(version, str) or not SEMVER.fullmatch(version):
            error(f"{label}: invalid semantic version '{version}'")

        check_skills(plugin_dir, label)
        plugins[name] = (plugin_dir, manifest)

    return plugins


def check_claude_plugins(entries, agents_plugins):
    seen_names = set()
    claude_names = set()
    marketplace_label = str(display_path(CLAUDE_MARKETPLACE))

    for index, entry in enumerate(entries):
        name = check_name(entry, index, seen_names, marketplace_label)
        if name is None:
            continue
        claude_names.add(name)

        label = f"{marketplace_label} {name}"
        plugin_dir = resolve_plugin_dir(entry.get("source"), label)
        if plugin_dir is None:
            continue

        manifest = load_manifest(plugin_dir / ".claude-plugin" / "plugin.json", label)
        if manifest is None:
            continue
        if manifest.get("name") != name:
            error(
                f"{label}: marketplace name does not match Claude manifest name "
                f"'{manifest.get('name')}'"
            )

        version = manifest.get("version")
        if not isinstance(version, str) or not SEMVER.fullmatch(version):
            error(f"{label}: invalid semantic version '{version}'")

        agents_plugin = agents_plugins.get(name)
        if agents_plugin is None:
            error(f"{label}: plugin is missing from {display_path(AGENTS_MARKETPLACE)}")
            continue

        agents_dir, agents_manifest = agents_plugin
        if agents_dir != plugin_dir:
            error(f"{label}: marketplace source paths do not resolve to the same plugin")
        if agents_manifest.get("version") != version:
            error(
                f"{label}: manifest version '{version}' does not match portable "
                f"manifest version '{agents_manifest.get('version')}'"
            )

    missing_from_claude = set(agents_plugins) - claude_names
    for name in sorted(missing_from_claude):
        error(f"{name}: plugin is missing from {marketplace_label}")


def main():
    agents_entries = load_marketplace(AGENTS_MARKETPLACE)
    claude_entries = load_marketplace(CLAUDE_MARKETPLACE)

    agents_plugins = check_agents_plugins(agents_entries)
    check_claude_plugins(claude_entries, agents_plugins)

    if errors:
        for message in errors:
            print(f"FAIL: {message}")
        print(f"\n{len(errors)} problem(s) found")
        sys.exit(1)

    print(
        "PASS: marketplace integrity verified for "
        f"{len(agents_plugins)} plugin(s) across 2 formats"
    )


if __name__ == "__main__":
    main()
