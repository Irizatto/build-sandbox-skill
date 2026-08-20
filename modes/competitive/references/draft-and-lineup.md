# Draft and lineup mechanics

## Ruleset fields

Record competition, season, stage, match format, version, eligible pool, roster eligibility, sides, side selection, phase graph, action counts, timing, uniqueness, role assignment, swaps, substitutions, series carry-over, remakes, penalties, and administrative overrides.

## Phase graph

Each phase needs a unique ID, acting participant or simultaneous group, action type, count, visibility, legal target filter, preconditions, commit behavior, next phase, and timeout policy. Every transition target must exist or be a declared terminal state.

## Legality

Validate at least:

- participant is eligible to act;
- phase and action type match;
- target belongs to the current eligible pool;
- target is not already unavailable under the ruleset;
- action count and timing are valid;
- final lineup satisfies size and role constraints;
- swaps and substitutions meet deadlines and permissions;
- series-level restrictions use prior committed games;
- an administrative override records authority and reason.

Never let an advisor recommendation mutate draft state. Only committed legal actions create events.

## Persistence

Store ruleset ID, phase ID, action index, actor, target, timestamp, seed where relevant, prior-state hash, resulting-state hash, and ruling metadata. Reload from committed events and compare the state hash.

