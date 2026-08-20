from __future__ import annotations

import argparse
import runpy
import sys
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a build-sandbox package by form")
    parser.add_argument("--mode", choices=["generic", "cultivation"], required=True)
    args, forwarded = parser.parse_known_args()
    script = Path(__file__).resolve().parents[1] / "modes" / args.mode / "scripts" / "scaffold_sandbox.py"
    sys.argv = [str(script), *forwarded]
    runpy.run_path(str(script), run_name="__main__")


if __name__ == "__main__":
    main()
