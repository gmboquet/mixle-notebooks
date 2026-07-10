Reproducibility Policy
======================

``mixle-notebooks`` is public documentation and executable evidence. A notebook
does not need to be fast, but readers should know whether it is expected to run
in a short smoke test, a longer validation job, or a manual environment with
optional services.

Notebook Tiers
--------------

Smoke
    Runs quickly on a developer laptop with local fixtures only. Smoke
    notebooks should avoid network calls, paid providers, and heavyweight
    training loops.

Validation
    Exercises a meaningful workflow and may take longer, but should still be
    deterministic enough for release validation. These notebooks should record
    seeds and data versions.

Manual
    Requires optional credentials, large downloads, specialized hardware, or
    interactive judgment. Manual notebooks should say why they are manual and
    what output a reviewer should expect.

Metadata Requirements
---------------------

Each maintained notebook should make the following visible near the top:

* purpose and package surface exercised;
* expected tier;
* required data files or download instructions;
* optional credentials or services, if any;
* approximate runtime on a normal laptop;
* random seed policy; and
* generated artifacts that should not be committed.

Execution Rules
---------------

Release validation should prefer deterministic execution:

* restart the kernel before running a notebook;
* execute cells in order;
* use local fixture data where possible;
* avoid hidden state from previous notebooks;
* make skipped cells explicit; and
* capture failures with the notebook path, cell number, timeout, and exception.

If a notebook cannot run under a short timeout, that is not automatically a
bug. It should, however, be classified so reviewers can tell a slow validation
workflow from bitrot.

Output Hygiene
--------------

Notebook outputs are useful when they document expected behavior, but they can
also hide drift. Public notebooks should avoid committing:

* large binary outputs;
* private data previews;
* local absolute paths;
* credentials or tokens;
* environment-specific warnings; and
* generated files that belong under ignored build or artifact directories.

Cross-Package Coverage
----------------------

The catalog should make clear which sibling package a notebook exercises:
core Mixle APIs, PDE modeling, MLOps gateway behavior, demo assets, knowledge
contracts, mobile bundle preparation, or discrete algorithms. That mapping is
what turns notebooks into release evidence instead of loose examples.
