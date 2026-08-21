from __future__ import annotations

import json
import subprocess
from pathlib import Path


def git_tree(repo_root: Path, path: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo_root), "rev-parse", f"HEAD:{path}"],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    manifest_path = repo_root / "vendor_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    failures: list[str] = []
    rows: list[dict[str, str | bool]] = []

    for mode, spec in manifest["modes"].items():
        path = spec["vendored_path"]
        expected = spec["source_tree"]
        actual = git_tree(repo_root, path)
        contract = repo_root / spec["required_contract"]
        ok = actual == expected and contract.is_file()
        rows.append(
            {
                "mode": mode,
                "path": path,
                "expected_tree": expected,
                "actual_tree": actual,
                "contract_exists": contract.is_file(),
                "pass": ok,
            }
        )
        if not ok:
            failures.append(mode)

    print(json.dumps({"status": "PASS" if not failures else "FAIL", "modes": rows}, indent=2))
    if failures:
        raise SystemExit(f"Vendored mode parity failed: {', '.join(failures)}")


if __name__ == "__main__":
    main()
