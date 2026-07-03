# data_science/ — a course in probabilistic data science

A self-contained course, ordered foundations to capstone. Each notebook explains a technique and its
theory, evaluates it on real or illustrative data, runs end to end, and finishes with exercises.

## Module 1 — Estimation foundations

| # | Notebook | What it covers |
|---|---|---|
| 1 | [mle_and_sufficient_statistics](mle_and_sufficient_statistics.ipynb) | What MLE optimizes, why exponential-family fits depend on the data only through sufficient statistics (= mixle's accumulators), and the consistency / asymptotic-normality guarantees. |
| 2 | [exponential_families_and_conjugacy](exponential_families_and_conjugacy.ipynb) | The exponential-family form that unifies most distributions: sufficiency, MLE as moment matching, and conjugacy as addition in statistic-space. |
| 3 | [em_and_map_strategies](em_and_map_strategies.ipynb) | EM vs gradient maximum-likelihood, MAP bias-variance on small data, and what alternative E-steps (annealed, hard) buy and cost. |
| 4 | [bootstrap_and_uncertainty](bootstrap_and_uncertainty.ipynb) | Confidence intervals for any estimate by resampling: the bootstrap vs the CLT formula, and percentile intervals for medians, ratios, and fitted parameters. |
| 5 | [model_selection_and_cross_validation](model_selection_and_cross_validation.ipynb) | Why training fit overfits, and AIC/BIC, k-fold cross-validation, and the one-standard-error rule for choosing complexity. |

## Module 2 — Density estimation & clustering

| # | Notebook | What it covers |
|---|---|---|
| 6 | [density_estimation_mixtures_vs_kde](density_estimation_mixtures_vs_kde.ipynb) | Parametric mixtures vs nonparametric KDE for estimating a density; the shared bias-variance knob (component count ≈ bandwidth), tuned by held-out likelihood. |
| 7 | [gaussian_mixtures_in_depth](gaussian_mixtures_in_depth.ipynb) | The practical traps of fitting GMMs: initialization & local optima (k-means seeding), label switching, choosing K with BIC, and the covariance-collapse singularity. |
| 8 | [model_based_clustering_evaluation](model_based_clustering_evaluation.ipynb) | Clustering as mixture fitting: hard vs soft assignment and confidence, and evaluating clusters with ARI/NMI (labels) and silhouette (no labels). |
| 9 | [heterogeneous_mixed_type_modeling](heterogeneous_mixed_type_modeling.ipynb) | One `Composite` model over numbers, categories, counts, sets, and sequences; an automatic DP mixture clusters records using every field at once. |
| 10 | [conjugate_and_nonparametric_bayes](conjugate_and_nonparametric_bayes.ipynb) | Conjugacy as posterior inference, NormalGamma regularization on small samples, and Dirichlet-process mixtures that infer their own complexity. |

## Module 3 — Distributions for special data

| # | Notebook | What it covers |
|---|---|---|
| 11 | [count_data_overdispersion](count_data_overdispersion.ipynb) | Poisson's mean=variance assumption, detecting overdispersion via the index of dispersion, and the negative binomial fix (plus zero-inflation). |
| 12 | [directional_statistics](directional_statistics.ipynb) | Data on circles and spheres: why the linear mean fails, the von Mises distribution for angles, and von Mises-Fisher for unit vectors. |
| 13 | [heavy_tails_and_survival](heavy_tails_and_survival.ipynb) | Survival and hazard functions, the Weibull shape as the aging story, right-censoring and the censored likelihood, and heavy-tailed (Pareto) risk. |

## Module 4 — Bayesian inference & workflow

| # | Notebook | What it covers |
|---|---|---|
| 14 | [bayesian_workflow_predictive_checks](bayesian_workflow_predictive_checks.ipynb) | The Bayesian workflow's self-checks: prior predictive, posterior predictive (catching a bimodality misfit), and credible-interval calibration. |
| 15 | [hierarchical_partial_pooling](hierarchical_partial_pooling.ipynb) | Complete vs no vs partial pooling: shrinkage toward a learned population mean, why small groups borrow strength, and the measurable error win. |
| 16 | [mcmc_uncertainty_quantification](mcmc_uncertainty_quantification.ipynb) | MH vs HMC mixing, effective sample size, conjugate anchoring, and posterior-predictive uncertainty. |
| 17 | [variational_inference_vs_mcmc](variational_inference_vs_mcmc.ipynb) | Two routes to a posterior: MCMC (exact, slow) vs variational inference (fast, overconfident), the ELBO, mean-field vs full-rank, and when to use which. |
| 18 | [constrained_inference](constrained_inference.ipynb) | Encoding domain knowledge as constraints: inequality (identifiable mixtures), soft equality with a penalty knob, monotone/convex shape constraints, and physics-informed `ode_residual` fitting. |

## Module 5 — Design of experiments & optimization

| # | Notebook | What it covers |
|---|---|---|
| 19 | [experimental_designs](experimental_designs.ipynb) | Choosing a fixed batch of input points up front: space-filling designs (LHS, maximin, Sobol, Halton) and model-based D/A/I-optimal designs that minimize parameter/prediction variance. |
| 20 | [bayesian_optimization](bayesian_optimization.ipynb) | Minimizing an expensive black-box in few evaluations: a GP surrogate plus an acquisition function (EI/PI/UCB), beating random search, and the explore/exploit tradeoff. |
| 21 | [sequential_design_for_small_samples](sequential_design_for_small_samples.ipynb) | The precious-evaluation regime: BO's sample efficiency, the ask-tell BayesianOptimizer (lab in the loop), and diverse batch proposals for parallel experiments. |
| 22 | [constrained_and_multiobjective_optimization](constrained_and_multiobjective_optimization.ipynb) | Real optimization: constrained BO (feasibility-weighted acquisition) and multi-objective optimization mapping the Pareto front of competing-objective trade-offs. |
| 23 | [adaptive_clinical_trials](adaptive_clinical_trials.ipynb) | Sequential design where the experiment is treating patients: Thompson-sampling response-adaptive randomization on Beta-Bernoulli arms, and Bayesian early stopping. |

## Module 6 — Supervised learning & detection

| # | Notebook | What it covers |
|---|---|---|
| 24 | [regression_and_glms](regression_and_glms.ipynb) | One linear predictor, three responses: linear / logistic / Poisson regression as GLMs (identity / logit / log link), and reading coefficients on the link scale. |
| 25 | [naive_bayes_text_classification](naive_bayes_text_classification.ipynb) | The generative classifier: multinomial naive Bayes on Wikipedia categories, the (false but robust) independence assumption, and the most discriminative words. |
| 26 | [classification_metrics_and_calibration](classification_metrics_and_calibration.ipynb) | Why accuracy misleads under imbalance: confusion matrix, ROC/AUC, precision-recall, and calibration (reliability diagrams) — ranking vs honest probabilities. |
| 27 | [anomaly_detection](anomaly_detection.ipynb) | Anomaly = low probability under a model of normal: density-based outlier scoring (−log p(x)), thresholds, ROC/AUC, and the heterogeneous-record payoff. |

## Module 7 — Sequences & time series

| # | Notebook | What it covers |
|---|---|---|
| 28 | [markov_chains_for_sequences](markov_chains_for_sequences.ipynb) | First-order Markov chains on text: transition structure, generating sequences, and the stationary distribution (the PageRank computation). |
| 29 | [hmm_from_scratch](hmm_from_scratch.ipynb) | The three HMM algorithms in NumPy — forward-backward, Viterbi, Baum-Welch — cross-checked against mixle's HMM. |
| 30 | [language_detection_hmm](language_detection_hmm.ipynb) | A conditional HMM with shared emission states detecting language from text (the Iliad in three languages). |
| 31 | [state_space_filtering](state_space_filtering.ipynb) | Continuous latent state over time: the Kalman filter, local-level vs AR(1), filtering vs smoothing, and forecasting with growing uncertainty. |
| 32 | [change_point_segmentation](change_point_segmentation.ipynb) | Detecting regime shifts two ways: an HMM decoded by Viterbi, and exact dynamic-programming segmentation under a penalty. |

## Module 8 — Structure, dependence & graphs

| # | Notebook | What it covers |
|---|---|---|
| 33 | [information_theory_in_practice](information_theory_in_practice.ipynb) | Entropy, KL divergence (and its asymmetry), and mutual information — with MI-based feature selection that catches nonlinear dependence correlation misses. |
| 34 | [character_models_chow_liu](character_models_chow_liu.ipynb) | Chow-Liu dependency trees vs Markov chains and mixtures of trees for character-level word modeling, in bits/letter. |
| 35 | [networks_and_community_structure](networks_and_community_structure.ipynb) | Random dot-product graphs: latent node positions, recovering communities by clustering the fitted positions (the latent-geometry view of networks). |
| 36 | [ranking_and_combinatorial_models](ranking_and_combinatorial_models.ipynb) | Distributions over combinatorial objects: Plackett-Luce and Mallows rankings, spanning trees, matchings, and random dot-product graphs — sampling, MLE recovery, and exact enumeration. |

## Module 9 — Latent-variable & topic models

| # | Notebook | What it covers |
|---|---|---|
| 37 | [latent_models_in_practice](latent_models_in_practice.ipynb) | Fitting and evaluating mixtures/HMMs/LDA with model selection, validation-LL convergence, component-trajectory diagnostics, and imputation. |
| 38 | [topic_modeling_plsi](topic_modeling_plsi.ipynb) | Probabilistic latent semantic indexing as 'LDA minus the prior' — overfitting and the transductive limitation that motivate going Bayesian. |
| 39 | [topic_modeling_lda](topic_modeling_lda.ipynb) | LDA and coupled conditional LDA on a Wikipedia corpus: the generative model, variational EM, topic interpretation, and held-out retrieval. |
| 40 | [learning_stop_words](learning_stop_words.ipynb) | Learning stop words from corpus behavior via keyed estimation and shared mixture components; an information-theoretic feature-selection task. |
| 41 | [market_basket_ibp](market_basket_ibp.ipynb) | The finite Indian buffet process on UCI Online Retail II: sparse baskets, per-product uncertainty, anomaly scoring, and personas. |
| 42 | [model_based_embeddings](model_based_embeddings.ipynb) | Posteriors-as-affinities embedding theory: the per-field evidence-capped default and why the degenerate alternatives produce rings/blobs. |

## Module 10 — Capstone

| # | Notebook | What it covers |
|---|---|---|
| 43 | [ppl_end_to_end_case_study](ppl_end_to_end_case_study.ipynb) | A full applied Bayesian workflow in `mixle.ppl`: pooled to hierarchical regression, held-out comparison, posterior-predictive check, and prediction with uncertainty. |

## Module 11 — Further methods

| # | Notebook | What it covers |
|---|---|---|
| 44 | [causal_inference_from_observational_data](causal_inference_from_observational_data.ipynb) | Potential outcomes and confounding; regression adjustment, propensity-score IPW, doubly robust estimation, and sensitivity to unmeasured confounders. |
| 45 | [conformal_prediction](conformal_prediction.ipynb) | Distribution-free prediction intervals and sets with finite-sample coverage; split conformal for regression and classification, marginal vs conditional coverage. |
| 46 | [multiple_testing_and_fdr](multiple_testing_and_fdr.ipynb) | Why many tests inflate false positives; family-wise control (Bonferroni, Holm) vs false discovery rate (Benjamini-Hochberg), verified on simulated screens. |
| 47 | [missing_data_and_imputation](missing_data_and_imputation.ipynb) | MCAR/MAR/MNAR mechanisms; complete-case and mean-imputation bias, multiple imputation with Rubin's rules, and mixle's OptionalDistribution. |
| 48 | [quantile_regression](quantile_regression.ipynb) | Modeling conditional quantiles via the pinball loss; adaptive prediction intervals on heteroscedastic data and quantile crossing. |
| 49 | [gaussian_process_regression](gaussian_process_regression.ipynb) | Nonparametric regression with a distribution over functions; prior samples, the posterior, and learning kernel hyperparameters by marginal likelihood. |
| 50 | [time_series_forecasting](time_series_forecasting.ipynb) | Trend and seasonal decomposition, Holt-Winters exponential smoothing, rolling-origin backtesting against a seasonal-naive baseline, and forecast intervals. |
| 51 | [extreme_value_theory](extreme_value_theory.ipynb) | The distributions of extremes; block maxima with the GEV, peaks-over-threshold with the generalized Pareto, and return levels beyond the data. |
| 52 | [cox_proportional_hazards](cox_proportional_hazards.ipynb) | Survival regression by partial likelihood; hazard ratios, the Schoenfeld residual check, and Breslow baseline survival curves. |
| 53 | [ab_testing_and_power](ab_testing_and_power.ipynb) | The two-proportion test, sample-size and power planning, the peeking problem, and Bayesian decision by expected loss. |
| 54 | [bayesian_model_comparison](bayesian_model_comparison.ipynb) | Bayes factors and the Jeffreys scale, and WAIC / leave-one-out cross-validation when the marginal likelihood is intractable. |
| 55 | [regularization_and_sparsity](regularization_and_sparsity.ipynb) | Ridge vs lasso, coefficient paths, sparse support recovery, and choosing the penalty by cross-validation. |
| 56 | [conformal_uq_on_graphs](conformal_uq_on_graphs.ipynb) | Conformal set-valued uncertainty on graphs and combinatorial objects: the exchangeability condition, conformal sets over rankings/permutations, transductive node-label sets, link-prediction neighbor sets, and knowledge-graph tail sets. |
| 57 | [knowledge_graph_completion_and_uncertainty](knowledge_graph_completion_and_uncertainty.ipynb) | Fitting a DistMult knowledge-graph model with the regular estimation framework, then completing any slot of a fact, recommending missing facts and subgraphs, and attaching uncertainty: conformal completion sets and epistemic (ensemble BALD) uncertainty. |
| 58 | [latent_fields_from_proxies](latent_fields_from_proxies.ipynb) | A shared latent field (GP / Gaussian-Markov random field) observed through many heterogeneous proxies, fit jointly with `fit_field`: the Gaussian forward model, logistic occupancy, and the log-Gaussian Cox process, with information additive across proxies and a posterior readable off any node. |
| 59 | [bayesian_inverse_problems](bayesian_inverse_problems.ipynb) | Recovering the unobservable drivers of an ODE/PDE — a rate, a source field, a coefficient, an initial condition — as a posterior from noisy, partial observations, with `DifferentialProxy` (differentiable RK4 / steady linear solve); ill-posedness regularized by the prior, and the Laplace posterior exact in the linear-Gaussian case. |
| 60 | [projecting_an_llm_onto_a_lookback_hmm](projecting_an_llm_onto_a_lookback_hmm.ipynb) | Variational projection of a language model onto a lookback HMM: distilling a small char-level GRU into a Markov-switching mixture of bigram models (`LookbackHiddenMarkovModelDistribution`, `lag=1`) by streaming EM over an unbounded supply of LM samples — a running accumulator at constant memory — with the bits/char gap to the LM's own entropy as the projection loss and each hidden state's bigram "voice" as the interpretable payoff. |
| 61 | [enumerating_a_language_model](enumerating_a_language_model.ipynb) | Exact best-first enumeration of an autoregressive LM (distilGPT-2) from the mode down — verified against brute force (exact order, exact probabilities, mode = argmax) on a restricted support, scaled to the full 50k vocabulary with the lazy-successor trick (top-10 of a 10¹⁴ space in ~80 pops), with the admissibility bound that makes it exact and the connection to `mixle.enumeration`'s `best_first` / `enumerator()` on factorised models. |
| 62 | [inverse_rl_maxent](inverse_rl_maxent.ipynb) | Exact maximum-entropy **inverse reinforcement learning** on a gridworld — recover a hidden reward from expert demonstrations alone. The hard step (the trajectory partition function `Z` and the expected state-visitation) is computed **exactly** by soft value-iteration + the forward visitation pass — the same `logsumexp`-over-paths **forward/backward algorithm** mixle runs for sequence models, no sampling. The outer reward-learning is one `mixle.program` move (`maxent_irl`, feature matching); behaviour is recovered 100% (the reward up to scale/shift). Notes the adversarial sibling (`gail`) and that the reward can be a `NeuralLeaf` instead of a table. |
| 63 | [tiny_vision_language_model](tiny_vision_language_model.ipynb) | A small captioning **VLM built the "tight" way** — exact object-centric perception (EM clustering pixels into object *slots*, the calibrated alternative to dense patch attention) + exact ordering + an exact grammar template, with a **neural part of only ~166 parameters** that learns the one genuinely-learned map (colour naming). Captions held-out scenes at ~98%. Shows the thesis that exact handles the math/structure and neural handles the learning, how it scales (CNN encoder + slot-conditioned LM), and why the blend can be the *better* model, not just the cheaper one. |
| 64 | [reasoning_over_real_images](reasoning_over_real_images.ipynb) | A **reasoning model on real COCO photographs**, on a laptop: **frozen** pretrained perception (a COCO-trained DETR, reused not retrained) + an **exact probabilistic reasoning program** over the detected objects — composable `filter`/`relate`/`count`/`exist`/`compare` with exact marginalisation over the detector's confidence. Answers compositional spatial/counting/comparison questions ("how many cats are on the couch → 2.00", "remote left of a cat → P=1.00") correctly and **calibrated**, generalising to unseen compositions *because the reasoning is computed, not learned*. The only trained part is a tiny question→program parser (`mixle.program`). The neuro-symbolic answer (NS-VQA) to "reasoning without a cluster": pretrained perception + exact reasoning. |
| 65 | [cifar10_conv_net_and_exact_head](cifar10_conv_net_and_exact_head.ipynb) | A **real conv net on real images, from scratch, on a laptop** — CIFAR-10 (60k natural photographs) trained end-to-end through `mixle.program` (one `minimize` move over streamed minibatches, on the GPU/MPS) to **~88–89%** in ~15 min: the ConvNetJS target, modernized (full ImageNet-to-SOTA stays a cluster job — stated honestly). Then the **exact+neural blend**: an exact per-class `MultivariateGaussian` head (`mixle.stats`, closed-form, **no backprop**) on the frozen features **matches/beats the trained softmax** (89.0% vs 87.9%) and **adds a brand-new class from 5 examples with no retraining** (87.8% recall on it). Honest about what the blend does *not* buy — calibration and naive density-OOD both failed, and that's reported, not hidden. |
