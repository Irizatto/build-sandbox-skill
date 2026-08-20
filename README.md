# build-sandbox-skill

One Codex skill with three selectable forms:

| Form | Use for |
| --- | --- |
| `generic` | Domain-neutral persistent sandbox core |
| `competitive` | Competitive rules, drafts, lineups, seasons, and matchups |
| `cultivation` | Cultivation/xianxia open worlds and SillyTavern packages |

Invoke `$build-sandbox`, then choose one form. The forms share one entry point but remain domain-isolated. The original three repositories are preserved in `modes/` as vendored source material, with their assets, references, and validators retained.

## Layout

```text
SKILL.md
agents/openai.yaml
scripts/                 # unified mode-dispatching commands
modes/generic/           # former build-persistent-sandbox
modes/competitive/       # former build-competitive-rules-sandbox
modes/cultivation/       # former build-cultivation-sandbox
```

MIT licensed.
