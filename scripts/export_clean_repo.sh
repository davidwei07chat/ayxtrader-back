#!/usr/bin/env bash
set -euo pipefail

SRC_ROOT="${1:-/TrendRadar}"
DEST_ROOT="${2:-/tmp/TrendRadar-newrepo}"

rm -rf "$DEST_ROOT"
mkdir -p "$DEST_ROOT"

rsync -a \
  --exclude '.git' \
  --exclude '.github/hooks' \
  --exclude '.agents' \
  --exclude '.claude' \
  --exclude '.codex' \
  --exclude 'output' \
  --exclude 'data' \
  --exclude 'venv' \
  --exclude '.env' \
  --exclude '.env.local' \
  --exclude '.env.*.local' \
  --exclude 'config/config.yaml' \
  --exclude 'config/profiles' \
  --exclude '__pycache__' \
  "$SRC_ROOT"/ "$DEST_ROOT"/

if [ -f "$DEST_ROOT/config/config.example.yaml" ]; then
  cp "$DEST_ROOT/config/config.example.yaml" "$DEST_ROOT/config/config.yaml"
fi

required_files=(
  "config/config.yaml"
  "config/frequency_words.txt"
  "config/timeline.yaml"
  "config/ai_analysis_prompt.txt"
  "config/ai_translation_prompt.txt"
  "docs/index.html"
  "docs/assets/script.js"
  "docs/assets/style.css"
  "docs/defaults/config.yaml"
  "docs/defaults/frequency_words.txt"
  "docs/defaults/timeline.yaml"
  "docs/defaults/ai_analysis_prompt.txt"
  "docs/defaults/ai_translation_prompt.txt"
  "docs/defaults/version_configs"
  ".env.example"
  "scripts/check_release_secrets.sh"
)

for file in "${required_files[@]}"; do
  if [ ! -f "$DEST_ROOT/$file" ]; then
    echo "Missing required migration file: $file" >&2
    exit 1
  fi
done

bash "$DEST_ROOT/scripts/check_release_secrets.sh" "$DEST_ROOT"

echo "Clean repo exported to: $DEST_ROOT"
