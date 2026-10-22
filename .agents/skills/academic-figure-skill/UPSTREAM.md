# Upstream attribution

- Project: `academic-figure-skill`
- Author: Tingxi Yu
- Source: https://github.com/TingxiYu/academic-figure-skill
- Source commit: `1df9940dd01ac939f072b12fe28d6353b79b90f9`
- License: Apache License 2.0

This project-level installation preserves `SKILL.md`, `references/`,
`scripts/`, `assets/`, and `install/codex/` from the upstream commit. The
accompanying `LICENSE` file is copied from the upstream repository.

## Verified upstream limitation

At the pinned commit, `scripts/run_ab_tests.py` contains invalid Python
identifiers with hyphens and does not compile. The file is preserved unchanged
for source fidelity. The remaining Python files compile successfully, and the
reference-integrity, QA-coverage, trigger-benchmark, and module-discovery checks
pass.
