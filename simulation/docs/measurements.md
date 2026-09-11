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

## F3: Register-bank alignment and bevel seating

`tools/dial_phase.py --fit` first measured the result-ones bevel pair. With the
original shaft seating, no tested dial phase clears the pair. A 3° dial phase
and 0.8 mm downward seating adjustment let the original, off-center pair clear
one complete 72° pinion tooth period. `bevel.BevelPair` then passed the faceted
and exact contracts: 6° samples through that period, ±0.1° free play and
blocking at ±12° at five phases. The unchanged seating failed both contracts.

Expanding that measurement exposed a common assembly-frame error, not seventeen
independent dial defects. The carriage body, its seventeen dial axles, dials and
detent balls share center (0.537721035, -0.038177283) mm and clocking
0.549916905°. Re-centering and unclocking that assembly puts every dial on a
71.474057463 mm radial datum with an inward radial axle at Z 33.9 mm. Result
stations are 0°, -20°, …, -200°; turns stations are 130°, 110°, …, 30°.
There are two 30° gaps, not eighteen uniform stations.

Sixteen source transmission shafts are on the corresponding 40.5 mm radius.
The result-tens shaft group `10236 <1>` alone has X 38.137315415 mm instead of
38.057551142 mm; Y is correctly -13.851815805 mm. Its complete keyed stack
requires a -0.079764273 mm X correction, not a separately displaced gear tip.
`tools/bevel_bank.py` retains the native phase/seating experiment for every pair.
With carriage alignment, sixteen pairs clear at 1.2 mm pinion seating drop; the
uncorrected off-axis shaft still overlaps by 0.003003038 mm³ there. After its
coaxial correction, all seventeen native pairs clear the sampled period at the
same 1.2 mm seating. The source-reference assembly
remains unchanged. The operating register banks and carrier now use the common
carriage correction. The operating transmission now applies the shared tip
seating and result-tens stack correction; full-bank contact regression remains
in progress.

The manual (p22) describes approximately 5 mm between the gear tips and shaft
tops and explicitly calls for a trial tight fit before adhesive. The source tip
top is 4.95 mm **above** the shaft top; a 1.2 mm seating drop would make that
3.75 mm. This is a measured simulation fit adjustment, not the original
dimension or a fabrication recommendation. Final keyed overlap and full-bank
engagement contracts must accompany integration.

## F4: Drum-to-input tooth fit

The five-tooth transmission pinion has 72° tooth pitch. The stepped drum's
32-station tooth pitch is 11.25°, so an engaged drum tooth advances the pinion
72° and, through the five-to-ten bevel pair, the result dial 36°.
`tools/input_contact.py` sweeps every 0.5° pinion phase during one tooth passage.
At crank angles 117–122° the unmodified profiles have no clear sampled phase;
the minimum faceted overlap reaches 0.328348412 mm³. A phase-only adjustment
cannot fix this source-profile conflict.

`fit.FittedInputPinion` explicitly offsets only the outer planar outline inward
0.35 mm, then intersects its extrusion with the original source shape. The
keyed bore and 1.5 mm thickness are preserved. This models the manual's trial
fitting/sanding step; it does not predict print strength, wear or tolerances.
No upstream geometry file is edited. The measured passage law starts at 113.5°,
lasts 11.25° and uses 4° home clocking. The red source tests failed at
0.003069493 mm³ overlap and at the ±0.1° perturbation (0.328663939 mm³).
After the explicit relief, all 61 half-degree passage samples and the free-play
/ ±12° blocking checks pass on both faceted and exact kernels. This proves the
single-row bench, not yet every drum row or the complete transmission train.

The complete printed input group exposed a second fit problem that the isolated
pinion cannot see. At digit zero and crank 18°, the ten-tooth row intersects
the 1.8 mm spacer: native overlap 0.060817327 mm³, radial interval
36.53–36.60 mm. Digit one exposes the identical problem in the next spacer;
digit two exposes the long ones sleeve. All seven source round input spacer /
sleeve types share a 3.97 mm outside radius. `InputSleeveFit` retains their
original bores and axial extents while fitting that outside radius to 3.85 mm:
40.5 mm shaft radius minus 36.6 mm drum radius minus the named 0.05 mm seat gap.
This is applied only to the input print groups, not unrelated carry spacers.
The full-row regression is being repeated after this explicit fit correction.

