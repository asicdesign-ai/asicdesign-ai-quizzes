# Quiz QA Plan

## Status

- Structural validation: implemented
- Prose validation: implemented
- CI workflow: implemented
- Remaining: optional future tightening if the repo content conventions change

## Goal

Build a real quality gate for quiz YAML so the repo catches more than just
“does this file exist?” mistakes.

The gate should cover:

- YAML syntax and duplicate keys
- quiz schema and required fields
- content invariants like IDs, topic folders, and choice structure
- spelling and prose quality in learner-facing text
- CI enforcement on pull requests and main-branch updates

## Why this matters

The quiz bank is the source of truth for the portal. If the YAML is wrong,
the portal can still build bad content. A useful QA pass should catch:

- malformed YAML
- duplicate or missing quiz IDs
- title/file/topic mismatches
- invalid answer keys
- weak or broken prose in prompts and explanations
- spelling mistakes in learner-facing text

## QA layers

### 1. Structure validation

Use a Python validator to check:

- YAML parses successfully
- top-level keys are expected
- `human_verified` is present and boolean
- `schema_version` is correct
- `question_type` is supported
- `topics.primary` matches the parent folder
- multiple-choice items have a valid choice set
- reviewed items have a valid answer and learner-facing explanation text
- reference URLs are structurally valid

### 2. Prose validation

Use local, reproducible content linters for learner-facing text:

- `codespell` for spelling
- `proselint` for limited prose/grammar-style issues, with a small suppression
  layer for technical false positives

These are a practical compromise for this repo because they are easy to run
in CI and do not depend on a Java runtime or a rate-limited external API.

### 3. CI enforcement

GitHub Actions should run the full gate on every PR touching quiz content or
validator code.

The workflow should:

1. set up Python
2. install the QA dependencies
3. run structural validation
4. run prose validation

## Commands

- Structural check:
  - `bash scripts/validate-quiz-metadata.sh`
- Full gate:
  - `bash scripts/validate-quiz-bank.sh`

## Acceptance criteria

The QA system is considered useful when it reliably catches:

- malformed YAML
- duplicate top-level keys
- duplicate quiz IDs
- invalid multiple-choice answer keys
- files in the wrong topic folder
- obvious spelling errors in prompts, titles, and explanations
- repeated-word or similar prose mistakes in learner-facing text

## Follow-up ideas

- Add a generated markdown QA report artifact in CI.
- Expand the structural checks if new quiz types are introduced.
- Add a stricter custom dictionary for domain vocabulary if the prose linter
  starts flagging legitimate ASIC and VLSI terms.
