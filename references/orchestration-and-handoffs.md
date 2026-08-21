# Orchestration and Handoffs

Use this for multi-phase sandbox work so the human remains product owner and final approver rather than a manual message router.

## Preferred role split

When Orca, Muse Spark Contributor, and Codex are available:

- **Orca** owns repository/workspace discovery, task state, delegation, phase sequencing, evidence collection, and handoffs.
- **Muse Spark Contributor** is the primary implementer for substantive design, code, schemas, migrations, data work, tests, and repair.
- **Codex** is the independent final auditor. It may make only localized non-architectural fixes; broad changes return through Orca to the primary implementer.

Do not silently replace the requested primary implementer with Codex and then claim delegation occurred.

## Workspace policy

- Reuse a valid existing workspace when possible.
- Respect the user's declared workspace-root/drive policy before creating clones, worktrees, agent workspaces, build outputs, or project caches.
- For the Windows `D:\AI` workflow, default new workspaces to `D:\AI\<Project>_Workbench` and do not place project repositories, worktrees, agent workspaces, long-lived build/task directories, or configurable project caches on `C:\`.
- If the required workspace policy cannot be honored, report the blocker rather than silently using another drive.

## No-human-router rule

Load the full multi-phase plan once. Orca transfers reports, acceptance state, deferred work, and next-phase instructions between agents. Do not ask the user to paste the next phase or shuttle implementation reports between agents.

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

Final integrated handoff:
- `FINAL_ACCEPTANCE_PACKET.md`
- acceptance index
- canonical changed-file summary
- migrations/rollback notes
- test matrix and gameplay review
- remaining P0/P1 and known limitations
- release recommendation and next project

## Auditor small-fix boundary

A Codex fix is small only if it is localized and does not create a new subsystem, broadly change authority ownership, add cross-phase architecture, perform a broad data rewrite, or silently implement deferred scope. Larger work goes back to Muse Spark Contributor through Orca.

## Git/worktree discipline

Inspect repository status before staging. Do not include unrelated user changes by default. Record the actual repository root, branch, and workspace path in the implementation report.

## Independent acceptance

The implementer's self-assessment is not acceptance. Codex should inspect the actual diff, verify authority/versioning, rerun critical tests when possible, and mark each acceptance gate with evidence before authorizing the next phase.
