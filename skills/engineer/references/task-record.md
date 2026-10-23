# Task record

For substantial or continued work, keep one short Markdown record outside the target repository.
Use an existing session artifact directory or a task-specific directory under the operating system's temporary directory.
Choose a known durable location when the work must survive temporary-file cleanup.
Tell the user and continuation mechanism the absolute path.
Update the same record after meaningful progress and before ending an incomplete turn.

Use the following fields. Keep evidence concise and link to relevant logs instead of copying bulk output.

```markdown
# Task

Outcome:
Scope and exclusions:
Authorized endpoint:
Workspace and branch:
Source revision and uncommitted changes:

| Requirement | Check or observation | Result and coverage limit | Revision |
| --- | --- | --- | --- |

Design decision and relevant source references:
Independent review scope, revision, and result:
Confirmed findings and disposition:
Current state:
Blocker, if any:
Next action:
```

Record tool results and observations. A checked box or narrative claim is not evidence by itself.
Include exit status and representative input when those determine what a check proves.
For uncommitted work, record the base commit and a saved patch fingerprint, including new files.
Reconcile the record with source and external state when resuming. Recheck evidence affected by intervening changes.
