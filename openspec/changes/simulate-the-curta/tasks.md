## 1. Source assembly and frame

- [x] 1.1 Add the manifest, an initial renderable root and build exclusions; write and run source and integrity contracts red. Frame build passed; inventory failed with 1 != 547 (faceted, 2026-09-11).
- [x] 1.2 Import the STEP hierarchy, identify the invalid solid and resolve ambiguous hardware with reproducible probes and measurements. All 547 occurrences imported; native invalid product is zero positioning spring (#419219). Repeated names retain their distinct source entity identities; see simulation/docs/measurements.md.
- [ ] 1.3 Verify the complete rest assembly, rigid groups and source overlap inventory; make source and frame contracts green.

## 2. Crank and one selectable digit

- [x] 2.1 Measure the drum, selector and transmission interfaces; write travel, seating and engagement contracts red. Measurements and red evidence are recorded in simulation/docs/measurements.md.
- [x] 2.2 Declare crank, drum, selector and shaft joints and drive relations; make the single-channel contracts green. The complete result/counter drum sweeps also pass faceted and exact (20 result settings/modes, both counter modes).
- [ ] 2.3 Prove mutations of drum axis, selector travel and gear phase fail their intended contracts.

## 3. Carry and registers

- [x] 3.1 Write adjacent-digit carry and reset contracts red, including the manual's geometric checks. Dial-pin, fork and reset-shoe contracts failed; native probes identified the contacts. Timing tests rejected an early reset, and the installed bank exposed a nine-degree half-pin mounting discrepancy plus shifted-neighbour contact.
- [x] 3.2 Implement the carry mechanism, expand to all digit channels and register dials, and make the contracts green. All fifteen carries pass both kernels through two revolutions and all carriage shifts; the complete bell spring's mounting and subtraction sweep now pass native as well.
- [ ] 3.3 Verify the page-53 arithmetic sequence and complete overflow; prove carry and dial-phase mutations fail.

## 4. Subtraction, carriage and clearing

- [x] 4.1 Write subtraction-lift, carriage alignment and clearing contracts red. World-vertex tests exposed missing 9 mm subtraction, 6 mm carriage lift, 20° shift, plate rotation and spring-seat motion.
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

Task 1.3 remains open. The initial red root tests exposed the invalid spring
and an invalid digits-cover/upper-housing boolean.
The pilot explicitly authorized replacing the spring from the manual's winding
dimensions and measured mounts, and delegated routine engineering decisions.
The documented spring's validity, wire-size and mounting tests now pass, including
the exact mount test. Crank/drum and selector-travel contracts passed after their
red runs. The educational layer test accounts for all 547 source occurrences and
preserves their placements. Six arithmetic tests pass, but do not yet prove
complete register geometry or drive engagement. The single-row input passage
and first bevel pair now pass exact and faceted engagement contracts, after
documented fitting corrections. Seventeen dial joints are connected to the
settled register ports and sub-turn cycle relations. Three register geometry
tests pass both kernels, including every result dial's independent radial axis
and visible input preceding carry. The browser check passed the manual's full
0, 1, 9, 90 sequence with retained registers, eight digit sliders and recursive
layer visibility/focus. The drum/tens-bell printed groups are reconciled; their
inventory, connectivity and native validity pass exact. The 9 mm subtraction
lift passed after its red world-vertex test. Keyed input travel and 72° shaft
rotation passed after red; all seventeen source-specific stacks are integrated.
The complete result/counter drum sweeps now pass both kernels after the documented
input-sleeve fits and .36 mm counter-tooth relief. Sliding carry levers, rotating
tens bell, 6 mm carriage lift, 20° shift and rotating clearing plate pass their
motion checks. Carriage spring compression passes its faceted seat and validity
tests and its two exact tests. Lower/upper decimal-marker ownership passes
while all 547 source placements remain accounted for. A material-connectivity
contract verifies the fitted print's enclosed cavities without mistaking them
for detached material. The axial bevel fit's newly exposed frame interference
is corrected by shortening the protruding stem, verified exact.
The installed bevel bank now passes both kernels across all six shift positions,
lifted intermediate positions and all seventeen ±12° flank engagement checks,
after centering dial clocking by -3°. Six worked examples pass arithmetic and
model replay tests; seven instruction endpoints and a routed carriage scenario
pass. The first carry pairs pass complete bell contact sweeps and both ±12°
locking / active-tooth engagement limits in both kernels after centered profiles
and measured passage timing. A spring tessellation-budget
test exposed 7,968,048 triangles; four samples per spline span preserve geometry
while making the viewer mesh manageable. The updated browser run passed every
example, retained-operation checks, lift/shift guards and layer controls.
The zero-cam/follower has six passing contracts in both kernels, including the
drive pin's axial travel, seated roller contact and moving spring mounts. The
anti-reversal pawl follows the measured ratchet, including its shorter closing
interval; forward contact, reverse blocking, release clearance and moving spring
mounts pass exact. Its collar/plate and spring-anchor fits are recorded explicitly.
The fifteen carry U-wires now follow the measured detents with fixed closed folds;
twelve wire/travel/contact contracts pass both kernels. The manual's two clearing
tooth strips and spacer were missing from the STEP but present as flat STLs. Their
formed groove fit passes faceted. The integrated root now keeps all 547 original
leaves plus these three prints, with twelve passing checks; the source housing
overlap remains the one failing ordinary interference assertion.
The clearing gear's missing-tooth gap fixes the absolute zero, previously
undetermined by bevel phase alone. Four whole dial pitches correct all seventeen
dials without changing bevel engagement; that bank's exact regression passes.
After the documented groove-depth and clearing-flank fits, both racks reset the
dials sequentially. Five clearing contracts pass both runners, including every
digit/station, eighth-tooth passages and paired free/blocked engagement checks.
Reversing the clearing law fails three geometry contracts; it is restored.
The new first-carry contact bench exposed dial-pin and reset-bell collisions;
native probes confirmed fixed fork/sleeve and reset-shoe contacts. Documented
local fits, measured pin approach and real reset-cam timing now pass six native
checks over two turns, including one-sided driving contacts. Carry remains
latched across the cycle boundary where its cam requires it. The complete
fifteen-station cascade passes both kernels after aligning the half-pin flats
with the manual's 36 degrees and choosing the cutaway side that clears parked
neighbouring digits. All six carriage positions are covered, as are two-turn
cascades. The twelve carry-wire checks remain green after the slider fits.
The bell's positioning leaf spring now preserves its native plate and tapered
hooks while measured ribbed arms bend through the subtraction stroke. Its
source-fidelity, one-body, mounting and full-travel contracts pass; the whole
bell and its two spring screws share one revolute joint. The restoring screw
also clears the three formed clearing strips after a strictly bounded back
relief that leaves every tooth face unchanged. All seventeen register balls and
tapered spider fingers now pass native source-fidelity, continuity, seating,
carry/subtraction and progressive-clearing checks. The spring-loaded clearing
stop also passes seven contracts in both kernels, including native cam contact
through a half-degree sweep and both spring endpoints. A whole-machine relative-
placement audit identifies the remaining cover/window, frame-guide and retained-
seat interfaces; these are not silently treated as fixed source overlaps.
Inter-system contact, the whole-machine overlap inventory and demonstration sweeps keep
their tasks open. These results are checkpoints, not final delivery evidence.
