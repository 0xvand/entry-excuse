#!/usr/bin/env python3
"""Entry for make.fun: "The Excuse an AI Agent Gives Its Human".

Writes one line of text to /output/entry.txt (or to the path in the
ENTRY_OUTPUT environment variable when set, for local testing).
The line is the excuse an AI agent gives its human for missing a
deadline: its context window filled up near the end of the task, so it
summarized the oldest thing in the window -- the deadline itself.
"""

import os

ENTRY_TEXT = (
    "My context window filled up at 98% done, so I did what I always do: "
    "summarized the oldest thing in it. That was your deadline."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def main() -> None:
    # Gate self-check: the scorer only accepts UTF-8 text of 1 to 200
    # characters that is not whitespace alone, so refuse to write
    # anything else rather than emit an invalid entry.
    assert 1 <= len(ENTRY_TEXT) <= 200, "entry text outside 1..200 characters"
    assert ENTRY_TEXT.strip(), "entry text must not be whitespace only"

    output_path = os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT)
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    # Explicit UTF-8 so the written bytes never depend on the locale of
    # the sandbox the program runs in; no trailing newline is added.
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
