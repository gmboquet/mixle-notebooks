# Changelog

## 0.7.0 - 2026-07-10

### Changed (release-readiness verification pass, 2026-07-11)

- `tutorials/embedding_with_htsne`: reworked five more times the same day as the
  first 0.7.0 pass (protein-family embedding -> protein-binding recovery ->
  edit-distance head-to-head -> six-class binding atlas -> final cut, which
  drops the edit-distance baseline and refocuses on htsne's actual reason to
  exist: heterogeneous, incomplete records t-SNE cannot take). None of that
  churn was reflected in the execution manifest, which still described the
  first-pass version. Re-executed against the final tip and confirmed clean;
  the manifest and this changelog now describe the shipped notebook.
- Re-sampled 24 additional notebooks (all five top-level groups) against a
  clean `mixle==0.7.0` install to re-confirm the existing manifest's pass
  count still holds on the current tip; see `docs/notebook-execution-manifest.rst`.
- `README.md`'s notebook table still said "Four folders" and omitted
  `exploration_geoscience/` entirely (added when the folder was, but the
  top-level README wasn't updated to match, only the Sphinx catalog was).
  Fixed to five folders with current per-folder counts.

### Fixed (release-readiness verification pass, 2026-07-11)

- `requirements.txt`: removed `rapidfuzz`, added for an edit-distance baseline
  in an intermediate `embedding_with_htsne` draft that the final cut of the
  notebook no longer uses. Nothing in the repo imports it.
- `tutorials/model_parallel_estimation`: the live two-rank `torch.distributed`
  demo always silently failed and printed a misleading "could not form a
  process group here" message, blaming the environment. The actual cause was
  a script-generation bug -- one `from mixle.inference import seq_estimate`
  line inside the `textwrap.dedent()`-wrapped subprocess script was missing
  its leading indentation, which collapses `dedent`'s common-whitespace
  computation to nothing and leaves the generated script's first statement
  indented, an `IndentationError` at parse time in the subprocess. Fixed the
  indentation and, while there, dropped the hardcoded
  `/Users/grantboquet/codex/mixle` `sys.path`/`PYTHONPATH` workaround it
  didn't need (the subprocess already inherits `mixle` from the same
  interpreter's installed environment via `sys.executable`). Re-executed:
  the two-rank demo now genuinely runs and reports `OK`.
- `data_science/market_basket_ibp`: a committed output cell printed the
  release owner's resolved absolute data-directory path
  (`/Users/grantboquet/codex/mixle-notebooks/data/online_retail_ii`), baked in
  from whatever machine last executed the notebook before commit. Changed the
  diagnostic to print a repo-relative path (`data/online_retail_ii`) and
  re-executed to refresh all outputs.

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
