---
name: build-sandbox
description: Build, expand, migrate, validate, and package persistent sandboxes in generic, competitive, or cultivation form. Use for executable world/state systems, living-world expansion, deterministic materialization, organization ecology, persistent character life, relationship/narrative runtime, token-safe lived-world experience, experience-surface upgrades, cross-linked content density, controlled scale-up, long-session gameplay review, and SillyTavern/world-simulation packaging. Use one primary mode per build unless the user explicitly requests a crossover.
---

# Build Sandbox

Use this as the single entry point for three forms of the same persistent-sandbox architecture:

- `generic` — domain-neutral persistent worlds, executable mechanics, state, history, retrieval, migration, world growth, organizations, actors, and validation.
- `competitive` — versioned competitions, drafts, lineups, rosters, seasons, careers, teams, staff, conditional matchup logic, and optional living-world/social simulation.
- `cultivation` — long-running xianxia worlds, sect/faction ecosystems, actor ecology, generational change, world expansion, SillyTavern packaging, experience-surface design, content renaissance, and cultivation-specific affordances.

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

The three source skills are vendored under `modes/`. After selecting a primary mode, **read and apply its `SKILL.md` before reading mode references or implementing changes**:

- `generic` → `modes/generic/SKILL.md`
- `competitive` → `modes/competitive/SKILL.md`
- `cultivation` → `modes/cultivation/SKILL.md`

Resolve relative `assets/`, `references/`, `scripts/`, and `agents/` paths inside a mode contract relative to that `modes/<mode>/` directory.

Competitive and cultivation mode contracts may mention their historical standalone dependency `$build-persistent-sandbox`. Inside this unified skill, resolve that dependency to `modes/generic/SKILL.md` and `modes/generic/references/...`; do not require a separately installed generic skill when the vendored core is already present.

Read `references/mode-routing-and-compatibility.md` whenever selecting a mode, auditing the unified skill, or updating vendored sources. Run `python -X utf8 scripts/audit_vendor_parity.py` before claiming source-mode parity after an update.

The root shared layer supplements the selected mode contract. It does not silently replace or weaken mode-specific rules.

## Determine task shape

Classify the request before building.

### Narrow subsystem

Examples: one draft state machine, one rules migration, one retrieval repair, one package validator. Read the selected mode contract, then only the relevant mode/shared references. Do not force a living-world program onto a narrow task.

### Living / long-running sandbox

Use the shared lifecycle when the product is expected to support open-ended travel/topology, persistent actors, offscreen organizations, relationships, emergent stories, large time skips, or hundreds of sessions.

Read:
- `references/living-sandbox-lifecycle.md` — six gated phases from horizon/topology through long-session hardening.
- `references/world-growth-and-materialization.md` — macro skeletons, latent seeds, deterministic materialization, organization seeds, actor promotion, Canon persistence.
- `references/character-life-relationship-narrative.md` — private/everyday life, actor promotion, multidimensional relationships, Character Anchors, NPC initiative, causal Story Beat runtime, reusable roleplay-card design patterns.
- `references/lived-world-token-safe-experience.md` — ordinary life, embodiment, material culture, social grammar, information ecology, player-created legacy, discovery, social friction, world scars and belonging without prompt growth scaling with world size.
- `references/content-density-and-controlled-scale.md` — broad-reference/narrow-implementation research, cross-linked content density, Pilot-first authoring, functional affordances, history-in-present, two-wave scale-up, content compression, blind/mutation tests, and 5x/10x inactive-context stress.
- `references/gameplay-review-and-validation.md` — periodic gameplay review, 3h/20h/100h thinking, long-session scenario suite, anti-pattern and release gates.
- `references/orchestration-and-handoffs.md` — either Orca→Muse→Codex orchestration or direct Muse implementation→independent Codex audit, with workspace policy and no-human-router handoffs.

Then read only the selected/mode references required by the task under `modes/<mode>/references/`.

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

Treat this as an experience layer over existing authorities, **not automatically as a seventh lifecycle phase**. A mature implementation may audit ten capabilities while implementing only measured gaps:

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

