## Context

Start from `simulation/assessment.md` and upstream geometry commit
`7023381a6d1c8797d84ae146abf47f4403b7f780`. The standard AP242 STEP contains
276 product definitions and 547 leaf occurrences. Its hierarchy supplies the
placements; the manual supplies the assembly and calibration evidence. There
is no previous executable simulation. The assessment remains historical evidence.

The pilot authorized implementing the simulation on 2026-09-11. This plan
records working implementation choices under that request, not a separate claim
that the pilot ratified every motion detail. On continuation the pilot explicitly
authorized modeling the documented spring and delegated routine engineering
decisions: make evidence-backed choices and record them without repeated approval
requests. Manufacturing certification remains out of scope.

## Coordinates

Preserve the STEP's millimetres, vertical Z axis and common main-shaft axis.
Read placements from the document; do not center individual parts on their
bounding boxes. A moving group owns a joint in its own rest frame. Site joints
are appropriate for imported parts whose axis is known in the assembly frame.
The completed model can translate the entire machine to a presentation origin.

## Goals / Non-Goals

Goals: the complete standard assembly; simple named joints and drive relations;
all eight selectors, eleven result dials and six turns dials; addition,
subtraction, carries, decimal shifting and clearing; repeatable demonstrations;
source, geometry and arithmetic contracts.

Non-goals: redesigning print geometry, optional modifications, contact dynamics,
friction, spring-force prediction, or fabrication certification.

## Decisions

1. **Import STEP components and preserve provenance.** Scaffold through
   `solid import-step`, retaining its hierarchy and transforms as an auditable
   source map. Simplify the moving mechanism into meaningful subassemblies only
   after source-drift checks exist. The STL assessment shows substantial topology
   defects, so replacing the STEP indiscriminately with STLs would lose evidence.
2. **Resolve ambiguous hardware explicitly.** `M4x10` and `6mm ball` each name
   two products. Compare their geometry and occurrences before choosing an import
   representation. No arbitrary first-name match is acceptable.
3. **Validate before animating.** Identify the invalid native solid by durable
   product identity. A correction must be explicit and measured; do not quietly
   repair the upstream document. Inventory pre-existing overlap pairs and their
   measured volumes where the author's unfinished fits overlap. Do not excuse a
   new motion collision with a volume threshold.
4. **Relations state mechanical dependencies.** Use `Revolute` and `Prismatic`
   at the moving bodies, broadcast repeated digit motions, and keep nonlinear
   intermittent laws in a small kinematics module. Keep structural placement in
   `render()` and runtime inputs in relations or `simulate()`.
5. **State must be reproducible.** Begin with explicit starting register values,
   operand, operation and crank progress, so scrubbing to a pose produces the
   same result without hidden Python history. Explain any distinction from a
   physical calculator's retained state in the final controls and README.
6. **Evidence supplies motion dimensions.** Derive selector travel, subtraction
   lift, carry travel, gear phase and carriage pitch from the source and manual;
   keep the probe and readings. A demonstration's timing is stated as a chosen
   manual operating speed and is not a measured speed rating.
7. **The navigation tree teaches the mechanism.** The pilot explicitly requested
   meaningful show/hide layers: enclosure, frame, input selectors, main drive,
   transmission, carry mechanism, and carriage/registers. Group by mechanical
   role, not STEP export order. Keep fasteners with their supported assembly,
   individual digit channels reachable, and moving carriage covers within the
   carriage's own frame. The raw source hierarchy remains a separate reference.
8. **Calculator sliders expose causes, not arbitrary component poses.** The pilot
   emphasized educational inputs and actual calculation. Operand, crank turns,
   operation, carriage shift and clearing drive the corresponding mechanism and
   register values. Starting registers make a calculation reproducible when
   scrubbing; a preset animation alone does not meet the requested interaction.
9. **Lift before shifting.** A continuous carriage-position driver traverses six
   discrete working detents. The page lifts 6 mm, shifts, then reseats; it refuses
   to commit calculations while lifted or between detents. The lower spring seat
   moves while the upper seat stays fixed. Clearing follows a lift/turn/lower
   sequence. Lower housing markers do not move with the carriage.
