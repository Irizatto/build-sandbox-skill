# Context engineering and SillyTavern

## Public firewall

Keep World Truth, NPC Belief, Player Knowledge, and Rumor separate. Never serialize story-registry secrets into an ordinary context packet.

## Retrieval scoring

Rank current region and faction first, then direct relationships and recent interaction, then event tags and detail tier. Return public fields only.

- ordinary scene: 4–10 named actors;
- complex meeting: 10–16;
- exceptional maximum: 20;
- Always-On full actor dossiers: 0.

## Lorebook rules

- Put invariant rules and world-scale public institutions in lore.
- Give only world-famous actors selective public entries.
- Never let a lore hit imply current presence.
- Keep current health, location, office, marriage, injuries, and death in runtime state.
- Default long-play World Info cap: 8K tokens. Lower it for contexts below 32K.

## Card and live installation

Produce one canonical `chara_card_v2` JSON and one PNG containing the same base64 `chara` chunk. Include authority, fairness, a non-dumping opening, an 8K selective book, an honest version, and no development inspiration metadata.

For a new major world version, use a separate extension folder, service port, and save name. Disable the previous bridge injection before enabling the new one. Bind local services only to `127.0.0.1`; reject path traversal, remote origins, oversized limits, and implicit year advancement. Do not stack multiple systems that claim the same memory or state authority.

Give every extension version a fully independent DOM/CSS namespace; changing the module name and port is insufficient if control IDs still collide with the previous bridge. When tuning a live installation, audit helper extensions that automatically maximize model context or force global World Info defaults. Disable those automation switches before applying explicit long-play limits, then reload the actual UI and verify displayed values rather than trusting the JSON file alone.

Prefer one long-term narrative memory authority. Keep automatic summaries, thought generators, RPG trackers, weather systems, and secondary memory injectors disabled when the sandbox already owns those state domains. “Disabled inside the extension” may still execute its client script; use SillyTavern's disabled-extension list when an overlapping extension continues to load or error.
