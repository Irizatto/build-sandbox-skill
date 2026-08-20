# Competitive evaluation

## Hard failures

- invalid or unreachable phase;
- duplicate phase ID;
- illegal actor or action accepted;
- unavailable target selected;
- final lineup violates role or size requirements;
- old-version relation used without explicit compatibility;
- hidden preparation exposed publicly;
- save/reload changes committed state;
- recommendation presented as official legality;
- unrelated domain vocabulary in ordinary competitive content.

## Required scenarios

Test a complete legal draft, every illegal action family, incomplete termination, simultaneous conflict, swap, substitution, series carry-over, administrative override, version change, hidden-information projection, deterministic replay, and bounded context retrieval.

Use mutation tests for a missing phase target, duplicate selection, stale relation, private leak, and changed event hash.

