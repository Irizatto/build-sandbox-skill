# Token-Safe Lived World Experience

Use this reference when a persistent sandbox must feel inhabited in ordinary life without making world size, history length, actor count, item count, or cultural depth scale linearly with LLM context.

The goal is not more lore. The goal is more world state that can exist outside the prompt and be projected sparsely when relevant.

## Core invariant

Prefer:

`authoritative structured state → deterministic filters → compact projection → LLM narrative`

Never solve lived-world depth primarily through:

`more Always-On lore → larger rolling summaries → more raw registry injection → higher context budget`

World size must not equal prompt size.

## Lived-world capability set

The following ten capabilities are implementable with current persistent-sandbox architecture when they extend existing state/event/context authorities rather than creating parallel prompt-owned systems.

1. Everyday World / ordinary life.
2. Embodiment / body state.
3. Material Culture.
4. Culture / Ritual as social grammar.
5. Information Ecology.
6. Player-created History / creation lineage.
7. Discovery / Unknown Preservation.
8. Social Friction / access and obligation.
9. World Memory / scars and legacy.
10. Belonging / personal anchors.

Player-created history is higher risk because it writes Canon. Belonging infrastructure is implementable, but no system should claim to guarantee emotional attachment.

## Shared architecture

Do not build ten independent services or ten always-running agents. Reuse a small set of substrates:

1. **State / Entity Layer** — actor, player, place, organization, item/template, creation.
2. **Event / Causal Layer** — committed events, provenance, scars/legacy derivation.
3. **Epistemic Layer** — observations, claims, beliefs, rumors, player knowledge.
4. **Social Layer** — relationship dimensions, access, obligation, norms.
5. **World/Regional Layer** — regional seeds, discovery state, material/cultural variants.
6. **Projection Layer** — Context Compiler selects current facets.
7. **Validation Layer** — legality, permissions, Canon-writing, idempotency.

Extend existing owners. Never create a shadow relationship graph, shadow event log, shadow mutable lorebook, or second Canon registry merely to implement lived-world flavor.

## Context selection order

Before projecting any lived-world record, filter by:

1. authority validity;
2. actor/player knowledge rights;
3. current location and physical reachability;
4. present/referenced actors;
5. current action/intent;
6. relationship/access constraints;
7. current time/season/environment;
8. causal relevance and unresolved local history;
9. personal anchors;
10. semantic ranking;
11. token budget and deduplication.

Embedding similarity is never authority and never bypasses knowledge rights.

## Context-budget rule

Do not give each capability a permanent prompt section. Most scenes should activate only a subset.

For a conventional long-running text sandbox, a useful engineering target is:

- ordinary low-complexity scene: roughly 250–900 incremental tokens from lived-world facets;
- ordinary social scene: roughly 500–1,200;
- unusually dense cultural/social scene: preferably below roughly 1,800;
- treat approximately 2,000 incremental tokens as a warning boundary unless measured evidence justifies more.

These are targets, not required allocations and not permission to pad prompts. Existing project budgets take precedence when stricter.

## 1. Everyday World

Support residence/home anchors, recurring shops/services/workplaces, availability schedules, ordinary actor obligations, stable mundane locations, seasonal/daypart differences, local prices/supply effects when simulated, and repeatable low-stakes actions.

Project only the current place, currently available services, a few relevant local changes, relevant familiar-person history and current time constraints.

Do not turn daily life into mandatory quests, simulate every shopkeeper with a continuous LLM, or load a city schedule into every prompt.

## 2. Embodiment

Represent relevant body state structurally: fatigue, sleep debt, injury, pain, recovery, environmental exposure, illness/poison/intoxication, mobility/concentration/endurance constraints and domain-specific bodily adaptations.

Project only action-relevant or threshold-crossing conditions. Healthy/normal dimensions should usually be omitted.

Data can be hard while presentation stays soft. Do not print a full RPG HUD every response and do not let prose invent authoritative wounds.

## 3. Material Culture

Use:

`material template → regional/social variant → producer/craft lineage → current instance when needed`

