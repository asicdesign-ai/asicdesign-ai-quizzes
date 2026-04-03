# AGENTS.md

## Project Identity

This repository is the source-of-truth for quiz content used by the `asicdesign.ai` ecosystem.

Quiz items in this repo are authored for human review first and machine ingestion second. The portal or other downstream systems can normalize this content into JSON or another delivery format, but the editable source lives here.

## Source Format

- Author quiz items in YAML.
- Store one quiz item per file.
- Keep quiz content under `quizzes/` grouped by topic or domain.
- Prefer stable, descriptive file names and stable `id` values.

## Required Quiz Pattern

All quiz YAML files should follow the same basic pattern:
- stable metadata fields
- explicit answer structure
- a short user-facing explanation
- a longer explanation when useful

For reviewed quiz items, `answer.short_explainer` is required.

This field is intended for direct rendering in the website UI after the user answers a question. It should be concise, readable, and useful without requiring the user to open a longer explanation panel.

## `answer.short_explainer` Rules

- Required for all quiz YAML files.
- Keep it short: usually 1 to 3 sentences.
- Write it for the learner, not for internal tooling.
- State why the correct answer is right.
- When useful, briefly contrast it with why the competing options are weaker.
- Avoid unnecessary jargon unless the quiz itself is advanced.

## `answer.explanation` Rules

- Keep `answer.explanation` available for a fuller explanation.
- It can be longer than `answer.short_explainer`.
- Use it for nuance, tradeoffs, design context, or implementation details.

## Draft Items

If a quiz item is still incomplete:
- set `review_state` accordingly, such as `needs_answer`
- set `answer.correct` to `null`
- set `answer.short_explainer` to `null`
- set `answer.explanation` to `null`

## Research-Backed Items

When an answer depends on platform practice, security reasoning, or implementation tradeoffs, prefer adding a `references` section with source links.

Use official documentation and primary sources whenever possible.

## Template

Use `quizzes/templates/multiple-choice.template.yml` as the default starting point for new multiple-choice items.

## Preferred Outcome

Over time, this repository should become a clean, automation-friendly quiz bank with a consistent authoring pattern that is easy to review, ingest, and render in `asicdesign-ai-portal`.

## Current Progress Snapshot

Updated: 2026-04-03

- The repository currently contains reviewed quiz content under `quizzes/cache-coherency`, `quizzes/firmware`, `quizzes/l2-cache-controller`, `quizzes/simulation`, `quizzes/systemverilog`, and `quizzes/vlsi`.
- Current reviewed counts by directory are:
  - `cache-coherency`: 30
  - `l2-cache-controller`: 10
  - `firmware`: 1
  - `simulation`: 1
  - `systemverilog`: 1
  - `vlsi`: 2
- `quizzes/cache-coherency/` now holds a larger research-backed set that covers protocol families, invariants, MSI/MESI/MOESI/MESIF concepts, invalidation and update behavior, snooping and directory basics, false sharing, inclusion, and LLC behavior.
- `quizzes/l2-cache-controller/` has been created and populated with research-backed reviewed items covering L2 hierarchy policy, unified versus split lower-level caches, banking, MSHRs, and write-back buffering behavior.
- The current trusted source set used in recent research-backed items includes:
  - Sorin, Hill, and Wood, *A Primer on Memory Consistency and Cache Coherence*
  - MIT 6.823 lecture and handout material
  - CMU 15-418 cache-coherence implementation material
  - University of Utah CS 6810 cache-coherence material
  - *The MESIF Cache Coherence Protocol for the Intel QuickPath Interconnect*
  - UPenn CIS 501 cache lectures
  - Wisconsin CS/ECE 752 cache lectures
  - Kroft, *Lockup-Free Instruction Fetch/Prefetch Cache Organization*
  - gem5 classic cache documentation as supporting systems documentation
- A GitHub Actions workflow now exists in this repo to trigger a portal rebuild when `quizzes/**` changes land on `main`.
- For new researched quizzes, keep preserving per-item `references` sections and avoid adding claims that are not supported by a trustworthy source.

## Still Missing / Open Gaps

- Coverage is still thin outside `cache-coherency` and `l2-cache-controller`; most other domains currently have only one or two reviewed items.
- `quizzes/verilog/` currently exists but has no quiz content. Future work should either populate it or remove the empty category if it is no longer needed.
- This repo still lacks its own dedicated schema-validation or content-lint workflow. Validation currently happens mainly through manual checks and the downstream portal ingestion/build pipeline.
- As the quiz bank grows, continue normalizing older and newer items so explanation quality, metadata consistency, and source citation depth stay aligned across directories.
