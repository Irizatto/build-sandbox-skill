# Character Life, Relationships, and Narrative Runtime

Persistent actors should be **people with lives**, not quest interfaces or stat rows.

## Character Life model

For important actors, progressively support:

### Identity layers
- PUBLIC_SELF;
- PROFESSIONAL_SELF;
- PRIVATE_SELF;
- INTIMATE_SELF when boundaries/relationship context make it relevant.

The intimate layer means private trust, vulnerability and boundaries. It does not require explicit sexual content.

### Character structure
- values, principles, desires, fears;
- contradictions, weaknesses, biases;
- short/medium/life goals;
- relaxed/stressed/angry/embarrassed/excited/tired behavior;
- hobbies, comforts, annoyances;
- sleep, food, money, home/personal-space habits;
- family, friends, mentors, students, colleagues, rivals, former ties;
- formative events, unresolved issues, current pressures;
- voice, vocabulary, rhythm, humor, common expressions, silence/avoidance patterns;
- a few dialogue exemplars when useful.

Do not load all of this every turn. Project only relevant facets.

## Anti-collapse distribution

Do not make every major actor calm, rational, optimization-driven and institutionally reformist. Populations may be driven by love, family, jealousy, vanity, honor, faith, curiosity, aesthetics, pleasure, loneliness, revenge, fear of death, nostalgia, ambition, status, identity, irrational loyalty or simple passion.

Reasonable-but-suboptimal decisions are valid when character-consistent.

Charm is not the same as beauty, youth, romance or availability to the player.

## Actor promotion / bookmark

A contextual actor may become recurring or major because of repeated contact, shared events, obligations, historical importance or an explicit player bookmark.

Bookmark/favorite may increase:
- retention;
- simulation detail;
- memory preservation;
- retrieval priority.

It must not automatically increase:
- power;
- fame;
- luck;
- affection/attraction;
- access;
- plot armor;
- world importance.

Bookmarked actors may reject the player, prefer others, move, marry, fail, succeed, age or die.

## Relationship model

Do not compress all interpersonal state into one affection value. Use only domain-relevant dimensions, potentially including:
- familiarity;
- trust;
- respect;
- comfort;
- emotional openness;
- dependence/attachment;
- obligation;
- authority;
- rivalry;
- resentment;
- fear;
- attraction;
- romantic interest;
- commitment.

Separate shared/dyadic facts from A's state toward B, B's state toward A, public status, private status and player knowledge. Relationships may be asymmetric.

Major transitions require causal history, time, evidence, compatible boundaries and hysteresis. Repeated chatting alone should not speedrun intimacy.

## Character Anchor

For active scenes project a compact anchor:
- identity;
- current goal and relevant motive;
- voice;
- relevant memory;
- relationship slice;
- stress/energy state;
- knowledge boundary;
- one current contradiction/pressure when relevant.

This protects personality from being overwritten by the immediate plot.

## Narrative Runtime

Use a proposal pipeline:

`actor anchors → scene state → progress/repetition signals → stagnation detector → beat candidates → causal eligibility → proposal → authoritative validation/commit if stateful → narrative projection`

Possible scene signals include momentum, novelty, goal progress, conflict pressure, unresolved hooks, interaction repetition, location staleness and cast staleness.

A beat may be an actor decision, question, arrival/departure, eligible information, environmental change, old consequence, personal issue or natural end of a mundane activity.

Never use:
- flat `50% story beat`;
- guaranteed drama every N turns;
- every quiet scene becomes crisis/secret/romance;
- coincidence as the default route for important meetings.

`Nothing important happens` is valid gameplay.

## NPC initiative

Support:

`NPC goal → decision → action → world delta → player may or may not notice`

NPCs may cooperate with others, refuse the player, change plans, form relationships, move, work, train, create organizations, pursue opportunities, fail, retire or die offscreen.

The player does not have universal narrative priority.

## Plot scale and dormancy

Allow micro, personal, relationship, local, organization, regional, world and generational stories to remain at their natural scales.

Useful thread states may include AVAILABLE / ACTIVE / DORMANT / ESCALATING_OFFSCREEN / FAILED / RESOLVED / SUPERSEDED. Refusing a hook should not force the same hook back until accepted.

## Reusable structural patterns from roleplay cards

When studying third-party cards, extract mechanisms rather than copying plots or unsafe content. Useful transferable patterns include:
- Character Anchor and compact persona projection;
- dialogue exemplars and distinct speaker voice;
- public/private self and relationship boundaries;
- Entity Facet Retrieval rather than mega-biographies;
- hierarchical world retrieval;
- structured procedural generation axes;
- history → official record → faction interpretation → folklore/rumor layers;
- open-world deferred plots;
- player-agency guard / never author the player's thoughts or commitments;
- state/UI/narrative projection separation;
- world mutation transaction with validation and reconciliation.

Adult/NSFW source cards may be studied only for compliant structural lessons such as boundaries, trust, private self, relationship stages and intimacy dimensions. Do not reproduce explicit sexual content, coercive content, unsafe age framing, or source-specific scenes.

## Core tests

Run repeated-actor voice tests, relationship stress tests, asymmetric-relationship tests, quiet-scene tests, NPC-initiative tests, multi-NPC speaker/knowledge isolation, player-refusal tests, long-absence return tests and bookmark-without-destiny tests.
