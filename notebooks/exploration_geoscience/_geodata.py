"""Real-dataset loaders for the *Exploration Geoscience* course.

Each loader returns clean, analysis-ready arrays/frames from a real, openly-published dataset that lives under
``notebooks-repo/data/``, so a course notebook opens with a single ``load_*()`` call and spends its code on
modelling, not parsing. Pure I/O — no modelling here.
"""

from __future__ import annotations

import os
from types import SimpleNamespace

import numpy as np

_DATA = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", "data"))


def load_hugoton(standardize=True, logs=("GR", "ILD_log10", "DeltaPHI", "PHIND", "RELPOS")):
    """SEG-2016 Hugoton-Panoma facies dataset: 10 training wells (with core facies) + 2 blind wells, with the
    blind logs aligned to their true core facies by nearest depth.

    Returns a namespace with ``train`` / ``blind`` DataFrames (blind has ``true_code``), the ``logs`` list, the
    facies code list, names and palette indices, and (if ``standardize``) the train mean/std used to z-score
    both sets. Real data, real held-out test.
    """
    import pandas as pd
    d = os.path.join(_DATA, "hugoton_panoma")
    train = pd.read_csv(os.path.join(d, "training_wells.csv")).sort_values(["Well Name", "Depth"])
    blind = pd.read_csv(os.path.join(d, "blind_wells_logs.csv")).sort_values(["Well Name", "Depth"])
    core = pd.read_csv(os.path.join(d, "blind_wells_core_facies.csv"))
    logs = list(logs)
    mu = sd = None
    if standardize:
        mu, sd = train[logs].mean(), train[logs].std(ddof=0)
        train = train.copy(); blind = blind.copy()
        train[logs] = (train[logs] - mu) / sd
        blind[logs] = (blind[logs] - mu) / sd

    def _attach(b, c):
        c = c.sort_values("Depth.ft"); cd = c["Depth.ft"].to_numpy(); code = c["LithCode"].to_numpy()
        bd = b["Depth"].to_numpy(); j = np.clip(np.searchsorted(cd, bd), 0, len(cd) - 1); jl = np.clip(j - 1, 0, len(cd) - 1)
        nearest = np.where(np.abs(cd[jl] - bd) < np.abs(cd[j] - bd), jl, j)
        out = b.copy(); out["true_code"] = code[nearest]; out["join_dist"] = np.abs(cd[nearest] - bd); return out

    facies = list(range(1, 10))
    blind = pd.concat([_attach(b, core[core["WellName"] == w]) for w, b in blind.groupby("Well Name", sort=False)],
                      ignore_index=True)
    blind = blind[blind["true_code"].isin(facies) & (blind["join_dist"] <= 0.5)].reset_index(drop=True)
    names = {1: "SS", 2: "CSiS", 3: "FSiS", 4: "SiSh", 5: "MS", 6: "WS", 7: "D", 8: "PS", 9: "BS"}
    return SimpleNamespace(train=train, blind=blind, logs=logs, facies=facies, names=names, mu=mu, sd=sd)


def load_heat_flow(region="west"):
    """IHFC Global Heat Flow Database 2024 — US onshore-continental wells carrying the full Fourier trio
    (heat flow ``q`` mW/m², temperature gradient ``T_grad`` K/km, thermal conductivity ``tc`` W/m·K), with
    location, depth, and lithology. Real measured data, CC-BY 4.0.

    ``region``: ``'west'`` (conterminous western US, lon −125…−103, lat 31…49 — the Cordilleran geothermal
    belt), ``'conus'`` (whole lower-48), or ``'all'``.

    Returns a namespace with the DataFrame ``df`` (columns ``lon, lat, q, T_grad, tc, depth, elevation,
    lithology, stratigraphy``) and convenience arrays ``lon, lat, q``.
    """
    import pandas as pd
    df = pd.read_csv(os.path.join(_DATA, "heat_flow", "ihfc_us_onshore.csv"))
    df = df.rename(columns={"long_EW": "lon", "lat_NS": "lat", "T_grad_mean": "T_grad", "tc_mean": "tc",
                            "total_depth_MD": "depth", "geo_lithology": "lithology",
                            "geo_stratigraphy": "stratigraphy"})
    df = df[["lon", "lat", "q", "T_grad", "tc", "depth", "elevation", "lithology", "stratigraphy"]]
    if region == "west":
        df = df[df.lat.between(31, 49) & df.lon.between(-125, -103)]
    elif region == "conus":
        df = df[df.lat.between(24, 50) & df.lon.between(-125, -66)]
    df = df.reset_index(drop=True)
    return SimpleNamespace(df=df, lon=df.lon.to_numpy(), lat=df.lat.to_numpy(), q=df.q.to_numpy())


