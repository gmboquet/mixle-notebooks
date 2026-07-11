Changelog
=========

This changelog tracks documentation-visible changes for ``mixle-notebooks``
— what's in the manual and catalog, not per-notebook execution results,
which belong in :doc:`notebook-execution-manifest` so pass/fail/skip/block
status stays auditable there. See :doc:`release-notes` for scope, validation
evidence, and known risks.

0.7.0 - 2026-07-11
------------------

Added
~~~~~

* mixle 0.7.0 capability-showcase notebooks under ``data_science``, each
  executed against a clean ``mixle==0.7.0`` install: ``agentic_system_facade``
  (the ``System`` facade -- ``answer`` / ``ingest`` / ``improve``, budgeted
  spend receipts, named degraded modes), ``cross_modal_belief_transport``
  (structured belief nodes, premise-checked transports, belief-walk coverage by
  hop count, abstention, task-sufficient projection), and
  ``copulas_and_gated_mixtures`` (the new ``CopulaDistribution`` and
  ``GatedMixtureDistribution`` families), documented in :doc:`catalog`.
* Sphinx manual covering notebook cataloging, authoring, execution sweeps,
  reproducibility, validation, and troubleshooting, backed by a generated API
  reference for the helper modules that support notebook discovery.

Changed
~~~~~~~

* Docs target mixle 0.7.0 (``release`` / ``version`` set to ``0.7.0`` /
  ``0.7``).
* Incremental EM examples use the keyword call
  ``inc.update(chunk, chunk_id=cid)`` matching the current mixle API.
* Installation docs point at sibling checkouts through relative paths rather
  than developer-local absolute paths.

Fixed
~~~~~

* The execution manifest's 5 ``BLOCKED`` and 2 slow/manual notebooks had only
  ever been named and skipped, never actually run; all 7 now execute for real
  (including a live two-rank ``mpiexec`` run and a 55+-stage local
  ``SparkContext`` job). The manifest reads 121/121 pass, 0 blocked, 0
  slow/manual.
* ``data_science/cifar10_conv_net_and_exact_head`` used a retired
  script-based HuggingFace dataset id that only appeared to work locally
  because of a stale cache; switched to the actively-maintained
  ``uoft-cs/cifar10`` mirror (schema-identical, same accuracy numbers).
