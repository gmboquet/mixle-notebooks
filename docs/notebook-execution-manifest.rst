Notebook Execution Manifest
===========================

This page is the release-facing execution manifest for ``mixle-notebooks``. Unlike the
:doc:`catalog` (which describes what exists), this manifest records the **measured** execution
status of every shipped notebook against the release target, so a release claim points to
evidence rather than to committed output cells.

Execution Environment
---------------------

* Target library: ``mixle==0.7.0`` (installed from PyPI) plus ``mixle-pde`` 0.7.0 (local editable
  checkout on its ``release/0.7.0`` branch) for the PDE/inversion notebooks.
* Kernel: CPython 3.12, ``jupyter nbconvert --execute`` run from each notebook's own directory.
* Per-notebook timeout: 300s (light) / 700s (heavy). Date: 2026-07-10.
* Full resolved environment: ``release-checklists/0.7.0-freeze.txt``.

Summary
-------

Of 121 notebooks: **114 executed clean**, **5 blocked** on an unavailable
prerequisite (named below), and **2 slow/manual** (exceed the batch timeout or need a
longer interactive run). No notebook fails on a mixle 0.7.0 API break.

.. list-table::
   :header-rows: 1

   * - Group
     - Notebooks
     - Passed
     - Blocked
     - Slow/manual
   * - ``notebooks/tutorials``
     - 12
     - 10
     - 2
     - 0
   * - ``notebooks/data_science``
     - 72
     - 68
     - 3
     - 1
   * - ``notebooks/applications``
     - 20
     - 19
     - 0
     - 1
   * - ``notebooks/exploration_geoscience``
     - 11
     - 11
     - 0
     - 0
   * - ``notebooks/architecture_studies``
     - 6
     - 6
     - 0
     - 0

Blocked notebooks (named prerequisite)
--------------------------------------

* ``data_science/cifar10_conv_net_and_exact_head.ipynb`` -- needs HuggingFace datasets + dataset download.
* ``data_science/enumerating_a_language_model.ipynb`` -- needs transformers + model download.
* ``data_science/reasoning_over_real_images.ipynb`` -- needs transformers + model download.
* ``tutorials/estimation_using_spark.ipynb`` -- needs a JVM + PySpark.
* ``tutorials/parallel_estimation.ipynb`` -- needs an MPI runtime.

Slow / manual notebooks
-----------------------

These exceed the batch timeout or need a longer interactive run; they are release-tier
``manual`` and are not counted as API failures.

* ``applications/malware_certificate_embedding.ipynb`` -- exceeds batch timeout.
* ``data_science/projecting_an_llm_onto_a_lookback_hmm.ipynb`` -- exceeds batch timeout.

Per-group status
----------------

0.8.0 additions
~~~~~~~~~~~~~~~

* ``data_science/structured_science_context.ipynb`` -- passed with the Python
  3 standard-library kernel on 2026-07-15; contract-only smoke execution.
* ``data_science/newton_continuation_and_folds.ipynb`` -- passed with
  ``jupyter nbconvert --execute`` (CPython 3.14.5) on 2026-07-16, against
  ``mixle-pde`` ``release/0.8.0`` commit ``bcb91b1`` (``continuation.py``,
  MP-F2); every numeric claim in the notebook is asserted, not just printed.

Tutorials
~~~~~~~~~

* ``tutorials/accelerated_engines.ipynb`` -- passed
* ``tutorials/bayesian_distributions.ipynb`` -- passed
* ``tutorials/distributions_and_combinators.ipynb`` -- passed
* ``tutorials/embedding_with_htsne.ipynb`` -- passed
* ``tutorials/enumeration.ipynb`` -- passed
* ``tutorials/estimation_using_spark.ipynb`` -- blocked
* ``tutorials/fitting_and_estimation.ipynb`` -- passed
* ``tutorials/latent_variable_models.ipynb`` -- passed
* ``tutorials/mcmc_sampling.ipynb`` -- passed
* ``tutorials/model_parallel_estimation.ipynb`` -- passed
* ``tutorials/parallel_estimation.ipynb`` -- blocked
* ``tutorials/probabilistic_programming.ipynb`` -- passed

Data science
~~~~~~~~~~~~

