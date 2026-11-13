#!/usr/bin/env python3
"""Validate the harness: frontmatter, cross-references, README/agent consistency, settings."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILTIN_AGENTS = {"Explore", "general-purpose", "Plan"}
MODELS = {"opus", "sonnet", "haiku", "inherit"}
errors: list[str] = []


def err(path: Path, msg: str) -> None:
    errors.append(f"{path.relative_to(ROOT)}: {msg}")


def frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not match:
        err(path, "missing or unterminated frontmatter")
        return {}, text
    fields = {}
    for line in match.group(1).splitlines():
        key, sep, value = line.partition(":")
        if not sep or not key.strip():
            err(path, f"malformed frontmatter line: {line!r}")
            continue
        fields[key.strip()] = value.strip()
    return fields, match.group(2)


def require(path: Path, fields: dict[str, str], keys: list[str]) -> None:
    for key in keys:
        if not fields.get(key):
            err(path, f"frontmatter missing '{key}'")


skill_dirs = sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir() and p.name != "synced")
agent_files = sorted((ROOT / "agents").glob("*.md"))
command_files = sorted((ROOT / "commands").rglob("*.md"))

skills = {p.name for p in skill_dirs}
agents = {p.stem for p in agent_files}
agent_models: dict[str, str] = {}
documents: list[Path] = [ROOT / "CLAUDE.md"]

for directory in skill_dirs:
    path = directory / "SKILL.md"
    if not path.is_file():
        err(directory, "missing SKILL.md")
        continue
    fields, _ = frontmatter(path)
    require(path, fields, ["name", "description"])
    if fields.get("name") and fields["name"] != directory.name:
        err(path, f"name '{fields['name']}' does not match directory '{directory.name}'")
    documents.append(path)

for path in agent_files:
    fields, _ = frontmatter(path)
    require(path, fields, ["name", "description", "tools", "model"])
    if fields.get("name") and fields["name"] != path.stem:
        err(path, f"name '{fields['name']}' does not match filename")
    if fields.get("model") and fields["model"] not in MODELS:
        err(path, f"unknown model '{fields['model']}'")
    agent_models[path.stem] = fields.get("model", "")
    documents.append(path)

for path in command_files:
    fields, _ = frontmatter(path)
    require(path, fields, ["description"])
    documents.append(path)

for path in documents:
    text = path.read_text(encoding="utf-8")
    for name in re.findall(r"`([A-Za-z-]+)` skill\b", text):
        if name not in skills:
            err(path, f"references unknown skill '{name}'")
    for name in re.findall(r"`([A-Za-z-]+)` (?:sub)?agent\b", text):
        if name not in agents | BUILTIN_AGENTS:
            err(path, f"references unknown agent '{name}'")
    for name in re.findall(r"/wf:([a-z-]+)", text):
        if not (ROOT / "commands" / "wf" / f"{name}.md").is_file():
            err(path, f"references unknown command '/wf:{name}'")

readme = ROOT / "README.md"
readme_text = readme.read_text(encoding="utf-8")
for name, model in re.findall(r"^\| `([a-z-]+)` \| (\w+) \|", readme_text, re.M):
    if name not in agent_models:
        err(readme, f"agent table lists unknown agent '{name}'")
    elif agent_models[name] != model:
        err(readme, f"agent table says '{name}' uses {model}, agent file says {agent_models[name]}")
for name in agents:
    if f"`{name}`" not in readme_text:
        err(readme, f"agent '{name}' is not documented")
for name in skills:
    if f"`{name}`" not in readme_text:
        err(readme, f"skill '{name}' is not documented")
for path in command_files:
    if f"/wf:{path.stem}" not in readme_text:
        err(readme, f"command '/wf:{path.stem}' is not documented")

settings = ROOT / "settings.json"
try:
    json.loads(settings.read_text(encoding="utf-8"))
except json.JSONDecodeError as exc:
    err(settings, f"invalid JSON: {exc}")

if errors:
    print("\n".join(errors))
    print(f"\n{len(errors)} problem(s) found")
    sys.exit(1)
print(f"OK: {len(skills)} skills, {len(agents)} agents, {len(command_files)} commands")
