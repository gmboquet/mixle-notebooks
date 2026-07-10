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
