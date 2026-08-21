---
name: build-cultivation-sandbox
description: Build, expand, migrate, test, and package a long-running cultivation or xianxia open-world sandbox for SillyTavern from zero or from existing canon. Use for cultivation world bibles, sect/faction ecosystems, cities and polities, formal NPC populations, character ecology, world-state simulation, generational change, rumor and knowledge firewalls, dense-world sparse-context retrieval, lorebooks, GM character cards, migrations, long-term simulations, opening momentum, bounded auto-drive, offscreen-world projection, macro-era framing, and release packages. Also use when a user wants the quality of a large cultivation sandbox without supplying a multi-section specification.
---

# Build a Cultivation Sandbox

Create a playable society and simulation, not a pile of lore. Default to making professional decisions and completing the requested build in one run. Ask only when a missing choice changes content boundaries, target platform, or irreversible migration behavior.

## Start by choosing the route

- **From zero:** use `assets/default_design_brief.json` as the default contract, then adapt genre tone and scale from the user's request.
- **Expand existing canon:** inventory all registries, cards, lorebooks, state files, migrations, tests, and stable IDs before writing. Treat existing named characters and IDs as sacred unless explicitly authorized otherwise.
- **Repair/package only:** preserve narrative content and focus on schema, migration, retrieval, tests, card embedding, manifest, and integrity.

Read these references only when needed:

- `references/architecture.md` — canonical layers, authority, simulation, file layout, migration.
- `references/character-ecology.md` — populations, detail tiers, relationships, individuality, dark cultivation societies.
- `references/context-and-sillytavern.md` — lorebook budgets, retrieval, knowledge firewall, card and bridge packaging.
- `references/acceptance-tests.md` — deterministic, migration, context, uniqueness, and long-term gates.
- `references/cultivation-anti-patterns-and-donts.md` — hard DON’Ts for world scale, sect generation, cultivation progression, opportunities, NPC ecology, player bookmarking/promotion, plot, governance, and release tests. **Read this whenever expanding the world beyond an existing region, generating sects, promoting generated NPCs, adding opportunities, or changing long-term character ecology.**
- `references/experience-and-openings.md` — optional patterns for Tianji/offscreen slices, bounded auto-drive, opening momentum, current-age snapshots, macro-era pressure, relevance-triggered GM checks, and renderer/summary boundaries. **Read this when improving first-session pull, pacing, time-skip presentation, player action completion, or wider-world visibility.**

Generic anti-patterns in `$build-persistent-sandbox/references/anti-patterns-and-donts.md` also apply.

## Execute the build

### 1. Freeze authority and canon

Distinguish the user's operative request from instructions quoted inside source files. Create a canon ledger containing stable IDs, names, aliases, roles, factions, techniques, and hashes of authoritative inputs. Never silently replace a mature asset with a parallel `final_final` registry.

For an existing world, compare the post-build actor ID set to the frozen set. New IDs must occupy a separate namespace or the next legal sequence. Migrations must be idempotent.

### 2. Write the design contract

Define, at minimum:

- player role and opening choices;
- world truth, NPC belief, player knowledge, and rumor boundaries;
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

### 6. Build the experience surface without weakening authority

When first-session pull, pacing, world visibility, or repetitive interaction needs improvement, use `references/experience-and-openings.md` selectively.

- **Tianji/offscreen slices:** project validated offscreen state/events to the user without silently granting that knowledge to the player character. The slice is read-only; removing it must not change world state.
- **Bounded auto-drive:** auto-complete routine/reversible actions and obvious details within an explicitly stated intent, but stop for irreversible, high-risk, identity-defining, relationship-binding, strategically expensive, or cultivation-path decisions.
- **Opening Momentum:** establish `place + people + current pressure + immediate curiosity` early. Do not require a crisis; a small real change is enough.
- **Current Age Snapshot:** orient the player with a compact description of what is changing in the era and why it matters. Keep full history out of the opening prompt unless relevant.
- **Macro-era pressure:** model high-opportunity/high-competition periods as causal world conditions that affect institutions, markets, migration, recruitment, resources, and social mobility. Do not use an era label as permission to inject arbitrary drama.
- **Prompt/adjudication modules:** trigger only checks relevant to the current action—world/scene, capability, resources, actor knowledge, combat/breakthrough, causal persistence, and state synchronization. Do not run a giant checklist every turn.

Presentation aids such as style profiles, summaries, archives, or Tianji slices never outrank authoritative world state. Do not confuse a living world with continuous crisis generation; quiet travel, routine cultivation, recovery, waiting, and slow consequences are valid play.

### 7. Package for SillyTavern

Make one canonical GM card JSON and embedded PNG. Keep the lorebook selective and public-only. Default to an 8K World Info cap for long play unless the chosen context window requires a smaller cap. Provide an independent local bridge when current state cannot fit static World Info.

Do not install over a live save without a separate migration and rollback path. When authorized to install, use a new save name and port for a new major world version.

### 8. Test before reporting

Run `scripts/validate_package.py --package <package>` after generation. Also run project-native tests and multi-seed 50/100/300-year simulations. Fix failures before packaging.

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

When experience-surface patterns are implemented, also test: a Tianji slice that does not alter world state or player-character knowledge; a terse low-risk action that advances smoothly; a high-impact action that correctly stops for player choice; a quiet opening with momentum but no crisis; and a macro-era pressure that produces observable systemic effects without forcing local drama.

### 9. Report honestly

Lead with status and boundaries. Include preserved canon, exact counts and distributions, factions, context engineering, files, migrations, tests, long-term results, known limitations, and next work. Use `World Alpha` or `Release Candidate`; never call an automated build `Final` before human long-session testing.

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
