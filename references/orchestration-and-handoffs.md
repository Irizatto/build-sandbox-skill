# Orchestration and Handoffs

Use this for multi-phase sandbox work so the human remains product owner and final approver rather than a manual message router.

## Choose the lightest orchestration model that preserves evidence

Do not add an orchestration agent merely because one exists.

Two valid patterns are:

### A. Orchestrated multi-agent build

When the project genuinely benefits from persistent cross-agent routing and the user wants Orca in the loop:

- **Orca** owns repository/workspace discovery, task state, delegation, phase sequencing, evidence collection, and handoffs.
- **Muse Spark Contributor** is the primary implementer for substantive design, code, schemas, migrations, data work, tests, and repair.
- **Codex** is the independent final auditor. It may make only localized non-architectural fixes; broad changes return through Orca to the primary implementer.

### B. Direct single-owner implementation + independent audit

When the user wants one implementation owner and the project/workspace is already stable:

`Muse primary implementation → self-gate / handoff → STOP → Codex independent audit`

This is often lower-friction than inserting an orchestrator into a mature project.

In this mode:

- Muse owns baseline discovery, implementation, repair, tests, reports, and phase handoff;
- Muse does not call Codex during implementation unless the user explicitly authorizes it;
- the implementation handoff ends with `next_phase: null` when an independent audit is intended to be manually authorized afterward;
- Codex audits actual files/diffs/evidence rather than trusting Muse's PASS report;
- the user is not used as a repeated copy/paste router inside the implementation phase.

Do not silently replace the requested primary implementer with Codex and then claim delegation occurred.

## Workspace policy

- Reuse a valid existing workspace when possible.
- Respect the user's declared workspace-root/drive policy before creating clones, worktrees, agent workspaces, build outputs, or project caches.
- For the Windows `D:\AI` workflow, default new workspaces to `D:\AI\<Project>_Workbench` and do not place project repositories, worktrees, agent workspaces, long-lived build/task directories, or configurable project caches on `C:\`.
- If the required workspace policy cannot be honored, report the blocker rather than silently using another drive.

## No-human-router rule

Load the full multi-phase plan once when practical. Transfer reports, acceptance state, deferred work, and next-phase instructions through files/ledgers/handoffs rather than asking the user to shuttle giant prompts and reports repeatedly.

In Orca mode, Orca performs the routing.

In direct-Muse mode, Muse reads prior phase artifacts from the workspace and writes the next handoff itself; the user only authorizes major phase transitions or product decisions.

Only request user intervention for a genuine external blocker or a failed gate that requires a product decision.

## Phase ledger

Track:
- phase/task ID and assignee;
- dependencies and input versions;
- changed files;
- schema/migration state;
- tests and evidence;
- unresolved/deferred work;
- gate status;
- next handoff.

## Standard artifacts

Use phase-specific names:
- `PHASE_X_IMPLEMENTATION_REPORT.md`
- `PHASE_X_ACCEPTANCE.md`
- `PHASE_X_HANDOFF.json`

For research-only phases, also allow:
- `PHASE_X_BASELINE.md`
- `PHASE_X_GAP_AUDIT.md`
- `PHASE_X_SELECTION.md`
- `PHASE_X_REJECTION_DEFER_LIST.md`

Final integrated handoff:
- acceptance packet;
- acceptance index;
- canonical changed-file summary;
- migrations/rollback notes;
- test matrix and gameplay review;
- remaining P0/P1 and known limitations;
- release recommendation and next project.

## Implementer self-gate boundary

The implementer may produce a self-gate, but it must be explicitly labeled as self-assessment, for example:

`SELF_GATE_ONLY — NOT INDEPENDENTLY AUDITED`

A self-gate may say PASS for implementation completeness. It may not be treated as independent release acceptance.

## Auditor small-fix boundary

A Codex fix is small only if it is localized and does not create a new subsystem, broadly change authority ownership, add cross-phase architecture, perform a broad data rewrite, or silently implement deferred scope.

Small auditor fixes are appropriate for local trigger/key mistakes, small test defects, straightforward documentation/evidence mismatch, or similarly bounded issues.

If the audit finds a P0/P1 problem in authority, Canon, retrieval ownership, migration/save compatibility, direct playability, or context inflation, return targeted required fixes to the primary implementer rather than letting the auditor redesign the project.

## Git/worktree discipline

Inspect repository status before staging. Do not include unrelated user changes by default. Record the actual repository root, branch, and workspace path in the implementation report.

Never reset, stash, delete, overwrite, stage, or commit unrelated user work merely to produce a clean build report.

## Independent acceptance

The implementer's self-assessment is not acceptance.

An independent auditor should inspect the actual diff/files, verify authority/versioning, inspect test quality, rerun critical tests when possible, and mark each acceptance gate with evidence.

Do not count report prose as evidence when the claimed behavior is not exercised by an inspectable artifact/test.

For mature SillyTavern work, independent audit should pay particular attention to:

- canonical Tier A package integrity;
- optional Tier B fallback;
- Tier C harness claims vs player-facing implementation;
- actual/fidelity-documented context measurement;
- mutation-resistant tests rather than `assert(true)` placeholders;
- secret/knowledge leakage;
- inactive-world context scaling.
