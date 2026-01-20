#!/usr/bin/env sh
set -euo pipefail

# ============================================================
#  INSTALL UV (manual staff utility)
# ------------------------------------------------------------
# This script reinstalls uv using the official installer.
# It is safe to run multiple times.
# Students should not need this during normal operation.
# ============================================================

echo "[install-uv] Checking for existing uv installation..."
if command -v uv >/dev/null 2>&1; then
    echo "[install-uv] uv is already installed ($(uv --version))"
else
    echo "[install-uv] uv not found. Installing..."
fi

# Official installer (safe, idempotent)
curl -LsSf https://astral.sh/uv/install.sh | sh

echo "[install-uv] uv installation complete."

