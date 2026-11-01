import json

from tally.cli import main


def test_json_multiple_files_in_argument_order(tmp_path, capsys):
    a = tmp_path / "a.txt"
    b = tmp_path / "b.txt"
    a.write_text("x\n", encoding="utf-8")
    b.write_text("one two three", encoding="utf-8")
    assert main(["--json", str(b), str(a)]) == 0
    assert json.loads(capsys.readouterr().out) == [
        {"file": str(b), "lines": 1, "words": 3, "chars": 13},
        {"file": str(a), "lines": 1, "words": 1, "chars": 2},
    ]


def test_json_missing_file_reported_and_status_1(tmp_path, capsys):
    a = tmp_path / "a.txt"
    a.write_text("x\n", encoding="utf-8")
    missing = tmp_path / "missing.txt"
    assert main(["--json", str(missing), str(a)]) == 1
    captured = capsys.readouterr()
    assert json.loads(captured.out) == [{"file": str(a), "lines": 1, "words": 1, "chars": 2}]
    assert "missing.txt" in captured.err
