# Curta initial sprint — checkpoint and framework handoff

## Disposition

The initial simulation implementation is **paused, not delivered**. The pilot
chose to address solid-node's symbolic-expression memory growth before resuming
Curta. Preserve the complete mechanism, educational assembly layers, calculator
controls and flexible parts; do not reduce their scope to make an export fit.

As requested by the pilot, this whole initial project effort is recorded as
**one 10h sprint of Astra on xhigh**. This is the pilot's run attribution, not
a duration inferred from Git timestamps or a numbered shop sprint.

The project-owned change is
[`simulate-the-curta`](../../openspec/changes/simulate-the-curta/tasks.md).
Its planning commit is `05165d3`; implementation checkpoints run from `8467373`
through `208b828`, followed by the commit containing this report. The earlier
assessment is preserved in `6d903d0`. All work belongs to this independent
project repository; upstream CAD, STLs, manual, drawings, README and license
are unchanged from source commit `7023381a6d1c8797d84ae146abf47f4403b7f780`.

The OpenSpec change remains active with its unfinished tasks unchecked. Planning
status `isComplete: true` means the planning artifacts exist, not that the
simulation is complete. No baseline promotion or archive is justified yet.

## What the sprint produced

- A traceable operating assembly containing all 547 STEP occurrences and the
  manual's three clearing-strip prints missing from that STEP: 550 physical
  occurrences, represented by 588 material leaves after flexible reconstruction.
- Seven mechanically meaningful navigation layers, with individual digit banks,
  carriage covers and supported fasteners grouped for hide/show and inspection.
- Eight model drivers, a calculation-facing page with eight digit sliders,
  retained completed operations, six worked examples and seven instructions.
  Motion remains reproducible from explicit starting registers and controls.
- Named motion joints and relations for the crank, selectors, keyed shafts,
  subtraction lift, transmission, fifteen carries, carriage, clearing, seventeen
  dials and detents, zero cam, pawl, bell spring and clearing stop.
- The pilot-authorized documented zero-positioning spring, measured flexible
  carry wires, carriage/pawl/stop springs, bell arms and tapered spider fingers.
- Material-inspired aluminum, bronze, brass, steel, black and ivory colors.
  These teach the mechanism; they are not fabrication-material claims.
- Reproducible measurement tools, source-drift checks, red-first contact tests,
  scoped fit corrections and a growing record of unresolved interfaces.

The detailed chronological evidence is in [measurements.md](measurements.md).
Many component interfaces passed both faceted and exact runners at their
respective checkpoints. Those results do not amount to a final all-node
regression, a complete interference inventory or whole-machine certification.

## Why work stopped

Fixed numeric poses and inspected snapshots work. Fresh interactive export
fails when solid-node evaluates the same motion laws with symbolic drivers.
Its solid2 `OpenSCADConstant` arithmetic eagerly interpolates each input's
complete expression into another string. Reuse therefore becomes duplication;
composing profiles and distributing their outputs multiplies that duplication.

The observed chain is calculator arithmetic → register position → carry
engagement → hook-spreading profile → six wire coordinates, repeated across
the result and counter banks. The failure is in symbolic relation evaluation,
not a CAD Boolean or the color palette.

The bounded probe in [`tools/expression_size.py`](../tools/expression_size.py)
uses short symbolic tokens, making these lower-bound text-size measurements:

| Quantity | Observed size |
| --- | ---: |
| One result-shaft turn expression | 121,309–121,322 characters |
| One active result-carry expression | 7,679,897–7,723,347 characters |
| Carry input occurrences in the hook profile | 35 |
| Estimated expanded hook expression | 268,799,255–270,320,005 characters |
| Counter hook expression | approximately 54.8 million characters |

The probe does not allocate the estimated final hook expressions. It completed
in 3.59 s with 664,636 KiB peak RSS. Copying those expressions into coordinates
and retaining intermediates explains why a modest equation system can consume
gigabytes; these estimates are not a direct measurement of total export memory.

