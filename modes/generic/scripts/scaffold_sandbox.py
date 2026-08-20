from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


DIRECTORIES = [
    "00_Core",
    "01_Domain",
    "02_Player",
    "03_Context/public_packets",
    "04_Actors",
    "05_Organizations",
    "06_Locations",
    "07_Mechanics",
    "08_State",
    "09_Knowledge",
    "10_History",
    "11_Runtime",
    "12_Tests/fixtures",
]


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a domain-neutral persistent sandbox scaffold")
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--name", required=True)
    parser.add_argument("--domain", required=True, help="Stable primary domain identifier")
    parser.add_argument("--force-empty", action="store_true")
    args = parser.parse_args()

    output = args.output.resolve()
    if output.exists() and (not args.force_empty or any(output.iterdir())):
        raise SystemExit(f"Refusing to overwrite non-empty or unapproved target: {output}")
    output.mkdir(parents=True, exist_ok=True)
    for relative in DIRECTORIES:
        (output / relative).mkdir(parents=True, exist_ok=True)

    skill_root = Path(__file__).resolve().parents[1]
    brief = json.loads((skill_root / "assets" / "default_design_brief.json").read_text(encoding="utf-8"))
    brief["primary_domain"] = args.domain
    write_json(output / "00_Core" / "design_brief.json", brief)
    shutil.copy2(skill_root / "assets" / "domain_profile.schema.json", output / "01_Domain")
    shutil.copy2(skill_root / "assets" / "mechanic_contract.schema.json", output / "07_Mechanics")

    write_json(
        output / "01_Domain" / "domain_profile.json",
        {
            "domain_id": args.domain,
            "domain_version": "0.1.0",
            "allowed_vocabulary": [],
            "forbidden_vocabulary": [],
            "actor_types": ["UNSET"],
            "organization_types": [],
            "mechanic_families": ["UNSET"],
            "time_model": {"unit": "UNSET", "cadences": []},
            "core_loops": ["UNSET"],
            "secondary_domains": [],
            "crossover_policy": "forbidden",
        },
    )
    write_json(output / "07_Mechanics" / "mechanics.json", {"mechanics": []})
    write_json(output / "00_Core" / "registry_index.json", {"entities": [], "references": []})
    write_json(
        output / "03_Context" / "context_budget.json",
        {"max_packet_tokens": 8000, "total_active_budget_tokens": 12000, "measurement": "estimate"},
    )
    required_gates = [
        "schema",
        "references",
        "domain_isolation",
        "mechanic_legality",
        "public_private_firewall",
        "deterministic_replay",
        "save_reload_equivalence",
        "context_budget",
        "mutation_tests",
    ]
    write_json(output / "12_Tests" / "test_manifest.json", {"required_gates": required_gates})
    write_json(
        output / "manifest.json",
        {
            "package": args.name,
            "package_schema_version": "1.0.0",
            "version": "0.1.0-alpha1",
            "domain_id": args.domain,
            "release_status": "Scaffold-Unvalidated",
            "validated_release": False,
            "pending_gates": required_gates + ["implementation", "human_long_session_playtest"],
            "declared_counts": {},
            "forbidden_claim": "A scaffold is not a playable or validated world.",
        },
    )
    print(json.dumps({"status": "created", "output": str(output), "domain": args.domain}, ensure_ascii=False))


if __name__ == "__main__":
    main()

