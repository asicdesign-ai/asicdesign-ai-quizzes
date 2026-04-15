# Contributing to asicdesign-ai-quizzes

Thanks for helping improve the quiz source data behind `asicdesign.ai`.

This repository is the editable YAML source-of-truth for quiz content. The
portal consumes generated data from this repo, but quiz authoring and review
belong here.

## Product direction

Please keep the portal's top goals in mind when contributing:

- move the quiz bank toward real engineer-reviewed knowledge from practicing
  industry contributors
- encourage content that invites correction, clarification, and deeper review by
  experienced engineers
- prioritize the quality of the short and long explainers shown after answer
  resolution
- write long-form explanations so they can later support diagrams such as
  WaveDrom waveforms, Mermaid FSMs, and other teaching visuals

## Start from the template

Use `quizzes/templates/multiple-choice.template.yml` as the default starting
point for a new quiz.

Author one quiz per YAML file and place it in the most specific learner-facing
topic folder under `quizzes/`.

## Required authoring model

Every quiz file should:

- be valid YAML
- contain one clear prompt
- contain one set of answer choices
- preserve stable metadata fields
- include learner-facing explanation text

For reviewed items, `answer.short_explainer` is required and should be ready to
show directly in the portal feedback UI.

## Field guide

`status`

- Use this for the content lifecycle, for example whether the item is still a
  draft or ready to be treated as published content.

`review_state`

- Use this for the current review condition of the quiz, such as whether the
  answer is still missing or the item still needs review work.

`human_verified`

- This must be a top-level boolean on every quiz file.
- Set it to `true` only when a human reviewer has manually approved the item
  for the portal's human-verification badge.

`answer.short_explainer`

- This is the short learner-facing explanation shown right after answer
  resolution in the portal.
- Keep it concise, clear, and useful on its own.
- Treat it as a high-priority teaching surface, not a checkbox field.

`answer.explanation`

- Use this for the deeper explanation shown after the short explainer.
- Prefer teaching-oriented explanation over minimal answer justification.
- When the topic would benefit from visuals, write it so future portal diagram
  support can attach cleanly to the concept.

`references`

- Use this to store source links when the answer depends on research, tool
  behavior, methodology, standards, or implementation tradeoffs.

`automation.ready_for_ingestion`

- Use this to signal whether the quiz is ready for downstream ingestion into
  generated portal artifacts.

## Minimum bar for a contribution

Before opening a PR, make sure the quiz has:

- valid YAML
- required metadata fields present
- a clear prompt and answer choices
- the correct answer set when the item is reviewed
- a short learner-facing explainer in `answer.short_explainer`

## Source quality guidance

Please keep source quality high.

- Prefer official documentation and other primary sources when practical.
- For broad ASIC or VLSI methodology, prefer standards, textbooks, university
  material, and widely used technical references.
- Do not base a broad methodology quiz mainly on a single patent, vendor app
  note, product page, or tool-specific white paper.
- Vendor-specific or tool-specific sources are fine when the quiz is clearly
  about that vendor, tool, primitive, or feature.
- When you use a secondary source for a broad concept, add a second
  corroborating source when practical.

## Local validation

Install the prose QA dependencies if you want the full gate:

`python3 -m pip install -r requirements-quiz-qa.txt`

Run the structure check before you open a PR:

`bash scripts/validate-quiz-metadata.sh`

Run the full QA gate when you want spelling and prose checks too:

`bash scripts/validate-quiz-bank.sh`

The structure check now validates quiz schema, ID/folder alignment, answer
choice structure, and required answer metadata. The full gate adds spelling
and prose checks for learner-facing text.

## Pull request expectations

Please include:

- what topic or lane you changed
- whether the item is new, expanded, or corrected
- what sources support the answer, if references were added or updated
- the validation command you ran and whether it passed

If the change should appear on the website right away, note that the portal
still needs its build or dispatch hop to regenerate public quiz artifacts.

## License note

Quiz content in this repository is licensed under CC BY 4.0. Preserve
attribution when reusing or adapting this material, and do not remove upstream
credit when copying quiz content into another surface.
