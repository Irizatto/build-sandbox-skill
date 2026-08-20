# Anti-Patterns and Hard DON’Ts

Treat these as build-time constraints, not optional style advice. A package that materially violates them is not release-ready merely because schemas validate.

## Retrieval and lorebook

- **Do not use high-frequency generic words as selective retrieval keys.** Reject empty keys, stopword-like keys, generic verbs/nouns, and generic role words unless a secondary condition makes the trigger specific.
- **Do not use single-character CJK keys by default.** Characters such as `的`, `一`, `是`, `了`, `我`, or similarly frequent characters create near-Always-On retrieval. Any single-character key requires explicit justification plus collision tests.
- **Do not use generic titles or offices as actor-specific triggers.** `宫主`, `门主`, `队长`, `教练`, `经理`, `医生`, `老师`, `captain`, etc. can load an unrelated dossier. Prefer canonical names, stable aliases, organization-qualified roles, and secondary keys.
- **Do not assume whitespace or whole-word matching works equally across languages.** Chinese, Japanese, and other non-whitespace languages require language-aware key design and explicit trigger tests.
- **Do not create mega-entries whose many unrelated keys load the same large block.** Split large entities into facets or hierarchical entries.
- **Do not allow trigger avalanches.** One ordinary sentence must not activate a large fraction of the lorebook through overlapping aliases, broad concepts, or recursive chains.
- **Do not enable recursive retrieval without bounded depth, cycle checks, and token tests.**
- **Do not treat a lore hit as proof of current presence, current state, knowledge, or relevance.** Static lore may identify an entity; runtime state decides whether it is alive, present, informed, available, or involved.
- **Do not use static World Info as authority for mutable state.** Location, health, inventory, relationship state, office holder, schedule, event result, current ruleset, and similar facts belong to the runtime owner.
- **Do not rely only on nominal lorebook token budgets.** Measure the fully assembled prompt under adversarial trigger combinations.

### Required retrieval tests

At minimum test:

1. ordinary dialogue containing common nouns and role words;
2. CJK prose containing frequent single characters;
3. ambiguous aliases shared by multiple actors or organizations;
4. one entity name plus several adjacent concept terms;
5. recursive references near the configured scan limit;
6. an actor mentioned historically while currently absent or dead;
7. a scene in which no important lore should load.

Validators should include deliberately bad fixtures and prove that broad-key, single-character, empty-key, title-collision, mega-entry, and recursion-loop cases fail.

## Context architecture

- **Do not dump raw databases into prompts.** Project sparse views based on location/topology, current mechanic, relationship, event, recent contact, knowledge rights, and relevance.
- **Do not place complete formal NPC biographies in Always-On context.** Load identity plus only currently relevant facets.
- **Do not keep obsolete phase material active.** Unload resolved phases, expired events, stale rules, old schedules, and irrelevant dossiers.
- **Do not let private truth leak into public or player-facing packets.** Separate world truth, actor belief, player knowledge, rumor, and narrator-only hypotheses.
- **Do not stack multiple memory/state extensions that own the same fact class.** Define one runtime owner for current state, time, memory, summarization, and authoritative transitions.
- **Do not solve context pressure only by raising token budgets.** First reduce duplication, improve retrieval specificity, facet large entities, and project sparse state.

## State, persistence, and causality

- **Do not let prose itself commit consequential state.** Narrative may propose or render; the authoritative mechanic/runtime commits the delta.
- **Do not reroll committed outcomes on reload.** Seed randomness from stable event coordinates and persist resolved outcomes.
- **Do not reuse stable IDs for a different entity.** Death, retirement, renaming, succession, and role changes are state/history transitions, not identity replacement.
- **Do not erase history when an entity leaves play.** Preserve relationships, debts, offices, descendants, records, obligations, techniques, and historical references as applicable.
- **Do not create parallel `final`, `final2`, `final_final` registries.** Migrate or explicitly version the canonical authority.
- **Do not retroactively invent authoritative history merely to support the current scene.** Unknown facts remain unknown until generated through an authorized creation path and committed with provenance.
- **Do not let important generated entities or places become persistent canon without stable identity, provenance, and ownership.**

