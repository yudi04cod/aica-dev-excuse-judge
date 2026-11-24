"""Aica Dev Excuse — make.fun entry.

Writes one funny single-line excuse a developer gives when code breaks
in production to /output/entry.txt.
"""

import os

ENTRY = (
    "It worked in staging because staging is just my laptop with a "
    "fancier hostname \u2014 and my laptop has never met a real user, "
    "a real timezone, or a real database."
)


def validate(entry: str) -> None:
    """Check the entry before writing it: one non-empty line, 1-200 chars."""
    if not entry or not entry.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if not 1 <= len(entry) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(entry)}")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
