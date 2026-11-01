import argparse
import json
import sys

from .core import count_file


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="tally", description="Count lines, words and characters.")
    p.add_argument("--json", action="store_true", help="print a JSON array, one object per file (FR-004)")
    p.add_argument("files", nargs="+")
    args = p.parse_args(argv)
    status = 0
    results = []
    for f in args.files:
        try:
            c = count_file(f)
        except OSError as e:
            print(f"tally: {f}: {e.strerror}", file=sys.stderr)
            status = 1
            continue
        if args.json:
            results.append({"file": f, "lines": c.lines, "words": c.words, "chars": c.chars})
        else:
            print(f"{c.lines:>7} {c.words:>7} {c.chars:>7} {f}")
    if args.json:
        print(json.dumps(results))
    return status


if __name__ == "__main__":
    sys.exit(main())
