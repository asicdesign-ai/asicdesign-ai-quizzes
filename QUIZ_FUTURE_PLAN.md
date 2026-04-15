# QUIZ_FUTURE_PLAN.md

## Purpose

This file is the working execution plan for the next major quiz-bank expansion.

It converts the research in `research/asic-vlsi-interview-topic-research-2026-04-06.md` into a concrete authoring backlog with lane decisions, content rules, and a question-by-question plan.

This wave should be authored as broad educational content for freshers, beginners, and seasoned engineers alike. Avoid recruitment-oriented framing, and prefer language about understanding, practice, and knowledge-building.

## Status

- Plan date: 2026-04-06
- Updated after interactive planning review: 2026-04-06
- Overall status: completed
- Total planned questions in this wave: 50
- Scope:
  - `rtl-design`: 35
  - `synthesis`: 15
- Progress:
  - authored so far: 50 of 50
  - completed batches: Batch 1, Batch 2, Batch 3
  - next recommended batch: future backlog refresh

- Outside-wave note:
  - A separate `error-detection` category was added on 2026-04-15 with 10 initial reviewed questions covering parity, CRC, Hamming distance, SECDED, ECC memory, and retransmission tradeoffs.

## Planning Answers Captured

- Audience: mixed
- Reasoning depth: mix of quick checks and deeper engineering reasoning
- Tone: education-first, with realistic engineering scenarios
- Role focus: generic ASIC
- HDL language bias: SystemVerilog-first framing
- Assertions: include inside `rtl-design`
- `rtl-design` balance: even split between control and datapath where practical
- `synthesis` style: general concepts are primary, but it is acceptable to assume familiarity with tools such as Fusion Compiler, Genus, and Design Compiler
- Difficulty: include a few intentionally hard separators
- Distractors: plausibly wrong, not obviously wrong
- Immediate explanation: keep short
- Learn-mode explanation: medium-long, with emphasis on diagrams and schematics
- Visual timing depth: basic handshakes, stalls, and bubbles by default
- Diagram style: mostly consistent where practical
- References: not required for very trivial questions; required when the claim is methodological, nuanced, tool-behavior-related, or otherwise non-obvious
- `human_verified` default for new items: `false`
- Overlap with existing `simulation`, `cdc`, and `sta` content: avoid overlap
- Style guidance: mention when multiple styles are acceptable, but keep explanations concise
- Execution pace: continue through the whole wave
- Existing `quizzes/systemverilog/flop-reset-value.yml`: move into `rtl-design`
- Completion bar: full QA pass
- Plan flexibility: allow small refinements during execution

## Repo Decisions For This Wave

### 1. Do not create a separate `rtl-hdl` lane

Decision:

- Do not create `quizzes/rtl-hdl/`.
- Fold RTL language, synthesizable coding style, and assertion-related questions into `quizzes/rtl-design/`.
- Do not add new files under `quizzes/verilog/`.
- Do not add new files under `quizzes/systemverilog/` for this wave.

Reason:

- The user wants one broader RTL learning lane rather than a split between language and design.
- In practice, SystemVerilog syntax, coding intent, and design reasoning reinforce each other and are easier to learn together.

### 2. Use `rtl-design` as the main RTL learning lane

Decision:

- `quizzes/rtl-design/` will contain both:
  - 15 RTL coding / SystemVerilog intent questions
  - 20 design and microarchitecture questions

Reason:

- This keeps the learner experience aligned with real design work, which rarely separates coding semantics cleanly from design reasoning.

### 3. Keep `synthesis` focused on low-to-mid complexity

Decision:

- Create `quizzes/synthesis/` with practical educational synthesis questions.
- Keep the topic generally tool-agnostic in concept, but it is fine to mention familiar synthesis behavior that many engineers may associate with Fusion Compiler, Genus, or Design Compiler.
- Avoid deep signoff-specialist topics in this wave.

Reason:

- The immediate goal is broad ASIC learning value and knowledge building.

## Content Rules For This Wave

### Global rules

