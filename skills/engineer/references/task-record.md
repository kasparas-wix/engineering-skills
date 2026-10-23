# Task record

For substantial work, or work that will continue across turns, keep one short Markdown record outside the target repository.
Use an existing session artifact directory or a task-specific directory under the operating system's temporary directory.
Choose a known durable location when the work must survive temporary-file cleanup.
Tell the user, and the goal skill if one is running, the record's absolute path.
Update the same record after meaningful progress and before ending a turn with work unfinished.

Use the following fields. Keep evidence concise and link to logs instead of copying bulk output.

```markdown
# Task

Outcome:
Scope and exclusions:
Stopping point:
Workspace and branch:
Source revision and uncommitted changes:

| Requirement | Check or observation | Result and coverage limit | Revision |
| --- | --- | --- | --- |

Design decision and source references:
Independent review scope, revision, and result:
Confirmed findings and disposition:
Current state:
Blocker, if any:
Next action:
```

Record tool results and observations. A checked box or a narrative claim is not evidence by itself.
Include the exit status and representative input when they determine what a check proves.
For uncommitted work, record the base commit and a hash of the uncommitted changes, such as `git diff HEAD` plus the list of untracked files.
When resuming, compare the record with the current source and external state. Recheck any evidence that later changes could have affected.
