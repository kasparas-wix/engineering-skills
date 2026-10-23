---
name: prevent-repeat
description: Investigate recurring engineering mistakes and replace repeated corrections with enforceable repository constraints. Use when the same class of defect or review correction has occurred more than once.
---

# Prevent repeat

Turn a demonstrated recurring mistake into a constraint that catches or eliminates it.
Keep this work within its own authorized scope. A correction during another task does not authorize unrelated restructuring.

## Establish recurrence

Read the supplied corrections and relevant commits, reverts, reviews, or failing examples.
Stay within the project and evidence sources authorized for this task.
Group instances by the underlying mistake, rather than shared wording or filenames.
Identify at least two demonstrated instances before describing a class as recurring.
If only one instance is available, report that limit. A justified local fix can proceed within scope without claiming recurrence.

## Choose the strongest proportionate correction

First consider whether ownership, a canonical representation, or an inaccessible internal module can eliminate the mistake.
Read the shared [architecture criteria](../engineer/references/architecture.md) before proposing structural changes.
Then consider a type constraint, import restriction, lint rule, or existing build check.
Use a behavioral regression check when the failure depends on runtime input or state.
Keep guidance for decisions that require judgment and cannot be enforced reliably.

Prefer existing enforcement mechanisms and dependencies.
Choose a narrow constraint that catches the demonstrated class while accepting legitimate neighboring behavior.
For widespread existing violations, consider enforcing new violations before proposing a separate migration.
Explain why a broader structural correction is unsuitable when choosing a lower-cost check.

## Implement only within authorization

For a proposal request, present the evidence and recommended correction without changing the repository.
For authorized implementation, establish a representative failing case before the correction.
Prove the constraint rejects a real past mistake and accepts a legitimate neighboring case.
Run the relevant repository checks. Make the same check part of existing CI when that change is within scope.
Preserve security, compatibility, and required test coverage.
Apply repository approval rules before changing contracts, deleting files, or adding dependencies.

## Preserve the lesson

Record the mistake class, evidence, enforcing mechanism, and verification command in the project's existing guidance location.
Explain the mechanism's coverage limit. Do not claim that one example proves the entire class impossible.
Keep any necessary judgment rule short and linked to its reason.
Do not modify global skills, memory, or unrelated repositories without task authorization.

Report the demonstrated recurrence, chosen correction, rejected alternatives, verification results, and remaining limitations.
