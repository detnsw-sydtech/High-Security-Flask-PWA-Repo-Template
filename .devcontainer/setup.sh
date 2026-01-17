#!/usr/bin/env bash
set -e

# ------------------------------------------------------------
# SETUP SCRIPT (runs once when the Codespace is created)
# ------------------------------------------------------------
# This script installs:
#   - uv (fast Python package manager)
#   - your project virtual environment
#   - all dependencies from pyproject.toml
#   - developer tools (pre-commit, nox)
#
# Students never need to run pip install manually.
# ------------------------------------------------------------

echo "[setup] Installing uv..."
curl -LsSf https://astral.sh/uv/install.sh | sh

echo "[setup] Creating virtual environment..."
uv venv .venv

echo "[setup] Installing project dependencies..."
uv sync

echo "[setup] Installing developer tools..."
source .venv/bin/activate
pip install pre-commit nox
pre-commit install

echo "[setup] Setup complete."
