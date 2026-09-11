## ADDED Requirements

### Requirement: Traceable standard assembly
The simulation SHALL account for every component of the standard STEP assembly
and preserve its documented rest placement and the project's attribution.

#### Scenario: Build the standard machine
- **WHEN** the maker builds the default simulation
- **THEN** all 547 source leaf occurrences are represented or explicitly mapped
  to their physically joined printed group, and no optional modification is substituted
- **AND** every transcribed placement agrees with its source within 0.01 mm

### Requirement: Honest physical interfaces
The simulation SHALL verify connected rigid parts and measured assembly
interfaces, recording any source defect that prevents a passing contract.

#### Scenario: Inspect the nominal assembly
- **WHEN** the standard assembly is tested at rest
- **THEN** each rigid part is connected and valid, or a named unresolved finding
  prevents the affected integrity contract from passing
- **AND** any source overlaps are an explicit inventory of pairs and measured
  volumes, with newly introduced or changed overlaps detected

#### Scenario: Operate a verified interface
- **WHEN** a driven pair moves through a complete tooth engagement
- **THEN** the parts stay seated, remain free within measured play, and block
  beyond it in the directions where the mechanism transmits motion

### Requirement: Inspectable machine
The simulation SHALL let a maker inspect the frame, drum, digit transmission,
carry mechanism and complete machine using named subassemblies.

#### Scenario: Inspect a moving pose
- **WHEN** the maker advances the crank from rest
- **THEN** the moving parts follow their own physical axes and the fixed frame
  remains fixed, with material colors distinguishing the mechanism

#### Scenario: Reveal an educational layer
- **WHEN** the maker hides the enclosure or isolates an input, transmission,
  carry, or register assembly in the navigation tree
- **THEN** the tree groups the corresponding mechanical parts together under
  meaningful names, and changing calculator controls moves the visible mechanism
- **AND** purchased fasteners remain grouped with the assembly they secure