- Keep questions concrete and engineering-oriented.
- Prefer design reasoning over trivia.
- Use one quiz item per file.
- Preserve references when the answer depends on methodology, tool behavior, or a non-obvious claim.
- Do not overlap with existing `simulation`, `cdc`, and `sta` content unless a question is materially reframed and adds distinct learner value.
- All new items should default to `human_verified: false`.
- Wrong choices should be plausible enough to reflect real misunderstandings.
- Include a few hard separator questions in the overall set.
- Correct-answer positions should be balanced fairly across each authored batch. Avoid obvious answer-key patterns such as all-`a` or heavily front-loaded correct choices.

### Explanation rules

- `answer.short_explainer` should stay short and immediate.
- `answer.explanation` should be medium-long and suitable for a Learn mode experience.
- Learn-mode explanations should prefer visual teaching where helpful, especially WaveDrom, Mermaid, and block/schematic-style diagrams.
- When multiple coding styles are acceptable, mention that briefly without turning the explanation into a long style debate.

### `rtl-design` rules

- Every `rtl-design` item must include example RTL code.
- The 20 design-heavy questions should strongly prefer visual assets in the question or explanation.
- Some visuals may be added later when the question still teaches well without them on day one.
- Use Mermaid at medium detail when included.
- Keep diagram style mostly consistent across the set.
- Use WaveDrom mainly for handshakes, stalls, bubbles, and similar timing flows unless a corner case is the core point of the question.
- Assertion-related questions belong in `rtl-design`, not in a separate lane.
- SystemVerilog should be the default modern framing unless the question is explicitly about older Verilog behavior.

### `synthesis` rules

- Stay at low-to-mid complexity.
- Focus on RTL-to-gates consequences that learners can reason through without niche physical-signoff expertise.
- It is acceptable to mention familiar behavior patterns associated with mainstream synthesis tools, but the question should still teach a general principle.
- Use simple code snippets where they materially help.

## Execution Order

1. Create `quizzes/rtl-design/` and author the 15 RTL coding / SystemVerilog intent questions.
2. Continue in `quizzes/rtl-design/` with the 20 design and microarchitecture questions.
3. Create `quizzes/synthesis/` and author the 15 synthesis questions.
4. Move `quizzes/systemverilog/flop-reset-value.yml` into `quizzes/rtl-design/` during the wave.
5. Run metadata validation and a full QA pass after each meaningful batch.
6. Continue through the whole wave unless a major issue appears.
7. Update this file as scope, status, or lane decisions change.

## Batch Plan

### Batch 1: `rtl-design` coding and SystemVerilog intent set

Status: completed on 2026-04-06

Target: 15 questions

Definition of done:

- all 15 files created under `quizzes/rtl-design/`
- each has example RTL code
- each has a strong `answer.short_explainer`
- questions avoid overlap with existing `simulation` items
- the set feels practice-oriented rather than textbook-only
- the batch passes full QA

### Batch 2: `rtl-design` design and microarchitecture set

Status: completed on 2026-04-06

Target: 20 questions

Definition of done:

- all 20 files created under `quizzes/rtl-design/`
- every question has code
- visuals are included where they add clear value, with some allowed to land in a follow-up pass
- the set includes WaveDrom, Mermaid FSM, and Mermaid block-diagram coverage
- the batch passes full QA

### Batch 3: `synthesis` core set

Status: completed on 2026-04-06

Target: 15 questions

Definition of done:

- all 15 files created under `quizzes/synthesis/`
- explanations focus on reasoning, not tool-brand trivia
- question difficulty stays low-to-mid complexity, with a few harder separators allowed
- the batch passes full QA

## Question Backlog

## `rtl-design` backlog: RTL coding and SystemVerilog intent

Target directory: `quizzes/rtl-design/`

