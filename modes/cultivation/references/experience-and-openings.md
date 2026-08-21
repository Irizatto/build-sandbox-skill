# Cultivation Experience, Openings, and Projection Patterns

Use this reference when improving how a cultivation sandbox **feels to play**: opening momentum, macro-era framing, offscreen-world projection, bounded player-action completion, and prompt/adjudication discipline.

These are **patterns, not mandatory subsystems**. Before adopting one, identify the concrete player/world problem it solves, check whether existing architecture already solves it, and estimate agency, context, authority, simulation, and pacing costs. `NO CHANGE` is valid.

## 1. Tianji / offscreen world slices

A Tianji slice is a short player-facing glimpse of something happening away from the player character.

Its job is to make the wider world perceptible without granting the player character omniscience.

Prefer:

`authoritative world state/events → salience selection → read-only slice → renderer`

Never:

`renderer invents distant drama → distant drama silently becomes canon`

Rules:

- Slices project events or states that already exist, or events first produced and validated by the normal world simulation pipeline.
- A slice may reveal information to the **user** while remaining unknown to the **player character**.
- Do not copy slice knowledge into player-character knowledge unless a valid information path later exists.
- Use slices selectively: long travel, seclusion, training, time skips, chapter transitions, major consequences, or a genuinely salient far-field development.
- Do not require a fixed number per turn.
- Ordinary life may be shown. A slice does not need murder, conspiracy, treasure, romance, or catastrophe.
- A slice should end before it resolves an entire distant causal chain when later uncertainty still matters.

Useful modes include:

- **众生 / Everyday:** a small view of ordinary life elsewhere;
- **暗流 / Undercurrent:** an already-existing institutional or social pressure becoming relevant;
- **因果 / Consequence:** a distant effect of prior actions or historical causes.

Acceptance checks:

1. No slice creates an unvalidated world fact.
2. Removing the slice does not change world state.
3. Player-character knowledge is unchanged unless separately transmitted.
4. Save/reload and deterministic replay preserve the source event/state used by the slice.

## 2. Bounded auto-drive

A cultivation GM should not force the player to specify every trivial physical step, but it must not seize important decisions.

Use three action-completion bands:

### AUTO

Routine, reversible, low-risk actions implied by context.

Examples: stand up, dress, pack ordinary belongings, walk through a known corridor, greet a clerk, enter a public market, perform routine sect etiquette.

### ASSUME WITHIN INTENT

The user has clearly stated the goal; the renderer may fill obvious execution details that do not change the goal, values, allegiance, resources beyond trivial cost, or long-term commitments.

Example: `去坊市看看` may include leaving residence, ordinary travel, entering the market, observing visible stalls, and normal time passage.

### STOP FOR PLAYER

Pause before decisions that are irreversible, identity-defining, high-risk, value-laden, strategically expensive, relationship-binding, or meaningfully uncertain.

Examples include killing, betrayal, marriage/bonding, becoming a disciple, exposing a major secret, accepting an unknown dangerous medicine, entering an obvious lethal zone, choosing a cultivation path, spending a major resource, signing a binding contract, or making a decisive political commitment.

Auto-drive may make the world respond; it may not manufacture player intent.

Acceptance checks:

- A terse player action can progress without repeated `what next?` prompts.
- Major choices remain explicitly player-controlled.
- Auto-completed actions are consistent with inventory, location, capability, time, and knowledge.

## 3. Opening Momentum, not mandatory Opening Crisis

A strong opening should make the player feel that the world is already moving.

Do not require poisoning, assassination, apocalypse, a countdown, or immediate combat.

Within the first few meaningful turns, establish:

`PLACE + PEOPLE + CURRENT PRESSURE + IMMEDIATE CURIOSITY`

The opening should introduce at least one **newly visible variable or change** such as:

- someone arrives, leaves, or fails to appear;
- a small rumor reaches the player;
- a market price has changed;
- a local rule is being enforced differently;
- a familiar place has changed hands;
- a minor anomaly appears;
- a sect recruitment, inspection, festival, caravan, examination, or seasonal task begins;
- an old relationship produces a new obligation.

The change may be small. It must not be forced into a major plot merely to increase dramatic density.

Opening types may include quiet, social, economic, exploratory, institutional, mystery, wonder, crisis, recovery, or travel openings.

## 4. Current Age Snapshot

Do not begin a large cultivation sandbox with a lore dump.

