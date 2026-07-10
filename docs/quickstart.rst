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

Report Results
--------------

Every notebook run should record:

* path;
* timeout;
* status: passed, failed, timed out, skipped, or blocked;
* first meaningful error for failures;
* optional dependency or data requirement;
* whether outputs were intentionally refreshed.

Read :doc:`authoring-guide` before adding new notebooks and
:doc:`execution-runbook` before running a full bitrot pass.

Quickstart Boundary
-------------------

The quickstart proves that the environment can execute one notebook. It is not
a substitute for a catalog-wide bitrot report. Use the execution manifest when
claiming release health for the notebook collection.
