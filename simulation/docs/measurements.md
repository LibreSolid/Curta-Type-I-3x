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

## Carry springs and their detent seats

Manual page 30 and the inspected first-lever close-up locate the closed U on
the bearing's lower support. Its open legs straddle the slider's notched side
edges. Their elastic movement is transverse spreading while the slider moves
4.2 mm vertically, not translation of the spring with the slider. The original
source wire is .6 mm diameter and approximately 55.09 mm long, consistent with
trimming the manual's approximately 57 mm forming blank.

The first source spring is not a clearance-verified installed shape. New exact
contracts fail against its bearing (.205872 mm³ in the test) and against the
slider at the upper pose (.833851 mm³). `tools/carry_spring.py` sweeps 21 positions
and locates the native contact regions. Slider contact is in the two free hooks;
bearing contact is mostly on one long leg, with smaller closed-end contacts.
The probe selects the actual occurrence by its assembly translation, not merely
the first repeated product name. All ten result stations share one relative
spring/bearing frame; the five counter stations share a second, tilted .5° less.
The source bend has a 10° closed-fold plane. A 3.4 mm half-span clears the bearing's
6 mm waist. The free-hook center is moved .119583 mm relative to the closed fold
to follow the slider's measured .075 mm bearing-frame offset.

`tools/carry_profile.py` measures the two detent outlines at 101 stroke positions
using .35 mm radius hook gauges for .30 mm radius wire. `detents.py` retains those
piecewise spreading laws, with knot compression bounded to .0005 mm in the
measured coordinate, not a collision-volume tolerance. The free hooks spread;
the closed U remains seated. Its remaining .006304 mm³ native contact is removed
by a .70 mm groove swept only around that fixed fold. The guide, slider outline
and spring wire size are unchanged. `carry_seat.py` records the two source-frame
placements, reproducible with `tools/carry_frames.py`.

Twelve tests pass faceted (217.60 s) and exact (193.96 s): 41 slider positions in
each bank, five spring/bearing poses, .01 mm free and .20 mm blocked hook checks,
one valid .60 mm wire, <20,000 triangles per spring, and a stationary closed-fold
centerline. The latter measures mesh-ring centers: individual circular-profile
vertices rotate slightly as the transported frame follows the bending legs,
which does not move the circular wire's centerline. The original point-identity
test exposed this distinction; the positional bound remains .00001 mm.
The formed wire is approximately 54.6–54.7 mm long. Its prescribed shape does not
solve spring forces, strain or material-length conservation. All fifteen levers
now use these fitted spring seats and motion relations. The whole-lever snapshot
was inspected, including the fixed U, both free hooks and the guide.

## Clearing strips omitted from the STEP

Manual page 38 requires two tooth plates and a spacer. They are absent from the
547-leaf STEP but supplied as three standard print occurrences in
`STLs/37 - Clearing Cover/`: two copies of `clearing cap teeth x2.stl`
(505.383213 mm³ each) and `clearing cap tooth segment spacer.stl` (729.675010 mm³).
All are watertight single bodies. The plate is a flat 72 mm strip with nine teeth
on one half, spaced 3.75 mm; the .9 mm thick plates face opposite ways in the
manual's curved stack. The spacer is 70.5 × 6.9 × 1.5 mm. `tools/clearing_probe.py`
retains the readings and flat-profile plot used to identify this assembly step.

The cover's groove runs from radius 49.05 to 52.5 mm, with its floor at local
Z 9 mm. `clearing.py` bends each source print about its own mid-thickness radius,
preserving its neutral-axis length, and registers its midpoint to the cover's
-Y screw/rivet pair. The radial layers are 49.10–50.00, 50.025–51.525 and
51.55–52.45 mm: .05 mm wall allowance and .025 mm between layers. Their backs
stand .05 mm above the floor. The two tooth rows face opposite halves; the
source dial types have correspondingly offset reset features.

Planar Manifold refinement to 1 mm precedes the bend, without smoothing or mesh
repair. Each tooth strip has 40,522 triangles; the spacer has 3,176. The three
formed/source volume ratios are .999955, .999936 and .999936, consistent with
the refined cylindrical approximation. The cover's .5 rad source tessellation
falsely encroached 99.421788 mm³ into the outer row; .01 mm / .1 rad tessellation
clears the fitted strips without any change to the exact cover or test bound.
The three groove/integrity tests pass faceted and with the exact runner (128.18 s;
the STL interfaces deliberately remain faceted). The underside stack snapshot was
inspected against the manual. The operating model now represents the original
547 leaves plus these three upstream prints; the raw STEP placement contract
still covers exactly 547. Clearing-to-dial contact and progressive timing remain
open, not certified by the successful groove fit.
The new contact bench fails all three initial checks: dials move by .295547 mm
during lifting before the clearing cover rotates, the parked outer strip has a
.005794 mm³ dial contact, and the full sweep also collides. These remain honest
red contracts while the installed phases and clearing law are calibrated.

### Absolute zero and clearing engagement — calibration in progress

