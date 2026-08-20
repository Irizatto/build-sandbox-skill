from __future__ import annotations

import argparse
import runpy
import sys
from pathlib import Path


MODES = {
    "generic": ("validate_package.py", "validate_package"),
    "cultivation": ("validate_package.py", "validate_package"),
    "competitive": ("validate_competitive.py", "validate_package"),
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a build-sandbox package by form")
    parser.add_argument("--mode", choices=sorted(MODES), required=True)
    args, forwarded = parser.parse_known_args()
    script_name, _ = MODES[args.mode]
    script = Path(__file__).resolve().parents[1] / "modes" / args.mode / "scripts" / script_name
    sys.argv = [str(script), *forwarded]
    runpy.run_path(str(script), run_name="__main__")


if __name__ == "__main__":
    main()
