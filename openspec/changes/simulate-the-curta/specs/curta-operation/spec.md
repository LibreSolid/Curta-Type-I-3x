## ADDED Requirements

### Requirement: Calculator controls
The simulation SHALL express operation in calculator terms: eight decimal input
digits, crank progress, addition or subtraction, carriage position and clearing.
Every displayed pose SHALL be reproducible from its stated starting registers
and controls, with the state convention explained to the maker.

#### Scenario: Set an input digit
- **WHEN** an input changes from zero to nine
- **THEN** its selector moves from the top detent to the bottom detent and its
  matching transmission gear follows the measured selector travel

#### Scenario: Shift a decimal place
- **WHEN** the carriage is lifted, advanced one position and reseated
- **THEN** the input's contribution to the result is multiplied by ten and the
  physical carriage aligns with the next digit position

### Requirement: Author calibration sequence
The simulation SHALL reproduce the arithmetic and associated mechanism motion
of the calibration checks on page 53 of the build manual.

#### Scenario: Zero and successive carries
- **WHEN** cleared registers receive successive crank turns with inputs 0, 1,
  9 and 90
- **THEN** the result register reads 0, 1, 10 and 100 respectively, and the
  turns register reads 1, 2, 3 and 4

#### Scenario: Cascade through both registers
- **WHEN** all eleven result dials and six turns dials start at nine and the
  maker adds one
- **THEN** every result and turns dial returns to zero through the carry sequence

#### Scenario: Add and subtract one
- **WHEN** the maker adds one to cleared registers and then subtracts one
- **THEN** both registers return to zero

### Requirement: Carry engagement and reset
The simulation SHALL move each carry lever and gear consistently with the
manual's depressed, engaged and reset positions.

#### Scenario: Carry into the next digit
- **WHEN** a dial passes nine during addition
- **THEN** its lever enables the adjacent carry gear, the tens bell advances
  the next shaft once, and the mechanism returns the lever to its upper position

### Requirement: Clearing and repeatable demonstrations
The simulation SHALL provide a small named demonstration set that includes
normal addition, carry, overflow, subtraction, carriage shifting and clearing.

#### Scenario: Clear a register
- **WHEN** the maker completes the clearing-ring movement
- **THEN** the affected dials reach zero and the ring reaches its rest position

#### Scenario: Replay a demonstration
- **WHEN** the same demonstration is replayed or its timeline is revisited
- **THEN** it reaches the same exact targets, and geometric sampling checks the
  moving interfaces throughout the demonstration