The bevel tests establish phase only modulo 36°, not the absolute digit index.
The clearing gear supplies that missing datum: its eight remaining tooth tips
are centered at local -72, -36, 0, 36, 72, 108, 144 and 180 degrees; the two
missing positions leave a gap centered at -126°. `tools/dial_zero.py` measures
that direction in the operating assembly. All seventeen gaps were 142° from
up at the previous logical zero. Adding four whole dial pitches puts the gap
2° from up, preserving the already-fitted bevel phase modulo one tooth.
`registers.CLEARING_ZERO_INDEX` records this correction. The installed bevel-bank
tests still pass faceted (82.51 s), as do the three register-motion tests
(60.78 s). This closes an absolute-index blind spot in the earlier evidence;
those tests alone never proved mechanical zero.

At the initial strip height, the parked rack also fouled a dial. Its 3 mm tooth
depth places the nominal rack pitch line only 5.45 mm above the dial axis,
against the dial gear's 6 mm pitch radius (7.2 mm tips, ten 36° positions).
The current trial deepens only the cover's annular groove floor .6 mm, from
local Z 9 to 8.4 mm; each strip back retains its .05 mm seat gap. This raises
the installed rack pitch line to 6.05 mm above the dial axis without moving
the cover, its fasteners or radial groove walls. The three groove/integrity
checks pass again with the exact runner (114.22 s; STL interfaces stay faceted).

An independent forward-contact probe still found double-flank jamming: a
one-to-zero trace had to jump five digits to find another clear pose. A .1 mm
outside-profile relief of the clearing gear removes that jump in the diagnostic
trace. `dial_fits.py` applies it only in the source clearing-gear bands:
local Z 18.45–20.40 for type 1 and 21.00–23.70 for type 2. The axle bore, dial
body and bevel gear remain untouched. This is a measured working fit, not a
manufacturing recommendation or a completed contact proof.

The initial fitted contact bench passed the lift-hold and every-digit parked
clearance checks. Its full sweep remains red (one reported inner-row contact
is .000828 mm³). `tools/clearing_fit.py` is testing constant-pitch laws from the
3.75 mm source rack pitch and each installed strip's neutral radius; the
forward-contact tool is diagnostic evidence, not a license to animate jumps.
The contact-following trace is not used as an animation law.

The remaining zero-position contacts lay between world Z 38.450000 and
38.472954 mm: the rack tip clipped the shoulder beside the missing-tooth gap.
Deepening the groove a further .075 mm (total .675, local floor 8.325) places
that tip at Z 38.525, leaving .052046 mm above the measured shoulder. No tooth
is shortened and the source strip profiles remain unchanged. Both complete
rows now pass a zero dial without any positive overlap through 0–80° at .25°
intervals (`clearing-zero-identified-seat.jsonl`). Four native checks pass
(271.39 s): both dial types remain one valid solid, material is only removed,
and all removal stays in the named clearing-gear band outside the axle bore.

A build-artifact discrepancy was caught during this calibration: direct
`ClearingTeeth.adjust()` gave minimum local Z 8.375, while the built STL still
gave 8.450 despite carrying the changed module timestamp. The cause is not
established; other project watchers were active. The groove floor is now a
public `Length` parameter on the cover and all three strips, so geometry
variants have distinct artifact identities. The groove contract also checks
the actual back height, not merely that it lies above the floor. The earlier
`clearing-zero-seated.jsonl` and `clearing-linear-fit-seated.jsonl` readings
describe stale 8.4-floor geometry and are not evidence for the final seat.

The constant-pitch survey finds a clear outer-row start at 9.75° for every
nonzero digit, and a clear inner-row start at 10.5° for the longest (one-to-zero)
passage. Their pitches are 4.131907° and 4.336209°, from 3.75 mm at neutral
radii 52 and 49.55 mm. `cycle.cleared_position()` uses those two measured
phases plus each dial's station offset. It holds the dials during lifting,
advances them sequentially as the appropriate row arrives, and stops at the
missing-tooth gap before lowering. The new station-order unit contract first
failed the global tween. Full installed sweep validation passes: five tests
faceted (132.79 s) and with the exact runner (119.08 s; STL contacts remain
faceted). Coverage includes all ten digits on all seventeen dials over 121
clearing positions, finer eighth-tooth sampling on both row types, and .1° free /
12° blocked perturbations in both directions at engagement. The exact bevel-bank
regression also passes (82.47 s). The fitted stack snapshot was inspected.
Reversing the clearing angle in node code fails three geometry tests; one
full-sweep contact is .821898 mm³. The correct law is restored, with its
post-mutation regression passing all five checks (103.41 s, faceted).

Verification now uses the same workspace venv with `SOLID_BUILD_DIR=_build_checks`.
This isolates ignored artifacts and the build lock from the live preview watcher;
the published preview continues to use `_build`. The earlier queued carry and
fine-clearing runs were interrupted deliberately, not counted as test evidence.

## Carry trigger, fork and reset shoe — open contact checks

`carry_contact.py` combines the first source lever in each bank with the actual
keyed shaft, dial/pin and printed bell, driven by the same operation law as the
root. The initial dial-pin and bell contracts fail: 3.966415 mm³ at the result
half-pin with digit nine, and 8.123323 mm³ at the reset shoe. The first fork test
also exposed a test-authoring error: an assembly has no rigid STL; it now checks
each printed solid in the shaft stack. That error is not mechanical red evidence.

