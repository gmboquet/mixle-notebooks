Package Map
===========

``notebooks/tutorials``
    Syntax-first walkthroughs of the core Mixle API.

``notebooks/data_science``
    Course-style examples for probabilistic data science, uncertainty,
    calibration, model comparison, inference, graphical models, time series,
    optimization, and representation learning.

``notebooks/applications``
    End-to-end domain workflows for finance, geoscience, NLP, social data,
    radar, seismic inversion, retail, anomaly detection, and graph examples.

``notebooks/exploration_geoscience``
    Geoscience-focused notebooks for basin modeling, geochemical
    fingerprinting, kriging, GPR tomography, gravity inversion, joint
    inversion, well logs, and drilling value of information.

``notebooks/architecture_studies``
    Import, warmup, data scaling, engine benchmarks, model scaling, parallel
    scaling, and PPL comparison notebooks.

``data``
    Small local datasets and fixtures used by notebooks.

Release Review Surface
----------------------

``docs/catalog``
    Human-readable inventory of notebook groups and expected ownership.

``docs/execution-runbook``
    Execution workflow for bitrot sweeps, timeouts, skip reasons, and output
    handling.

``docs/notebook-execution-manifest``
    Release-facing execution status and retry policy.

``docs/reproducibility``
    Environment, seed, output, and dependency guidance for repeatable runs.

Public notebook evidence should include a status for every linked notebook:
passed, failed, skipped with reason, blocked by dependency, or timed out with
the timeout value used.

``docs/api``
    Generated API pages for helper scripts committed with the notebook
    collection. If a helper script becomes reusable package code, move it to the
    owning package and leave a notebook-facing example here.

Ownership Notes
---------------

Notebook directories own examples, narrative, and reproducible execution
metadata — they are not the source of truth for core algorithms, gateway
routes, PDE solvers, or release schemas. When a notebook discovers reusable
behavior, move the implementation to the owning package first and then
update the notebook to demonstrate the reviewed API, rather than letting the
notebook itself become the canonical copy.

The ``data`` directory should stay small and explicit. Large, private, or
externally licensed datasets should be documented as prerequisites instead of
being committed silently. If a notebook depends on a generated artifact, record
the command and package revision that produced it.