These capabilities must reuse existing State, Event/Causal, Epistemic, Social, World/Regional, Projection and Validation layers rather than spawning one LLM agent or mutable subsystem per feature.

A key acceptance property is **context invariance**: enlarging offscreen population, object catalogs, historical depth or cultural records must not cause the same current scene to grow linearly in prompt size.

## Content-density / controlled-scale layer

When authority/state/retrieval are already strong but the world still feels generic, compartmentalized, or insufficiently inhabited, read `references/content-density-and-controlled-scale.md`.

The core method is:

`research broadly → audit actual content → select narrowly → Pilot → playtest → scale the method, not the template`

Do not turn reference research into a feature quota. Explicitly allow `ALREADY_PRESENT`, `DEFER`, and `REJECT` outcomes, including for attractive source-derived ideas.

Prefer **cross-linked content density** over isolated enrichment:

`character ↔ place ↔ domain practice/object ↔ history ↔ institution ↔ causal thread`

Depth is not completeness. Audit broadly but deepen only content with player-visible weakness. Avoid template-filling actors, locations, techniques/items, and threads.

After a successful Pilot, use two-wave controlled scale-up. Gate each content class independently as `GREEN_CONTINUE`, `YELLOW_LIMIT`, or `RED_STOP_CLASS`. Stop scaling a class when it becomes repetitive even if other classes remain valuable.

A content repository may grow substantially while the same active scene remains almost flat. Run 5x/10x inactive-content stress rather than assuming selective retrieval scales.

## SillyTavern-first layer

When the requested artifact is directly played in SillyTavern, read `references/sillytavern-first-playability.md`.

Optimization order becomes:

`SillyTavern playability > continuity > bounded context > causal consistency > feature richness > future-runtime purity`

For mature packages, freeze and measure the working baseline. Candidate capabilities are diagnostics, not quotas. Implement only `TUNE_EXISTING` / `IMPLEMENT_GAP` changes with clear player-visible return.

Tier A product, Tier B optional ST enhancement, and Tier C validation/future-runtime evidence must remain distinct.

For cultivation experience-surface work, also read `modes/cultivation/references/experience-and-openings.md`. In particular, user-only Tianji/offscreen information requires real epistemic quarantine; a prompt instruction saying “the PC does not know this” is insufficient if the secret remains in subsequent model-visible conversation history.

## World growth contract

When the sandbox may expand beyond an initial slice, prefer:

`stable macro skeleton → latent seeds → relevance/history trigger → deterministic materialization → stable ID → Canon → runtime evolution`

Latent areas/organizations may accumulate coarse history before detailed materialization. Once an identity is committed, generator/model/schema upgrades must not reroll it. Unknowns may remain unknown.

World size must not equal prompt size. Use hierarchical/facet retrieval and measure assembled context.

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

## Roleplay/reference pattern extraction

When studying third-party cards, lorebooks, novels, games, or other source corpora, extract transferable structure rather than copying plots or distinctive content.

Useful patterns include:
- Character Anchors and dialogue exemplars;
- public/private self and boundaries;
- Entity Facet Retrieval and hierarchical retrieval;
- procedural generation axes;
- history/official record/faction interpretation/folklore/rumor layers;
- deferred open-world plot states;
- player-agency guards;
- state/UI/narrative projection separation;
- validated world-mutation transactions;
- institutions whose worldview is visible through practical rules;
- domain mechanics that change daily life rather than only labels/stats;
- history that leaves present-day traces;
- delayed payoff through recontextualization rather than retcon.

Track derivation/homogenization risk. External references should make the research space larger, not force the implementation pass larger.

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

## Evidence quality

A test counts only when the behavior being wrong can make it fail.

Do not count:
- `assert(true)` / unconditional PASS;
- fixtures that certify values they just assigned;
- `expected = implementation output`;
- mocks that bypass claimed authority/retrieval paths;
- generated transcripts that merely grade themselves;
- custom projection metrics presented as exact product context without fidelity evidence.

Use mutation and blind tests where behavior is experiential: character differentiation, place identity, domain-mechanic differentiation, region contrast, ignored-thread continuation, knowledge leakage, retrieval isolation, and context scaling.

## Shared core workflow

