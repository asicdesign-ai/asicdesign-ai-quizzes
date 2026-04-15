#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import yaml


EXPECTED_SCHEMA_VERSION = 1
EXPECTED_QUESTION_TYPE = "multiple_choice"
ALLOWED_DIFFICULTIES = {"beginner", "intermediate", "advanced"}
TOP_LEVEL_KEYS = {
    "schema_version",
    "id",
    "status",
    "review_state",
    "human_verified",
    "question_type",
    "title",
    "prompt",
    "code",
    "topics",
    "difficulty",
    "source",
    "choices",
    "answer",
    "notes",
    "references",
    "automation",
}
REQUIRED_TOP_LEVEL_KEYS = TOP_LEVEL_KEYS - {"notes", "references", "code"}


class UniqueKeyLoader(yaml.SafeLoader):
    pass


def construct_mapping(loader: yaml.Loader, node: yaml.nodes.MappingNode, deep: bool = False) -> dict[str, Any]:
    mapping: dict[str, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                f"found duplicate key ({key!r})",
                key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(  # type: ignore[attr-defined]
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    construct_mapping,
)


@dataclass
class Issue:
    path: Path
    message: str


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.load(handle, Loader=UniqueKeyLoader)


def check(condition: bool, issues: list[Issue], path: Path, message: str) -> None:
    if not condition:
        issues.append(Issue(path=path, message=message))


def check_text_fields(
    issues: list[Issue],
    path: Path,
    field_name: str,
    value: Any,
    *,
    allow_none: bool = False,
) -> None:
    if value is None and allow_none:
        return
    check(isinstance(value, str), issues, path, f"{field_name} must be a string")
    if isinstance(value, str):
        check(value.strip() != "", issues, path, f"{field_name} must not be empty")


def check_choice_ids(issues: list[Issue], path: Path, choices: list[Any]) -> list[str]:
    expected = [chr(ord("a") + index) for index in range(len(choices))]
    actual: list[str] = []

    for index, choice in enumerate(choices):
        choice_path = f"choices[{index}]"
        check(isinstance(choice, dict), issues, path, f"{choice_path} must be a mapping")
        if not isinstance(choice, dict):
            continue
        choice_id = choice.get("id")
        choice_text = choice.get("text")
        check_text_fields(issues, path, f"{choice_path}.id", choice_id)
        check_text_fields(issues, path, f"{choice_path}.text", choice_text)
        if isinstance(choice_id, str):
            actual.append(choice_id)

    check(
        len(choices) in {4, 5},
        issues,
        path,
        "multiple_choice items must have 4 or 5 answer choices",
    )
    check(
        actual == expected,
        issues,
        path,
        f"choice IDs must be consecutive letters {expected!r}",
    )
    return actual


def check_references(issues: list[Issue], path: Path, references: Any) -> None:
    check(isinstance(references, list), issues, path, "references must be a list when present")
    if not isinstance(references, list):
        return

    for index, reference in enumerate(references):
        ref_path = f"references[{index}]"
        check(isinstance(reference, dict), issues, path, f"{ref_path} must be a mapping")
        if not isinstance(reference, dict):
            continue
        check_text_fields(issues, path, f"{ref_path}.title", reference.get("title"))
        check_text_fields(issues, path, f"{ref_path}.url", reference.get("url"))
        note = reference.get("note")
        if note is not None:
            check_text_fields(issues, path, f"{ref_path}.note", note)
        url = reference.get("url")
        if isinstance(url, str):
            parsed = urlparse(url)
            check(
                parsed.scheme in {"http", "https"} and bool(parsed.netloc),
                issues,
                path,
                f"{ref_path}.url must be a valid http(s) URL",
            )


def validate_file(path: Path) -> list[Issue]:
    issues: list[Issue] = []

    try:
        data = load_yaml(path)
    except yaml.YAMLError as exc:
        return [Issue(path=path, message=f"YAML parse error: {exc}")]

    check(isinstance(data, dict), issues, path, "top-level YAML document must be a mapping")
    if not isinstance(data, dict):
        return issues

    extra_keys = sorted(set(data) - TOP_LEVEL_KEYS)
    check(not extra_keys, issues, path, f"unexpected top-level keys: {extra_keys}")
    missing_keys = sorted(REQUIRED_TOP_LEVEL_KEYS - set(data))
    check(not missing_keys, issues, path, f"missing required top-level keys: {missing_keys}")

    check_text_fields(issues, path, "id", data.get("id"))
    check_text_fields(issues, path, "title", data.get("title"))
    check_text_fields(issues, path, "prompt", data.get("prompt"))
    check(data.get("schema_version") == EXPECTED_SCHEMA_VERSION, issues, path, "schema_version must be 1")
    check(
        data.get("question_type") == EXPECTED_QUESTION_TYPE,
        issues,
        path,
        f"question_type must be {EXPECTED_QUESTION_TYPE!r}",
    )
    check(isinstance(data.get("human_verified"), bool), issues, path, "human_verified must be boolean")
    check(isinstance(data.get("status"), str) and data["status"].strip(), issues, path, "status must be a non-empty string")
    check(
        isinstance(data.get("review_state"), str) and data["review_state"].strip(),
        issues,
        path,
        "review_state must be a non-empty string",
    )
    check(
        data.get("difficulty") in ALLOWED_DIFFICULTIES,
        issues,
        path,
        f"difficulty must be one of {sorted(ALLOWED_DIFFICULTIES)}",
    )

    code = data.get("code")
    if code is not None:
        check(isinstance(code, dict), issues, path, "code must be a mapping when present")
        if isinstance(code, dict):
            check("language" in code, issues, path, "code.language is required")
            check("snippet" in code, issues, path, "code.snippet is required")
            if "language" in code and code["language"] is not None:
                check_text_fields(issues, path, "code.language", code["language"])
            if "snippet" in code and code["snippet"] is not None:
                check_text_fields(issues, path, "code.snippet", code["snippet"], allow_none=False)

    topics = data.get("topics")
    check(isinstance(topics, dict), issues, path, "topics must be a mapping")
    if isinstance(topics, dict):
        primary = topics.get("primary")
        check_text_fields(issues, path, "topics.primary", primary)
        if isinstance(primary, str):
            check(
                path.parent.name == primary,
                issues,
                path,
                f"topics.primary must match the parent folder name ({path.parent.name!r})",
            )
        secondary = topics.get("secondary")
        if secondary is not None:
            check(isinstance(secondary, list), issues, path, "topics.secondary must be a list when present")
            if isinstance(secondary, list):
                seen = Counter()
                for index, item in enumerate(secondary):
                    check_text_fields(issues, path, f"topics.secondary[{index}]", item)
                    if isinstance(item, str):
                        seen[item] += 1
                duplicates = sorted([item for item, count in seen.items() if count > 1])
                check(not duplicates, issues, path, f"topics.secondary contains duplicates: {duplicates}")

    source = data.get("source")
    check(isinstance(source, dict), issues, path, "source must be a mapping")
    if isinstance(source, dict):
        check_text_fields(issues, path, "source.platform", source.get("platform"))
        check_text_fields(issues, path, "source.import_kind", source.get("import_kind"))

    choices = data.get("choices")
    check(isinstance(choices, list), issues, path, "choices must be a list")
    actual_choice_ids: list[str] = []
    if isinstance(choices, list):
        actual_choice_ids = check_choice_ids(issues, path, choices)
        if actual_choice_ids:
            choice_texts = [choice.get("text") for choice in choices if isinstance(choice, dict)]
            seen_texts = Counter(choice_texts)
            duplicates = sorted(
                [text for text, count in seen_texts.items() if isinstance(text, str) and count > 1]
            )
            check(not duplicates, issues, path, f"choices contain duplicate texts: {duplicates}")

    answer = data.get("answer")
    check(isinstance(answer, dict), issues, path, "answer must be a mapping")
    if isinstance(answer, dict):
        correct = answer.get("correct")
        short_explainer = answer.get("short_explainer")
        explanation = answer.get("explanation")
        reviewed = data.get("status") == "reviewed"
        if reviewed:
            check_text_fields(issues, path, "answer.correct", correct)
            if isinstance(correct, str) and actual_choice_ids:
                check(
                    correct in actual_choice_ids,
                    issues,
                    path,
                    f"answer.correct must be one of {actual_choice_ids!r}",
                )
            check_text_fields(issues, path, "answer.short_explainer", short_explainer)
            check_text_fields(issues, path, "answer.explanation", explanation)
        else:
            if correct is not None:
                check_text_fields(issues, path, "answer.correct", correct)
            if short_explainer is not None:
                check_text_fields(issues, path, "answer.short_explainer", short_explainer)
            if explanation is not None:
                check_text_fields(issues, path, "answer.explanation", explanation)

    notes = data.get("notes")
    if notes is not None:
        check(isinstance(notes, list), issues, path, "notes must be a list when present")
        if isinstance(notes, list):
            for index, note in enumerate(notes):
                check_text_fields(issues, path, f"notes[{index}]", note)

    references = data.get("references")
    if references is not None:
        check_references(issues, path, references)

    automation = data.get("automation")
    check(isinstance(automation, dict), issues, path, "automation must be a mapping")
    if isinstance(automation, dict):
        ready = automation.get("ready_for_ingestion")
        review_required = automation.get("review_required")
        check(isinstance(ready, bool), issues, path, "automation.ready_for_ingestion must be boolean")
        check(isinstance(review_required, bool), issues, path, "automation.review_required must be boolean")
        if data.get("status") == "reviewed":
            check(ready is True, issues, path, "reviewed items must be ready_for_ingestion: true")
            check(review_required is False, issues, path, "reviewed items must have review_required: false")

    if data.get("status") == "reviewed":
        check(data.get("review_state") == "answered", issues, path, "reviewed items must have review_state: answered")

    return issues


def collect_quiz_files(repo_root: Path) -> list[Path]:
    files = []
    for suffix in ("*.yml", "*.yaml"):
        files.extend(
            path
            for path in repo_root.glob(f"quizzes/*/{suffix}")
            if "templates" not in path.parts
        )
    return sorted(files)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate quiz YAML structure and invariants.")
    parser.add_argument("--repo-root", default=Path(__file__).resolve().parents[1], type=Path)
    args = parser.parse_args()

    files = collect_quiz_files(args.repo_root)
    if not files:
        print("ERROR: no quiz files found", file=sys.stderr)
        return 1

    all_issues: list[Issue] = []
    seen_ids: dict[str, Path] = {}

    for path in files:
        issues = validate_file(path)
        all_issues.extend(issues)
        try:
            data = load_yaml(path)
        except Exception:
            continue
        if isinstance(data, dict):
            quiz_id = data.get("id")
            if isinstance(quiz_id, str) and quiz_id.strip():
                if quiz_id in seen_ids and seen_ids[quiz_id] != path:
                    all_issues.append(
                        Issue(path=path, message=f"duplicate quiz id {quiz_id!r} also used in {seen_ids[quiz_id]}")
                    )
                else:
                    seen_ids[quiz_id] = path

    if all_issues:
        for issue in all_issues:
            print(f"ERROR: {issue.path}: {issue.message}", file=sys.stderr)
        print(f"Checked {len(files)} quiz files; found {len(all_issues)} structure issues.", file=sys.stderr)
        return 1

    print(f"Checked {len(files)} quiz files; structure validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
