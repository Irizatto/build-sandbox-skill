from __future__ import annotations

import argparse
import json
import shutil
import tempfile
from pathlib import Path
from typing import Any


DRAFT_REQUIRED = {
    "stable_id",
    "version",
    "domain_id",
    "competition",
    "ruleset",
    "participants",
    "eligible_pool",
    "phases",
    "terminal_states",
    "lineup_constraints",
    "tests",
}


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def rows(payload: Any, key: str) -> list[dict[str, Any]]:
    if isinstance(payload, dict) and isinstance(payload.get(key), list):
        return [row for row in payload[key] if isinstance(row, dict)]
    if isinstance(payload, dict):
        return [payload]
    if isinstance(payload, list):
        return [row for row in payload if isinstance(row, dict)]
    return []


def validate(package: Path) -> dict[str, Any]:
    errors: list[str] = []
    incomplete: list[str] = []
    parsed: dict[Path, Any] = {}
    for path in package.rglob("*.json"):
        try:
            parsed[path] = read_json(path)
        except Exception as error:
            errors.append(f"invalid JSON {path.relative_to(package)}: {error}")

    profile_path = package / "01_Domain" / "domain_profile.json"
    profile = parsed.get(profile_path)
    if not isinstance(profile, dict):
        errors.append("competitive domain profile missing")
        profile = {}
    elif profile.get("domain_id") != "competitive_rules":
        errors.append(f"unexpected domain_id: {profile.get('domain_id')!r}")
    if profile.get("crossover_policy") == "forbidden" and profile.get("secondary_domains"):
        errors.append("secondary domains declared while crossover is forbidden")

    draft_contracts: list[tuple[Path, dict[str, Any]]] = []
    mechanics_root = package / "07_Mechanics"
    if mechanics_root.exists():
        for path, payload in parsed.items():
            try:
                relative = path.relative_to(mechanics_root)
            except ValueError:
                continue
            if path.name.endswith("schema.json") or relative.parts[0].startswith("."):
                continue
            for row in rows(payload, "drafts"):
                if "phases" in row or "eligible_pool" in row:
                    draft_contracts.append((path, row))
    if not draft_contracts:
        incomplete.append("no competitive draft contract found")

    for path, draft in draft_contracts:
        label = str(draft.get("stable_id", path.name))
        missing = sorted(DRAFT_REQUIRED - set(draft))
        if missing:
            errors.append(f"draft {label} missing fields: {missing}")
            continue
        if draft.get("domain_id") != "competitive_rules":
            errors.append(f"draft {label} domain mismatch")
        participants = draft.get("participants", [])
        if not isinstance(participants, list) or len(participants) < 2:
            errors.append(f"draft {label} requires at least two participants")

        pool = draft.get("eligible_pool", [])
        pool_ids = [item.get("id") if isinstance(item, dict) else item for item in pool] if isinstance(pool, list) else []
        if not pool_ids or any(not isinstance(item, str) or not item for item in pool_ids):
            errors.append(f"draft {label} has invalid eligible pool IDs")
        if len(pool_ids) != len(set(pool_ids)):
            errors.append(f"draft {label} has duplicate eligible pool IDs")

        phases = draft.get("phases", [])
        phase_ids = [phase.get("id") for phase in phases if isinstance(phase, dict)] if isinstance(phases, list) else []
        if not phase_ids or any(not isinstance(item, str) or not item for item in phase_ids):
            errors.append(f"draft {label} has invalid phase IDs")
        if len(phase_ids) != len(set(phase_ids)):
            errors.append(f"draft {label} has duplicate phase IDs")
        terminals = set(item for item in draft.get("terminal_states", []) if isinstance(item, str))
        allowed_targets = set(phase_ids) | terminals
        for phase in phases if isinstance(phases, list) else []:
            if not isinstance(phase, dict):
                errors.append(f"draft {label} contains a non-object phase")
                continue
            for field in ("id", "actor", "action_type", "count", "visibility", "next_phase"):
                if field not in phase:
                    errors.append(f"draft {label} phase {phase.get('id', '<unknown>')} missing {field}")
            target = phase.get("next_phase")
            if isinstance(target, str) and target not in allowed_targets:
                errors.append(f"draft {label} phase {phase.get('id')} targets unknown phase {target}")
            if isinstance(phase.get("actor"), str) and phase["actor"] not in participants:
                errors.append(f"draft {label} phase {phase.get('id')} uses unknown participant {phase['actor']}")
            if isinstance(phase.get("count"), int) and phase["count"] < 1:
                errors.append(f"draft {label} phase {phase.get('id')} has non-positive count")

        constraints = draft.get("lineup_constraints")
        if not isinstance(constraints, dict) or not isinstance(constraints.get("size"), int) or constraints.get("size", 0) < 1:
            errors.append(f"draft {label} needs a positive lineup size")

    matchup_required = {"subject", "relation_type", "ruleset_version", "contexts", "confidence", "provenance", "timestamp"}
    for path, payload in parsed.items():
        if "matchup" not in path.name.casefold():
            continue
        for row in rows(payload, "matchups"):
            missing = sorted(matchup_required - set(row))
            if missing:
                errors.append(f"matchup in {path.relative_to(package)} missing fields: {missing}")
            confidence = row.get("confidence")
            if confidence is not None and (not isinstance(confidence, (int, float)) or not 0 <= confidence <= 1):
                errors.append(f"matchup in {path.relative_to(package)} has invalid confidence")

    forbidden = profile.get("forbidden_vocabulary", []) if isinstance(profile, dict) else []
    for dirname in ["02_Player", "03_Context", "04_Actors", "05_Organizations", "06_Locations", "07_Mechanics", "08_State", "09_Knowledge", "10_History", "11_Runtime"]:
        root = package / dirname
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file() or path.name.endswith("schema.json") or path.suffix.lower() not in {".json", ".md", ".txt", ".yaml", ".yml"}:
                continue
            text = path.read_text(encoding="utf-8", errors="replace").casefold()
            for term in forbidden:
                if isinstance(term, str) and term and term.casefold() in text:
                    errors.append(f"unrelated domain vocabulary {term!r} in {path.relative_to(package)}")
                    break

    status = "fail" if errors else ("incomplete" if incomplete else "pass")
    return {"status": status, "package": str(package), "draft_contracts": len(draft_contracts), "errors": errors, "incomplete": incomplete}


