# Release checklists

This folder is the tracked, public record of what has to be true before a `mixle-notebooks` release
ships. It mirrors the process used by `mixle` core, adapted for a repository whose product is a
collection of **executable notebooks** rather than a published package.

- **`<version>.md`** (`0.7.0.md`, `0.7.1.md`, …) — one checklist per release, created when
  preparation begins and updated in place *with evidence* as gates are verified. It stays in git
  history after the release ships, so anyone can see exactly what was checked, how, and when.
- **`lessons-learned.md`** — a cumulative, cross-release record of what went wrong (or nearly did),
  where each lesson is tied to the checklist gate that now catches it. This is what keeps the
  checklist from being a static wish-list: it grows from real failures.

This is a checklist of **gates**, not a task list. An unchecked item means the release is not
ready, full stop — there is no "ship now, verify later" for anything marked here.

## Scope

This tracks `mixle-notebooks`: the notebooks, their helper modules, their data-prep scripts, and the
Sphinx docs in this repository. Each release **targets a specific `mixle` version** (0.7.0 for this
release) and every shipped notebook must execute against a clean install of that version, or be
explicitly marked blocked with a reason. Sibling packages a notebook may need (`mixle-pde`, a Spark
JVM, an MPI runtime, GPU/transformer weights) are the reason a notebook is *blocked*, not an excuse
to skip it silently — the version and prerequisite are part of the evidence.

Unlike `mixle` core, this repository is **not published to PyPI**. "Publication" here means the
release branch is merged to `main`, tagged, and (optionally) the docs are rebuilt and deployed to
GitHub Pages.

## Status legend

| Status | Meaning |
| --- | --- |
| `TODO` | Required, no evidence yet. |
| `PARTIAL` | Some evidence exists but doesn't cover the exact release commit, or is otherwise incomplete. |
| `DONE` | Verified against the exact commit that will be (or was) released, with evidence recorded inline. |
| `EXCLUDED` | Explicitly out of scope for this release, with a one-line reason. Silence is not the same as excluded. |
| `BLOCKED` | A notebook that cannot execute in the release environment because it needs an unavailable prerequisite (GPU, JVM, PDE stack, private data). The prerequisite is named; the notebook is not counted as passing. |

## Evidence discipline

A gate is `DONE` only when the entry names, at minimum:

- the command run;
- the commit SHA it was run against;
- the target `mixle` version it was run against;
- the result (pass/fail, with the actual number — "96/102 executed" not "notebooks ran");
- the date.

"It rendered fine last month" does not satisfy a gate for the current tip. A notebook whose source
or whose target `mixle` version changed since the last green run needs a fresh execution — a stored
output cell is not evidence that the notebook still runs.

## What's checked here

The gate categories run pre-flight → verify → publish:

- **Branch / CI state** — the release branch is current, `main` is not ahead, no pre-existing tag.
- **Version and metadata** — the docs `release`/`version`, the `CHANGELOG.md` entry, and the target
  `mixle` version are all set and consistent.
- **Environment** — a clean, isolated environment installing the *target* `mixle` version (not a
  warm dev tree), with the resolved dependency set captured.
- **Notebook execution (the core gate)** — every shipped notebook executes end-to-end against the
  clean install, or is `BLOCKED` with a named prerequisite. Recorded in an execution manifest with
  the kernel, timeout, per-notebook status, and first meaningful failure.
- **Dependency correctness** — `requirements.txt` matches what the notebooks import; sibling-package
  pins are recorded.
- **Documentation** — the Sphinx docs build strict (`-W --keep-going`), the catalog matches the
  notebooks actually present, and process references resolve within the repo.
- **Hygiene** — no secrets or private paths in outputs, no oversized data committed, clean
  commit/author history.
- **Reproducibility** — the environment freeze and the target `mixle` version are captured so a
  reviewer can reproduce the execution evidence.
- **Publication** — merge the release branch to `main`, tag it, and rebuild/deploy the docs.
- **Sign-off** — a named, dated release decision, only after everything above is `DONE`,
  `EXCLUDED`, or `BLOCKED`-with-reason.

## Using this for a new release

1. Copy the most recent release's file as a starting template — the shape doesn't change much
   release to release, but re-verify every gate; don't carry over old evidence.
2. Fold in every open lesson from `lessons-learned.md`: each one should already correspond to a gate
   in the template. If a past lesson has no gate yet, add it before you start.
3. Update the version-specific specifics (target `mixle` version, changelog section, any new gates).
4. Work through it in roughly top-to-bottom order — branch/CI state and version metadata gate
   everything after them.
5. Commit progress as you go, in the open, so the file's git history shows how the release actually
   got verified, not just a final "all green" snapshot.

## Closing the loop after a release

The checklist only gets better if failures feed back into it. After each release — or each release
*attempt* that got blocked — run a short retrospective (`lessons-learned.md` describes the steps):
write up what went wrong or nearly did, and for each item, add or strengthen the gate that would
have caught it, in the same change. A lesson that doesn't change the checklist is just a story.
