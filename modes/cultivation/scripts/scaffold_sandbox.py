from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


DIRECTORIES = [
    "00_Core_GM_Character", "01_Core_Rules", "02_Player_Persona", "03_World_Lorebook",
    "04_Geography", "05_Cultivation_System", "06_Technique_Lorebook", "07_Factions",
    "08_NPC_System", "09_Economy", "10_Encounter_Engine", "11_World_State",
    "12_Memory_System", "13_Rumor_Knowledge_System", "14_Sect_Governance",
    "15_Generational_System", "16_System_Module", "17_Openings", "18_Test_Scenarios/tests",
]


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a canonical cultivation sandbox package skeleton")
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--name", required=True)
    parser.add_argument("--force-empty", action="store_true")
    args = parser.parse_args()
    output = args.output.resolve()
    if output.exists() and (not args.force_empty or any(output.iterdir())):
        raise SystemExit(f"Refusing to overwrite non-empty or unapproved target: {output}")
    output.mkdir(parents=True, exist_ok=True)
    for relative in DIRECTORIES:
        (output / relative).mkdir(parents=True, exist_ok=True)
    skill_root = Path(__file__).resolve().parents[1]
    shutil.copy2(skill_root / "assets" / "default_design_brief.json", output / "01_Core_Rules" / "design_brief.json")
    manifest = {
        "package": args.name, "version": "0.1.0-alpha1",
        "release_status": "World-Alpha-Scaffold-Unvalidated", "validated_release": False,
        "authority": {}, "pending_gates": ["implementation", "automated_tests", "human_long_session_playtest"],
        "forbidden_claim": "A scaffold is not a playable or validated world."
    }
    (output / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "created", "output": str(output), "directories": len(DIRECTORIES)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
