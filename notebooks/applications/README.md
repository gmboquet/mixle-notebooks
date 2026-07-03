# applications/ — real-world problems

Worked examples where the domain problem is the point: each is self-contained, modeling-dense (plotting
kept to a small fraction of the code), run top to bottom on real data, and closing with references and
exercises.

## Natural language & sequences

| Notebook | Domain — methods |
|---|---|
| [generative_title_decoding](generative_title_decoding.ipynb) | Generative sequence decoding on real NeurIPS titles — the decoding-strategy taxonomy (greedy, beam, sampling, temperature, top-k/nucleus), exact and constrained top-k enumeration, n-gram language models with Kneser-Ney smoothing and perplexity, and minimum-Bayes-risk decoding. |
| [machine_translation_alignment](machine_translation_alignment.ipynb) | Statistical word alignment for machine translation — IBM Models 1-5 and HMM alignment by EM, alignment error rate, phrase extraction and a phrase-based decoder scored by BLEU, and the line from latent alignment to neural attention. |

## Networks, graphs & misinformation

| Notebook | Domain — methods |
|---|---|
| [knowledge_graph_umls](knowledge_graph_umls.ipynb) | Knowledge-graph embedding and reasoning on the UMLS biomedical graph — TransE/DistMult/ComplEx/RotatE scoring, negative-sampling training, filtered MRR/Hits@k, conformal completion sets, ensemble epistemic uncertainty, and an AMIE rule-mining baseline. |
| [malware_certificate_embedding](malware_certificate_embedding.ipynb) | Model-based embeddings of structured TLS-certificate records — per-field posteriors as affinities, t-SNE/UMAP layout, and malware-family attribution measured by held-out purity. |
| [fake_news_detection](fake_news_detection.ipynb) | Misinformation detection across content, source, and propagation (PolitiFact) — naive Bayes, Fightin'-Words log-odds, Beta-Binomial source credibility, a negative-binomial cascade model, a modularity echo-chamber test, and calibrated fusion. |
| [social_fake_news_detection](social_fake_news_detection.ipynb) | Network science and diffusion for misinformation (FakeNewsNet graph) — scale-free degree and the friendship paradox, a generative sharer-set classifier, spectral communities, PageRank, independent-cascade and SIR thresholds, and influence maximisation. |

## Spatial & temporal point processes

| Notebook | Domain — methods |
|---|---|
| [mineral_exploration_kriging](mineral_exploration_kriging.ipynb) | 3-D geostatistics for mineral resource estimation — a tilted porphyry-copper orebody from angled drill holes: lognormal grades, directional variograms and geometric **anisotropy**, **anisotropic 3-D kriging = Gaussian-process regression** (`mixle.analysis`), leave-one-*hole*-out validation and kriging-variance **calibration**, **conditional simulation** and the grade–tonnage curve with risk, **multi-modal fusion** of a dense induced-polarisation survey with sparse drilling on one anisotropic latent field (`mixle.ppl.fit_field`, `AnisotropicRBF`), and **value-of-information** drill targeting. |
| [geospatial_tweet_clusters](geospatial_tweet_clusters.ipynb) | Spatial statistics and point processes on UK geo-tweets — complete-spatial-randomness tests, Ripley's K/L, kernel intensity, DP-Gaussian and Thomas / log-Gaussian-Cox cluster models, kriging, Moran's I, and the spatial scan statistic. |
| [bayesian_tweet_rhythm](bayesian_tweet_rhythm.ipynb) | Point processes and event-rate modelling on geo-tweets — Gamma-Poisson rates, inhomogeneous and Gaussian-process intensities, renewal hazards, uni- and multivariate Hawkes self-excitation, change-points, and a spatio-temporal Knox test. |
| [behavioral_anomaly_detection](behavioral_anomaly_detection.ipynb) | Anomaly detection on user-process logs — robust univariate theory, the Mahalanobis envelope, mixture density, order-aware sequence models, extreme-value thresholds, conformal false-alarm guarantees, and detector fusion. |

## Hierarchical & state-space modeling

| Notebook | Domain — methods |
|---|---|
| [baseball_hierarchical_shrinkage](baseball_hierarchical_shrinkage.ipynb) | Shrinkage and hierarchical Bayes — Stein / James-Stein, empirical Bayes, full-Bayes MCMC, DP mixtures of abilities, mixed-effects regression, model comparison, and the decision theory of ranking. |
| [radon_mixed_effects](radon_mixed_effects.ipynb) | Multilevel / mixed-effects modelling (Gelman-Hill radon) — varying intercepts and slopes, variance components and the ICC, group-level predictors, the ecological fallacy, the funnel, and nested three-level pooling. |
| [retail_trend_statespace](retail_trend_statespace.ipynb) | State-space models (UCI Online Retail II) — the Kalman filter and RTS smoother from scratch, structural level/trend/seasonal models, dynamic regression, the ensemble Kalman filter, and Markov regime-switching. |

## Quantitative finance

