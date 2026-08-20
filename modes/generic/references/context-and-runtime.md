# Context and runtime projection

## Contents

1. Projection model
2. Retrieval
3. SillyTavern routing
4. Model profiles
5. Runtime ownership

## Projection model

Never inject the raw world database. Build viewer-specific packets from viewer, location or topology, mechanic phase, relationships, current event, recent contact, and knowledge rights. Separate world truth, actor belief, player knowledge, rumor, and recommendation. Public serializers must omit private fields by schema, not by prompt request alone.

## Retrieval

Use deterministic candidate filters before semantic ranking. Reserve explicit budgets for core rules, current state, active entities, retrieved history, and response space. Measure the fully assembled request with the target tokenizer when available. Test unload behavior after leaving a location or phase.

## SillyTavern routing

- Put invariant instructions and compact public institutions in character data or constant/selective World Info.
- Put keyword or regex-addressable facts in World Info.
- Put context-specific public lore in character, persona, or chat lore.
- Put large reference documents in Data Bank/RAG.
- Put mutable state and private projections in one runtime-owned state packet.
- Put deterministic actions and updates in STscript, an extension, or a local bridge.
- Use World Info outlets when exact prompt placement is required and supported.

Configure scan depth, recursion, filters, triggers, token budget, and vector matching intentionally. For languages without whitespace word boundaries, disable whole-word matching unless keys were designed for it. Test recursive activation for loops and budget avalanches.

## Model profiles

Create a profile per target model family containing context limit, reserved output, prompt format, system-role behavior, tokenizer or estimate, instruction density, retrieval chunk size, and maximum active entities. Use a small-context profile as the correctness baseline.

## Runtime ownership

Assign one owner for current state, long-term narrative memory, summarization, and time advancement. Disable overlapping extensions or adapters. Bind local services to loopback, validate origins and paths, cap payload sizes, version saved state, and provide idempotent migration plus rollback.

