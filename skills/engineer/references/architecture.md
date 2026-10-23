# Architecture criteria

Read this when a change moves ownership, changes shared behavior, or changes an important interface.
Apply the criteria that fit the affected area. Existing architecture and deployment constraints still apply.

## Responsibility and caller knowledge

A module is a function, class, package, or cohesive slice with an interface and implementation.
Its interface includes everything callers must know, including ordering, failure behavior, configuration, and types.
Prefer a small interface with substantial logic behind it. Such a module is called a deep module.

For example, a parser exposes `parse(input)` and owns decoding and validation.
Callers receive a defined result instead of coordinating those internal steps themselves.
The implementation can still contain small internal functions.

Identify which module owns each rule and each mutable state value.
Keep each decision behind its owner's interface, so callers do not depend on internal representations.
Respect boundaries needed for security, transactions, separate deployment, or distinct domain responsibilities.

## Does the abstraction earn its place?

Apply the deletion test: imagine inlining the abstraction into its callers while preserving behavior.
If the code gets simpler, the abstraction is probably unnecessary.
If each caller would have to repeat its policy or coordination, the abstraction is probably useful.

Look for forwarding methods, one-caller wrappers, public configuration of internal stages, and duplicated lists.
A wrapper can earn its place through validation, adaptation, policy, or a required dependency boundary.
Prefer one canonical decision over several places that must change together.
Reject speculative extension points without a concrete consumer or variation.

## Proportionate robustness

For a speculative or vanishingly unlikely race or security edge case, explain the concrete failure mode before adding complexity.
State its likelihood and the complexity cost, including uncertainty in the likelihood estimate.
Get the user's buy-in before implementing that added complexity.
Do not silently expand scope for theoretical robustness.

## Compare meaningful alternatives

When ownership or an important interface changes, sketch two materially different designs before substantial implementation.
Show a representative caller for each design. Include ordering and failure behavior when those affect correct use.
Compare what callers must learn, what stays private, which paths change, where future fixes land, and what each design costs to maintain.
Use a small isolated experiment when an observable fact can settle the choice.
Decide on demonstrated constraints. Fewer files or more abstraction does not by itself make a design better.

## Test at a useful boundary

Verify outcomes through the interface the caller in question uses.
Choose a boundary that includes the behavior under review, including the coordination where defects can occur.
Prefer coverage that survives internal restructuring.

Keep pure computation directly testable. Use existing local substitutes for dependencies when they behave like the real ones in the ways the test needs.
For network or process boundaries, reuse existing adapters or test doubles before introducing a new port.
Introduce dependency injection only when a concrete production or testing need justifies the separation.
A test substitute does not justify exposing every internal collaborator to callers.
Match claims to coverage. A substitute cannot prove real transport behavior or compatibility with a deployed service.

## Preserve knowledge and existing behavior

Use the project's domain terms. Read existing architecture decisions before revisiting a settled choice.
Record a durable decision when it is hard to reverse, surprising without context, and chosen between real alternatives.
Follow existing documentation conventions. A missing glossary does not require creating one for every task.

For structural changes, pin the observable behavior first, with adequate existing coverage or a focused characterization check.
Move in verifiable steps. Account for every affected caller and representation within scope.
Contract compatibility and deployment order can require a staged migration.
Replace redundant tests only after equivalent behavior coverage exists and deletion is authorized.

## Review questions

- What responsibility does this module own?
- What must callers understand to use it correctly?
- Which complexity does the interface hide?
- Does the change concentrate knowledge or duplicate it?
- Does each new abstraction pass the deletion test?
- Does representative verification exercise the operation that changed?
- Which existing decisions and compatibility requirements constrain the change?

Report concrete structural problems and what they will cost future maintainers. Use these questions for judgment, not as a score.
