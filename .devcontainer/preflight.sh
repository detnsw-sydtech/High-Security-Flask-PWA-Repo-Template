#!/usr/bin/env bash
set -euo pipefail

REQUIRED="3.12"
CURRENT="$(python3 --version 2>/dev/null | awk '{print $2}' | cut -d. -f1-2)"

if [ "$CURRENT" != "$REQUIRED" ]; then
  echo "❌ ERROR: This Codespace is running Python $CURRENT but the project requires Python $REQUIRED."
  echo "Please rebuild the container or update your devcontainer.json."
  exit 1
fi

echo "✅ Python version OK ($CURRENT)"
