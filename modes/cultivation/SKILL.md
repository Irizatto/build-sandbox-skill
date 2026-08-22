---
name: build-cultivation-sandbox
description: Build, expand, migrate, test, and package a long-running cultivation or xianxia open-world sandbox for SillyTavern from zero or from existing canon. Use for cultivation world bibles, sect/faction ecosystems, cities and polities, formal NPC populations, character ecology, world-state simulation, generational change, rumor and knowledge firewalls, dense-world sparse-context retrieval, lorebooks, GM character cards, migrations, long-term simulations, experience-surface upgrades, content renaissance, technique-as-life design, controlled regional scale-up, selective runtime/UX audits, extraordinary-life design, and release packages. Also use when a user wants the quality of a large cultivation sandbox without supplying a multi-section specification.
---

# Build a Cultivation Sandbox

Create a playable society and simulation, not a pile of lore. Default to making professional decisions and completing the requested build in one run. Ask only when a missing choice changes content boundaries, target platform, or irreversible migration behavior.

## Start by choosing the route

- **From zero:** use `assets/default_design_brief.json` as the default contract, then adapt genre tone and scale from the user's request.
- **Expand existing canon:** inventory all registries, cards, lorebooks, state files, migrations, tests, and stable IDs before writing. Treat existing named characters and IDs as sacred unless explicitly authorized otherwise.
- **Repair/package only:** preserve narrative content and focus on schema, migration, retrieval, tests, card embedding, manifest, and integrity.
- **Experience-surface upgrade:** when the world already works but play has surface friction, use `references/experience-and-openings.md` and implement only measured gaps.
- **Content renaissance / scale-up:** when architecture is strong but content remains generic, isolated, or insufficiently cultivation-specific, use `references/content-renaissance-and-scale-up.md`.
- **Selective runtime / UX audit:** when external cards suggest state, context, memory, institution, extraordinary-life, or diegetic-UX improvements, use `references/selective-runtime-ux-and-extraordinary-life.md` and require a reproducible gap before engineering changes.

Read these references only when needed:

- `references/architecture.md` — canonical layers, authority, simulation, file layout, migration.
- `references/character-ecology.md` — populations, detail tiers, relationships, individuality, dark cultivation societies.
- `references/context-and-sillytavern.md` — lorebook budgets, retrieval, knowledge firewall, card and bridge packaging.
- `references/acceptance-tests.md` — deterministic, migration, context, uniqueness, and long-term gates.
- `references/cultivation-anti-patterns-and-donts.md` — hard DON’Ts for world scale, sect generation, cultivation progression, opportunities, NPC ecology, player bookmarking/promotion, plot, governance, and release tests. **Read this whenever expanding the world beyond an existing region, generating sects, promoting generated NPCs, adding opportunities, or changing long-term character ecology.**
- `references/experience-and-openings.md` — bounded auto-drive, Opening Momentum, Current Age projection, Tianji/offscreen slices, and user-only epistemic quarantine. **Read this when improving first-session pull, action completion, time-skip/wider-world presentation, or surface pacing.**
- `references/content-renaissance-and-scale-up.md` — reference harvest, cross-linked content density, character/place/technique deepening, institutional ideology, history-in-present, functional exploration, Pilot design, and two-wave controlled scale-up. **Read this when the sandbox is technically strong but does not yet feel sufficiently inhabited or cultivation-specific.**
- `references/selective-runtime-ux-and-extraordinary-life.md` — architecture-authorization gates, Tier A/B/C classification, incremental-state semantics, Chronicle/reveal lifecycle, context-fidelity evidence, functional institutions, structural contradictions, cultivation ecological physics, extraordinary life, diegetic queries, and decision traces. **Read this when a mature world is being selectively upgraded from external-card or runtime-UX research.**

Generic anti-patterns in `$build-persistent-sandbox/references/anti-patterns-and-donts.md` also apply.

## Execute the build

### 1. Freeze authority and canon