| Status | Planned file | Working title | Core teaching goal |
| --- | --- | --- | --- |
| completed | `rtl-design-logic-default-for-synthesizable-rtl.yml` | Why is `logic` a better default than `wire` or `reg` for most synthesizable RTL? | Teach the practical boundary between variable semantics and old Verilog type habits. |
| completed | `rtl-design-always-ff-contract.yml` | What design mistakes does `always_ff` help prevent compared with plain `always`? | Show why `always_ff` is an intent declaration, not just syntax sugar. |
| completed | `rtl-design-always-comb-complete-assignment.yml` | Why do complete assignments still matter even when using `always_comb`? | Connect `always_comb` intent to latch avoidance and readable combinational coding. |
| completed | `rtl-design-always-latch-explicit-intent.yml` | When should `always_latch` be used, and why is accidental latch inference usually a bug? | Separate intentional storage from incomplete combinational code. |
| completed | `rtl-design-latch-inference-from-missing-else.yml` | Which coding pattern accidentally infers a latch, and why? | Make latch inference easy to spot from small RTL snippets. |
| completed | `rtl-design-unique-vs-priority-case.yml` | When should `unique case` be preferred over `priority case`, and what hardware intent does each imply? | Teach case-style intent and the cost of getting it wrong. |
| completed | `rtl-design-casez-vs-casex-safety.yml` | Why is `casez` usually safer than `casex` in synthesizable RTL? | Cover X-masking dangers in design code. |
| completed | `rtl-design-packed-vs-unpacked-array-modeling.yml` | When should a structure be modeled as a packed vector versus an unpacked array? | Clarify bus-style data versus collection-style storage. |
| completed | `rtl-design-signed-width-extension-trap.yml` | What common signed and width-extension mistake changes arithmetic results in RTL? | Teach arithmetic correctness, not just syntax. |
| completed | `rtl-design-generate-loop-parameterization.yml` | When is a `generate for` loop the right RTL pattern? | Show scalable replication and elaboration-time structure. |
| completed | `rtl-design-parameter-vs-localparam-boundary.yml` | When should a value be a `parameter` versus a `localparam`? | Teach override boundaries and API hygiene for reusable RTL. |
| completed | `rtl-design-enum-state-typing-benefit.yml` | Why do typed enums improve FSM readability and debug quality? | Tie language features to maintainable control logic. |
| completed | `rtl-design-packed-struct-bus-bundling.yml` | When is a packed struct better than manual bit slicing? | Improve readability and reduce indexing bugs. |
| completed | `rtl-design-concurrent-assertion-handshake-check.yml` | Which concurrent assertion best checks a simple valid/ready handshake requirement? | Introduce basic assertion reasoning without turning the lane into pure verification trivia. |
| completed | `rtl-design-flop-reset-value-constant.yml` | Invalid reset-value source in `always_ff` reset code | Check whether learners distinguish a true reset constant from another runtime signal. |

## `rtl-design` backlog: design and microarchitecture

Target directory: `quizzes/rtl-design/`

Visual asset policy for this 20-question subset:

- every item: example RTL code
- visuals strongly preferred in the first authoring pass
- some visuals may be deferred if the explanation still works and the follow-up need is noted
- at least 8 items: WaveDrom
- at least 6 items: Mermaid FSM
- at least 10 items: Mermaid block diagram