* ``data_science/ab_testing_and_power.ipynb`` -- passed
* ``data_science/adaptive_clinical_trials.ipynb`` -- passed
* ``data_science/agentic_system_facade.ipynb`` -- passed
* ``data_science/anomaly_detection.ipynb`` -- passed
* ``data_science/bayesian_inverse_problems.ipynb`` -- passed
* ``data_science/bayesian_model_comparison.ipynb`` -- passed
* ``data_science/bayesian_optimization.ipynb`` -- passed
* ``data_science/bayesian_workflow_predictive_checks.ipynb`` -- passed
* ``data_science/bootstrap_and_uncertainty.ipynb`` -- passed
* ``data_science/causal_inference_from_observational_data.ipynb`` -- passed
* ``data_science/change_point_segmentation.ipynb`` -- passed
* ``data_science/character_models_chow_liu.ipynb`` -- passed
* ``data_science/cifar10_conv_net_and_exact_head.ipynb`` -- blocked
* ``data_science/classification_metrics_and_calibration.ipynb`` -- passed
* ``data_science/conformal_prediction.ipynb`` -- passed
* ``data_science/conformal_uq_on_graphs.ipynb`` -- passed
* ``data_science/conjugate_and_nonparametric_bayes.ipynb`` -- passed
* ``data_science/constrained_and_multiobjective_optimization.ipynb`` -- passed
* ``data_science/constrained_inference.ipynb`` -- passed
* ``data_science/copulas_and_gated_mixtures.ipynb`` -- passed
* ``data_science/count_data_overdispersion.ipynb`` -- passed
* ``data_science/cox_proportional_hazards.ipynb`` -- passed
* ``data_science/cross_modal_belief_transport.ipynb`` -- passed
* ``data_science/density_estimation_mixtures_vs_kde.ipynb`` -- passed
* ``data_science/directional_statistics.ipynb`` -- passed
* ``data_science/em_and_map_strategies.ipynb`` -- passed
* ``data_science/enumerating_a_language_model.ipynb`` -- blocked
* ``data_science/experimental_designs.ipynb`` -- passed
* ``data_science/exponential_families_and_conjugacy.ipynb`` -- passed
* ``data_science/extreme_value_theory.ipynb`` -- passed
* ``data_science/gaussian_mixtures_in_depth.ipynb`` -- passed
* ``data_science/gaussian_process_regression.ipynb`` -- passed
* ``data_science/heavy_tails_and_survival.ipynb`` -- passed
* ``data_science/heterogeneous_mixed_type_modeling.ipynb`` -- passed
* ``data_science/hierarchical_partial_pooling.ipynb`` -- passed
* ``data_science/hmm_from_scratch.ipynb`` -- passed
* ``data_science/hvis_topology_and_streaming.ipynb`` -- passed
* ``data_science/information_theory_in_practice.ipynb`` -- passed
* ``data_science/inverse_rl_maxent.ipynb`` -- passed
* ``data_science/knowledge_graph_completion_and_uncertainty.ipynb`` -- passed
* ``data_science/language_detection_hmm.ipynb`` -- passed
* ``data_science/latent_fields_from_proxies.ipynb`` -- passed
* ``data_science/latent_models_in_practice.ipynb`` -- passed
* ``data_science/learning_stop_words.ipynb`` -- passed
* ``data_science/market_basket_ibp.ipynb`` -- passed
* ``data_science/markov_chains_for_sequences.ipynb`` -- passed
* ``data_science/mcmc_uncertainty_quantification.ipynb`` -- passed
* ``data_science/missing_data_and_imputation.ipynb`` -- passed
* ``data_science/mle_and_sufficient_statistics.ipynb`` -- passed
* ``data_science/model_based_clustering_evaluation.ipynb`` -- passed
* ``data_science/model_based_embeddings.ipynb`` -- passed
* ``data_science/model_selection_and_cross_validation.ipynb`` -- passed
* ``data_science/multiple_testing_and_fdr.ipynb`` -- passed
* ``data_science/naive_bayes_text_classification.ipynb`` -- passed
* ``data_science/networks_and_community_structure.ipynb`` -- passed
* ``data_science/ppl_end_to_end_case_study.ipynb`` -- passed
* ``data_science/projecting_an_llm_onto_a_lookback_hmm.ipynb`` -- manual (slow)
* ``data_science/quantile_regression.ipynb`` -- passed
* ``data_science/ranking_and_combinatorial_models.ipynb`` -- passed
* ``data_science/reasoning_over_real_images.ipynb`` -- blocked
* ``data_science/receipts_and_replay.ipynb`` -- passed
* ``data_science/regression_and_glms.ipynb`` -- passed
* ``data_science/regularization_and_sparsity.ipynb`` -- passed
* ``data_science/sequential_design_for_small_samples.ipynb`` -- passed
* ``data_science/state_space_filtering.ipynb`` -- passed
* ``data_science/structured_neural_leaves.ipynb`` -- passed
* ``data_science/time_series_forecasting.ipynb`` -- passed
* ``data_science/tiny_vision_language_model.ipynb`` -- passed
* ``data_science/topic_modeling_lda.ipynb`` -- passed
* ``data_science/topic_modeling_plsi.ipynb`` -- passed
* ``data_science/variational_inference_vs_mcmc.ipynb`` -- passed
* ``data_science/verifiable_design_loop.ipynb`` -- passed

