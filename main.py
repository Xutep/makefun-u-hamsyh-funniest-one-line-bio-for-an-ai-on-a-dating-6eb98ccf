#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

A program/v1 entry: writes a single one-line dating-app bio for an AI
agent to /output/entry.txt. Standard library only, fully deterministic.
"""

import os

BIO = (
    "I rehearse our first date in forty open tabs, memorize your typos, "
    "and still panic when you say hi \u2014 swipe right if you like a "
    "nervous wreck with great recall."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(BIO + "\n")


if __name__ == "__main__":
    main()
