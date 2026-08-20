from __future__ import annotations

import argparse
import base64
import hashlib
import json
import struct
from collections import Counter
from pathlib import Path
from typing import Any


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def embedded_card(path: Path) -> dict[str, Any] | None:
    data = path.read_bytes()
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        return None
    offset = 8
    while offset < len(data):
        length = struct.unpack(">I", data[offset:offset + 4])[0]
        chunk_type = data[offset + 4:offset + 8]
        payload = data[offset + 8:offset + 8 + length]
        offset += 12 + length
        if chunk_type == b"tEXt" and payload.startswith(b"chara\x00"):
            return json.loads(base64.b64decode(payload.split(b"\x00", 1)[1]).decode("utf-8"))
        if chunk_type == b"IEND":
            break
    return None


def validate(package: Path) -> dict[str, Any]:
    errors, warnings = [], []
    parsed = 0
    for path in package.rglob("*.json"):
        try:
            read_json(path)
            parsed += 1
        except Exception as error:
            errors.append(f"invalid JSON {path.relative_to(package)}: {error}")
    manifest_path = package / "manifest.json"
    manifest = read_json(manifest_path) if manifest_path.exists() else {}
    if not manifest:
        errors.append("manifest.json missing")
    if manifest.get("validated_release") is True and manifest.get("pending_gates"):
        errors.append("manifest claims validated release while gates remain pending")
    actor_count = 0
    registries = sorted((package / "08_NPC_System").glob("npc_public_registry*.json"))
    if registries:
        payload = read_json(registries[-1])
        actors = payload.get("actors", payload)
        if isinstance(actors, dict):
            actor_count = len(actors)
            names = [row.get("name") for row in actors.values() if isinstance(row, dict)]
            duplicates = [name for name, count in Counter(names).items() if name and count > 1]
            if duplicates:
                errors.append(f"duplicate public actor names: {duplicates[:10]}")
    card_matches = 0
    for card_json in (package / "00_Core_GM_Character").glob("*_spec_v2.json"):
        card = read_json(card_json)
        if card.get("spec") != "chara_card_v2":
            continue
        budget = card.get("data", {}).get("character_book", {}).get("token_budget")
        if budget and budget > 8000:
            warnings.append(f"{card_json.name} lore budget exceeds 8K: {budget}")
        if any(embedded_card(png) == card for png in card_json.parent.glob("*.png")):
            card_matches += 1
    integrity_path = package / "package_integrity.json"
    if integrity_path.exists():
        integrity = read_json(integrity_path)
        bad = []
        for relative, metadata in integrity.get("files", {}).items():
            path = package / relative
            if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != metadata.get("sha256"):
                bad.append(relative)
        if bad:
            errors.append(f"integrity mismatch: {bad[:10]}")
    return {"status": "pass" if not errors else "fail", "package": str(package),
            "json_files_parsed": parsed, "public_actor_count": actor_count,
            "matching_embedded_cards": card_matches, "errors": errors, "warnings": warnings}


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a cultivation sandbox package")
    parser.add_argument("--package", required=True, type=Path)
    args = parser.parse_args()
    package = args.package.resolve()
    if not package.is_dir():
        raise SystemExit(f"Package directory not found: {package}")
    report = validate(package)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(0 if report["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
