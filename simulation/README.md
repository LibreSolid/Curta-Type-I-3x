# Curta simulation — implementation in progress

The complete standard STEP assembly now builds in solid-node: all 547 leaf
occurrences, plus the manual's three clearing-strip prints omitted from the STEP,
organized into educational show/hide layers. The root has
calculator controls, working input selectors, subtraction lift, keyed-shaft
motion, lifting/shifting carriage, clearing plate and prescribed sub-turn dial
rotations. Input, bevel, carry and clearing contact contracts now pass, as does
the bell spring's full subtraction sweep. **Register detents, the whole-machine
seat inventory and final demonstration verification remain open; this is not a
delivered calculator simulation.** Follow the
[implementation tasks](../openspec/changes/simulate-the-curta/tasks.md).

Work starts from the previous [assessment](assessment.md). The new
[measurements and validation findings](docs/measurements.md) identify the invalid
spring, distinguish the hardware products sharing names, and document why the
rest assembly's integrity tests currently fail. The invalid spring has an
explicitly authorized, documented replacement; upstream geometry is untouched.

## Run

From this project's root, with the workspace venv active:

```sh
solid build
solid snapshot -o snapshot-rest.png --autocenter --viewall
python -m unittest simulation.test_source
solid test --faceted simulation/standard/assembly.py
solid test --exact simulation/curta.py
python -m simulation.tools.probe
```

Without activating the workspace environment, use `../../../.venv/bin/solid`
and `../../../.venv/bin/python` in this checkout. The exact root test is
intentionally failing until the recorded source findings are resolved. A
successful build alone is not an assembly-validation result.

Independent subassemblies are inspectable by explicit class reference:

```sh
solid build simulation/standard/assembly.py:UpperFrame1
solid build simulation/standard/assembly.py:MainAxleStepDrum1
solid build simulation/standard/assembly.py:LowerFrame1
solid build simulation/standard/assembly.py:DigitSelectorAxle1
solid build simulation/standard/assembly.py:Carriage1
solid build
```

The last command restores the complete model as the published viewer document.
No floor or development server is launched by these commands.

### Calculator page

The project-owned page adds retained calculations and recursive layer controls
over the public solid-node viewer. Export, then serve the project root locally:

```sh
solid export -o _build_export
python -m http.server 8766 --bind 127.0.0.1
```

Open `http://127.0.0.1:8766/simulation/viewer/`. Set the eight input sliders or
type an exact input, then turn the crank. Completed turns become the next starting
registers; repeated turns and decimal shifting support multiplication. “See
inside” hides the enclosure, frame and carriage covers/supports. The assembly
tree independently hides, shows and focuses every subtree. Session values live
in the page and reset on reload. A partial turn can be inspected but not committed.
The carriage-lift slider exposes the 6 mm disengagement stroke and compressing
spring. Changing decimal position lifts, shifts and reseats the carriage; crank
controls are disabled while lifted or between detents. Completed turns are kept
before manual lifting. The model has eight independent drivers; the eight digit
sliders are a convenient presentation of its single exact operand driver.

The readouts calculate with the verified arithmetic convention; they do not turn
the currently incomplete mechanical motion into a validated whole machine.

Six worked examples cover addition, carry, full overflow, subtraction, decimal
shifting and clearing. “Load and run example” replaces the current page registers;
pause at any point to inspect the mechanism. The underlying instructions are
`Rest`, `Set one`, `Turn crank`, `Lift carriage`, `Shift ×10`, `Seat carriage`,
and `Clear both`. Use lift → shift → seat in that order; `Rest` resets a
reproducible pose, not a claim that a physical crank can run backward.

## Source mapping

- `curta.py`: the manifest's root, calculator controls and register-state relation.
- `assemblies.py`: seven educational layers, with separate result/turns registers,
  carriage covers, input banks, drive and carry subassemblies.
- `mechanism.py`, `drive.py`, `selectors.py`: named joints and drive relations.
- `arithmetic.py`: reproducible arithmetic; six calibration/operation tests pass.
- `registers.py`: seventeen radial dial joints and measured source clocking.
- `transmission.py`: result/turns banks with sliding inputs and keyed rotation.
- `cycle.py`, `carry_motion.py`: sub-turn input, decimal complement, measured pin
  approach, retained carry and reset-cam timing.
- `input_mesh.py`, `bevel.py`: exact-verified single-interface engagement benches.
- `bevel_bank.py`: the installed seventeen-channel interface, including all six
  carriage detents and lifted intermediate positions; both kernels pass.
