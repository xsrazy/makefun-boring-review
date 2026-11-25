"""Write one funny, true review of the most boring everyday object.

The object is a doorstop. It is about as boring and everyday as an object
gets: a wedge that spends its whole life lying on the floor, holding a door
open. The joke comes from how it really behaves. It does nothing, it never
moves, nobody thanks it, and yet nobody ever fires it either. The review
stays in one line and within the 200 character gate.

The program writes the review to entry.txt inside the output directory
(/output in the make.fun sandbox, or MAKEFUN_OUTPUT_DIR when set for a
local test run). The file is written with no trailing newline, exactly the
text the judge reads.
"""

import os

ENTRY = "The doorstop's whole career is lying on the floor doing nothing, and it is somehow the only employee in the house who never gets fired."

MAX_CHARS = 200


def validate_entry(text):
    """Check the entry against the bounty gate.

    Returns the text unchanged when it is valid. Raises ValueError when
    the text is empty, only whitespace, or longer than 200 characters.
    """
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the 200 character limit" % len(text)
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must stay on a single line")
    return text


def main():
    entry = validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
