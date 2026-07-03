"""One EM fit of a fixed Gaussian mixture under a chosen execution backend; prints a JSON line with
per-iteration wall time and the fitted log-likelihood. Used by parallel_scaling.ipynb to benchmark the
data-parallel backends (local / mp / spark / dask / ray / mpi) in isolated subprocesses so each cluster
spins up and tears down cleanly. Run directly:

    python parallel_bench.py <backend> <n> <workers> <iters>
    mpirun -n <W> python parallel_bench.py mpi <n> <W> <iters>
"""

import json
import sys
import time

import numpy as np

import mixle.stats as stats
import mixle.utils.parallel  # noqa: F401  (registers the encoded-data backends)
from mixle.inference import optimize


def make(n, k=10, dim=0, seed=0):
    """A k-component mixture and n samples. dim=0 -> scalar Gaussians (memory-bound); dim>0 -> MVGaussian
    components whose O(dim^2) per-observation quadratic form is compute-bound (the regime that scales)."""
    rng = np.random.RandomState(seed)
    if dim:
        comps = [stats.MultivariateGaussianDistribution((rng.randn(dim) * 3).tolist(), np.eye(dim).tolist()) for _ in range(k)]
        init = stats.MixtureDistribution(comps, [1.0 / k] * k)
        est = stats.MixtureEstimator([stats.MultivariateGaussianEstimator(dim=dim) for _ in range(k)])
        data = [(rng.randn(dim) + comps[rng.randint(k)].mu).tolist() for _ in range(n)]
    else:
        init = stats.MixtureDistribution(
            [stats.GaussianDistribution(float(i) - (k - 1) / 2, 1.0) for i in range(k)], [1.0 / k] * k
        )
        est = stats.MixtureEstimator([stats.GaussianEstimator() for _ in range(k)])
        data = [float(rng.randn() + 3 * (rng.randint(k) - (k - 1) / 2)) for _ in range(n)]
    return est, init, data


def ll(model, data):
    return float(np.sum(model.seq_log_density(model.dist_to_encoder().seq_encode(data))))


def run(backend, n=200_000, workers=4, iters=10, dim=0):
    est, init, data = make(n, dim=dim)

    if backend == "mpi":
        from mpi4py import MPI

        from mixle.utils.parallel.mpi import MPIEncodedData, mpi_out

        enc = MPIEncodedData(data, estimator=est)
        optimize(None, est, enc_data=enc, prev_estimate=init, max_its=1, out=mpi_out())  # warm
        t0 = time.perf_counter()
        m = optimize(None, est, enc_data=enc, prev_estimate=init, max_its=iters, out=mpi_out())
        secs = (time.perf_counter() - t0) / iters
        if MPI.COMM_WORLD.Get_rank() == 0:
            print(json.dumps({"backend": "mpi", "secs": secs, "ll": ll(m, data), "workers": MPI.COMM_WORLD.Get_size()}))
        return

    extra, data_arg, teardown = {}, data, lambda: None
    if backend == "spark":
        from pyspark import SparkConf, SparkContext

        sc = SparkContext.getOrCreate(
            SparkConf().setMaster(f"local[{workers}]").setAppName("pb").set("spark.ui.enabled", "false")
        )
        sc.setLogLevel("ERROR")
        data_arg = sc.parallelize(data, workers * 2)
        teardown = sc.stop
    elif backend == "dask":
        from dask.distributed import Client, LocalCluster

        cl = Client(LocalCluster(n_workers=workers, threads_per_worker=1, processes=True, dashboard_address=None))
        extra["client"] = cl
        extra["num_workers"] = workers
        teardown = cl.close
    elif backend == "ray":
        import ray

        ray.init(num_cpus=workers, include_dashboard=False, ignore_reinit_error=True, log_to_driver=False)
        extra["num_workers"] = workers
        teardown = ray.shutdown
    elif backend in ("mp", "multiprocessing"):
        extra["num_workers"] = workers

    optimize(data_arg, est, prev_estimate=init, max_its=1, out=None, backend=backend, **extra)  # warm
    t0 = time.perf_counter()
    m = optimize(data_arg, est, prev_estimate=init, max_its=iters, out=None, backend=backend, **extra)
    secs = (time.perf_counter() - t0) / iters
    print(json.dumps({"backend": backend, "secs": secs, "ll": ll(m, data), "workers": workers}))
    teardown()


if __name__ == "__main__":
    run(
        sys.argv[1],
        n=int(sys.argv[2]) if len(sys.argv) > 2 else 200_000,
        workers=int(sys.argv[3]) if len(sys.argv) > 3 else 4,
        iters=int(sys.argv[4]) if len(sys.argv) > 4 else 10,
        dim=int(sys.argv[5]) if len(sys.argv) > 5 else 0,
    )
