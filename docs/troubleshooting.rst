Troubleshooting
===============

Notebook Times Out
------------------

Record the timeout and retry intentionally with a larger limit if the notebook
is expected to run. Do not count a timeout as a pass. If it depends on a slow
optional service, mark the prerequisite.

When rerunning with a larger timeout, keep the old timeout result in the review
notes so release owners can distinguish a slow notebook from a corrected
notebook.

Notebook Needs Missing Data
---------------------------

Mark the notebook blocked with the missing dataset or service. Avoid adding
private data to the repo to make a notebook pass.

Parallel Run Is Flaky
---------------------

Check for shared output paths, global random seeds, and notebooks that mutate
the same local files. Retry serially before changing notebook code.

Unexpected Notebook Diff
------------------------

Separate source changes from output metadata churn. Only commit rerun outputs
when the output is meaningful for the release review.

If output is intentionally cleared, make sure the execution manifest still
records the last successful run, environment, and data inputs.

Docs Build Fails
----------------

Run:

.. code-block:: console

   make -C docs html SPHINXOPTS="-W --keep-going"

Autodoc failures usually mean a notebook helper module moved without its API
page being regenerated, or that a docs dependency is missing from the validation
environment.

Execution Manifest Is Stale
---------------------------

If the execution manifest lists notebooks that no longer exist, or omits
newly added notebooks, update the manifest before rerunning the sweep. The
manifest is the release ledger: it should name every notebook, its status,
timeout, prerequisite, and failure reason. A stale manifest makes a green docs
build look more complete than it really is.
