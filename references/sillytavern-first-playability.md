# SillyTavern-First Playability Contract

Use this reference when the requested deliverable is a SillyTavern character/world package that must be directly playable in SillyTavern, even if the broader architecture could later support a custom runtime.

## Priority order

For this target, optimize in this order:

`SillyTavern playability > chat/save continuity > bounded context > causal consistency > feature richness > future architecture purity`

Do not turn a working SillyTavern package into a prototype for a future client.

## Mature-baseline / delta-only rule

When the package already has a mature persistent-world baseline, do **not** implement every listed lived-world capability merely because the reference mentions it.

First freeze and measure the working baseline. Classify each candidate capability as:

- `KEEP_EXISTING` — the current package already produces the desired play experience;
- `TUNE_EXISTING` — a small targeted change has clear player-facing value;
- `IMPLEMENT_GAP` — a real playability gap exists;
- `DEFER_NO_PROVEN_RETURN` — possible feature, but current value does not justify complexity;
- `BLOCKED` — requires an explicit product decision or forbidden dependency.

Only `TUNE_EXISTING` and `IMPLEMENT_GAP` authorize implementation work. `KEEP_EXISTING` must not receive a second state owner, extra World Info, scripts, schemas or prompt sections just for completeness.

Every selected change should be explainable as:

`baseline weakness → smallest safe change → player-visible improvement → measured context/state cost`

If that chain is unclear, do not keep the change.

## Architecture gap is not implementation authorization

For a mature ST-first package, a cleaner architecture is not itself a gap.

Before adding a new state layer, router, compiler, database, actor store, event processor, external helper, or authority owner, require a reproducible failure in at least one of:

- player experience;
- state correctness;
- knowledge/privacy boundaries;
- save/reload;
- context/retrieval;
- deterministic behavior the package explicitly promises;
- current SillyTavern playability.

Use:

`ACTUAL FAILURE → EXISTING OWNER CANNOT CLEANLY SOLVE IT → SMALLEST DELTA → PLAYER/CORRECTNESS RETURN → TEST`

If that chain cannot be demonstrated, prefer `NO_CHANGE_NEEDED`, `DEFER`, or a clearly labeled Tier C prototype.

External-card research may broaden the option space. It does not authorize implementation by itself.

## Product / harness evidence boundary

A SillyTavern-first project may contain an external JS/Python harness, schemas, deterministic simulators or validators **without making those tools part of the playable product**. This is valid when the boundary is explicit.

Classify evidence separately:

- **Tier A product evidence** — the authoritative Character Card / GM spec / World Info / registries actually imported or used by SillyTavern, plus player-facing regression evidence.
- **Tier B enhancement evidence** — optional STscript / Quick Replies / selective World Info or similar artifacts that a player may enable, with extension-off fallback.
- **Tier C validation-harness evidence** — external scripts, schemas, replay/simulation prototypes, validators and test fixtures used to check invariants or future-runtime ideas.

For selective audits it is useful to classify candidate outcomes more precisely as:

```text
TIER_A_CANONICAL_ST
TIER_B_OPTIONAL_ST
TIER_C_VALIDATION_OR_FUTURE_RUNTIME
CONTENT_ONLY
SKILL_ONLY
NO_PROJECT_CHANGE
```

A Tier C harness may prove schema validity, stable IDs, deterministic materialization, idempotency, migration behavior or other properties it genuinely exercises. It does **not** by itself prove that SillyTavern players experience those behaviors.

Do not reject a healthy Tier A package merely because a removable Tier C harness exists outside its manifest. Conversely, do not call a feature implemented in the playable package merely because a harness contains a class, schema or passing unit test for it.

### Acceptance-evidence rule

A test counts as acceptance evidence only when its assertion can fail because the behavior under test is wrong.

Reject as behavioral proof:

- `assert(true)` / unconditional PASS markers;
- tests that only assert a fixture value they just assigned;
- mocks that bypass the authority/retrieval/state transition being claimed;
- a synthetic projection that is not linked to the actual ST package while being presented as measured ST context;
- self-grading generated transcripts;
- report prose that has no inspectable artifact/test behind it.

