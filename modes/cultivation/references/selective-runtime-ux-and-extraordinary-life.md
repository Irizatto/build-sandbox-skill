# Selective Runtime UX and Extraordinary-Life Guidance

Use this reference when a mature cultivation sandbox is already playable, but external-card research exposes possible state, context, memory, institution, cultivation-life, or diegetic-UX improvements.

This reference is deliberately **selective**. A cleaner architecture is not enough reason to change a mature project.

Core sequence:

`REFERENCE PATTERN → REPRODUCIBLE GAP → EXISTING OWNER → SMALLEST DELTA → TEST → KEEP/REVERT`

If no reproducible player-facing, correctness, privacy, save/reload, retrieval, or deterministic failure exists, prefer `NO_CHANGE_NEEDED`, `SKILL_ONLY`, `DEFER`, or `TIER_C_ONLY`.

## 1. Architecture gap is not implementation authorization

Do not add a new state patch layer, context router, Chronicle compiler, actor database, event processor, external service, or authority owner merely because a public card or future engine uses one.

Implementation requires a real failure in at least one of:

- player experience;
- state correctness;
- knowledge/privacy boundaries;
- save/reload;
- context/retrieval;
- deterministic replay;
- current SillyTavern playability.

Use:

`ACTUAL FAILURE → EXISTING OWNER CANNOT CLEANLY SOLVE IT → SMALLEST DELTA → PLAYER/CORRECTNESS RETURN → TEST`

A mature system is allowed to conclude that an external pattern is good but already covered.

## 2. Delivery tier must stay explicit

Classify every candidate and every claimed implementation:

- `TIER_A_CANONICAL_ST` — current canonical SillyTavern card/World Info/package behavior;
- `TIER_B_OPTIONAL_ST` — optional Regex/STscript/Quick Reply/UI enhancement; Tier A works without it;
- `TIER_C_VALIDATION_OR_FUTURE_RUNTIME` — harness, deterministic prototype, validator, simulator, or future engine work;
- `CONTENT_ONLY` — selective canon/content expression using existing owners;
- `SKILL_ONLY` — reusable lesson, no project change;
- `NO_PROJECT_CHANGE` — useful reference evidence but no justified delta.

Tier C can validate a design. Tier C does not prove that the current player-facing SillyTavern package already supports the feature.

## 3. Incremental state semantics

For mutable durable state, omission from narration or a partial update must not imply deletion.

Useful semantic operations include:

- `RETAIN` — leave a durable fact unchanged;
- `UPDATE/SET` — replace an owned value explicitly;
- `ADD/REMOVE` — modify a collection explicitly;
- `INCREMENT/DECREMENT` — bounded numeric change where the schema permits it;
- `DELETE` — explicit removal when deletion is valid;
- `PURGE` — remove invalid/transient data under an authorized cleanup rule;
- `ROUTE/MOVE` — send a fact/change to the correct owner rather than mutating the wrong record.

A robust patch record may include:

```text
entity_id
field/path
operation
precondition/version
new_value
cause_event_id
provenance
```

Required properties where applicable:

- idempotent retry;
- duplicate protection;
- schema validity;
- stable IDs;
- no deletion by omission;
- save/reload equivalence;
- wrong-owner changes rejected or routed.

Do not create a separate patch engine if the current state owner already provides these semantics.

## 4. Active actor → offscreen actor

Leaving a scene should lower scene resolution, not erase the person.

Transient scene data may disappear:

- pose;
- current animation/presentation;
- scene-local action;
- temporary rendering state.

Durable data persists or updates through the existing actor/state owner:

- actor ID;
- injuries/conditions;
- inventory/property;
- location;
- goals;
- obligations;
- relationships;
- knowledge/beliefs;
- offscreen intention where the project models it.

Test return after time progression. Do not create a second actor database merely to model LOD.

## 5. Chronicle and summaries are derived views

Event History remains authority.

