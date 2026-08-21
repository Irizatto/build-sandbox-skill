# Content Density and Controlled Scale-Up

Use this reference when a persistent sandbox already has strong authority/state/retrieval machinery, but the **player-facing content** still feels generic, isolated, repetitive, or too shallow to inhabit.

This layer is deliberately separate from world-machinery expansion.

Core sequence:

`RESEARCH BROADLY → AUDIT CURRENT CONTENT → SELECT NARROWLY → PILOT → PLAYTEST → CONTROLLED SCALE-UP`

The goal is **more play and meaning per unit of active context**, not more entries per repository.

## 1. Broad research, narrow implementation

When using external games, novels, cards, simulations, or communities as design references, harvest abstract patterns rather than copying content.

For each pattern record:

```text
PATTERN
ABSTRACT PRINCIPLE
PLAYER VALUE
ALREADY PRESENT? YES/PARTIAL/NO
CURRENT GAP
NATIVE TRANSFORMATION
DERIVATION / HOMOGENIZATION RISK
CONTEXT COST
SYSTEM COST
ADOPT / ADAPT / EXPLORE / ALREADY_PRESENT / DEFER / REJECT
```

A good harvest has many `ALREADY_PRESENT`, `DEFER`, and `REJECT` outcomes. Reference sources are not feature checklists.

The first research/audit phase should normally make **no canonical changes** in a mature world.

## 2. Pilot before scale

Do not turn a broad content audit into a broad rewrite.

Select a small Pilot that covers the highest-return gaps. Typical Pilot dimensions may include:

- a small recurring cast;
- a handful of high-frequency places;
- a few domain-specific mechanics/objects/techniques;
- several causal threads;
- a few historical traces;
- one or two functional affordance families.

These are not quotas. Smaller is valid.

**Depth > coverage.**

## 3. Cross-linked content density

Do not enrich content as isolated workstreams.

Prefer natural webs such as:

`CHARACTER ↔ PLACE ↔ PRACTICE / OBJECT ↔ HISTORY ↔ INSTITUTION ↔ THREAD`

A useful deepened element should normally connect to at least two existing or selected elements when natural.

Do not maximize edges. Preserve dense local clusters, weak bridges, strangers, isolated actors, and relationships that may remain unknown.

The purpose is for players to encounter the same world from multiple causal angles.

## 4. Function before encyclopedia

A place, institution, object, practice, or relationship becomes more playable when the player can **do** something meaningful with it.

A functional affordance should connect to real state such as:

`time / resource / knowledge / relationship / access / reputation / location / health / ownership / obligation / history`

If an action changes nothing and reveals nothing meaningful, it may remain flavor and does not need a subsystem.

Begin with 1–2 high-return affordance families before adding more.

## 5. History in the present

Do not let history exist only as archive prose.

Prefer present traces:

- architecture;
- routes;
- ownership;
- institutions;
- customs;
- memorials;
- economic patterns;
- inherited objects/practices;
- NPC memories;
- biased public stories.

Use:

`present object/person/rule → implies old cause`

rather than exposition dumps.

### Delayed payoff

Use only facts that really existed earlier:

`OLD FACT → WORLD CHANGES → NEW CONTEXT → OLD FACT GAINS NEW SIGNIFICANCE`

This is recontextualization, not retcon.

## 6. Institutions should reveal values through procedures

A strong institution communicates what it values through practical interaction, not only lore slogans.

Use:

`WORLDVIEW → RULE → INCENTIVE / COST → DAILY BEHAVIOR → CHARACTER ADAPTATION`

Examples include access, teaching, credit/debt, resource allocation, promotion, outsider treatment, punishment, service obligations, and facility use.

## 7. Character deepening without template fill

Audit broadly; deepen selectively.

Before changing an actor:

```text
WHY THE PLAYER RE-ENCOUNTERS THEM
CURRENT STRENGTH
SPECIFIC WEAKNESS
WHAT MUST NOT CHANGE
1–3 DIMENSIONS TO DEEPEN
```

Do not give every character the same schema-completion package of hobby/favorite food/fear/catchphrase.

