# Cultivation Anti-Patterns and Hard DON’Ts

These are cultivation/xianxia-specific constraints. Generic retrieval, persistence, actor, context, and world-expansion anti-patterns in `build-persistent-sandbox/references/anti-patterns-and-donts.md` still apply.

## World structure

- **Do not make the opening region secretly equal to the whole world.** A local vertical slice may be dense, but the macro world needs stable continents/regions, routes, polities, cultivation ecologies, major organizations, trade corridors, and historical pressures beyond it.
- **Do not prewrite hundreds of empty sects merely to claim scale.** Use a fixed macro skeleton plus organization seeds that materialize when geography, history, trade, politics, lineage, migration, or player travel makes them relevant.
- **Do not improvise a full sect from unconstrained prose when first mentioned.** Resolve from a seed contract, check collisions and regional constraints, assign stable IDs, then commit it as canon.
- **Do not make every region play like the opening region with renamed nouns.** Regions should differ in qi ecology, resources, institutions, cultivation traditions, mortal-cultivator relations, orthodoxy/heterodoxy, economy, danger, and opportunity ecology.
- **Do not let famous far-field NPCs substitute for a populated far-field world.** Named masters are not the same thing as routes, towns, sects, institutions, ordinary actors, local conflicts, and playable economies.

## Sect and organization generation

A generated sect should never be just:

`name + element + leader + three elders`.

At minimum resolve:

- stable organization ID and aliases;
- home region and topology;
- founding origin and age;
- cultivation tradition and tacit knowledge;
- recruitment and membership ecology;
- governance and succession;
- offices and internal factions;
- resource base and dependencies;
- economy, labor, logistics, and externalities;
- allies, rivals, creditors, protectors, dependents;
- mortal relationship;
- law/custom/discipline;
- public reputation versus internal reality;
- current pressure;
- one or more failure modes;
- historical scars;
- what ordinary days inside the sect look like.

- **Do not guarantee every generated sect a secret treasure, ancient inheritance, hidden traitor, or world-level conspiracy.** Ordinary institutions are necessary.
- **Do not make demonic/heterodox organizations survive through random cruelty alone.** They need enforceable institutions: contracts, hierarchy, kinship, quotas, compensation, retaliation, shared infrastructure, registration, patronage, or other durable mechanisms.
- **Do not make every sect leader the sole organization.** Offices, procedures, knowledge holders, factions, logistics, disciples, and succession must survive leader absence or death when appropriate.

## Cultivation progression

- **Do not reduce realms to universal game levels.** Regional interpretations, technique-specific requirements, body/soul differences, tacit skill, resources, timing, risk, and social access should matter.
- **Do not make time investment alone guarantee breakthrough.**
- **Do not grant free cross-realm victories because the player is clever or narratively important.** Extraordinary wins require explicit preparation, information, environment, counters, allies, sacrifice, or lasting cost.
- **Do not treat reading a manual as mastery.** Text, instruction rights, tacit calibration, bodily adaptation, practice, and lineage access may differ.
- **Do not make every rare technique strictly stronger.** Techniques should create tradeoffs, niches, dependencies, risks, social consequences, and environmental fit.

## Opportunities and wonder

- **Do not turn travel into continuous jackpot delivery.** Large opportunities need exposure conditions, windows, competitors, cost, risk, and second-order consequences.
- **Do not reserve opportunities for the player.** NPCs may discover, purchase, inherit, steal, destroy, misunderstand, or miss them.
- **Do not make every cave, ruin, rumor, strange weather event, or old object a hidden inheritance.**
- **Do not confuse exotic names with cultivation wonder.** Wonder should change decisions, bodies, economies, beliefs, geography, techniques, institutions, or history.
- **Do not let the social simulation overwhelm the fantastical layer.** A cultivation world needs genuine qi ecology, strange geography, nonhuman life, techniques, artifacts, rituals, cosmology, forbidden practices, cave heavens, secret realms, and unknowns—but these must still obey persistence and causality.

