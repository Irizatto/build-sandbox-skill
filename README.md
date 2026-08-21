# build-sandbox-skill

One Codex skill with three selectable forms and a shared living-world lifecycle.

| Form | Use for |
| --- | --- |
| `generic` | Domain-neutral persistent sandbox core |
| `competitive` | Competitive rules, drafts, lineups, seasons, careers, teams and matchups |
| `cultivation` | Cultivation/xianxia open worlds and SillyTavern packages |

Invoke `$build-sandbox`, select one primary form, then **read the preserved mode contract at `modes/<mode>/SKILL.md`** before applying its references. The root shared layer supplements those contracts; it does not replace them.

## Source-mode parity

The original three skill repositories are vendored intact under `modes/`. `vendor_manifest.json` records the exact source commit and Git tree SHA for each mode. Run:

```powershell
python -X utf8 scripts/audit_vendor_parity.py
```

before claiming that an update still preserves all source-mode files.

At the current manifest revision:

- `modes/generic` matches `Irizatto/build-persistent-sandbox` tree `333fb85d2a7218d0732f1a24d70d7093f694f43e`.
- `modes/competitive` matches `Irizatto/build-competitive-rules-sandbox` tree `a178cd93c73e855120240bb38520cac73e6302eb`.
- `modes/cultivation` matches `Irizatto/build-cultivation-sandbox` tree `e14fc41518f1f226f1e61dc36d01283796e7413d`.

This verifies byte-level vendored-tree parity at the recorded commits. Behavioral parity additionally depends on reading the selected mode `SKILL.md`; see `references/mode-routing-and-compatibility.md`.

## Shared living-world layer

The root `references/` directory contains domain-neutral patterns for persistent living worlds:

- `mode-routing-and-compatibility.md` — mandatory preserved-mode loading, generic-core dependency mapping, source-tree parity and competitive from-zero routing.
- `living-sandbox-lifecycle.md` — six gated phases: horizon/topology, organizations, actor promotion/life, relationships/narrative, domain depth, long-session hardening.
- `world-growth-and-materialization.md` — stable macro skeletons, latent seeds, deterministic materialization, Canon persistence and bounded context.
- `character-life-relationship-narrative.md` — private/everyday life, bookmark without destiny inflation, multidimensional relationships, Character Anchors, NPC initiative and causal scene progression.
- `lived-world-token-safe-experience.md` — everyday life, embodiment, material culture, social grammar, information ecology, player-created history, discovery, social friction, world scars and personal belonging while keeping prompt growth bounded.
- `sillytavern-first-playability.md` — delivery contract for projects whose real product is the SillyTavern package itself: core-playable Tier A, optional STscript/Quick Replies Tier B, optional future runtime Tier C, plus ST-realistic context and playability gates.
- `gameplay-review-and-validation.md` — periodic gameplay review and long-session test matrix.
- `orchestration-and-handoffs.md` — Orca → Muse Spark Contributor → Codex workflow, workspace policy and automatic phase handoffs.

The token-safe lived-world layer is deliberately **not a mandatory seventh lifecycle phase**. It is an experience layer for mature sandboxes that need stronger ordinary-life realism and player-specific history. Its core acceptance property is context invariance: increasing offscreen world size, catalog size or historical depth must not make the same current scene grow linearly in prompt size.

When the requested artifact is directly played in SillyTavern, `sillytavern-first-playability.md` changes the optimization order: **SillyTavern playability and continuity beat future-runtime purity.** For an already mature/working package, lived-world capabilities are a diagnostic checklist rather than a feature quota: freeze and measure the baseline, keep capabilities that already play well, implement only gaps with clear player-visible return, and keep ordinary assembled context approximately token-neutral.

These shared references prevent a recurring failure mode: a sandbox with lots of lore or an unconstrained LLM but no stable world growth, persistent ordinary people, independent organizations, believable relationships, lived-world texture or long-session validation.

## Compatibility note

The competitive and cultivation mode contracts were originally separate skills and may mention `$build-persistent-sandbox`. Inside this unified repository, resolve that dependency to `modes/generic/SKILL.md` and `modes/generic/references/`; a separate external install is not required.

The original competitive skill did not include its own scaffold. For a new competitive package, use the generic scaffold with domain ID `competitive_rules`, then apply `modes/competitive/assets/competitive_domain_profile.json` and the draft schema when relevant.

## Layout

```text
SKILL.md
vendor_manifest.json
references/              # shared living-world architecture, routing and review patterns
agents/openai.yaml
scripts/                 # unified mode-dispatching commands + parity audit
modes/generic/           # preserved build-persistent-sandbox tree
modes/competitive/       # preserved build-competitive-rules-sandbox tree
modes/cultivation/       # preserved build-cultivation-sandbox tree
```

The mode directories remain domain-isolated. The shared root layer describes reusable architecture, not cross-domain vocabulary.

MIT licensed.