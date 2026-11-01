import json

from tally.cli import main


def test_json_argument_order(tmp_path, capsys):          # FR-004
    a = tmp_path / "a.txt"
    b = tmp_path / "b.txt"
    a.write_text("x\n", encoding="utf-8")
    b.write_text("y z\n", encoding="utf-8")
    assert main(["--json", str(b), str(a)]) == 0
    out = json.loads(capsys.readouterr().out)
    assert [o["file"] for o in out] == [str(b), str(a)]


def test_json_missing_file(tmp_path, capsys):             # FR-003 with FR-004
    a = tmp_path / "a.txt"
    a.write_text("x\n", encoding="utf-8")
    assert main(["--json", str(tmp_path / "missing.txt"), str(a)]) == 1
    captured = capsys.readouterr()
    assert json.loads(captured.out) == [{"file": str(a), "lines": 1, "words": 1, "chars": 2}]
    assert "missing.txt" in captured.err
