# Changelog

## 0.7.0 - 2026-07-10

### Added (second pass)

- Four `data_science` notebooks closing the remaining mixle 0.7.0 feature-coverage
  gaps, each executed against a clean `mixle==0.7.0` install:
  - `receipts_and_replay` - `ExecutionTrace` bit-identical replay (with tamper
    detection) and the `Receipt` object verified offline by `verify_receipt`.
  - `structured_neural_leaves` - `make_deep_set`, `make_monotonic_mlp`,
    `HamiltonianNet`, and `build_product_energy_net`: structure (permutation
    invariance, monotonicity, energy conservation) guaranteed by construction.
  - `verifiable_design_loop` - `doe.VerifiableOracle` + `optimize_under_oracle`,
    with the self-graded / no-oracle honesty guards.
  - `hvis_topology_and_streaming` - `nerve_report` / `component_tree` topology
    receipts, deterministic `model_map`, and `StreamingHvis` atlas placement.

### Changed (second pass)

- Reconciled two duplicated notebooks: removed the `applications/` copies of
  `crosshole_gpr_tomography` and `well_log_facies_hmm`, keeping the more complete
  `exploration_geoscience/` versions (which use the shared geoscience data/vis
  helpers) as canonical.
- Added `xlrd` to requirements (legacy `.xls` reader for the basalt loader).

### Fixed (second pass)

- `applications/radar_tomography`: replaced `np.cross` on 2-D vectors with the
  explicit 2-D cross product (NumPy 2.0 removed the 2-vector `np.cross`).


### Added

- Three `data_science` notebooks showcasing capabilities introduced in mixle
  0.7.0, each executed against a clean `mixle==0.7.0` install:
  - `agentic_system_facade` - the `mixle.system.System` facade (`answer` /
    `ingest` / `improve`), budget as a hard ceiling, auditable spend receipts,
    and named degraded modes.
  - `cross_modal_belief_transport` - cross-modal reasoning with structured
    belief nodes, premise-checked conditional transports, a belief walk with
    coverage checked by hop count, abstention, and task-sufficient projection.
  - `copulas_and_gated_mixtures` - the new `CopulaDistribution` (Sklar) and
    `GatedMixtureDistribution` (learned gate `p(k | z)`) families.
- Catalog section "mixle 0.7.0 Capability Showcase" describing the new
  notebooks.

### Changed

- Docs now target mixle 0.7.0 (`release`/`version` set to `0.7.0` / `0.7`).
- Incremental EM examples use the keyword call
  `inc.update(chunk, chunk_id=cid)` matching the current mixle API.

## 0.6.3 notebook documentation branch - 2026-07-08

### Added

- Sphinx docs for installation, package map, catalog, execution runbook,
  reproducibility policy, validation, troubleshooting, release notes, and
  security/data handling.

### Changed

- Notebook documentation now distinguishes smoke, validation, and manual tiers
  and records timeout, worker-count, skipped, blocked, and failed execution
  evidence.

### Fixed

- `docs/_build` is ignored for local Sphinx builds.

### Removed

- Nothing removed for this documentation pass.

### Known limitations

- A one-minute timeout is triage evidence only. Public release still needs an
  execution manifest and current notebook results for shipped or linked
  notebooks, with explicit reasons for exclusions.