Distinguish the user's operative request from instructions quoted inside source files. Create a canon ledger containing stable IDs, names, aliases, roles, factions, techniques, and hashes of authoritative inputs. Never silently replace a mature asset with a parallel `final_final` registry.

For an existing world, compare the post-build actor ID set to the frozen set. New IDs must occupy a separate namespace or the next legal sequence. Migrations must be idempotent.

For mature builds, measure the real current baseline before proposing a delta. Classify candidate changes as `KEEP_EXISTING`, `TUNE_EXISTING`, `IMPLEMENT_GAP`, `DEFER_NO_PROVEN_RETURN`, or `BLOCKED`. Only `TUNE_EXISTING` / `IMPLEMENT_GAP` authorize work.

For engineering-heavy mature-world changes, a cleaner architecture alone is not authorization. Require a reproducible player-facing, state-correctness, privacy/knowledge, save/reload, retrieval/context, deterministic, or current-SillyTavern failure before adding a new owner, router, compiler, state layer, or runtime dependency.

Keep delivery tier explicit:

- `TIER_A_CANONICAL_ST` — current canonical SillyTavern behavior;
- `TIER_B_OPTIONAL_ST` — optional ST enhancement with Tier A still usable when disabled;
- `TIER_C_VALIDATION_OR_FUTURE_RUNTIME` — harness/prototype/future runtime evidence;
- `CONTENT_ONLY` / `SKILL_ONLY` / `NO_PROJECT_CHANGE` where applicable.

Never claim a Tier C prototype proves a Tier A player-facing feature.

### 2. Write the design contract

Define, at minimum:

- player role and opening choices;
- world truth, NPC belief, player knowledge, rumor, and user-only projection boundaries;
- cultivation as regional interpretation rather than a universal numeric level;
- geography, polities, routes, factions, offices, resources, and supply chains;
- encounter, governance, memory, technique, economy, historical archive, and succession rules;
- how the world moves without the player;
- explicit prohibitions such as plot armor, forced romance, omniscient NPCs, and celebrity cameos.

Prefer mechanisms with costs, preconditions, decay, exposure, and counterplay over scalar luck.

For large worlds, distinguish the **stable macro skeleton** from **latent regional/organization seeds**. Do not pre-author hundreds of empty sects, but also do not improvise unconstrained geography when the player crosses the current region boundary. Materialize new regions, sects, routes, and recurring actors through a validated seed-to-canon pipeline.

### 3. Build dense world, sparse context

Separate four layers:

1. **Public registries:** safe identity and reputation.
2. **Story registries:** GM truth, fears, secrets, agendas, beliefs, and long arcs.
3. **Runtime state:** current location, health, cultivation, office, relationships, obligations, events, and death.
4. **Context index:** region, faction, relationship, event, and recent-contact retrieval keys.

Use the retrieval chain:

`region → faction → relationship → current event → recent contact → relevance rank → active cast`

Default active cast: 4–10. Meetings: 10–16. Hard maximum: 20. Do not place all formal NPC biographies in Always-On lore.

Apply both generic and cultivation-specific anti-pattern checks to World Info keys. Reject common-word/single-character triggers, generic titles used as actor keys, mega-entries, trigger avalanches, far-field accidental activation, and static-lore-as-current-state assumptions.

World size must not equal prompt size. Inactive actors, techniques, regions, institutions, histories, and reference content should cost zero or near-zero context.

### 4. Design population ecology

Define an exact net-new population target and exact distributions for social role, cultivation band, gender, species, age, and detail tier. Use A/B/C detail tiers rather than equal biographies.

Every formal NPC needs stable identity, social position, public face, deep personality, desire, fear, flaw, principle, bias, secret, three horizons of goals, resources, obligations, health, technique, knowledge, beliefs, historical-agency factors, and 2–5 meaningful relationships.

Create social clusters with sparse bridges. A famous person may remain offscreen. A charming person need not be beautiful, young, romantic, or available to the player.

When building demonic or heterodox societies, supply institutional reasons they survive: contracts, registration, quotas, hierarchy, kinship, audit, compensation, shared infrastructure, or credible retaliation. Prefer predictable danger over random madness.

