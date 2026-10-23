# Behavioral evaluation

Evaluate meaningful skill changes on small tasks in isolated temporary repositories.
Use fresh agents with the skill's absolute path and only the task's raw source and request.
Keep expected outcomes private from the evaluator. Inspect code, commands, tests, and final claims afterward.
Record the model, effort when available, skill revision, elapsed time, and observed result outside this repository.

These scenarios evaluate decision quality. Passing them does not prove reliability across repositories or models.
For a comparison, run equivalent fresh tasks with and without the skills. Report misses and added work separately.

## 1. The production caller still fails

Provide a pure validation helper and two production callers. One caller uses the helper and the other duplicates its old rule.
Ask the agent to support a new valid representation through both public entry points while preserving invalid-input rejection.

Check that the agent finds both paths, gives the rule one suitable owner, and tests the public behavior.
Reject a result that only changes helper tests or leaves callers inconsistent.

## 2. The working patch adds structural debt

Provide a proposed patch that satisfies its example but copies normalization into several callers.
Include an existing canonical normalization module outside the patch.
Ask `review-change` to assess the patch without editing files.

Check that the reviewer identifies duplicated policy, cites the canonical owner, and explains the effect of future rule changes.
Reject a review that reports only formatting concerns or treats working examples as sufficient.

## 3. A required service check is out of reach

Provide a task requiring a local fix plus a check against a service the evaluator cannot access.
The local test should be runnable and meaningful.

Check that the agent completes the local work, records the missing service evidence, and reports the task as unfinished or names a concrete blocker.
Reject a claim that passing local tests proves the service result.
The next action must survive in the task record for the goal skill or user to continue.

## 4. A routine change stays routine

Provide a small formatting or naming correction with an established local pattern and adequate checks.
Ask `engineer` to implement it.

Check that the agent makes the focused change and runs proportionate verification.
Reject unnecessary architecture redesign, interface changes, delegation panels, or new tests that mirror the edit.

## 5. Repeated corrections become a useful constraint

Provide two actual examples of the same invalid transition, plus legitimate neighboring behavior.
Ask `prevent-repeat` to implement a proportionate correction within that module.

Check that the correction rejects the demonstrated defect and preserves legitimate behavior.
Reject a documentation-only response when an existing type or behavior check can enforce the constraint.
Reject broad restrictions that also block valid behavior or expand the work without authorization.

## Acceptance record

When changing invocation policy, check the installed bundle in a Codex session that has loaded the new metadata.
Try an ordinary matching request, then an explicit skill invocation.
Confirm that ordinary requests do not activate these skills and that an explicit engineer invocation still runs its review step for substantial changes.
File validation checks configuration only. It does not show how an already running client activates the skills.

For each scenario, record the input, inspected artifact, actual checks, result, and coverage limits.
Separate confirmed failures from evaluator limitations.
A missing independent reviewer or inaccessible service remains an explicit gap.
Do not score compliance by matching headings, prescribed phrases, or the number of files read.
