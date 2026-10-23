# Engineering skills

A small skill stack for completing software tasks without accumulating avoidable complexity.

## Skills

| Skill | Purpose |
| --- | --- |
| [engineer](skills/engineer/SKILL.md) | Investigate, choose a design, implement, verify, and confirm what is done. |
| [review-change](skills/review-change/SKILL.md) | Independently assess requirements, correctness, and structural quality. |
| [prevent-repeat](skills/prevent-repeat/SKILL.md) | Convert demonstrated recurring mistakes into enforced constraints. |

`engineer` is the normal entry point. For substantial changes it runs `review-change` with a fresh reviewer.
Invoke `prevent-repeat` when the same correction keeps coming back.
All three skills share one [architecture reference](skills/engineer/references/architecture.md).

## Explicit invocation

All three skills set `policy.allow_implicit_invocation: false` in `agents/openai.yaml`.
Codex does not select them automatically from a matching task. Explicit `$skill-name` invocation remains available.
See the [Codex invocation policy](https://learn.chatgpt.com/docs/build-skills#optional-metadata).

Invoking `$engineer` covers the `review-change` step it runs for substantial changes. You do not need to invoke it separately.
To review a change on its own, or to work on a recurring mistake, invoke `$review-change` or `$prevent-repeat` directly.

## Use without installation

Give the agent the absolute path to the entry skill:

```text
Use /Users/kasparasb/Personal/engineering-skills/skills/engineer/SKILL.md.
Fix the duplicate notifications after a retry.
Done means the reproduction passes and the patch is ready for my review.
```

The repository is usable by file path immediately. It is not automatically installed into any agent application.

## Install locally for Codex

Install all three directories together. The skills link to each other's files.
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

If you use a goal skill, one that keeps an agent working on a task across turns, pair it with `engineer`.
The goal skill holds the requested outcome. The task record holds requirements, evidence, and remaining work.
This stack provides no scheduler, model routing, or automatic merge permission.

## How much process applies

A routine change that follows an established pattern needs focused investigation and the checks that cover it.
[Substantial changes](skills/engineer/SKILL.md) also get a task record, a design comparison, and an independent review.
Choose the reviewer from models available in the current environment. No model names are hardcoded.

Repository guidance and existing testing, security, cleanup, and shipping procedures remain authoritative.
The skills do not expand task scope or grant external-action permissions.
They guide decisions. Only executable checks and independent evidence prove results, and only for what they cover.

## Validate changes

```sh
python3 scripts/check.py
```

This checks the authored frontmatter format, explicit invocation policies, the expected skill directories, and local Markdown links.
It does not test how well the skills work. Use the [evaluation scenarios](evals/README.md) for that.