- `demo.py`: stepped demonstrations and replay checks shared with the page examples.
- `engagement.py`: complete printed-drum contact sweeps, passing both kernels.
- `carry.py`, `standard/carry.py`: fifteen sliding carry levers and stationary bearings.
- `carry_spring.py`, `detents.py`, `carry_seat.py`: spreading U-wires, measured
  detent profiles and explicit mounting-groove fits; twelve tests pass both kernels.
- `clearing.py`: the manual's two opposed tooth strips and spacer, formed from
  the author's flat STLs into the measured cover groove, with a local retaining-
  screw relief. Every tooth remains unchanged; clearing contact passes both runners.
- `retaining_spring.py`, `bell_spring_motion.py`: the bell's native mounting plate
  and hooks, joined by measured ribbed flexible arms following the drum pockets.
- `views.py`: explicit inspection poses for snapshots at driver defaults.
- `positioning.py`: moving spring seat and port-driven carriage spring compression.
- `zero.py`: retained zero cam, sliding drive pin, grouped roller/lever and moving
  spring terminal, with six passing contact/mount contracts on both kernels.
- `pawl.py`, `pawl_spring.py`: measured anti-reversal ratchet following, reverse
  blocking and a seven-turn spring fitted between the plate and moving pawl.
- `bearing.py`: bevel-tip/frame bearing clearance after the axial fit.
- `prints.py`, `standard/printed.py`: printed bodies from exact STEP ingredients.
- `fit.py`: explicit, documented assembly and tooth-outline fit corrections.
- `viewer/`: the educational calculator page and tested page-local accumulator.
- `flexibles.py`: the documented zero spring and source-sized carriage spring.
- `contracts.py`: material connectivity that distinguishes enclosed voids from
  detached positive-volume bodies; rigid bodies and flexible material patches
  are checked. A reconstructed spring still counts as one physical occurrence.
- `standard/parts.py` and `standard/assembly.py`: compacted output of
  `solid import-step`, with source product names and all source placements.
- `source.py`: creates the ignored STEP import copy with unique names for
  otherwise ambiguous products. A restoration test proves every other byte
  remains upstream's.
- `standard/test_assembly.py`: verifies the world placement of every mesh against
  the source occurrence. A deliberate 1 mm crank misplacement was detected.
- `test_curta.py`: inventory, connectivity, source validity and interference
  contracts. Failed contracts are retained.
- `tools/probe.py`: reproducible measurements and housing-interface diagnostics.
- `tools/compact_import.py`: one-time mechanical cleanup of a fresh scaffold;
  do not rerun it over edited mechanism code.
- `tools/check_calculator.py`: reproducible headless browser calculation and layer checks.

The ignored import copy is prepared automatically when the parts module loads.
If the upstream CAD file changes during a live session, explicitly run
`python -m simulation.source`, rebuild, and run the placement contract. The live
watcher sees the generated import copy; it does not watch its upstream input
through this preprocessing step. Changes to hierarchy require reviewing the
generated source mapping, not just refreshing that copy.

## Current findings

The lighter spring tessellation retains the same spline and wire dimensions:
Molejo samples per spline span, so four samples per span provide 128 rings per
coil. The previous 1,000-per-span setting created almost eight million triangles
and stalled software-rendered browser interaction. A geometry/mesh-budget test
now passes below 50,000 triangles; the original exact wire shape is unchanged.

The invalid STEP product is the zero-positioning spring (#419219). Automatic
repair remains invalid and splits it into two native solids. The pilot authorized
the documented spring. Its installed shape uses the manual's 1.1 mm wire and five
counter-clockwise turns, with terminal placement and installed bore fitted to the
measured mounting parts. Native validity, wire-size and both faceted/exact mounting
contracts pass. The 11.5 mm winding mandrel is distinguished from installed bore;
springback and force are not predicted. See the measurements for the fit decision.

The original STEP digits-cover / upper-housing intersection returns invalid
geometry. The operating model now uses the author's original print STLs for
those two parts and the crank collar, whose STEP tessellations are not watertight.
The replacement files are valid, but a positive nominal housing overlap remains;
the complete nominal overlap inventory is not yet established. See the measurements
for the current diagnostic evidence. Working motion and arithmetic are not a
claim of complete physical validation or fabrication readiness.

The project-owned OpenSpec change is `simulate-the-curta`. Its planning commit is
`05165d3`; it remains active and unarchived. Current controls describe an operation
from explicit starting registers: changing crank progress is reproducible, rather
than accumulating hidden Python state. The calculation-facing page retains
completed operations while the underlying model stays scrub-friendly.

## Attribution

This simulation layer uses Marcus Wu's Curta-Type-I-3x source and retains this
repository's CC BY-NC-SA 4.0 license and acknowledgments. The standard design is
used; none of the optional modifications has been selected. The historical
assessment remains unchanged as the record of the earlier research session.