`tools/carry_contact.py` preserves a complete 1° survey, with contacts also present
when no carry occurs. `tools/carry_sections.py` independently confirms at rest
9.693762 mm³ native fork/shaft contact and 8.696464 mm³ native shoe/bell contact.
The former occupies the fork's axial band; the latter has an 8.277196 mm³ region
near world (31.060370, -8.875742, -25.05), plus a .419269 mm³ edge region near
(34.668711, -6.786791, -23.775). Native side sections were inspected. These fixed
contacts need fitting separately from the late trip timing: the current law
keeps the lever up while a dial pin is already contacting it. Manual page 37's
half-pin orientation and protrusion guidance was re-read and visually inspected.
No carry-trigger or reset-contact proof is claimed yet.

### Local carry-fork and reset-shoe fits

The standard lever STLs have the same bounds as the STEP; their approximately
.07 mm³ volume differences are consistent with tessellation, not a newer fit.
The fork rubs the 3.97 mm sleeve in its 5.55 mm axial band. `carry_fits.py` opens
that local clearance to radius 4.02 mm and gives its lower flange face .05 mm
axial play. The fitted pinion reaches radius 6.164278 mm; the face fit is confined
to radius 6.22 about that shaft and the machine's inner 45 mm region, preserving
the free fork ends. The shaft's keyed bore and teeth remain untouched.

The reset shoe's upper face originally enters the 35.4 mm locking-disc envelope
by .9 mm. It is filed below that disc's Z -25.5 plane with .05 mm clearance.
At the lower detent, its sole also enters the carry-ring base by .3 mm. The native
ingredient probe names `results_counter_carry_ring`, not the support plate;
at crank 149° the original shoe overlaps it by 2.365942 mm³. Its furthest tooth
radius is 36.48 mm (radial vertices, not the smaller axis-aligned bounding box).
The sole is shortened .35 mm inside that envelope plus .05 mm. Both types remain
one body. The source guides, spring detents, pin-contact tips and upper fork faces
are unchanged by these foot fits.

Eight native fit tests pass (27.80 s), including precise permitted-removal regions
and equality of the built shape with a fresh adjustment. The initial provisional
25 mm³ removal budget was replaced by those stronger location-specific checks:
the final direct adjustments remove 24.826147 / 25.192377 mm³, and mass alone
cannot establish that the right surfaces were filed. The guide-protection test
also caught .019176 mm³ of unnecessary filing outside radius 45; the cutting
tool was restricted, not that protected region relaxed.

A second cache discrepancy was measured: the fresh result adjustment had volume
856.022273 mm³, but `shape()` returned 855.891594 mm³ from an earlier flange cut;
the counter differed similarly. The flange and ring-tip radii now have explicit
`Length` identities, alongside the fork radius and seat gap. The shape-equality
tests pass for those identified variants. This does not establish the framework
failure's cause. Three of four installed carry-contact checks passed before the
last identity correction: fork clearance, .01 mm free / .20 mm blocked axial
capture, and bell clearance through a whole cycle. Pin contact remains red;
the identified geometry is being rechecked.

### Dial-pin approach and real reset phase

The independent pin probe moves the dial continuously, leaving the candidate
crank law out of the measurement. The original half pin first meets the raised
lever at about digit 8.5; at nine it already requires 2.028591 mm depression,
and later needs more than the modeled 4.2 mm stroke. Full pins likewise require
about 5.4 mm at the worst passage. Rotating a half pin can improve its own
passage, but cannot fix the full pin, so that is not the adopted remedy.
A diagnostic 1.25 mm tip trim reduces the full-pin maximum to about 4.15 mm.
That still jams a dial parked at nine against the reset cam. The adopted
`carry_heads.py` fit uses common installed tip height Z 31.15 mm: full-pin
depression at nine is 1.11085 mm, below the cam's 1.25 mm available drop at its
crest even with the two .05 mm contact gauges. Full-pin maximum depression is
3.54606 mm; both pin types still push past the spring-spread crest near 2.562 mm.
Only the contact tip changes, not the fork, guide or spring detents. Both native
head-locality tests pass (21.08 s), proving one valid body and no added material.

The reset probe also rejects the current early reset animation as a driving
proof. With the lever independently lowered, the first result cam reaches maximum
lift near crank 3–5°, across the cycle boundary; the first counter does so near
53°. Later lever stations add 20° each. Maximum geometric lift is about 2.95 mm,
enough to cross the spring detent before its remaining snap travel. A carried
lever can therefore remain latched into the next revolution. The replacement
motion law now includes pin approach, retained carry and this measured reset
phase. Non-interference of the old early-reset law alone did not prove cam drive.

`carry_motion.py` expresses those three phases with public motion math and the
measured profiles in `carry_profiles.py`. Previous-cycle carry is reconstructed
from settled registers and completed crank turns; it is not hidden mutable state.
Three timing tests failed the early-reset law and now pass. A fourth proves that
a parked nine preloads rather than latches the lever, and lifting the carriage
removes that preload. The cam follows its measured rise until the spring crosses
over centre, then the remaining .2 mm rise triggers a prescribed snap. This is
kinematics, not a force/friction prediction. Independent operation setup and the
calculator page's Commit action initialize a new operation; they do not preserve
unexposed physical latch history across separate setups.

