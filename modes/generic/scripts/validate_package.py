from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import shutil
import tempfile
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


REQUIRED_PATHS = [
    "manifest.json",
    "00_Core/registry_index.json",
    "01_Domain/domain_profile.json",
    "03_Context/context_budget.json",
    "07_Mechanics/mechanics.json",
    "12_Tests/test_manifest.json",
]
DOMAIN_REQUIRED = {
    "domain_id",
    "domain_version",
    "allowed_vocabulary",
    "forbidden_vocabulary",
    "actor_types",
    "organization_types",
    "mechanic_families",
    "time_model",
    "core_loops",
    "crossover_policy",
}
MECHANIC_REQUIRED = {
    "stable_id",
    "version",
    "domain_id",
    "state_schema",
    "initial_state",
    "participants",
    "phases",
    "actions",
    "invariants",
    "terminal_conditions",
    "visibility",
    "tests",
}
PRIVATE_KEYS = {
    "secret",
    "secrets",
    "gm_truth",
    "world_truth_private",
    "private_agenda",
    "hidden_goal",
    "hidden_risk",
    "internal_reasoning",
}
TEXT_SUFFIXES = {".json", ".md", ".txt", ".yaml", ".yml"}


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def walk(value: Any) -> Iterable[Any]:
    yield value
    if isinstance(value, dict):
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def collect_ids(parsed_files: dict[Path, Any]) -> tuple[Counter[str], list[tuple[str, str]]]:
    ids: Counter[str] = Counter()
    refs: list[tuple[str, str]] = []
    for payload in parsed_files.values():
        for node in walk(payload):
            if not isinstance(node, dict):
                continue
            stable_id = node.get("stable_id")
            if isinstance(stable_id, str) and stable_id:
                ids[stable_id] += 1
            source = stable_id if isinstance(stable_id, str) else "<unknown>"
            for key in ("refs", "reference_ids"):
                values = node.get(key, [])
                if isinstance(values, list):
                    refs.extend((source, target) for target in values if isinstance(target, str))
    return ids, refs


def contains_private_key(value: Any) -> str | None:
    if isinstance(value, dict):
        for key, child in value.items():
            if key.lower() in PRIVATE_KEYS:
                return key
            found = contains_private_key(child)
            if found:
                return found
    elif isinstance(value, list):
        for child in value:
            found = contains_private_key(child)
            if found:
                return found
    return None


def estimate_tokens(text: str) -> int:
    cjk = len(re.findall(r"[\u3400-\u9fff\uf900-\ufaff]", text))
    other = max(0, len(text) - cjk)
    return math.ceil(cjk / 1.5 + other / 4)


def mechanic_rows(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, dict) and isinstance(payload.get("mechanics"), list):
        return [row for row in payload["mechanics"] if isinstance(row, dict)]
    if isinstance(payload, dict) and "stable_id" in payload:
        return [payload]
    if isinstance(payload, list):
        return [row for row in payload if isinstance(row, dict)]
    return []


