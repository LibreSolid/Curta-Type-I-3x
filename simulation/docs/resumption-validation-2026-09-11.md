# Resumption validation — 2026-09-11

This records the cover-fit increment after the export-memory fix. It is not
whole-machine acceptance: the OpenSpec change remains active and unarchived.

Framework: `5e591474b5cf54c2b41f223400d2b6ee3cbb97ae` (`expression-graphs`, ADR-101).
The starting project checkpoint was `d80e7bf`, the initial 10h Astra/xhigh sprint.
No motion-law adaptation was needed to use the merged framework.

## Export and calculator

The initial fresh export passed in 25.66 s at 613820 KiB peak process RSS.
This was a new publication using the existing CAD cache, not a cold-cache build.
Its schema-4 manifest contained all eight drivers, seven instructions and seven
root teaching layers. The browser passed page-53 calibration, all six examples,
retained operations, lift/shift guards, eight input sliders, layers and capture.
That initial export preceded the cover fits. After the full regression, a finite
root build passed in 41.69 s at 613928 KiB peak process RSS, and the refreshed
export passed in 41.43 s at 817216 KiB. These also used the existing CAD cache.

The refreshed build document is 840296 bytes; the export manifest is 1670616
bytes. Both are schema 4 with 9969 bindings, eight drivers, seven instructions,
seven teaching layers, 390 rigid published leaves, 38 flexible leaves and all
six colors. The two fitted covers and seventeen fitted axles are present.
Every referenced model exists, and SHA-256 comparisons match all 390 rigid
occurrence artifacts between build and export. This publication count is not
the separately tested 547 STEP occurrences plus three supplemental prints.

The refreshed browser check passes in 103.06 s: page-53 calibration, all six
worked examples, retained operations, lift/shift guards, eight selector controls,
recursive layers and capture, with no page errors. The capture was inspected:
the calculator controls and silver/bronze/black internal contrast are visible.
The browser runs without the CAD address-space guard because Chromium reserves
large virtual ranges; the test closes its own browser and loopback server.

Five OpenSCAD snapshots at 1400 × 1100 were rendered and inspected: complete
assembly, exposed mechanism, upper-housing axle pockets, digit-cover inner land,
and the moving register detents. The cover views show intact windows and threads,
shallow flange pockets and no detached fins. The sub-millimetre seat dimensions
are proved by the contracts, not inferred from pixels. Standalone cover views use
OpenSCAD's default diagnostic color; the assembled covers remain black.

Snapshot references are `simulation/curta.py:Curta`,
`simulation/views.py:InsideCurta`, `simulation/cover_fits.py:FittedUpperHousing`,
`simulation/cover_fits.py:FittedDigitsCover`, and
`simulation/views.py:RegisterDetentMoving`. In that order, the seven-component
camera values are `0,0,0,55,0,25,650`, `0,0,0,55,0,25,650`,
`0,0,22,35,0,15,450`, `0,0,-6,145,0,15,450`, and
`0,0,0,45,0,25,450`. Use `--autocenter --viewall --projection ortho` and the
stated image size. Images/logs are `_build_evidence/resume-{assembled,inside,
housing,digit-cover,moving-register}.png` and `resume-snapshot-<pose>.log`.

After inspection the finite full-root build was restored successfully in
44.33 s at 608672 KiB peak process RSS. Its seven-layer document has no errors
record, and all 390 rigid artifact hashes still match the browser-tested export.

## Regression

All 37 tested node modules were run sequentially with the faceted runner:
142/144 tests pass, with 1131.43 s summed process wall time and 799256 KiB
maximum process RSS. These are per-process measurements, not aggregate cgroup
memory. Jobs used an 8 GiB address-space guard and one BLAS/OpenMP thread.

The same 37 modules also completed the native runner: 143/144 tests pass,
with 3071.57 s summed process wall time and 1275152 KiB maximum process RSS.
The one native failure is the unchanged cover/housing thread contact below.
The framework remained at the recorded commit throughout both matrices.

