# Competitive Anti-Patterns and Hard DON’Ts

These are domain-specific build constraints. Generic retrieval, state, persistence, actor, and context anti-patterns live in `build-persistent-sandbox/references/anti-patterns-and-donts.md` and still apply.

## Rules and legality

- **Do not infer the current ruleset from memory or from a different event.** Pin competition, season, stage, patch, match format, eligibility, side-selection policy, series carry-over, and source date.
- **Do not encode recommendations as legality.** A weak choice may be legal; a strong choice may be illegal.
- **Do not silently repair an illegal or inconvenient result through narration.** The authoritative ruleset and committed state win.
- **Do not use one title's draft, substitution, roster, overtime, remake, or side-selection rules as a generic template without explicit parameterization.**
- **Do not let stale rules or patch data remain active after a version transition.**

## Matchups and metagame

- **Do not write universal `A counters B` truth without context.** Matchups depend on version, role/position, map, side, phase, composition, proficiency, strategy, sample quality, and freshness.
- **Do not reduce composition effects to pairwise edges when the interaction is genuinely multi-entity.** Use hyperedges/packages where needed.
- **Do not convert public win rates into eternal ability ratings or deterministic outcomes.**
- **Do not mix observed statistics, expert judgment, model estimates, participant beliefs, and narrative commentary without provenance.**
- **Do not expose private preparation, scrim knowledge, hidden selections, or simulation parameters to a public/player view.**

## Rosters, actors, and career simulation

- **Do not make the player's career the reason every roster move happens.** Teams and competitors continue to practice, scout, sign, bench, promote, retire, and adapt offscreen.
- **Do not remove or degrade an established competitor merely to create space for the player.**
- **Do not use fame as omniscience or automatic access.** A famous competitor does not automatically know, notice, mentor, rival, or befriend an unknown player.
- **Do not collapse professional respect, tactical trust, personal closeness, rivalry, pressure, and public reputation into one relationship score.**
- **Do not force every slump, benching, missed qualification, roster failure, or defeat into a redemption arc.** Failure is a valid persistent outcome.

## Retrieval and naming

- **Do not use generic positions, roles, titles, or team-category words as actor-specific World Info triggers.** Examples: `support`, `coach`, `captain`, `manager`, `pitcher`, `catcher`, `starter`, `rookie` without qualification.
- **Do not rely on loose English handle or short team-name boundary matching.** Test aliases, case variants, substrings, punctuation, romanization, and collisions explicitly.
- **Do not load the entire roster, league, historical season, champion/player database, or matchup graph into an ordinary scene.**
- **Do not let a historical mention of a player/team imply current roster membership, availability, health, or presence.**

## Simulation and commentary

- **Do not make commentary authoritative state.** Broadcast, fan discussion, media narratives, and analyst takes are noisy views.
- **Do not give the player fog-of-war truth, hidden opponent intent, private comms, unrevealed preparation, or future results.**
- **Do not make pressure a flat scalar debuff shared by all actors.** Pressure may affect sleep, attention, hesitation, risk preference, communication, or execution differently.
- **Do not make every competition scene a highlight reel.** Routine practice, preparation, travel, recovery, admin work, and quiet periods are legitimate career gameplay.

## Validation

Test at least:

1. version/ruleset mismatch;
2. alias and short-handle collision;
3. generic role-word retrieval;
4. illegal action that narration must not override;
5. stale patch/matchup evidence;
6. hidden-information leakage;
7. save/reload during an incomplete phase;
8. a season where the player is benched or irrelevant to major events;
9. ordinary daily-life context with zero competitive database dump;
10. deliberately corrupted ruleset and retrieval fixtures.

A competitive sandbox is not release-ready if the rules are correct only when the narrator happens to remember them correctly.
