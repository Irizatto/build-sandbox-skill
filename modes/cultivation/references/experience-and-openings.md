# Cultivation Experience Surface Patterns

Use this reference when the world machinery already works but play still has friction at the surface: micro-step interaction, weak first-session pull, poor era orientation, or a wider world that exists in state but is hard for the player to perceive.

These are **patterns, not a feature quota**. For each candidate classify `KEEP_EXISTING`, `TUNE_EXISTING`, `IMPLEMENT_GAP`, `DEFER_NO_PROVEN_RETURN`, or `BLOCKED`. Only `TUNE_EXISTING` / `IMPLEMENT_GAP` authorize work.

Default approved surface set:

1. bounded auto-drive;
2. Opening Momentum;
3. Current Age Snapshot;
4. Tianji/offscreen slices with epistemic quarantine.

Do not treat this reference as authorization for a macro-era rewrite, a giant adjudication checklist, or continuous drama generation.

## 1. Bounded auto-drive

Goal: remove low-value conversational friction without taking meaningful decisions away from the player.

Use three bands:

### AUTO

Routine, reversible, low-risk execution details already implied by context: standing up, ordinary dressing, habitual belongings, walking a known safe route, routine greetings, ordinary etiquette, entering an open public venue, and normal time passage caused by those actions.

### ASSUME_WITHIN_INTENT

The player has stated a clear goal. The GM may complete obvious intermediate actions if they do not materially change strategic intent, values, allegiance, cultivation path, major resources, long-term relationship commitment, secret exposure, or meaningful risk.

`去坊市看看` may include leaving home, taking the familiar route, arriving, and observing immediately visible public surroundings.

### STOP_FOR_PLAYER

Stop before killing, betrayal, marriage/binding bonds, oath, disciple/lineage commitment, major secret exposure, unknown dangerous consumption, obvious lethal risk, cultivation-path choice, major spending, binding contract, decisive political/institutional commitment, irreversible body/soul modification, or materially different interpretations of ambiguous high-impact intent.

Default policy is **conservative**.

> Auto-drive may complete **how** the stated action is carried out. It may not decide **what the player chooses to do next**.

Auto-drive must still respect location, travel time, inventory, access, injury, fatigue, cultivation capability, permissions, and known routes.

Mutation tests should fail if auto-drive is altered to spend a major resource, bypass access/injury, or commit the player to a high-impact choice.

## 2. Opening Momentum

A strong opening should feel active without requiring an opening crisis.

Within the first few meaningful turns, establish:

`PLACE + PEOPLE + CURRENT PRESSURE + IMMEDIATE CURIOSITY`

The pressure may be small. Curiosity does **not** require anomaly.

Valid quiet examples include a regular vendor being absent, a shop changing hands, a medicine costing slightly more, rain delaying transport, a caravan arriving, seasonal work beginning, a familiar person acting differently, a local rule changing, or a teahouse changing its sign.

Preserve multiple opening modes: quiet life, market/social, sect/institutional, travel, exploration, recovery, wonder, mystery, and higher-pressure/crisis.

The player may ignore the initial curiosity. If ignored, the underlying situation continues, fades, resolves, or changes according to world causality. The Director must not enlarge it into a crisis merely to recover attention.

Mutation tests should fail if every opening is forced into a crisis, ignored hooks automatically escalate, or curiosity becomes a mandatory quest.

## 3. Current Age Snapshot

Current Age is a **projection of existing Canon**, not permission to invent a new era.

Use:

`existing canon / world history / validated current state → 2–4 relevant macro facts → compact orientation`

The player-facing result should usually be one short paragraph or a few concise lines answering:

- what historical moment this is;
- what is changing now;
- what ordinary people notice;
- what kinds of mobility, pressure, or opportunity exist;
- where the current locality sits within that moment.

Prefer causal structure:

`long-term cause → institutional/resource/social consequence → ordinary-life manifestation`

Do not duplicate the same era explanation into GM prompt + World Info + opening prose. Keep full history in canonical lore/retrieval and render a selective snapshot only when relevant: fresh opening, explicit orientation request, meaningful long time skip, arrival in a materially different region, or a committed macro transition.

Ordinary home scenes should normally pay zero tokens for this snapshot.

If the current Canon does not support a dramatic era pressure, a quiet/stable age is valid. Do not manufacture a Great Contest merely because a reference pattern exists.

