Release Notes
=============

``mixle-notebooks`` is the example and tutorial package for the Mixle family.
This release targets mixle 0.7.0: it adds a capability-showcase set of
notebooks and records notebook groups, execution expectations, and bitrot
reporting rules.

mixle 0.7.0 Capability Showcase
-------------------------------

Three ``data_science`` notebooks were added and executed against a clean
``mixle==0.7.0`` install:

* ``agentic_system_facade`` -- the ``mixle.system.System`` facade
  (``answer`` / ``ingest`` / ``improve``), with budget as a hard ceiling,
  auditable spend receipts, and named degraded modes.
* ``cross_modal_belief_transport`` -- cross-modal reasoning with structured
  belief nodes, premise-checked conditional transports, a belief walk whose
  coverage is checked by hop count, cycle-consistency abstention, and
  task-sufficient projection.
* ``copulas_and_gated_mixtures`` -- the new ``CopulaDistribution`` (Sklar's
  theorem) and ``GatedMixtureDistribution`` (learned gate ``p(k | z)``)
  families, each measured against the baseline it improves on.

Included
--------

* Sphinx manual with catalog, execution runbook, validation, and
  troubleshooting pages.
* Documentation of staged timeout strategy for notebook reruns.
* ``docs/_build`` ignore rule for local builds.
* Notebook-execution manifest guidance for timeout, worker count, execution
  scope, status, and first meaningful failure.
* Security/data guidance for downloaded datasets, private prerequisites,
  rendered outputs, and cleared artifacts.
* Strict local Sphinx Makefile path for documentation validation.

Changed
-------

Notebook health is documented as execution evidence rather than a visual
spot-check. Short timeout sweeps are useful for triage, but public release
evidence needs either a successful execution record or an explicit
skip/block reason for every shipped or linked notebook.

Validation Evidence
-------------------

Record:

* notebook discovery scope;
* worker count for parallel execution;
* timeout used for each sweep or retry;
* status per attempted notebook;
* first meaningful error for failures;
* ``make -C docs html SPHINXOPTS="-W --keep-going"``.
* data prerequisites and whether they are public, synthetic, derived, or
  private;
* package versions or sibling checkout commits used for execution; and
* whether outputs were refreshed, preserved, or intentionally cleared.

Known Risks
-----------

* A one-minute timeout is a triage pass, not proof that long notebooks are
  healthy.
* Output-only notebook churn can obscure real source changes.
* Some notebooks require optional data, JVMs, GPUs, or PDE dependencies and
  should be marked blocked rather than counted as failed or passed.
* Executing from a warm developer environment can hide undeclared dependencies.
* Long-running notebooks should be retried with intentional timeout settings
  instead of being silently excluded from the release record.