## NPC ecology and character charm

- **Do not make all high-level cultivators rational reformers, institution builders, or policy experts.** Include love, faith, vanity, beauty, curiosity, jealousy, family, revenge, pride, loneliness, pleasure, art, fear of death, obsession, tradition, ambition, and irrational commitments.
- **Do not make every important female NPC beautiful, romantically available, or attracted to the player.**
- **Do not make every master notice a low-level player.** Direct access requires route, institution, shared event, reputation, referral, duty, or another causal path.
- **Do not make all charismatic actors high-tier.** A boatman, disciple, shopkeeper, healer, clerk, mortal relative, rival apprentice, or innkeeper may become more important to a particular playthrough than a famous immortal.
- **Do not let relationship importance imply cultivation importance.** A player-favorite NPC can remain ordinary in power and public status.

## NPC promotion / player bookmarking

Support a distinction between:

1. **world importance** — fame, office, power, institutional weight;
2. **simulation importance** — how much offscreen detail the runtime allocates;
3. **narrative importance** — relevance to current arcs and relationships;
4. **player bookmark** — explicit player preference to retain and revisit an actor.

A bookmark may promote an ephemeral/generated actor from Tier C to B/A detail and persist its stable ID, memories, relationships, routine, voice, goals, and future simulation budget.

- **Do not let bookmarking automatically increase affection, romance, cultivation talent, luck, plot armor, fame, office, availability, or connection to world mysteries.**
- **Do not retroactively rewrite the actor into having always been secretly important.** Promotion adds future detail while preserving established history.
- **Do not discard a promoted actor on context compression.** Keep compact identity/history and reload richer facets when relevant.

## Sect seeding and materialization

Prefer:

`macro region → regional constraints → organization seed → relevance trigger → deterministic materialization → collision/authority validation → stable ID commit → sparse public projection`

A seed may contain only latent variables such as:

- region/subregion;
- age band;
- scale band;
- cultivation family;
- resource dependency;
- governance archetype;
- orthodoxy/heterodoxy;
- social base;
- current pressure;
- historical scar;
- relationship hooks to already canonical organizations.

Do not materialize all seeds at startup. Materialize when the world needs a concrete organization because of travel, trade, news, ancestry, politics, recruitment, investigation, or offscreen history.

Once materialized, it is canon and may evolve independently.

## Plot and mystery

- **Do not make every personal arc converge on one ancient secret.**
- **Do not make all historical contradictions part of one conspiracy.** Independent causes are allowed.
- **Do not turn every local dispute into a cultivation apocalypse.**
- **Do not use an NPC scholar, prophet, immortal, archive, or artifact as a truth-dump device.** Knowledge remains source-bound and fallible.
- **Do not make a player's refusal to pursue a plot freeze it.** Factions, disasters, reforms, succession, research, wars, and discoveries continue offscreen when their causes persist.

## Sect governance

- **Do not turn becoming a sect leader into an unrelated management minigame.** Governance should grow from the same actors, resources, relationships, offices, routes, debts, teachings, and history already simulated.
- **Do not require the player to manually approve every routine action.** Use policy, delegation, budgets, offices, and exception briefs.
- **Do not make silence stop administration.** Authorized defaults continue unless an exception crosses authority, budget, irreversible-harm, or value-conflict thresholds.

## Release tests

Test at least:

1. player leaves the opening region immediately;
2. a previously latent region/sect is materialized and revisited years later;
3. two generated sect seeds collide on name/resource/history and the validator resolves or rejects them;
4. a player bookmarks an ordinary generated NPC and revisits them after months/years;
5. bookmarked NPC remains personally important without receiving supernatural promotion;
6. high-tier famous NPC stays offscreen despite keyword mentions;
7. one century of sect succession and organizational survival;
8. quiet travel with no treasure or major plot;
9. NPC wins an opportunity the player could have pursued;
10. a distant region feels mechanically and socially different from the opening region.
