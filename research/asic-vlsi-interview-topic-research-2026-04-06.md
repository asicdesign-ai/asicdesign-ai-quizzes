# ASIC/VLSI Interview Topic Research and Quiz Expansion Plan

Date: 2026-04-06

## Scope

This note answers one practical question for the quiz bank:

Which topics show up most often in public ASIC and digital VLSI interview material, and where should this repository expand next?

The research is intentionally biased toward digital ASIC, RTL, SoC, and front-end interview patterns because:

- that is the dominant scope of the current quiz bank
- the most visible public interview evidence is strongest for RTL, DV, timing, CDC, and test
- "VLSI interview" is too broad to combine digital ASIC, analog, physical design, and verification into one fair ranking without role-specific separation

For this repo, the most useful interpretation is:

Top recurring topics across ASIC RTL, digital design, design integration, and closely adjacent verification interviews.

## Method

I combined three evidence buckets:

1. Public interview banks and study guides that aggregate real interview reports.
2. Recent company-specific interview reports that mention actual screened topics.
3. Current 2025-2026 semiconductor job descriptions that show what hiring teams expect candidates to know.

I then compared the recurring topics against the current repo coverage to identify gaps worth filling next.

## Top 5 Most Common Interview Topics

### 1. RTL coding in Verilog and SystemVerilog

Why it ranks this high:

- It appears in nearly every design-facing interview path.
- It is often used as the first technical screen because interviewers can test both language fluency and design judgment quickly.
- Public interview reports repeatedly mention blocking vs nonblocking, FSM coding, combinational vs sequential coding style, and synthesizable RTL.

Typical question patterns:

- blocking vs nonblocking
- `always_comb` vs `always_ff`
- latch inference
- `wire` vs `reg` vs `logic`
- `case`, `unique case`, `priority case`
- writing an FSM, arbiter, FIFO, counter, or handshake block
- signed arithmetic and width propagation

Why it matters for this repo:

- `quizzes/verilog/` is empty
- `quizzes/systemverilog/` has only 1 item
- some related semantics already live under `quizzes/simulation/`, but direct interview-style language coverage is still thin

### 2. Static timing analysis and SDC constraints

Why it ranks this high:

- Timing is one of the few topics that crosses front-end RTL, integration, synthesis, and signoff roles.
- Public interview guides and current job descriptions both emphasize setup/hold, constraints, clocking, and timing closure.
- Interviewers use timing questions to test whether a candidate can reason about real silicon behavior instead of only simulation behavior.

Typical question patterns:

- setup vs hold
- positive and negative skew
- false path vs multicycle path
- `set_input_delay` and `set_output_delay`
- generated clocks
- asynchronous clock groups
- useful skew
- timing closure tradeoffs

Why it matters for this repo:

- `quizzes/sta/` is already strong at 21 items
- the next opportunity is not breadth but deeper signoff-level coverage

### 3. CDC and RDC fundamentals

Why it ranks this high:

- CDC appears in both interview banks and current job postings as a direct screening topic.
- It is a strong discriminator because many candidates know the textbook 2-FF synchronizer but struggle with pulses, multi-bit crossings, reconvergence, RDC, or async FIFOs.
- CDC questions are common in design, integration, and verification interviews.

Typical question patterns:

- metastability and MTBF
- 2-FF synchronizer limits
- slow-to-fast vs fast-to-slow crossings
- handshake synchronizers
- async FIFO pointer design
- Gray code usage
- reset deassertion synchronization
- reconvergence and false CDC violations
- RDC vs CDC

Why it matters for this repo:

- `quizzes/cdc/` is already strong at 21 items
- the highest-value additions are advanced CDC/RDC questions rather than beginner repetition

### 4. Digital design and microarchitecture problem solving

Why it ranks this high:

- Interviewers frequently move from language trivia into a design exercise.
- Public interview reports repeatedly mention FSMs, FIFOs, pipelining, arbitration, cache behavior, register slices, and protocol reasoning.
- Current design job descriptions also emphasize data path and control path design, micro-architecture, and standard interconnect familiarity.

Typical question patterns:

- design an FSM from a spec
- build a synchronous or asynchronous FIFO
- design an arbiter or register slice
- explain pipelining tradeoffs
- valid/ready backpressure behavior
- cache write-back vs write-through
- AMBA basics
- throughput vs latency tradeoffs

Why it matters for this repo:

- protocol and architecture coverage exists in `quizzes/amba/`, `quizzes/cache-coherency/`, and `quizzes/l2-cache-controller/`
- the repo is still missing a focused learner-facing lane for general RTL design and microarchitecture interview problems

### 5. DFT and testability

Why it ranks this high:

