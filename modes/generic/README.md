# build-persistent-sandbox

Domain-neutral Codex skill for building persistent worlds and stateful sandboxes. It provides domain isolation, source and conflict mapping, executable mechanic contracts, deterministic state transitions, actor and organization simulation, knowledge firewalls, sparse context projection, migrations, and adversarial validation.

Use this core alone for a generic world, or pair it with one explicit domain pack such as:

- [build-cultivation-sandbox](https://github.com/Irizatto/build-cultivation-sandbox)
- [build-competitive-rules-sandbox](https://github.com/Irizatto/build-competitive-rules-sandbox)

Do not load multiple domain packs merely to add content. A crossover requires an explicit secondary domain, mapping, conflict matrix, and leakage tests.

## Validate

```powershell
python -X utf8 scripts/validate_package.py --package <directory> --strict
python -X utf8 scripts/validate_package.py --self-test
```

## Layout

- `SKILL.md` — core workflow
- `agents/openai.yaml` — UI metadata
- `assets/` — neutral briefs and schemas
- `references/` — domain isolation, mechanics, simulation, runtime, and evaluation
- `scripts/` — scaffold and package validator

## License

MIT