Such placeholders may remain during development, but they must be labeled `SCAFFOLD / NOT VERIFIED` and excluded from PASS counts.

For player-facing claims such as mundane 20-turn play, recurring-NPC continuity, anti-protagonist behavior, knowledge firewall, long absence, social access or long-session stability, require either a real ST-facing scenario test or a faithful package-level simulation that exercises the same prompt/lore/state path. Human playtest remains a separate higher evidence tier.

For high-risk deltas, prefer mutation evidence: deliberately break the claimed behavior and require the corresponding test to fail.

### Baseline integrity evidence

Before treating an existing ST package as the baseline, verify as available:

- canonical card / GM / World Info / registry files still exist at expected paths;
- manifest/package-integrity hashes still match when the package uses them;
- import instructions still identify the playable artifacts;
- optional add-on directories are outside the authoritative manifest unless intentionally promoted;
- disabling/removing optional add-ons leaves Tier A playable;
- no validation harness silently replaced the canonical package.

## Delivery tiers

### Tier A — required core-playable package

The package must remain playable using ordinary SillyTavern prompt construction, Character Card and World Info behavior. Do not require a separate World Engine executable, external database, custom cloud backend or unknown third-party extension for the base experience.

When exact simulation is impossible in core SillyTavern, degrade honestly through bounded GM rules, selective lore and explicit uncertainty rather than inventing fake deterministic state.

Tier A decides whether the build passes.

### Tier B — optional built-in automation

When useful and compatible, SillyTavern's own STscript / Quick Replies / chat-local variables / World Info Automation IDs / timed effects / outlets / inclusion groups may provide deterministic low-token enhancements.

Use Tier B for small recoverable state and housekeeping, for example:

- current day/daypart or compact scene flags;
- a bounded set of player-known facts;
- a bounded set of access permissions/favors;
- personal anchor IDs;
- initialization and debugging helpers.

Do not use it as a second giant world database, a one-agent-per-NPC simulator, or a mandatory manual-maintenance layer. The package must degrade gracefully if the enhancement is disabled.

### Tier C — optional future extensions/runtime

UI extensions, Server Plugins, external databases, runtime bridges and custom clients may later improve exactness. Do not make them mandatory unless the user explicitly requests that deployment target or the existing project already declares them as required.

## Incremental state and derived-view discipline

When the package or an attached runtime owns mutable durable state, omission from current narration or a partial update must not imply deletion.

Useful semantics include:

- `RETAIN` — unchanged durable fact remains;
- `UPDATE/SET` — explicit replacement;
- `ADD/REMOVE` — explicit collection change;
- `INCREMENT/DECREMENT` — explicit bounded numeric change when valid;
- `DELETE` — explicit valid removal;
- `PURGE` — authorized cleanup of invalid/transient data;
- `ROUTE/MOVE` — send a change to the correct owner instead of mutating the wrong record.

Prefer existing owner semantics. Do not add a separate patch engine merely to obtain these names.

Where applicable, test idempotent retry, duplicate protection, stable IDs, wrong-owner rejection/routing, and save/reload equivalence.

Leaving a scene should lower presentation resolution rather than erase a persistent actor: scene pose/action may disappear while durable identity, condition, inventory/property, location, goals, obligations, relationships and knowledge remain with the current actor/state owner.

Chronicles, summaries and memory views are derived projections of authoritative Event History. They may organize `ACTION → REACTION → RESULT` and expose selected source event IDs, time ranges, actors, locations, open threads and knowledge scope, but they must not invent facts or become a second Canon owner. Removing a derived view must change no world truth.

## Reveal lifecycle

Repeated exposition is both a playability and context problem.

When the existing knowledge/memory owner can support it, distinguish:

```text
UNKNOWN
FIRST_REVEAL
KNOWN
RECALL_WHEN_RELEVANT
```

Do not re-explain the same basic location, organization rule, public fact, or domain mechanic on every revisit.

