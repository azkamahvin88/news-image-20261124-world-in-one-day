"""Entry program for make.fun news-image-20261124.

Copies the entry image (entry.png, drawn during the build from the day's
news) to /output/entry.png. Standard library only, no network, no clock,
no randomness: the same bytes come out on every run. The image itself is
the deliverable; this program is only the deterministic courier that
places it where the grader expects it.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.png", OUT_DIR / "entry.png")


if __name__ == "__main__":
    main()
