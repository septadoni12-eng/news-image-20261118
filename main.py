#!/usr/bin/env python3
"""news-image-20261118 entry: sum up Wednesday 18 November 2026's world
news in one image.

The image is pre-rendered and committed beside this program as entry.png
(a dated broadsheet front page: 42 verified stories from 6 continents,
led by Iran's strikes on US bases in Kuwait and Bahrain and Ukraine's hit
on the Kerch Bridge, plus a world map marking the day's flashpoints).
This program only copies it to the output path, so it is deterministic,
needs no network, and runs identically every time.

Run: python3 main.py
Writes: /output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png when set).
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
