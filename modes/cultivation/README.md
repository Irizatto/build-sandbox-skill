# build-cultivation-sandbox

A Codex skill for building, expanding, migrating, testing, and packaging a long-running cultivation or xianxia open-world sandbox for SillyTavern — from zero or from existing canon.

The skill produces a dense-world, sparse-context sandbox: a playable society and simulation, not a pile of lore.

## Features

- Design contract from `assets/default_design_brief.json` (World Alpha scale: 8 macroregions, 120 formal NPCs)
- Dense world, sparse context: public registries, story registries, runtime state, and a context index
- Layered world simulation (annual / five-year / ten-year ticks) with permanent death and legacy persistence
- Character ecology with A/B/C detail tiers and required variety
- SillyTavern packaging: one canonical `chara_card_v2` JSON + PNG, selective 8K lorebook, safe migration path

## Usage

Reference the skill as `$build-cultivation-sandbox`, then choose a route: from zero, expand existing canon, or repair/package only.

Bootstrap a clean package skeleton:

```powershell
python scripts/scaffold_sandbox.py --output <directory> --name <world-name>
```

Validate a package:

```powershell
python scripts/validate_package.py --package <directory>
```

## Layout

- `SKILL.md` — skill entry point
- `agents/openai.yaml` — OpenAI agent interface metadata
- `assets/default_design_brief.json` — default design contract
- `references/` — architecture, character ecology, context engineering, acceptance tests
- `scripts/` — scaffold and validation tooling

## License

MIT