Store origin, material, use, price/availability band, social usage, maintenance dependencies and provenance for important instances.

The catalog stays outside the prompt. Project only what is seen, used, bought, compared, repaired or culturally diagnostic in the current scene.

Do not confuse thousands of item names with material culture and do not instantiate every trivial object as a permanent unique entity.

## 4. Culture / Ritual as Social Grammar

Represent norms operationally rather than as adjectives. A norm may include scope, triggering behavior, expected interpretation, violation severity, affected social groups, exceptions and historical version/provenance.

The same action may be interpreted differently by different actors because personality, age, status, relationship and goals still matter.

Only scene-relevant norms should be evaluated/projected. Do not load a full regional culture bible or make every resident react identically.

## 5. Information Ecology

Distinguish at least:

- world truth;
- observation;
- evidence/source;
- claim/report;
- belief + confidence;
- rumor/public narrative;
- player knowledge;
- freshness/time;
- propagation channel when relevant.

Information propagation should primarily be event/rule/relationship/institution driven. Persistent existence does not require one LLM agent per NPC.

An actor receives only facts/claims/beliefs it can legitimately access. Never dump the global knowledge graph or treat Memory as Truth.

## 6. Player-Created History

Allow validated creations — methods, variants, crafts, writings, shops, organizations, practices, teachings or rules as appropriate to the domain — to enter history through:

`proposal → prerequisite/capability validation → creation event → stable ID if persistent → provenance → adoption → variants/derivations → spread/rejection → legacy/forgetting`

Track creator/collaborators, time/place, source lineage, ownership/rights when relevant, adopters, variants, attribution state and causal consequences.

Creation is not automatic fame, power, correctness or adoption. Canon-writing must use existing materialization/provenance authority and be idempotent under retry.

Project only current relevant provenance and nearby lineage, never the full history tree.

## 7. Discovery / Unknown Preservation

`UNKNOWN` is a valid state.

Player map knowledge must be separable from world geography. Reports may be incomplete or wrong. Observations can update knowledge without forcing all hidden detail to materialize. New concrete detail enters Canon only through the authorized deterministic materialization pipeline.

Project only the current map slice, known routes, relevant reports and uncertainty. Never inject undiscovered seeds or force every unknown to contain reward/plot significance.

## 8. Social Friction

Freedom should come from multiple plausible routes through constraints rather than universal access.

Access decisions may depend on location, schedule, relationship, reputation, organization membership/office, introduction/sponsor, debt/favor, legal/ritual permission, price/resources and alternative routes.

Return structured reasons for denial/permission and legal alternate affordances where appropriate.

Do not assume `select NPC = guaranteed conversation`, fame = universal access, or binary locked/unlocked design when social routes exist.

## 9. World Memory / Scars

Do not preserve long history by injecting old transcripts. Derive compact current consequences from committed events.

A scar/legacy may reference causal event IDs, affected entities, type (physical/legal/economic/demographic/social/ritual/reputational/personal), start time, decay/transformation, observable effects, knowledge/rememberers and superseding repair/reform.

The Event Log remains causal evidence; scars are current projection-friendly consequences rather than a duplicate history authority.

Only currently relevant scars enter context. `event inactive` must not mean `all consequences erased`.

## 10. Belonging / Personal Anchors

Represent the substrate of belonging without inventing a universal emotional score:

- home/residence anchors;
- visit/use frequency and recency;
- shared-history event references;
- familiarity with people/places/routes/services;
- provenance-bearing possessions/mementos;
- local recognition/reputation;
- recurring routines;
- losses and changed familiar places;
- player-created local legacy.

Project only scene-relevant personal anchors. Familiarity must not imply love, destiny, romance or objective world importance.

## Suggested implementation order

When foundations already exist:

### Workstream A — cheap, high-value substrate
1. Embodiment.
2. Everyday World.
3. Social Friction.
4. Discovery / Unknown Preservation.

### Workstream B — local differentiation
5. Material Culture.
6. Culture / Ritual Social Grammar.