| Node module (`simulation/`) | Faceted passed/total | Native passed/total |
| --- | ---: | ---: |
| assemblies.py | 3/3 | 3/3 |
| bearing.py | 0/1 | 1/1 |
| bell_spring.py | 8/8 | 8/8 |
| bevel.py | 2/2 | 2/2 |
| bevel_bank.py | 2/2 | 2/2 |
| carry.py | 12/12 | 12/12 |
| carry_bank.py | 4/4 | 4/4 |
| carry_contact.py | 6/6 | 6/6 |
| carry_fits.py | 8/8 | 8/8 |
| carry_heads.py | 2/2 | 2/2 |
| carry_mesh.py | 3/3 | 3/3 |
| clearing.py | 4/4 | 4/4 |
| clearing_contact.py | 5/5 | 5/5 |
| clearing_fasteners.py | 1/1 | 1/1 |
| clearing_stop.py | 7/7 | 7/7 |
| covers.py | 7/7 | 7/7 |
| curta.py | 12/13 | 12/13 |
| demo.py | 2/2 | 2/2 |
| dial_detent_bank.py | 4/4 | 4/4 |
| dial_detents.py | 5/5 | 5/5 |
| dial_fits.py | 4/4 | 4/4 |
| display.py | 2/2 | 2/2 |
| drive.py | 2/2 | 2/2 |
| engagement.py | 2/2 | 2/2 |
| flexibles.py | 3/3 | 3/3 |
| frame.py | 2/2 | 2/2 |
| input_mesh.py | 2/2 | 2/2 |
| pawl.py | 6/6 | 6/6 |
| positioning.py | 2/2 | 2/2 |
| prints.py | 3/3 | 3/3 |
| registers.py | 3/3 | 3/3 |
| selectors.py | 1/1 | 1/1 |
| spider_bank.py | 2/2 | 2/2 |
| spider_shape.py | 2/2 | 2/2 |
| standard/assembly.py | 1/1 | 1/1 |
| transmission.py | 2/2 | 2/2 |
| zero.py | 6/6 | 6/6 |

## Findings retained

- The bearing's faceted test reports `0.0000032402102747 mm³` contact. Its native
  check passes (1.08 s). This is a mesh-precision disagreement, not an overlap
  waived with an epsilon or a reason to alter the native fit.
- The root still fails at the digit-cover/upper-housing thread intersection:
  `224.32750533797636 mm³` on both runners (both covers are source STLs).
  Its other twelve tests pass on both runners,
  including every represented source occurrence, material integrity and validity.
  The upstream seat inventory and remaining moving frame/control interfaces must
  be resolved before the ordinary root assertion can be replaced by an honest
  exact inventory contract. No part or positive overlap has been omitted.
- Each new cover fit was removed separately in node code: rim facing failed
  three contracts; housing pockets and axle-flat extension failed two each.
  The code was restored and all seven cover contracts passed again.
  All seven also pass on the exact runner in 30.99 s; interfaces involving
  source STLs remain faceted, while the native axle/carrier/collar checks use OCCT.
- The complete native register-detent bank passes all four checks in 457.17 s
  (480.54 s process wall time, 615348 KiB peak RSS). This closes the pre-pause
  compact-cam-law verification gap, including every digit/shift combination,
  carry/subtraction cascades, individual ball capture and progressive clearing.
- The bell spring passes all eight native checks, including its full 37-position
  subtraction sweep, in 923.19 s (944.20 s process wall time, 982660 KiB peak RSS).
  Its long geometric sweep is distinct from the now-resolved export-memory issue.

See [measurements](measurements.md#cover-neighbours--measured-local-fits-after-resumption)
for rejected placements, relief bounds and the one explicitly measured source
facet-diagonal fidelity limit. Upstream STEP/STL files remain unchanged.

## Reproduction

From the project root, in the workspace environment, run each table module with
`solid test --faceted simulation/<module>.py`, then `--exact` for native checks.
Each module has its own ignored `_build_evidence/resume-{faceted,exact}-<module>.log`
(the slash in `standard/assembly` is a hyphen in its log name). Do not treat a
loop finishing as a green suite: inspect each module's failed count.

The final lightweight rerun passes 27 Python unit tests (1.789 s) and five
calculator JavaScript tests. `openspec validate simulate-the-curta --strict`
passes. The change remains active with 7/17 tasks complete; these full regression
runs do not close final acceptance while the root contact assertion is red.

## Next mechanical increment

The memory-dependent work is unblocked; no further framework change is needed
to continue. Next isolate the remaining lower-housing/control windows and
frame/carry-guide/carriage passages with measured neighbour contracts. Only
after resolving moving contacts should the fixed source thread and retained-seat
overlaps become an explicit, exact named-pair inventory. New or changed contacts
must still fail, however small. Remaining motion mutations and whole-machine
demonstration sweeps precede final acceptance and OpenSpec archival.

Raw logs, meshes and screenshots remain ignored. The historical memory stop and
framework-cycle handoff remain in [the pause report](pause-report-2026-09-11.md).
