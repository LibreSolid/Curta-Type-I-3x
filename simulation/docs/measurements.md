# Source assembly measurements

Measured 2026-09-11 using the workspace's editable solid-node installation,
CadQuery 2.7.0 and Trimesh 4.4.9. These extend the historical
[assessment](../assessment.md); they do not certify a functioning calculator.

## Reproduce

From the project root, with the workspace environment active:

```sh
python -m simulation.tools.probe
python -m unittest simulation.test_source
solid build
solid test --faceted simulation/standard/assembly.py
solid test --exact simulation/curta.py
```

The last command currently fails; the findings below are unresolved.
`tools/probe.py` prints all 131 part-product readings and the housing diagnostic
as JSON. It applies no repair. Its trial `fix()` call is diagnostic only.

## Import identity and placement

The original STEP has 276 product definitions, 691 occurrences including
subassemblies, and 547 leaf occurrences. The built viewer document has 692 tree
nodes including its root, 547 rigid leaves and no missing model files.

The unmodified `solid import-step` scaffold is unusable for this file: repeated
subassembly names conflate definitions, and identity-only `render()` methods
contain no Python statement. The raw generated files are retained in ignored
`_build_import/raw-scaffold/` for diagnostics.

`source.py` produces an ignored, deterministic STEP copy at
`simulation/_source/curta.step`. Only a repeated PRODUCT name receives its own
existing entity number, such as `M4x10 [#419010]`; identifiers, descriptions,
geometry, references and placements are unchanged. A byte-for-byte restoration
test proves that removing those name suffixes yields the original document.

`standard/` was scaffolded from that copy, then mechanically compacted with
`tools/compact_import.py`: repeated path/tessellation declarations move to a base
class, comments are removed and empty render methods are omitted. All placement
operations are preserved. This is generated source mapping, not motion code.

The placement contract compares every world-space mesh vertex with the original
local artifact transformed by its STEP occurrence matrix, to 0.00001 mm. All
547 pass. Deliberately shifting the main crank +1 mm fails at occurrence
`0:1:1:18:1` with 1.0000000000700737 mm drift. The mutation was reverted.

## Same names, different hardware

| Source product | Occurrences | Native volume, mm³ | Measured local extent |
| --- | ---: | ---: | --- |
| `M4x10`, #419010 | 6 | 202.882649712 | Z: 0 to 11.1 mm |
| `M4x10`, #419159 | 2 | 156.865192240 | Z: 0 to 8.1 mm |
| `6mm ball`, #419094 | 1 | 220.893233456 | Diameter 7.5 mm |
| `6mm ball`, #419241 | 17 | 113.097335529 | Diameter 6.0 mm |

The two balls are not duplicates. Their distinct geometry and occurrence frames
are preserved. Screw Z extent includes the modeled head and is not a measured
thread-length specification.

## F1: Invalid zero-positioning spring

Native solid 413 from the original assessment is the product
`zero positioning spring`, STEP PRODUCT #419219. All other 130 part products
pass `Shape.isValid()` individually.

- Source solid: invalid, one native solid, volume 939.675495825 mm³.
- Local bounds: X/Y ±9.9 mm; Z -6.340759704 to 16.240759767 mm.
- Native world center: (40.559916636, 33.833477173, -147.674713217) mm.
- Published mesh: two connected bodies.
- CadQuery `fix()` trial: still invalid, now two native solids, volume
  984.512917392 mm³. This result is rejected, not substituted.

The manually wound spring described on manual page 14 uses approximately
11.5 mm mandrel diameter, 1.1 mm music wire and five counter-clockwise turns.
The winding and its terminal legs must be fitted to the measured sleeve and
lever mounts before an analytic replacement can be accepted. This is an explicit
simulation-layer source correction explicitly authorized by the pilot.

### Documented replacement and measured mounts

`flexibles.ZeroSpring` replaces that one occurrence with a Molejo swept 1.1 mm
wire. The source CAD remains unchanged. The spring tests first failed on native
validity and cap area: 3.463605901 mm² versus the documented 0.950331778 mm².
The source therefore modeled approximately 2.1 mm wire, not the manual's 1.1 mm.

The lever has a 13.5 mm outside collar around the 7.361 mm sleeve stem. The
manual's 11.5 mm winding mandrel is not an installed bore specification. Use an
installed 13.6 mm bore (0.05 mm radial seat allowance) and 7.35 mm centerline
radius. This is a fit assumption, not a prediction of springback or preload.
Five CCW windings descend from Z -143.5 to -149.5 mm, giving 1.2 mm pitch.
The fixed terminal is seated in the bearing plate's 3 mm bore centered at
(33.552746609, 28.154097304); its tip is Z -133.45 mm within the plate, whose
faces here are Z -132.45 and -138.45 mm. The moving terminal is in the lever's
2.7 mm bore centered at (40.5, 24.9), with tip Z -157.3 mm through the 3 mm plate.

