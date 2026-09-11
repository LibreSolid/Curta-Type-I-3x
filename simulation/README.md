# Curta simulation handoff

This folder contains the pre-implementation assessment for simulating
Curta-Type-I-3x with the LibreSolid Studio `simulate-project` workflow.
**There is no simulation implementation yet.**

The pilot requested this handoff on 2026-09-11 so a fresh session could begin
the simulation without repeating the assessment. The findings describe
upstream commit `7023381a6d1c8797d84ae146abf47f4403b7f780`.

## Start here

Read [the assessment and evidence](assessment.md) before planning the model.
It records the source inventory, successful imports, geometry defects,
assembly evidence, limitations, and references retrieved during assessment.

The recommendation is to use this project in preference to ReCurta. Its STEP
assembly supplies named components and placements, and its build manual
supplies assembly and calibration evidence. A complete functioning calculator
still needs explicit motion and state modeling, plus geometric validation.

The pilot's latest request was:

> Ok, create simulation folder in Curta-Type-I-3x with all relevant information
> you already retrieved. I will start a fresh session to simulate it.

This authorized the handoff. It did not ratify a simulation design, choose
optional modifications, or approve a restricted final scope. The incremental
sequence below is a recommendation, not an accepted specification.

## Workspace and workflow

In the assessed workspace:

- Shop: `/home/asa/devel/libresolid-studio`
- Project: `/home/asa/devel/libresolid-studio/projects/Calculators/Curta-Type-I-3x`
- Workspace CLI: `/home/asa/devel/libresolid-studio/.venv/bin/solid`
- Workspace Python: `/home/asa/devel/libresolid-studio/.venv/bin/python`

Start the fresh session through the shop's operating contract and read its
current `skills/simulate-project/SKILL.md`,
`shop-skills/solid-node-api/SKILL.md`, and
`shop-skills/solid-node/SKILL.md`. Those files own the workflow and public API;
this handoff records project evidence and does not replace them. The assessment
used `simulate-project` and the public API/craft references, with Context7
documentation for the mesh and CAD inspection APIs.

This project is an independent Git repository. Confirm its repository root
before writes or commits. Run project commands from this directory with the
workspace environment. Keep project work and its OpenSpec records in this
repository. Do not stage it in the shop or open a shop/framework cycle for it.

At assessment time there was no simulation manifest, Python implementation,
test suite, or OpenSpec record. This handoff adds documentation only. The
fresh session should follow the current `simulate-project` procedure for
proposal, planning commit, implementation, validation, and closeout. Do not
mistake the assessment probes for a successful `solid build` or contract suite.

## Suggested first work

1. Establish the source and import policy for the standard design. Start with
   `CAD/Curta Assembly.step`; retain the upstream geometry. Reconcile its
   constituent solids with the rigid printed groups represented by the STLs.
2. Resolve the one invalid STEP solid and the duplicate hardware product names.
   Establish a reproducible mapping between parts, occurrences, and diagnostic
   findings. Check the initial assembly's fit without assuming that import
   success proves non-interference.
3. Open the project-owned OpenSpec simulation proposal. Record the agreed
   scope, controls, units, rest pose, fidelity limits, and acceptance scenarios.
4. As implementation increments, import the complete static assembly, then
   prove one selectable digit channel, then a carry between adjacent digits.
   Extend to all digits, subtraction, carriage shifting, and clearing as the
   ratified scope requires. These increments are not a proposal to deliver
   only a partial calculator.
5. Use the author's calibration sequence on manual page 53 as a source of
   acceptance scenarios. Add geometric engagement and interference contracts;
   a numerically correct display alone does not prove that the mechanism works.

Do not silently repair upstream files, substitute an optional mod, or claim
force/contact simulation from prescribed kinematics. Geometry findings and any
necessary decisions belong in the project's implementation record.
