---
name: build-competitive-rules-sandbox
description: Build, expand, validate, and package a persistent competitive rules sandbox for esports, sports-like simulations, drafting games, roster strategy, pick-ban systems, lineup construction, patch or ruleset metagames, conditional counters, tournaments, seasons, and analyst or coach roleplay. Pair with build-persistent-sandbox for generic state, history, context, migration, and validation. Do not use for fantasy cultivation, sect, or xianxia worldbuilding unless the user explicitly requests a crossover.
---

# Build a Competitive Rules Sandbox

Apply competitive-domain rules to the domain-neutral persistent-sandbox core. Build legal, versioned competition rather than flavor text or a universal matchup chart.

## Select the route

- **From zero:** use `$build-persistent-sandbox`, set `domain_id` to `competitive_rules`, then apply `assets/competitive_domain_profile.json`.
- **Existing competition:** freeze competition, league, season, stage, ruleset, patch, roster, eligibility, historical results, and source timestamps before changing anything.
- **Draft or lineup module:** formalize phases, legal actions, locks, uniqueness, role constraints, and completion conditions before adding advice.
- **Simulation or analyst mode:** separate official rules, observed data, model estimates, participant beliefs, and recommendations.

Read these references as needed:

- `references/competitive-domain-contract.md` — domain boundary, participants, seasons, organizations, and player roles.
- `references/draft-and-lineup.md` — configurable pick-ban, lineup legality, phase graphs, and series rules.
- `references/matchups-and-metagame.md` — conditional counters, synergies, patches, confidence, and provenance.
- `references/competitive-evaluation.md` — legality, replay, leakage, balance, and context tests.
- `references/competitive-anti-patterns-and-donts.md` — hard domain-specific DON’Ts for rules, matchups, rosters, alias retrieval, hidden information, career simulation, and validation. **Read this whenever creating or changing competition rules, player/team aliases, roster context, matchup evidence, or public/private competitive views.**

Generic anti-patterns in `$build-persistent-sandbox/references/anti-patterns-and-donts.md` also apply.

## Lock the competitive domain

Use neutral competitive terms: competitor, player, coach, team, league, tournament, roster, role, map, side, ruleset, patch, draft, selection, ban, lineup, strategy, matchup, result, and season. Keep unrelated fantasy institutions, advancement systems, and resource metaphors out unless a crossover is explicitly declared.

Do not assume one title's rules. Record the competition ID, governing body, league or circuit, season, stage, match format, ruleset version, patch or balance version, roster eligibility, side-selection policy, series carry-over rules, and source provenance. Unknown rules remain unknown.

## Formalize draft and lineup rules

Represent drafting as a state machine:

`ruleset + eligible pool + participants + current phase → legal actions → committed choice → next phase`

Parameterize:

- phase sequence and acting side;
- action type and count;
- simultaneous or alternating actions;
- uniqueness and duplicate restrictions;
- hidden or revealed actions;
- role or position assignment;
- swaps and deadlines;
- series-wide restrictions;
- disconnect, remake, substitution, and administrative rulings;
- terminal legality and incomplete states.

Do not encode recommendation rules as legality. A weak choice may be legal; a strong choice may be illegal because of phase, pool, roster, or series state.

## Model matchup and metagame conditionally

Counter and synergy relations depend on ruleset version, role, lane or position, map, side, phase, allied composition, opposing composition, participant proficiency, strategy, sample quality, and information freshness. Store evidence, confidence, uncertainty, exceptions, and expiration.

Use pairwise edges only when sufficient. Composition effects often require hyperedges. Separate observed statistics, expert judgment, model estimates, participant beliefs, and narrative commentary.

## Simulate competition and history

Track teams, players, coaches, analysts, staff, contracts, eligibility, form, preparation, strategy libraries, scrim knowledge, public reputation, hidden preferences, schedule, standings, series, roster moves, rule changes, and institutional decisions as authorized by scope.

Offscreen teams continue to practice, adapt, scout, change lineups, and compete. Results must follow committed events and the selected simulation model. Do not force every season to revolve around the user-controlled participant.

## Project sparse context

During a draft, load the current ruleset, current phase, available pool, committed actions, relevant participants, role constraints, and a bounded set of matchup evidence. Do not load every historical patch, every competitor, or the full matchup graph.

Public commentary must not expose hidden preparation, private confidence, unrevealed selections, or GM-only simulation parameters. After a match or ruleset change, unload obsolete phase material and retain a compact event record.

Apply `references/competitive-anti-patterns-and-donts.md` to handles, team abbreviations, role labels, patch aliases, and roster retrieval. Generic role words or short aliases must not accidentally load unrelated actor/team dossiers, and historical mentions must not imply current roster membership or availability.

## Validate

Run the generic validator and:

```powershell
python -X utf8 scripts/validate_competitive.py --package <directory> --strict
python -X utf8 scripts/validate_competitive.py --self-test
```

Test every phase, illegal action class, duplicate restriction, role assignment, series carry-over rule, version mismatch, hidden-information view, deterministic replay, save/reload equivalence, context budget, stale evidence, and at least one deliberately corrupted ruleset.

Also run negative retrieval/alias fixtures from `references/competitive-anti-patterns-and-donts.md`.

Report the exact ruleset and evidence date. Never claim official or current correctness without authoritative sources for the named competition and version.