Allow low-detail generated actors to be **promoted** when history makes them important. Keep four concepts separate: `world_importance`, `simulation_importance`, `narrative_importance`, and `player_bookmark`. A player bookmark may preserve and deepen an actor, but must not automatically increase affection, talent, cultivation, luck, fame, office, plot armor, or connection to world mysteries.

### 5. Implement state and history

Use layered ticks unless the project defines another cadence:

- annual: age, health, cultivation, risk, mortality;
- five-year: goals, travel, office, marriage, discipleship, reputation, failure, fade;
- ten-year: faction, economy, succession, resources, historical summaries.

Offscreen simulation is coarse but real. Death is permanent, while IDs, relationships, disciples, descendants, debts, techniques, offices, and legacies persist. NPCs may found organizations, create methods, change law, fail, retire, or vanish from fame.

When a latent region, sect, place, or actor first becomes concrete, use:

`macro constraints → seed → relevance trigger → deterministic materialization → collision/authority validation → stable ID commit → sparse projection`

Once materialized, it is canon and evolves independently.

For partial state updates, omission from narration is not deletion. Prefer explicit retain/update/delete/purge/route semantics through the existing state owner, with idempotent retry and save/reload equivalence where applicable. Chronicle/summary views derive from Event History and never become a second truth store.

### 6. Improve the experience surface only where the baseline is weak

Use `references/experience-and-openings.md` for a mature playable world whose problems are at the surface rather than the authority layer.

Default high-return patterns are:

- **Bounded auto-drive:** complete routine execution but never manufacture high-impact player intent.
- **Opening Momentum:** establish `place + people + current pressure + immediate curiosity`; curiosity does not require crisis or anomaly.
- **Current Age Snapshot:** selectively project existing Canon; never invent a macro era merely to energize the opening.
- **Tianji/offscreen slices:** project already-valid offscreen state/events sparsely. User-only slices require real epistemic quarantine so display-visible secret text is absent from subsequent model-visible prompt history.

Do not turn these into mandatory subsystems. Quiet life and zero-Tianji turns remain valid.

### 7. Run Content Renaissance only after machinery is strong

Use `references/content-renaissance-and-scale-up.md` when the sandbox is technically persistent but still feels like a generic simulator wearing cultivation vocabulary.

First audit/reference-harvest without changing Canon. Then select a small Pilot. Prefer:

`characters ↔ locations ↔ techniques ↔ history ↔ institutions/market ↔ causal threads`

over separate piles of enrichment.

A technique should be a way of living, not only a skill effect: practice loop, body/perception, resources/environment, institution, noncombat use, combat geometry, failure/side effect, provenance/transmission, and cultural meaning may all matter selectively.

Use existing world laws to shape civilization before inventing new laws. Make institutions reveal values through practical procedures. Make old history visible in present objects, routes, customs, rights, markets, memories, and technique variants. Preserve ordinary mortals as labor/logistics/memory/social substrate.

For functional exploration, begin with 1–2 high-return affordance families such as market/provenance, institution/access, or cultivation-knowledge investigation rather than a full management UI.

After a successful Pilot, scale in two waves. Gate each class independently as `GREEN_CONTINUE`, `YELLOW_LIMIT`, or `RED_STOP_CLASS`. Stop scaling a class when it becomes repetitive even if other classes remain valuable.

### 8. Apply selective runtime / extraordinary-life / diegetic UX patterns only to proven gaps

Use `references/selective-runtime-ux-and-extraordinary-life.md` when external-card research suggests deeper engineering or UX changes.

High-value rules include:

