# Mode Routing and Compatibility

The unified root skill **supplements** the three preserved mode skills. It does not replace them.

## Mandatory mode loading

After selecting exactly one primary mode, read that mode's preserved contract **before** mode-specific references:

- `generic` → `modes/generic/SKILL.md`
- `competitive` → `modes/competitive/SKILL.md`
- `cultivation` → `modes/cultivation/SKILL.md`

Then resolve any relative `assets/`, `references/`, `scripts/`, or `agents/` paths inside that contract relative to the selected `modes/<mode>/` directory.

A task is not fully routed merely because the files exist in `modes/`; the mode contract must actually be read and applied.

## Generic-core compatibility mapping

The competitive and cultivation mode contracts were vendored from standalone skills and may refer to `$build-persistent-sandbox` or its references. Inside this unified repository, interpret those dependencies as the preserved generic mode:

- `$build-persistent-sandbox` → `modes/generic/SKILL.md`
- `$build-persistent-sandbox/references/...` → `modes/generic/references/...`

Do not require a separately installed external generic skill when the unified repository already contains the vendored generic mode.

When a competitive or cultivation task needs the generic core, apply:

`root shared contract → modes/generic core contract/relevant references → selected domain mode contract/relevant references`

while keeping the selected primary domain vocabulary isolated.

## Root vs mode precedence

Use this precedence:

1. user's current operative request;
2. authoritative existing project/canon and migration constraints;
3. root shared invariants/living-sandbox contracts;
4. selected mode `SKILL.md`;
5. selected/generic mode references;
6. examples and presentation patterns.

If a shared root rule and a mode-specific rule appear to conflict, preserve the stricter authority/privacy/persistence requirement and document the conflict rather than silently dropping the mode behavior.

## Vendored parity

`vendor_manifest.json` records the source repositories, source commits, and expected Git tree SHAs for each vendored mode. Run:

```powershell
python -X utf8 scripts/audit_vendor_parity.py
```

before claiming that an updated unified skill still contains the source modes intact.

Tree parity proves byte-level preservation of the vendored source tree at the recorded commit. It does **not** prove behavioral routing; mandatory mode loading above addresses that second requirement.

## From-zero competitive route

The original competitive skill is layered on the generic persistent scaffold and did not contain its own scaffold script. For a new competitive package:

1. use the generic scaffold with domain ID `competitive_rules`;
2. apply `modes/competitive/assets/competitive_domain_profile.json` to the package domain profile;
3. include `modes/competitive/assets/draft_contract.schema.json` when draft/lineup mechanics are in scope;
4. run both generic and competitive validation relevant to the package.

Do not treat the absence of a standalone competitive scaffold as permission to skip the generic core.

## Narrow tasks

A narrow rules or repair task need not activate the full six-phase living-world lifecycle. It still reads its selected mode contract and the specific references required by the change.
