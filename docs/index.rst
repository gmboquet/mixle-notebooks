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

Notebook Health
---------------

The catalog above describes what each notebook is for; :doc:`notebook-execution-manifest`
describes whether it currently runs. Keep those two views aligned, and treat
notebook health as execution evidence — kernel, timeout, package versions,
and pass/skip/block status per notebook — rather than a visual spot-check of
committed output cells. A notebook that needs private data or an external
service should say so and stay marked blocked rather than silently pass
against different inputs.