1. Resolve the real repo/package/workspace and freeze authoritative inputs, IDs, hashes/provenance, schema versions and user scope.
2. Select one primary mode and **load `modes/<mode>/SKILL.md`**. If that mode depends on the generic core, load `modes/generic/SKILL.md` as well.
3. Classify narrow vs living-world task shape and load only the shared/mode references needed.
4. If living-world scope applies, assess the six-phase lifecycle and continue from the earliest materially incomplete phase instead of restarting mature work.
5. If lived-world experience depth is in scope, audit existing capabilities first and add only measured gaps with context-invariance tests.
6. If the machinery is already strong but content quality/density is weak, run the content-density method: reference/audit without Canon changes → narrow Pilot → playtest → controlled scale-up only if the Pilot earns it.
7. Write or update the domain contract before expanding content.
8. Keep one authority owner per mutable fact class; use explicit transitions, append-only events where appropriate, migrations and deterministic replay.
9. Separate facts, observations, estimates, beliefs, user-only projections and commentary.
10. Project sparse state/context by relevance and knowledge rights.
11. Validate schema, references, legality, privacy, retrieval, save/reload, deterministic replay, mutations and player-facing scenario behavior.
12. Run long-session gameplay review when the product claims persistent/living-world quality.
13. Report exact mode, versions, evidence, tests, limitations, human gates and release status.

## Mode-specific rules

### Generic

Load `modes/generic/SKILL.md` first. Keep vocabulary domain-neutral in the shared core. Put domain concepts in `01_Domain/domain_profile.json`. Use `modes/generic/references/anti-patterns-and-donts.md` as a hard gate for living worlds.

### Competitive

Load `modes/competitive/SKILL.md` **and** the generic core when state/history/context/persistence are involved. Pin competition, league/circuit, season/stage, ruleset/patch, roster/eligibility and source date. Keep recommendation separate from legality. Matchups are conditional, not eternal scalar truth. If the product includes persistent careers, teams, staff or daily life, also apply the shared actor/relationship/gameplay lifecycle and content-density method when appropriate. Read `modes/competitive/references/competitive-anti-patterns-and-donts.md`.

For a new competitive package, scaffold with the generic core using domain ID `competitive_rules`, then apply `modes/competitive/assets/competitive_domain_profile.json`; include `modes/competitive/assets/draft_contract.schema.json` when draft/lineup mechanics are in scope.

### Cultivation

Load `modes/cultivation/SKILL.md` plus the generic core where referenced. Build a society and simulation rather than a lore pile. Keep public registry, story truth, runtime state and context index separate. Use regional interpretation rather than a universal game level, sparse active casts, layered time ticks, permanent death with legacy, organization/sect ecology, deterministic world expansion and selective SillyTavern packaging.

For mature experience-surface work, read `modes/cultivation/references/experience-and-openings.md`.

For content-quality deepening and scale-up, read `modes/cultivation/references/content-renaissance-and-scale-up.md`. Favor technique-as-life, institution-as-practical-ideology, history-in-present, mortal substrate, functional exploration, xianxia-specific blind tests, Pilot-first authoring, and two-wave scale-up.

Read `modes/cultivation/references/cultivation-anti-patterns-and-donts.md`.

## Multi-agent orchestration

Do not force an orchestrator merely because one exists.

Two valid patterns are:

- `Orca orchestration/workspace → Muse primary implementation → Codex independent audit/small fixes`
- `Muse direct primary implementation → explicit self-gate/handoff → STOP → Codex independent audit`

Use the lightest pattern that preserves workspace continuity and independent acceptance. The user should not act as a repeated copy/paste router. See `references/orchestration-and-handoffs.md`.

Respect declared workspace-root policy; for Windows `D:\AI`, do not place project/worktree/agent/build/cache work on `C:\`.

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

For competitive from zero, use the generic scaffold route described above.

## Release honesty

Do not call a build Final because JSON parses, simulations run, self-gates say PASS, or generated scenario tests pass. Distinguish automated validation, deterministic simulation, faithful package-level tests, implementer self-gates, independent audit, and actual human long-session playtesting.

Use Alpha or Release Candidate until the relevant experiential gates are honestly satisfied.