| Status | Planned file | Working title | Required assets | Core teaching goal |
| --- | --- | --- | --- | --- |
| completed | `rtl-design-sequence-detector-mealy-vs-moore.yml` | Should this sequence detector be Mealy or Moore? | code, Mermaid FSM, WaveDrom | Compare output timing, state count, and glitch tradeoffs. |
| completed | `rtl-design-register-slice-valid-ready.yml` | What does a one-stage valid/ready register slice change in latency and backpressure behavior? | code, Mermaid block diagram, WaveDrom | Teach handshake decoupling and pipeline insertion. |
| completed | `rtl-design-skid-buffer-backpressure.yml` | Why is a skid buffer useful when the downstream side stalls late? | code, Mermaid block diagram, WaveDrom | Show how a skid buffer preserves throughput without dropping data. |
| completed | `rtl-design-sync-fifo-full-empty-logic.yml` | Which full/empty strategy is safest for a synchronous FIFO teaching example? | code, Mermaid block diagram, WaveDrom | Cover occupancy tracking and off-by-one mistakes. |
| completed | `rtl-design-round-robin-arbiter-fairness.yml` | Why does a round-robin arbiter avoid starvation that a fixed-priority arbiter can create? | code, Mermaid block diagram | Teach fairness and implementation cost. |
| completed | `rtl-design-fixed-priority-arbiter-starvation.yml` | In which situation is a fixed-priority arbiter still the right choice? | code, Mermaid block diagram, WaveDrom | Show simplicity-versus-fairness tradeoffs. |
| completed | `rtl-design-onehot-vs-binary-fsm-encoding.yml` | When is one-hot FSM encoding worth the extra flops? | code, Mermaid FSM | Compare decode simplicity, area, and speed. |
| completed | `rtl-design-pulse-stretcher-minimum-width.yml` | How can an RTL pulse stretcher guarantee a request stays visible for enough cycles? | code, WaveDrom | Teach minimum pulse-width control. |
| completed | `rtl-design-counter-terminal-count-pulse.yml` | What is the cleanest way to generate a one-cycle terminal-count pulse? | code, WaveDrom | Reinforce counter edge cases and rollover logic. |
| completed | `rtl-design-credit-counter-flow-control.yml` | How does a credit counter implement flow control without per-transfer acknowledgements? | code, Mermaid block diagram, WaveDrom | Connect counters to practical pipeline throttling. |
| completed | `rtl-design-pipeline-register-critical-path.yml` | Where should a pipeline register be inserted to shorten the critical path without breaking behavior? | code, Mermaid block diagram | Teach timing-driven microarchitecture changes. |
| completed | `rtl-design-fanout-heavy-enable-restructuring.yml` | Why does a wide-enable network become a timing bottleneck, and how should the RTL be restructured? | code, Mermaid block diagram | Teach fanout-aware architectural fixes. |
| completed | `rtl-design-mux-tree-vs-shared-bus.yml` | When is a mux tree better than a shared bus with centralized select logic? | code, Mermaid block diagram | Compare timing, fanout, and modularity tradeoffs. |
| completed | `rtl-design-request-ack-level-handshake.yml` | Why is a level-based request/acknowledge handshake safer than a pulse in some control paths? | code, Mermaid block diagram, WaveDrom | Teach robust control transfer design. |
| completed | `rtl-design-busy-idle-done-controller-fsm.yml` | What is the simplest correct FSM for an idle, busy, done control block? | code, Mermaid FSM, WaveDrom | Walk through state design from a small behavioral spec. |
| completed | `rtl-design-write-buffer-decouples-producer-consumer.yml` | Why does a write buffer improve throughput even when the main datapath is unchanged? | code, Mermaid block diagram, WaveDrom | Show queue-based decoupling between producer and consumer. |
| completed | `rtl-design-valid-ready-bubble-propagation.yml` | How do bubbles propagate through a multi-stage valid/ready pipeline? | code, Mermaid block diagram, WaveDrom | Teach throughput loss and stall propagation. |
| completed | `rtl-design-iterative-vs-pipelined-datapath.yml` | When should an iterative datapath be chosen over a pipelined datapath? | code, Mermaid block diagram | Compare area, throughput, and latency. |
| completed | `rtl-design-timeout-counter-controller.yml` | How should a timeout counter interact with a controller FSM? | code, Mermaid FSM, WaveDrom | Combine control logic with time-based exit behavior. |
| completed | `rtl-design-address-decode-onehot-vs-encoded.yml` | When is one-hot address decode preferable to encoded select logic? | code, Mermaid block diagram | Teach decode depth and wiring tradeoffs. |

## `synthesis` backlog

Target directory: `quizzes/synthesis/`

Difficulty policy:

- low-to-mid complexity only, with a few harder separators allowed
- avoid AOCV, POCV, SI, or advanced signoff-only topics in this wave

