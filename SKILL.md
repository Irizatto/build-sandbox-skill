---
name: build-sandbox
description: Build, expand, migrate, validate, and package persistent sandboxes in generic, competitive, or cultivation form. Use for executable world/state systems, living-world expansion, deterministic materialization, organization ecology, persistent character life, relationship/narrative runtime, token-safe lived-world experience, long-session gameplay review, and SillyTavern/world-simulation packaging. Use one primary mode per build unless the user explicitly requests a crossover.
---

# Build Sandbox

Use this as the single entry point for three forms of the same persistent-sandbox architecture:

- `generic` — domain-neutral persistent worlds, executable mechanics, state, history, retrieval, migration, world growth, organizations, actors, and validation.
- `competitive` — versioned competitions, drafts, lineups, rosters, seasons, careers, teams, staff, conditional matchup logic, and optional living-world/social simulation.
- `cultivation` — long-running xianxia worlds, sect/faction ecosystems, actor ecology, generational change, world expansion, SillyTavern packaging, and knowledge firewalls.

## Select exactly one primary mode

Start by selecting `generic`, `competitive`, or `cultivation`, and declare it in the package domain profile. Do not combine modes merely to add flavor. A real crossover requires explicit secondary domains, mapping, a conflict matrix, authority decisions, and leakage tests.

All modes share these invariants:
- freeze authority and provenance before generation;
- use stable IDs and explicit versioning;
- formalize consequential transitions rather than trusting prose;
- separate world truth, actor belief, player knowledge, rumor, commentary and projections;
- preserve history and offscreen agency;
- project sparse context rather than raw databases;
- validate adversarially and report release status honestly.

## Mandatory: load the preserved mode contract

The three original skills are vendored intact under `modes/`. Their presence alone is not enough: after selecting a primary mode, **read and apply its preserved `SKILL.md` before reading mode references or implementing changes**:

- `generic` → `modes/generic/SKILL.md`
- `competitive` → `modes/competitive/SKILL.md`
- `cultivation` → `modes/cultivation/SKILL.md`

Resolve relative `assets/`, `references/`, `scripts/`, and `agents/` paths inside a vendored mode contract relative to that `modes/<mode>/` directory.

Competitive and cultivation mode contracts may still mention their historical standalone dependency `$build-persistent-sandbox`. Inside this unified skill, resolve that dependency to `modes/generic/SKILL.md` and `modes/generic/references/...`; do not require a separately installed external generic skill when the vendored core is already present.

Read `references/mode-routing-and-compatibility.md` whenever selecting a mode, auditing the unified skill, or updating vendored sources. Run `python -X utf8 scripts/audit_vendor_parity.py` before claiming the three source modes remain intact after a merge/update.

The root shared layer supplements the selected mode contract. It does not silently replace or weaken mode-specific rules.

## Determine task shape

Classify the request before building:

### Narrow subsystem
Examples: one draft state machine, one rules migration, one retrieval repair, one package validator. Read the selected mode contract, then only the relevant mode/shared references. Do not force a six-phase living-world program onto a narrow task.

### Living / long-running sandbox
Use the shared lifecycle when the product is expected to support open-ended travel/topology, persistent actors, offscreen organizations, relationships, emergent stories, large time skips, or hundreds of sessions.

Read:
- `references/living-sandbox-lifecycle.md` — six gated phases from horizon/topology through long-session hardening.
- `references/world-growth-and-materialization.md` — macro skeletons, latent seeds, deterministic materialization, organization seeds, actor promotion, Canon persistence.
- `references/character-life-relationship-narrative.md` — private/everyday life, actor promotion, multidimensional relationships, Character Anchors, NPC initiative, causal Story Beat runtime, reusable roleplay-card design patterns.
- `references/lived-world-token-safe-experience.md` — ordinary life, embodiment, material culture, social grammar, information ecology, player-created legacy, discovery, social friction, world scars and belonging without prompt growth scaling with world size.
- `references/gameplay-review-and-validation.md` — periodic gameplay review, 3h/20h/100h thinking, long-session scenario suite, anti-pattern and release gates.
- `references/orchestration-and-handoffs.md` — multi-agent execution, Orca/Muse Spark Contributor/Codex role split, workspace policy, no-human-router handoffs.

Then read only the selected/generic mode references required by the task under `modes/<mode>/references/`.

## Shared living-world lifecycle

For a mature open-ended sandbox, assess these six phases even when some are already implemented:

