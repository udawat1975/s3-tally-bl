import argparse
import sys

from .core import count_file


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="tally", description="Count lines, words and characters.")
    p.add_argument("files", nargs="+")
    args = p.parse_args(argv)
    status = 0
    for f in args.files:
        try:
            c = count_file(f)
        except OSError as e:
            print(f"tally: {f}: {e.strerror}", file=sys.stderr)
            status = 1
            continue
        print(f"{c.lines:>7} {c.words:>7} {c.chars:>7} {f}")
    return status


if __name__ == "__main__":
    sys.exit(main())
