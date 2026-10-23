---
name: engineer
description: Complete software changes with source investigation, proportionate design comparison, independent review, and evidence of completion. Use for implementing features, fixing bugs, or refactoring existing code.
---

# Engineer

Own the requested outcome through its authorized endpoint.
Use the target repository's instructions and existing testing and shipping procedures.
Resolve this file's real filesystem path before opening sibling skills or references.
Install this bundle's three skill directories together.

## 1. Establish completion

Read the request and relevant repository guidance. Resolve retrievable facts from source and tools.
Name the expected behavior, task scope, required checks, and authorized endpoint.
Ask only for missing decisions that materially affect the work and cannot be established from available evidence.
Approval to implement does not authorize publishing, merging, deployment, or unrelated cleanup.

For substantial or continued work, use the [task record](references/task-record.md).
If a goal skill is active, keep its outcome aligned with this record. Leave continuation to that skill.

## 2. Understand the affected system

Trace the production entry point, the module owning the behavior, callers, and relevant stored or external representations.
Search for an existing implementation and a representative test before adding another path.
Read the relevant architecture decisions and project terminology when available.
Explain where the change belongs and which other paths depend on it. Cite source locations.
Investigate until placement, affected behavior, and verification are justified. File counts do not establish understanding.

## 3. Choose the design

Read the [architecture reference](references/architecture.md) when ownership, shared behavior, or an important interface changes.
Compare the proposed approach with one credible alternative for those changes.
Give each candidate a caller example and explain complexity hidden, required caller changes, and maintenance costs.
Choose the simplest design that covers the affected behavior within the authorized scope.
Routine changes following a clear existing pattern need only a brief placement rationale.

If two attempts fail for the same assumed reason, state and test that assumption before another patch.
If implementation repeatedly needs casts, duplicated rules, or special cases, reconsider the design.
An existing rule or public contract can be a necessary constraint. Request a decision before crossing an authorization boundary.

## 4. Implement and verify

Use repository-specific implementation and testing procedures when available.
For functional changes, establish a failing reproduction or acceptance check before the fix when a practical path exists.
If reproduction is unavailable, record the limitation and the strongest available check.
Implement in coherent units and verify each affected behavior through its production-facing interface.
Exercise the assumption that makes a risky change safe. Explain evidence gaps explicitly.
Use existing checks when they already prove the requirement. New abstractions and tests must earn their maintenance cost.
Keep unrelated discoveries separate. Record them without silently expanding the assignment.

## 5. Review the result

For substantial changes, use [review-change](../review-change/SKILL.md) with a fresh reviewer before declaring completion.
Substantial includes changed ownership, important interfaces, shared state, or behavior spanning several production paths.
Supply requirements, the exact review scope, and repository access. Let the reviewer inspect surrounding code independently.
Use available models and delegation tools. A different model can add perspective but is not a requirement.
Verify each finding before acting. Fix confirmed in-scope defects and justify rejected findings.
After a fix, rerun affected checks and request a focused review of changed risk.
Reopen full review when the scope materially changes.
If independent review is unavailable, record it as incomplete. Self-review cannot establish independent review completion.

## 6. Establish the final state

Compare every requirement with evidence from the current revision and relevant build artifacts.
Later edits invalidate the affected verification and review evidence.
Run existing cleanup, CI, and shipping procedures through the authorized endpoint.
Waiting for an outstanding required check is unfinished work. Preserve the next action for continuation.
Repeated failures require diagnosis or escalation, not weaker acceptance criteria.

Declare completion only when all required behavior, checks, and the authorized endpoint are established.
Otherwise report unfinished work or a concrete blocker. Missing access, unavailable services, and required user decisions remain explicit.
Report the user-visible result, checks and their coverage limits, current revision, and remaining work.
Distinguish local implementation, passed checks, merged code, deployment, and observed production behavior.
