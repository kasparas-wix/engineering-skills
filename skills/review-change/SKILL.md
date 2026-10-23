---
name: review-change
description: Independently review a change for requirements, correctness, and structural quality. Use when explicitly requested or within an explicitly requested engineer workflow.
---

# Review change

Activate only when the user explicitly requests it or an explicitly invoked engineer workflow delegates it.
Check the stated requirements against source and observable evidence.
Keep the review read-only. Findings are claims for the implementer to verify.
Resolve this file's real filesystem path before opening sibling resources. Installed copies may be symlinks.

## Establish the scope

Read the requirements and the repository guidance that applies to them.
Identify the target, the actual base, the current revision, and any uncommitted changes in scope.
Include uncommitted and newly created files. The committed diff alone misses them.
For a proposed design, review its caller examples, responsibilities, and constraints instead of requiring an implementation diff.
If the scope or the intended behavior cannot be determined, report what is missing and limit the verdict accordingly.

If you wrote the change, do not review it yourself. Give this file to a fresh reviewer when one is available.
Give that reviewer the requirements, scope, and source access, without your preferred conclusion or expected findings.
If you are that fresh reviewer, review directly. Delegating again adds no independence.
When no fresh reviewer is available, label the result self-review and record independent review as incomplete.

## Inspect independently

Read the changed code and the surrounding production paths needed to understand its effects.
Trace the callers, stored representations, errors, and lifecycle transitions the change affects.
Read the shared [architecture criteria](../engineer/references/architecture.md) for the structural assessment.
Use the project's own review and verification procedures where they add evidence.

Answer these questions:

- Does every requirement reach the actual production caller?
- Can a concrete input or state produce wrong behavior?
- Do ownership and interfaces fit the existing system?
- Does the change duplicate rules or representations that must stay synchronized?
- Does an existing abstraction already handle complexity the patch adds?
- Do new abstractions hide useful complexity and keep internal details private?
- Do checks exercise the behavior claimed, including the coordination between parts?
- Do compatibility, authorization, concurrency, and deployment constraints hold where affected?
- Does added complexity for speculative or vanishingly unlikely race or security cases have the user's approval?

Follow promising concerns until you have evidence. Do not list hypothetical failures or stylistic preferences.
Report concrete structural regressions as findings even when behavior appears correct.
Explain which callers or future changes will bear the maintenance cost.
List unrelated cleanup ideas separately. They are not findings unless this change introduced or exposed the problem.

## Report a reasoned verdict

For each finding, give the location, severity, consequence, evidence, and proposed correction.
Use the repository's severity scale when it has one. Otherwise separate blocking defects from optional improvements.
For behavior, give a concrete input or state that fails. For structure, describe the duplicated knowledge or the unnecessary burden on callers.
Separate confirmed findings from unverified concerns. Run a permitted read-only check when it can resolve the uncertainty.
Do not edit files, stage changes, or publish findings without authorization.

Finish with the reviewed revision or design scope, material findings, evidence limits, and one verdict:

- **Changes required** when confirmed defects or material structural regressions remain.
- **No blocking findings found** when the reviewed scope produced none.
- **Incomplete** when missing source, intent, or required evidence prevents an assessment.

An empty finding list means only that this review found no blocking issue within its scope.
When reviewing fixes, assess the change since the last review and its affected callers. Ask for a fresh full review only after a material scope change.
