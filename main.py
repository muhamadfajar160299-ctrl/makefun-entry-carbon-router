"""Router confession entry writer.

Reads entry.txt next to this script and writes it to
$MAKEFUN_OUTPUT_DIR/entry.txt for the grader.

The entry is one line, 1-200 characters, UTF-8. This writer only
copies and validates it; the joke itself lives in entry.txt.
"""

import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.txt")
    try:
        with open(src, "r", encoding="utf-8") as f:
            line = f.read()
    except OSError as exc:
        raise SystemExit("cannot read entry.txt: %s" % exc)
    line = line.strip()
    if not line:
        raise SystemExit("entry.txt is empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if len(line) > 200:
        raise SystemExit("entry exceeds 200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        dst = os.path.join(out_dir, "entry.txt")
        with open(dst, "w", encoding="utf-8", newline="\n") as f:
            f.write(line + "\n")
    except OSError as exc:
        raise SystemExit("cannot write output: %s" % exc)
    return 0


if __name__ == "__main__":
    sys.exit(main())