10. **Examples and operation remain separate.** Six worked examples explicitly
    replace the page-local starting registers, then run named mechanical moves.
    The ordinary controls retain completed calculations. Seven small instructions
    expose rest, setting one, one crank turn, lift, shift, reseat and clearing.
11. **Material-inspired colors teach the layers.** The pilot requested aluminum,
    bronze and black contrast while physical verification continues. The display
    palette uses silver structure/drum, bronze transmission/carry gearing, brass
    guides/clearing teeth, steel shafts/springs/hardware, black housing/controls
    and ivory number rolls. These are illustrative display choices, not a claim
    about the printed project's construction materials or a metal Curta's bill
    of materials. Colors are declared on material leaves and fused prints, so
    recursive navigation and exports retain them without altering geometry.

## Findings

The complete 547-occurrence source assembly builds and its placement contract
passes. Duplicate product names are resolved by suffixing only those names with
their existing STEP entity numbers in an ignored import copy; a restoration test
proves that every other source byte is preserved. This is necessary because the
same hardware names designate different geometry, and repeated subassembly names
otherwise conflate their definitions in the scaffold. Generated empty render
methods are removed mechanically. See `simulation/docs/measurements.md`.

The invalid solid is the zero-positioning spring (#419219). Automatic repair
remains invalid and produces two native solids. An analytic replacement based
on manual page 14 and measured mounting points was authorized by the pilot.
The digits-cover / upper-housing boolean also yields invalid geometry,
so no certified nominal overlap inventory exists yet. The spring replacement now
passes native validity, wire-size and exact/faceted mounting contracts. Crank,
drum and eight selector motions are implemented with joints and relations, and
the arithmetic unit tests pass. Seven educational layers preserve every original
source placement. The complete result/counter drum passes both kernels after
recorded outside-profile and sleeve fits. All seventeen installed bevel pairs
now pass exact/faceted engagement checks, including sampled carriage positions.
Their axial fit alone had biased play; an additional -3° dial clocking centers
both flank limits without weakening the ±12° engagement contract. The new stem
trim keeps that axial fit above the frame bearing plane.

Fifteen carry sliders, the tens bell, carriage and clearing plate now move.
The first carry channels pass full-bell sweeps and bidirectional engagement in
both kernels after tooth-profile fitting and measured phase corrections, without
relaxed assertions. Remaining carry-lever contacts and flexible parts, clearing-tooth contact,
complete source overlap inventory and full demonstration interference remain
open. Checkpoints and detailed measurements are in simulation/docs/measurements.md.

The zero-positioning cam now rotates at its retained height while its transverse
pin slides through the axial slots for subtraction. A measured cam profile drives
the grouped roller/lever and the documented spring's moving terminal. Six contact,
travel and spring contracts pass both kernels. The pawl's repeating ratchet ramp
includes the source's shorter closing tooth interval; its contact sweep passes,
and its spring and mounting fits now pass exact. The collar trim and missing
spring-anchor bore are explicit builder-style fits confined to simulation. The
pawl's reverse-blocking contract recognizes tooth-pitch backlash and separately
checks that release clears the tooth; it does not claim an ideal one-way clutch.

The carry U-wires now spread against measured slider detents while their closed
folds stay on their supports. The fixed bearing grooves gain .05 mm radial wire
allowance without modifying the guide or slider. Twelve motion, seating and wire
contracts pass both kernels. The missing clearing components are the manual's
two tooth strips and spacer, supplied as flat standard STLs. They are formed
into the measured cover groove and retained as three separately selectable
leaves. The operating inventory is consequently 550 physical occurrences,
including every original STEP occurrence; the immutable source-placement
inventory remains 547. Reconstructing the bell spring with five proven-connected
patches gives 554 material leaves without changing that occurrence count.
The later seventeen-finger spider reconstruction brings this to 588 material
leaves, still representing the same 550 physical occurrences.
The groove, retaining-screw relief and progressive clearing-to-dial contact
and timing are now verified.

### Carry contacts and timing

The carry forks, reset shoes and pin-contact tips require local fitting, bounded
by native permitted-removal contracts. The half pins also need their cutaway
side selected deliberately: the manual's approximately 36-degree flat angle
alone leaves two orientations. Both complete dial banks now pass native and
faceted carry/parked-pin checks at all six carriage positions. The measured cam
resets some levers in the next crank revolution, so carry motion retains the
previous cycle's latch until that station's cam arrives. See the reproducible
profiles and validation in `simulation/docs/measurements.md`.

### Register detents

The source spider is unloaded: each of its seventeen fingers intersects its
6 mm ball by about 11.937 mm³, and each ball intersects its dial by about
.001647 mm³ natively. The operating layer now drives the balls from the actual
dial joints through one measured periodic rise profile, then drives each
finger from its ball. The source ring and rounded tips are retained; a
variable side-profile sweep preserves each arm's tapered thickness. Native
contracts prove the full reconstruction remains one connected spring, adds no
source material when unloaded and removes only a bounded upper-cone skin.

The ring retains its source collar interference, to be named in the fixed-seat
inventory rather than advertised as clearance. A ±4 mm height survey rejects
moving the whole source spring as a cure: lowering enters the carrier and
raising increases collar/cover overlap. A named .05 mm carrier seating gap is
separate from each finger's .05 mm ball gap. Bending is prescribed, not a
spring-force or strain calculation. The first station passes native and
faceted full-pitch clearance and free/blocked seating checks. The complete
bank now also passes both kernels through all digit/shift combinations,
carry and subtraction cascades, and progressive clearing; every ball is
independently checked as captured by its own dial and spring tip.

The clearing stop is now a source pin driven vertically by the cover's measured
cam. Its documented eight-turn .6 mm wire spring compresses between the native
sleeve seat and pin shoulder, with .05 mm seating gaps. Native distance
measurement replaces an invalid near-contact Boolean measurement; independent
full-sweep contact and spring tests pass both kernels. No pin or sleeve geometry
is changed. The whole-machine audit still needs cover/window and frame-guide
interfaces resolved before the source overlap inventory can be accepted.

## Findings for the framework

- Exact printed groups can contain enclosed voids represented by disconnected
  negative-volume mesh shells. The project checks material connectivity, not
  surface-shell count, and separately requires one valid native solid. Every
  rigid body remains covered; no part is skipped.
- A placement joint on a Molejo leaf is counted in its required shape-parameter
  ports. A thin mounting assembly separates placement from wire deformation.
- Reusing a wrapped assembly render directly in a fusion crosses the assembly's
  simulation-phase boundary. Generated ordinary placement methods avoid that.
- STEP products with repeated human-readable names need identity-based import
  selection. The project uses a byte-audited ignored name-disambiguation copy.
- Two imported-part adjustments returned older built geometry than a fresh
  adjustment after changing helper constants. Explicit dimensional parameter
  identities and built/fresh equality contracts resolve the project cases;
  the cause is not established. Independent ignored verification artifacts use
  `SOLID_BUILD_DIR=_build_checks` with the same workspace environment, separate
  from the live preview's publication lock.
- OpenSCAD output in a nested inspection directory rebases rigid STL imports
  but leaves flexible snapshot STL paths relative to the flexible module's
  directory. The image silently omitted the two spring arms although their
  meshes existed. Moving inspection classes from `simulation/tools/views.py`
  to `simulation/views.py` restored both arms in the snapshot. This is an
  artifact-path finding, not permission to treat an incomplete image as proof.

These are evidence for an upstream finding record, not framework changes or
claims that a new API has been accepted. No framework implementation was edited.

## Risks / Trade-offs

- Nominal source fits may not operate without the manual's sanding and tuning:
  distinguish the nominal source inventory from verified moving interfaces.
- Arithmetic can be right while gears do not engage: require geometry contracts
  alongside the author's numerical calibration cases.
- STEP subassemblies sometimes describe separately modeled pieces printed as a
  group: preserve all constituents and verify connected rigid groups deliberately.
- A static spring cannot prove moving spring clearance: use a measured flexible
  representation where motion changes its shape, or record the interface as open.

## Migration Plan

Add only the simulation package, project manifest, build exclusions and records.
Commit this plan, implement from the frame upward, then sync specifications and
archive only after the required evidence passes. Upstream CAD remains unchanged.

## Open Questions

What causes the invalid cover/housing intersection, and
what is the faithful representation of its finished fit? What are the measured
engagement phases and operating clearances? Resolve these in the import and
single-channel increments before replicating the mechanism.