1. **Horizon / Topology Foundation** — the world/ecosystem continues beyond the starting slice through a stable macro skeleton, aggregate offscreen state, latent seeds, deterministic materialization and sparse context.
2. **Organization / Institution Ecology** — organizations can form, persist, split, merge, decline, dissolve and leave legacies through resources, governance, membership and succession.
3. **Actor Promotion / Character Life** — ordinary actors can become persistent through history/bookmark without gaining destiny privileges; important actors have voice, routine, social and private lives.
4. **Relationship / Narrative Runtime** — relationships are multidimensional history; Character Anchors, NPC initiative and causal beat proposals keep scenes alive without forced drama.
5. **Domain Depth / Wonder / Affordance Ecology** — the selected domain creates genuinely different gameplay rather than more names.
6. **Long-Session Gameplay Hardening** — mundane life, recurring actors, absence, long skips, anti-protagonist play, weird actions, retrieval/persistence and human-playtest gates.

Do not pre-author the whole world merely to make it feel large. Make the world structurally possible, materialize relevant detail, and persist what becomes real.

## Token-safe lived-world experience layer

The six-phase lifecycle establishes a functioning living-world substrate. When the user wants the stronger feeling of *living inside* that world — ordinary routines, bodies, local objects, social customs, incomplete information, player-created history, exploration uncertainty, social barriers, historical scars, or personal belonging — read `references/lived-world-token-safe-experience.md`.

Treat this as an experience layer over existing authorities, **not automatically as a seventh lifecycle phase**. A mature implementation may add all ten capabilities while preserving bounded context:

- Everyday World;
- Embodiment;
- Material Culture;
- Culture/Ritual as social grammar;
- Information Ecology;
- Player-created History / creation lineage;
- Discovery / Unknown Preservation;
- Social Friction / access and obligation;
- World Memory / scars and legacy;
- Belonging / personal anchors.

These capabilities must reuse existing State, Event/Causal, Epistemic, Social, World/Regional, Projection and Validation layers rather than spawning one LLM agent or one mutable subsystem per feature.

A key acceptance property is **context invariance**: enlarging offscreen world population, object catalogs, historical depth or cultural records must not cause the same current scene to grow linearly in prompt size. Prefer deterministic authority/knowledge/location/action filtering before semantic ranking. Do not raise the global token budget as the primary implementation strategy.

## World growth contract

When the sandbox may expand beyond an initial slice, prefer:

`stable macro skeleton → latent seeds → relevance/history trigger → deterministic materialization → stable ID → Canon → runtime evolution`

Latent areas/organizations may accumulate coarse history before detailed materialization. Once an identity is committed, generator/model/schema upgrades must not reroll it. Unknowns may remain unknown.

World size must not equal prompt size. Use hierarchical/facet retrieval and measure the assembled context.

## Actor and character-life contract

Separate:
- world importance;
- simulation importance/detail;
- current narrative relevance;
- player bookmark/favorite.

A bookmark may improve retention, memory and simulation detail. It must not automatically change power, fame, luck, affection, attraction, access, plot armor, availability or world importance.

For important actors, progressively support public/professional/private self, goals, contradictions, routine, hobbies, home/personal-space habits, social circles, state-dependent behavior, voice, meaningful memories and independent offscreen action.

Do not let all major actors converge on one rational/optimization personality template.

## Relationship and narrative contract

Do not reduce relationships to one affection number when the domain requires richer social simulation. Model relevant dimensions, potentially asymmetrically, with causal history and boundaries.

Narrative runtime should follow:

`actor anchors → scene state → progress/repetition signals → stagnation detector → beat candidates → causal eligibility → proposal → authoritative validation/commit → narrative projection`

Never force a plot beat every N turns or by a flat probability. `Nothing important happens` is valid gameplay.

## Roleplay-card pattern extraction

When studying third-party cards or lorebooks, extract transferable structure rather than copying plots or unsafe content. Useful patterns include:
- Character Anchors and dialogue exemplars;
- public/private self and boundaries;
- Entity Facet Retrieval and hierarchical retrieval;
- procedural generation axes;
- history/official record/faction interpretation/folklore/rumor layers;
- deferred open-world plot states;
- player-agency guards;
- state/UI/narrative projection separation;
- validated world-mutation transactions.

Adult/NSFW source material may contribute only compliant structural lessons such as boundaries, trust, private self and relationship stages. Do not reproduce explicit sexual content, coercive content, unsafe age framing, or source-specific scenes.

## Retrieval and context hard gates

Across all modes, reject or constrain:
- high-frequency generic keys;
- empty keys;
- single-character CJK keys without explicit justification and collision tests;
- generic titles/roles as entity-specific triggers;
- ambiguous short aliases;
- mega-entries;
- uncontrolled recursive retrieval;
- lore hits treated as proof of current presence/state/knowledge;
- static World Info owning mutable facts;
- raw full-database prompt injection;
- solving context pressure only by raising token budgets.

