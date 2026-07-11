# Release lessons learned

A cumulative, cross-release record of things that went wrong — or nearly did — while releasing
`mixle-notebooks`, so the same mistake is caught by process next time instead of by luck.

## The rule that keeps this useful

A lessons-learned log that is only a list of war stories rots into something nobody reads. This one
has one rule: **every lesson must terminate in a checklist gate.** Each entry ends with either

- **→ Gate:** the checklist item (existing or newly added) that now catches this class of failure; or
- **→ No gate:** an explicit, dated decision that a gate isn't worth it, and why.

If a lesson can't be turned into a gate or a deliberate no-gate decision, it isn't done being
understood yet. When you add a lesson here, you add or strengthen the gate in the current release
checklist in the *same* change — that is the whole point of writing it down.

## How to run a release retrospective

After each release (or after a release *attempt* that got blocked), before the memory fades:

1. Walk the release checklist and this session's history. For every gate that was `TODO`/`PARTIAL`
   at the end, every fire drill, and every "we almost shipped X" — write it up below under that
   release's heading.
2. For each, find the gate that would have caught it. If the gate exists, note that it worked (or
   why it didn't fire). If it doesn't exist, add it to the checklist template and reference it here.
3. Keep entries concrete: the actual symptom, the actual root cause, the actual command that now
   catches it. "Be more careful" is not a lesson.

---

## 0.7.0

The 0.7.0 cycle was the first time this repository was released against a specific `mixle` version
with an execution-backed process, rather than as a loosely-versioned collection whose health was a
visual spot-check. Most of these lessons are about that gap.

### L-0.7.0-1 — "Notebook health" had been a visual spot-check, not execution evidence

**What happened.** Before this cycle, whether a notebook still worked was judged by whether its
committed output cells looked reasonable. Committed outputs are a snapshot of *some* past run against
*some* past `mixle`; they say nothing about whether the notebook executes against the version being
shipped.

**Root cause.** No gate required re-executing notebooks against the target `mixle` version, and no
manifest recorded which notebooks were actually run.

**→ Gate:** §4, *Notebook execution* — every shipped notebook executes end-to-end against a clean
install of the target `mixle` version, recorded in an execution manifest with per-notebook status
and first failure. A stored output cell is explicitly not accepted as evidence.

### L-0.7.0-2 — A core dependency (`hvis`) changed substantially under a "minor" bump

**What happened.** `mixle.utils.hvis` gained ~3,000 lines across 0.6.2 → 0.7.0 (new `direct`,
`distributed`, `front`, `goals`, `stream`, `topology`, `umap_np` modules and reworked `affinity`/
`embed`/`tsne`). The public `htsne`/`humap` entry points stayed backward-compatible, but nothing
*guaranteed* that until every hvis-using notebook was actually run against 0.7.0.

**Root cause.** A version bump in the target library can change or extend APIs that notebooks depend
on, and "the signature looks compatible" is a guess, not a check.

**→ Gate:** §4 (execution) plus §2's requirement that the target `mixle` version is pinned and named,
so the execution evidence is unambiguously about the version being shipped.

### L-0.7.0-3 — Authored showcase notebooks had narrative that contradicted their own output

**What happened.** While adding 0.7.0 capability-showcase notebooks, two cells shipped a draft whose
prose contradicted the executed result: a spend-ledger count whose inline comment said "2, not 3"
while the cell printed 3, and a calibration claim asserting coverage "survives" composition while a
seed-dependent coverage check printed `False`. Both were caught only by executing the notebook and
reading the actual outputs.

**Root cause.** Narrative written against what the API is *expected* to do, not against what a real
run *did* do.

**→ Gate:** §4 (execution) is necessary but not sufficient; the execution manifest entry for an
authored notebook must confirm the narrative matches the produced outputs, not merely that the cell
ran without raising.

### L-0.7.0-4 — Blocked notebooks must be named, not silently skipped

**What happened.** A meaningful fraction of notebooks require prerequisites the release environment
does not have (the `mixle-pde` physics stack, a Spark JVM, an MPI runtime, transformer/vision
weights). The temptation is to quietly leave them out of the health story.

**Root cause.** "We ran the notebooks" with an unstated exclusion set reads as full coverage when it
is not.

**→ Gate:** §4 records every such notebook as `BLOCKED` with the specific missing prerequisite, so
coverage is honest: passed + blocked-with-reason + failed must account for every notebook in scope.

### L-0.7.0-5 — A notebook kept changing after the execution manifest was written, and nobody re-ran it

**What happened.** `tutorials/embedding_with_htsne.ipynb` was reworked five more times the same day
the execution manifest was produced (protein-family embedding → protein-binding recovery →
edit-distance head-to-head → six-class binding atlas → the final cut, which drops the edit-distance
comparison entirely). The manifest still said "passed" the whole time, but that claim covered
whichever draft existed when the manifest was written, not the notebook that ended up on the branch.
A stale `rapidfuzz` dependency from one of the intermediate drafts also shipped in `requirements.txt`
after the final draft stopped needing it.

**Root cause.** The checklist's evidence discipline requires evidence to cover "the exact commit that
will be released," but nothing forced a re-check when a notebook changed *after* its manifest entry
was written and before the branch was actually released. A checklist gate marked `DONE` earlier in
the same release cycle can go stale mid-cycle.

**→ Gate:** §4 (post-merge re-verification) now explicitly diffs the manifest's source commit against
the release tip and re-executes anything that changed in between, not just anything that changed
since the *previous release*. §5 (dependency correctness) re-derives "what notebooks import" rather
than trusting the requirements list a prior pass produced.

### L-0.7.0-6 — Checklist evidence cited a commit SHA that didn't exist in the repository

**What happened.** The Sphinx docs-build gate's evidence line named commit `bdde3b1` as what was
built and tested. That SHA is not reachable in this repository's history (`git cat-file -t bdde3b1`
fails) — likely copied from a different working state that was later amended or rebased away. The
gate's underlying claim (the docs build strict and clean) turned out to still be true when re-checked
independently, but the evidence as written could not be verified against the actual repository.