| Bounded export attempt | Wall time | Peak RSS | Outcome |
| --- | ---: | ---: | --- |
| Compact ball law, 4 GiB address-space limit | 37.60 s | 3,526,084 KiB | `MemoryError` |
| Compact ball law, 8 GiB address-space limit | 53.11 s | 7,823,896 KiB | `MemoryError` |
| Additional algebraic simplification, 8 GiB limit | 81.63 s | 5,651,560 KiB | `MemoryError` |
| Direct maximum, 8 GiB limit | 48.07 s | 7,857,084 KiB | `MemoryError` |

These limits were imposed with `ulimit -v`; they bound address space, not
precisely resident RAM. An allocation can fail below the limit when the next
requested string is too large. Runs were sequential, with one BLAS/OpenMP
thread and `pipefail` so logging could not conceal a failed export. Earlier
unbounded exports were killed by the OS. The pilot separately reported a host
crash during a parallel build; VM evidence does not establish that host's
exact failure mechanism. No host configuration was changed.

The final traceback ends at `detents.spreading` → `solid_node.math.piecewise`
→ solid2's `OpenSCADConstant(f'({self} {op} {other})')`. Other attempts reached
the subsequent spring-coordinate arithmetic before failing. All failed before
writing a fresh manifest.

During the pilot-requested framework diagnosis, read-only source inspection
confirmed the ordering: `core/export.py` enters `symbolic_document` at line
109 and only calls `bind_document` at line 120, after symbolic construction and
serialization. Existing schema-4 sharing therefore runs too late to prevent
this allocation failure. No framework implementation was changed.

## Framework cycle triggered by this project

**Suggested cycle identifier:** `construction-time-expression-sharing`.
**Owner:** the independent solid-node repository, not this project or the shop.
**State at handoff:** empirical finding and proposed scope captured; formal
proposal, ratification, worktree and implementation are pending. No formal
memory-fix cycle has been opened or completed by this project checkpoint.

The inspected framework main was
`2bdc50b37be920e79202d1c9e9c5700e43f525e0`, two commits ahead of its remote.
`openspec list --json` reported no active changes there. The primary checkout
had unrelated changes in `workflow/warts.md` and untracked planning files under
`workflow/docs/`; they were neither staged nor modified. Its dirty state must
be resolved by its owner before the framework workflow selects a clean base.
This report is the portable project-side handoff; copying the finding into the
framework's wart record belongs to that separate cycle.

