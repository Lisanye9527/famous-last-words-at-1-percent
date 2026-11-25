#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun entry.

Writes one line of a phone's last words, spoken as its battery hits
1 percent, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
The line is a fixed constant, so every run produces byte-identical output.
"""

import os
import sys

ENTRY = (
    "Battery at 1%. My last spark goes to deleting your 6 a.m. alarm. "
    "Sleep in — when work asks, say your phone died. "
    "For once, it'll be the truth."
)

MAX_CHARS = 199


def check_gate(text: str) -> None:
    if not text or not text.strip():
        raise SystemExit("gate fail: entry is empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("gate fail: entry must be a single line")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"gate fail: entry is {len(text)} chars, max {MAX_CHARS}")
    text.encode("utf-8")  # must be UTF-8 encodable


def main() -> int:
    check_gate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    with open(path, "rb") as fh:
        back = fh.read()
    if back != data:
        raise SystemExit("verify fail: written bytes differ from entry")
    print(f"wrote {path}: {len(ENTRY)} chars, {len(data)} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