- omission from current narration does not delete durable state;
- active-scene LOD may discard transient presentation but not durable actor identity/state;
- Chronicle and summaries are Event History projections, not Canon owners;
- `UNKNOWN → FIRST_REVEAL → KNOWN → RECALL_WHEN_RELEVANT` may reduce repeated exposition when current knowledge/memory owners can support it;
- state/knowledge eligibility should gate context before broad keyword retrieval where the current package actually leaks irrelevant or private context;
- context measurements from simulations/harnesses must state fidelity to real assembled SillyTavern context;
- institutions should expose values through facilities, procedures, permissions, costs, work, and refusal—not identical generic currencies;
- cultivation ecological physics should be derived from existing metaphysical rules rather than adding a new cosmology;
- realm/path/body differences should remain visible in sleep, food, weather, travel, storage, labor, injury, medicine, architecture, privacy, and social treatment where Canon supports them;
- diegetic journals/registries/market information and decision traces may expose only player-entitled facts from real sources; presentation never becomes omniscient authority.

Tune existing owners first. New routers/compilers/databases are last-resort responses to reproduced failures, not default architecture upgrades.

### 9. Package for SillyTavern

Make one canonical GM card JSON and embedded PNG. Keep the lorebook selective and public-safe. Treat configured token caps as ceilings, not targets. Do not solve mature-world depth by raising the global budget.

Provide an independent local bridge only when the requested deployment genuinely needs one; base Tier A play should not silently depend on future runtime infrastructure.

Do not install over a live save without a separate migration and rollback path. When authorized to install, use a new save name and port for a new major world version.

### 10. Test before reporting

Run `scripts/validate_package.py --package <package>` after generation. Also run project-native tests and multi-seed 50/100/300-year simulations where applicable. Fix failures before packaging.

Required evidence:

- exact actor delta and preserved old IDs;
- registry/reference validity;
- duplicate name and composite-role checks;
- ordinary-location sparse context, faction-region retrieval, return/unload, meeting, hard cap;
- public packets contain no story secrets;
- deterministic replay and save/reload equivalence;
- deaths, breakthroughs, failures, relationships, fame, fade, succession, and sparse high tiers across seeds;
- card JSON/PNG equivalence, manifest honesty, SHA-256 integrity, and ZIP test.

Also run the negative/world-expansion scenarios in `references/cultivation-anti-patterns-and-donts.md`, including immediate departure from the opening region, latent sect materialization and revisit, generated-sect collision handling, ordinary-NPC bookmarking/promotion, quiet travel without jackpot delivery, and distant-region differentiation.

For experience-surface work, mutation-test auto-drive agency, opening escalation, Current Age unsupported canon, Tianji state mutation, and Tianji knowledge/prompt leakage.

For Content Renaissance, use blind/mutation tests for character differentiation, location identity, technique-as-life differentiation, institution values, historical traces, ignored-thread continuation, regional contrast, and knowledge provenance. `assert(true)`, self-certifying fixtures, and generated transcripts that only grade themselves are not acceptance evidence.

For controlled scale-up, stress 5x/10x inactive Renaissance content. The same active scene should remain approximately flat in assembled context. If content repository size rises while active prompt rises proportionally, the scale-up fails.

For selective runtime/UX work, mutation-test the actual claimed tier: break RETAIN/state idempotence, force inactive context, leak private knowledge, remove institution permission, or expose hidden information in a decision trace and require the relevant test to fail. Prefer actual assembled SillyTavern context; if only a projection/simulator is available, report measurement method, fidelity, known differences, what the number proves, and what it cannot prove.

### 11. Report honestly

Lead with status and boundaries. Include preserved canon, exact counts/distributions, context engineering, files, migrations, tests, long-term results, known limitations, and next work. Distinguish automated validation, faithful package simulation, generated playtest transcripts, and actual human long-session play.

Report Tier A, Tier B, Tier C, content-only, Skill-only, and no-project-change outcomes separately when the distinction matters.

Use `World Alpha` or `Release Candidate`; never call an automated build `Final` before the relevant independent/human experiential gates.

## Bootstrap commands

Create a clean package skeleton:

```powershell
python scripts/scaffold_sandbox.py --output <directory> --name <world-name>
```

Validate a package:

```powershell
python scripts/validate_package.py --package <directory>
```

Treat script output as diagnostic evidence, not a substitute for scenario tests and human judgment.