Useful differences may come from home, work, resource pressure, social network, contradiction, wrong belief, profession, domain practice, historical agency, or independent goals.

Allow competent actors to remain sentimental, vain, timid, lazy, prejudiced, artistic, nostalgic, afraid, or otherwise non-optimal.

Blind-test representative characters with names removed.

## 8. Domain-specific mechanics should change lives

For a deep domain object/practice/technique, ask whether it changes several of:

- practice loop;
- body or capability;
- perception;
- resources;
- environment;
- institutional access;
- non-core uses;
- tactical geometry;
- failure modes;
- long-term side effects;
- provenance/transmission;
- cultural meaning.

If only the label or damage type changes, the content is still generic.

For cultivation mode, apply the stronger `technique as a way of living` contract in `modes/cultivation/references/content-renaissance-and-scale-up.md`.

## 9. Scale the method, not the template

After a Pilot passes, scale through two waves.

### Wave A

Expand a small first ring. Then gate every content class separately:

- `GREEN_CONTINUE`
- `YELLOW_LIMIT`
- `RED_STOP_CLASS`

### Wave B

Only green/yellow-permitted classes continue.

If one class becomes repetitive, stop scaling that class while allowing other useful classes to continue.

`STOPPED_CLASS_AFTER_WAVE_A` and `REVERTED_NO_VALUE` are valid disciplined outcomes.

Bad scale-up duplicates a Pilot schema across dozens of actors/places/items.

Good scale-up uses:

`actual local weakness → smallest deepening → natural cross-links → player-visible test → keep/revert`

## 10. Unequal depth is a feature

Do not author the entire world at equal resolution.

Prefer:

`current/opening area HIGH → adjacent area MEDIUM → one contrasting area MEDIUM/selective → rest sparse`

Likewise preserve actor/content detail tiers.

A large world feels large partly because much of it remains outside current focus.

## 11. Content compression

When a new selective facet replaces weak generic prose:

1. find redundant old prose;
2. remove or compact it when safe;
3. preserve one authority;
4. split deep data into selective facets;
5. keep private details out of broad public context.

Do not keep old generic text + new rich text merely because both already exist.

## 12. World size must remain decoupled from prompt size

Repository/content growth is not itself a problem. Active-prompt growth is.

Inactive actors, regions, histories, items, institutions, and practices should cost zero or near-zero context.

For mature SillyTavern packages, useful default guards remain:

- always-on/core: prefer `<= +50`, warning around `+100`;
- quiet/inactive scene: `<= min(+5%, +200)`;
- ordinary social: `<= min(+7%, +350)`;
- dense local: `<= min(+10%, +600)`.

The project's stricter measured baseline wins.

Also run scale stress:

```text
5x inactive content → same active scene approximately flat
10x inactive content → same active scene approximately flat
```

Success means:

`CONTENT REPOSITORY ↑↑ while ORDINARY ACTIVE PROMPT ≈ FLAT`

## 13. Evidence must discriminate good from broken implementations

Do not count:

- `assert(true)`;
- fixtures that certify themselves;
- `expected = implementation output`;
- mocks bypassing the real authority/retrieval path;
- generated transcripts that only grade themselves.

Use mutation/blind tests.

Examples:

- make two regions structurally identical → contrast test must fail;
- strip actor differences → character blind test must fail;
- reduce domain mechanics to label swaps → specificity test must fail;
- force ignored threads to escalate → agency test must fail;
- inject distant inactive content → context-scale test must fail;
- leak private knowledge → epistemic test must fail.

## 14. Quiet play remains a hard gate

More content must not create more event bombardment.

A scale-up should still support long stretches of:

- routine;
- work;
- travel;
- recovery;
- ordinary relationships;
- low-stakes obligations;
- slow historical consequences.

A living world is not a world that constantly tries to entertain the player with crisis.

## 15. Final criterion

The content-density layer succeeds when players can care about more people, places, practices, institutions, and history because those elements reinforce one another—without mass-produced sameness, duplicate authority, forced drama, or prompt growth proportional to world size.

> **Research broadly. Select narrowly. Implement narrowly. Cross-link deeply. Scale the method, not the template.**
