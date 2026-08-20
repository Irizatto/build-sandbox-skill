# build-competitive-rules-sandbox

Competitive-rules domain pack for persistent esports and sports-like sandboxes. It covers versioned rulesets, pick-ban and draft state machines, lineup legality, roles, series and season history, roster changes, conditional matchup and synergy relations, evidence provenance, and sparse current-phase context.

Use it together with the domain-neutral core: [build-persistent-sandbox](https://github.com/Irizatto/build-persistent-sandbox).

It is intentionally title-neutral. A named competition, league, season, stage, patch, and authoritative rules source must be supplied before claiming current legality.

## Use

Invoke `$build-persistent-sandbox` with `$build-competitive-rules-sandbox`, set `domain_id` to `competitive_rules`, and keep `secondary_domains` empty unless a crossover is explicit.

Validate a package:

```powershell
python -X utf8 scripts/validate_competitive.py --package <directory> --strict
python -X utf8 scripts/validate_competitive.py --self-test
```

The pack keeps competitive rules separate from fantasy cultivation institutions and progression systems.

## Layout

- `SKILL.md` — domain skill entry point
- `agents/openai.yaml` — UI metadata
- `assets/` — competitive profile and draft schema
- `references/` — domain, draft, matchup, and evaluation contracts
- `scripts/` — competitive validator

## License

MIT
