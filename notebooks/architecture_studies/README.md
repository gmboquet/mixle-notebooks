# architecture_studies/ — performance, scaling, and internals

Self-contained timing and scaling studies of the library itself (synthetic data only); each ships
pre-executed. Numbers are machine-specific — the shapes and ratios are the point.

| Notebook | What it covers |
|---|---|
| [import_and_warmup](import_and_warmup.ipynb) | Import cost, the numba cold-vs-warm disk cache (~7.6× cold-start saving), and the encode-once pattern. |
| [data_scaling](data_scaling.ipynb) | EM throughput vs dataset size N — linear per-iteration time and steady-state points/sec for mixtures and composites. |
| [model_scaling](model_scaling.ipynb) | Cost vs model size — mixture components K (linear), HMM states S (~S²), and sequence length L (linear). |
| [engine_benchmarks](engine_benchmarks.ipynb) | numpy vs numba vs torch and where each wins (the torch crossover), plus the convergence-LL double-pass overhead. |
| [ppl_scaling_vs_pyro_stan](ppl_scaling_vs_pyro_stan.ipynb) | `mixle.ppl` vs sampling-based PPLs: closed-form EM vs torch-Adam (Pyro-SVI stand-in, ~40×, same answer), exact conjugate vs MCMC (~865×, same posterior), and MCMC/HMC throughput — with honest framing on the unavailable baselines. |
| [parallel_scaling](parallel_scaling.ipynb) | Data sharding × model sharding across every backend (`local`/`mp`/`spark`/`dask`/`ray`/`mpi` + GPU): the `balance_plan` FLOPs+memory grid chooser, model-parallel threads (bit-identical), all six data backends returning the *same* fit (overhead-vs-scale profile), a **strong-scaling sweep over 2/4/6/8 cores** (data sharding via MPI ranks out-scales model-parallel threads, which hit the GIL ceiling), the data×model composition, and the torch GPU engine (MPS/CUDA). Uses [parallel_bench.py](parallel_bench.py) for isolated per-backend subprocess runs. |

Practical takeaways: keep the numba cache directory persistent (cold starts recompile every kernel,
~7.6× slower); encode once and reuse; pick the engine by data size (default numpy for small-medium N,
torch only above the crossover / on GPU); note that each EM iteration re-scores emissions in a
separate convergence-likelihood pass (~half of per-iteration work); and for parallelism, prefer data
sharding (it never changes the answer and is trivially balanced) — reach for model sharding only when the
model won't fit memory or there are fewer observations than workers, and let `balance_plan` choose.