## 4. Tianji / offscreen world slices

Tianji makes the wider world perceptible without making the player character omniscient.

Core flow:

`authoritative state / committed event → relevance + salience selection → read-only Tianji projection → user-visible rendering`

Never:

`renderer invents interesting distant event → event silently becomes canon`

Removing a Tianji block from display must not alter world state.

Useful sparse modes:

- `天机·众生` — ordinary life elsewhere;
- `天机·暗流` — an already-existing social/institutional/economic/cultivation pressure;
- `天机·因果` — a distant consequence of prior causes.

Eligible contexts include meaningful time skips, long travel, seclusion, long recovery, phase transitions, salient offscreen consequences, major already-committed regional change, or an explicit request to view the wider world.

Normal turns may produce zero Tianji. Do not use a fixed count or every-N-turn quota.

## 5. Tianji epistemic quarantine

Hard distinction:

`USER KNOWLEDGE != PLAYER CHARACTER KNOWLEDGE != NPC KNOWLEDGE`

A statement in the GM prompt saying “the PC does not know this” is not sufficient protection when the same secret text remains in subsequent model-visible conversation history.

### Tier A safe mode

Without verified outgoing-prompt quarantine, Tianji may show only information that is safe if the model later sees it: broad public macro movement, ordinary non-secret life elsewhere, already-public institutional changes, or low-risk atmosphere.

Do not use Tier A Tianji for hidden murder plans, undiscovered identities, private strategy, secret techniques, hidden treasure locations, concealed NPC motives, or other facts whose leakage would damage the epistemic model.

### Tier B user-only mode

If the deployment supports a scoped outgoing-prompt transformation (for example a SillyTavern Regex rule configured to alter outgoing prompt while leaving chat display/storage intact), user-only Tianji may be marked with a stable wrapper such as:

```xml
<天机 type="众生|暗流|因果" visibility="user_only">
...
</天机>
```

The exact syntax is project-specific. The required behavior is:

- stored/displayed chat: Tianji remains visible to the user;
- next outgoing model prompt: the quarantined block is absent;
- normal non-Tianji prose is preserved;
- the filter is scoped to the intended character/world rather than globally destructive.

If quarantine is unavailable or disabled, secret user-only Tianji must be disabled or downgraded to a safe Tier A slice. Never silently emit secret user-only information without quarantine.

### Verification

A Tianji quarantine does not PASS because the display looks correct. Verify:

`CHAT DISPLAY contains slice`

and

`OUTGOING PROMPT does not contain quarantined slice`

Prefer actual assembled-prompt inspection. If only a custom simulator is available, document its fidelity and do not claim exact SillyTavern behavior.

Mutation tests should fail if the user-only slice is left in the outgoing prompt, copied into PC knowledge, granted to NPCs, or allowed to mutate world state.

## 6. Sparse context and authority

Classify every added item as `ALWAYS_ON`, `SELECTIVE`, `RENDER_ONLY`, `OPTIONAL_TIER_B`, or `DEVELOPMENT_ONLY`. Prefer selective/render-only.

Reject broad common-word triggers, single-character CJK triggers without proof, empty keys, generic titles as entity keys, mega-entries, trigger avalanches, uncontrolled recursion, or renderer-created Canon.

The experience surface must reuse existing State, Event/History, Epistemic, Projection, and Validation owners. Do not create a second world authority.

## 7. Evidence quality

Do not count `assert(true)`, fixture self-certification, `expected = implementation output`, or mocks that bypass the real retrieval/authority path as behavioral evidence.

A meaningful test must be able to fail when the behavior is deliberately broken.

At minimum test:

- low-risk terse action advances naturally;
- high-impact ambiguous action stops;
- quiet opening has momentum but no crisis;
- ignored opening curiosity does not force escalation;
- Current Age uses existing Canon and does not repeat in unrelated scenes;
- normal turns can produce zero Tianji;
- Tianji source maps to authority;
- user-only Tianji preserves PC/NPC knowledge boundaries;
- extension/quarantine-off fallback leaves Tier A playable;
- baseline-vs-final assembled context remains approximately neutral.

## 8. Final principle

The experience layer is successful when the world becomes easier to enter, easier to move through, and easier to perceive **without becoming louder, more omniscient, more scripted, or more expensive to prompt**.
