Quickstart
==========

``mixle-notebooks`` is a notebook collection, so the first useful workflow is
to create a clean environment, open the catalog, and execute a small notebook
with a bounded timeout.

Create an Environment
---------------------

From the repository root:

.. code-block:: console

   python -m venv .venv
   . .venv/bin/activate
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt

The current requirements include notebook tools, plotting packages, scientific
libraries, and sibling Mixle packages. For public release execution, prefer a
constraints file or released package versions over unpinned source URLs.

Open the Catalog
----------------

Start with the catalog before choosing a notebook:

.. code-block:: console

   python -m jupyter lab

The best starting notebooks are under ``notebooks/tutorials``. Architecture
studies, application notebooks, and exploration-geoscience notebooks can be
heavier and may require optional dependencies.

Execute One Notebook
--------------------

Use ``nbconvert`` when checking a single notebook from the command line:

.. code-block:: console

   python -m jupyter nbconvert \
     --to notebook \
     --execute \
     --ExecutePreprocessor.timeout=120 \
     notebooks/tutorials/<notebook>.ipynb

Replace ``<notebook>`` with the specific notebook being checked. Do not count a
saved output as execution evidence unless the notebook was rerun from a clean
kernel.

Prefer a short timeout for exploratory checks and a recorded timeout for release
evidence. If a notebook times out, report the timeout value and do not mark the
notebook as failed until the owner decides whether it needs a larger gate or a
performance fix.

Next Steps
----------

This proves the environment can execute one notebook — it isn't a
catalog-wide bitrot report, and :doc:`notebook-execution-manifest` is the
source of truth for release health across the collection. Read
:doc:`authoring-guide` before adding new notebooks and
:doc:`execution-runbook` before running a full sweep, which covers what to
record per run (path, timeout, status, first meaningful error, and whether
outputs were intentionally refreshed).
