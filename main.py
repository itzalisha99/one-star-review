#!/usr/bin/env python3
"""One-Star Review of Something Essential — make.fun entry.

Writes one single-line deadpan one-star review of sleep to
/output/entry.txt. Stdlib only, deterministic.
"""

import os

REVIEW = (
    "Sleep takes a third of my life, charges me eight hours a night, "
    "and delivers a version of me that is still tired. One star."
)


def validate(text: str) -> None:
    """Mirror the bounty gate: 1-160 chars, UTF-8, not only whitespace."""
    if not text or text != text.strip() or text.isspace():
        raise ValueError("review must not be empty or only whitespace")
    if len(text) > 160:
        raise ValueError(f"review is {len(text)} chars, over the 160 cap")
    if "\n" in text or "\r" in text:
        raise ValueError("review must be a single line")
    text.encode("utf-8")


def main() -> None:
    validate(REVIEW)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
