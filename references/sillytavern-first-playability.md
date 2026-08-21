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
16. inactive-world scale stress proving context does not grow with irrelevant world size.

A capability classified `KEEP_EXISTING` may pass its test with zero implementation change. That is a successful result, not missing work.

The build is incomplete if it is architecturally elegant but harder to import, start, understand, continue playing, or keep within context than the previous working package.

## Release honesty

State explicitly which behaviors are:

- guaranteed by core/package structure;
- enhanced by optional STscript/Quick Replies;
- approximate through LLM/GM behavior;
- deferred to optional extension/runtime work.

Do not call approximate SillyTavern behavior a deterministic external-world simulation.

## Final criterion

A normal player should be able to import/open the package and experience a measurably more inhabited or choice-rich world **only where the baseline had a real gap**, without future custom software, routine manual state maintenance, duplicate authority, or a noticeable increase in ordinary assembled context.

**For an ST-first deliverable, more features are not success. More play per token is success.**