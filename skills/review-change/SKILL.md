---
name: review-change
description: Independently review a change for requirements, correctness, and structural quality. Use when explicitly requested or within an explicitly requested engineer workflow.
---

# Review change

Activate only when explicitly requested by the user or delegated by an explicitly invoked engineer workflow.
Assess the stated requirements against source and observable evidence.
Keep the review read-only. Findings are claims for the implementer to verify.
Resolve this file's real filesystem path before opening sibling resources.

## Establish the scope

Read the requirements and relevant repository guidance.
Identify the target, actual base, current revision, and uncommitted changes included in the review.
Include newly created files. A committed diff alone cannot establish the state of an edited worktree.
For a proposed design, review its caller examples, responsibilities, and constraints instead of requiring an implementation diff.
If scope or required intent cannot be established, report the missing information and limit the verdict accordingly.

If this context authored the change, delegate the assessment to a fresh reviewer when available.
Give the reviewer requirements, scope, and source access without the author's preferred conclusion or expected findings.
If already acting as the fresh reviewer, perform the assessment directly. Nested reviewer chains add no independence.
When fresh review is unavailable, label the result self-review and keep independent review incomplete.

## Inspect independently

Read changed code and the surrounding production paths needed to understand its effects.
Trace required callers, stored representations, errors, and relevant lifecycle transitions.
Read the shared [architecture criteria](../engineer/references/architecture.md) for structural assessment.
Use existing project-specific review and verification procedures where they add relevant evidence.

Assess these questions:

- Does every requirement reach the actual production caller?
- Can a concrete input or state produce wrong behavior?
- Do ownership and interfaces fit the existing system?
- Does the change duplicate rules or representations that must stay synchronized?
- Does an existing abstraction remove complexity added by the patch?
- Do new abstractions hide useful complexity and keep internal details private?
- Do checks exercise the behavior claimed, including the relevant coordination?
- Do compatibility, authorization, concurrency, and deployment constraints hold where affected?

Follow promising concerns to evidence. Avoid lists of hypothetical failures and stylistic preferences.
Treat concrete structural regressions as review findings even when behavior appears correct.
Explain which callers or future changes incur the maintenance cost.
An opportunity for unrelated cleanup is separate from a defect introduced or exposed by this change.

## Report a reasoned verdict

For each finding, provide a location, severity, consequence, evidence, and proposed correction.
Use the repository's severity scale when available. Otherwise distinguish blocking defects from optional improvements.
For behavior, give a concrete failing input or state. For structure, describe duplicated knowledge or unnecessary caller obligations.
Separate confirmed findings from unverified concerns. Run a permitted read-only check when it can resolve uncertainty.
Do not edit files, stage changes, or publish findings without authorization.

Finish with the reviewed revision or design scope, material findings, evidence limits, and one verdict:

- **Changes required** when confirmed defects or material structural regressions remain.
- **No blocking findings found** when the reviewed scope produced none.
- **Incomplete** when missing source, intent, or required evidence prevents an assessment.

An empty finding list establishes only that this review found no blocking issue within its scope.
When reviewing fixes, assess the delta and affected callers. Request a fresh full assessment only after a material scope change.
