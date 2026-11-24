"""One-Liner Marathon entry: writes a single one-line joke to /output/entry.txt.

The gate requires /output/entry.txt to be UTF-8 text of 1 to 280
characters, not only whitespace, so the program validates the line
before writing it.
"""

import os

JOKE = "I bought a standing desk to get healthier. Now I just sit on a taller chair."

MAX_CHARS = 280


def validate(line):
    """Check the entry against the competition gate."""
    if not line or line != line.strip():
        raise ValueError("entry must be non-empty with no surrounding whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError("entry is over %d characters" % MAX_CHARS)
    return line


def main():
    line = validate(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