The installed first-pair contact bench passes four complete-turn checks (46.54 s,
faceted), then the same four through two turns (part of a 63.75 s run). New
pin/cam driving checks initially used the two-sided blocking default, which
incorrectly demands a follower be blocked away from its driving surface too.
They now explicitly test .01 mm free in both directions, .2 mm blocked toward
the surface and .2 mm free away from it. That correction is a test-authoring
fix, not new geometry evidence. All six checks then pass the native runner
(133.42 s), including the two-turn collision sweeps and both driving surfaces.

The installed bank caught .012033 mm³ contact at crank 170° on a type-2 half
pin. Normalizing all fifteen native pin mountings to one station shows matching
axes and protrusions, but the four type-2 half-pin flats differ by nine degrees
from the four type-1 flats. Their angles to the pin's dial-radius vector are
27° and 36° respectively; manual page 37 calls for approximately 36°.
`pin_mounts.py` turns the four type-2 pins nine degrees around their own axes,
leaving the cylindrical bore seats unchanged. The native eight-pin angle check
and complete fifteen-station, two-turn carry cascade pass (part of a 74.11 s
faceted run). The shifted-carriage test remains red: at shift two, digit two,
a counter half pin touches the side of the last inactive result lever by
.174401 mm³ faceted / .183256 mm³ native. Moving that pin outward by up to
1 mm does not remove this side contact. `tools/carry_side_clearance.py` measures
the complete neighbouring-pin passage before a bounded local fit is chosen.

That survey rules out more head filing: the neighbouring pin crosses the thin
head's body, not just a disposable edge. A 3 mm reduction in pin exposure also
loses intended drive, so it was rejected and pin depth is unchanged. The flat's
36° angle leaves two possible cutaway sides. Rotating the half pins another
180° selects the side that clears every neighbouring **integer** digit while
still tripping its own lever. The independent continuous diagnostic does find
contact at neighbouring positions 1.10–1.78, but those positions cannot occur
during a legal operation: the neighbouring bank's pins here are below the
selected decimal place and do not turn. A separate arithmetic-cycle contract
proves that invariant in both modes at every shift; lifted carriage transit is
also covered. This is not a claim of unrestricted clearance for arbitrary
off-detent dial positions or shifting the carriage while seated.

All four installed-bank checks now pass (233.91 s, faceted): all ten parked
digits at all six detents, eight native 36° flat angles, a dense two-turn cascade
at home, and cascades at the other five shifts with parked lower digits set to
two. No additional lever material was removed. The adopted half-pin clocking is
180° for type 1 and 189° for type 2, in each pin's own frame. Their cylindrical
mounts and material are unchanged.

The corrected half/full pin depression profiles differ by at most .004390 mm.
The production motion now uses their common measured envelope plus the named
.05 mm gauge, avoiding two almost identical driver expressions. The direct
probe of the installed half pin reproduces `carry_profiles.py` byte for byte
through its compiler. Six first-pair native contact checks pass again with this
final profile (140.32 s), as do the three carry-pinion/bell checks (70.03 s).
Seventeen pure timing/cycle/arithmetic checks pass. All four installed-bank
native checks pass (454.49 s), as do all twelve carry-wire/travel/contact checks
after these slider fits (68.12 s). The moving carry bench snapshot and native
sections were inspected. `views.py` supplies explicit driver-default poses
for snapshots; the CLI's `--set` selects construction parameters, not drivers.

The refreshed native rest inventory has 372 rigid occurrences and 291 positive
overlaps, with no refused booleans. This is a diagnostic, not an accepted seat
list. New strip/screw contacts and retained source joints still require review;
whole-machine and scenario integrity are not yet certified.

## Stepped-drum positioning leaf spring: source and ownership

