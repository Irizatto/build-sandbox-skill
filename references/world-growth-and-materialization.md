# World Growth and Materialization

A large persistent sandbox should be **structurally large before it is textually large**.

Prefer:

`stable macro skeleton → latent seeds → relevance/history trigger → deterministic materialization → stable ID → Canon → runtime evolution`

instead of pre-authoring hundreds of shallow locations, factions or actors.

## Stable macro skeleton

Freeze only facts that must not move arbitrarily:
- macro topology or ecosystem structure;
- adjacency and major routes/links;
- broad regional/institutional identities;
- resource and authority patterns;
- historical constraints;
- anchor organizations;
- aggregate offscreen pressures.

Do not make the starting vertical slice the world center unless canon requires it.

## Latent is not nonexistent and not frozen

A latent area/entity has constrained potential but may not yet have full local detail. It can still participate in aggregate history.

Example:
- Year 0: a region exists as a profile + seed + aggregate state.
- Years 1–30: wars, trade shocks, migrations or resource pressure affect its aggregate state.
- Year 31: the player arrives. Materialization uses both the original seed and accumulated history.

Never generate it as if Year 31 were Year 0.

## Materialization transaction

Use an explicit transaction:

`trigger/request → resolve parent constraints → authority check → load current date/history → derive deterministic seed → generate candidate → validate collisions/invariants → allocate stable ID → commit identity/provenance → initialize runtime state → append event → project sparse context`

The commit should be atomic or recoverable. Do not leave half-canonical entities after failure.

### Stable seed coordinates

Derive randomness from stable coordinates such as world/save ID + latent seed ID + materialization schema/generator version. Wall-clock randomness must not reroll a committed identity.

### Canon precedence

Once materialized:
- Canon beats the generator;
- generator upgrades do not rewrite identity;
- migrations transform data explicitly;
- save/reload returns the same entity;
- later history changes state, not identity.

## Unknown Preservation

Distinguish:
- KNOWN;
- KNOWN-BUT-SPARSE;
- RUMORED;
- UNMAPPED / UNRESOLVED;
- INACCESSIBLE / UNKNOWN.

Crossing a frontier does not authorize retroactive omniscient history. Unknowns may remain open until an authorized generation/discovery path resolves them.

## Organization seeds

Organizations should materialize from constraints including:
- region/ecosystem;
- founding or preexistence semantics;
- resource dependencies;
- social base and recruitment;
- authority/governance;
- succession;
- property/finance;
- external obligations and rivals;
- historical scar/current pressure.

Distinguish:
- **latent preexisting organization** — already part of aggregate history but not detailed;
- **future formation possibility** — may come into existence only if causal conditions occur.

Organizations need life cycles: founding, recognition, growth, reform, stagnation, split, merger, migration, succession, decline, dissolution, legacy.

Office identity must be separate from office holder identity.

## Actor promotion

Generated/minor actors need stable IDs and provenance from first canonical appearance. They may later be promoted in simulation detail without becoming more important in-world.

Separate:
- world importance;
- simulation detail;
- current narrative relevance;
- player bookmark/favorite.

Promotion must not invent contradictory retroactive achievements, bloodlines, relationships or secrets.

## World scale without context scale

Use hierarchical sparse projection. Typical spatial world:

`world summary → current macro region → local network → site → scene → active actors`

A competitive/career world may use:

`competition/circuit → current season/stage → team/org → event → active participants`

Do not load the whole database because the world is large.

## Retrieval gates

Reject or heavily constrain:
- common high-frequency keys;
- single-character CJK keys;
- empty keys;
- generic role/title words as entity-specific triggers;
- ambiguous short aliases;
- mega-entries;
- uncontrolled recursion;
- a lore hit implying current presence, office, health or knowledge.

Measure the assembled context under adversarial combinations, not only configured token budgets.

## Core tests

At minimum test:
1. leave the starting area immediately;
2. materialize the same seed twice;
3. materialize after a long period of aggregate history;
4. leave and return years later;
5. organization leadership succession;
6. new organization formation after game start;
7. actor promotion without destiny inflation;
8. save/reload equivalence;
9. deterministic replay;
10. context budget and trigger collisions;
11. corrupted IDs, adjacency, provenance and seed conflicts.