## Actors and relationships

- **Do not make every actor reactive to the player.** Actors require independent goals, schedules, resources, obligations, relationships, and offscreen agency.
- **Do not give the player universal narrative priority.** Other actors may obtain opportunities, form relationships, fail, leave, succeed, or die without player involvement.
- **Do not let actor knowledge equal narrator knowledge.** Consequential beliefs need plausible sources, observation time, confidence, or institutional channels.
- **Do not collapse relationships into a single affection score.** Distinguish familiarity, trust, respect, comfort, obligation, rivalry, resentment, authority, attachment, attraction, commitment, or other domain-relevant dimensions.
- **Do not speedrun intimacy through repeated conversation alone.** Important transitions require shared history, evidence, time, compatible boundaries, and hysteresis.
- **Do not make every actor share the same voice, ideology, emotional regulation, or optimization style.** Uniformly rational institutional reformers are still a character-collapse failure.
- **Do not make charm synonymous with beauty, youth, romance, or availability to the player.**
- **Do not let a player bookmark/favorite flag rewrite the actor’s in-world status.** A presentation/persistence preference may increase retention or detail, but must not automatically increase power, fame, affection, plot immunity, availability, or cosmic importance.

## Narrative and encounters

- **Do not force a plot beat every N turns or by a flat probability.** Beats require causal eligibility and should respond to scene momentum, goals, pressures, unresolved hooks, repetition, and current actors.
- **Do not turn every quiet scene into a crisis, secret, quest, romance, or revelation.** `Nothing important happens` is a valid outcome.
- **Do not make every stranger secretly important.** Ordinary workers, neighbors, competitors, clerks, travelers, and acquaintances are part of a living world.
- **Do not escalate every local problem into a world-saving plot.** Preserve micro stories, personal arcs, local disputes, regional threads, and generational stories at their natural scales.
- **Do not use coincidence as the default encounter router.** Important meetings need geography, schedule, invitation, institution, event, relationship, or another traceable path.
- **Do not use lore dumps as a substitute for discovery.** Let players encounter consequences, testimony, records, evidence, disagreement, and partial views.

## Generation and world expansion

- **Do not confuse quantity with world depth.** Hundreds of names, techniques, factions, teams, or artifacts do not create gameplay unless they produce differentiated decisions and consequences.
- **Do not generate important canon without checking collisions, authority, topology, relationships, and existing history.**
- **Do not let procedural generation silently overwrite established canon or close intentional unknowns.**
- **Do not generate every entity at the same detail tier.** Use dense-world/sparse-detail tiers and promote entities when history makes them important.
- **Do not pre-author the entire world merely to make it feel large.** Prefer a stable macro skeleton plus latent seeds that deterministically materialize when travel, investigation, trade, politics, or history makes them relevant.
- **Do not improvise an unbounded new region from nothing when the player crosses an edge.** Expansion should resolve from registered macro geography, regional constraints, seeds, provenance, and a commit step.

## Validation

- **Do not call a build complete because JSON parses, schemas pass, or unit tests are green.** Also test player-facing behavior, retrieval, leakage, long-session drift, weird actions, save/reload, offscreen simulation, and content exhaustion.
- **Do not validate only happy paths.** Include corrupted packages, ambiguous aliases, illegal actions, stale state, missing authority, long absences, dead actors, and intentionally bad retrieval keys.
- **Do not call an automated build Final before long-session human playtesting.** Use Alpha or Release Candidate when experiential validation is incomplete.

## Release gate

Ask:

> Could an ordinary player sentence accidentally load unrelated private lore, create false current-state implications, or cause a context avalanche?

If yes, retrieval is not ready.

Then ask:

> If the player disappears for a long period, do actors and organizations still produce plausible history without waiting for the player?

If no, the world is not yet persistent in the gameplay sense.
