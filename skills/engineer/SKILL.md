---
name: engineer
description: Complete software changes with source investigation, design comparison, independent review, and evidence of completion. Use only when explicitly requested.
---

# Engineer

Activate only when the user explicitly names this skill or supplies its file path.
Follow the target repository's instructions and its existing testing and shipping procedures.
Resolve this file's real filesystem path before opening sibling skills or references. Installed copies may be symlinks, and relative links can resolve to the wrong place from a link's location.

A change is **substantial** when it moves ownership of a behavior, changes an important interface, touches shared state, or alters behavior on several production paths.
An **important interface** is public or used by more than one module or package.
Substantial changes get a task record, a design comparison, and an independent review. Routine changes skip them.

## 1. Decide what done means

Read the request and the repository guidance that applies to it. Look up facts in source and tools instead of asking for them.
Name the expected behavior, the scope, the checks that must pass, and the stopping point.
The **stopping point** is where the task ends, such as "patch ready for review", "pull request opened", or "merged and deployed".
Do not go past it without asking. Approval to implement is not approval to publish, merge, deploy, or clean up unrelated code.
Ask only about decisions that change the work and cannot be settled from available information.

For substantial work, or work that will continue across turns, keep a [task record](references/task-record.md).
A goal skill, if one is running, keeps the task going across turns. Keep its outcome consistent with the record and leave continuation to it.

## 2. Understand the affected system

Trace the production entry point, the module that owns the behavior, its callers, and any stored or external representations.
Search for an existing implementation and a representative test before adding another path.
Read the project's architecture decisions and terminology when they exist.
Explain where the change belongs and which other paths depend on it. Cite source locations.
Keep investigating until you can justify where the change goes, what it affects, and how to verify it. Reading many files is not the goal.

## 3. Choose the design

For substantial changes, read the [architecture reference](references/architecture.md) and compare the proposed design with one credible alternative as it describes.
Choose the simplest design that covers the affected behavior within scope.
Routine changes that follow a clear existing pattern need only a brief note on where the change goes.

If two attempts fail for the same assumed reason, state that assumption and test it before writing another patch.
If the implementation keeps needing casts, duplicated rules, or special cases, reconsider the design.
An existing rule or public contract may be a real constraint rather than an obstacle.
Ask before changing a public contract, deleting files, adding dependencies, or doing work outside the scope.

## 4. Implement and verify

Use the repository's implementation and testing procedures when they exist.
For functional changes, write a check that fails before the fix whenever practical. A check that never failed may not test the change.
If you cannot reproduce the failure, record that and use the strongest check available.
Implement in coherent steps. Verify each affected behavior through the interface its production callers use.
For a risky change, test the assumption that makes it safe. State any gaps in the evidence.
Use existing checks when they already prove the requirement. Add new abstractions and tests only when they are worth maintaining.
Record unrelated discoveries separately instead of quietly expanding the task.

## 5. Review the result

For substantial changes, have a fresh reviewer apply [review-change](../review-change/SKILL.md) before declaring completion.
The author's context shares the author's blind spots, so a reviewer without it catches more.
This review is part of the engineer invocation. The user does not need to invoke review-change separately.
Give the reviewer the requirements, the exact review scope, and repository access. Let it read surrounding code on its own.
Use whatever models and delegation tools are available. A different model can add perspective but is not required.
Verify each finding before acting on it. Fix confirmed defects within scope and explain why you rejected any finding.
After a fix, rerun the affected checks and ask for a focused review of what changed. Ask for a full review again if the scope changed materially.
If no independent reviewer is available, record the review as incomplete. Reviewing your own work does not count.

## 6. Confirm what is actually done

Compare every requirement with evidence from the current revision and its build output.
A later edit invalidates the checks and review it affects.
Run the existing cleanup, CI, and shipping procedures up to the stopping point.
A required check that is still running means the work is unfinished. Record the next action so the work can continue.
If checks keep failing, diagnose the cause or escalate. Do not weaken the acceptance criteria.

Declare completion only when all required behavior and checks pass and the stopping point is reached.
Otherwise report the unfinished work or a concrete blocker. Name missing access, unavailable services, and decisions the user still needs to make.
Report the user-visible result, the checks run and what they do not cover, the current revision, and remaining work.
Keep these states distinct: implemented locally, checks passed, merged, deployed, and observed working in production.
