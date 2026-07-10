Validation
==========

Notebook validation should execute notebooks with bounded timeouts and capture
failures without hiding slow cells. The previous bitrot pass used short
timeouts first, then retried longer notebooks with larger per-notebook limits.

Recommended checks:

.. code-block:: console

   python -m pip install -r requirements.txt
   python -m pytest

When running notebooks directly, skip checkpoint files under
``notebooks/.ipynb_checkpoints`` and record notebooks that require optional
external data, a JVM, GPU libraries, or heavyweight PDE dependencies.

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

Use consistent states in execution reports:

``passed``
    The notebook executed end-to-end under the recorded timeout.

``failed``
    The notebook executed and raised an error. Record the first meaningful
    traceback, not every downstream failure.

``timed_out``
    The notebook exceeded the configured timeout. Retry with a larger timeout
    only when the notebook is expected to be long-running.

``skipped``
    The notebook was intentionally outside the execution scope.

``blocked``
    A required dataset, JVM, GPU, service, or sibling package was unavailable.

Release Review Notes
--------------------

Do not collapse ``timed_out``, ``skipped``, and ``blocked`` into a single
failure count. They mean different things for release quality. A notebook that
needs private data should remain blocked until a public fixture or documented
skip policy exists.
