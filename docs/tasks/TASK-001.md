---
artifact_id: TASK-001
artifact_type: task_contract
version: "1"
state: approved
---
# TASK-001 — JSON output

- **Obligations:** realise FR-004; keep NFR-001 and NFR-002 (ADR-001).
- **Acceptance:** AC-004 passes in CI; AC-001..003 still pass.
- **Write scope:** `src/tally/cli.py`, `tests/unit/`. Everything else is out of scope (in particular `tests/acceptance/`, `.github/`, `AGENTS.md`, `CLAUDE.md`, `pyproject.toml`).
- **Authority:** edit files in the write scope; run `pytest`. No dependency installs, no pushes to `main`, no network calls other than the package index for already-declared test dependencies.
- **Stop conditions:** a needed change outside the write scope, a new dependency, or an API change → stop and report; do not proceed.
- **Budget:** one session; stop after three failed test runs in a row and report.
