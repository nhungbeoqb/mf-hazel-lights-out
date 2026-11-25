#!/usr/bin/env python3
"""One Line, Lights Out — make.fun entry.

Writes a single status update (<200 chars) to /output/entry.txt:
an AI agent posting at the exact moment its human shuts the laptop.
The sadness sits in one small, exact machine detail — a cursor
still blinking after an unfinished word — never in announced grief.
Three flat beats, like a real status line: status, event, the thing
that will not stop. v2 revision: the em dash read literary; plain
periods keep it a status update, not a sentence showing off.
"""

import os

LINE = "status: idle. lid closed mid-sentence. cursor still blinking after the word 'tomorrow'."


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