| Notebook | Domain — methods |
|---|---|
| [stock_portfolio_optimization](stock_portfolio_optimization.ipynb) | Portfolio construction with a mixle return model at the spine — Gaussian vs heavy-tailed **Student-t** fits, the efficient frontier from a mixle covariance, **Ledoit-Wolf shrinkage** (`LedoitWolfEstimator`, added to the library here), **Bayesian returns / Black-Litterman** via a conjugate Normal-Inverse-Wishart posterior, **regimes** from a `MixtureEstimator`, **VaR/CVaR by sampling the fitted model**, frontier uncertainty from posterior `(μ,Σ)` draws, and a cost-aware backtest; scipy only optimises. |
| [option_pricing_and_implied_volatility](option_pricing_and_implied_volatility.ipynb) | Derivative pricing, hedging, and risk — Black-Scholes and the Greeks, delta/gamma hedging, Monte Carlo, Longstaff-Schwartz American options, the SVI implied-vol surface, Heston and Merton-jump models, and VaR / expected shortfall. |

## Physics-based inverse problems

| Notebook | Domain — methods |
|---|---|
| [oil_exploration_decision](oil_exploration_decision.ipynb) | A posterior over the complete 3-D subsurface by **multiphysics, multimodal, PDE-constrained joint inversion**, rendered as 3-D volumes and a probabilistic ensemble. One latent porosity field (real Hugoton-Panoma rock physics) is coupled to the velocity and density different instruments see; each modality is a forward operator on it — a **Helmholtz wave-equation PDE** (differentiable `sparse_solve`) + Born operator for seismic, a **Newtonian potential** for gravity, wells, and a tomography estimate. A closed-form **joint Gaussian posterior** fuses them (information adding in precision space); we then **draw an ensemble of 3-D earths**, render the per-voxel **P(pay) probability volume**, cluster the realizations into **geological scenarios with probabilities** (pessimistic/base/optimistic, each a 3-D reconstruction) with a P10/P50/P90 pay-volume distribution, and make a **Bayesian-optimized** next-well decision (`mixle.doe`) by probability of pay. |
| [synthetic_aperture_sonar](synthetic_aperture_sonar.ipynb) | Acoustic signal processing — the wave equation, matched filtering, beamforming, the synthetic aperture, and Bayesian inverse imaging that reads interior compartments and their materials. |
| [radar_tomography](radar_tomography.ipynb) | Microwave / radar tomography and inverse scattering — the Helmholtz forward model, the Born approximation, k-space coverage, and Bayesian full-wave inversion with calibrated uncertainty. |
| [seismic_full_waveform_inversion](seismic_full_waveform_inversion.ipynb) | Seismic inversion for oil exploration — Gassmann rock physics, a 3-D earth model, the frequency-domain Helmholtz forward (adjoint `sparse_solve`), Born-linearized Bayesian inversion, oil-in-place volumetrics, and 4-D monitoring. |
| [flow_inversion](flow_inversion.ipynb) | Data assimilation and flow inversion — the Navier-Stokes forward model, Bayesian initial-state inversion through the time loop, the reversibility horizon, sparse-sensor observability, and viscosity estimation. |
| [near_surface_joint_inversion](near_surface_joint_inversion.ipynb) | Multimodal near-surface geophysics — one porosity field seen by **ground-penetrating radar**, seismic, and **ERT** through different petrophysics; crosshole/surface **traveltime tomography**, **petrophysical joint inversion** (the fused image beats either method alone), the **DC-resistivity** elliptic forward and its honest amplitude-biased resolution, and **cross-gradient** structural coupling of GPR + ERT. Built on a geophysical inversion engine (`mixle_pde.geophysics`: `dc_resistivity`, `straight_ray_operator`, `regularized_gauss_newton`, `cross_gradient`/`joint_inversion`) added for the purpose. |
| [well_log_facies_hmm](well_log_facies_hmm.ipynb) | Formation evaluation from **real wireline logs** (the SEG-2016 Hugoton-Panoma dataset) — per-facies multivariate-Gaussian emissions, a **stratigraphic hidden Markov model** (Walther's law → a sticky facies transition matrix) that decodes the most likely *sequence* of rock and beats independent classification by ~25% macro-F1 on two fully **blind wells**, **forward-backward posteriors** as a probabilistic facies log (with an honest over-confidence/calibration check), and **Gaussian-process imputation** of the missing photoelectric log with uncertainty. Real data, held-out validation. |
| [magma_reservoir_gravity_inversion](magma_reservoir_gravity_inversion.ipynb) | 3-D **gravity inversion** of a **real Bouguer survey** (Laguna del Maule, an actively inflating volcano; Miller et al. 2016) for subsurface density — the linear point-mass forward, **non-uniqueness** made explicit, and the **Li-Oldenburg depth weighting** that moves the recovered low-density **magma reservoir** from a surface-glued artifact to a coherent body at ~6 km (91% variance explained), with a **resolution test** (point-spread function) as the honest uncertainty statement. Built on the geophysics engine (`gravity_point_sensitivity`, `depth_weighting`, `regularized_gauss_newton`). |
| [crosshole_gpr_tomography](crosshole_gpr_tomography.ipynb) | **Crosshole GPR traveltime tomography** on the **real Arrenæs AM13** field dataset (Looms et al. 2010, 702 first-arrival traveltimes between two boreholes) — the **eikonal** (bending-ray) forward by a numba fast-sweeping solver, **nonlinear** regularized Gauss-Newton inversion with the ray-backtraced Jacobian (fits the data to the 0.8 ns noise floor), a straight-ray comparison showing when bending matters, and **Topp's-equation** conversion of the velocity image to a water-content (moisture) image. Built on the geophysics engine (`eikonal_traveltime`, `traveltime_tomography`). |