- DFT is not asked in every role, but it shows up consistently enough across ASIC and integration hiring to make the top five.
- Current job postings still call out scan, ATPG, BIST, and test planning directly.
- Many broad VLSI interview guides include scan-chain and testability questions even outside dedicated DFT roles.

Typical question patterns:

- scan chain purpose
- stuck-at vs transition fault
- ATPG basics
- LBIST and MBIST
- OCC usage
- compression and X-handling
- JTAG basics
- lockup latches

Why it matters for this repo:

- `quizzes/dft/` is already strong at 20 items
- like STA and CDC, the best next additions are more advanced, role-realistic scenarios

## Honorable Mention: Low Power and Clock Gating

This topic did not make the top five on recurrence, but it is rising and worth special attention.

Why it still matters:

- public interview guides explicitly call out clock gating
- Arm-style front-end roles increasingly mention multi-power domains, clock gating, CDC partitioning, and UPF familiarity
- this repo only has 5 clock-gating items and no dedicated low-power lane

Recommendation:

Treat low power as the highest-value expansion just outside the top five.

## Evidence Summary

The following source set strongly supports the ranking above.

### Interview banks and study guides

- Hardware Interview study guide:
  - sections on low power, advanced RTL, STA, CDC, and bus interconnect design
  - includes questions on arbitration, memory-controller design, async FIFO constraints, `set_input_delay` and `set_output_delay`, useful skew, CDC reconvergence, reset synchronizers, and AXI crossings
  - https://www.hardware-interview.com/study

- VLSIGuru "Top VLSI Interview Questions and How to Answer Them":
  - highlights blocking vs nonblocking, setup and hold, ASIC design flow, clock gating, metastability, synthesis, scan chain, and SDC
  - https://vlsiguru.com/blog/top-vlsi-interview-questions-and-how-to-answer-them

- VLSI Verify interview introduction:
  - identifies Digital Electronics, Verilog, SystemVerilog, DFT, STA, and computer architecture as recurring interview preparation areas
  - https://vlsiverify.com/interview-questions/

### Company-specific public interview reports

- Qualcomm RF DV interview report:
  - Mealy vs Moore, CDC methods, and coding an FSM in Verilog
  - https://www.hardware-interview.com/question/789ea373-a29b-48fa-a6bd-fa3f87726008

- Apple CPU DV interview report:
  - cache coherence protocols, cache questions, prefetching, write-back, and write-through
  - https://www.hardware-interview.com/question/46ff425d-9012-4a4c-bdd5-8128c3e3bf74

- Qualcomm SoC verification interview report:
  - blocking vs nonblocking, pipelining, delay reasoning, and verification flow questions
  - https://www.hardware-interview.com/question/c1be8ed0-1c91-4a10-8e13-4b97d39a8f40

- Amazon phone-screen examples listed in the Hardware Interview study guide:
  - async FIFO constraints and timing-path reasoning
  - https://www.hardware-interview.com/study

### Current job descriptions

- Arm Principal Hardware Design Engineer:
  - calls out multi-clock and multi-power domain design, CDC architecture, clock gating strategy, SystemVerilog/Verilog RTL, AMBA familiarity, and timing-closure exposure
  - https://careers.arm.com/job/sophia-antipolis/principal-hardware-design-engineer/33099/91645123456

- Synopsys IP Design Technical Lead / Staff ASIC RTL Design Engineer:
  - calls out synthesizable Verilog/SystemVerilog, timing closure, CDC analysis, lint, static timing analysis, and protocol familiarity including AMBA
  - https://careers.synopsys.com/job/bengaluru/ip-design-technical-lead-staff-asic-rtl-design-engineer/44408/90581151808

- NVIDIA Senior STA Engineer:
  - calls out PrimeTime, constraints, SDC generation, advanced STA, timing ECOs, and full timing closure
  - https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/Senior-STA-Engineer--Sub-Chip_JR2001453

- NVIDIA Senior DFT Engineer:
  - calls out scan test plans, BIST, fault modeling, ATPG, and fault simulation
  - https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/Senior-DFT-Engineer_JR2000499

## Current Repo Coverage Snapshot

As of 2026-04-06:

- `cache-coherency`: 30
- `cdc`: 21
- `sta`: 21
- `amba`: 20
- `dft`: 20
- `simulation`: 16
- `l2-cache-controller`: 10
- `clock-gating`: 5
- `firmware`: 1
- `systemverilog`: 1
- `verilog`: 0

## Gap Analysis

### Strong already

- `cdc`
- `sta`
- `dft`
- `amba`
- `cache-coherency`

### Moderately covered but still expandable

- `simulation`
- `l2-cache-controller`
- `clock-gating`

### Under-covered relative to interview frequency

- `verilog`
- `systemverilog`
- general RTL design and microarchitecture coding exercises
- low power beyond basic clock-gating
- synthesis and design-flow literacy as a dedicated learner-facing lane

