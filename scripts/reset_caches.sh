#!/usr/bin/env bash
set -euo pipefail

echo "=== Resetting repository caches and build artefacts ==="

echo "Removing Python virtual environments..."
rm -rf .venv || true

echo "Clearing uv cache..."
uv cache clean || true

echo "Removing Python bytecode..."
find . -type d -name "__pycache__" -exec rm -rf {} + || true

echo "Removing framework build artefacts..."
rm -rf dist/ build/ .next/ vite/.cache || true
rm -rf .jinja2_cache || true

echo "Removing generated static assets..."
rm -rf static/generated/* || true

echo "Cleaning ignored files via git..."
git clean -fdX || true

echo "Reinstalling dependencies from lockfile..."
uv sync --frozen --directory .venv

echo "Validating dependency integrity..."
uv pip check

echo "Reset complete."