Read the applicable mode anti-pattern reference as mandatory build-time constraints.

## Shared core workflow

1. Resolve the real repo/package/workspace and freeze authoritative inputs, IDs, hashes/provenance, schema versions and user scope.
2. Select one primary mode and **load `modes/<mode>/SKILL.md`**. If that mode depends on the generic core, load `modes/generic/SKILL.md` as well using the compatibility mapping.
3. Classify narrow vs living-world task shape and load only the shared/mode references needed.
4. If living-world scope applies, assess the six-phase lifecycle and continue from the earliest materially incomplete phase instead of restarting mature work.
5. If lived-world experience depth is in scope, extend existing authorities using `references/lived-world-token-safe-experience.md` and add context-invariance tests rather than more permanent prompt content.
6. Write or update the domain contract before expanding content.
7. Keep one authority owner per mutable fact class; use explicit transitions, append-only events where appropriate, migrations and deterministic replay.
8. Separate facts, observations, estimates, beliefs and commentary.
9. Project sparse state/context by relevance and knowledge rights.
10. Validate schema, references, legality, privacy, retrieval, save/reload, deterministic replay, mutations and player-facing scenario behavior.
11. Run long-session gameplay review when the product claims persistent/living-world quality.
12. Report exact mode, versions, evidence, tests, limitations, human gates and release status.

## Mode-specific rules

### Generic
Load `modes/generic/SKILL.md` first. Keep vocabulary domain-neutral in the shared core. Put domain concepts in `01_Domain/domain_profile.json`. Use `modes/generic/references/anti-patterns-and-donts.md` as a hard gate for living worlds.

### Competitive
Load `modes/competitive/SKILL.md` **and** the generic core when state/history/context/persistence are involved, as the original competitive skill requires. Pin competition, league/circuit, season/stage, ruleset/patch, roster/eligibility and source date. Keep recommendation separate from legality. Matchups are conditional, not eternal scalar truth. If the product includes persistent careers, teams, staff or daily life, also apply the shared actor/relationship/gameplay lifecycle. Read `modes/competitive/references/competitive-anti-patterns-and-donts.md`.

For a new competitive package, the preserved source skill layers on the generic scaffold rather than owning a standalone scaffold: scaffold with the generic core using domain ID `competitive_rules`, then apply `modes/competitive/assets/competitive_domain_profile.json`; include `modes/competitive/assets/draft_contract.schema.json` when draft/lineup mechanics are in scope.

### Cultivation
Load `modes/cultivation/SKILL.md` plus the generic core where it is referenced. Build a society and simulation rather than a lore pile. Keep public registry, story truth, runtime state and context index separate. Use regional interpretation rather than a universal game level, sparse active casts, layered time ticks, permanent death with legacy, organization/sect ecology, deterministic world expansion and selective SillyTavern packaging. Read `modes/cultivation/references/cultivation-anti-patterns-and-donts.md`.

## Multi-agent orchestration

When Orca, Muse Spark Contributor and Codex are available for a large build, prefer:

`Orca orchestration/workspace → Muse Spark Contributor primary implementation → Codex independent audit/small fixes → acceptance handoff`

The user should not act as a copy/paste router between phases. Respect the user's workspace-root policy; for the Windows `D:\AI` policy, do not place project/worktree/agent/build/cache work on `C:\`. See `references/orchestration-and-handoffs.md`.

## Commands

From this skill directory:

```powershell
python -X utf8 scripts/audit_vendor_parity.py
python -X utf8 scripts/scaffold_sandbox.py --mode generic --output <directory> --name <name> --domain <domain_id>
python -X utf8 scripts/scaffold_sandbox.py --mode cultivation --output <directory> --name <name>
python -X utf8 scripts/validate_sandbox.py --mode generic --package <directory> --strict
python -X utf8 scripts/validate_sandbox.py --mode cultivation --package <directory>
python -X utf8 scripts/validate_sandbox.py --mode competitive --package <directory> --strict
```

For competitive from zero, use the generic scaffold route described above; the original competitive skill did not contain its own scaffold script.

The mode-specific scripts under `modes/` remain available for compatibility and direct debugging.

## Release honesty

Do not call a build Final because JSON parses, simulations run, or agent scenario tests pass. Distinguish automated validation, deterministic long-run simulation, agent-driven gameplay scenarios and actual human long-session playtesting. Use Alpha or Release Candidate until the relevant experiential gates are honestly satisfied.