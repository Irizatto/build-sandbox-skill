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
- actual human long-session playtest.

Do not report automated/agent tests as human validation. Use Alpha or Release Candidate while important experiential gates remain unresolved.

## Final question

Every periodic gameplay review should end by answering:

> If only one problem could be fixed next, which change would most clearly make the player feel that the world is more alive, more coherent, or more worth returning to?
