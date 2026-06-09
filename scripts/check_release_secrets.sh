#!/usr/bin/env bash
set -euo pipefail

TARGET_ROOT="${1:-.}"

if [ ! -d "$TARGET_ROOT" ]; then
  echo "Secret scan target does not exist: $TARGET_ROOT" >&2
  exit 1
fi

for forbidden in \
  ".env" \
  ".env.local" \
  "config/profiles" \
  "output" \
  "data"
do
  if [ -e "$TARGET_ROOT/$forbidden" ]; then
    echo "Forbidden release path exists: $forbidden" >&2
    exit 1
  fi
done

scan_paths=(
  "$TARGET_ROOT/config"
  "$TARGET_ROOT/docs/defaults"
  "$TARGET_ROOT/README.md"
  "$TARGET_ROOT/README-EN.md"
  "$TARGET_ROOT/DEPLOYMENT.md"
  "$TARGET_ROOT/docker-compose.yml"
  "$TARGET_ROOT/docker"
)

patterns=(
  'sk-[A-Za-z0-9]{20,}'
  'gho_[A-Za-z0-9_]{20,}'
  'xox[baprs]-[A-Za-z0-9-]{20,}'
  'AIza[0-9A-Za-z_-]{20,}'
  'hooks\.slack\.com/services/[A-Za-z0-9/_-]+'
)

for pattern in "${patterns[@]}"; do
  if rg -n --hidden --glob '!.git' "$pattern" "${scan_paths[@]}" >/tmp/trendradar-secret-scan.txt; then
    cat /tmp/trendradar-secret-scan.txt >&2
    echo "Potential secret matched pattern: $pattern" >&2
    exit 1
  fi
done

echo "Release secret scan OK: $TARGET_ROOT"
