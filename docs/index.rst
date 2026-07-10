mixle-notebooks
===============

``mixle-notebooks`` is the worked-example, course, and benchmark package for
the Mixle ecosystem. It contains notebooks for tutorials, probabilistic data
science, domain applications, geoscience workflows, and architecture studies.

Start Here
----------

Start with :doc:`quickstart` to create an environment and execute a notebook.
Use :doc:`catalog` to choose notebook groups, :doc:`authoring-guide` before
adding notebooks, and :doc:`execution-runbook` for bitrot sweeps.

This package should make examples reproducible and reviewable. It should not
hide package behavior behind manually edited outputs or unchecked local
artifacts.

.. toctree::
   :caption: Start Here
   :hidden:
   :maxdepth: 2

   installation
   quickstart
   package-map
   catalog
   authoring-guide
   execution-runbook
   notebook-execution-manifest
   reproducibility
   release-readiness
   release-notes
   changelog
   security-and-data
   validation
   troubleshooting

.. toctree::
   :caption: Reference
   :hidden:
   :maxdepth: 2

   api/modules

Notebook Groups
---------------

``notebooks/tutorials``
    Syntax-first tutorials for core Mixle APIs.

``notebooks/data_science``
    Probabilistic data-science examples from foundations to capstone workflows.

``notebooks/applications``
    End-to-end domain examples.

``notebooks/exploration_geoscience``
    Geoscience and subsurface modeling examples.

``notebooks/architecture_studies``
    Timing, scaling, warmup, and architecture studies.

Release Review
--------------

Notebook health should be reported as execution evidence, not as a visual
spot-check. A review record should include the kernel, timeout, package
versions, data prerequisites, executed notebooks, skipped notebooks, failures,
and whether outputs were intentionally refreshed. Notebooks that require
private data or external services should state the prerequisite and remain
blocked rather than silently passing with different inputs.

Reader Expectations
-------------------

Readers should be able to tell whether a notebook is a tutorial, course
example, domain workflow, geoscience study, or performance experiment. Release
reviewers should be able to tell whether it was executed, skipped, blocked, or
timed out. Those two views need to stay aligned: the catalog describes purpose,
and the execution manifest describes current health.

Release Claim Standard
----------------------

A public claim about notebook health should point to an execution manifest, not
only to committed notebook files. The manifest should cover every notebook in
scope or explain why a notebook was skipped, blocked, or timed out.
