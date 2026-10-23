#!/usr/bin/env python3
"""Check frontmatter, explicit-only policies, and local Markdown links."""

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent.parent
EXPECTED = {"engineer", "review-change", "prevent-repeat"}


def check(root):
    root = root.resolve()
    errors = []
    skills = root / "skills"
    found = {path.name for path in skills.iterdir() if path.is_dir()}
    if found != EXPECTED:
        errors.append(f"skills: expected {sorted(EXPECTED)}, found {sorted(found)}")

    for name in sorted(EXPECTED):
        path = skills / name / "SKILL.md"
        if not path.is_file():
            errors.append(f"{path.relative_to(root)}: missing entry")
            continue
        text = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\nname: ([a-z0-9-]+)\ndescription: ([^\n]+)\n---\n", text)
        if not match:
            errors.append(f"{path.relative_to(root)}: use name and description as plain single-line scalars")
            continue
        if match[1] != name:
            errors.append(f"{path.relative_to(root)}: name differs from directory")
        description = match[2]
        if len(description) > 1024 or any(c in description for c in "<>\"'{}[]#") or ": " in description:
            errors.append(f"{path.relative_to(root)}: invalid plain-scalar description")
        if not description.strip():
            errors.append(f"{path.relative_to(root)}: empty description")

        policy = skills / name / "agents" / "openai.yaml"
        if not policy.is_file():
            errors.append(f"{policy.relative_to(root)}: missing explicit invocation policy")
        elif policy.read_text(encoding="utf-8") != "policy:\n  allow_implicit_invocation: false\n":
            errors.append(f"{policy.relative_to(root)}: expected policy-only YAML with allow_implicit_invocation set to false")

    for path in sorted(root.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", text):
            link = urlsplit(target)
            if link.scheme or link.netloc or not link.path:
                continue
            destination = (path.parent / unquote(link.path)).resolve()
            if not destination.is_relative_to(root):
                errors.append(f"{path.relative_to(root)}: local link escapes bundle: {target}")
            elif not destination.is_file():
                errors.append(f"{path.relative_to(root)}: missing link target: {target}")
    return errors


if __name__ == "__main__":
    failures = check(ROOT)
    if failures:
        print("\n".join(failures), file=sys.stderr)
        sys.exit(1)
    print("Checked 3 skill entries, explicit invocation policies, and all local Markdown links.")