## Calculator controls and visible dials

`registers.py` declares seventeen radial revolute joints. Changing the result
from zero to one initially failed its independent world-vertex rotation test
with 6.200526686 mm error. The corrected carriage frame and dial relation pass
the same test, and both banks are now connected to the root's settled register
ports. These are real dial mesh rotations. Sub-turn drive is now integrated;
carry timing is still a prescribed candidate pending full contact verification.

`viewer/` is a project-owned educational host of the public viewer API, not a
second renderer. It exposes eight digit sliders, crank progress, addition /
subtraction, decimal position, exact starting registers and recursive show/hide
and focus controls. Its small session controller keeps completed operations
by writing the next starting registers and returning crank progress to zero.
It refuses to commit a partial turn. Three JavaScript tests first failed, then
passed for the author's sequence, multiplication, shifting, subtraction,
clearing, overflow and explicit commit behavior. The Python arithmetic tests
remain the model's independent checks. Session state is page-local, not saved
across reloads. Mechanical completion remains governed by the active tasks.

## Printed-group reconciliation

The standard print stages identify the top and bottom drum halves and the tens
bell as three printed bodies. The STEP instead carries 59 ingredients plus the
three separate joining pins. The first printed-group inventory contract failed
62 != 6. `standard/printed.py` now declares exact fusions of the source
ingredients, with their source placements, and `prints.PrintedDrive` retains
the three separate pins. Both inventory and connectivity contracts pass on
faceted and exact kernels. A third native-validity contract also passes exact.
The operating root uses those fusions.
Generated declarations also identify the individual transmission print groups;
their full integration and connectivity regression remain in progress.

Reusing a wrapped `AssemblyNode.render` method directly on a `FusionNode` failed
with a missing `simulate` attribute. The generator instead emits an ordinary
fusion render containing the source's placement data. No framework internals
or framework edits are used. This is an adapter/phase-boundary finding.

The browser's first full-size captures timed out under headless software WebGL.
A 1200×850 Chromium run with `--disable-dev-shm-usage`, SwiftShader and two
animation frames before capture succeeded. The inside screenshot was visually
inspected: the whole mechanism is framed, case/frame layers are hidden, dials,
input selectors and drive stack remain visible, and the eight sliders/readouts
are legible. The original tiny model was a host sizing error: mounting sets the
host's positioning inline; an explicit full-height positioned host corrects it.
No claim about hardware-GPU performance is made from this headless check.

## Sub-turn register progression

`cycle.py` now describes unwrapped dial positions within the current turn. The
single-row input timing is measured; initial carry timing comes from the native
carry-ring tooth stations (result ring outer tooth vertices 55–56.18°, source
clocking +77°; turns ring 57–58.18°, source clocking -103°). These carry timings
remain prescribed candidates pending the carry-contact bench. The turns drum's
one-tooth row spans approximately 297.5–300.5° locally, at source clocking
2.604082802°, giving a 51.25° phase difference from result input at the first
counter station. Positive crank travel is clockwise from above; the root's
direction test failed with 128.625810814 mm vertex error before correcting its
sign and then passed. Root faceted checks now pass 6/7; the remaining failure is
the recorded nominal cover overlap, not a hidden exception.

Four pure cycle tests first failed and then passed for carry order, both complete
register wraps, all six decimal positions and complement subtraction. The latter
advances digits positively through the complement rather than simply reversing
all gears. An independent mesh test first failed with 5.840373659 mm missing
rotation, then verified that 9 + 1 advances the ones dial before the tens dial.
A further world-vertex test covers the radial axle of every result dial,
including the ungrouped highest dial. All three register geometry tests pass on
both faceted and exact kernels.

