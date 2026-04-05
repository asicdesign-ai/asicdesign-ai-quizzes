# asicdesign-ai-quizzes

Editable YAML source-of-truth for quiz content used by the `asicdesign.ai`
portal.

## What lives here

This repository stores quiz items as authored YAML, grouped by learner-facing
topic. The portal builds normalized frontend data from this repo, but the quiz
content itself is edited here.

## Portal goals

- build toward a quiz and interview-question portal reviewed by real engineers
  who actively work in industry
- encourage practitioner engagement so quiz quality improves through human
  feedback and review
- treat `answer.short_explainer` and `answer.explanation` as core learner value,
  not optional filler
- evolve long explainers toward richer visual teaching aids such as WaveDrom
  waveforms, Mermaid FSMs, and similar diagrams

## Repository layout

- `quizzes/<topic>/` - one YAML file per quiz item
- `quizzes/templates/` - starter templates for new quiz authoring
- `scripts/validate-quiz-metadata.sh` - lightweight local metadata validation

Use `quizzes/templates/multiple-choice.template.yml` as the default starting
point for a new multiple-choice quiz.

## Authoring model

- keep one quiz per YAML file
- use stable `id` values and descriptive filenames
- write `answer.short_explainer` for immediate learner feedback
- make `answer.explanation` strong enough to teach the concept after answer
  resolution
- add `references` when the answer depends on research, tool behavior, or
  design methodology

## How content reaches the portal

This repo does not publish directly to `https://asicdesign.ai` on its own.

The normal flow is:

1. update reviewed quiz YAML in this repo
2. validate it locally
3. merge it here
4. let the portal repo regenerate its quiz artifacts and deploy

The portal-side generated outputs live in `asicdesign-ai-portal`, not here.

## Local validation

Run:

`bash scripts/validate-quiz-metadata.sh`

This checks required quiz metadata before you open a PR.

## Contributing

See `CONTRIBUTING.md` for the detailed contribution rules, review expectations,
field guidance, and license note.
