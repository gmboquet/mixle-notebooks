"""Plotting helpers for the *Exploration Geoscience* course.

The course's rule: a notebook cell should be **modelling**, not matplotlib boilerplate. Every figure in the
course is one call into this module, so each notebook reads as ``load -> model -> show`` and the only
non-trivial code left on the page is the call into ``mixle`` / ``mixle_pde`` that does the inference.
Nothing here models anything; it only draws.

Conventions: functions take already-computed arrays and return the Matplotlib ``Figure`` (so a notebook can
tweak it if needed) after drawing. Colours and sizing are consistent across the course.
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

plt.rcParams.update({"figure.dpi": 110, "axes.grid": False})

# A shared, colour-blind-friendly facies palette (SEG / Hugoton-Panoma order) reused across the course.
FACIES_COLORS = ["#d4b483", "#e3c565", "#c2d076", "#7fb069", "#56a3a6",
                 "#4d8fac", "#9b7ede", "#d36582", "#8c4843"]
FACIES_CMAP = ListedColormap(FACIES_COLORS)


def _grid_extent(grid):
    """(x0, x1, z0, z1) display extent for a (gx, gz) axis pair, depth increasing downward."""
    gx, gz = grid
    return [gx.min(), gx.max(), gz.max(), gz.min()]


def geoscatter(lon, lat, value, *, title="", clabel="", cmap="inferno", vmin=None, vmax=None, s=14, ax=None):
    """Point map: scatter of (lon, lat) coloured by ``value`` (e.g. heat flow per well). Latitude-corrected aspect."""
    own = ax is None
    if own:
        fig, ax = plt.subplots(figsize=(6.4, 5.2))
    sc = ax.scatter(lon, lat, c=value, cmap=cmap, s=s, vmin=vmin, vmax=vmax, edgecolors="none")
    ax.set_aspect(1.0 / np.cos(np.deg2rad(float(np.mean(lat)))))
    ax.set(xlabel="longitude", ylabel="latitude", title=title)
    if own:
        fig.colorbar(sc, ax=ax, shrink=0.8, label=clabel); fig.tight_layout(); return fig
    return sc


def variogram(lag, semivariance, *, sill=None, nugget=None, title="empirical variogram", xlabel="separation"):
    """Empirical semivariance vs lag, with optional sill / nugget lines — how much variance is spatially
    structured (interpolable) vs nugget (unpredictable at this spacing)."""
    fig, ax = plt.subplots(figsize=(6.0, 3.6))
    ax.plot(lag, semivariance, "o-", color="#3b6ea5")
    if sill is not None:
        ax.axhline(sill, ls="--", color="0.5", label=f"sill (total var) {sill:.0f}")
    if nugget is not None:
        lab = f"nugget {nugget:.0f} ({100 * nugget / sill:.0f}% of sill)" if sill else f"nugget {nugget:.0f}"
        ax.axhline(nugget, ls=":", color="#d36582", label=lab)
    ax.set(xlabel=xlabel, ylabel="semivariance γ(h)", title=title, ylim=(0, None)); ax.legend(fontsize=8)
    fig.tight_layout(); return fig


def calibration(nominal, empirical, *, title="predictive-interval calibration"):
    """Reliability curve: empirical coverage vs nominal level. Below the diagonal = overconfident (intervals too
    narrow), above = conservative. The honest-UQ check."""
    fig, ax = plt.subplots(figsize=(4.4, 4.2))
    ax.plot([0, 1], [0, 1], "k--", lw=1, label="perfect")
    ax.plot(nominal, empirical, "o-", color="#3b6ea5", label="observed")
    ax.set(xlabel="nominal coverage", ylabel="empirical coverage", title=title, xlim=(0, 1), ylim=(0, 1))
    ax.legend(fontsize=8); ax.set_aspect("equal"); fig.tight_layout(); return fig


# --------------------------------------------------------------------------- 1-D / logs
def well_track(depth, curves, facies=None, *, facies_names=None, title=None, width=11):
    """A wireline-log track: each named curve in its own column against depth, with an optional facies strip.

    Args:
        depth: (n,) depth values.
        curves: dict ``{name: (n,) array}`` of logs to plot left-to-right.
        facies: optional (n,) integer facies codes (1-based) drawn as a colour strip on the right.
        facies_names: optional ``{code: label}`` for the strip.
    """
    ncol = len(curves) + (1 if facies is not None else 0)
    fig, ax = plt.subplots(1, ncol, figsize=(width, 5), sharey=True)
    ax = np.atleast_1d(ax)
    for a, (name, v) in zip(ax, curves.items()):
        a.plot(v, depth, lw=0.6, color="#333"); a.set_title(name, fontsize=9); a.grid(alpha=0.3)
    ax[0].set_ylabel("depth"); ax[0].invert_yaxis()
    if facies is not None:
        a = ax[len(curves)]
        a.imshow(np.asarray(facies)[:, None], aspect="auto", cmap=FACIES_CMAP, vmin=1, vmax=9,
                 extent=[0, 1, np.max(depth), np.min(depth)])
        a.set_title("facies", fontsize=9); a.set_xticks([])
    if title:
        fig.suptitle(title, y=1.02)
    fig.tight_layout(); return fig


def crossplot(x, y, c, *, xlabel="", ylabel="", clabel="", ticks=None, ticklabels=None, cmap=None, title=None):
    """Coloured scatter (e.g. two logs coloured by facies) in one call."""
    fig, ax = plt.subplots(figsize=(6.2, 4.4))
    sc = ax.scatter(x, y, c=c, s=4, alpha=0.5, cmap=cmap or FACIES_CMAP)
    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    cb = fig.colorbar(sc, label=clabel)
    if ticks is not None:
        cb.set_ticks(ticks)
    if ticklabels is not None:
        cb.ax.set_yticklabels(ticklabels)
    fig.tight_layout(); return fig


def facies_posterior(depth, posterior, truth=None, *, names=None, calibration=None, title=None):
    """A probabilistic facies log: the (T, K) posterior probability heatmap against depth, an optional true
    facies strip, and an optional (confidence, accuracy) calibration curve."""
    K = posterior.shape[1]
    ncol = 1 + (1 if truth is not None else 0) + (1 if calibration is not None else 0)
    widths = [3] + ([0.5] if truth is not None else []) + ([1.6] if calibration is not None else [])
    fig, ax = plt.subplots(1, ncol, figsize=(4 + 2.6 * ncol, 4.6), gridspec_kw={"width_ratios": widths})
    ax = np.atleast_1d(ax)
    ax[0].imshow(posterior, aspect="auto", cmap="viridis", vmin=0, vmax=1,
                 extent=[1, K, np.max(depth), np.min(depth)])
    ax[0].set(title=title or "posterior facies probability", xlabel="facies", ylabel="depth")
    if names:
        ax[0].set_xticks(range(1, K + 1)); ax[0].set_xticklabels([names[i] for i in range(1, K + 1)], fontsize=7)
    k = 1
    if truth is not None:
        ax[k].imshow(np.asarray(truth)[:, None], aspect="auto", cmap=FACIES_CMAP, vmin=1, vmax=9,
                     extent=[0, 1, np.max(depth), np.min(depth)])
        ax[k].set(title="true", xticks=[]); k += 1
    if calibration is not None:
        conf, acc = calibration
        ax[k].plot(conf, acc, "o-", color="#d36582"); ax[k].plot([0, 1], [0, 1], "k--", lw=1)
        ax[k].set(title="calibration", xlabel="confidence", ylabel="accuracy", xlim=(0, 1), ylim=(0, 1))
    fig.tight_layout(); return fig


# --------------------------------------------------------------------------- maps / sections / volumes
def anomaly_map(x, y, d, *, title="", clabel="", cmap="RdBu_r", units_km=True, symmetric=True):
    """Scatter map of a geophysical anomaly (gravity/magnetic station values)."""
    s = 1e3 if units_km else 1.0
    vmax = np.abs(d).max() if symmetric else None
    fig, ax = plt.subplots(figsize=(5.6, 4.4))
    sc = ax.scatter(np.asarray(x) / s, np.asarray(y) / s, c=d, cmap=cmap, s=45, edgecolor="k", lw=0.2,
                    vmin=-vmax if symmetric else None, vmax=vmax)
    ax.set(xlabel="easting (km)" if units_km else "x", ylabel="northing (km)" if units_km else "y",
           title=title, aspect="equal")
    fig.colorbar(sc, label=clabel); fig.tight_layout(); return fig


def section(field, grid, *, title="", clabel="", cmap="RdBu_r", symmetric=False, points=None, ax=None):
    """A 2-D cross-section image of a field on a (gx, gz) grid (depth down). ``points`` overlays e.g. sensors."""
    own = ax is None
    if own:
        fig, ax = plt.subplots(figsize=(5.2, 4.0))
    vmax = np.abs(field).max() if symmetric else None
    im = ax.imshow(field.T, origin="upper", extent=_grid_extent(grid), aspect="auto", cmap=cmap,
                   vmin=-vmax if symmetric else None, vmax=vmax)
    if points is not None:
        ax.scatter(points[:, 0], points[:, 1], s=4, c="w")
    ax.set(title=title, xlabel="x", ylabel="depth")
    if own:
        ax.figure.colorbar(im, ax=ax, label=clabel); ax.figure.tight_layout()
    return im


def sections(fields, grid, *, titles=None, clabel="", cmap="RdBu_r", symmetric=False, vlim=None):
    """A row of cross-sections sharing a colour scale (e.g. truth | recovered | uncertainty)."""
    n = len(fields)
    fig, ax = plt.subplots(1, n, figsize=(3.7 * n, 3.6))
    ax = np.atleast_1d(ax)
    vmax = vlim if vlim is not None else (np.abs(np.concatenate([f.ravel() for f in fields])).max() if symmetric else None)
    for a, f, t in zip(ax, fields, titles or [""] * n):
        im = a.imshow(f.T, origin="upper", extent=_grid_extent(grid), aspect="auto", cmap=cmap,
                      vmin=-vmax if symmetric else None, vmax=vmax)
        a.set(title=t, xlabel="x")
    ax[0].set_ylabel("depth")
    fig.colorbar(im, ax=ax, fraction=0.02, label=clabel); return fig


def volume3d(cells, values, *, mask=None, title="", clabel="", cmap="viridis", elev=18, azim=-65, depth_up=True):
    """A 3-D scatter of the cells whose ``values`` pass ``mask`` (e.g. an ore body / reservoir)."""
    m = np.ones(len(cells), bool) if mask is None else mask
    fig = plt.figure(figsize=(5.4, 4.6)); ax = fig.add_subplot(111, projection="3d")
    p = cells[m]
    sc = ax.scatter(p[:, 0], p[:, 1], p[:, 2], c=np.asarray(values)[m], cmap=cmap, s=24)
    ax.set(title=title, xlabel="x", ylabel="y", zlabel="depth"); ax.view_init(elev, azim)
    if depth_up:
        ax.invert_zaxis()
    fig.colorbar(sc, ax=ax, shrink=0.6, label=clabel); fig.tight_layout(); return fig


def ray_geometry(sources, receivers, color_by=None, *, title="", clabel="", every=9):
    """Crosshole/survey geometry: source and receiver positions and a sample of the rays between them.
    ``sources``/``receivers`` are (n, 2) (x, depth); ``color_by`` optionally colours a second panel."""
    S, R = np.asarray(sources), np.asarray(receivers)
    ncol = 2 if color_by is not None else 1
    fig, ax = plt.subplots(1, ncol, figsize=(5 * ncol, 4.2)); ax = np.atleast_1d(ax)
    for k in range(0, len(S), every):
        ax[0].plot([S[k, 0], R[k, 0]], [S[k, 1], R[k, 1]], "-", color="0.7", lw=0.3)
    ax[0].scatter(S[:, 0], S[:, 1], c="C0", s=10, label="transmitters")
    ax[0].scatter(R[:, 0], R[:, 1], c="C3", s=10, label="receivers")
    ax[0].set(title=title or "survey geometry", xlabel="x (m)", ylabel="depth (m)"); ax[0].invert_yaxis(); ax[0].legend(fontsize=8)
    if color_by is not None:
        sc = ax[1].scatter((S[:, 1] + R[:, 1]) / 2, color_by[0], c=color_by[1], cmap="viridis", s=8)
        ax[1].set(title=color_by[2], xlabel="mid-depth (m)", ylabel=color_by[3]); fig.colorbar(sc, ax=ax[1], label=clabel)
    fig.tight_layout(); return fig


def tomogram(velocity, grid, *, rays=None, title="", clabel="m/ns", cmap="turbo", ax=None):
    """A velocity/property tomogram (depth down), optionally overlaying ray paths ``rays`` (a list of (x, z)
    polylines in metres)."""
    own = ax is None
    if own:
        fig, ax = plt.subplots(figsize=(5.0, 4.4))
    im = ax.imshow(velocity.T, origin="upper", extent=_grid_extent(grid), aspect="auto", cmap=cmap)
    if rays is not None:
        for rx, rz in rays:
            ax.plot(rx, rz, color="k", lw=0.3, alpha=0.5)
    ax.set(title=title, xlabel="x (m)", ylabel="depth (m)")
    if own:
        ax.figure.colorbar(im, ax=ax, label=clabel); ax.figure.tight_layout()
    return im


def wavefronts(T, grid, source_xy, *, title="", clabel="traveltime"):
    """Contour the (nx, nz) traveltime field as wavefronts, marking the source."""
    gx, gz = grid
    fig, ax = plt.subplots(figsize=(4.6, 4.4))
    cs = ax.contour(gx, gz, T.T, levels=15, cmap="viridis")
    ax.plot(source_xy[0], source_xy[1], "r*", ms=12)
    ax.set(title=title, xlabel="x", ylabel="depth", aspect="equal"); ax.invert_yaxis()
    fig.colorbar(cs, label=clabel); fig.tight_layout(); return fig


def age_spectrum(ages, *, components=None, weights=None, bw=40.0, title="", xlabel="age (Ma)", logx=False):
    """Kernel-density spectrum of a set of ages, optionally overlaying fitted mixture components (a list of
    ``(mean, sd)`` and their ``weights``) — the detrital-geochronology age-population picture."""
    ages = np.asarray(ages); xs = np.linspace(ages.min(), ages.max(), 600)
    kde = np.exp(-0.5 * ((xs[:, None] - ages[None, :]) / bw) ** 2).sum(1) / (len(ages) * bw * np.sqrt(2 * np.pi))
    fig, ax = plt.subplots(figsize=(7.5, 3.6))
    ax.fill_between(xs, kde, color="0.85"); ax.plot(xs, kde, color="0.4", lw=1, label="KDE of grain ages")
    if components is not None:
        w = weights if weights is not None else np.ones(len(components)) / len(components)
        for (mu, sd), wk in zip(components, w):
            ax.plot(xs, wk * np.exp(-0.5 * ((xs - mu) / sd) ** 2) / (sd * np.sqrt(2 * np.pi)), lw=1.5)
            ax.axvline(mu, color="k", ls=":", lw=0.6)
    if logx:
        ax.set_xscale("log")
    ax.set(title=title, xlabel=xlabel, ylabel="density"); ax.legend(fontsize=8); fig.tight_layout(); return fig


def scatter_classes(x, y, labels, *, xlabel="", ylabel="", title="", logx=False, logy=False, lines=None):
    """Scatter coloured by discrete class with a legend (e.g. a tectonic-discrimination diagram). ``lines`` is
    an optional list of (x_array, y_array, label) reference boundaries."""
    fig, ax = plt.subplots(figsize=(5.6, 4.4))
    for c in sorted(set(labels)):
        m = np.array(labels) == c
        ax.scatter(np.asarray(x)[m], np.asarray(y)[m], s=12, alpha=0.6, label=str(c))
    if lines:
        for lx, ly, ll in lines:
            ax.plot(lx, ly, "k--", lw=0.8, alpha=0.6)
    if logx:
        ax.set_xscale("log")
    if logy:
        ax.set_yscale("log")
    ax.set(xlabel=xlabel, ylabel=ylabel, title=title); ax.legend(fontsize=8); fig.tight_layout(); return fig


def provenance_bars(samples, fractions, *, era_names=None, groups=None, title="", ylabel="fraction of grains"):
    """Stacked bar per sample of its source-population fractions (the provenance fingerprint), samples ordered
    by group. ``fractions`` is (n_samples, n_eras); ``groups`` optionally separates e.g. trunk vs dune."""
    fractions = np.asarray(fractions)
    order = np.argsort(groups) if groups is not None else np.arange(len(samples))
    fig, ax = plt.subplots(figsize=(max(7, 0.4 * len(samples)), 3.8))
    bottom = np.zeros(len(samples))
    for k in range(fractions.shape[1]):
        ax.bar(range(len(samples)), fractions[order, k], bottom=bottom[order],
               label=(era_names[k] if era_names else f"pop {k}"))
        bottom = bottom + fractions[:, k]
    ax.set(xticks=range(len(samples)), title=title, ylabel=ylabel)
    ax.set_xticklabels(np.array(samples)[order], rotation=90, fontsize=7)
    ax.legend(fontsize=8, ncol=fractions.shape[1]); fig.tight_layout(); return fig


def mds_map(coords, labels, *, groups=None, title="multidimensional scaling"):
    """2-D MDS scatter of samples (one point each), labelled, optionally coloured by group."""
    coords = np.asarray(coords)
    fig, ax = plt.subplots(figsize=(5.2, 4.6))
    if groups is None:
        ax.scatter(coords[:, 0], coords[:, 1], s=40, c="#4d8fac")
    else:
        for grp in sorted(set(groups)):
            m = np.array(groups) == grp
            ax.scatter(coords[m, 0], coords[m, 1], s=40, label=str(grp))
        ax.legend(fontsize=8)
    for (x, y), lab in zip(coords, labels):
        ax.annotate(lab, (x, y), fontsize=7, alpha=0.7)
    ax.set(title=title, xlabel="MDS-1", ylabel="MDS-2"); fig.tight_layout(); return fig


def range_chart(taxa, fad, lad, *, fad_ci=None, lad_ci=None, title="", xlabel="age (Ma)"):
    """Stratigraphic range chart: a horizontal bar per taxon from FAD to LAD (in Ma, older left), with optional
    Strauss-Sadler confidence-interval extensions. Taxa are drawn in the given order (e.g. the composite
    sequence)."""
    fig, ax = plt.subplots(figsize=(7.5, 0.32 * len(taxa) + 1.2))
    for i, t in enumerate(taxa):
        ax.plot([fad[t], lad[t]], [i, i], "-", color="#3b6ea5", lw=4, solid_capstyle="butt")
        if fad_ci is not None:
            ax.plot([fad[t] + fad_ci[t], fad[t]], [i, i], "-", color="#3b6ea5", lw=1)
        if lad_ci is not None:
            ax.plot([lad[t], lad[t] - lad_ci[t]], [i, i], "-", color="#3b6ea5", lw=1)
    ax.set(yticks=range(len(taxa)), title=title, xlabel=xlabel); ax.set_yticklabels(taxa, fontsize=8)
    ax.invert_xaxis()  # older (larger Ma) on the left
    fig.tight_layout(); return fig


def matrix(M, *, labels=None, title="", clabel="", cmap="magma", row_normalize=False):
    """A labelled matrix heatmap (transition matrix, confusion matrix, covariance)."""
    M = np.asarray(M, float)
    if row_normalize:
        M = M / np.clip(M.sum(1, keepdims=True), 1e-12, None)
    fig, ax = plt.subplots(figsize=(4.6, 4.0))
    im = ax.imshow(M, cmap=cmap)
    if labels is not None:
        ax.set(xticks=range(len(labels)), yticks=range(len(labels)))
        ax.set_xticklabels(labels, fontsize=7, rotation=45, ha="right"); ax.set_yticklabels(labels, fontsize=7)
    ax.set_title(title)
    fig.colorbar(im, ax=ax, fraction=0.046, label=clabel); fig.tight_layout(); return fig


# --------------------------------------------------------------------------- diagnostics
def fit_scatter(obs, pred, *, units="", title=None, ax=None):
    """Observed-vs-predicted data fit with the 1:1 line."""
    own = ax is None
    if own:
        fig, ax = plt.subplots(figsize=(4.4, 4.0))
    ax.scatter(obs, pred, s=10, alpha=0.4, c="#4d8fac")
    lim = [min(np.min(obs), np.min(pred)), max(np.max(obs), np.max(pred))]
    ax.plot(lim, lim, "k--", lw=1)
    ax.set(xlabel=f"observed {units}", ylabel=f"predicted {units}", title=title)
    if own:
        ax.figure.tight_layout()
    return ax


def forest(labels, estimate, ci_low, ci_high, *, ref=None, title="", xlabel="", sort=True):
    """A forest plot: each item's point estimate with its confidence interval as a horizontal bar, optionally
    against a reference line; intervals clearing the reference are highlighted. The natural figure for a
    quantified, UQ'd decision (effect sizes with credible intervals)."""
    est = np.asarray(estimate, float); lo = np.asarray(ci_low, float); hi = np.asarray(ci_high, float)
    labels = np.asarray(labels)
    order = np.argsort(est) if sort else np.arange(len(est))
    fig, ax = plt.subplots(figsize=(6.4, 0.32 * len(est) + 1.0))
    for row, i in enumerate(order):
        clears = ref is not None and (lo[i] > ref or hi[i] < ref)
        col = "#d36582" if clears else "0.55"
        ax.plot([lo[i], hi[i]], [row, row], "-", color=col, lw=2)
        ax.plot(est[i], row, "o", color=col, ms=5)
    if ref is not None:
        ax.axvline(ref, color="k", ls="--", lw=1)
    ax.set(yticks=range(len(est)), title=title, xlabel=xlabel); ax.set_yticklabels(labels[order], fontsize=8)
    fig.tight_layout(); return fig


def interval_band(x, mean, sd, truth=None, *, z=1.96, title=None, xlabel="", ylabel="", sort=True):
    """A predicted value with an uncertainty band (e.g. an imputed log), optionally vs held-out truth."""
    x = np.asarray(x); order = np.argsort(mean) if sort else np.arange(len(mean))
    xs = np.arange(len(order))
    fig, ax = plt.subplots(figsize=(7.5, 3.4))
    ax.fill_between(xs, (mean - z * sd)[order], (mean + z * sd)[order], alpha=0.25, color="#4d8fac",
                    label=f"{int(100*(1-2*(1-0.975))) if z==1.96 else ''}95% interval")
    ax.plot(xs, mean[order], color="#4d8fac", lw=1, label="predicted")
    if truth is not None:
        ax.scatter(xs, np.asarray(truth)[order], s=4, c="k", label="true")
    ax.set(title=title, xlabel=xlabel or "sample (sorted)", ylabel=ylabel); ax.legend(fontsize=8)
    fig.tight_layout(); return fig
