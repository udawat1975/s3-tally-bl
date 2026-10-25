from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Counts:
    lines: int
    words: int
    chars: int


def count_text(text: str) -> Counts:
    """Count lines, whitespace-separated words and characters (FR-001)."""
    lines = text.count("\n") + (1 if text and not text.endswith("\n") else 0)
    return Counts(lines=lines, words=len(text.split()), chars=len(text))


def count_file(path: str | Path, encoding: str = "utf-8") -> Counts:
    """Count a file's contents (FR-002)."""
    return count_text(Path(path).read_text(encoding=encoding))