| Status | Planned file | Working title | Core teaching goal |
| --- | --- | --- | --- |
| completed | `synthesis-incomplete-conditional-infers-latch.yml` | Why does an incomplete conditional infer a latch after synthesis? | Tie simple RTL omissions to unintended hardware. |
| completed | `synthesis-default-assignment-avoids-latch.yml` | Why do default assignments often fix unintended latch inference cleanly? | Show a practical combinational coding pattern. |
| completed | `synthesis-resource-sharing-area-throughput-tradeoff.yml` | When does resource sharing save area but hurt throughput? | Connect microarchitecture choices to synthesized hardware. |
| completed | `synthesis-constant-propagation-removes-dead-logic.yml` | What kinds of RTL logic disappear because of constant propagation? | Teach why some written logic never reaches the gate-level netlist. |
| completed | `synthesis-retiming-register-movement-intuition.yml` | What problem can retiming solve without changing cycle-level behavior? | Give a practical retiming intuition without deep theory. |
| completed | `synthesis-high-fanout-control-path-cost.yml` | Why can a single control bit become the critical path after synthesis? | Explain fanout cost and replicated-control fixes. |
| completed | `synthesis-reset-mux-datapath-cost.yml` | How does adding reset behavior to a datapath register change synthesized logic cost? | Teach reset tradeoffs in wide datapaths. |
| completed | `synthesis-if-else-priority-depth.yml` | Why can a long `if/else if` chain synthesize into deeper logic than expected? | Connect coding style to priority logic depth. |
| completed | `synthesis-case-style-parallel-selection.yml` | When does a well-structured case statement synthesize more cleanly than chained conditionals? | Compare parallel selection to priority decision logic. |
| completed | `synthesis-operator-sharing-mutually-exclusive-paths.yml` | When can mutually exclusive operations share hardware safely? | Teach synthesis-friendly sharing opportunities. |
| completed | `synthesis-bitwidth-trimming-benefit.yml` | Why does reducing unnecessary bit width improve area and often timing? | Reinforce width discipline in RTL authoring. |
| completed | `synthesis-comparator-decoder-logic-growth.yml` | Why do wide comparators and decoders grow expensive faster than many learners expect? | Build logic-cost intuition from common control and decode blocks. |
| completed | `synthesis-combinational-loop-is-not-a-feature.yml` | Why is a combinational loop a design bug rather than a clever optimization? | Clarify what synthesis can and cannot legalize. |
| completed | `synthesis-enable-check-vs-data-mux.yml` | What hardware difference appears between guarding an assignment with `if (en)` and explicitly muxing the datapath? | Teach equivalent intent and where implementations diverge. |
| completed | `synthesis-lint-vs-synthesis-vs-sta-boundaries.yml` | Which problem should be caught by lint, by synthesis review, or by STA? | Build practical flow literacy. |

## Migration And Cleanup Tasks

- planned: create `quizzes/rtl-design/`
- completed: create `quizzes/rtl-design/`
- completed: create `quizzes/synthesis/`
- planned: decide whether to keep `quizzes/verilog/` as an empty legacy directory or remove it later
- completed: move `quizzes/systemverilog/flop-reset-value.yml` into `quizzes/rtl-design/`
- planned: decide whether to keep `quizzes/systemverilog/` as a legacy directory or retire it after migration
- completed: update repo counts and progress notes in `AGENTS.md` after the first completed authoring wave

## Execution Notes

- Batch 1 was completed with 15 `rtl-design` coding and SystemVerilog-intent questions.
- Batch 2 was completed with 20 `rtl-design` design and microarchitecture questions, including Mermaid FSMs, Mermaid block diagrams, and WaveDrom timing sketches.
- Batch 3 was completed with 15 `synthesis` questions focused on practical RTL-to-gates reasoning.
- A temporary interface/modport question was dropped during execution to keep Batch 1 aligned with the planned 15-question count.
- `quizzes/systemverilog/` is now empty after the reset-value item was moved and should be revisited later as a taxonomy cleanup task.
- Batch 1 answer positions were later rebalanced after review because the initial authored set was too heavily skewed toward `a` as the correct choice.
- The wording for this wave was refined away from recruitment-oriented framing so the authored content stays useful for learners at many experience levels.
- Final answer-key distributions for the completed wave are balanced by batch: Batch 1 `4/4/4/3`, Batch 2 `5/5/5/5`, and Batch 3 `4/4/4/3` across `a/b/c/d`.

## QA Requirements

Each completed batch should include:

- metadata validation
- filename sanity check
- duplicate-topic check against existing lanes
- short-explainer quality pass
- long-explainer quality pass
- consistency pass on terminology, difficulty, and distractor quality
- answer-key distribution check to avoid obvious correct-choice patterns
- plan update in this file

## Update Rule

After any meaningful quiz-planning or quiz-authoring work in this repository:

1. update this file
2. mark completed items explicitly
3. adjust counts if scope changes
4. note any lane-name or taxonomy decision changes
5. record the next recommended batch
6. note any small refinements discovered during execution
