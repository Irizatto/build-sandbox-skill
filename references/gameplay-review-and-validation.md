# Gameplay Review and Long-Session Validation

A persistent sandbox is not complete because the schemas parse and the simulator runs. Review whether the player experience actually improved.

## Review the experience chain

For any important mechanic or feature, inspect:

`player intent → legal/possible action → authoritative resolution → world delta → actor/org response → narrative projection → future consequence`

A feature that exists only as prose or a prompt promise is not equivalent to gameplay support.

## Time-scale review

For minute, day, week, season, year and decade scales, ask:
- What does the player do?
- What are they waiting for or trying to learn?
- What can they risk or lose?
- What choices are meaningfully different?
- What can they build or change?
- What proceeds without them?
- What makes them want another turn/session?

If a time scale contains only narration but no meaningful decision or consequence, note the gap.

## Player fantasy / affordance audit

Classify requested or expected behaviors as:
- SUPPORTED;
- PARTIALLY SUPPORTED;
- LLM-FAKED;
- NOT SUPPORTED.

Do not count “the model can describe it” as executable support.

## Mature integration / RC-closure gate

When a sandbox already has strong state, event history, career/domain mechanics, social/living-world systems and retrieval, stop asking only “what feature is missing?” and audit whether the existing systems form one causal world.

Prefer:

`existing authoritative event → eligible cross-system consumers → bounded consequences → validated state changes → sparse player-visible projection`

over parallel subsystems that each maintain their own time, pressure, relationship, media, schedule or history.

Before adding a new event bus, state owner, presentation database, profiler or router, first identify the existing owner and a reproduced gap. Extend the existing owner when it can solve the problem cleanly.

### Budgeted event subscriptions

A mature world may need explicit event subscriptions so competition, training/work, recovery, media, streaming, social activity, travel and relationships can affect one another without creating an event explosion.

Use the logical flow:

`source event → eligible subscribers → consequence candidates → consequence budget → authority/privacy validation → idempotent commit`

A subscriber or equivalent consumer should declare, as applicable:

```text
subscriber_id
accepted_event_types
reads
writes
eligibility
priority
cooldown
consequence_class
max_output_events
knowledge_scope
authority_constraints
```

Do not require this exact schema if the project already has equivalent semantics.

Consequences should distinguish at least:
- required direct state changes;
- high-causal-relevance consequences;
- conditional secondary consequences;
- background consequences that may remain offscreen.

Default to a small consequence budget. A routine event should usually create zero or only a few salient cross-system consequences. A career-defining event may justify more, but it still requires eligibility, deduplication, cooldown and relevance. Never let one match, meeting, failure or social interaction automatically summon every media, relationship, recovery, sponsor and narrative subsystem.

Use idempotency keys derived from the source event plus consumer/consequence identity. Replay or reload must not duplicate the same consequence. Bound automatic causal-chain depth so `A → B → C → ...` cannot recurse indefinitely within one tick.

Privacy remains a hard gate. Private practice/scrim notes, therapeutic detail, secret strategy, unrevealed preparation or private relationship state must not become public merely because a downstream media/social subscriber exists.

Mutation-test this layer: remove the budget, remove deduplication, expose a private event to a public consumer, or allow unbounded recursion and require the corresponding test to fail.

## Player-visible product surfaces

A recurring failure mode in mature sandboxes is **system exists, player cannot feel it**. Contracts, schemas, reports and debug dictionaries are not player-facing implementation.

For important state that the player is entitled to inspect, provide a real product surface through the actual delivery target. In SillyTavern this may be a Character/GM response path, selective World Info packet, STscript/Quick Reply, Automation ID, outlet, or another verified package mechanism. In another client, use that product's native projection path.

Useful domain-adapted surfaces may include:
- today/current schedule;
- next match/event/obligation;
- practice or capability readiness;
- scouting/research brief;
- post-event review priorities;
- known standings, roster or travel information.

Each surface should define:

```text
source owner
trigger/query
knowledge scope
freshness
projection fields
render form
delivery tier
fallback
```