def valid_fixture(root: Path) -> None:
    profile = json.loads((Path(__file__).resolve().parents[1] / "assets" / "competitive_domain_profile.json").read_text(encoding="utf-8"))
    write_json(root / "01_Domain" / "domain_profile.json", profile)
    write_json(
        root / "07_Mechanics" / "draft.json",
        {
            "stable_id": "DRAFT_TEST_001",
            "version": "1",
            "domain_id": "competitive_rules",
            "competition": {"id": "COMP_TEST"},
            "ruleset": {"id": "RULE_TEST", "version": "1"},
            "participants": ["side_a", "side_b"],
            "eligible_pool": ["unit_a", "unit_b", "unit_c", "unit_d"],
            "phases": [
                {"id": "p1", "actor": "side_a", "action_type": "select", "count": 1, "visibility": "public", "next_phase": "p2"},
                {"id": "p2", "actor": "side_b", "action_type": "select", "count": 1, "visibility": "public", "next_phase": "complete"}
            ],
            "terminal_states": ["complete"],
            "lineup_constraints": {"size": 1, "unique": True},
            "tests": ["legal_sequence", "duplicate_rejected"]
        },
    )


def self_test() -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="competitive-validator-") as temp:
        good = Path(temp) / "good"
        valid_fixture(good)
        good_status = validate(good)["status"]

        bad_transition = Path(temp) / "bad-transition"
        shutil.copytree(good, bad_transition)
        payload = read_json(bad_transition / "07_Mechanics" / "draft.json")
        payload["phases"][0]["next_phase"] = "missing"
        write_json(bad_transition / "07_Mechanics" / "draft.json", payload)

        duplicate_pool = Path(temp) / "duplicate-pool"
        shutil.copytree(good, duplicate_pool)
        payload = read_json(duplicate_pool / "07_Mechanics" / "draft.json")
        payload["eligible_pool"].append("unit_a")
        write_json(duplicate_pool / "07_Mechanics" / "draft.json", payload)

        domain_leak = Path(temp) / "domain-leak"
        shutil.copytree(good, domain_leak)
        (domain_leak / "03_Context").mkdir(parents=True, exist_ok=True)
        (domain_leak / "03_Context" / "packet.txt").write_text("宗门", encoding="utf-8")

        mutations = {
            "missing_phase": validate(bad_transition)["status"],
            "duplicate_pool": validate(duplicate_pool)["status"],
            "domain_leak": validate(domain_leak)["status"],
        }
        ok = good_status == "pass" and all(status == "fail" for status in mutations.values())
        return {"status": "pass" if ok else "fail", "good_fixture": good_status, "mutations": mutations}


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a competitive rules sandbox")
    parser.add_argument("--package", type=Path)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        report = self_test()
        print(json.dumps(report, ensure_ascii=False, indent=2))
        raise SystemExit(0 if report["status"] == "pass" else 1)
    if not args.package:
        parser.error("--package is required unless --self-test is used")
    package = args.package.resolve()
    if not package.is_dir():
        raise SystemExit(f"Package directory not found: {package}")
    report = validate(package)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    failed = report["status"] == "fail" or (args.strict and report["status"] != "pass")
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
