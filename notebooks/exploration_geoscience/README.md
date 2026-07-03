# Exploration Geoscience: AI / ML / UQ for finding things underground

A course on inferring the Earth — its resources and its history — from indirect, noisy, multi-modal data,
**with calibrated uncertainty as the deliverable**. It spans the data that exploration actually uses:
geophysics, well logs, geochemistry, geochronology, the stratigraphic and fossil record, tectonics and
deep-time Earth history — and the decisions they feed (oil, minerals, water, hazard).

Two principles run through every notebook:

1. **The library does the modelling.** Every model — a distribution, a mixture, a hidden Markov model, a
   Gaussian process or field, a PDE/eikonal/potential-field forward, a regularized inversion, a Bayesian-
   optimal design — is a call into [`mixle`](https://github.com/gmboquet/mixle) or
   [`mixle-pde`](https://github.com/gmboquet/mixle-pde). If a capability is missing, we add it to
   the library, not to the notebook.
2. **You can see the modelling.** Data loading is one call into [`_geodata`](_geodata.py); every figure is one
   call into [`_geoviz`](_geoviz.py); the modelling lines are marked `# --- MODEL ---`. A notebook reads
   **load → model → show**, so the method is on the page, not buried under 100 lines of matplotlib.

Real, openly-published data throughout; held-out or resolution-based validation; honest negatives.

## Curriculum

### Module 0 — Foundations · **start here**
- [**00_foundations**](00_foundations.ipynb) ✅ — the exploration inverse problem on a tiny worked example
  (6 data, 24 unknowns → an 18-dim null space → many exact fits → a regularized estimate *with* its ±2σ
  posterior → a decision read from the posterior, P=0.98 vs 0.23). Then the **five habits** the course practices
  (resolution-is-the-deliverable; accuracy ≠ calibration ≠ decision value; run the control / decline the
  unidentifiable; decisions need a calibrated probability *and* a value function; real data + honest negatives),
  each linked to where it's earned, and the **toolbox map**: `mixle` (densities, mixtures, HMMs, GPs/fields,
  inference/calibration, DoE/BO) + `mixle_pde` (eikonal / potential-field / geotherm+EASY%Ro forwards +
  `regularized_gauss_newton`).

### Module 1 — Geophysical imaging
| Notebook | Status | Methods |
|---|---|---|
| [crosshole_gpr_tomography](crosshole_gpr_tomography.ipynb) | ✅ | Real AM13 crosshole GPR → velocity → water content (Topp). The earned lesson: **resolution is the deliverable** — checkerboard + point-spread tests through the same operator show the tomogram recovers ~18% of true amplitude, strongly **anisotropic** (vertical 33% vs horizontal 18%), and the L-curve shows the regularizer (not the data) sets the texture. Honest resolution-qualified water map. |
| [magma_reservoir_gravity](magma_reservoir_gravity.ipynb) | ✅ | Real Laguna del Maule Bouguer gravity → a low-density (melt/hydrothermal) body. The earned core is **non-uniqueness made quantitative**: a depth–mass equivalence (a 2.5 km body re-fits as 6 km, mass ∝ depth²), a resolution test (depth biased deep & saturating; lateral ±250 m, mass ±40%), and regularization-as-choice (the prior alone moves the body 2.4 km). Constrained: position + order-of-magnitude mass; **not** depth. |
| [near_surface_joint_inversion](near_surface_joint_inversion.ipynb) | ✅ | Real co-located Schilthorn ERT + seismic refraction (Wagner et al. 2019). Derives the **cross-gradient** (shared boundaries, no petrophysical law); a controlled test (real geometry, known truth) proves + quantifies that coupling sharpens the **under-resolved** velocity (RMSE 0.79→0.53) and aligns structure (mismatch 0.09→0.03) while the well-resolved resistivity is unchanged; then the real joint inversion (mismatch 2.7→0.7). Honest about the straight-ray approximation. |
| electrical_resistivity | ⬜ | DC resistivity / ERT imaging and its honest amplitude limits. |

### Module 2 — The borehole: petrophysics & logs
| Notebook | Status | Methods |
|---|---|---|
| [well_log_facies_hmm](well_log_facies_hmm.ipynb) | ✅ | Real Hugoton-Panoma logs → net-pay decision. Walther's-law HMM (forward-backward) beats the per-foot classifier on blind wells AND removes the flicker — but is badly **over-confident** (ECE 0.45 vs 0.13); temperature scaling fixes it (→0.10) without touching accuracy, and the calibrated P(reservoir) makes the better completion decision. Accuracy ≠ calibration ≠ decision. |
| rock_physics_fluid_substitution | ⬜ | Gassmann fluid substitution, porosity/saturation inversion with UQ. |

### Module 3 — Geochemistry & provenance
| Notebook | Status | Methods |
|---|---|---|
| [geochemical_fingerprinting](geochemical_fingerprinting.ipynb) | ✅ | Real Vermeesch (2006) basalts → arc-vs-not (porphyry-Cu/Au) prospectivity, held out *by locality*. Derives compositional closure, then **runs the control**: raw-ppm is over-confident, but plain log-concentrations already match the full Aitchison log-ratio (clr/ilr) — the gain is the **log scale**, not the closure correction. Teaches *when* compositional geometry earns its keep; calibrated P(arc) is the deliverable. |

### Module 4 — Geochronology & age models
| Notebook | Status | Methods |
|---|---|---|
| [detrital_zircon_provenance](detrital_zircon_provenance.ipynb) | ✅ | Real Namib / Orange-River detrital-zircon U-Pb ages as a derived, quantified inverse question — *are the dunes purely recycled river sand?* `mixle.inference` permutation test + Benjamini-Hochberg FDR (11/14 reject), Wasserstein effect sizes with bootstrap CIs, and a proof that the mixing fraction is unidentifiable (so it is declined, not invented). |

### Module 5 — Deep time: the stratigraphic & fossil record
| Notebook | Status | Methods |
|---|---|---|
| [biostratigraphy_event_ordering](biostratigraphy_event_ordering.ipynb) | ✅ | Real PBDB Ordovician graptolites; `mixle` Kemeny/Mallows **consensus ranking** (RASC/CONOP core). Earned + quantified: **bootstrap over sections → a posterior on each event's rank** (some boundaries firmly placed, others coin-flips — the resolution of the biostratigraphy), and the consensus-beats-sections margin as a *tested* claim (Δ=4.6 pairwise errors, 95% CI excludes 0). Honest external-validation failure shown, not hidden. |
| paleoenvironment_fields | ⬜ | Reconstructing ancient climate/environment fields from proxies (shared GP/GMRF field, many proxies). |

### Module 6 — Tectonics & ancient Earth
| Notebook | Status | Methods |
|---|---|---|
| [basin_thermal_history](basin_thermal_history.ipynb) | ✅ | Real IHFC Global Heat Flow Database (US west); the subsurface thermal field → geothermal fairway + petroleum oil window. The lesson: a smooth-GP heat-flow map fails cross-validation (no skill, 36% coverage) because the variogram is 96% nugget — honest UQ needs aggregation, and the decision is regional + probabilistic. Modelling: `mixle` GP + `mixle_pde` (`geotherm`, `easy_ro`). |

### Module 7 — Decision under uncertainty
| Notebook | Status | Methods |
|---|---|---|
| [where_to_drill_value_of_information](where_to_drill_value_of_information.ipynb) | ✅ | The capstone, on the real calibrated heat-flow cells: derive EVPI / EVSI decision theory, compute the value of information in dollars, and show the earned punchline — the decision-value-optimal survey (EVSI) has ~0/8 overlap with "drill the hottest" or "sample the most uncertain" (`mixle.doe.alm_scores`). Information ≠ decision value. |

### Module 8 — Minerals: resource estimation
| Notebook | Status | Methods |
|---|---|---|
| [mineral_exploration_kriging](mineral_exploration_kriging.ipynb) | ✅ | Real Babbitt Cu-Ni drilling (399 holes, Duluth Complex; Patelke/NRRI). Desurvey + composite the assays, derive the **variogram** and **ordinary kriging** (= a `mixle` GP, range/sill/nugget fit by marginal likelihood), then earn the central pitfall of resource estimation: **kriging estimates the mean, which smooths** (the kriged block model holds only ~48% of the data's grade variance). Tonnage/grade above a cutoff from the kriged-mean map vs from **conditional simulations** disagree by a cutoff-dependent sign — kriged-mean **over-states** ore tonnage +16% at the 0.30% cutoff but **under-states** it −42% to −74% at higher cutoffs, and only the simulations carry a P10-P90 band. Read the resource off the simulations, not the smooth map. |

✅ done · ⏳ exists, to port into the course architecture · ⬜ planned

## Running

```bash
cd notebooks/exploration_geoscience
jupyter lab            # the _geoviz / _geodata helpers import locally; data lives under ../../data
```

Each notebook needs `mixle` and (for the imaging/PDE notebooks) `mixle-pde`. Datasets are real and
openly licensed; see each notebook's references.
