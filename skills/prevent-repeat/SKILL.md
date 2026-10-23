---
name: prevent-repeat
description: Investigate recurring engineering mistakes and replace repeated corrections with enforceable repository constraints. Use only when explicitly requested.
---

# Prevent repeat

Activate only when the user explicitly names this skill or supplies its file path.
Turn a demonstrated recurring mistake into a constraint that catches or eliminates it.
Stay within this task's scope. A correction you received during another task is not permission to restructure code outside this one.

## Establish recurrence

Read the supplied corrections and the related commits, reverts, reviews, or failing examples.
Use only the projects and evidence sources this task covers.
Group instances by the underlying mistake, not by shared wording or filenames.
Call a mistake recurring only when you have at least two demonstrated instances.
With only one instance, say so. A justified local fix can still proceed within scope, without claiming recurrence.

## Choose the strongest proportionate correction

First consider whether clear ownership, a single canonical representation, or making an internal module impossible to import from outside would eliminate the mistake.
Read the shared [architecture criteria](../engineer/references/architecture.md) before proposing structural changes.
Next consider a type constraint, import restriction, lint rule, or existing build check.
Use a behavioral regression check when the failure depends on runtime input or state.
Use written guidance only for decisions that need judgment and cannot be enforced reliably.

Prefer existing enforcement mechanisms and dependencies.
Choose a narrow constraint that catches the demonstrated mistake and still allows legitimate neighboring behavior.
When many violations already exist, consider enforcing the rule on new code only and proposing the cleanup of existing cases as separate work.
When you choose a cheaper check over a structural correction, explain why the structural correction does not fit.

## Implement only within authorization

If the user asked for a proposal, present the evidence and the recommended correction without changing the repository.
If implementation is authorized, first create a representative case that fails.
Show that the constraint rejects a real past mistake and accepts a legitimate neighboring case.
Run the repository's checks. Add the new check to existing CI when that change is within scope.
Preserve security, compatibility, and required test coverage.
Follow the repository's approval rules before changing contracts, deleting files, or adding dependencies.

## Preserve the lesson

Record the mistake, the evidence, the enforcing mechanism, and the verification command where the project already keeps its guidance.
State what the mechanism does not cover. One rejected example does not prove the whole class of mistake is impossible.
Keep any remaining judgment rule short and give its reason.
Do not modify global skills, memory, or unrelated repositories unless the task authorizes it.

Report the demonstrated recurrence, the chosen correction, rejected alternatives, verification results, and remaining limitations.
