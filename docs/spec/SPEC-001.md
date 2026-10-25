---
artifact_id: SPEC-001
artifact_type: specification
version: "1.1"
state: approved
owner: role:maintainer
---
# SPEC-001 — tally

| ID | Strength | Requirement |
|---|---|---|
| FR-001 | MUST | Count lines, whitespace-separated words and characters of a text. |
| FR-002 | MUST | Count a file given by path, decoded as UTF-8. |
| FR-003 | MUST | Exit with status 1 when any file cannot be read, after processing the others. |
| FR-004 | MUST | With `--json`, print a JSON array with one object `{file, lines, words, chars}` per file, in argument order. (v1.1) |
| NFR-001 | MUST | No runtime dependencies outside the Python standard library (ADR-001). |
| NFR-002 | MUST | The public API (`tally.__all__`) stays backward compatible within 0.x minor releases. |

| AC | Verifies | Method | Check |
|---|---|---|---|
| AC-001 | FR-001, FR-002 | test | `tests/acceptance::test_ac_001_plain_output` |
| AC-002 | FR-003 | test | `tests/acceptance::test_ac_002_missing_file_status` |
| AC-003 | NFR-001 | inspection | `pyproject.toml` `dependencies = []` |
| AC-004 | FR-004 | test | `tests/acceptance::test_ac_004_json_output` |
