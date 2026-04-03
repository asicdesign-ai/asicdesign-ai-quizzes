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