#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any
from urllib.parse import urlparse
import re

import yaml


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


def collect_quiz_files(repo_root: Path) -> list[Path]:
    files: list[Path] = []
    for suffix in ("*.yml", "*.yaml"):
        files.extend(
            path
            for path in repo_root.glob(f"quizzes/*/{suffix}")
            if "templates" not in path.parts
        )
    return sorted(files)


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.load(handle, Loader=UniqueKeyLoader)


def resolve_tool(name: str) -> str:
    venv_candidate = Path(sys.executable).with_name(name)
    if venv_candidate.exists():
        return str(venv_candidate)
    from shutil import which

    resolved = which(name)
    if resolved:
        return resolved
    raise RuntimeError(
        f"{name} is not installed. Run: python3 -m pip install -r requirements-quiz-qa.txt"
    )


def extract_prose(doc: dict[str, Any]) -> str:
    parts: list[str] = []
    for label in ("title", "prompt"):
        value = doc.get(label)
        if isinstance(value, str) and value.strip():
            parts.append(f"{label.upper()}\n{value.strip()}\n")

    choices = doc.get("choices")
    if isinstance(choices, list):
        for choice in choices:
            if not isinstance(choice, dict):
                continue
            choice_id = choice.get("id", "?")
            text = choice.get("text")
            if isinstance(text, str) and text.strip():
                parts.append(f"CHOICE {choice_id}\n{text.strip()}\n")

    answer = doc.get("answer")
    if isinstance(answer, dict):
        for label in ("short_explainer", "explanation"):
            value = answer.get(label)
            if isinstance(value, str) and value.strip():
                parts.append(f"ANSWER {label}\n{value.strip()}\n")

    notes = doc.get("notes")
    if isinstance(notes, list):
        for index, note in enumerate(notes):
            if isinstance(note, str) and note.strip():
                parts.append(f"NOTE {index + 1}\n{note.strip()}\n")

    return "\n".join(parts).strip() + "\n"


def build_prose_corpus(repo_root: Path, tempdir: Path) -> list[Path]:
    generated: list[Path] = []
    for quiz_file in collect_quiz_files(repo_root):
        doc = load_yaml(quiz_file)
        if not isinstance(doc, dict):
            continue
        prose = extract_prose(doc)
        out_path = tempdir / quiz_file.relative_to(repo_root)
        out_path = out_path.with_suffix(".md")
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(f"# {quiz_file}\n\n{prose}", encoding="utf-8")
        generated.append(out_path)
    return generated


def run_command(cmd: list[str], label: str) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run(cmd, text=True, capture_output=True)
    return proc


IGNORED_PROSELINT_RULES = {
    "misc.greylist",
    "misc.phrasal_adjectives.ly",
    "redundancy.misc.after_the_deadline",
    "spelling.er_or",
    "typography.diacritical_marks",
    "typography.symbols.curly_quotes",
    "typography.symbols.ellipsis",
    "typography.symbols.multiplication",
    "weasel_words.very",
}


def should_ignore_lexical_illusion(snippet: str) -> bool:
    tokens = [token for token in re.findall(r"[A-Za-z0-9']+", snippet) if token]
    if not tokens:
        return True
    if any(token in {"TITLE", "CHOICE", "ANSWER", "NOTE"} for token in tokens):
        return True
    if any(token.isupper() for token in tokens):
        return True
    if any(len(token) <= 1 for token in tokens):
        return True
    return False


def filter_proselint_output(raw_output: str) -> list[str]:
    if not raw_output.strip():
        return []

    try:
        payload = json.loads(raw_output)
    except json.JSONDecodeError:
        return [raw_output.strip()]

    diagnostics: list[str] = []
    result = payload.get("result", {})
    for file_uri, info in result.items():
        parsed = urlparse(file_uri)
        file_path = Path(parsed.path)
        try:
            text = file_path.read_text(encoding="utf-8")
        except OSError:
            text = ""
        for diag in info.get("diagnostics", []):
            rule = diag.get("check_path", "")
            message = diag.get("message", "")
            line, col = diag.get("pos", [0, 0])
            span = diag.get("span", [0, 0])
            snippet = text[span[0] : span[1]] if len(span) == 2 else ""
            if rule in IGNORED_PROSELINT_RULES:
                continue
            if rule == "lexical_illusions" and should_ignore_lexical_illusion(snippet):
                continue
            diagnostics.append(f"{file_path}:{line}:{col}: {rule}: {message}")
    return diagnostics


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate quiz prose with codespell and proselint.")
    parser.add_argument("--repo-root", default=Path(__file__).resolve().parents[1], type=Path)
    parser.add_argument(
        "--ignore-words-file",
        default=Path(__file__).resolve().parent / "quiz-prose-ignore-words.txt",
        type=Path,
    )
    args = parser.parse_args()

    repo_root = args.repo_root
    files = collect_quiz_files(repo_root)
    if not files:
        print("ERROR: no quiz files found", file=sys.stderr)
        return 1

    ignore_words = ""
    if args.ignore_words_file.exists():
        ignore_words = ",".join(
            word.strip()
            for word in args.ignore_words_file.read_text(encoding="utf-8").splitlines()
            if word.strip() and not word.lstrip().startswith("#")
        )

    with tempfile.TemporaryDirectory(prefix="quiz-prose-qa-") as tmp:
        tempdir = Path(tmp)
        build_prose_corpus(repo_root, tempdir)

        codespell_cmd = [resolve_tool("codespell"), str(tempdir), "--quiet-level=2"]
        if ignore_words:
            codespell_cmd.extend(["-L", ignore_words])
        proselint_cmd = [resolve_tool("proselint"), "check", "--output-format", "json", str(tempdir)]

        failures = 0
        codespell_proc = run_command(codespell_cmd, "codespell")
        if codespell_proc.returncode != 0:
            if codespell_proc.stdout.strip():
                sys.stdout.write(codespell_proc.stdout)
            if codespell_proc.stderr.strip():
                sys.stdout.write(codespell_proc.stderr)
            sys.stderr.write("\nERROR: codespell failed.\n")
            failures += 1

        proselint_proc = run_command(proselint_cmd, "proselint")
        proselint_issues = filter_proselint_output(proselint_proc.stdout)
        if proselint_issues:
            for issue in proselint_issues:
                print(issue)
            sys.stderr.write("\nERROR: proselint found issues.\n")
            failures += 1

    if failures:
        print(f"\nChecked {len(files)} quiz files; prose validation found issues.", file=sys.stderr)
        return 1

    print(f"Checked {len(files)} quiz files; prose validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
