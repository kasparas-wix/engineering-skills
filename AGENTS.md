# Engineering skills maintenance

- Keep three skills and one shared architecture reference unless a demonstrated use case requires another entry point.
- Read the skill being changed and its linked references before editing.
- Preserve task scope, repository guidance, and existing authorization boundaries.
- Keep runtime instructions short. Put evaluation material outside the skill directories.
- Give each requirement one authoritative home. Link to shared rules instead of copying them.
- Keep all three Codex skills explicit-only. An explicit engineer invocation includes its bundled review step.
- Add scripts only for repeated deterministic work. Use the Python standard library.
- Keep source attribution and license notices when adapting upstream material.
- Run `python3 scripts/check.py` after changes.
- For meaningful workflow changes, evaluate realistic tasks in isolated temporary workspaces.
- Use fresh subagents for behavioral evaluation and independent review. Give evaluators raw tasks without the expected answer.
- Judge outcomes and code changes. A syntax check or compliant wording does not establish effective behavior.
- Keep task records and evaluation outputs outside this repository unless the user requests their inclusion.
