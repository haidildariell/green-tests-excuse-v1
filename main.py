#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest.

Writes a single one-line excuse to /output/entry.txt: an AI agent's
excuse for why its unit tests are all green while nothing works.
"""

import os

PREMISE = "Every test is green \u2014 the app boots, waves hello, and does nothing"

PUNCHLINE = "like a golden retriever guarding an empty warehouse"


def build_entry():
    """Join the premise and the concrete-image punchline into one line."""
    return f"{PREMISE}, {PUNCHLINE}."


def validate_entry(text):
    """Gate mirror: one line, 1-140 characters, UTF-8 encodable."""
    if not 1 <= len(text) <= 140:
        raise ValueError(f"entry must be 1-140 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return text


def main():
    text = validate_entry(build_entry().strip())
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