Three continuous cubic paths describe the upper terminal bend, five-turn coil,
and lower terminal bend. The coil has 32 interpolation points per turn; the
Molejo B-rep reports its 1e-6 mm sweep approximation. A single interpolant across
all bends initially cut the collar (faceted 0.001964709 mm³; exact also failed).
Explicit matching tangents at the coil boundaries resolved that geometric
failure without altering the fit allowance or the test. Both faceted and exact
mount contracts now pass: no overlap with lever, sleeve or bearing plate, and
terminal cap centers match the measured mounting points within 0.001 mm.
The lower-frame and standalone replacement snapshots were inspected; the frame
view occludes the spring beneath the bearing plate, reinforcing the need for
independently hideable educational layers.

The spring's installed rest shape is verified. Moving-lever deformation and
clearance remain part of the motion work; this is not spring-force validation.

## Selector and first drive channel

The selector shaft bottom contains ten small planar detent faces at local
Z 19.08, 25.08, 31.08, 37.08, 43.08, 49.08, 55.08, 61.08, 67.08 and 73.08 mm.
Their angular progression is 36 degrees per 6 mm step. Descending the knob from
zero to nine therefore translates it 54 mm and turns the shaft/number roll
324 degrees. The first selector axis is (58.5, 0), parallel to Z.

`drive.DriveTrain` is an inspectable single-channel bench. World-vertex tests
failed with 83.530683769 mm crank drift and 54 mm missing selector travel before
the joints existed. Both pass after declaring the crank/drum revolute joints,
selector prismatic joint, and drive relations. These tests prove placement and
travel, not yet drum-to-transmission tooth engagement or complete calculation.

The standalone spring snapshot was visually inspected. Native connectivity
alone is insufficient here: the exact connectivity check sees one solid and
passes, while native validity and the faceted connectivity check expose defects.

## F2: Unreliable digits-cover / upper-housing boolean

Both STEP products individually report valid native solids. The digits-cover
export at angular deflection 0.5 is not watertight (4,875 vertices, 9,819 faces,
one connected component, no degenerate triangles).

The exact root interference assertion fails at this pair and reports signed
intersection volume -4759.760488150 mm³. Independently applying the document's
full-precision rotation/translation to the two native products and intersecting
them directly with CadQuery yields an **invalid** result with nine solids and
signed volume -5087.175057851 mm³. These negative numbers are failed geometry
operations, not physical overlap measurements or acceptable tolerances.

The author's corresponding STLs under `STLs/42 - Digit Cover & Upper Housing/`
are both watertight and have the same local bounds at mesh precision:

| Part | STEP volume, mm³ | Source STL volume, mm³ |
| --- | ---: | ---: |
| Digits cover | 24864.182527449 | 24850.735678557 |
| Upper housing | 122281.102102807 | 122340.222560752 |

Their Manifold intersection at the STEP placements returns signed volume
224.326830384 mm³, but the returned Trimesh is not watertight. That is additional
diagnostic evidence, not a certified overlap inventory. No epsilon, automatic
repair, alternate print geometry or clearance adjustment has been applied.

### Representation decision after the complete mesh audit

The audit of 130 remaining distinct rigid artifacts found exactly three
non-watertight STEP tessellations: digits cover, upper housing and crank collar.
The author's corresponding standard print STLs are each watertight and one body.
The collar print is 20732.746529261 mm³, with bounds X/Y ±28.5 and Z 0–58.5 mm.
`print_parts.py` now imports these three author-supplied print files, without any
repair, in their original local frames. The source-reference assembly continues
to use STEP, and the operating model records these substitutions explicitly.

Direct native Manifold evaluation of the cover/housing print-file pair reports
`NoError` for both inputs and the result, with 224.327505535 mm³ overlap when
the document's transforms are applied in Manifold. The previous Trimesh result
lost watertight topology when its nearly coincident result vertices were welded.
Using the standard node mesh-placement path, the root contract now fails on an
ordinary positive overlap of 224.327505338 mm³, not on invalid geometry. This
resolves representation, not the source's fit. The inventory probe records which
kernel it uses; an exact run necessarily uses facets at these three interfaces.

The first whole-machine faceted scan found 660 positive overlap sums and 89
negative contact sums from the valid kernel; many are nominal face contacts or
constituents of printed groups. No positive value was removed by a threshold.
The probe preserves signed nonpositive sums as diagnostics, rejects invalid
kernel results, and is being repeated with native solids where available. The
inventory is not yet accepted as a verified moving assembly contract.

## Validation boundary

- Initial frame-only root: faceted inventory contract failed `1 != 547`.
- Complete static root: `solid build` succeeds; every published STL exists.
- Source name adaptation: two unit tests pass.
- Source placements: one contract covering all 547 occurrences passes; the
  deliberate +1 mm mutation fails as intended.
- Root faceted run: 1 pass, 3 failures (mesh admission at digits cover,
  spring connectivity, spring native validity).
- Root exact run: 2 passes, 2 failures (cover/housing intersection and spring
  validity). This does not certify the assembly.
- Complete assembly and standalone spring snapshots were visually inspected.

The model keeps the source's neutral gray colors. Motion, material presentation,
rigid printed-group reconciliation, overlap inventory and arithmetic remain open
in `openspec/changes/simulate-the-curta/tasks.md`. The simulation is not delivered.
