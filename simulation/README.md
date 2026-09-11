# Curta simulation — implementation in progress

The complete standard STEP assembly now builds in solid-node: 547 placed leaf
occurrences, now organized into educational show/hide layers. The root has
calculator controls, working input selectors and crank/drum motion. **Complete
register motion, engagement verification and demonstrations are still being
implemented; this is not a delivered calculator simulation.** Follow the
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

## Source mapping

- `curta.py`: the manifest's root, calculator controls and register-state relation.
- `assemblies.py`: seven educational layers, with separate result/turns registers,
  carriage covers, input banks, drive and carry subassemblies.
- `mechanism.py`, `drive.py`, `selectors.py`: named joints and drive relations.
- `arithmetic.py`: reproducible arithmetic; six calibration/operation tests pass.
- `flexibles.py`: the documented five-turn, 1.1 mm wire replacement spring.
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

The ignored import copy is prepared automatically when the parts module loads.
If the upstream CAD file changes during a live session, explicitly run
`python -m simulation.source`, rebuild, and run the placement contract. The live
watcher sees the generated import copy; it does not watch its upstream input
through this preprocessing step. Changes to hierarchy require reviewing the
generated source mapping, not just refreshing that copy.

## Current findings

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
than accumulating hidden Python state. A calculation-facing UI is planned to
retain completed operations while the underlying model stays scrub-friendly.

## Attribution

This simulation layer uses Marcus Wu's Curta-Type-I-3x source and retains this
repository's CC BY-NC-SA 4.0 license and acknowledgments. The standard design is
used; none of the optional modifications has been selected. The historical
assessment remains unchanged as the record of the earlier research session.
