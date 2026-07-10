Notebook Authoring Guide
========================

``mixle-notebooks`` should contain runnable learning and benchmark artifacts,
not stale screenshots of old APIs. A notebook is documentation, test surface,
and user onboarding all at once.

Notebook Structure
------------------

A release-quality notebook should include:

``purpose``
    One short opening cell that says what the notebook demonstrates.

``environment``
    Imports, package versions when useful, optional dependency notes, and data
    requirements.

``data setup``
    Deterministic synthetic data generation or clearly documented public data
    loading.

``workflow``
    Small steps that map to public APIs. Avoid hidden state and out-of-order
    execution.

``validation``
    Assertions, metric checks, shape checks, or plotted diagnostics that prove
    the example ran correctly.

``limitations``
    Runtime, stochastic behavior, heavy dependencies, or intentionally mocked
    steps.

Execution Rules
---------------

Every notebook should run from a clean kernel. Use deterministic seeds unless
the notebook is explicitly about stochastic variation. Avoid depending on
files outside the repository unless the first cells download or generate them
with a documented source.

Notebook outputs should be regenerated when APIs, seeds, data, or dependency
versions change. A saved output from an older release is not evidence that the
current notebook still works.

Dependency Policy
-----------------

Keep optional dependencies visible:

* place heavyweight imports near the cell that needs them;
* explain GPU, JVM, PDE, or cloud requirements up front;
* skip or split notebooks that cannot run on a normal development machine;
* pin or constrain tutorial environments for release execution;
* avoid secret-bearing environment variables in saved outputs.

When a notebook depends on a sibling package, prefer the released package
version for public docs. Git URLs should be used only with an explicit
reproducibility note and commit pin.

Review Checklist
----------------

Before a notebook is linked from public docs:

1. Execute it top-to-bottom on a clean kernel.
2. Confirm the first meaningful failure is recorded if it does not pass.
3. Check saved outputs for secrets, private paths, and stale warnings.
4. Confirm synthetic data is labeled.
5. Confirm plots and tables match the current code.
6. Add the notebook to the execution manifest with status and timeout policy.