def validate(package: Path) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    incomplete: list[str] = []
    parsed_files: dict[Path, Any] = {}

    for relative in REQUIRED_PATHS:
        if not (package / relative).exists():
            errors.append(f"required file missing: {relative}")

    for path in package.rglob("*.json"):
        try:
            parsed_files[path] = read_json(path)
        except Exception as error:
            errors.append(f"invalid JSON {path.relative_to(package)}: {error}")

    manifest = parsed_files.get(package / "manifest.json", {})
    profile = parsed_files.get(package / "01_Domain" / "domain_profile.json", {})
    if isinstance(profile, dict):
        missing = sorted(DOMAIN_REQUIRED - set(profile))
        if missing:
            errors.append(f"domain profile missing fields: {missing}")
        if profile.get("crossover_policy") not in {"forbidden", "explicit_only", "enabled"}:
            errors.append("invalid crossover_policy")
        if profile.get("crossover_policy") == "forbidden" and profile.get("secondary_domains"):
            errors.append("secondary domains declared while crossover is forbidden")
    else:
        errors.append("domain profile must be an object")

    ids, refs = collect_ids(parsed_files)
    duplicates = sorted(stable_id for stable_id, count in ids.items() if count > 1)
    if duplicates:
        errors.append(f"duplicate stable IDs: {duplicates[:20]}")

    registry = parsed_files.get(package / "00_Core" / "registry_index.json", {})
    if isinstance(registry, dict):
        for row in registry.get("references", []):
            if isinstance(row, dict) and isinstance(row.get("target_id"), str):
                refs.append((str(row.get("source_id", "<index>")), row["target_id"]))
    broken_refs = sorted({f"{source}->{target}" for source, target in refs if target not in ids})
    if broken_refs:
        errors.append(f"broken explicit references: {broken_refs[:20]}")

    domain_id = profile.get("domain_id") if isinstance(profile, dict) else None
    mechanic_count = 0
    for path, payload in parsed_files.items():
        try:
            relative = path.relative_to(package).as_posix()
        except ValueError:
            continue
        if not relative.startswith("07_Mechanics/") or path.name.endswith("schema.json"):
            continue
        for row in mechanic_rows(payload):
            mechanic_count += 1
            missing = sorted(MECHANIC_REQUIRED - set(row))
            if missing:
                errors.append(f"mechanic {row.get('stable_id', path.name)} missing fields: {missing}")
            if domain_id and row.get("domain_id") != domain_id:
                errors.append(f"mechanic {row.get('stable_id', path.name)} domain mismatch")
            for field in ("participants", "phases", "actions", "invariants", "terminal_conditions", "tests"):
                if field in row and not isinstance(row[field], list):
                    errors.append(f"mechanic {row.get('stable_id', path.name)} field {field} must be a list")
                elif field in row and not row[field]:
                    errors.append(f"mechanic {row.get('stable_id', path.name)} field {field} is empty")

    forbidden = profile.get("forbidden_vocabulary", []) if isinstance(profile, dict) else []
    content_roots = [package / name for name in ["02_Player", "03_Context", "04_Actors", "05_Organizations", "06_Locations", "07_Mechanics", "08_State", "09_Knowledge", "10_History", "11_Runtime"]]
    for root in content_roots:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES or path.name.endswith("schema.json"):
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            for term in forbidden:
                if isinstance(term, str) and term and term.casefold() in text.casefold():
                    errors.append(f"forbidden domain vocabulary {term!r} in {path.relative_to(package)}")
                    break

    public_root = package / "03_Context" / "public_packets"
    if public_root.exists():
        for path in public_root.rglob("*.json"):
            payload = parsed_files.get(path)
            if payload is not None:
                leaked = contains_private_key(payload)
                if leaked:
                    errors.append(f"private key {leaked!r} in public packet {path.relative_to(package)}")

    budget = parsed_files.get(package / "03_Context" / "context_budget.json", {})
    max_packet = budget.get("max_packet_tokens", 8000) if isinstance(budget, dict) else 8000
    if public_root.exists() and isinstance(max_packet, int):
        for path in public_root.rglob("*"):
            if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
                tokens = estimate_tokens(path.read_text(encoding="utf-8", errors="replace"))
                if tokens > max_packet:
                    errors.append(f"context packet exceeds budget: {path.relative_to(package)} estimated={tokens} limit={max_packet}")

    test_manifest = parsed_files.get(package / "12_Tests" / "test_manifest.json", {})
    required_gates = test_manifest.get("required_gates", []) if isinstance(test_manifest, dict) else []
    test_results = parsed_files.get(package / "12_Tests" / "test_results.json")
    passed_gates: set[str] = set()
    if isinstance(test_results, dict):
        results = test_results.get("gates", {})
        if isinstance(results, dict):
            passed_gates = {key for key, value in results.items() if value in {True, "pass", "passed"}}
    missing_gates = sorted(set(required_gates) - passed_gates)
    if missing_gates:
        incomplete.append(f"required test gates not passed: {missing_gates}")

    if not mechanic_count:
        incomplete.append("no implemented mechanic contracts")

    validated = isinstance(manifest, dict) and manifest.get("validated_release") is True
    pending = manifest.get("pending_gates", []) if isinstance(manifest, dict) else []
    if validated and (pending or incomplete):
        errors.append("manifest claims validated release while gates remain pending")
    if not validated:
        incomplete.append("manifest does not claim a validated release")

    integrity_path = package / "package_integrity.json"
    if integrity_path.exists() and integrity_path in parsed_files:
        bad: list[str] = []
        integrity = parsed_files[integrity_path]
        if isinstance(integrity, dict):
            for relative, metadata in integrity.get("files", {}).items():
                path = package / relative
                expected = metadata.get("sha256") if isinstance(metadata, dict) else None
                if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
                    bad.append(relative)
        if bad:
            errors.append(f"integrity mismatch: {bad[:20]}")

    status = "fail" if errors else ("incomplete" if incomplete else "pass")
    return {
        "status": status,
        "package": str(package),
        "domain_id": domain_id,
        "json_files_parsed": len(parsed_files),
        "stable_id_count": len(ids),
        "mechanic_count": mechanic_count,
        "errors": errors,
        "warnings": warnings,
        "incomplete": sorted(set(incomplete)),
    }


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def make_self_test_fixture(root: Path) -> None:
    domain = {
        "domain_id": "neutral_test",
        "domain_version": "1",
        "allowed_vocabulary": ["unit"],
        "forbidden_vocabulary": ["forbidden_domain_word"],
        "actor_types": ["participant"],
        "organization_types": ["group"],
        "mechanic_families": ["selection"],
        "time_model": {"unit": "turn"},
        "core_loops": ["choose_resolve_record"],
        "secondary_domains": [],
        "crossover_policy": "forbidden",
    }
    mechanic = {
        "stable_id": "MEC_TEST_001",
        "version": "1",
        "domain_id": "neutral_test",
        "state_schema": {"phase": "string"},
        "initial_state": {"phase": "open"},
        "participants": ["side_a", "side_b"],
        "phases": ["open", "closed"],
        "actions": ["commit"],
        "invariants": ["one commit per side"],
        "terminal_conditions": ["both committed"],
        "visibility": {"public": ["phase"]},
        "tests": ["happy_path", "duplicate_commit_rejected"],
    }
    gates = ["schema", "references", "domain_isolation", "mechanic_legality", "public_private_firewall", "deterministic_replay", "save_reload_equivalence", "context_budget", "mutation_tests"]
    write_json(root / "manifest.json", {"validated_release": True, "pending_gates": []})
    write_json(root / "00_Core" / "registry_index.json", {"references": []})
    write_json(root / "01_Domain" / "domain_profile.json", domain)
    write_json(root / "03_Context" / "context_budget.json", {"max_packet_tokens": 100})
    write_json(root / "03_Context" / "public_packets" / "current.json", {"phase": "open"})
    write_json(root / "07_Mechanics" / "mechanics.json", {"mechanics": [mechanic]})
    write_json(root / "12_Tests" / "test_manifest.json", {"required_gates": gates})
    write_json(root / "12_Tests" / "test_results.json", {"gates": {gate: "pass" for gate in gates}})