The reproducible browser check `python -m simulation.tools.check_calculator`
passed the manual's 0, 1, 9, 90 sequence, page-local commits, eight input sliders,
and layer hide/show controls with no page errors. Its captured inside view was
inspected. This was the settled-register export; the subsequent sub-turn model
must be re-exported and checked before final delivery.

## Subtraction lift and keyed transmission

The source result input detents have 6 mm axial pitch. At the first detent,
the regular zero gear is Z -64.925 mm, the nine-tooth row is Z -73.8 mm, and
the ones channel's extra upper gear is Z -58.925 mm opposite the ten-tooth row
at Z -67.8 mm. Raising the drum 9 mm selects the complementary rows in both
cases. This is one and a half selector pitches, not a 3 mm lift. The root's
world-vertex test failed with 9 mm missing movement before the two prismatic
joints were wired; it now passes for the crank and complete printed drum.
The frame remains stationary. This run passes 7/8 root contracts, with only
the known source cover overlap still red before later transmission integration.

`standard/channels.py` preserves each source shaft and its associated printed
input and carry groups, with explicit joints. `transmission.py` groups these
as result and turns banks with named decimal places. The selector gear slides
54 mm for digit nine; one digit turns the keyed stack 72°. Both independent
world-vertex tests failed before the relations and passed afterward.
All seventeen operating stacks now have input and carry travel and shaft
rotation wired through the public motion API. Carry engagement/reset timing
is still a candidate; wiring alone does not certify contact.

The source counter input groups are centered 4.5 mm below their normal working
position. At the source pose, higher counter pinions meet the one-tooth row
and would falsely advance every place. Lifting all six input groups 4.5 mm
puts the first channel's lowest pinion at -44.85 mm against the one-tooth row,
while higher channels sit at -40.35 mm above the addition rows. With the drum
raised 9 mm, those higher pinions meet the nine-tooth row at -40.7 mm. This
is a measured normal-counter assembly assumption, not an independent reversing
lever control. The full printed upper drum and complete first-counter input
group pass a 3° faceted sweep in both modes. The complete result-drum sweep
still exposes a positive overlap; that contract remains red while investigated.

The original manufacturer's [1967 Model I service manual](https://www.mycurta.com/Documents/Curta_1_Servivce_Manual_engl.pdf)
was consulted as a primary cross-check, without importing its geometry. PDF
page 26 (Folio F-1) identifies freely sliding transmission gears, the first
counter's middle gear in the reversing yoke, and the first result's lower
gear in the setting knob. Page 27 (F-2) specifies depressed carry levers,
upward cam reset, and clearance so the lever does not force a shaft sideways.
The printed 3× model's measured dimensions govern this simulation; original
metal-machine tolerances are not silently scaled into print tolerances.

## Complete drum contact and material connectivity

After fitting the round input sleeves to 3.85 mm radius, all twenty result
digit/mode combinations pass the full drum's 3° sweep on both kernels. The
counter faceted sweep passed but exact detected 0.000010358908 mm³ at subtraction,
crank 84°: the nine-tooth upper row against the first counter's middle pinion.
`tools/engagement_probe.py --counter --subtract 1 --crank 84` identified the pair.
Counter pinions alone receive .36 mm outer-profile relief instead of .35 mm.
Both exact full-drum tests now pass (193.02 s); no contact-volume epsilon is used.

The fitted result-ones input print is one valid native solid, 444.038178 mm³,
but its tessellation has three surface components: one positive outer boundary
and two enclosed negative-volume cavity shells, about -.60881 mm³ each. The
framework's disconnected-solids assertion counts those surfaces as three parts.
`contracts.assert_connected_material` instead requires every shell watertight,
exactly one positive material boundary, all negative cavity vertices enclosed
by that boundary, and positive total volume. Exact checks additionally require
one native solid. Unit tests admit a hollow body and reject two separate bodies
or an external negative shell. The root checks every rigid part uniformly and
now passes material integrity. This does not excuse mechanical interferences.

## Carriage, clearing and marker ownership