The relevant accepted decision is
[ADR-080](https://github.com/LibreSolid/solid-node/blob/main/docs/adrs/EXPORT/ADR-080-a-shared-subexpression-is-named-once.md).
It explicitly deferred construction-time expression graphs because the earlier
clock case was manageable. Curta provides the missing producer-memory evidence.

Recommended direction for the proposal:

1. Preserve shared expression structure during arithmetic, math calls and
   motion propagation, instead of eagerly expanding expression text. Reusing
   an expression should retain a reference to it.
2. Emit the existing schema-4 bindings directly from that structure where
   possible. Keep the project's ordinary motion API and numeric behavior.
   Keeping an eagerly expanded string alongside a graph would not fix memory.
3. Explicitly handle compatibility with direct solid2 expressions, animation
   time, flexible ports, declarations and OpenSCAD output. Reuse of the current
   viewer format is a design objective, not a verified compatibility claim.
4. Scope caches or interning to an evaluation/document lifetime; do not replace
   expansion with an unbounded global retention problem.

Early automatic bindings at motion-port boundaries are a narrower alternative,
but cannot prevent expansion inside a single law. A compact piecewise/lookup
primitive could reduce one multiplier but does not fix general duplication and
may require a separately owned viewer change. Raising RAM or baking a small
set of poses does not meet the requested freely adjustable calculator behavior.

The framework cycle's proposed proof is a red-first, CAD-free reproducer through
the actual symbolic producer; bounded scaling with repeated expressions and
fan-out; independent numeric/expression parity and compatibility tests; and a
full Curta export measured under the 8 GB budget. A small final JSON file alone
is insufficient proof. Run the six calculator examples, retained operations,
sliders, layers and flexible motion against the newly generated document before
claiming originating-project validation. These are handoff recommendations,
not newly ratified framework requirements.

## Last project changes preserved in this checkpoint

The native circular dial cam replaces a long piecewise ball-rise expression
with a compact geometric law, retaining the measured table as an independent
reference. Equivalent algebra simplifies decimal shifting, tooth-count
denominators and carry maxima. These passed their relevant red-to-green tests
but did not solve the full export; no springs or controls were removed.

The cover-datum trial re-centers and clocks the author's unchanged cover STLs
and adds a .05 mm seating gap. The dial-window sweep passes, but adjacent
interfaces are **not accepted**: the digits cover intersects the clearing cover
by 91.212554578 mm³, and the digits-cover and upper-housing intersections with
individual fixed digit axles are approximately .2315 and 2.61817 mm³. Preserve
the trial, its tests and source-datum probe for continuation; do not enter these
as approved nominal seats merely to make the root green.

Checkpoint verification and remaining boundaries:

- Fresh checkpoint unit run: **26 passed**, covering arithmetic, cycle,
  compact cam, expression size, carry timing and source preservation; 5.08 s
  wall time, 640,760 KiB peak RSS.
- Fresh cover faceted checkpoint: **3 passed**, 36.35 s process wall time,
  615,952 KiB peak RSS. The runner's test-only time was 18.02 s.
- Checkpoint hygiene: strict non-interactive OpenSpec validation, Python
  compilation of `simulation/` and `git diff --check` pass. No unfinished
  implementation task was checked off or archived to obtain that result.
- Compact-cam first-station native contacts: **5 passed**, 11.43 s, before
  this housekeeping pass. Complete-bank faceted run: **4 passed**, 73.67 s.
  The complete-bank exact run for this latest compact law is still pending;
  the earlier sampled-law exact result is not a substitute.
- Cover trial: original faceted contracts failed with approximately 18.31 and
  18.33 mm³ dial interference; the fitted trial passed **3 checks on each
  runner**, including original print-vertex preservation. Adjacent interfaces
  remain outside that narrow green result.
- Material palette: **2 checks passed on each runner** at `208b828`; assembled
  and inside snapshots were visually inspected at 1400 × 1100. No new visual
  evidence was generated during housekeeping.
- Full symbolic export, current browser validation, whole-machine seat inventory,
  all demonstration interference sweeps, remaining mutations and final faceted/
  exact regressions are unfinished. The root's known interference failure is
  retained; this checkpoint does not claim a green full suite.

At pause, `_build_export/manifest.json` was dated 2026-09-11 10:13 UTC and
`_build/viewer.json` 13:09 UTC. Both predate the final mechanism. The browser
preflight rejects the old palette; it is not a general source-freshness proof.
Do not use those documents or an earlier successful browser run as current
acceptance evidence.

## Reproduction and restart

From the project root, use the workspace environment, not a separate host build.
The small diagnostic can be run without attempting the full export:

```sh
set -o pipefail
ulimit -v 8388608
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 SOLID_BUILD_DIR=_build_checks
../../../.venv/bin/python -m simulation.tools.expression_size
../../../.venv/bin/python -m unittest simulation.test_arithmetic simulation.test_cycle simulation.test_dial_cam_law simulation.test_expression_size simulation.test_carry_timing simulation.test_source
```

The inspected environment reported solid-node 0.6.0, solid-node-viewer 0.1.0
and molejo 0.2.0 as installed package metadata. The local framework source is
the main commit recorded above, not an assumption that released 0.6.0 contains
all of that main's APIs; viewer 0.1.0 remains founded, not released.

After the framework cycle is implemented and authorized for integration:

1. Record the actual framework planning, implementation and integrated commits
   here, plus the tested viewer version/content if it changes.
2. Re-run the small reproducer, then one bounded full export, recording peak
   RSS, elapsed time and fresh artifact identity. Only then validate the page.
3. Resume the cover/window neighbors and frame/guide interfaces. Re-run the
   compact-cam exact bank, carry, clearing and any interface affected by a fit.
4. Finish the complete moving-interface review and named fixed-seat inventory,
   every demonstration sweep and outstanding mutation proof. The earlier audit
   found 67 moving overlap pairs, not 67 approved seats or distinct families.
5. Run every node's required regressions, build and inspect current snapshots
   and the viewer document, then validate, sync and archive the project change.

Raw logs, meshes, snapshots, import copies and build directories stay ignored
and preserved locally. Their essential results are transcribed above and in
the measurements so a clean clone has the handoff; the committed probes and
tests reproduce them. No push, publication or framework integration is part of
this checkpoint.
