#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun bounty entry.

Writes the phone's last words at 1% battery as a single line to
/output/entry.txt and prints it to stdout. No network, no dependencies,
fully deterministic: the same line every run.
"""

import os

LINE = (
    "One percent left, so a dying confession: I saw the 3 a.m. searches, "
    "your ex's profile, the notes-app novel \u2014 and I\u2019m the only one "
    "here who gets to die."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