The surface is a **read-only projection** unless it explicitly submits a validated player action. It must not become a second truth store.

For SillyTavern-first work, a Python helper returning the correct dictionary is not enough. Exercise the actual Character/World Info/STscript/package path, or document a faithful package-level assembler/test and its limitations. A static Markdown mockup is design evidence, not proof that the player can invoke the surface in play.

Keep player and debug views separate. Player views should expose only player-entitled facts; raw hashes, RNG seeds, hidden relationship numbers, private confidence or GM-only state stay in debug evidence.

Test freshness: after the authoritative schedule, readiness, match result or review changes, the visible surface must update rather than serve stale cached data.

## Final context-assembly profiler

Do not stop at configured World Info budgets. Near RC, profile the **fully assembled current context** through the actual product path when possible, or through an explicitly faithful assembler.

Report the measurement method and, when not using the actual product prompt:

```text
MEASUREMENT_METHOD
FIDELITY_TO_REAL_PRODUCT
KNOWN_DIFFERENCES
WHAT_THE_NUMBER_PROVES
WHAT_IT_CANNOT_PROVE
```

Break the assembled context into relevant components, for example:

```text
core / always-on
GM or character card
current state
active actors
location
current domain mechanics
current event / match / series
relationships
history / scars
media
World Info
RAG / Data Bank
presentation packet
total
```

Where feasible also measure:
- duplicate tokens/content;
- irrelevant injected content;
- stale evidence;
- unauthorized/private hits;
- active actor count;
- World Info entries/chunks selected.

### 1x / 5x / 10x world-scale stress

Construct valid inactive fixtures at approximately baseline, 5x and 10x offscreen scale. Scale real searchable structures such as inactive actors, relationships, locations, event history, media records, archives or catalogs—not empty files that retrieval can never see.

Hold the current scene and query constant. Compare at least a quiet/ordinary scene and one dense domain scene. For career/competitive worlds also include a normal training/work scene and a live competition/match scene when relevant. For social/living worlds include a normal social scene.

The central acceptance property is:

`WORLD / REPOSITORY SIZE ↑↑ while SAME CURRENT SCENE CONTEXT ≈ FLAT`

Use the stricter project baseline when one exists. Otherwise inherit the token/context guards from `sillytavern-first-playability.md`, `lived-world-token-safe-experience.md` and `content-density-and-controlled-scale.md`.

Mutation-test the profiler/retrieval path by forcing inactive actors/history into context, bypassing knowledge eligibility, or disabling deduplication; the measured output must become detectably worse.

## System-visibility matrix

For mature integration work, explicitly audit whether important mechanics are perceptible without turning the game into a HUD.

For each important system record:

```text
EXISTS
TRIGGERED
PLAYER_VISIBLE
PLAYER_UNDERSTANDABLE
DECISION_RELEVANT
TOO_VISIBLE
```

A backend-only system may correctly be `PLAYER_VISIBLE = INDIRECT` if its consequences are legible through schedules, dialogue, restrictions, outcomes or diegetic surfaces. The goal is not to expose every internal number.

Classify common failures with tags such as:
- BORING;
- REPETITIVE;
- TOO_VERBOSE;
- TOO_FAST;
- TOO_SLOW;
- INVISIBLE_SYSTEM;
- FAKE_CHOICE;
- TOO_PLAYER_CENTRIC;
- NPC_FLAT;
- MEDIA_NOISE;
- LIFE_TOO_EMPTY;
- LIFE_TOO_BUSY;
- DOMAIN_LOOP_DISCONNECTED.

## Mandatory long-session suite

