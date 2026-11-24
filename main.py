#!/usr/bin/env python3
"""Two Lines to Your Past Self — make.fun entry.

Writes exactly two lines to /output/entry.txt:
line 1 warns the past self about one specific moment;
line 2 says why that moment mattered and what changed because of it.
Python 3.13 standard library only; deterministic output — the same
bytes on every run, no randomness, no network, no file reads.
"""

import os

ENTRY = (
    "Don't delete your grandmother's voicemail on 3 October \u2014 save it, "
    "because it is the last time you will ever hear her voice.\n"
    "You replayed it every birthday after she died, and hearing her laugh "
    "again taught you to call the people you love before it is too late.\n"
)


def _validate(text: str) -> None:
    """Gate: exactly two lines, one sentence each, 1-280 chars, non-blank."""
    lines = text.rstrip("\n").split("\n")
    assert len(lines) == 2, "entry must be exactly two lines"
    assert all(line.strip() for line in lines), "no blank lines allowed"
    assert 1 <= len(text.rstrip("\n")) <= 280, "entry must be 1-280 characters"
    assert all(line.count(".") >= 1 for line in lines), "one sentence per line"


def main() -> None:
    _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