Recall remains appropriate when the player asks, after long absence, when memory is uncertain, when the decision requires the rule, or when the player only learned a partial version earlier.

Do not create a second exposition tracker if the current knowledge/memory state can express the lifecycle.

## SillyTavern World Info rules

Use World Info for durable/public/static or slow-changing facets and compact projection, not as a shadow mutable-state database.

Prefer:

- narrow specific keys;
- optional filters;
- inclusion groups for competing facets;
- deterministic priority where appropriate;
- concise standalone entries;
- outlets when placement matters;
- character/chat-specific binding when it reduces irrelevant activation;
- timed effects only when message-count semantics truly fit the state.

Reject or mutation-test:

- generic role/title entity keys;
- empty keys;
- single-character CJK keys without proof;
- ambiguous short aliases;
- mega-entries;
- uncontrolled recursion;
- broad always-on lived-world sections;
- probability-triggered authoritative state changes.

Vector/embedding retrieval is optional recall support. It must not own secrets, alive/dead state, current location, ownership, access permission, relationship truth or other critical Canon.

When raw keyword matching is insufficient, prefer eligibility from current state and player knowledge before selective facets are injected:

`AUTHORITATIVE STATE + PLAYER KNOWLEDGE + SCENE → ELIGIBILITY → SELECTIVE FACETS / WORLD INFO → MODEL`

Useful gates include location, active actor IDs, organization/membership, identity/role, player knowledge, active/relevant event, and committed world phase.

Tune the current retrieval owner first. A new router is justified only by measured leakage or retrieval failure such as distant actors loading in unrelated scenes, private facts loading without eligibility, region changes failing to change context, generic-key collisions, or inactive content growing active prompt size.

## Token-neutrality rule

Do not solve lived-world depth by increasing the global World Info/context budget. Measure the actual assembled prompt/context against the working baseline.

For mature packages, prefer **approximately token-neutral migration** over additive prompt growth. A useful default guardrail is:

- always-on/core prompt delta: target `<= +100 tokens`, preferably `<= 0`;
- ordinary inactive scene: increase no more than the smaller of `+5%` or `+200 tokens`;
- ordinary social scene: increase no more than the smaller of `+7%` or `+350 tokens`;
- dense local cultural/history scene: increase no more than the smaller of `+10%` or `+600 tokens`;
- multiplying inactive actors/catalog/history by 10x should not make the same scene grow by more than the smaller of `+5%` or `+200 tokens`.

These are default engineering guardrails, not universal quotas. A project's stricter measured baseline wins.

A capability irrelevant to the current scene should contribute zero or near-zero prompt content. When a new selective facet adds value, remove or compact redundant old prose where safe instead of stacking both.

For a claim of measured ST context, prefer the actual assembled ST prompt/context or an explicitly documented faithful assembler using the real card/World Info activation rules.

If a custom projection, simulator, synthetic tokenizer or external harness is used, report:

```text
MEASUREMENT_METHOD
FIDELITY_TO_REAL_ST
KNOWN_DIFFERENCES
WHAT_THE_NUMBER_CAN_PROVE
WHAT_IT_CANNOT_PROVE
```

A synthetic projection is useful engineering evidence but must not be labeled exact ST context unless equivalence is demonstrated.

Before/after comparisons should keep the same user input, character, World Info configuration, recursion/depth, retrieval settings, scene state and tokenizer/method.

## Diegetic query and decision-trace boundary

A world-native query surface is useful only when it answers a real player problem through a real authorized source.

Examples include a player-known travel/history journal, public organization registry, market-information sheet, collected rumor book, or player-filtered Chronicle view.

For a pilot define:

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

Do not expose NPC-only memory, secret identity, private plans, hidden goals, or facts with no valid player information path.

A structured decision trace may explain a validated result using player-entitled facts, for example known access requirement, current known status and known alternate route. It must never expose hidden chain-of-thought or unknown premises.

Presentation remains presentation. A title card, hero card, journal, decision trace, memory view or renderer profile may not mutate or outrank world truth.

