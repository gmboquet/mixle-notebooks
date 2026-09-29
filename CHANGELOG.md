# Changelog

## 0.8.3 - Unreleased

The corpus tracks the mixle 0.8.3 pre-release cycle: `requirements.txt` installs `mixle`, `mixle-sim` and
`mixle-physics` from their `release/0.8.3` branches (`mixle` at `0.8.3rc1` until the final cut). No notebook
changed; the retained outputs are the 2026-09-15 execution on the final 0.8.2 candidate wheel.

## 0.8.2 - 2026-09-17

### Fixed

Repairs for the notebook findings the ten adversarial reviews of the 0.8.1 candidate deferred to
this release (`mixle`'s `release-checklists/0.8.2-followups.md`), all re-executed against the
repaired library.

- `applications/knowledge_graph_umls` reads the tail conditional it says it is reporting.
  `KnowledgeGraphDistribution.log_density` is the JOINT `log p(h, r, t)`, so comparing it with a
  `-log(entities)` tail baseline made the model look worse than uniform (-12.118 against -4.905)
  when the conditional it meant is -3.384, well above it. The cell now calls `tail_log_posterior`
  (P07-F06).
- `applications/bayesian_tweet_rhythm`, `option_pricing_and_implied_volatility` and
  `fake_news_detection` fit the distributions they compare. A distribution written with all-constant
  parameters has nothing to fit and `.fit()` returns it unchanged, so the printed likelihoods were
  those of the placeholder values -- which made a fitted-Poisson-vs-negative-binomial comparison
  meaningless and stated outright that a Student-t log-likelihood of -1554 "beats" a Gaussian -527.
  The parameters the estimator moves are now `free`; the Student-t's degrees of freedom stays a
  named constant, because that estimator is a fixed-df moment fit and mixle now says so (P07-F03).
- `applications/baseball_hierarchical_shrinkage` samples its grouped Bernoulli-Beta posterior
  instead of falling back to the grid: the library path it needs works again (P07-F04).
- `applications/retail_trend_statespace` fits its local-level model to convergence and states what
  "matches" means: the two smoothers agree to 7e-15 over 739 days, and the whole disagreement is a
  thirty-day initial-state transient, not the 3.3 an under-budgeted fit produced (P07-F05).
- `architecture_studies/ppl_scaling_vs_pyro_stan`'s takeaway describes a constant factor to be
  re-measured rather than "1-2 orders of magnitude", because the gradient baseline's own backend has
  become several times faster since the stored run; the conjugate-vs-sampling gap, which is about
  the method rather than either implementation, keeps its "hundreds of times". `engine_benchmarks`
  says plainly that numba does not always beat numpy on an already-vectorized E-step. Every
  architecture study's stored timings are this host's (P07-F11).
- `data_science/heterogeneous_mixed_type_modeling` compares its heterogeneous and numeric-only
  clusterings at the SAME cluster budget. Letting the DP choose its own number for each input meant
  the comparison measured how many clusters each input made it want: numeric-only "beat" the full
  record 0.759 to 0.658. Controlled, the full record wins 0.883 to 0.661, and the per-field ablation
  is reported beside the group ablation, which is what shows the non-numeric fields to be jointly
  worth 0.331 and individually redundant (P08-F09).
- `data_science/latent_models_in_practice` reads its one-shot fit's own receipt. That fit lands a
  nested component with a variance of 1e-13 carrying 0.2% of the weight; the library now discloses
  it, the notebook prints the effective rows each component won (0.71 for two parameters), and the
  prose makes it the lesson the section is there to teach (P08-F10).

## 0.8.0 - Unreleased

### Added

- `data_science/newton_continuation_and_folds` - a tutorial for `mixle-pde`'s new
  `continuation` module (MP-F2): `natural_continuation` steps a parameter directly and
  fails honestly at a fold (a typed `failure_reason`, never a fabricated point), while
  `arclength_continuation` (Keller 1977, pseudo-arclength) traces through the same fold
  onto the far branch. Worked on the classic Bratu equation, with the traced fold checked
  against a closed-form reference and the discretization gap shown shrinking under mesh
  refinement.

### Changed

- `requirements.txt`: pin `mixle-pde` to `release/0.8.0` commit `bcb91b1` so
  `continuation.py` installs; it is not yet on a PyPI release or on `mixle-pde`'s `main`
  branch.

### Fixed

- Forward-ported four fixes that landed on `release/0.7.0` but never made it to
  `release/0.8.0`:
  - `data_science/cifar10_conv_net_and_exact_head`: `load_dataset("cifar10")` used a
    script-based dataset id the Hub has retired; switched to the maintained mirror
    `uoft-cs/cifar10` (schema-identical; re-verified it loads from an empty
    `HF_HOME` and the notebook re-executes clean end to end).
  - `data_science/market_basket_ibp`: a committed output cell printed the resolved
    absolute data directory from whichever machine last executed the notebook;
    now prints a repo-relative path.
  - `tutorials/model_parallel_estimation`: the generated two-rank
    `torch.distributed` subprocess script had one `from mixle.inference import
    seq_estimate` line missing its indentation, which broke `textwrap.dedent()`
    and crashed every run with a swallowed `IndentationError` misreported as an
    environment problem; fixed the indentation and dropped the hardcoded
    `/Users/.../mixle` `sys.path`/`PYTHONPATH` workaround it didn't need.
  - `requirements.txt`: dropped the unused `rapidfuzz` dependency (added for an
    edit-distance baseline that was later dropped from `embedding_with_htsne`;
    nothing in the repo imports it).
- `README.md`/`LICENSE`: the notebook-count table still said "Four folders" and
  omitted `exploration_geoscience/` entirely, with per-folder counts stale since
  before that folder was added; refreshed against the real tree (12/75/20/11/6 =
  124 notebooks across five folders). `LICENSE` named an unrelated institutional
  copyright holder left over from a template; corrected to match the convention
  used by the rest of the `mixle` family.
- `requirements.txt`: added the missing `datasets` dependency. Nothing installed
  it transitively (it isn't a hard dependency of `transformers`), so
  `cifar10_conv_net_and_exact_head` (and only that notebook) failed with
  `ModuleNotFoundError: No module named 'datasets'` on a clean environment; this
  predated the 0.7.0 gap above and affected both release branches.

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
