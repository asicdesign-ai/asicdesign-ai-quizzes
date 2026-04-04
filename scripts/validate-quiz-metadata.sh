#!/usr/bin/env bash

set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

mapfile -d '' quiz_files < <(
  find quizzes -mindepth 2 -maxdepth 2 -type f \( -name '*.yml' -o -name '*.yaml' \) \
    ! -path 'quizzes/templates/*' -print0 | sort -z
)

if [[ ${#quiz_files[@]} -eq 0 ]]; then
  echo "ERROR no quiz YAML files were found" >&2
  exit 1
fi

validation_failed=0

for file_path in "${quiz_files[@]}"; do
  match_count="$(rg -c '^human_verified: (true|false)$' "$file_path" || true)"
  if [[ "$match_count" != "1" ]]; then
    echo "ERROR ${file_path} must contain exactly one top-level 'human_verified: true|false' field" >&2
    validation_failed=1
  fi
done

if [[ "$validation_failed" != "0" ]]; then
  exit 1
fi

echo "Validated ${#quiz_files[@]} quiz YAML files with human_verified metadata."