The forked printed `TensBellSpring` is not a rigid link. The author's
[Part IX build log](https://www.digitaltorque.com/articles/curta-9/) identifies
it as the stepped-drum positioning spring, attached below the tens bell, and
describes thickening its arms and adding half-cylinder ribs so the drum snaps
between addition and subtraction. The STEP includes that ribbed revision.
Manual page 9 attaches its plate with two M4 screws. These two screws were
incorrectly grouped under the fixed frame; red quarter-turn vertex tests
measured 15.581880 mm screw drift and 20.827569 mm spring-mount drift. Moving the
complete bell assembly through one revolute joint, with its two screws owned
by that assembly, makes both tests pass. The manual says M4×6 while the STEP
names them M4×10; source hardware is retained pending its seating check.

The source spring is valid, with volume 1582.129669 mm³. Its mounted cap is at
Z −6.9 and its lowest hook at −61.966932 mm. Native normal sections measure
each long arm as a 6.9×1.8 mm strip with an inward R .9 stiffening rib, inclined
4.977196° toward the centre. `retaining_spring.py` preserves the perforated
mounting plate and both tapered hooks as native source cuts, replacing only
the 35.132474 mm constant-section arms with analytic sweeps. The 24-chord rib
contour differs from its semicircle by less than .002 mm. Two native tests
pass (37.27 s): the unloaded five-patch union is one valid solid, adds no
material to the source, and omits only .255092 mm³ inside the two bounded rib
regions; the union stays valid and connected through 0–6 mm radial deflection.
The .05 mm patch joins are overlap inside one continuous printed part, not
clearance at an assembly seat.

Installed shape is still under measurement. Leaving the source spring unloaded
intersects the drum top/bottom by 114.833142/11.728560 mm³ in addition and
57.933724/115.065533 mm³ in subtraction (native). The independent phase sweep
rules out rotating the drum as a remedy. Horizontal sections resolve the two
off-centre hook pockets, which a single axial section obscures. A radial hook
survey finds free positions without moving the mounting plate or shortening
the source hooks. The full contact-following deflection profile and arm
clearance are not yet certified. `tools/bell_spring.py`, `bell_spring_phase.py`
and `bell_spring_fit.py` reproduce these measurements. Prescribed arm bending
does not claim stress, spring force or material-length conservation.

The installed seat adds a named .05 mm gap below the cap. The pocket probe
samples the complete 9 mm subtraction stroke every .05 mm, bisects each hook's
first free radial position, then takes their common envelope plus .05 mm.
`bell_spring_motion.py` is a compact piecewise relation: no live booleans or
per-frame source meshes. The hooks require approximately 6.86 mm spread at
addition, crest near 7.27 mm during the shift, and settle at 4.16 mm for
subtraction. Both native seating checks pass (.01 mm free, .2 mm blocked inward
at every .25 mm of drum travel). The spring's whole-assembly quarter-turn and
subtraction sweep pass faceted (three tests, 33.82 s).

An early arm curve entered the bell lip by .547692 mm³ faceted. Delaying most
of the bend until below the lip removes that contact, but a subsequent native
union check caught an irregular spline/source join at 2 mm spread. One-millimetre
source-straight cuffs at both ends make the joints regular. The final two native
shape tests pass at 0, 2, 4, 6 and 8 mm spread (33.94 s), retaining the unloaded
source-fidelity bound. All three installed contact tests then pass faceted
(23.63 s) and native (859.83 s), including both hooks' seating and the complete
37-position arm/hook/mount clearance sweep against bell and drum. The superseded
long sweep was stopped, not counted as a pass.

The root now counts the spring as one physical source occurrence represented
by five material patches. The old literal leaf-count assertion correctly failed
551 != 547 after subtracting the three supplemental clearing prints. Its
replacement explicitly folds only this one proven-connected spring and still
requires all 547 original occurrences plus those three supplements. Material
integrity includes every patch, including the two flexible arms.

The first installed-spring snapshot from a nested `simulation/tools/views.py`
showed its plate and hooks but omitted both arms. Inspection of the generated
SCAD found existing flexible STLs referenced from the wrong directory. Moving
the pose classes beside the model, to `simulation/views.py`, restores the
arms. The corrected image was inspected. This records a framework artifact-path
finding; no framework implementation or generated source artifact was patched.

## Clearing retaining-screw relief

Restoring the missing strips introduced three screw contacts: inner strip
5.745261 mm³, spacer 3.074284 mm³ and outer strip .006199 mm³. The independent
hardware contract fails before fitting. `tools/clearing_fastener.py` measures
the original R 2.1 screw at 45° through the cover's R 1.65 pilot bore and R 4
counterbore; its axis is .289514 mm off the bore axis. The axial section shows
the shank entering only the strips' backs, not their teeth. Source screw, hole,
head seating and rivets remain unchanged; their nominal fixed fits belong to
the source inventory.

`clearing.py` now gives the three backs an R 2.15 screw relief, a named .05 mm
radial allowance. The cutter follows the source screw's measured axis in the
cover frame, starting at (.13205562, −45.57669045, 11.52567171), 135° about X,
over its 8.4 mm cylindrical shank. No source STL is edited. Removed volumes are
6.164691, 3.506547 and .020890 mm³ respectively. The original screw and both
rivets clear all three strips (one faceted contract, 50.66 s).

A copy-against-copy boolean is not a suitable fidelity test here: it reports
5.53e−16 mm³ before mesh export and 7.64e−7 mm³ after newly cut vertices are
quantized to float32. No volume epsilon is introduced. Instead the artifact
contract compares every source/export triangle exactly, independent of vertex
ordering, and bounds **every changed face** to the small backing region (the
bore plus at most one 1 mm refined source edge). All unaffected faces, including
all teeth, must remain bit-identical. `tools/clearing_relief.py` reproduces the
342/226/68 changed-face counts and their bounds. Four groove/connectivity/locality
contracts pass (24.22 s, faceted); all five clearing-motion contracts remain
green (157.90 s, faceted).
The exact runner also passes all four locality/groove checks (18.21 s) and
all five clearing-motion checks (111.06 s); interfaces involving the source
strip STLs intentionally remain faceted. The installed addition and subtraction
leaf-spring snapshots were inspected, with the flexible arms present.

The subsequent native rest inventory has 374 rigid occurrences, 288 positive
overlaps and no refused booleans. No strip/screw or spring/drum overlap remains.
The source's unloaded spider spring still intersects all seventeen balls by
about 11.936925 mm³ each, and their nominal zero seats touch the dials by about
.001647 mm³ each. These moving detents require fitted motion; they are not
accepted into a static seat list by default. The root's current faceted run is
12 passes and one expected source-housing inventory failure (73.79 s).

## Register balls and the tapered spider spring

The original valid spider has volume 4732.786576872 mm³. Its bottom is local
Z −.2; the upper cone starts at Z 2.22 at radius 24 and falls with slope
1.22/21. Each radial finger is 4.5 mm wide and ends in an R 2.25 rounded tip
at radius 45. Result fingers occupy 0, −20, …, −200 degrees; the counter
fingers occupy 130, 110, 90, 70, 50 and 30 degrees. The installed source frame
is recentered with the other carriage parts, leaving mounting Z 45.2.

At zero, each source R 3 ball is centered at Z 43.35. Native tests find
.001646968832 mm³ ball/dial overlap and 11.936924875 mm³ ball/spider overlap.
The first faceted run missed the tiny dial overlap but caught the unloaded
spring and absent ball motion: one pass, two failures. The native run failed
all three checks. These are moving contacts, not permitted static overlaps.

`tools/dial_detent.py` measures both native dial types every half degree over
one 36-degree pitch. Its original Boolean binary search refused an invalid
intersection at type 1, 13.5 degrees, trial rise .68359375 mm. It was replaced
by the exact distance from the sphere's center to the dial solid: distance
below the 3 mm sphere radius means obstruction. This avoids manufacturing a
near-tangent Boolean sliver; it does not ignore an invalid result or change
the collision tolerance. Seventeen bisections bound vertical measurement
resolution by 5/2¹⁷ mm. An additional named .05 mm vertical gap gives rises
.05–.800008 mm. The two-type envelope is compiled into `dial_detent_motion.py`
with at most .0005 mm profile-compression error, independently checked against
the native parts. At the calibrated zero the rise is .089253 mm.

The whole spider cannot simply be lifted above its balls. The source ring
already overlaps the collar by 467.192338397 mm³. Surveying −4 to +4 mm in
.25 mm increments shows lowering enters the carrier (517.220246807 mm³ at
−.25), while raising increases collar interference and enters the cover
starting at +.75. `tools/spider_mount.py` and `tools/spider_section.py` retain
this diagnostic. The ring remains source geometry, with a named .05 mm gap
above the carrier; its fixed collar overlap is an inventory finding, not a
clearance claim.

`spider.py` retains the native ring through radius 25 and the native rounded
tips beyond radius 42. A sixteen-vertex parametric side profile is swept
through the constant 4.5 mm width. Unlike a constant-thickness beam, this
preserves the measured taper. The sampled upper curve uses the width edge of
the cone and lies inside the source; missing material is bounded by a .007 mm
upper-cone skin. Internal .05 mm patch overlaps and source-straight end cuffs
keep the reconstruction one physical body. Twelve coordinate ports are driven
by one smoothstep bend relation; each tip has a vertical prismatic joint.
Each ball drives its own finger with 1.35 mm preload, leaving another .05 mm
between ball top and finger bottom. No force, strain or inextensibility result
is claimed.

Native source-fidelity/continuity checks pass for the first finger (2 tests,
35.31 s) and complete seventeen-finger spring (2 tests, 25.18 s). The full
unloaded reconstruction adds zero native material and all removal lies in the
named cone skin. Every material patch is valid; their native union remains
one solid at unloaded, installed and crest bends through the 3 mm bench limit.
The first finger's 73-position pitch sweep, ball motion and free/blocked
seating pass both kernels: 5 faceted tests in 22.31 s and 5 native tests in
28.51 s. Perturbation directions use the sphere's source frame, whose +Z
points down after its source rotation.

The first whole-bank cascade failed at crank 242 degrees: two counter
occurrences had been mapped in the wrong order in the new detent layer.
The source stations are counter digit 4 = `p_10205_4`, ball 10, 70 degrees;
digit 5 = `p_10204_7`, ball 6, 50 degrees. The mapping was corrected and a
free/blocked capture contract added for all seventeen balls. This is a
prototype wiring correction, not an upstream source or framework defect.
Whole-bank reruns pass: 4 faceted tests in 109.82 s and 4 native tests in
546.44 s. These cover all digits at all six carriage positions, addition and
subtraction carry cascades sampled every two crank degrees, every ball's
free/blocked seating and 101 positions through progressive clearing.
Re-running the independent native measurement after integration reproduced
all 146 ball-profile readings exactly.

The root count test caught `581 != 547` when analytic patches were counted as
source occurrences. It now collapses only the proven-connected bell and
spider springs, explicitly requiring five and thirty-five patches respectively.
There are 588 material leaves representing 547 STEP occurrences plus the
three missing clearing-print occurrences. The source-placement map is unchanged.
`RegisterDetentMoving` is a standalone inspection view with its own complete
motion bindings; the OpenSCAD image was inspected and shows the full ring,
seventeen tapered fingers, balls and both dial banks. It is not a whole-machine
clearance certificate. The updated root faceted run is 12 passes and one
known whole-machine inventory failure in 82.29 s. Its exact rest inventory
finds 254 positive overlaps among 391 rigid patches, with zero refusals;
the seventeen ball/dial and seventeen ball/spider overlaps are gone. The
retained source ring/collar overlap, after the named carrier seating gap,
is 504.871504376 mm³. This inventory is diagnostic until its remaining moving
interfaces and source provenance are closed.

## Clearing stop pin and compression spring

Manual page 40 specifies a .6 × 5 × 20 mm spring under the clearing stop pin.
The source pin is valid, one solid, volume 433.642112895 mm³, with local Z
0–34.2 and a 6 mm diameter rounded head. Its placement puts the shoulder at
world Z 44.4 and the top at 55.8. The sleeve's inner seat is world Z 27.0.
The native spring has .6 mm wire, 2.55 mm centerline radius, eight turns and
21 mm centerline height (21.6 mm outside height), volume 36.399728308 mm³.
An X/Z section gives alternate ±2.55 mm crossings every 1.3125 mm vertically,
proving the eight turns; the measured free height differs from the manual's
nominal 20 mm and is recorded, not silently reconciled.

The static source pin overlaps the operating cover by 47.909403919 mm³
natively (45.859461118 mm³ faceted). Its spring overlaps the pin by
6.359523492 mm³ and the sleeve by .111595849 mm³. All four initial motion,
clearance and seating contracts fail; the static pin does not move relative
to its sleeve during clearing. The manual page was rendered and inspected.

`clearing_stop_spring.py` leaves the pin and sleeve geometry unchanged. Two
vertical prismatic joints move the pin and the spring's upper mounting frame;
one height relation shortens the spring while its lower endpoint stays fixed.
The measured wire/radius/turn count are a Molejo helix. Named .05 mm seating
gaps put the wire between Z 27.05 and `44.35 − press`, giving centerline
height `16.7 − press`. Wire diameter, validity, endpoint tracking and seating
have independent contracts. No force, stress or inextensibility is claimed.

`tools/clearing_stop.py` first measured the cover every degree on faceted
geometry. This gives 2.782208–7.900006 mm depression, with two short cam
passages and long flat sections. The corresponding seven faceted contracts
pass in 41.98 s, including a half-degree full sweep, one-sided drive, spring
seats, both endpoint trajectories and native wire validity/diameter. The
first native run passes spring seating but finds .000375132542 mm³ pin/cover
overlap at one sampled angle; that faceted profile is not accepted as final.

A native Boolean measurement then refuses an invalid near-contact sliver at
14 degrees and trial depression 7.828125 mm. The probe now measures native
shape distance to a real .05 mm minimum surface separation, without a volume
epsilon or skipped intersection. The expensive full-distance run was stopped
deliberately after 84 completed readings; those are reused while refining the
remaining turning points selected from the earlier profile. The independent
half-degree native collision sweep still covers the full rotation. The native
profile is now compiled: zero depression 3.089172 mm, sampled minimum
2.861206 mm and maximum 7.900085 mm. The installed centerline height therefore
ranges approximately 8.800–13.839 mm. All seven contracts pass on the final
profile: faceted 42.11 s, native 184.56 s. The original pin and sleeve remain
unchanged; no contact was waived. See `clearing-stop-native-fit-*.log` in the
ignored evidence directory and the reproducible probe/compiler.

The compressed-pin OpenSCAD cutaway was inspected: it retains the native head
and shaft and shows all eight windings. The sleeve is hidden only in this
inspection view; the spring's clearance and capture against it are tested.

## Whole-machine moving-seat triage — open

`tools/moving_seats.py` separates fixed imported overlaps from interfaces whose
relative placement changes across input settings, two crank turns, subtraction,
lift/shift and clearing. It composes public node placements into world matrices;
the .00001 placement-precision threshold classifies motion, never overlap volume.
The intermediate post-stop rest inventory produced 67 moving pairs, including
the now-resolved tiny pin/cover overlap. Most belong to repeated interface
families: lower housing around input controls, frame around carry guides and
the carriage, selector balls, dial covers, and a few retained ring/shaft seats.
They are not accepted as static inventory merely because they already overlap
at rest. Cover datum and guide checks are the next open contracts.

## Material-inspired display palette — geometry unchanged

The pilot requested aluminum, bronze and black contrast. `colors.py` supplies
six display colors: aluminum structure/drum, bronze transmission/carry gearing,
brass guides/clearing teeth, steel springs/shafts/hardware, black housing/grips,
and ivory number rolls. These are illustrative, not fabrication materials.
STEP subclasses, physical fused prints, source-STL replacements and flexible
leaves all declare colors; no solid, placement or motion law changes for color.

The two palette contracts fail on the previous colors (19.42 s), then pass
faceted (43.02 s) and on the exact runner (6.51 s). Both the assembled and
uncovered OpenSCAD snapshots were inspected at 1400 × 1100. The uncovered
view hides the same enclosure, frame, covers and carrier layers as the page's
See inside control; nothing is removed from the operating machine.

The fresh interactive export is not yet validated. Two exports were killed by
the OS for memory exhaustion: PIDs 2754982 and 2760833, resident anonymous
memory approximately 10.3 and 9.4 GB respectively (kernel journal). The older
manifest remained in place. A new browser preflight rejects that stale palette
explicitly; passing calculations against that old document are not current
validation. Investigation of repeated motion-expression expansion is ongoing;
the colors are verified in snapshots but the exported browser update is open.

## Symbolic expression growth — current export blocker

The pilot reported a separate host crash during a parallel build, then clarified
that this VM may use 8 GB. Subsequent heavyweight jobs run sequentially with
`ulimit -v 8388608`, `OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1`, and
`set -o pipefail` so a logging pipeline cannot hide the failing process status.
No host settings or shared library implementation were changed.

Native circular edges provide an algebraic register-ball cam: R7.2 lands,
R4.5 scallops centered at R6, and a 3 mm ball. The circle intersection fixes
the half-dwell at 2.529120217 degrees. `dial_cam.py` preserves the .05 mm
seat gap and adds only the original probe's upper-bracket resolution,
5 / 2^17 mm. It agrees with every recorded envelope knot within .00004 mm.
The sampled table remains an independent reference. A source-circle probe
is retained in `tools/dial_cam.py`; no curve was guessed from appearance.
The law's symbolic size decreases from 4570 to 235 characters for a short
input token. Five native first-station contact/seating tests pass in 11.43 s.

Two exact algebraic simplifications also reduce repeated text: decimal shifting
uses the same linear interpolation between adjacent powers of ten instead of
six copied branches; nonnegative tooth counts use `max(1, count)` for their
safe denominator. Carry engagement uses the math API's direct `max` rather
than expanding it into repeated sums and absolute values. Decimal-shift text
falls from 316 to 49 characters, and the isolated carry expression from 17082
to 5135. The expression-size failures were recorded before these changes;
19 arithmetic/cycle/profile/size tests and five carry-timing tests pass.
Interpolation between lifted carriage detents is preserved, not silently
replaced by rounding.

These improvements do not solve the whole export. Bounded fresh exports fail
with `MemoryError` during symbolic relation evaluation, before a new manifest
is written. The 4 GB run peaks at 3526084 KiB RSS; later 8 GB runs reach
7823896 and 7857084 KiB. The stacks name expansion of `detents.spreading`
and the following six `carry_spring.coordinates` outputs. They are not CAD
Boolean failures, and the old 10:13 export must not count as current evidence.

`tools/expression_size.py` reproduces the growth without building CAD or
allocating the final expanded wires. Even using short symbolic tokens, one
result-channel carry expression is about 7.72 million characters; the measured
35-interval hook profile expands that to about 270.3 million. That result is
then copied into six wire coordinates across ten result stations (plus five
counter stations). The diagnostic completes in 3.59 s with 664636 KiB peak
RSS. This is a lower bound because real driver identifiers are longer.
The source import alone exceeds a 1 GB address-space ceiling; the diagnostic
succeeds under 4 GB.

The public framework documentation describes post-construction sharing in
schema 4, but the failing expressions exhaust resources while being constructed,
before that sharing runs. Preserving shared expressions through evaluation is
an upstream requirement, not a new calculator control or permission to remove
working springs. A separate framework cycle needs pilot authority; no framework
source had been inspected at the time of those project probes. In the later
pilot-requested diagnosis, read-only inspection of solid-node main
`2bdc50b37be920e79202d1c9e9c5700e43f525e0` confirmed that `symbolic_document`
runs before `bind_document`, as documented in ADR-080. No framework code was
changed. The pilot then paused project implementation for that framework work;
see [the checkpoint and cycle handoff](pause-report-2026-09-11.md). The existing
model and color snapshots remain available, but fresh interactive export and
complete delivery are blocked here.

## Cover-datum trial — dial clearance proved, neighbors unresolved

The covers' source center is (.386511579, -.028412332), distinct from the
carrier's (.537721035, -.038177283). Re-centering on that cover datum, rotating
by -.549916905 degrees and seating upward .05 mm removes the dial-window
encroachment while preserving both of the author's print meshes. The source
comparison is reproducible with `tools/cover_fit.py`, which reconstructs the
untouched STL placements independently of the currently installed trial.

The initial two faceted tests fail at 18.310925201 and 18.325069902 mm³
dial/cover intersection. Three fitted tests pass faceted (35.86 s) and on the
exact runner (35.92 s), including every integer digit, sampled carry/clearing
motion and source print-vertex preservation. This is a local clearance result,
not acceptance of the cover's other interfaces or exact recovery of STL surfaces.

The adjacent-pair diagnostic still finds a 91.212554578 mm³ intersection with
the clearing cover. Each fixed digit axle intersects the digits cover by
approximately .2315 mm³ and the upper housing by 2.61817 mm³. These contacts
remain findings, not approved source seats. The trial and its honest contracts
are committed for continuation; whole-carriage validation remains open.

## Pause-checkpoint verification

The compact native-circle cam's complete-bank faceted run finished with four
passing tests in 73.67 s after the last project edits. Its complete-bank exact
run remains pending; the earlier exact result used the sampled law.

Housekeeping re-ran 26 arithmetic/cycle/cam/size/carry-timing/source unit tests:
all pass, with 5.08 s process wall time and 640760 KiB peak RSS. The current
cover trial also passes all three faceted contracts again, with 36.35 s process
wall time, 18.02 s test time and 615952 KiB peak RSS. Both runs use the same
workspace environment and the 8 GiB address-space guard. No full export, final
all-node regression or new snapshot was attempted during this pause checkpoint.

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

At that historical checkpoint the model kept the source's neutral gray colors;
motion, material presentation, printed groups, overlap inventory and arithmetic
were open. Later evidence above supersedes those initial results. The complete
simulation remains active in `openspec/changes/simulate-the-curta/tasks.md`.
