#!/usr/bin/env python3
"""Entry for make.fun bounty 'The Most Shameless Lie'.

Writes the one-line entry text to /output/entry.txt with no
trailing newline.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

ENTRY_TEXT = "I read the whole document"


def main() -> None:
    output_dir = os.path.dirname(OUTPUT_PATH)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