## Lived-world capability mapping for ST

When applying `lived-world-token-safe-experience.md`, **audit all ten but implement only measured gaps**:

1. **Everyday World** — recurring mundane anchors, local routine/daypart facets and ordinary actions; not a citywide always-on schedule.
2. **Embodiment** — small qualitative conditions; normal state omitted; optional compact chat-local state.
3. **Material Culture** — reusable regional/object-family facets; unique persistent instances only when history matters.
4. **Culture/Ritual** — operational social-norm entries triggered only by relevant action/place/status.
5. **Information Ecology** — retrieval separation and compact knowledge labels for important facts/actors; do not expose secret truth merely to tell the model it is secret when avoidable.
6. **Player-created History** — bounded validated creations with stable identity/provenance and a small meaningful adoption lineage; do not claim exact unlimited diffusion simulation.
7. **Discovery / Unknown Preservation** — UNKNOWN is valid; hidden seeds do not become player-facing lore simply because asked about.
8. **Social Friction** — compact access/obligation facets for actors/organizations where access matters; offer plausible alternate routes when appropriate.
9. **World Scars** — current consequence facets tied to event provenance; do not inject full old transcripts.
10. **Belonging** — sparse home/familiar-place/contact/shared-history anchors; no universal belonging scalar.

If the existing package already passes the relevant player-facing test for one of these capabilities, record `KEEP_EXISTING` and do not enlarge the package for that item.

## Playability-first implementation order

For selected gaps only, prefer high-return work first:

A. ordinary life / anti-forced-plot / recurring-place continuity;

B. knowledge leakage / unknown preservation / social access;

C. embodiment / local material and cultural differentiation;

D. world scars / personal revisit / player-created history.

Run a player-facing and context gate after each selected change. If a change does not produce clear player-visible value, revert it rather than keeping it because implementation work was already spent.

## Mandatory ST-realistic tests

At minimum verify, as applicable to the selected gaps and existing baseline:

1. fresh chat/opening regression;
2. 20-turn mundane play without forced major plot;
3. recurring place/person continuity;
4. body-state sparsity;
5. local custom reaction without culture dump;
6. secret/knowledge firewall;
7. social-access denial plus legitimate alternate route;
8. unknown preservation and stable later materialization;
9. historical-scar revisit without full-history injection;
10. long-absence personal-anchor revisit;
11. modest player-created object/practice persistence without fame inflation when creation is in scope;
12. World Info trigger collisions and recursive activation;
13. chat reload/branch safety for any STscript variables;
14. extension-off fallback if Tier B artifacts exist;
15. baseline-vs-final assembled-context comparison;
16. inactive-world scale stress proving context does not grow with irrelevant world size;
17. partial-state omission does not delete durable facts when mutable state is in scope;
18. Chronicle/memory view contains only source-backed, player-entitled history and can be removed without changing Canon;
19. reveal lifecycle reduces repeated exposition without suppressing necessary recall;
20. diegetic queries/decision traces cannot reveal private unknown truth.

A capability classified `KEEP_EXISTING` may pass its test with zero implementation change. That is a successful result, not missing work.

The build is incomplete if it is architecturally elegant but harder to import, start, understand, continue playing, or keep within context than the previous working package.

## Release honesty

State explicitly which behaviors are:

- guaranteed by core/package structure;
- enhanced by optional STscript/Quick Replies;
- approximate through LLM/GM behavior;
- supported only by Tier C validation/future-runtime prototypes;
- content-only projections using existing owners;
- Skill-only lessons with no project delta;
- deferred to optional extension/runtime work.

Do not call approximate SillyTavern behavior a deterministic external-world simulation. Do not upgrade placeholder tests into evidence merely because the test command exits green.

## Final criterion

A normal player should be able to import/open the package and experience a measurably more inhabited or choice-rich world **only where the baseline had a real gap**, without future custom software, routine manual state maintenance, duplicate authority, or a noticeable increase in ordinary assembled context.

**For an ST-first deliverable, more features are not success. More play per token is success.**