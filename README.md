# build-sandbox-skill

One Codex skill with three selectable forms and a shared persistent/living-world methodology.

| Form | Use for |
| --- | --- |
| `generic` | Domain-neutral persistent sandbox core |
| `competitive` | Competitive rules, drafts, lineups, seasons, careers, teams and matchups |
| `cultivation` | Cultivation/xianxia open worlds, SillyTavern packages, experience-surface design and content renaissance |

Invoke `$build-sandbox`, select one primary form, then **read the mode contract at `modes/<mode>/SKILL.md`** before applying its references. The root shared layer supplements those contracts; it does not replace them.

## Source-mode parity

The three source repositories are vendored under `modes/`. `vendor_manifest.json` records source commit and Git tree SHA for each mode. Run:

```powershell
python -X utf8 scripts/audit_vendor_parity.py
```

before claiming parity after an update.

Current source-mode targets are recorded in `vendor_manifest.json`; shared root references may add reusable behavior without modifying generic/competitive mode vocabulary.

## Shared living-world layer

The root `references/` directory contains reusable patterns:

- `mode-routing-and-compatibility.md` — mode loading, dependency mapping, source-tree parity and competitive from-zero routing.
- `living-sandbox-lifecycle.md` — six gated phases: horizon/topology, organizations, actor promotion/life, relationships/narrative, domain depth, long-session hardening.
- `world-growth-and-materialization.md` — stable macro skeletons, latent seeds, deterministic materialization, Canon persistence and bounded context.
- `character-life-relationship-narrative.md` — private/everyday life, bookmark without destiny inflation, multidimensional relationships, Character Anchors, NPC initiative and causal scene progression.
- `lived-world-token-safe-experience.md` — everyday life, embodiment, material culture, social grammar, information ecology, player-created history, discovery, social friction, world scars and belonging while keeping prompt growth bounded.
- `content-density-and-controlled-scale.md` — research-broad/implement-narrow discipline, cross-linked content density, Pilot-first authoring, history-in-present, functional affordances, two-wave scale-up, blind/mutation tests and 5x/10x inactive-context stress.
- `sillytavern-first-playability.md` — Tier A/B/C product/evidence boundary, direct ST playability, delta-only upgrades, context gates and test-evidence hardening.
- `gameplay-review-and-validation.md` — periodic gameplay review and long-session test matrix.
- `orchestration-and-handoffs.md` — both Orca→Muse→Codex and direct Muse→independent Codex workflows, workspace policy, self-gate boundaries and no-human-router handoffs.

The lived-world layer is deliberately **not a mandatory seventh lifecycle phase**. For mature packages, its capabilities are diagnostic: freeze and measure the baseline, keep what already plays well, implement only measured gaps, and keep ordinary assembled context approximately neutral.

The content-density layer applies later, when machinery is already strong but the world still feels generic or compartmentalized. Its core sequence is:

```text
research broadly
→ audit current content
→ select narrowly
→ Pilot
→ playtest
→ controlled two-wave scale-up
```

Content scale succeeds only when repository/world depth can grow while the same inactive scene remains approximately flat in context.

## Cultivation-specific references

The cultivation source mode now includes:

- `modes/cultivation/references/experience-and-openings.md` — conservative bounded auto-drive, Opening Momentum, Current Age projection, Tianji/offscreen slices and user-only epistemic quarantine.
- `modes/cultivation/references/content-renaissance-and-scale-up.md` — reference-harvest discipline, cross-linked character/place/technique/history design, technique-as-life, institutional ideology, world-rule consequence audit, xianxia flavor layers, mortal substrate, market/provenance affordance, delayed payoff, Pilot scope and controlled scale-up.

For Tianji/user-only projection, merely telling the model “the PC does not know this” is not enough when the secret remains in later model-visible chat history. Use a safe public slice or verified outgoing-prompt quarantine and test both display and outgoing prompt.

## Core design maxims

- World size must not equal prompt size.
- More features are not success; more play per token is success.
- Research broadly, implement narrowly.
- Cross-link deeply instead of mass-generating isolated content.
- Scale the method, not the template.
- Existing world rules should shape civilization before new cosmic rules are invented.
- A test counts only if broken behavior can make it fail.
- Implementer self-gates are not independent release acceptance.

## Compatibility note

Competitive and cultivation mode contracts may mention `$build-persistent-sandbox`. Inside this unified repository, resolve that dependency to `modes/generic/SKILL.md` and `modes/generic/references/`; a separate external install is not required.

For a new competitive package, use the generic scaffold with domain ID `competitive_rules`, then apply `modes/competitive/assets/competitive_domain_profile.json` and the draft schema when relevant.

## Layout

```text
SKILL.md
vendor_manifest.json
references/              # shared living-world, content-density, routing and review patterns
agents/openai.yaml
scripts/                 # unified mode-dispatching commands + parity audit
modes/generic/           # vendored generic source
modes/competitive/       # vendored competitive source
modes/cultivation/       # vendored cultivation source
```

MIT licensed.