A Chronicle may derive readable segments such as:

```text
ACTION → REACTION → RESULT
```

with fields like:

```text
segment_id
time_range
location_ids
actor_ids
event_ids
category
significance
summary
open_threads
knowledge_scope
```

The Chronicle must not invent facts, silently become a second truth store, or overwrite authoritative events.

Removing a Chronicle view should change no Canon.

Prefer selective event query/rendering over building a compiler when that already solves the player-facing history problem.

## 6. Reveal lifecycle

Repeated exposition is both a continuity and context problem.

Where useful, distinguish:

```text
UNKNOWN
FIRST_REVEAL
KNOWN
RECALL_WHEN_RELEVANT
```

Do not re-explain the same location, institution, realm rule, or public fact every visit merely because the current response mentions it again.

Reminder remains valid when:

- the player asks;
- long absence makes recall useful;
- memory is uncertain;
- current decisions require the rule;
- the character learned only a partial version earlier.

Reuse existing knowledge/memory owners. Do not create a separate exposition tracker if current state can express the lifecycle.

## 7. State-gated context eligibility

Prefer:

`AUTHORITATIVE STATE + PLAYER KNOWLEDGE + SCENE → ELIGIBILITY → SELECTIVE FACETS/WORLD INFO → MODEL`

over raw keyword hit as the only gate.

Useful eligibility dimensions include:

- location;
- active actor IDs;
- organization/membership;
- identity/role;
- player knowledge;
- active/relevant event;
- committed world phase;
- optional experience profile.

Tune the existing retrieval owner first. A new router is a last resort.

Implementation needs measured evidence such as distant actors loading in unrelated scenes, private facts loading without eligibility, region changes failing to change context, generic-key collisions, or inactive content growing active prompt size.

## 8. Context evidence must state fidelity

Prefer actual assembled SillyTavern prompt / World Info activation inspection.

If measurements come from a custom projection, simulator, synthetic tokenizer, or external harness, record:

```text
MEASUREMENT_METHOD
FIDELITY_TO_REAL_ST
KNOWN_DIFFERENCES
WHAT_THE_NUMBER_CAN_PROVE
WHAT_IT_CANNOT_PROVE
```

Do not label simulator-only values as exact SillyTavern prompt cost.

Before/after comparisons should keep identical user input, character, World Info configuration, recursion/depth, retrieval settings, scene state, and tokenizer/method.

For large latent families, run 5x/10x inactive-content stress. The same active scene should remain approximately flat.

## 9. Functional institutions: belief must become procedure

A strong institution can be understood by using it.

Use:

`BELIEF → FACILITY → PROCEDURE → WORK → PERMISSION → COST → CONSEQUENCE`

Ask:

- what did the institution build because of its values?
- what does it teach/produce/protect?
- what does an ordinary member actually do?
- what can a visitor/member request or use?
- what requires permission?
- what can be refused?
- what records the interaction?

Possible affordances include request access, use/borrow facility, seek teaching, commission service, perform duty, petition/apply, or trade.

Each implemented affordance should have authority, eligibility, cost, time, result, record, and refusal/failure behavior where relevant.

Do not assume every sect uses contribution points or the same access economy.

## 10. Structural contradictions should come from the world

Plot pressure is stronger when it grows from real structure rather than faction labels.

Audit:

```text
RESOURCE OWNER
RESOURCE USER
REGULATOR
PROTECTOR
DEPENDENT POPULATION
EXEMPTION
TAX/TRIBUTE
TEACHING RIGHT
TRANSPORT
SUCCESSION
BOTTLENECK
CURRENT PRESSURE
```

Prefer a few player-visible consequences over a universal conflict engine.

## 11. Cultivation ecological physics

Do not force one cosmology.

Ask whether cultivation activity leaves material/ecological consequences in this setting.

Useful causal form:

`CULTIVATION ACTIVITY → RESOURCE/ECOLOGY CONSEQUENCE → PRODUCTION/LIVELIHOOD → ECONOMY/ORGANIZATION → POLITICS/MIGRATION → FUTURE CULTIVATION CONDITIONS`

First use existing metaphysical rules. Do not invent a new cosmic law or global ecology meter merely to fill this pattern.

A pilot should connect to at least one real region/resource loop and persist through time if the underlying Canon supports persistence.

## 12. Extraordinary life outside battle

Realm/path/body identity should remain visible in ordinary life.

Audit how cultivation changes assumptions about:

- sleep;
- food;
- disease;
- temperature/weather;
- light;
- storage/carrying;
- travel/falling;
- communication;
- labor;
- injury/healing/medicine;
- architecture;
- privacy;
- social treatment.

Core test:

> If the cultivator were replaced with a normal mortal, could the scene remain almost word-for-word identical?

If yes, cultivation may be under-expressed.

Do not solve this with unsupported “high realm ignores everything”. Use canon-supported differences and selective content before inventing runtime systems.

## 13. Capability exemplars

If the model repeatedly miscalibrates what realms/paths can accomplish, a very small set of canonical historical benchmarks may help.

Each exemplar should record:

```text
actor realm/path
conditions
achievement
duration
cost
recovery
historical evidence
```

Use only established Canon. Do not create a battle wiki or exhaustive power database.

## 14. Diegetic query surfaces

A world-native query interface is useful only when it answers a real player problem through a real source.

Possible examples:

- known travel/history journal;
- public organization registry;
- market information sheet;
- collected rumor book;
- player-known Chronicle view.

For each pilot define:

```text
in-world source
owner
access
freshness
query fields
knowledge scope
provenance
render form
delivery tier
```

Hard rule:

`DIEGETIC UI != OMNISCIENCE`

Do not expose NPC-only memory, secret identities, private plans, or facts the player has no valid information path to know.

If ordinary selective dialogue/query already solves the problem well, do not build a UI.

## 15. Decision trace without hidden reasoning

A decision trace may expose structured, player-entitled facts behind a validated result:

```text
ACCESS: DENIED
Known requirement: inner-disciple authorization
Your current status: outer disciple
Known alternate route: elder token / formal application
```

Never expose private chain-of-thought.

Decision traces are presentation. They do not become authority and cannot reveal hidden premises the player does not know.

## 16. Renderer / presentation boundary

Renderer may control rhythm, diction, description density, camera distance, sensory focus, title cards, dialogue ratio, or soft cliché lint.

Renderer may not control world truth, success, inventory, relationship truth, knowledge, cultivation state, or Canon.

Prefer soft lint:

`detect generic/clichéd wording → suggest concrete action/material/environment/voice`

over giant permanent banned-word lists.

Hero/title cards must not reveal unknown realm, secret identity, hidden goal, private relationship, or future fate.

## 17. Evidence must discriminate good from broken implementations

Do not count:

- `assert(true)`;
- self-certifying fixtures;
- `expected = implementation output`;
- mocks that bypass the real owner/retrieval path;
- self-grading generated transcripts;
- manual PASS text with no failure condition.

For high-risk deltas, mutation should cause the corresponding test to fail.

Examples:

- break RETAIN → state test fails;
- force distant World Info active → context test fails;
- copy private knowledge to an NPC → epistemic test fails;
- remove institution permission → institution test fails;
- expose hidden facts in a decision trace → UX test fails.

## 18. Final rule

The desired outcome is not more engines, flags, panels, or prompts.

The desired outcome is:

- fewer duplicate owners;
- durable state that does not disappear from omission;
- history that is selectively inspectable without becoming a second truth store;
- context gated by current state and knowledge rights;
- institutions that can actually be used;
- cultivation that changes ordinary life;
- world-native UX that never becomes omniscient;
- evidence that proves the actual product tier being claimed.

> **Audit ruthlessly. Change minimally. Reuse owners. Prove the delta.**