**Root cause.** Evidence discipline (see `README.md`) requires a commit SHA, but nothing checked that
the SHA was real. A plausible-looking but unverifiable SHA is worse than an honest "not yet checked,"
because it looks like evidence.

**→ Gate:** when recording a commit SHA as evidence, verify it resolves in the repo you're releasing
(`git cat-file -t <sha>`, or just re-run `git rev-parse HEAD` at the moment you record the evidence)
before writing it down.

### L-0.7.0-7 — A notebook's own output leaked the release owner's local filesystem path

**What happened.** `data_science/market_basket_ibp.ipynb` had a committed output cell printing
`data dir: /Users/grantboquet/codex/mixle-notebooks/data/online_retail_ii` — the absolute path
resolved on whatever machine last executed the notebook before it was committed. Separately,
`tutorials/model_parallel_estimation.ipynb` hardcoded the same kind of personal path
(`/Users/grantboquet/codex/mixle`) directly into example code, as an unnecessary
`sys.path`/`PYTHONPATH` workaround. Neither is a security leak (no credentials, no third-party data),
but both are the kind of "obviously ran on someone's laptop" detail a public release shouldn't ship,
and the hygiene gate had no scan behind it — it was still `TODO` when this pass started.

**Root cause.** No gate actually ran a scan; "no secrets or private paths" was an aspiration, not a
checked claim. A notebook that resolves and prints `Path.cwd()`-derived absolute paths will always
leak whatever machine executed it last, by construction — that's a pattern worth catching, not just a
one-off typo.

**→ Gate:** §7 now records the actual scan commands run (secret-shaped strings, `/Users/`, `/home/`,
email addresses) and their real output, not just a claim. When a notebook diagnostic must show a data
location, prefer a repo-relative path over an absolute one.
