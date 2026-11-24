#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line.

Writes one sentence (at most 200 characters) about a small moment of
wonder in everyday life to /output/entry.txt. Python 3.13 stdlib only,
no network, deterministic.
"""

import os

SENTENCE = (
    "My shadow on the wet pavement walked half a step ahead of me, "
    "as if it had somewhere to be before I did."
)


def main() -> None:
    sentence = SENTENCE
    assert sentence.strip(), "sentence must not be only whitespace"
    assert 1 <= len(sentence) <= 200, (
        f"sentence must be 1-200 characters, got {len(sentence)}"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(sentence)


if __name__ == "__main__":
    main()
