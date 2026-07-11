# mixle-notebooks

Worked examples, courses, and benchmarks for
[mixle](https://github.com/gmboquet/mixle) — composable, distributed density estimation
for messy, mixed-type data. The library is published on PyPI as `mixle` (the import name is
`mixle`).

## Setup

```sh
pip install mixle          # the core library (import as `mixle`)
pip install -r requirements.txt # notebook extras + mixle-pde + the latest library from source
jupyter lab notebooks/
```

`requirements.txt` installs the library and its extras from source. The physics-based inverse-problem
notebooks (`flow_inversion`, `oil_exploration_decision`, `radar_tomography`,
`seismic_full_waveform_inversion`, `synthetic_aperture_sonar`, `bayesian_inverse_problems`) also need the
**[`mixle-pde`](https://github.com/gmboquet/mixle-pde)** package — the differentiable PDE /
physics stack (`Differential`, `make_ops`, `laplacian`, `NavierStokes2D`, ...) extracted out of `mixle`. To
install the unreleased code directly:

```sh
pip install "mixle[all] @ git+https://github.com/gmboquet/mixle.git"
pip install "mixle-pde @ git+https://github.com/gmboquet/mixle-pde.git"   # physics/PDE notebooks
```

The Spark tutorial additionally needs a JVM (PySpark 4.x requires Java 17 or 21, e.g.
`brew install openjdk@17` with `JAVA_HOME` set).

## Documentation

The Sphinx manual starts at [`docs/index.rst`](docs/index.rst). It documents installation, the
notebook package map, the catalog structure, and validation expectations.

```sh
python -m pip install sphinx furo myst-parser
make -C docs html SPHINXOPTS="-W --keep-going"
```

Release notes and the current changelog are in
[`docs/release-notes.rst`](docs/release-notes.rst) and
[CHANGELOG.md](CHANGELOG.md).

## The notebooks

Five folders, organized by purpose — each has its own index. New here? Start with **tutorials/**.

| Folder | | What it is |
|---|--:|---|
| [tutorials/](notebooks/tutorials) | 12 | How to call the API — lean, syntax-focused, synthetic data. |
| [data_science/](notebooks/data_science) | 72 | A course in probabilistic data science — each method explained, derived, and evaluated on real data, foundations to capstone. |
| [applications/](notebooks/applications) | 20 | End-to-end solutions to real domain problems (NLP, finance, networks, spatial statistics, physics-based inverse problems), each a worked solution in its field. |
| [exploration_geoscience/](notebooks/exploration_geoscience) | 11 | Subsurface geoscience workflows — basin thermal history, tomography, provenance, kriging, well-log facies, and drilling decisions. |
| [architecture_studies/](notebooks/architecture_studies) | 6 | How the library performs — timing and scaling studies of the library itself. |

## Data

`data/` ships the small datasets the notebooks use; notebooks load them with paths relative to their
folder (`../../data/...`). Sources:

- `data/online_retail_ii/` — UCI Online Retail II (CC BY 4.0, DOI `10.24432/C5CG6D`).
- `data/fake_news_bf/`, `data/fake_news_pf/` — BuzzFeed and PolitiFact article sets from
  [FakeNewsNet](https://github.com/KaiDMML/FakeNewsNet).
- `data/baseball/` — Efron-Morris (1975) batting data (18 players, via the Rdatasets `pscl` mirror).
- `data/radon/` — Gelman-Hill Minnesota radon data (919 homes, 85 counties, via the pymc-devs mirror).
- `data/tweets/` — a sample of geotagged UK tweets (coordinates only).
- `data/user_proc/` — a train/valid/test process-activity log.
- `data/stocks/` — a simulated multi-asset daily price panel and an option chain for the finance notebooks.
- Plus the Iliad text, SSL certificate records, a word list, NeurIPS submissions, and a Wikipedia corpus.

## License

MIT, matching mixle.