The root's 20° decimal shift, 6 mm lift, clockwise tens-bell rotation and clearing
plate rotation each failed independent vertex tests before their relations.
They now pass. Six millimeters raises the lowest dial teeth from Z 24.45 to
30.45 mm, above the fitted tips' Z 28.65 mm maximum. This is an explicit
disengagement-stroke assumption; the complete shift-path contact audit remains
open. The bell rotates with the crank but stays at its axial bearing height,
including during the 9 mm subtraction lift.

Clearing is a three-phase control: first tenth lifts, middle eight tenths turn
the plate one revolution, final tenth lowers. The toothed clearing cover moves
with the handle, not the stationary carriage housing. Dial-clear timing has not
yet been contact-calibrated to this sequence. Clear lift and manual carriage
lift share one maximum-height relation rather than adding their strokes.

Manual page 46 and the source placements distinguish five lower decimal markers
(source marker groups 1–5, marker Z -144.14024 mm) from five upper markers (6–10,
Z 49.03898 mm). The former belong under enclosure/decimal_markers, the latter
under the operating clearing plate. Static ownership initially failed; after
regrouping, all three educational-layer contracts pass, including preservation
of every source placement. No marker is dropped or duplicated.

The carriage spring has 1.8 mm wire (native cap area 2.544690 mm²), centerline
radius 13.2 mm, and approximately four turns. Its source endpoints are at
Z 27.0225 and 51.0225 mm, clocked 35.717779468°. The lower thrust washer follows
the carriage; the upper sleeve stays on the main shaft. A red seat test found
1.5 mm missing movement. `positioning.py` now gives the washer and spring mount
matching prismatic motion, and drives spring height as 24 mm minus lift.
Two faceted tests pass at five samples across the stroke, measuring wire cap
centers directly rather than pitch-dependent bounding boxes. This Molejo helix
uses constant pitch instead of the source's flattened ends; fixed coil radius
and prescribed height are a visualization approximation, not an inextensible
wire, preload or force solution. Manual page 48's spring instructions are
unfinished, so measured source geometry supplies these dimensions.

A flexible leaf's shape-port validation also counts a site joint as a port.
Attaching a prismatic directly to the spring therefore failed because its shape
names only height. A thin mounting assembly carries the placement joint; its
height port drives the wire's height. This stays entirely in the public API.

## Bevel fit must also clear the frame

The complete overlap inventory exposed a consequence missed by the isolated
bevel-pair bench: lowering a tip 1.2 mm also lowers its tubular stem below the
frame's Z 9 mm bearing surface. The source tip/frame pair has zero overlap;
the unshortened fitted ones tip has 86.362013 mm³ exact overlap (85.507495 mm³
faceted). `test_bearing.py` first failed for that interference. The fitted tip
now retains the source lower-end datum while its gear head remains 1.2 mm lower:
the newly protruding stem end alone is trimmed by 1.2 mm. This leaves 11.85 mm
of the original 13.05 mm stem and preserves its keyed bore. Thirteen exact
rotation samples pass against the frame. It is a documented trial assembly fit,
not a manufacturing-strength recommendation. Full-bank integration remains to
be checked; the original exploratory single-pair bench is not that check.

## Carry-lever motion checkpoint

Fifteen carry sliders now follow their corresponding shaft's carry state with
4.2 mm travel; their guide bearings stay fixed. Result upper/lower gear datums
are -29.4/-33.6 mm; turns are -14.7/-18.9 mm. Source counter gears and sliders
were placed between detents and are normalized consistently. The first result
slider's travel test failed before wiring and both travel/reset tests pass
faceted afterward. This proves placement, not the candidate trigger/reset
timing or spring deformation; those remain open contracts.

## Installed-bank engagement and phase centering

The installed-bank contract checks all seventeen tip/dial pairs rather than
assuming the exploratory first-pair bench covers them. It initially passed
clearance at six detents and five lifted intermediate positions, but failed
the -12° flank perturbation. `tools/bevel_play.py` measured essentially identical
behavior on all seventeen pairs: at -12° no contact, -18° about .342646 mm³,
and +12° about 1.087920 mm³. This was biased clocking, not an absent gear.

