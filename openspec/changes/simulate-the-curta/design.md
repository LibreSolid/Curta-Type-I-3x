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
the arithmetic unit tests pass. Whole-machine geometry and register motion remain
open. Seven educational layers preserve every original source placement.

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
