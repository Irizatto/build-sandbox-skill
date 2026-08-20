---
name: build-sandbox
description: Build, expand, migrate, validate, and package one persistent sandbox skill in generic, competitive, or cultivation form. Use one mode per build unless the user explicitly requests a crossover.
---

# Build Sandbox

Use this single skill as the entry point for three forms of the same system:

- `generic` — domain-neutral persistent worlds, executable mechanics, state, history, retrieval, migration, and validation.
- `competitive` — versioned leagues, tournaments, drafts, lineups, rosters, seasons, and conditional matchup logic.
- `cultivation` — long-running xianxia worlds, sects, NPC ecology, generational change, SillyTavern packaging, and knowledge firewalls.

## Select exactly one form

Start every task by selecting `--mode generic`, `--mode competitive`, or `--mode cultivation` in the command examples, and declare that mode in the package's domain profile. Do not combine forms merely to add content. A crossover requires an explicit secondary domain, mapping, conflict matrix, and leakage tests.

All forms share the same principles: freeze authority, use stable IDs, formalize consequential mechanics as state machines, separate public/private knowledge, project sparse context, preserve history, validate adversarially, and report release status honestly.

## Shared core workflow

1. Freeze authoritative inputs, IDs, source provenance, and user scope.
2. Select one form and read only its references under `modes/<form>/references/`.
3. Write the domain contract before adding lore or recommendations.
4. Keep state ownership singular; use append-only events and deterministic replay.
5. Separate official facts, observed data, estimates, beliefs, and commentary.
6. Validate schema, references, legality, privacy boundaries, retrieval, replay, save/reload, and mutations.
7. Report exact mode, versions, evidence dates, tests, limitations, and human gates.

## Mode-specific rules

### Generic

Keep vocabulary domain-neutral and use the persistent package layout. Use the generic scaffold and validator. Domain terms belong in `01_Domain/domain_profile.json`, never in the core.

### Competitive

Use title-neutral competitive terms. Model drafts and lineups as legal state machines. Keep recommendation separate from legality. Matchups are conditional on patch, role, map, side, composition, proficiency, evidence, confidence, and freshness.

### Cultivation

Build a society and simulation rather than a lore pile. Keep public registry, story truth, runtime state, and context index separate. Use sparse active casts, layered time ticks, permanent death with legacy persistence, and selective SillyTavern packaging.

## Commands

From this skill directory:

```powershell
python -X utf8 scripts/scaffold_sandbox.py --mode generic --output <directory> --name <name> --domain <domain_id>
python -X utf8 scripts/scaffold_sandbox.py --mode cultivation --output <directory> --name <name>
python -X utf8 scripts/validate_sandbox.py --mode generic --package <directory> --strict
python -X utf8 scripts/validate_sandbox.py --mode cultivation --package <directory>
python -X utf8 scripts/validate_sandbox.py --mode competitive --package <directory> --strict
```

The original mode-specific scripts remain under `modes/` for compatibility and direct debugging. The root scripts are the recommended single-skill interface.
