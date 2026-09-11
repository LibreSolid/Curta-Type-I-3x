## 1. Source assembly and frame

- [x] 1.1 Add the manifest, an initial renderable root and build exclusions; write and run source and integrity contracts red. Frame build passed; inventory failed with 1 != 547 (faceted, 2026-09-11).
- [x] 1.2 Import the STEP hierarchy, identify the invalid solid and resolve ambiguous hardware with reproducible probes and measurements. All 547 occurrences imported; native invalid product is zero positioning spring (#419219). Repeated names retain their distinct source entity identities; see simulation/docs/measurements.md.
- [ ] 1.3 Verify the complete rest assembly, rigid groups and source overlap inventory; make source and frame contracts green.

## 2. Crank and one selectable digit

- [ ] 2.1 Measure the drum, selector and transmission interfaces; write travel, seating and engagement contracts red.
- [ ] 2.2 Declare crank, drum, selector and shaft joints and drive relations; make the single-channel contracts green.
- [ ] 2.3 Prove mutations of drum axis, selector travel and gear phase fail their intended contracts.

## 3. Carry and registers

- [ ] 3.1 Write adjacent-digit carry and reset contracts red, including the manual's geometric checks.
- [ ] 3.2 Implement the carry mechanism, expand to all digit channels and register dials, and make the contracts green.
- [ ] 3.3 Verify the page-53 arithmetic sequence and complete overflow; prove carry and dial-phase mutations fail.

## 4. Subtraction, carriage and clearing

- [ ] 4.1 Write subtraction-lift, carriage alignment and clearing contracts red.
- [ ] 4.2 Implement the measured joints and relations, including affected flexible parts, and make the contracts green.
- [ ] 4.3 Prove subtraction, shift and clearing mutations fail their intended contracts.

## 5. Complete machine and evidence

- [ ] 5.1 Finish calculator controls, educational show/hide assembly layers and the small instruction set; assert exact targets, layer membership and sample interference through every demonstration.
- [ ] 5.2 Run every node's faceted regression, build the root and inspect its viewer document and all referenced artifacts.
- [ ] 5.3 Render and inspect rest, moving, isometric and alignment snapshots; record measured findings and fidelity limits.
- [ ] 5.4 Run every node's exact regression and write the final simulation README from the verified implementation.
- [ ] 5.5 Validate and sync the accepted specifications, archive the completed change and commit implementation and evidence.

## Current evidence and continuation

The source assembly builds and its complete 547-occurrence world placement check
passes. A +1 mm main-crank placement mutation fails that check with measured
1.00000000007 mm drift at occurrence 0:1:1:18:1; the mutation is reverted.

Task 1.3 remains open. Root tests are honestly red: the zero-positioning spring
is invalid, and the digits-cover/upper-housing boolean produces an invalid result.
The pilot explicitly authorized replacing the spring from the manual's winding
dimensions and measured mounts, and delegated routine engineering decisions.
The documented spring's validity, wire-size and mounting tests now pass, including
the exact mount test. Crank/drum and selector-travel contracts passed after their
red runs. The educational layer test accounts for all 547 source occurrences and
preserves their placements. Six arithmetic tests pass, but do not yet prove
register geometry or drive engagement. Remaining boxes stay open for that work.
