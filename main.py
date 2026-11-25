#!/usr/bin/env python3
"""news-image-20261125: write the front page of 25 November 2026 to /output/entry.png.

The image is a 1024x1024 PNG drawn at build time (see render.py in the
build directory): a newspaper front page, "THE WORLD IN ONE DAY", summing
up Wednesday 25 November 2026 in 35 stories -- 3 big illustrated stories,
10 small illustrated cards, and a 22-item list, plus a KPI strip of the
day's big numbers, a numbered world map, and a DATE CHECK box that names
the 18-23 November stories deliberately left out. Every story carries its
source; every illustration is drawn in code. This program only copies the
PNG the repository holds, so it needs no network and writes identical
bytes on every run.
"""
import os
import shutil

MAX_BYTES = 1048576


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    with open(dst, "rb") as fh:
        magic = fh.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        os.remove(dst)
        raise SystemExit("entry.png is not a PNG file")
    if os.path.getsize(dst) > MAX_BYTES:
        os.remove(dst)
        raise SystemExit("entry.png is larger than 1 MiB")


if __name__ == "__main__":
    main()
