#!/usr/bin/env python3
"""Check the project locally. Use --baseline to compare with the original import."""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPLICIT = {
    "grill-with-docs", "handoff", "implement", "implement-spec",
    "improve-codebase-architecture", "init-notion-project", "project-docs",
    "retro", "setup-matt-pocock-skills", "simplify", "teach", "to-notion",
    "to-pm", "triage", "wayfinder",
}
IMPLICIT = {
    "code-review", "codebase-design", "diagnosing-bugs", "domain-modeling",
    "grilling", "prototype", "research", "tdd", "writing-for-agents",
}
EXPECTED = EXPLICIT | IMPLICIT


def prose_lines(source):
    """Code fences in the shipped Markdown templates contain example destinations."""
    fence = None
    for line in source.splitlines():
        if fence:
            marker = line.strip()
            if marker.startswith(fence) and not marker.strip(fence[0]):
                fence = None
            continue
        opening = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if opening:
            fence = opening.group(1)
        else:
            yield line


def check(root):
    root = root.resolve()
    errors = []
    skills = {p.parent.name: p for p in (root / "skills").glob("*/SKILL.md")}
    catalog = (root / "docs/skills.md").read_text(encoding="utf-8")
    indexed = set(re.findall(r"\]\(\.\./skills/([^/]+)/SKILL\.md\)", catalog))
    for label, names in (("skill directories", set(skills)), ("documented skill index", indexed)):
        if names != EXPECTED:
            errors.append(f"{label}: missing {sorted(EXPECTED - names)}, unexpected {sorted(names - EXPECTED)}")

    for name, path in sorted(skills.items()):
        source = path.read_text(encoding="utf-8")
        parts = source.split("---", 2)
        if not source.startswith("---\n") or len(parts) < 3:
            errors.append(f"{name}: missing frontmatter")
            continue
        if not re.search(r"^name: " + re.escape(name) + r"\s*$", parts[1], re.M):
            errors.append(f"{name}: frontmatter name mismatch")
        if not re.search(r"^description: \S.+$", parts[1], re.M):
            errors.append(f"{name}: missing description")
        flags = re.findall(r"^disable-model-invocation:[ \t]*(.*)$", parts[1], re.M)
        if name in EXPLICIT and flags != ["true"]:
            errors.append(f"{name}: expected disable-model-invocation: true")
        elif name in IMPLICIT and flags not in ([], ["false"]):
            errors.append(f"{name}: expected model invocation to be enabled")

        metadata = path.parent / "agents/openai.yaml"
        if not metadata.is_file():
            errors.append(f"{name}: missing {metadata.name}")
            continue
        yaml = metadata.read_text(encoding="utf-8")
        if not re.search(r"^interface:\s*\n[ \t]+display_name:\s*\S", yaml, re.M):
            errors.append(f"{name}: missing interface metadata")
        # An omitted policy opts into implicit invocation in the imported Codex format.
        policy = re.search(r"^policy:[ \t]*\n((?:[ \t]+[^\n]*\n?)*)", yaml, re.M)
        value = re.findall(r"^[ \t]+allow_implicit_invocation:[ \t]*(\S+)[ \t]*$", yaml, re.M)
        if value or name in EXPLICIT:
            expected = "false" if name in EXPLICIT else "true"
            field = rf"^[ \t]+allow_implicit_invocation:[ \t]*{expected}[ \t]*$"
            if value != [expected] or not policy or not re.search(field, policy[1], re.M):
                errors.append(f"{name}: expected policy.allow_implicit_invocation = {expected}")

    for path in sorted(root.rglob("*.md")):
        source = path.read_text(encoding="utf-8")
        for line in prose_lines(source):
            for target in re.findall(r"\]\(([^)]+)\)", line):
                target = target.split("#", 1)[0]
                if not target or re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                    continue
                resolved = (path.parent / target).resolve()
                if root not in resolved.parents and resolved != root:
                    errors.append(f"{path.relative_to(root)}: reference escapes project: {target}")
                elif not resolved.exists():
                    errors.append(f"{path.relative_to(root)}: missing reference: {target}")
        if re.search(r"/Users/[^/\s]+/|https://(?:app\.)?notion\.(?:so|com)/", source):
            errors.append(f"{path.relative_to(root)}: review private path or Notion URL")
    return errors


def check_baseline(root):
    record = json.loads((root / "docs/source-baseline.json").read_text(encoding="utf-8"))
    expected = dict(record["sha256"])
    license_path = record["upstream"]["license_file"]
    expected[license_path] = record["upstream"]["license_sha256"]
    actual = {
        p.relative_to(root).as_posix()
        for p in (root / "skills").rglob("*")
        if p.is_file() and p.name != ".DS_Store" and "__pycache__" not in p.parts
    }
    if (root / license_path).is_file():
        actual.add(license_path)
    errors = [f"missing import file: {p}" for p in sorted(expected.keys() - actual)]
    errors.extend(f"added since import: {p}" for p in sorted(actual - expected.keys()))
    for name in sorted(actual & expected.keys()):
        if hashlib.sha256((root / name).read_bytes()).hexdigest() != expected[name]:
            errors.append(f"changed since import: {name}")
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", action="store_true", help="also verify the import manifest")
    args = parser.parse_args()
    problems = check(ROOT)
    if args.baseline:
        problems.extend(check_baseline(ROOT))
    for problem in problems:
        print("ERROR:", problem)
    if problems:
        sys.exit(1)
    print(f"PASS: {len(EXPECTED)} skills, catalog, invocation policies, local links and privacy scan")
    if args.baseline:
        print("PASS: imported skill files and upstream license match the SHA-256 manifest")
