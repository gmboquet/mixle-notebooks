"""Make sibling `mixle`/`mixle-pde` source checkouts importable for notebook execution.

Mirrors the sibling-checkout convention `mixle-demos/tests/conftest.py` already uses. A normal
`pip install -r requirements.txt` installs `mixle`/`mixle-pde` as real packages and this file is a
no-op; inside this monorepo layout (this repo checked out next to `mixle`/`mixle-pde`), it puts the
sibling source trees on `PYTHONPATH` instead. `nbmake` runs every notebook in its own Jupyter-kernel
subprocess, which inherits the process environment, so setting `PYTHONPATH` here -- before pytest
collection starts a single kernel -- is enough for every notebook under `pillar_validation/` to pick
it up without each one repeating the path setup.
"""

import os
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_SIBLINGS = {
    "mixle": _HERE.parent / "mixle" / "mixle" / "__init__.py",
    "mixle_pde": _HERE.parent / "mixle-pde" / "mixle_pde" / "__init__.py",
    # mixle-sim is a separate package, not a former name of mixle-pde: it owns the FEM/adaptivity
    # surface (Domain2D, assemble_p1_diffusion, error_estimation.drive_adaptation, ...) that
    # mixle_pde does not provide under any name, and adaptive_mesh_refinement imports it.
    "mixle_sim": _HERE.parent / "mixle-sim" / "mixle_sim" / "__init__.py",
}

_extra = [
    str(marker.parent.parent) for marker in _SIBLINGS.values() if marker.is_file()
]
if _extra:
    existing = [p for p in os.environ.get("PYTHONPATH", "").split(os.pathsep) if p]
    os.environ["PYTHONPATH"] = os.pathsep.join(dict.fromkeys([*_extra, *existing]))
