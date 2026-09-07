# tutorials/ — syntax and usage

How to call the mixle API: lean, syntax-focused notebooks on synthetic data. Start with
`distributions_and_combinators`, then `fitting_and_estimation`.

| Notebook | What it covers |
|---|---|
| [distributions_and_combinators](distributions_and_combinators.ipynb) | The building blocks: base distributions (Gaussian, Gamma, categorical, Markov chains, the full leaf catalog) and the combinators (Composite, Sequence, Optional, Ignored, Conditional, FiniteStochasticTransform). Start here. |
| [fitting_and_estimation](fitting_and_estimation.ipynb) | The fitting entry points: `optimize`/`best_of` (EM), `fit_mle`/`fit_map` (gradient + MAP), the EM-strategy zoo, and custom objectives. |
| [probabilistic_programming](probabilistic_programming.ipynb) | `mixle.ppl`: the one-rule modeling surface (`free` / value / distribution-in-slot), `.fit()`, `how=` engine routing (conjugate/MCMC/HMC/NUTS/ensemble/VI/VMP), regression with `Field` (incl. heteroskedastic scale), hierarchical `.each()`, mixtures, constraints, and RV algebra. |
| [bayesian_distributions](bayesian_distributions.ipynb) | Attaching conjugate priors in `mixle.stats` (`prior=`), `fit` returning a posterior, priors nesting through composites, and a Dirichlet-process mixture call. |
| [latent_variable_models](latent_variable_models.ipynb) | Constructing and fitting mixtures, HMMs, LDA, and hierarchical/joint mixtures; reading component posteriors. |
| [embedding_with_htsne](embedding_with_htsne.ipynb) | `htsne`/`humap`: one-call model-based 2-D embeddings of heterogeneous data, and the `affinity=` options. |
| [mcmc_sampling](mcmc_sampling.ipynb) | `sample_parameter_posterior` (MH/HMC) and exact `sample_conjugate_posterior`, and the `MCMCResult` surface. |
| [enumeration](enumeration.ipynb) | `dist.enumerator()` / `top_k`: iterating a discrete distribution's support in decreasing-probability order. |
| [accelerated_engines](accelerated_engines.ipynb) | Compute engines: the same model on numpy (numba auto-selected), `TorchEngine`, and the symbolic engine with SymPy export. |
| [parallel_estimation](parallel_estimation.ipynb) | Distributed and streaming estimation: `optimize(backend='mp'|'dask'|'mpi')`, DataFrame ingestion, the planner, and `StreamingEstimator`. |
| [model_parallel_estimation](model_parallel_estimation.ipynb) | Splitting the model and the data: component-sharded mixtures across a device mesh, with a live two-rank `torch.distributed` run. |
| [estimation_using_spark](estimation_using_spark.ipynb) | The same estimation code on Spark RDDs: distributed EM via per-partition sufficient statistics. |
