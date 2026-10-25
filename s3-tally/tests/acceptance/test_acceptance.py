"""Acceptance checks for SPEC-001. Owned by the verification role; implementers must not edit
this directory (CODEOWNERS, AGENTS.md). AC-004 fails until TASK-001 is implemented."""
import json

from tally.cli import main


def test_ac_001_plain_output(tmp_path, capsys):          # AC-001 -> FR-001, FR-002
    f = tmp_path / "x.txt"
    f.write_text("one two\nthree\n", encoding="utf-8")
    assert main([str(f)]) == 0
    assert capsys.readouterr().out.split()[:3] == ["2", "3", "14"]


def test_ac_002_missing_file_status(tmp_path, capsys):   # AC-002 -> FR-003
    assert main([str(tmp_path / "missing.txt")]) == 1


def test_ac_004_json_output(tmp_path, capsys):           # AC-004 -> FR-004 (TASK-001)
    f = tmp_path / "x.txt"
    f.write_text("one two\nthree\n", encoding="utf-8")
    assert main(["--json", str(f)]) == 0
    out = json.loads(capsys.readouterr().out)
    assert out == [{"file": str(f), "lines": 2, "words": 3, "chars": 14}]
