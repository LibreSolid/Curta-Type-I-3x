# Pre-simulation assessment

Assessed on 2026-09-11, before implementation. Source commit:
`7023381a6d1c8797d84ae146abf47f4403b7f780` (`Fix Discord link in README`,
2026-01-15). The project worktree was clean during the assessment.

## Conclusion

Curta-Type-I-3x is a stronger candidate than ReCurta for a staged simulation.
The main advantage is an assembled STEP document with named parts, exact
geometry, and occurrence placements. The illustrated build manual describes
mechanical engagement and gives concrete arithmetic checks. This removes much
of ReCurta's placement reconstruction burden.

The assessment does **not** establish a functioning calculator, a clean
interference sweep, or fabrication readiness. One STEP solid fails native
shape validation, several STL exports have topology defects, and motion/state
behavior remains to be implemented.

## Sources and provenance

| Source | What it contributes |
| --- | --- |
| [Project README](../README.md) | Three-times-scale Curta Type I adapted for FDM printing; BOM, video, and license links. |
| [STEP assembly](../CAD/Curta%20Assembly.step) | Assembly hierarchy, components, placements, exact geometry, and colors. Approximately 25 MB. |
| [Standard STL tree](../STLs/) | Printed parts organized by assembly stage; filenames often encode quantities. |
| [Build manual](../Manual/Curta%20Build%20Manual.pdf) | 54 PDF pages, including illustrated construction, fitment, and calibration. The final page has no extracted text. |
| [Drawings](../Drawings/) and [painting drawings](../Manual/Painting/) | Markings and finishing references; not a kinematic model. |
| [Optional modifications](../Mods/) | Metal main shaft and printed lettering variants. No variant was selected during assessment. |
| [License](../LICENSE) | CC BY-NC-SA 4.0. |

External sources opened during assessment:

