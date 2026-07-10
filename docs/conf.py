"""Sphinx configuration for the mixle-notebooks documentation."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

project = "mixle-notebooks"
author = "Grant Boquet"
copyright = "2014-2026, Grant Boquet and contributors"
release = "0.7.0"
version = "0.7"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

source_suffix = {".rst": "restructuredtext"}
master_doc = "index"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "../notebooks/.ipynb_checkpoints"]

autodoc_default_options = {
    "members": True,
    "no-index": True,
    "show-inheritance": True,
}
autodoc_member_order = "bysource"
autodoc_typehints = "description"
autodoc_typehints_format = "short"
autodoc_preserve_defaults = True
add_module_names = False
napoleon_google_docstring = True
napoleon_numpy_docstring = True
autodoc_mock_imports = ["openpyxl", "pandas"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

html_theme = "furo"
html_title = "mixle-notebooks"
html_static_path = []
todo_include_todos = False