`tools/bevel_phase.py` tested a complete 72° tooth period while clocking the
dials, without changing the 1.2 mm tip seating. An additional -3° dial phase
keeps every sampled nominal position clear and gives positive contact at both
±12° limits throughout that period (minimum .028029 mm³ faceted in the probe).
`BEVEL_DIAL_CLOCKING` records this adjustment. Both installed-bank tests now
pass faceted and exact (83.29 s exact): all seventeen home engagements and
cross-pair clearance through every detent and sampled lifted travel. No bound
was enlarged to turn the red test green.

## Carry fits and current engagement boundary

The inactive carry groups initially hit their locking discs: .025854/.070910
mm³ faceted for result/counter at crank zero; exact ingredient probes measured
.098123 mm³ in both pentagonal lockouts. Phase alone could not clear the source:
even its best phase retained .032501 mm³. Uniform .4 mm outline relief cleared
the full inactive sweep but left biased play at -12°. The current fit instead
clips the source to a .15 mm inward-offset outline clocked back by the input's
4° phase. It removes material only; the original keyway and height remain.
Both lockout limits now pass. The source is not modified.

The active ring tooth then hit the .6 carry pinion (result crank 150°:
.020995 mm³ exact; counter crank 204°: .316473 mm³). A .42 mm outer-profile fit
scales the .35 mm measured input-pinion fit by the .6/.5 tooth size; both full
bell sweeps passed faceted and exact afterward. This is a trial assembly
correction, not a manufacturing recommendation. Engagement remained a separate
red test; mere non-interference did not settle it.

The full-bell probe now compares passage width, phase and both ±12° tooth
limits. It locates the first carried tooth's midpoint at crank 152° for results
and 204° for turns, at which the worst blocked volumes are .042901 and .046604
mm³ faceted. Retaining the 11.25° passage puts the bank end datums at 137.625°
and 189.625°. All three refined full-sweep/engagement tests pass faceted and
exact (102.78 s exact, including time waiting for the shared build lock).
Lever trigger geometry, reset-cam contact and moving carry springs remain open.

## Demonstrations and spring tessellation

Seven small root instructions land exactly on their targets. A stepped test
routes lift → shift → seat, samples the adjacent bevel interface at .2 s
cadence, and finishes clearing; this is explicitly not yet whole-model
interference coverage. Six JSON worked examples are shared with the calculator
page: 123+456, 9+1, both registers overflowing, 100−1, 12×10 by carriage shift,
and clearing. JavaScript checks their arithmetic and safe shift order; model
tests replay each twice and verify the same answers and instruction targets.
Both model scenario tests pass faceted. The previous current-carriage browser
run passed the manual's 0, 1, 9, 90 sequence, retained values and layer navigation.

A subsequent full-example browser run stalled after its first four examples.
The source was project-owned tessellation, not a library change: Molejo's
`path_samples` is per spline span, so the zero spring's 1,000 samples over
166 spans generated 7,968,048 triangles. A new mesh-budget contract failed
before changing it. Four samples per span produce 128 rings per coil and
31,920 triangles, with the same exact centerline and 1.1 mm wire. Native validity,
cap area and the mesh-volume ratio (>98% of native, consistent with the
24-sided profile) pass on both kernels. The lighter export's complete browser
regression now passes: all six examples, retained calculations, lifted/between-
detent guards and recursive layer controls. The resulting calculator screenshot
was inspected. This does not claim a measured hardware-GPU frame rate.

## Zero cam, roller and moving spring

`zero.py` groups the lever, roller and their fastening hardware into one follower.
The disc's retaining clip keeps its axial position fixed; the crank drives its
rotation. The transverse drive pin rotates with it and slides 9 mm in its two
axial slots when the crank is raised for subtraction. Manual pages 15–17 and the
source slots establish this distinction; raising the entire disc would be wrong.

The original static assembly failed the crank/roller tests: 48.778205 mm disc
vertex drift and no follower displacement. `tools/zero_profile.py` measures the
native cam against a 10.4 mm radius cylindrical gauge: the source roller's
10.35 mm radius plus .05 mm seating clearance. The 33.6 mm arm swings about
(40.5, 33.6), reaching 7.523028° on the circular 34.5 mm cam flank. Two short
measured profiles describe departure from and return to the detent, with a flat
dwell between them. The public `piecewise` law drives the follower's revolute
joint; no assumed sinusoidal cam or collision solver runs in the viewer.