- [Workspace fork](https://github.com/LibreSolid/Curta-Type-I-3x)
- [Marcus Wu's upstream repository](https://github.com/marcuswu/Curta-Type-I-3x)
- [Author-linked bill of materials](https://docs.google.com/spreadsheets/d/16EJePozXW-uC6UFISzyT2eMk7c8wh6v-EP5L1U8fzfM/edit?usp=sharing)
- [Creative Commons license summary](https://creativecommons.org/licenses/by-nc-sa/4.0/)

The BOM's accessible printed-parts table was read, including quantities,
original part-number mappings, print settings, and fitment notes. A complete
audit of every spreadsheet tab or hardware entry was not performed. Retrieve
and record the relevant BOM data when implementing; an external spreadsheet
can change independently of the Git commit.

The README and manual also link the
[assembly video](https://youtu.be/zh2Z11miQ0w). Its contents were not watched
or validated during this assessment. The README credits mcmaven's
[Curta Calculator Mods](https://www.thingiverse.com/thing:3126676) as an
influence on the carry levers; that external model was not inspected.

The STEP header records an AP242 export dated 2022-03-31, made with
ST-DEVELOPER v18.101. Git history places the CAD/STL restructuring on that
date. The 2025-07-06 update changed the manual and added painting drawings;
the checked history showed no CAD or standard-STL change in that update.
Do not assume the standard design incorporates the optional mods.

## Inventory

Tracked files included:

- 2 STEP documents: the calculator assembly and a carry-lever spring tool.
- 79 standard STL files under `STLs/`, including the spring-forming tool.
- 65 additional STL files under `Mods/`, plus 6 optional 3MF files.
- 1 build-manual PDF, 10 DXF files, 1 DWG file, 6 SVG files, and 6 PNG files.

There were no tracked Python files, tests, simulation manifest, project-local
`AGENTS.md`, or OpenSpec artifacts in the checked source. The existing
`.gitignore` does not constitute simulation build hygiene; add the exclusions
required by the workflow when implementation starts.

## STEP import evidence

The workspace's public `StepAssembly` reader successfully read
`CAD/Curta Assembly.step`. Its inventory was:

| Measurement | Result |
| --- | ---: |
| Product definitions | 276 |
| Root assemblies | 1 |
| Sub-assembly definitions | 144 |
| Part definitions | 131 |
| Occurrences, including sub-assemblies | 691 |
| Leaf solid instances | 547 |
| Solids in each part definition | 1 |
| Improper occurrence placements (mirrored/scaled) | 0 |

The 131 part definitions are not 131 distinct names. Two hardware names each
identify two different product definitions:

- `M4x10`: occurrence counts 6 and 2.
- `6mm ball`: occurrence counts 1 and 17.

Several sub-assembly names also recur, for example `10207 <1>` and
`10220 / 410003 <1>`. Preserve document identities and hierarchy; names alone
are not globally unique. The public `StepNode` contract refuses an ambiguous
part name. Resolve these hardware cases explicitly during import planning.

The STEP includes purchased hardware and springs: nuts and screws, balls,
carry-lever springs, selector springs, carriage spring, anti-reversal spring,
zero-positioning spring, and others. It also separates parts that the STL set
combines into a printed group. Examples include the drum segments and frames,
the tens-bell stack, and transmission gear/sleeve groups. The simulation must
represent which components are rigidly joined and which move independently.

Sample occurrence placements returned by the reader, with translations in mm:

| Product | Parent | Rotation | Translation |
| --- | --- | --- | --- |
| `main body` | `Upper frame <1>` | 0 degrees | `(0, 0, 0)` |
| `bearing plate` | `Lower frame <1>` | 180 degrees about X | approximately `(0, 0, -118.35)` |
| `selector shaft bottom` | `Digit Selector Axle <1>` | approximately 4.4 degrees about Z | approximately `(58.5, 0, -127.775)` |
| `Transmission Gear Tip` | one `10207 <1>` occurrence | 0 degrees | approximately `(-20.25, -35.074029, 22.05)` |

These are examples of document placements, not a transcribed simulation layout.
Use the reader's full occurrence hierarchy and world/local transform semantics.
Other occurrences of the same gear and selector have different placements.

### Native geometry check

A separate read through CadQuery's `importers.importStep(...).val()` yielded
547 solids. Every solid had positive volume. Native `isValid()` checks passed
for 546 solids and failed for one:

```text
SOLIDS 547
INVALID_SOLID_INDICES [413]
NONPOSITIVE_VOLUME_INDICES []
ASSEMBLY_EXTENTS_MM (159.781, 165.064, 321.6)
```

`413` is a **zero-based index in that import's `shape.Solids()` sequence**,
not a product ID or durable part identifier. The invalid solid's product name
was not resolved. Do not claim that it is cosmetic, harmless, or repairable
without investigation. The extents are the imported assembly's bounding-box
dimensions, including protruding features, not a manufacturing specification.

The probe was read-only:

```python
import cadquery as cq

shape = cq.importers.importStep("CAD/Curta Assembly.step").val()
solids = shape.Solids()
invalid = [i for i, solid in enumerate(solids) if not solid.isValid()]
nonpositive = [i for i, solid in enumerate(solids) if solid.Volume() <= 0]
bounds = shape.BoundingBox()
```

This checks individual shapes. It does not prove clearances, absence of
intersections between parts, correct assembly, or correct motion.

### Import attempts and limits

- `StepAssembly` successfully provided the inventory and placements above.
- Constructing temporary in-memory `StepNode` subclasses and calling
  `.shape()` failed with `ProjectManifestError`: no `pyproject.toml` containing
  `[tool.solid-node]` exists above the source STEP. No manifest was created
  for the assessment. This is not evidence that a properly configured
  simulation project cannot import the geometry.
- `cadquery.Assembly.load(path, importType="STEP")` failed while recovering
  named hierarchy with `ValueError: Unique name is required. M4x16 hex is
  already in the assembly`. This is a separate duplicate-instance-name issue
  from the two duplicated product names reported above. It prevented that
  diagnostic route from identifying the invalid solid.
- No `solid import-step` scaffold, `solid build`, snapshot of a simulation,
  project contract suite, or motion validation was run.

The public API describes a STEP scaffolding route through `solid import-step`
and part import through `StepNode`, with declared tessellation. Consult the
current public API before using these. Full scaffolding success on this
particular document remains untested.

## Standard STL evidence

All 79 standard STLs were inspected in memory with Trimesh. Default loading
merged coincident vertices; no hole filling, face repair, or source writes
were performed. Connected components were counted from face adjacency,
including open components.

```text
files:                     79
triangles:            968,966
total file bytes:  48,454,936
watertight meshes:          70
valid closed volumes:      70
single face components:    67
```

Nine files were not watertight; another three were watertight but contained
two disconnected face components. All listed meshes had consistent face
winding under the probe.

| File, relative to `STLs/` | Watertight | Face components |
| --- | --- | ---: |
| `11 - Assemble Step Drum/main axle and step drum bottom.stl` | No | 10,930 |
| `11 - Assemble Step Drum/main axle and step drum top.stl` | No | 986 |
| `22 - Transmission Shaft 10216/10218.stl` | No | 7 |
| `22 - Transmission Shaft 10216/10222.stl` | No | 3 |
| `23 - Transmission Shaft 10207/10220 - 410003 x15.stl` | No | 5 |
| `23 - Transmission Shaft 10207/10230 - 410008 x15.stl` | No | 3 |
| `24 - Transmission Shaft 10208/10219 - 410002.stl` | No | 5 |
| `24 - Transmission Shaft 10208/10221.stl` | No | 3 |
| `8 - Assemble Tens Bell/tens bell.stl` | No | 15 |
| `27 - Assemble Reversing Lever/reversing lever knob.stl` | Yes | 2 |
| `31 - Assemble Input Selectors/selector shaft top x8.stl` | Yes | 2 |
| `34 - Lower Housing & Base Plate/lower housing.stl` | Yes | 2 |

The very large component counts are mesh-topology findings, not counts of
intended mechanical parts. Do not split those exports into thousands of
simulation nodes. Determine their relation to the STEP's constituent solids.

The essential checks used were:

```python
import numpy as np
import trimesh

mesh = trimesh.load_mesh(path, process=True)
components = trimesh.graph.connected_components(
    mesh.face_adjacency,
    nodes=np.arange(len(mesh.faces)),
    min_len=1,
)
# Read mesh.is_watertight, mesh.is_winding_consistent, mesh.is_volume,
# len(components), mesh.bounds, and mesh.extents.
```

Sample STL extents in the source coordinate system:

| Part | X × Y × Z (mm, rounded) |
| --- | --- |
| Main body | `136.051 × 136.050 × 84.000` |
| Bearing plate | `128.111 × 128.109 × 33.600` |
| Transmission shaft 10207 | `5.449 × 5.890 × 165.000` |
| Selector shaft bottom | `7.390 × 7.390 × 86.075` |
| Carriage body | `97.500 × 97.500 × 20.100` |
| Drum/axle bottom | `68.008 × 66.406 × 108.750` |
| Drum/axle top | `67.906 × 63.203 × 149.250` |

These are diagnostic bounding-box readings, not fitted diameters or layout
constants. The drum halves have local Z ranges `[-102.75, 6]` and
`[6, 155.25]`; do not center each STL independently and discard this evidence.
No claim was established that every STL shares a complete machine frame.
The optional `Mods/` meshes were not included in these checks.

## Mechanical evidence from the manual

The manual's PDF pages were read as text. Pages 31 (carry levers) and 47
(carriage installation) were also rendered and visually inspected. Temporary
rendered copies were diagnostic artifacts outside the repository; the upstream
PDF remains the durable source. Folder stage numbers and PDF page numbers do
not always match.

Useful construction and motion evidence:

- Page 6: the author intentionally expects filing/sanding and trial fitting
  against mating parts. Nominal exported geometry must not be assumed to
  represent every finished operating clearance.
- Pages 10 and 13: the tens bell and stepped drum should spin freely.
- Page 12: glue the drum's top and bottom together with three printed pins.
- Pages 14–19: zero-positioning and anti-reversal mechanisms, spring winding
  dimensions, and the pin that couples disc rotation while permitting the
  drum's axial movement.
- Pages 22–26: 17 transmission shafts, their different gear groups, and which
  groups are fixed to their shafts. Gear tips sit approximately 5 mm below
  the shaft tops. Some joints are fixed with adhesive or nail polish.
- Pages 28–29: reversing mechanism assembly, ball/spring detents, and
  alignment with the turns-counter gears.
- Pages 30–31: 10 result carry levers and 5 turns carry levers. Each should
  snap between upper and lower positions. A complete main-shaft turn should
  reset a lowered lever. Lever legs engage the adjacent transmission gear
  flanges. Carry springs use approximately 57 mm lengths of 0.6 mm music wire.
- Pages 32–33: eight input selectors, their ball/spring detents, and selector
  engagement with the transmission gears; the ones position uses the lower
  of its two gears.
- Page 37: 11 result dials and 6 turns dials. Seven full carry pins and eight
  half carry pins are used; two dials are unpinned. Half pins have an
  approximately 36-degree orientation. Pins must depress carry levers when
  passing nine without contacting the digit cover.
- Page 38: clearing teeth comprise two tooth plates and a spacer, with a
  prescribed stacking and registration. Ring clipping may require adjustment.
- Pages 40–42: dial axles, free-running dial fit, spider spring, and balls.
- Pages 45 and 47: a housing pin is drilled during assembly, and the carriage
  is aligned so its ones digit meets the body's ones digit.
- Page 48: the carriage-spring instructions still contain `DESCRIBE THIS`.
  Use the STEP, BOM, and additional evidence to resolve that gap.
- Page 50: the crank's rest orientation is between the final turns digit
  and the ones digit of the result register.

### Acceptance scenarios supplied by the author

Manual page 53 describes the following sequence, starting from cleared
registers:

1. All selectors at zero; one crank turn gives result `0`, turns `1`.
2. Ones selector at one; one turn gives result `1`, turns `2`.
3. Ones selector at nine; one turn gives result `10`, turns `3`.
4. Ones selector back to zero, tens selector at nine; one turn gives result
   `100`, turns `4`. Continue across the input positions to exercise carries.
5. With all result and turns dials manually set to nine and the first input
   set to one, one crank turn should cascade carries and return all dials to
   zero.
6. From zero, add one and then subtract one; both the result and turns
   registers should return to zero.

It also describes geometric carry checks: a depressed lever aligns its carry
gear with the tens-bell carry tooth, engagement rotates the transmission shaft,
and a subsequent rotation resets the lever so the tooth no longer engages.
Use those checks alongside arithmetic outcomes. The assessment did not execute
these scenarios or independently establish their correctness on the CAD model.

## Motion scope and limits

The STEP provides a static assembly. No executable motion model or explicit
kinematic pair entities were found by the targeted source search. Implement
digit selection, crank rotation, intermittent engagement, carry and reset
timing, subtraction, carriage shifting, clearing, and arithmetic state as the
ratified scope requires.

Solid-node's documented motion and contract APIs can express prescribed
kinematics and test geometry. They do not infer calculator operation from
contact between teeth, solve friction or torque, or prove the forces needed
to snap a carry spring. Flexible shapes can represent changing spring geometry;
that is not evidence of spring-force behavior.

Decide controls in calculator terms. Crank progress, operand setting,
addition/subtraction, and carriage position are candidate meanings, not
ratified driver declarations. Do not expose every internal joint as a root
slider. Establish how operations retain state and how demos repeat before
promising an unrestricted interactive calculator.

## Optional variants

The [metal main shaft mod](../Mods/Metal%20Main%20Shaft/README.md) addresses
printed shaft breakage along layer lines. It uses a 9 mm rod or tube cut to
258 mm, replacement drum halves, and locating pins. This was read as evidence
of a physical build issue; it was not selected for the simulation. It has no
separate assembled STEP in the checked inventory.

Printed lettering variants add STL/3MF geometry. Their geometry and licenses
were not separately audited. Start from the standard design unless the pilot
selects a variant, and keep any choice explicit.

## License and comparison with ReCurta

Curta-Type-I-3x is CC BY-NC-SA 4.0: attribution, noncommercial use, and
share-alike conditions apply as described in the project's license. Preserve
the author and contributor acknowledgments. This differs from ReCurta's
public-domain declaration and matters for distribution or commercial reuse.
No permission to publish, contact an author, or select a different license
was requested or granted during the assessment.

For context, the preceding ReCurta assessment found 140 SolidWorks parts,
129 STLs (125 closed volumes), custom viewer meshes, 61 scanned assembly
images, mixed STL units, and no assembled CAD document. Its placements would
need reconstruction. Curta-Type-I-3x's STEP hierarchy is the decisive technical
advantage; the original calculator's carry/state complexity remains in both.
Do not combine their geometries without a deliberate, documented decision.

## Environment and verification boundary

The probes used the existing workspace venv, from this project directory:

```text
solid-node 0.6.0 (installed distribution metadata)
cadquery 2.7.0
trimesh 4.4.9
```

Distribution metadata alone does not identify which post-release framework
changes are present. Read the shop's current public API skill rather than
assuming that a release number describes the checkout's complete interface.

Context7 was used for current Trimesh and CadQuery documentation, including
mesh validity, connected components, STEP import, shape validity, and named
assembly import. The observed results above are from the installed versions.
Relevant documentation references:

- [Trimesh](https://github.com/mikedh/trimesh)
- [CadQuery import/export](https://cadquery.readthedocs.io/en/latest/importexport.html)
- [CadQuery shape validation](https://cadquery.readthedocs.io/en/latest/_modules/cadquery/occ_impl/shapes.html)

No upstream source, geometry, manifest, or environment was modified during the
assessment. No simulation code was written. No full model was built, no
interference or engagement contracts were executed, no motion was demonstrated,
and no exact fabrication or physical-performance claim is supported yet.
