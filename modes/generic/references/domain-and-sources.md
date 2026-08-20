# Domain isolation and source synthesis

## Contents

1. Domain profile
2. Source map
3. Design DNA
4. Conflict matrix
5. Crossover policy

## Domain profile

Freeze one primary domain before generating content. Use an explicit profile with:

- `domain_id` and `domain_version`;
- allowed and forbidden vocabulary;
- actor, organization, location, resource, event, and mechanic families;
- topology and time model;
- player roles and advancement paths;
- tone and dramatic-density limits;
- source policy and visibility policy;
- authorized secondary domains, normally empty.

Treat the denylist as a generation and validation boundary, not a style suggestion. Generic core schemas use neutral nouns. A domain pack maps neutral nouns to its own terms.

## Source map

Inventory files before reading deeply. For each source record its authority, scope, format, size, integrity, useful sections, and prohibited uses. Choose close-read, sample, skim, or ignore with a reason.

Classify sources as authority, design DNA, mechanical reference, presentation reference, or excluded. Extract mechanisms as `pressure → institution/behavior → consequence → failure mode`. Do not transplant names, prose, plots, iconic combinations, or hidden development metadata.

## Conflict matrix

Resolve conflicts before content generation. Compare scale and time, capability progression, resource scarcity, organization logic, knowledge availability, player privileges, mortality, randomness, legal rules, and narrative density.

Record the selected rule, rejected alternatives, reason, affected schemas, migration effect, and tests.

## Crossover policy

Default to no crossover. A crossover requires an explicit secondary domain, a mapping table, conflict resolutions, and a test proving unrelated vocabulary does not leak into ordinary scenes. A mere example in a prompt or reference never authorizes crossover content.

