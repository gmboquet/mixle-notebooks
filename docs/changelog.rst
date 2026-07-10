Changelog
=========

This changelog records documentation-visible release changes for
``mixle-notebooks``.

0.7.0 - 2026-07-10
------------------

See :doc:`release-notes` for scope, validation evidence, and known risks.
This changelog tracks documentation-visible changes only; notebook execution
results belong in the execution manifest so pass, fail, skipped, and blocked
states remain auditable.

Added
~~~~~

* mixle 0.7.0 capability-showcase notebooks under ``data_science``, each
  executed against a clean ``mixle==0.7.0`` install: ``agentic_system_facade``
  (the ``System`` facade -- ``answer`` / ``ingest`` / ``improve``, budgeted
  spend receipts, named degraded modes), ``cross_modal_belief_transport``
  (structured belief nodes, premise-checked transports, belief-walk coverage by
  hop count, abstention, task-sufficient projection), and
  ``copulas_and_gated_mixtures`` (the new ``CopulaDistribution`` and
  ``GatedMixtureDistribution`` families).
* Catalog section describing the mixle 0.7.0 capability showcase.
* Sphinx manual for notebook cataloging, authoring, execution sweeps,
  reproducibility, validation, and troubleshooting.
* Notebook-execution manifest guidance for recording timeout, worker count,
  status, and first meaningful failure.
* Release-readiness checklist for notebook execution status, optional
  resources, bitrot evidence, and exclusion reasons.
* Generated API reference entry point for helper modules that support notebook
  discovery and validation.
* Security/data guidance for notebook outputs, private data prerequisites,
  downloaded datasets, and rendered artifacts.

Changed
~~~~~~~

* Docs target mixle 0.7.0 (``release`` / ``version`` set to ``0.7.0`` /
  ``0.7``).
* Incremental EM examples use the keyword call
  ``inc.update(chunk, chunk_id=cid)`` matching the current mixle API.
* Docs distinguish triage timeouts from public release evidence.
* The docs tree is Sphinx/reStructuredText only.
* Installation docs point at sibling checkouts through relative paths rather
  than developer-local absolute paths.
* Validation docs require explicit skip/block reasons for notebooks that need
  optional data, JVMs, GPUs, PDE dependencies, or external services.

Fixed
~~~~~

* Removed release-specific page naming from high-level navigation.
* Documented that output-only notebook churn should not be treated as source
  quality improvement.
* Clarified that a short timeout sweep is useful triage but not proof that
  long-running notebooks are release healthy.

Release Gate
~~~~~~~~~~~~

A public release is not complete until shipped notebooks and examples execute
against release code or have documented exclusions, strict Sphinx docs pass,
and the coordinated family manifest records the exact notebook package commit.
The release record should include the kernel, timeout, worker count, execution
scope, failed notebooks, skipped notebooks, blocked prerequisites, and whether
outputs were intentionally refreshed.
