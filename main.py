"""One-line roast: the gadget I use every day.

Writes a single original roast line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Stdlib only. Deterministic: the same bytes on every run.
"""

import os

LINE = "My earbuds pair with my neighbour's TV before they pair with my phone."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    text = LINE.strip()
    if "\n" in text or not 1 <= len(text) <= 200:
        raise SystemExit("roast line must be one line of 1-200 characters")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
