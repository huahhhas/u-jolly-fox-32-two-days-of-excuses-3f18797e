#!/usr/bin/env python3
"""Write the entry line for u-jolly-fox-32-two-days-of-excuses-3f18797e.

Writes exactly one line (no trailing newline) to $OUTPUT_DIR/entry.txt
(default /output) and self-verifies the written file: UTF-8, length within
the 1-200 character gate, exact match, no trailing newline, byte-identical.
Stdlib only.
"""

import os
import sys

LINE = "I finished it three days early \u2014 in the simulation where I actually started on time."


def main() -> int:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    # Self-verify the written file.
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        print("self-check failed: file bytes differ from expected line", file=sys.stderr)
        return 1
    text = written.decode("utf-8")  # raises if not valid UTF-8
    if not (1 <= len(text) <= 200):
        print(f"self-check failed: length {len(text)} outside 1-200", file=sys.stderr)
        return 1
    if text.strip() == "":
        print("self-check failed: only whitespace", file=sys.stderr)
        return 1
    if text.endswith("\n"):
        print("self-check failed: trailing newline", file=sys.stderr)
        return 1
    if "\n" in text:
        print("self-check failed: not a single line", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(text)} chars, {len(written)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