def self_test() -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="persistent-sandbox-validator-") as temp:
        base = Path(temp) / "good"
        make_self_test_fixture(base)
        good = validate(base)
        mutation_results: dict[str, str] = {}

        duplicate = Path(temp) / "duplicate"
        shutil.copytree(base, duplicate)
        write_json(duplicate / "04_Actors" / "duplicate.json", [{"stable_id": "MEC_TEST_001"}])
        mutation_results["duplicate_id"] = validate(duplicate)["status"]

        leakage = Path(temp) / "leakage"
        shutil.copytree(base, leakage)
        write_json(leakage / "03_Context" / "public_packets" / "leak.json", {"secret": "hidden"})
        mutation_results["private_leak"] = validate(leakage)["status"]

        vocabulary = Path(temp) / "vocabulary"
        shutil.copytree(base, vocabulary)
        (vocabulary / "03_Context" / "public_packets" / "bad.txt").write_text("forbidden_domain_word", encoding="utf-8")
        mutation_results["domain_leak"] = validate(vocabulary)["status"]

        broken_ref = Path(temp) / "broken_ref"
        shutil.copytree(base, broken_ref)
        write_json(broken_ref / "04_Actors" / "actor.json", {"stable_id": "ACT_TEST_001", "refs": ["MISSING_001"]})
        mutation_results["broken_reference"] = validate(broken_ref)["status"]

        ok = good["status"] == "pass" and all(status == "fail" for status in mutation_results.values())
        return {"status": "pass" if ok else "fail", "good_fixture": good["status"], "mutations": mutation_results}


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a domain-isolated persistent sandbox package")
    parser.add_argument("--package", type=Path)
    parser.add_argument("--strict", action="store_true", help="Return failure for incomplete candidates")
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
