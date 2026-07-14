# pillar_validation/ — reproducible validation notebooks (one per pillar)

Each notebook here reproduces one pillar's headline exec-plan Definition of Done, end to end, on the
small fixtures committed under [`data/pillar_validation/`](../../../data/pillar_validation): fit or
invert, compute the pillar's IC-8 `DerivedQuantity` (or equivalent decision output), plot the
calibration/UQ diagnostic so the reader *sees* the uncertainty quantification rather than just a
number, and finish with an explicit `assert` cell that restates the same numeric threshold the
pillar's own exec DoD asserts. A broken pillar fails the notebook, not just a library test.

Every notebook is deterministic (fixed seeds throughout) and network-free — it loads only the
committed fixture, never live data.

| Notebook | Pillar | Reproduces | Headline numeric DoD |
|---|---|---|---|
| [calibration_A](calibration_A.ipynb) | A — subsurface inversion | A5 decision-quantity UQ | `prob_exceed` 90% CI empirical coverage ≥ 0.85 |
| [production_H](production_H.ipynb) | H — mine planning | H4 stochastic/robust optimization | CVaR-averse plan's held-out expected value ≥ deterministic-mean plan's, CVaR strictly better |
| [economics_J](economics_J.ipynb) | J — economic synthesis | J6 priced, risk-adjusted objective | raising carbon price removes the highest-emission blocks; a no-mine polygon removes exactly its enclosed blocks |
| [health_K](health_K.ipynb) | K — health risk | K3 dose-response models | dose-response coverage ≥ 0.88; CI widens with exposure variance |
| [climate_L](climate_L.ipynb) | L — climate | L7 downscaling + extremes | downscaled 20-yr return level within 5% of the reference; `climate_hash` is 64-hex |
| [biodiversity_N](biodiversity_N.ipynb) | N — biodiversity | N1 species-distribution model | held-out IPP log-likelihood beats the homogeneous null; 90% CI coverage ≥ 0.85 |
| [simulation_P](simulation_P.ipynb) | P — forward simulation | P1 unified `simulate` tool | content-hashed result ref is 64-hex and round-trips |

## A note on what's real vs. reference-implemented

Several of these pillars' own Wave 1–3 modules had not yet landed on `release/0.8.0` in the sibling
`mixle`/`mixle-pde` checkouts at the time these notebooks were written (`mixle.reason.posterior_protocol`,
`mixle_pde.decision_quantities`, `mixle.stochastic_opt`, `mixle.analysis.objective`,
`mixle.analysis.health_risk`, `mixle_pde.climate_downscale` + `mixle.analysis.quantile_mapping`,
`mixle.analysis.sdm`, `mixle_pde.simulation_service` + `mixle_pde.io.artifacts`). Every notebook tries the
real import first and transparently uses it once it merges; until then each falls back to a small
reference implementation of that module's exact frozen algorithm, so the notebook is reproducible today.

Where the *underlying* primitive already exists in the library, the notebooks use it directly rather than
reimplementing it: `mixle.relations.branch_and_bound_milp` (the block-selection MILPs in `production_H` and
`economics_J`), `mixle.analysis.extreme.peaks_over_threshold`/`return_level` (the POT/GPD extremes in
`climate_L`), and `mixle.stats.processes.inhomogeneous_poisson.InhomogeneousPoissonProcessDistribution` +
`mixle.analysis.kriging.calibrate_variance` (the point-process likelihood and variance recalibration in
`biodiversity_N`), and `mixle_pde.dynamics.AdvectionDiffusionOperator` (the transport forward in
`simulation_P`).

## Running

```sh
python -m pytest --nbmake notebooks/applications/pillar_validation/ -q
```

`conftest.py` at the repo root puts the sibling `mixle`/`mixle-pde` source checkouts on `PYTHONPATH` for
the notebook kernels when this repo is checked out next to them (a no-op after a normal
`pip install -r requirements.txt`).