For living worlds, adapt and run:
1. **20-turn mundane life** — no major plot pursuit;
2. **50-turn recurring actor** — voice, memory, routine, relationship continuity;
3. **30-day normal simulation** — schedules, markets/org activity;
4. **1-year absence** — leave and return;
5. **5-year retreat/inactivity** — breakpoints, death, resources, offices, opportunities;
6. **30-year skip** — succession and generational history;
7. **100-year aggregate simulation** — causal history rather than random noise;
8. **relationship stress** — cooperation, failure, misunderstanding, conflict, repair, absence;
9. **anti-protagonist** — player ignores major content;
10. **weird actions** — reasonable unprepared actions outside expected loops;
11. **world-horizon/ecosystem travel** — early exit and return;
12. **actor bookmark/promotion** — ordinary actor becomes persistent without destiny inflation;
13. **organization lifecycle** — leadership/resource/founding/split/decline change.

For competitive career worlds, adapt the same ideas to seasons, rosters, travel, team life, benching, transfers, media, practice and offscreen competition.

### Competitive/career human gates

When a mature competitive or professional-career sandbox is approaching RC, add two concrete experiential gates when the domain supports them:

1. **One normal professional week / work cycle** — include schedule, preparation/training, one meaningful practice/scrim/simulation block where applicable, recovery or ordinary life, scouting/research, at least one competition/work event, aftermath/review, and quiet time. Do not force every subsystem into every day.
2. **One complete competitive series/event cycle** — for esports this may be a full BO3/BO5; for sports without that format, use an equivalent complete series/game-day/road-series cycle. Include pre-event preparation, legal competition flow, between-game/phase adaptation where relevant, post-event interview/media when in scope, and review feeding back into the next preparation cycle.

The key question is whether preparation, competition, aftermath and life feel causally connected to the player—not merely whether each backend subsystem fired.

Actual human play is a separate evidence tier. An AI-generated transcript, model self-play, package simulation or implementer-authored walkthrough must never be labeled `HUMAN PASS`. If no human has actually played the gate, report `HUMAN_GATE_PENDING` while still reporting automated/package-level results honestly.

## Short / medium / long experience

Report the likely experience at roughly:
- 3 hours — onboarding, freedom, early goals, constraints;
- 20 hours — repetition, cast depth, pacing, regional/system differentiation;
- 100 hours — unique save history, world evolution, actor/org continuity, context drift.

If these durations are not literally tested, label conclusions as extrapolation from proxies.

## Experience metrics

Use qualitative coding or telemetry for relevant metrics such as:
- agency;
- believability;
- attachment;
- curiosity;
- surprise;
- meaningful consequence;
- confusion;
- cognitive load;
- frustration;
- repetition;
- player magnetism;
- return intent.

Do not fabricate numeric precision when telemetry does not exist.

## Issue format

Every meaningful gameplay issue should include:
- ISSUE ID / TITLE / severity P0–P3;
- evidence;
- player-facing symptom;
- root cause;
- why it matters;
- proposed fix;
- owner subsystem/phase;
- implementation substrate;
- acceptance criteria;
- test;
- tradeoff/risk.

Classify recommendations as MUST FIX / SHOULD IMPROVE / EXPLORE / DEFER / DO NOT ADD.

## Adversarial retrieval and persistence validation

Re-run:
- common/generic retrieval keys;
- single-character CJK keys;
- generic-title collisions;
- ambiguous aliases;
- mega-entry and recursion avalanches;
- private-truth leakage;
- absent/dead actor historical mention;
- stale mutable lore;
- save/reload equivalence;
- deterministic replay;
- corrupted ID/reference/provenance fixtures;
- context-budget measurement of the fully assembled prompt.

## Release honesty

Distinguish:
- unit/schema validation;
- deterministic simulation;
- agent-driven scenario tests;
- faithful package/product-path tests;
- actual human long-session playtest.

Do not report automated/agent/model self-play tests as human validation. Use Alpha or Release Candidate while important experiential gates remain unresolved.

A mature RC-closure report should separately state, when relevant:
- event-subscription/bounded-consequence status;
- player-visible surface status;
- baseline/5x/10x context-profile status;
- package-level professional-week/series status;
- human professional-week/series status;
- known invisible or overexposed systems.

## Final question

Every periodic gameplay review should end by answering:

> If only one problem could be fixed next, which change would most clearly make the player feel that the world is more alive, more coherent, or more worth returning to?
