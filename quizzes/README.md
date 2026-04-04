# Quiz Content Layout

This folder stores structured quiz items that can be ingested by `asicdesign-ai-portal` or future content-processing scripts.

## Why YAML

YAML is a good authoring format here because it is:
- easy to read and edit by hand
- friendly to LLM and agent workflows
- easy to convert into JSON for frontend use
- flexible enough for draft items, reviewed items, and enriched metadata

## Automation Recommendation

Use YAML as the source-of-truth authoring format in this repo, then generate normalized JSON during portal build or ingestion.

That gives you:
- human-friendly editing in the content repo
- predictable machine-friendly output for the website
- room for draft items that are not fully reviewed yet

## Required Answer Pattern

All quiz YAML files should include:
- `human_verified`
- `answer.correct`
- `answer.short_explainer`
- `answer.explanation`

Use `answer.short_explainer` for the short learner-facing explanation shown immediately in the website UI after answer resolution.

Use `human_verified` as the manual trust flag that drives the portal badge:
- `true` means an admin or reviewer explicitly approved the item.
- `false` means the item is still awaiting that manual approval.

## Suggested Conventions

- One quiz item per file.
- Stable `id` per item.
- Store draft items even when the final answer is not confirmed yet.
- Keep prompt text and code snippets separate.
- Keep metadata easy to map into validation or build scripts later.
- Add `references` when an answer is backed by platform or vendor documentation.
- Start new multiple-choice quiz items from `templates/multiple-choice.template.yml`.
- Keep runtime feedback such as user progress, comments, and vote counts out of YAML.
