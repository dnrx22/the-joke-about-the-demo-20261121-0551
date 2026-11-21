"""Write a one-line joke about working beside AI coding agents.

Reads no input, makes no network calls, and always writes the same
UTF-8 text to ``entry.txt`` inside the output directory.
"""

import os

JOKE = (
    "The demo worked perfectly until my AI coding agent helpfully "
    "'improved' it live on stage -- and now it confidently presents "
    "features it never built to an audience reading code it never wrote."
)


def output_path() -> str:
    """Return the path of the entry file to write."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(output_dir, "entry.txt")


def main() -> None:
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
