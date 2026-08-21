# build-sandbox-skill

One Codex skill with three selectable forms and a shared living-world lifecycle.

| Form | Use for |
| --- | --- |
| `generic` | Domain-neutral persistent sandbox core |
| `competitive` | Competitive rules, drafts, lineups, seasons, careers, teams and matchups |
| `cultivation` | Cultivation/xianxia open worlds and SillyTavern packages |

Invoke `$build-sandbox`, select one primary form, then use only the shared references needed by the task.

## Shared living-world layer

The root `references/` directory contains domain-neutral patterns that apply across scripts when the product is meant to feel like a living persistent world:

- `living-sandbox-lifecycle.md` — six gated phases: horizon/topology, organizations, actor promotion/life, relationships/narrative, domain depth, long-session hardening.
- `world-growth-and-materialization.md` — stable macro skeletons, latent seeds, deterministic materialization, Canon persistence and bounded context.
- `character-life-relationship-narrative.md` — private/everyday life, bookmark without destiny inflation, multidimensional relationships, Character Anchors, NPC initiative and causal scene progression.
- `gameplay-review-and-validation.md` — periodic gameplay review and long-session test matrix.
- `orchestration-and-handoffs.md` — Orca → Muse Spark Contributor → Codex workflow, workspace policy and automatic phase handoffs.

These shared references are designed to prevent a recurring failure mode: a sandbox that has lots of lore or an unconstrained LLM, but lacks stable world growth, persistent ordinary people, independent organizations, believable relationships and long-session gameplay validation.

## Layout

```text
SKILL.md
references/              # shared living-world architecture and review patterns
agents/openai.yaml
scripts/                 # unified mode-dispatching commands
modes/generic/           # domain-neutral persistent core
modes/competitive/       # competitive rules and evaluation
modes/cultivation/       # cultivation/xianxia specialization
```

The mode directories remain domain-isolated. The shared root layer describes reusable architecture, not cross-domain vocabulary.

MIT licensed.