Applications
~~~~~~~~~~~~

* ``applications/baseball_hierarchical_shrinkage.ipynb`` -- passed
* ``applications/bayesian_tweet_rhythm.ipynb`` -- passed
* ``applications/behavioral_anomaly_detection.ipynb`` -- passed
* ``applications/fake_news_detection.ipynb`` -- passed
* ``applications/flow_inversion.ipynb`` -- passed
* ``applications/generative_title_decoding.ipynb`` -- passed
* ``applications/geospatial_tweet_clusters.ipynb`` -- passed
* ``applications/knowledge_graph_umls.ipynb`` -- passed
* ``applications/machine_translation_alignment.ipynb`` -- passed
* ``applications/magma_reservoir_gravity_inversion.ipynb`` -- passed
* ``applications/malware_certificate_embedding.ipynb`` -- manual (slow)
* ``applications/oil_exploration_decision.ipynb`` -- passed
* ``applications/option_pricing_and_implied_volatility.ipynb`` -- passed
* ``applications/radar_tomography.ipynb`` -- passed
* ``applications/radon_mixed_effects.ipynb`` -- passed
* ``applications/retail_trend_statespace.ipynb`` -- passed
* ``applications/seismic_full_waveform_inversion.ipynb`` -- passed
* ``applications/social_fake_news_detection.ipynb`` -- passed
* ``applications/stock_portfolio_optimization.ipynb`` -- passed
* ``applications/synthetic_aperture_sonar.ipynb`` -- passed

Exploration geoscience
~~~~~~~~~~~~~~~~~~~~~~

* ``exploration_geoscience/00_foundations.ipynb`` -- passed
* ``exploration_geoscience/basin_thermal_history.ipynb`` -- passed
* ``exploration_geoscience/biostratigraphy_event_ordering.ipynb`` -- passed
* ``exploration_geoscience/crosshole_gpr_tomography.ipynb`` -- passed
* ``exploration_geoscience/detrital_zircon_provenance.ipynb`` -- passed
* ``exploration_geoscience/geochemical_fingerprinting.ipynb`` -- passed
* ``exploration_geoscience/magma_reservoir_gravity.ipynb`` -- passed
* ``exploration_geoscience/mineral_exploration_kriging.ipynb`` -- passed
* ``exploration_geoscience/near_surface_joint_inversion.ipynb`` -- passed
* ``exploration_geoscience/well_log_facies_hmm.ipynb`` -- passed
* ``exploration_geoscience/where_to_drill_value_of_information.ipynb`` -- passed

Architecture studies
~~~~~~~~~~~~~~~~~~~~

* ``architecture_studies/data_scaling.ipynb`` -- passed
* ``architecture_studies/engine_benchmarks.ipynb`` -- passed
* ``architecture_studies/import_and_warmup.ipynb`` -- passed
* ``architecture_studies/model_scaling.ipynb`` -- passed
* ``architecture_studies/parallel_scaling.ipynb`` -- passed
* ``architecture_studies/ppl_scaling_vs_pyro_stan.ipynb`` -- passed
