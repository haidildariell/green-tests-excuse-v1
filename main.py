"""Green Tests, Nothing Works entry: write one funny excuse to /output/entry.txt."""

import os

SETUP = "The tests are green because I tested the code I wished I'd written,"
TURN = "not the code I shipped."


def build_excuse():
    """Compose the excuse from its setup and its turn."""
    return SETUP + " " + TURN


EXCUSE = build_excuse()


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
