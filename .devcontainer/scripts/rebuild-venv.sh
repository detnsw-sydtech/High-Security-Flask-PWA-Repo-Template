#!/usr/bin/env bash
set -euo pipefail

# ============================================================
#  REBUILD VIRTUAL ENVIRONMENT (manual staff utility)
# ------------------------------------------------------------
# This script:
#   1. Deletes the existing .venv
#   2. Creates a fresh uv virtual environment
#   3. Runs uv sync to reinstall dependencies
#
# Use this if:
#   - dependencies are corrupted
#   - Python version drift is detected
#   - uv.lock has changed significantly
# ============================================================

echo "[rebuild-venv] Checking for uv..."
if ! command -v uv >/dev/null 2>&1; then
    echo "[rebuild-venv] ERROR: uv is not installed or not on PATH."
    echo "[rebuild-venv] Run: bash .devcontainer/scripts/install-uv.sh"
    exit 1
fi

echo "[rebuild-venv] Removing existing virtual environment..."
rm -rf .venv

echo "[rebuild-venv] Creating new virtual environment with uv venv..."
uv venv

echo "[rebuild-venv] Activating new virtual environment..."
# shellcheck disable=SC1091
source .venv/bin/activate

echo "[rebuild-venv] Running uv sync..."
uv sync

echo "[rebuild-venv] Virtual environment rebuilt successfully."
