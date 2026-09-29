import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"

SEMVER = re.compile(
    r"^(0|[1-9]\d*)\."
    r"(0|[1-9]\d*)\."
    r"(0|[1-9]\d*)"
    r"(?:-[0-9A-Za-z.-]+)?"
    r"(?:\+[0-9A-Za-z.-]+)?$"
)

errors = []

def error(message):
    errors.append(message)

def fail(message):
    print(f"FAIL: {message}")
    sys.exit(1)


def load_json(path):
    if not path.is_file():
        fail(f"Missing file: {path.relative_to(ROOT)}")

    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError as exc:
        fail(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")


def main():
    marketplace = load_json(MARKETPLACE)
    
    plugins = marketplace.get("plugins")

    if not isinstance(plugins, list):
        fail("marketplace.json must contain a plugins array")

    if not plugins:
        fail("marketplace.json contains no plugins")

    seen_names = set()

    for entry in plugins:
        if not isinstance(entry, dict):
            fail(f"Marketplace plugin entry must be an object, got {type(entry).__name__}")
      
        name = entry.get("name")

        if not isinstance(name, str) or not name:
            fail("Marketplace plugin entry is missing a valid name")

        if name in seen_names:
            fail(f"Duplicate marketplace plugin name: {name}")

        seen_names.add(name)

        source = entry.get("source")

        if not isinstance(source, dict):
            fail(f"{name}: missing source configuration")

        if source.get("source") != "local":
            fail(f"{name}: expected local source")

        relative_path = source.get("path")

        if not isinstance(relative_path, str) or not relative_path.startswith("./"):
            fail(f"{name}: source path must begin with './'")

        plugin_dir = (ROOT / relative_path).resolve()

        try:
            plugin_dir.relative_to(ROOT)
        except ValueError:
            fail(f"{name}: source path escapes repository root")

        if not plugin_dir.is_dir():
            fail(f"{name}: plugin directory does not exist: {relative_path}")

        manifest_path = plugin_dir / "plugin.json"
        manifest = load_json(manifest_path)

        manifest_name = manifest.get("name")

        if manifest_name != name:
            fail(
                f"{name}: marketplace name does not match "
                f"plugin.json name '{manifest_name}'"
            )

        schema = manifest.get("$schema")

        if not isinstance(schema, str) or not schema:
            fail(f"{name}: plugin.json is missing $schema")

        version = manifest.get("version")

        if not isinstance(version, str) or not SEMVER.fullmatch(version):
            fail(f"{name}: invalid semantic version '{version}'")

        skills_dir = plugin_dir / "skills"

        if skills_dir.exists():
            if not skills_dir.is_dir():
                fail(f"{name}: skills exists but is not a directory")

            for skill_dir in skills_dir.iterdir():
                if not skill_dir.is_dir():
                    continue

                skill_file = skill_dir / "SKILL.md"

                if not skill_file.is_file():
                    fail(
                        f"{name}: skill '{skill_dir.name}' "
                        "does not contain SKILL.md"
                    )

    print(
        f"PASS: marketplace integrity verified "
        f"for {len(plugins)} plugin(s)"
    )


if __name__ == "__main__":
    main()
