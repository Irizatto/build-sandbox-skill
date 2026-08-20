# Architecture and authority

## Contents

1. Canon layers
2. Suggested package layout
3. Runtime actor contract
4. Simulation and history
5. Migration rules

## Canon layers

Use one authority per fact class:

- Design Bible: invariant world rules and creative direction.
- Public lore: what can safely enter prompts.
- Story registry: GM truth and private characterization.
- Runtime state: current mutable facts.
- Historical archive: causal summaries and legacies.
- Context index: retrieval metadata, never narrative authority.

When two sources disagree, prefer the more specific frozen contract, then the latest explicit user instruction, then the canonical runtime authority. Record the resolution; do not duplicate both.

## Suggested package layout

```text
00_Core_GM_Character/
01_Core_Rules/
02_Player_Persona/
03_World_Lorebook/
04_Geography/
05_Cultivation_System/
06_Technique_Lorebook/
07_Factions/
08_NPC_System/
09_Economy/
10_Encounter_Engine/
11_World_State/
12_Memory_System/
13_Rumor_Knowledge_System/
14_Sect_Governance/
15_Generational_System/
16_System_Module/
17_Openings/
18_Test_Scenarios/
manifest.json
package_integrity.json
```

Do not create parallel registries with names such as `final_final_v2`. Version the canonical file or add a migration.

## Runtime actor contract

Runtime actors should include immutable identity, social position, body state, agency, knowledge, history, and deepening state. Keep private fields out of public serializers.

Use deterministic random values derived from `(simulation seed, year, actor ID, event label)`. Every major outcome should point to source events. A political official or information broker may change more history than an isolated stronger fighter.

## Migration rules

1. Freeze old actor and faction ID sets.
2. Reject namespace collisions.
3. Copy old state; never mutate the source save during candidate construction.
4. Add new registries and references.
5. Validate every foreign key.
6. Assert exact set difference.
7. Add a migration marker and make a second run return the same state.
8. Preserve dead actors and old IDs.
