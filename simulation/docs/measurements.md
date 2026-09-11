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
simulation-layer source correction awaiting the pilot's choice.

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
