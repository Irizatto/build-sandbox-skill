# Mechanics and state machines

## Contents

1. Mechanic contract
2. Legality and transitions
3. Counters and synergies
4. Versioning and uncertainty
5. Tests

## Mechanic contract

Represent every consequential rule with a machine-readable contract. Require stable ID, version, domain, authority, state schema, initial state, participants, ordered phases, legal actions, preconditions, resolution priority, randomness, visibility, costs, commitments, terminal states, invariants, edge cases, and tests.

Use `assets/mechanic_contract.schema.json` as the minimum interchange schema. A project may extend it but must not weaken its invariants.

## Legality and transitions

Treat prose as explanation and the contract as authority. Expose functions equivalent to:

```text
legal_actions(state, actor, knowledge)
apply_action(state, action, seed) -> new_state + events
validate_state(state) -> violations
project_state(state, viewer) -> visible_state
```

Reject actions before mutation. Commit an append-only event before exposing the new state. Save/reload must reproduce the same committed result.

## Counters and synergies

Avoid a universal `A beats B` table. Represent a directed, versioned relation whose weight depends on phase, role, allied composition, environment, proficiency, information quality, and current ruleset. Store provenance, evidence class, confidence, uncertainty range, applicable contexts, exceptions, and expiration. Some interactions require hyperedges involving three or more entities rather than pairwise edges.

Separate legality, recommendation, prediction, and narrative opinion. Never present a recommendation as a rule or a noisy estimate as truth.

## Versioning and uncertainty

Pin each run to a ruleset version. Preserve historical outcomes under the rules that produced them. Mark unknown or disputed mechanics explicitly instead of inventing precision.

Derive randomness from stable coordinates such as `(simulation_seed, mechanic_id, ruleset_version, event_id, decision_index)`. Store the resulting event; do not reroll on reload.

## Tests

Every mechanic needs a happy path, each illegal action class, boundary state, priority conflict, save/reload equivalence, version mismatch, hidden-information projection, deterministic replay, one mutation that must fail, and a context packet containing only current-phase material.

