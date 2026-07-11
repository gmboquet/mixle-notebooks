Validation
==========

Notebook validation should execute notebooks with bounded timeouts and capture
failures without hiding slow cells. The previous bitrot pass used short
timeouts first, then retried longer notebooks with larger per-notebook limits.

This package has no standalone unit test suite — validation means executing
notebooks:

.. code-block:: console

   python -m pip install -r requirements.txt
   python -m jupyter nbconvert \
     --to notebook \
     --execute \
     --ExecutePreprocessor.timeout=120 \
     notebooks/tutorials/<notebook>.ipynb

When running notebooks directly, skip checkpoint files under
``notebooks/.ipynb_checkpoints`` and record notebooks that require optional
external data, a JVM, GPU libraries, or heavyweight PDE dependencies. See
:doc:`execution-runbook` for running a full sweep across the collection.

Strict Documentation Gate
-------------------------

.. code-block:: console

   make -C docs html SPHINXOPTS="-W --keep-going"

Clean-Archive Documentation Gate
--------------------------------

Before public release, also build the docs from tracked files only:

.. code-block:: console

   tmp=$(mktemp -d)
   git archive HEAD | tar -x -C "$tmp"
   make -C "$tmp/docs" html SPHINXOPTS="-W --keep-going"

Bitrot Report Requirements
--------------------------

Notebook reruns should report timeout, worker count, status, and the first
meaningful failure for every notebook attempted. A one-minute timeout is useful
for triage, but it should be labeled as such.

Status Vocabulary
-----------------

Use the same five states as :doc:`execution-runbook` (``passed``,
``failed``, ``timed_out``, ``skipped``, ``blocked``) in every validation
report, and keep them separate — don't collapse ``timed_out``, ``skipped``,
and ``blocked`` into a single failure count, since they mean different
things for release quality. A notebook that needs private data should stay
``blocked`` until a public fixture or documented skip policy exists.
