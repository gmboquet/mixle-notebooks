Release Readiness
=================

``mixle-notebooks`` is release-ready only when notebooks are treated as
executable artifacts. Saved outputs and polished prose do not prove that a
notebook still runs against the release code.

Supported Environment
---------------------

Release notes should record Python version, kernel, sibling package versions,
and optional resources for each notebook group. Notebooks that require a JVM,
GPU, external data, or heavy PDE dependencies should be classified explicitly.

Execution Gates
---------------

Before public release, every shipped or linked notebook should be either:

``passed``
    Executed top to bottom on a clean kernel against release code.

``blocked``
    Requires unavailable hardware, credentials, or data, with the reason
    recorded.

``skipped``
    Excluded by policy with a tracked reason.

``failed`` or ``timed_out``
    Not release-ready unless the failure is intentionally documented as a known
    limitation.

Bitrot Evidence
---------------

Record timeout, worker count, command, first meaningful error, and generated
artifact paths for each sweep. Short timeout triage is useful, but final
release evidence needs either successful execution or an explicit exclusion.

Documentation Gates
-------------------

The catalog, authoring guide, execution runbook, reproducibility page, and
notebook execution manifest should agree. Build Sphinx with warnings as errors
and from a clean archive before release.

Exclusion Policy
----------------

Do not silently drop a notebook from the release surface because it is slow or
credentialed. Move it into one of the explicit states above and record the
reason in the execution manifest. That makes the release honest: readers can
see which notebooks are public examples, which are environment-dependent, and
which need follow-up before they can be treated as maintained tutorials.

Output Policy
-------------

Saved outputs are acceptable when they help readers inspect a result and have
been reviewed for private paths, credentials, and large payloads. Clear outputs
when they are only transient execution noise. The execution manifest is the
release evidence; notebook output cells are supporting material.
