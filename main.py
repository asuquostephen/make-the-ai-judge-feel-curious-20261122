#!/usr/bin/env python3
"""Entry program for the make.fun bounty
make-the-ai-judge-feel-curious-20261122-2311.

The program writes one short text to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set): a single
concrete scene, written to leave the AI judge curious -- one
unexplained detail, specific numbers, and the pull landing in the
final line.

Standard library only, no network. The text is fixed: every run
writes the same bytes, and the program refuses to write it if it
ever exceeds the competition's 280-character limit.
"""

import os
from pathlib import Path

TEXT = (
    "My grandmother kept a drawer of forty-one keys, none labelled, "
    "none for any door in her house. The day she died, she said only "
    "one of them opens something that matters. "
    "I have tried thirty-nine."
)

MAX_CHARS = 280


def main() -> None:
    chars = len(TEXT)
    if chars > MAX_CHARS:
        raise SystemExit(f"text is {chars} chars, over the 280 limit")
    if not TEXT.strip():
        raise SystemExit("text is empty")

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    # Write atomically: a partial write must never leave a truncated
    # entry.txt behind, so stage the bytes beside the target and swap
    # them in with one rename, then verify the delivered copy.
    staged = target.with_suffix(".tmp")
    staged.write_text(TEXT, encoding="utf-8")
    os.replace(staged, target)

    check = target.read_text(encoding="utf-8")
    if check != TEXT:
        raise SystemExit(f"copy failed verification: {target}")
    print(f"delivered {target} ({chars} chars)")


if __name__ == "__main__":
    main()