Provide a compact current-age frame that answers:

- What kind of era is this?
- What is changing now?
- What are people competing over or adapting to?
- Why does the current period create unusual opportunity, pressure, uncertainty, or mobility?
- Where is the player located within that era?

Keep the player-facing snapshot short enough to function as an orientation layer, while the full historical model remains elsewhere.

A useful causal form is:

`long-term environmental/institutional change → resource/social effects → faction behavior → ordinary-life consequences`

Avoid declaring the whole world permanently chaotic merely because the opening needs activity.

## 5. Macro-era pressure / “Great Contest” pattern

A cultivation world may use a high-mobility era in which opportunities, competition, recruitment, migration, new organizations, exploration, and resource disputes become more common.

This is a **world-era condition**, not a plot injector.

Good implementation:

`macro cause → measurable regional effects → institutional response → market/social/cultivation consequences`

Possible causes include qi-cycle change, route reopening, demographic growth, institutional fragmentation, technological/technique diffusion, new frontier access, old monopolies weakening, ecological recovery, or the return of previously inaccessible sites.

Do not use the era label to justify arbitrary events.

A “Great Contest” era may increase:

- recruitment and training demand;
- migration and social mobility;
- material demand and price volatility;
- organization formation and expansion;
- competition over routes, land, mines, spirit fields, texts, teachers, and disciples;
- opportunities for previously marginal actors;
- failure rates and displacement as competition rises.

It does **not** imply constant warfare, universal crisis, or that every region is equally affected.

Quiet regions, routine life, stable institutions, and long periods with no major incident must remain possible.

## 6. Prompt/adjudication patterns

Borrow the discipline of a strong GM checklist without running a giant checklist every turn.

Use **relevance-triggered modules**.

Candidate modules:

### World / scene consistency

Check location, time, weather/environment, local qi conditions, visible actors, and world-state consequences only when they matter to the action.

### Capability / law boundary

Check whether the proposed action is physically, socially, institutionally, and cultivation-mechanically possible. Reject impossible results or resolve to the nearest feasible outcome rather than granting success because the player is important.

### Resource / object consistency

Check inventory, money, qi/energy, tools, materials, wounds, conditions, access rights, travel time, and scarce facilities when the action consumes or depends on them.

### Actor / knowledge consistency

For relevant NPCs, check identity, role, motives, memory, relationship, injury/status, beliefs, and information provenance. NPCs act on what they can know, not on GM truth.

### Combat / breakthrough / exceptional-action checks

Activate only when applicable. Verify prerequisites, preparation, environment, resource expenditure, risk, opponent capability, injury, and lasting cost. Do not use narrative importance as a substitute for mechanism.

### Causal persistence

Promises, debts, tasks, injuries, exposure, reputation, witnessed acts, legal consequences, and unfinished events persist when their causes persist.

### State synchronization

Narrative output and authoritative state must agree. If state changes are required, route them through the project’s normal validation/canonicalization path; prose alone does not mutate truth.

Principle:

> Trigger only the checks relevant to the current action. Do not pay the token, latency, and rigidity cost of running every module every turn.

## 7. Renderer and summary boundaries

Style profiles, summaries, archives, and slices are presentation/memory aids.

They are not higher authority than world state.

- Renderer may change tone, compression, sensory detail, sentence form, and presentation order.
- Summary may compress validated history but must not invent missing facts.
- Archive entries should retain provenance where the project supports it.
- A stylish or plausible narration must not override a failed validation.

## 8. Anti-overuse rules

Do not confuse “living world” with continuous event generation.

A living cultivation world may contain:

- routine work;
- quiet travel;
- uneventful training;
- recovery;
- waiting;
- slow relationship drift;
- seasonal economic changes;
- institutions functioning normally;
- consequences gradually becoming visible.

Do not force:

- a countdown into ordinary scenarios;
- a major hook into every location;
- Tianji slices every turn;
- NPC signature traits to dominate all behavior;
- macro-era pressure to affect every region equally;
- the entire adjudication checklist on every response.

The system should support drama without becoming addicted to drama.

## 9. Adoption rule

For each pattern, record one of:

- `ALREADY_STRONG`
- `TUNE`
- `ADOPT`
- `OPTIONAL_PATTERN`
- `REJECT`
- `DEFER`

Before `ADOPT`, name the concrete gap and test that the pattern closes it without violating player agency, authority, context budget, deterministic persistence, or quiet-world behavior.
