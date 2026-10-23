# Architecture criteria

Read this when changing ownership, shared behavior, or an important interface.
Apply the relevant criteria to the affected area. Existing architecture and deployment constraints still apply.

## Responsibility and caller knowledge

A module is a function, class, package, or cohesive slice with an interface and implementation.
Its interface includes everything callers must know, including ordering, failure behavior, configuration, and types.
Prefer a small interface that hides substantial complexity. This is a deep module.

For example, a parser exposes `parse(input)` and owns decoding and validation.
Callers receive a defined result instead of coordinating those internal steps themselves.
The implementation can still contain small internal functions.

Identify which module owns each rule and each mutable state value.
Concentrate decisions behind that owner's interface. Keep callers from depending on internal representations.
Respect boundaries needed for security, transactions, separate deployment, or distinct domain responsibilities.

## Does the abstraction earn its place?

Apply the deletion test. Imagine removing the abstraction while preserving behavior.
If complexity disappears, the abstraction may be unnecessary.
If the same policy or coordination spreads across callers, the abstraction is probably useful.

Check forwarding methods, one-caller wrappers, public configuration of internal stages, and duplicated lists.
A wrapper can earn its place through validation, adaptation, policy, or a required dependency boundary.
Prefer one canonical decision over several places that must change together.
Reject speculative extension points without a concrete consumer or variation.

## Compare meaningful alternatives

When the interface or ownership is uncertain, sketch two materially different designs before substantial implementation.
Show a representative caller for each design. Include ordering and failure behavior when those affect correct use.
Compare what callers learn, what stays private, which paths change, and where future fixes concentrate.
Use a small isolated experiment when an observable fact can settle the choice.
Choose on demonstrated constraints. Fewer files or more abstraction alone do not establish a better design.

## Test at a useful boundary

Verify outcomes through the interface used by the relevant caller.
Choose a boundary that includes the behavior under review, including coordination where defects can occur.
Prefer coverage that survives internal restructuring.

Keep pure computation directly testable. Use existing local substitutes for dependencies when they represent the required behavior.
For network or process boundaries, reuse existing adapters or test doubles before introducing a new port.
Introduce dependency injection when concrete production or testing needs justify the separation.
A test substitute does not justify exposing every internal collaborator to callers.
Match claims to coverage. A substitute cannot establish real transport behavior or deployed service compatibility.

## Preserve knowledge and existing behavior

Use the project's domain terms. Read relevant architecture decisions before revisiting a settled choice.
Record a durable decision when it is difficult to reverse, surprising without context, and based on real alternatives.
Follow existing documentation conventions. A missing glossary does not require creating one for every task.

For structural changes, pin relevant observable behavior with adequate existing coverage or a focused characterization check.
Move in verifiable units. Account for every affected caller and representation within scope.
Contract compatibility and deployment order can require staged migration.
Replace redundant tests only after equivalent behavior coverage is established and deletion is authorized.

## Review questions

- What responsibility does this module own?
- What must callers understand to use it correctly?
- Which complexity does the interface hide?
- Does the change concentrate knowledge or duplicate it?
- Does each new abstraction pass the deletion test?
- Does representative verification exercise the relevant operation?
- Which existing decisions and compatibility requirements constrain the change?

Report concrete structural problems and their maintenance consequences. Apply these questions as judgment criteria rather than numerical scores.
