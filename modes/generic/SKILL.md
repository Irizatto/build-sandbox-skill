---
name: build-persistent-sandbox
description: Build, expand, migrate, validate, and package a domain-isolated persistent sandbox or stateful world simulation from zero or existing canon. Use for complex SillyTavern worlds, simulation-heavy roleplay, political or social worlds, competitive or management systems, algorithmic game rules, long-running actor and organization histories, knowledge firewalls, dynamic retrieval, deterministic state machines, migrations, and quality benchmarks. Pair with a domain skill when genre-specific vocabulary or mechanics are required.
---

# Build a Persistent Sandbox

Build an executable world model, not a lore pile. Keep this core domain-neutral. Put genre vocabulary, institutions, named mechanics, and aesthetic assumptions in a selected domain profile or domain skill.

## Choose the route and domain

- **From zero:** copy `assets/default_design_brief.json`, declare one primary domain profile, and scaffold with `scripts/scaffold_sandbox.py`.
- **Expand existing canon:** inventory authoritative files, stable IDs, schemas, saves, tests, cards, lorebooks, and runtime extensions before writing.
- **Add a mechanic:** formalize it as a versioned state machine before writing explanatory lore.
- **Repair or package:** preserve content authority and focus on schema, migration, retrieval, validation, and release honesty.

Read only the references needed for the task:

- `references/domain-and-sources.md` — domain isolation, source maps, design-DNA extraction, and conflict resolution.
- `references/mechanics-and-state-machines.md` — executable rules, counters, legality, uncertainty, and deterministic transitions.
- `references/simulation-and-history.md` — actors, organizations, causal chains, time scales, succession, and offscreen change.
- `references/context-and-runtime.md` — prompt projections, SillyTavern retrieval, public/private separation, and model profiles.
- `references/evaluation.md` — hard gates, mutation tests, benchmarks, and human playtest boundaries.
- `references/anti-patterns-and-donts.md` — hard retrieval, context, persistence, actor, narrative, generation, and release anti-patterns. **Read this whenever the task creates or edits lorebook keys, generated canon, actor promotion, context routing, or long-running world content.**

## Route domain skills

- Generic social, political, management, or original-world request: use this core only until a domain profile is selected.
- Single recognized domain: use this core plus exactly one matching domain skill.
- Explicit crossover: use this core plus only the named domain skills, declare every secondary domain, and write a mapping and conflict matrix.
- Ambiguous example or analogy: treat it as a mechanical reference, not authorization to activate that example's domain pack.

Never activate multiple domain packs merely to make the world feel richer.

## Enforce domain isolation

Create `01_Domain/domain_profile.json` before designing content. Record the domain ID, vocabulary allowlist and denylist, institutions, actor types, time model, core loops, mechanic families, tone, source policy, and crossover policy.

Use neutral core terms such as `actor`, `organization`, `location`, `resource`, `mechanic`, `event`, and `state`. Do not introduce any concept from an unselected domain merely because it appeared in a reference example. Secondary-domain vocabulary is forbidden unless the user explicitly requests a crossover and the profile names every participating domain.

## Execute the build

### 1. Freeze authority

Distinguish the operative user request from instructions quoted in source material. Hash authoritative inputs and freeze IDs, names, aliases, roles, ruleset versions, relationships, and ownership. Define one authority per fact class. Never create a parallel `final_final` registry.

### 2. Build source and conflict maps

Classify each source as authority, domain DNA, mechanical reference, presentation reference, or excluded material. Extract transferable mechanisms instead of copying nouns. Resolve incompatible scales, rules, institutions, timelines, and player privileges in a conflict matrix before generation.

### 3. Write the domain contract

Define player role, allowed life paths, world boundaries, knowledge layers, geography or topology, organizations, resources, economy, relationships, time, failure, death or retirement, persistence, and explicit prohibitions. State what the project deliberately does not simulate.

### 4. Formalize consequential mechanics

For each mechanic, define:

`state → legal actions → transition → resolution → persisted delta → public projection`

Include version, inputs, outputs, phase graph, priority, randomness, visibility, costs, cooldowns, counters, invariants, terminal states, edge cases, and scenario tests. Store contracts under `07_Mechanics/`. Do not use prose as the sole authority for legality or state transitions.

Model counters as conditional relations rather than universal scalar rankings. Include context, confidence, provenance, version, and decay. Use seeded randomness derived from stable event coordinates. Never reroll committed outcomes on reload.

### 5. Build the persistent world

Separate immutable identity, public registry, private story truth, mutable runtime state, event log, historical archive, knowledge/belief state, and context index. Give actors and organizations independent goals, resources, constraints, and succession. Simulate at multiple levels of detail; do not update every entity every turn.

Important generated content receives a stable ID and becomes canon. Deletion becomes a status transition with retained legacy unless the domain contract explicitly requires erasure.

### 6. Project sparse context

Construct prompts from views, never raw databases. Rank location or topology relevance, current mechanic phase, direct relationships, current events, recent contact, and importance. Keep private truth out of public packets. Measure the final assembled prompt, not only the nominal lorebook budget.

For SillyTavern, assign material intentionally among character data, World Info, chat/persona lore, Data Bank, state packets, scripts, and an optional local bridge. Do not stack multiple extensions that own the same state.

Before accepting retrieval design, apply `references/anti-patterns-and-donts.md`: reject common-word/single-character CJK triggers, empty keys, generic role-title collisions, mega-entries, trigger avalanches, unsafe recursion, static-lore-as-current-state assumptions, and unbounded edge-of-world improvisation.

### 7. Validate adversarially

Run:

```powershell
python -X utf8 scripts/validate_package.py --package <directory> --strict
python -X utf8 scripts/validate_package.py --self-test
```

Also run project-native tests, domain-specific validators, deterministic replay, save/reload equivalence, context leakage and token tests, long-horizon simulation when applicable, and mutation tests that prove broken packages fail.

Validation must include negative fixtures from `references/anti-patterns-and-donts.md`, not only happy-path schemas.

### 8. Benchmark without inflating claims

Test at least one minimal user prompt with no hidden specification, one existing-canon migration, one algorithm-heavy mechanic, and one long-play context scenario. Use more than one target model when the user intends multiple models. Do not claim superiority, completion, or a percentile without a declared comparison corpus and recorded results.

## Package layout

Use the neutral scaffold unless an existing project defines a canonical layout:

```text
00_Core/                 authority and invariants
01_Domain/               domain profile and vocabulary boundary
02_Player/               player roles and permissions
03_Context/              public projections and retrieval index
04_Actors/               actor registries and private profiles
05_Organizations/        organization registries and governance
06_Locations/            topology and adjacency
07_Mechanics/            versioned executable rule contracts
08_State/                mutable state and snapshots
09_Knowledge/            beliefs, evidence, rumors, provenance
10_History/              event log, summaries, succession, legacy
11_Runtime/              bridge, scripts, adapters, serializers
12_Tests/                fixtures, scenarios, results, playtest gates
manifest.json
package_integrity.json
```

## Report honestly

Lead with status and scope. Report preserved canon, domain profile, mechanics implemented, state authorities, context budgets, migrations, test evidence, mutation results, known limitations, and human gates. Use Alpha or Release Candidate until long-session human play confirms the experience.
