Installation
============

``mixle-notebooks`` is an executable documentation package. Install the
notebook requirements in an isolated environment so execution results are not
affected by packages left over from model-development work.

Install the notebook environment:

.. code-block:: console

   python -m pip install -r requirements.txt
   jupyter lab notebooks/

The notebook collection expects the core package import name ``mixle``. This
release targets **mixle 0.7.0**; the capability-showcase notebooks in
:doc:`catalog` were executed against a clean ``mixle==0.7.0`` install. Some
physics-backed notebooks also need ``mixle-pde``. Spark notebooks require a
JVM compatible with the installed PySpark version.

Install sibling packages deliberately and record whether they came from editable
checkouts or released artifacts. Notebook output can change when a sibling
package branch changes, so the package revision is part of the evidence.

Recommended local checkout setup:

.. code-block:: console

   python -m pip install -e ../mixle
   python -m pip install -e ../mixle-pde

Build this documentation:

.. code-block:: console

   python -m pip install "sphinx>=7" furo
   make -C docs html SPHINXOPTS="-W --keep-going"

The documentation source is Sphinx/reStructuredText. Generated HTML belongs in
``docs/_build`` and should not be committed.

Execution Environment Notes
---------------------------

Notebook execution can require optional services or larger dependencies:

* Spark notebooks require a compatible JVM and PySpark installation.
* PDE/geoscience notebooks need ``mixle-pde`` and may need generated domain
  fixtures.
* Architecture studies may be sensitive to warmup, CPU count, BLAS, and
  optional accelerator availability.

:doc:`notebook-execution-manifest` records these prerequisites per notebook —
a notebook missing one of them should show up there as blocked, not as a
silent pass against different inputs.
