Execution Runbook
=================

Notebook maintenance is different from ordinary unit testing. A notebook can
import optional packages, touch local data, rely on plotting backends, or run
long enough that a short smoke timeout is only a triage signal. This page
defines how to rerun and report notebooks without overstating the result.

Discovery
---------

Include notebooks under:

* ``notebooks/tutorials``;
* ``notebooks/data_science``;
* ``notebooks/applications``;
* ``notebooks/exploration_geoscience``;
* ``notebooks/architecture_studies``.

Skip checkpoint files under ``.ipynb_checkpoints``. Record notebooks that are
intentionally excluded because they require unavailable private data, a GPU,
a JVM, or another external service.

Timeout Strategy
----------------

Use staged timeouts:

``short sweep``
    A fast pass, such as one minute per notebook, to find immediate bitrot.

``targeted retry``
    A longer retry, such as two to five minutes, for notebooks that are known
    to run real examples.

``manual/blocked``
    A notebook that requires external services should be marked blocked with
    the missing prerequisite, not silently counted as passing.

Parallel Execution
------------------

Parallel notebook execution is useful, but the report should include the
worker count and timeout. Avoid sharing mutable output directories between
workers unless the notebook is known to be isolated.

Failure Classification
----------------------

Use clear categories:

``passed``
    Executed all cells within the timeout.

``failed``
    A cell raised an error.

``timed_out``
    Execution exceeded the declared timeout.

``blocked``
    Required data, dependency, kernel, or service was unavailable.

``skipped``
    Intentionally omitted by the run configuration.

Release Report
--------------

A useful bitrot report should include:

* notebook path;
* timeout;
* status;
* first failing cell or exception summary;
* optional dependency or data requirement;
* whether outputs were intentionally refreshed.

Notebook output churn should be reviewed carefully. If outputs changed only
because of rerun metadata, avoid treating that as a documentation improvement.