The replacement spring's coil and fixed terminal stay in place. Four shape ports
move the lower terminal and shoulder with the lever, keeping the tip in the
original 2.7 mm bore. Its five turns, installed diameter and 1.1 mm wire are
unchanged. This is prescribed deformation, not elastic-force or strain analysis.

Six contracts pass faceted (54.26 s) and exact (99.90 s): disc rotation without
axial lift; complete pin travel through its slots; follower departure/return;
full cam clearance including quarter-degree interpolation samples near both
edges; seated contact; and valid connected spring deformation with both terminal
centers within .001 mm and no lever/sleeve/bearing-plate overlap. Native closest
points measure .0499993–.0500199 mm clearance at six flank positions. The .01 mm
free / .20 mm blocked perturbations use that contact normal in the roller frame,
not an arbitrary radial direction at the steep detent flank.

The initial .5 rad mesh angular deflection obscured this small curved contact,
even though the exact seating was correct. Only the cam and roller now use .01 mm
linear / .1 rad angular deflection; native shapes and all contact bounds remain
unchanged. The below-plate snapshot was inspected: roller in the detent, drive
pin in the retained slotted hub, and spring around the lever pivot.

## Anti-reversal pawl and its spring mounts

The source's stationary pawl intersects the ratchet by .243318 mm³. Its ratchet
roots use 116 intervals of 357/116 degrees and one 3° closing interval, not a
perfectly uniform 117-tooth circle. `tools/pawl_profile.py` measures the constant-
section interface at world Z -145.8 mm with a .05 mm inflated pawl gauge.
The resulting repeating ramp and the shorter closing interval drive a single
pawl joint. Both the full-turn sweep and ramp-motion tests pass faceted; exact
sweeps also pass, including fine samples around selected release phases.

The mounting test failed at the source collar: it extends .15 mm into the
bearing plate, sharing 11.558238 mm³. Trimming .20 mm from its local Z -5.4 mm
face leaves .05 mm axial play without changing its working tooth or bore.
The source spring also enters the plate without an anchor hole (1.637549 mm³
overlap). The explicit simulation fit drills a .70 mm bore at the source tail's
world axis (-54.476590334, 16.420391800), retaining the manual's .60 mm wire and
.05 mm radial clearance. The other tail is fitted to the actual pawl bore at
(-44.100577738, 13.347627455), rather than the offset source wire endpoint.
Manual pages 17–18 specify seven CCW turns on an approximately 9.5 mm winding
mandrel. Its installed bore must clear the 12.5 mm collar; the analytic
spring therefore uses 12.6 mm installed bore and a separately routed upper leg.
The coil is held between world Z -138.8 and -143.35 mm: .65 mm pitch leaves
.05 mm between .60 mm wires, and the envelope clears both the bearing plate and
pawl body. Its moving tail follows the measured pawl bore while the anchor and
coil stay fixed. This prescribes elastic shape, not preload, impact or force.

All six tests, including wire size and the <50,000-triangle budget, pass exact
(140.85 s) and faceted (54.08 s). Reverse blocking is
checked with the pawl engaged, acknowledging tooth-pitch backlash rather than
claiming an ideal zero-play clutch. The release check sweeps the raised pawl
clear of the tooth instead of assuming a discontinuous pose is sufficient.
The main crank drives both cam mechanisms; the root still represents 547 leaves
and passes all twelve other integrity/operation tests. Its one open ordinary
interference assertion still reports the documented 224.327505 mm³ housing
overlap. No upstream part, thread specification or source file has been changed.
Rest and close side snapshots were inspected; the side view exposes the spring,
its fixed tail, collar clearance and the pawl nose above the ratchet teeth.
The restored root build publishes schema 4 with eight drivers, seven instructions
and 370 motion bindings; all 126 referenced rigid model artifacts exist.

## Historical initial validation boundary

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