### Workstream C — epistemic and historical depth
7. Information Ecology hardening.
8. World Scars / Legacy.

### Workstream D — personal historical ownership
9. Belonging / Personal Anchors.
10. Player-created History / Creation Lineage.

Do not build a generalized AI cognition platform when deterministic rules/state/query logic solves the current capability.

## Model-use policy

Default to:

`rule / state machine / relational query / event queue / deterministic generator / cached template → small model if needed → strong LLM only for genuinely semantic or narrative work`

Examples:

- shop hours: rule;
- recovery: mechanic;
- access: graph/rule;
- information propagation: event/relationship/institution rule;
- material variants: constrained generation/materialization;
- cultural ambiguity: rules + actor context, optional model when ambiguity matters;
- final prose: LLM.

Persistent does not mean continuously thinking.

## SillyTavern compatibility

For SillyTavern-compatible packages, keep character cards and World Info as presentation/static-public background, not mutable state authority.

A bridge/runtime may provide compact lived-world facets before generation. Example logical facets include scene life, relevant body state, visible material culture, active norms, permitted knowledge, discovery state, social access, current scars, personal anchors and relevant creation lineage.

Reuse the project’s packet/schema names rather than forcing these examples.

When the external runtime is unavailable, degrade honestly instead of pretending static lore guarantees exact offscreen simulation, epistemic routing, body state, scars or player-created legacy.

## Mandatory context-invariance tests

A lived-world implementation is incomplete until context growth is proven bounded.

### World-scale invariance

Run the same current scene against a baseline world and against worlds with substantially more offscreen actors, objects, history/scars and cultural records. Current-scene context must not grow linearly with offscreen data.

### History-length invariance

Compare the same place after short and very long histories. Only current consequences/scars/anchors should project, not an ever-growing historical summary.

### Catalog invariance

Populate a large material catalog; enter one shop; only visible/relevant items or variants should project.

### Epistemic firewall

Store a true fact with no legitimate evidence path to an actor. Retrieval must not leak it.

### Culture relevance

Store many norms. Ordinary scenes should load/evaluate only relevant norms.

### Body sparsity

Healthy state should not create recurring body prose. Add a meaningful condition and verify only relevant effects appear.

### Social-friction causality

Fail access for a legitimate reason, satisfy an alternate route and verify the result changes causally.

### Unknown preservation

Ask about undiscovered detail; preserve uncertainty. Materialize later through the authorized pipeline and verify stable identity across reload.

### Scar persistence

End an active event, advance time and verify current consequences remain when warranted. Repair/supersede the scar and verify the transition.

### Personal-anchor revisit

Return after a long absence and recover sparse shared history without full transcript injection.

### Creation lineage

Create, adopt, derive, advance time and reload. Verify stable provenance without automatic fame or full-history prompt injection.

## Idempotency requirements

Retries/save-reload must not duplicate:

- creation commits;
- scar consequences;
- the same familiarity event reference;
- discovery/materialization identity;
- access costs/favor consumption;
- body-condition events unless explicit stacking is legal.

Use existing event IDs, deterministic coordinates and provenance conventions.

## Hard anti-patterns

Reject:

- one persistent LLM agent per NPC/place merely to make the world feel alive;
- full catalogs/culture bibles/relationship graphs in prompts;
- unbounded rolling summaries;
- Memory = Truth;
- embedding retrieval bypassing authority or knowledge rights;
- mutable state owned by World Info;
- automatic plot significance for ordinary life/discovery;
- player-created content automatically becoming famous/powerful;
- belonging reduced to one affection-like scalar;
- solving context pressure by raising the global token budget.

## Final quality criterion

A mature sandbox should support a scene in which a player returns after years to a familiar ordinary place and encounters persistent identity, legitimate recognition, changed ownership, local economic/cultural conditions, body relevance, historical scars and shared personal history — while none of the world’s thousands of irrelevant actors, objects, norms, events or memories enter the prompt.

**Make more of the world exist outside the prompt, not more of the prompt describe the world.**