Notebook Catalog
================

Tutorials
---------

The ``tutorials`` notebooks are the best starting point for users learning the
core API. They cover distributions, combinators, estimation, parallelism,
Bayesian distributions, probabilistic programming, MCMC, enumeration, latent
models, accelerated engines, and embedding examples.

Data Science
------------

The ``data_science`` notebooks form a broader course. Topics include
uncertainty, model comparison, calibration, conformal prediction, Gaussian
mixtures, Gaussian processes, HMMs, latent fields, inverse RL, topic modeling,
causal inference, experimental design, Bayesian optimization, graph UQ,
vision-language modeling, and the mixle 0.7.0 capability showcase below.

mixle 0.7.0 Capability Showcase
-------------------------------

These ``data_science`` notebooks were added to exercise capabilities introduced
in mixle 0.7.0. Each runs against a clean ``mixle==0.7.0`` install and checks
its claims against ground truth or an explicit ledger.

``data_science/agentic_system_facade``
    The ``mixle.system.System`` facade and its three verbs (``answer`` /
    ``ingest`` / ``improve``): budget as a hard ceiling, auditable spend
    receipts, and named degraded modes (``teacher_down`` / ``store_down``).
    Runs offline against a deterministic stub teacher.

``data_science/cross_modal_belief_transport``
    Cross-modal reasoning (workstream F) via ``mixle.reason``: modalities as
    structured belief nodes, fitted conditional transports that must pass a
    premise check before composition, a belief walk with coverage checked by
    hop count, cycle-consistency abstention, and task-sufficient projection.

``data_science/copulas_and_gated_mixtures``
    Two new 0.7.0 families: ``CopulaDistribution`` (Sklar's theorem --
    arbitrary marginals glued to a dependence core, fit by IFM) and
    ``GatedMixtureDistribution`` (a mixture of experts with a learned gate
    ``p(k | z)``), each measured against the baseline it improves on.

``data_science/receipts_and_replay``
    Offline-verifiable provenance: ``ExecutionTrace`` bit-identical replay (with
    tamper detection via ``diff``) and the ``Receipt`` object binding ledger +
    trace + calibration + provenance, checked claim-by-claim by
    ``verify_receipt``.

``data_science/structured_neural_leaves``
    Neural building blocks whose structure holds *by construction*, verified at
    random initialization: ``make_deep_set`` (permutation invariance),
    ``make_monotonic_mlp`` (monotonicity), ``HamiltonianNet`` (energy
    conservation), and ``build_product_energy_net`` to compose them.

``data_science/verifiable_design_loop``
    Honest de-novo optimization with ``mixle.doe``: a ``VerifiableOracle``
    (declared tier + per-evaluation receipt) drives the ``optimize_under_oracle``
    propose--test--learn loop, and a self-graded oracle -- or no oracle -- is
    refused.

``data_science/hvis_topology_and_streaming``
    Structure beyond the scatter plot: ``nerve_report`` / ``component_tree``
    report the model's topology (components and loops) as numbers, ``model_map``
    gives a deterministic model-derived layout, and ``StreamingHvis`` places
    arriving batches against a fixed atlas.

The ``embedding_with_htsne`` tutorial shows htsne's reason to exist: embedding
**heterogeneous, incomplete records** that t-SNE cannot take. Each protein is a
mixed-type record -- a real (hydropathy), a categorical (fold), a set of tags,
and an assay count that is *often missing* at a class-dependent rate -- and
htsne embeds it natively through a mixture model (Gaussian + Categorical +
Bernoulli-set + ``Optional``). It beats the standard flatten-and-mean-impute
t-SNE pipeline (purity ~0.87 vs ~0.83), because imputation destroys the
informative missingness that htsne's ``Optional`` field keeps as signal. It then
showcases the new hvis ``goals`` (``AxisAlign`` giving the map a hydropathy
axis) and ``embedding_health`` (trustworthiness/continuity receipt).

Applications
------------

The ``applications`` notebooks are worked solutions for real domain examples,
including mineral exploration, radar tomography, seismic inversion, finance,
machine translation, anomaly detection, fake-news detection, knowledge graphs,
and retail time-series modeling.

Exploration Geoscience
----------------------

The ``exploration_geoscience`` notebooks focus on geoscience workflows such as
basin thermal history, crosshole GPR tomography, detrital zircon provenance,
geochemical fingerprinting, gravity inversion, kriging, joint inversion, well
log facies, and value-of-information drilling decisions.

Architecture Studies
--------------------

The ``architecture_studies`` notebooks measure import and warmup behavior,
engine benchmarks, data scaling, model scaling, parallel scaling, and PPL
scaling against other systems.

Catalog Status Expectations
---------------------------

The catalog should describe notebooks that are actually present in the
repository. When a notebook is renamed, moved, or split, update the catalog and
execution manifest in the same change. A catalog entry should not imply that a
notebook is release-validated unless the execution manifest records a passing
run or a clear skip/block reason.

For public release, keep notebook groups useful to readers: tutorials teach API
syntax, data-science notebooks teach modeling patterns, applications show
domain workflows, geoscience notebooks exercise subsurface examples, and
architecture studies measure performance or scaling behavior.