## Recommended Quiz Expansion Roadmap

### Phase 1: Highest ROI

#### 1. Populate `quizzes/verilog/` with 15-20 core interview items

Suggested topics:

- blocking vs nonblocking beyond the beginner one already covered in `simulation`
- `wire`, `reg`, and `logic`
- inferred latch patterns
- `case`, `casex`, `casez`, `unique case`, `priority case`
- signed vs unsigned arithmetic
- reduction operators
- concatenation and replication
- packed vs unpacked dimensions
- `generate` blocks
- parameter override patterns
- synthesis vs simulation mismatch traps
- `full_case` and `parallel_case` anti-patterns

#### 2. Expand `quizzes/systemverilog/` to 15-20 items

Suggested topics:

- `always_comb`, `always_ff`, `always_latch`
- enum typing and state-encoding clarity
- structs and packed structs
- interfaces and modports
- packages and imports
- `typedef` usage
- `logic` in synthesizable RTL
- `unique` and `priority` semantics
- assertions for simple protocol properties
- immediate vs concurrent assertions at an interview-prep depth

#### 3. Create a new `quizzes/rtl-design/` lane with 20-25 design exercises

Suggested topics:

- FSM design tradeoffs
- sequence detector architecture
- synchronous FIFO interview questions
- skid buffers and valid/ready timing
- round-robin vs fixed-priority arbiters
- pulse stretcher design
- register slice insertion
- pipelining for timing closure
- fanout bottlenecks
- counter rollover edge cases
- one-hot vs binary state encoding
- mux-tree vs shared-resource tradeoffs

Why this lane should exist:

- it captures the most interview-like "design a block" questions that do not fit cleanly into `verilog`, `systemverilog`, `amba`, or `cdc`

### Phase 2: Next best additions

#### 4. Create `quizzes/synthesis/` with 10-15 items

Suggested topics:

- what synthesis changes and what it does not
- latch inference from incomplete conditionals
- retiming intuition
- area vs timing vs power tradeoffs
- resource sharing
- constant propagation
- reset style impact
- high-fanout nets
- synthesis pragmas and when not to trust them blindly
- lint vs synthesis vs STA responsibility boundaries

#### 5. Expand `quizzes/clock-gating/` into a broader low-power lane

Two good options:

- keep `clock-gating` and grow it to 12-15 items
- or create `quizzes/low-power/` and keep `clock-gating` as a subtopic

Suggested topics:

- integrated clock-gating latch behavior
- clock enable vs gated clock tradeoffs
- isolation cells
- retention flops
- power gating basics
- on-to-off and off-to-on crossings
- UPF intent at interview depth
- wakeup sequencing
- low-power verification gotchas

### Phase 3: Deepen strong lanes with advanced items

#### 6. Add advanced `sta` items

Suggested topics:

- graph-based vs path-based analysis
- OCV, AOCV, and POCV intuition
- generated-clock mistakes
- `set_clock_groups` vs false paths
- useful skew tradeoffs
- asynchronous reset timing checks
- timing exceptions audit questions

#### 7. Add advanced `cdc` items

Suggested topics:

- RDC-specific questions
- MCP synchronizers
- toggle synchronizers vs pulse synchronizers
- async FIFO full and empty corner cases
- CDC waiver triage
- CDC-safe clock-gating controls

#### 8. Add advanced `dft` items

Suggested topics:

- transition fault vs stuck-at
- X-bounding and X-masking
- compression architecture intuition
- chain balancing
- at-speed test tradeoffs
- MBIST algorithm intuition

## Prioritized Topic List for Immediate Authoring

If the goal is maximum portfolio impact with minimum duplication, the next 50 quiz items should be allocated like this:

1. `verilog`: 16
2. `systemverilog`: 14
3. `rtl-design`: 12
4. `clock-gating` or `low-power`: 4
5. `synthesis`: 4

Reason:

- these are the biggest coverage gaps relative to interview frequency
- they complement existing strong banks instead of overfilling already-healthy areas

## Recommended Quiz Authoring Rules for These New Topics

- Keep interview-style prompts concrete and realistic rather than trivia-heavy.
- Favor questions that reveal design reasoning, not just vocabulary recall.
- When a topic is a common coding screen question, prefer explanations that compare correct and incorrect coding styles directly.
- When a topic is timing- or protocol-heavy, write long explainers so they can later pair with WaveDrom or Mermaid diagrams.
- For language questions already partially covered under `simulation`, avoid duplicates by reframing around synthesizable RTL intent.

## Final Recommendation

If only one expansion wave is approved next, do this:

1. create `quizzes/verilog/`
2. expand `quizzes/systemverilog/`
3. create `quizzes/rtl-design/`

That wave best matches the research signal and addresses the clearest repo gaps.
