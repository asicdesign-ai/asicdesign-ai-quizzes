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

## Topic Taxonomy

- Do not use `quizzes/vlsi/` as a generic catch-all topic anymore.
- New quizzes should go into dedicated lanes such as `cdc`, `sta`, `clock-gating`, `simulation`, `systemverilog`, `cache-coherency`, `l2-cache-controller`, or another specific domain.
- If a question spans multiple areas, choose the best learner-facing primary lane and use `topics.secondary` to capture the cross-domain tags.

## Portal Publish Hop

Quiz content does not become visible on `https://asicdesign.ai` from this repo alone. There is a second hop through the portal repository that must succeed.

- The intended flow is:
  - push reviewed quiz YAML changes in this repo to `main`
  - let this repo's workflow `.github/workflows/trigger-portal-deploy.yaml` send a `repository_dispatch` event to `asicdesign-ai-portal`
  - let the portal repo regenerate `assets/data/quizzes/**` and `quiz/topics/**`, then deploy the site
- The dispatch step depends on the `PORTAL_REPO_DISPATCH_TOKEN` secret being configured in this repo.
- If that secret is missing, the workflow exits successfully but skips the portal notification. In that case, the quiz bank updates here, but the website keeps serving stale quiz JSON.
- Manual fallback when the portal did not refresh:
  - go to `/home/arik/projects/asicdesign-ai-portal`
  - run `npm run build:quiz`
  - run `npm test`
  - commit only the regenerated quiz artifacts, typically under `assets/data/quizzes/**` and the affected `quiz/topics/**` pages
  - push `main` in the portal repo
- Verify the public site using `https://asicdesign.ai/assets/data/quizzes/manifest.json`
- When verifying, compare `generated_at`, `total_reviewed`, and the relevant collection counts against the local source repo counts.
- Be careful not to commit unrelated dirty files in the portal repo during a manual refresh. In local work, `AGENTS.md` there may already be modified and should usually be left untouched.

## Current Progress Snapshot

Updated: 2026-04-04

- The repository currently contains reviewed quiz content under `quizzes/cache-coherency`, `quizzes/cdc`, `quizzes/clock-gating`, `quizzes/firmware`, `quizzes/l2-cache-controller`, `quizzes/simulation`, `quizzes/sta`, and `quizzes/systemverilog`.
- Current reviewed counts by directory are:
  - `cache-coherency`: 30
  - `cdc`: 21
  - `clock-gating`: 5
  - `l2-cache-controller`: 10
  - `firmware`: 1
  - `simulation`: 16
  - `sta`: 21
  - `systemverilog`: 1
- `quizzes/cache-coherency/` now holds a larger research-backed set that covers protocol families, invariants, MSI/MESI/MOESI/MESIF concepts, invalidation and update behavior, snooping and directory basics, false sharing, inclusion, and LLC behavior.
- `quizzes/cdc/` now holds a reviewed, ASIC-oriented set focused on metastability, synchronizers, handshake choices, async FIFOs, reconvergence, reset crossings, and MTBF tradeoffs.
- `quizzes/l2-cache-controller/` has been created and populated with research-backed reviewed items covering L2 hierarchy policy, unified versus split lower-level caches, banking, MSHRs, and write-back buffering behavior.
- `quizzes/sta/` now holds a reviewed STA set covering slack, path classes, PVT corners, skew, multicycle versus false-path intent, WNS/TNS, I/O constraints, and common hold-fix practice.
- `quizzes/simulation/` now holds a reviewed simulation set covering preprocessing, elaboration, min/typ/max delays, blocking versus nonblocking assignments, event regions, assertion scheduling, RTL-vs-gate mismatches, and timing-simulation limits.
- The old generic `vlsi` quiz lane has been retired; its remaining reviewed items were folded into dedicated domain lanes.
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
- Recent quiz-bank expansions also rely on source sets from VerilogPro, AnySilicon, OpenLane, Verilator, Icarus Verilog, Cliff Cummings papers, and university timing/metastability lecture material.
- A GitHub Actions workflow now exists in this repo to trigger a portal rebuild when `quizzes/**` changes land on `main`, but that hop depends on the dispatch token described above.
- For new researched quizzes, keep preserving per-item `references` sections and avoid adding claims that are not supported by a trustworthy source.

## Still Missing / Open Gaps

- Coverage is still thinner in `firmware` and `systemverilog` than in the larger banks such as `cache-coherency`, `cdc`, `sta`, and `simulation`.
- `quizzes/verilog/` currently exists but has no quiz content. Future work should either populate it or remove the empty category if it is no longer needed.
- This repo still lacks its own dedicated schema-validation or content-lint workflow. Validation currently happens mainly through manual checks and the downstream portal ingestion/build pipeline.
- As the quiz bank grows, continue normalizing older and newer items so explanation quality, metadata consistency, and source citation depth stay aligned across directories.
