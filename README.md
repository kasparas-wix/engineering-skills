# Engineering skills

A small skill stack for completing software tasks without accumulating avoidable complexity.

## Skills

| Skill | Purpose |
| --- | --- |
| [engineer](skills/engineer/SKILL.md) | Investigate, choose a design, implement, verify, and establish completion. |
| [review-change](skills/review-change/SKILL.md) | Independently assess requirements, correctness, and structural quality. |
| [prevent-repeat](skills/prevent-repeat/SKILL.md) | Convert demonstrated recurring mistakes into enforced constraints. |

`engineer` is the normal entry point. It requests an independent review for substantial changes.
`prevent-repeat` runs when recurring corrections justify separate work.
Both core skills share one [architecture reference](skills/engineer/references/architecture.md).

## Explicit invocation

All three skills set `policy.allow_implicit_invocation: false` in `agents/openai.yaml`.
Codex does not select them automatically from a matching task. Explicit `$skill-name` invocation remains available.
See the [Codex invocation policy](https://learn.chatgpt.com/docs/build-skills#optional-metadata).

Invoking `$engineer` includes its bundled `review-change` step. You do not need to invoke that step separately.
Standalone review and recurring-correction work require explicit invocation of their respective skills.

## Use without installation

Give the agent the absolute path to the entry skill:

```text
Use /Users/kasparasb/Personal/engineering-skills/skills/engineer/SKILL.md.
Fix the duplicate notifications after a retry.
Done means the reproduction passes and the patch is ready for my review.
```

The repository is usable by file path immediately. It is not automatically installed into any agent application.

## Install locally for Codex

Install all three directories together because the core skills share files.
From this repository, run:

```sh
python3 - <<'PY'
from pathlib import Path

source = Path.cwd() / "skills"
destination = Path.home() / ".codex" / "skills"
names = ("engineer", "review-change", "prevent-repeat")
for name in names:
    if not (source / name / "SKILL.md").is_file():
        raise SystemExit("Run this command from the engineering-skills repository.")
    target = destination / name
    if target.exists() or target.is_symlink():
        raise SystemExit(f"Existing destination requires inspection: {target}")
destination.mkdir(parents=True, exist_ok=True)
for name in names:
    (destination / name).symlink_to(source / name, target_is_directory=True)
PY
```

The command checks all destinations before creating links. Inspect a conflict before choosing another destination or replacing an installation.
When the skills appear in your agent's skill list, invoke them by name:

```text
$engineer Fix duplicate notifications after a retry. Reproduce the failure and verify the real caller.
$review-change Review this branch against the notification requirements. Do not edit files.
$prevent-repeat Investigate our repeated imports of package internals. Propose an enforceable correction.
```

Pair `engineer` with your existing goal skill for continued execution.
The goal holds the requested outcome. The task record holds requirements, evidence, and remaining work.
This stack provides no scheduler, model routing, or automatic merge permission.

## How much process applies

A routine change following an established pattern needs focused investigation and its relevant checks.
Changes to ownership, important interfaces, shared state, or several production paths need design comparison and independent review.
Choose the reviewer from models available in the current environment. No model names are hardcoded.

Repository guidance and existing testing, security, cleanup, and shipping procedures remain authoritative.
The skills do not expand task scope or grant external-action permissions.
They guide decisions. Executable checks and independent evidence establish the results they actually cover.

## Validate changes

```sh
python3 scripts/check.py
```

This checks the authored frontmatter format, explicit invocation policies, bundled skills, and local Markdown links.
It does not establish behavioral quality. Use the [evaluation scenarios](evals/README.md) for that.