def load_laguna_gravity(detrend="planar"):
    """Laguna del Maule Bouguer-gravity survey (Miller et al. 2016; 191 stations). Returns local-east/north
    coordinates (m, centred), observation height, the Bouguer anomaly, and a regional-trend-removed residual.

    ``detrend``: ``'planar'`` (remove a least-squares plane), ``'mean'``, or ``None``.
    """
    raw = open(os.path.join(_DATA, "laguna_gravity", "LdM_grav_obs.grv")).read().split("\n")
    n = int(raw[0].split()[0])
    rows = np.array([[float(v) for v in l.split()] for l in raw[1:n + 1] if l.strip()])
    x, y, z, g = rows[:, 0], rows[:, 1], rows[:, 2], rows[:, 3]
    ox, oy = x - x.mean(), y - y.mean()
    if detrend == "planar":
        A = np.column_stack([np.ones_like(ox), ox, oy]); res = g - A @ np.linalg.lstsq(A, g, rcond=None)[0]
    elif detrend == "mean":
        res = g - g.mean()
    else:
        res = g.copy()
    return SimpleNamespace(obs=np.column_stack([ox, oy, z]), x=ox, y=oy, z=z, bouguer=g, anomaly=res, n=n)


def load_basalts():
    """Vermeesch (2006) labelled basalt tectonic-discrimination dataset: training classes IAB / MORB / OIB
    (island-arc / mid-ocean-ridge / ocean-island basalt) and three held-out test localities (Aleutian arc,
    Galapagos ridge, Pitcairn islands) of known affinity. Returns ``train`` {class: DataFrame} and ``test``
    {locality: (DataFrame, true_class)}, headers normalized (uppercase, ``(WT%)``/``(PPM)`` stripped).
    """
    import pandas as pd
    xls = pd.ExcelFile(os.path.join(_DATA, "basalt_geochem", "vermeesch_basalts.xls"))
    norm = lambda df: df.rename(columns=lambda c: str(c).upper().replace("(WT%)", "").replace("(PPM)", "").strip())
    train = {c: norm(xls.parse(c)) for c in ["IAB", "MORB", "OIB"]}
    test = {"Aleutian arc": (norm(xls.parse("Aleutian arc")), "IAB"),
            "Galapagos ridge": (norm(xls.parse("Galapagos ridge")), "MORB"),
            "Pitcairn islands": (norm(xls.parse("Pitcairn islands")), "OIB")}
    return SimpleNamespace(train=train, test=test,
                           classes=["IAB", "MORB", "OIB"],
                           names={"IAB": "island arc", "MORB": "mid-ocean ridge", "OIB": "ocean island"})


def load_namib_zircon():
    """Namib Sand Sea detrital-zircon U-Pb ages (Vermeesch & Garzanti 2015; 16 samples, 1534 grains): 14 dune
    samples (N1-N14) + 2 Orange-River trunk samples (T8, T13). Returns ``ages`` (dict sample -> grain ages in
    Ma), ``sigma`` (dict sample -> 1-sigma), ``all_ages`` (pooled), and ``samples``/``trunk`` lists.
    """
    import csv
    d = os.path.join(_DATA, "detrital_zircon")

    def _cols(fn):
        rows = list(csv.reader(open(os.path.join(d, fn), encoding="utf-8-sig")))
        hdr = rows[0]; out = {h: [] for h in hdr}
        for r in rows[1:]:
            for h, v in zip(hdr, r):
                if v.strip():
                    out[h].append(float(v))
        return hdr, out

    hdr, ages = _cols("Namib_DZ.csv")
    _, sig = _cols("Namib_DZerr.csv")
    ages = {h: np.array(ages[h]) for h in hdr}
    sig = {h: np.array(sig[h]) for h in hdr}
    return SimpleNamespace(ages=ages, sigma=sig, all_ages=np.concatenate([ages[h] for h in hdr]),
                           samples=hdr, trunk=[h for h in hdr if h.startswith("T")])


def load_graptolites():
    """Ordovician graptolite occurrences from the Paleobiology Database (real, CC-BY). Returns a DataFrame of
    occurrences (taxon, genus, collection, formation, max_ma/min_ma age bounds, lat/lng) for the canonical
    index fossils of Ordovician biostratigraphy.
    """
    import pandas as pd
    df = pd.read_csv(os.path.join(_DATA, "biostratigraphy", "graptolites_ordovician.csv"))
    df = df[df.accepted_rank.isin(["genus", "species"])].copy()
    df["genus"] = df.accepted_name.str.split().str[0]
    df["mid_ma"] = (df.max_ma + df.min_ma) / 2
    return df.dropna(subset=["formation", "mid_ma", "genus"]).reset_index(drop=True)


def load_am13():
    """Arrenæs AM13 crosshole GPR first-arrival traveltimes (Looms et al. 2010; 702 rays, 2 boreholes 5 m
    apart). Returns source/receiver coordinates (x, depth in m), traveltimes (ns), per-datum std, and the full
    data covariance matrix.
    """
    from scipy.io import loadmat
    m = loadmat(os.path.join(_DATA, "crosshole_gpr", "AM13_data.mat"))
    S, R = m["S"], m["R"]
    return SimpleNamespace(S=S, R=R, traveltime=m["d_obs"].ravel(), std=m["d_std"].ravel(),
                           cov=m["Ct"], n_rays=len(m["d_obs"].ravel()))
