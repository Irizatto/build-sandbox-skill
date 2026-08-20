# Evaluation and release gates

## Hard gates

Fail on invalid schema, duplicate stable ID, broken explicit reference, authority collision, undeclared domain vocabulary leakage, illegal mechanic transition, replay mismatch, private truth in a public packet, non-idempotent migration, unconditional context overflow, or unsupported release claims.

## Quality rubric

- causal coherence and canon integrity: 15;
- executable mechanics and counterplay: 15;
- persistent simulation and history: 15;
- context efficiency and knowledge safety: 15;
- actor and organization texture: 15;
- player agency, failure, and quiet states: 10;
- originality and domain fidelity: 10;
- packaging and usability: 5.

Do not convert this score into a community percentile without a declared comparison corpus.

## Mutation tests

Inject one defect at a time: duplicate ID, missing reference, forbidden-domain word, illegal transition, private key in a public packet, changed replay result, oversized packet, falsely validated manifest, and stale ruleset reference. Each mutation must produce a failing result.

## Scenario benchmarks

Run a minimal from-zero prompt, existing-canon expansion, algorithm-heavy rule module, long skip, quiet sequence, context load/unload cycle, knowledge challenge, and save/reload replay. For multi-model use, repeat representative scenarios per model profile and record settings, seed, hashes, failures, and human observations.

## Release status

- **Scaffold:** directories and contracts only.
- **Prototype:** one mechanic or slice runs.
- **Alpha:** integrated systems pass automated gates; human play remains.
- **Release Candidate:** migrations, packaging, and long-session tests are credible.
- **Stable:** sustained human use found no release-blocking defect.

