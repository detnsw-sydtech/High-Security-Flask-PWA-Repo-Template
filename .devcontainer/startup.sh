#!/usr/bin/env bash
set -euo pipefail

# ============================================================
#  STARTUP SCRIPT (runs every time the Codespace starts)
# ------------------------------------------------------------
# Responsibilities:
#   1. Ensure uv is available
#   2. Ensure a virtual environment exists (.venv)
#   3. Activate the environment safely
#   4. Run `uv sync` to confirm dependencies
#   5. Launch the Flask app in the background
#
# This script is intentionally idempotent:
#   - Safe to run on subsequent boots
#   - Fails loudly if environment is not initialized
# ============================================================

# If uv is not installed yet, exit gracefully so the container can finish setup
if ! command -v uv >/dev/null 2>&1; then
    echo "[startup] uv not installed yet — skipping startup tasks."
    echo "[startup] Run: bash .devcontainer/scripts/install-uv.sh"
    exit 0
fi

echo "[startup] STARTUP SCRIPT RAN" > /tmp/startup.log

# ---------------------------------------------------------
# 1 — Ensure virtual environment exists
# ---------------------------------------------------------
if [ ! -d ".venv" ]; then
    echo "[startup] ERROR: .venv missing — environment not initialized."
    echo "[startup] Run: bash .devcontainer/scripts/rebuild-venv.sh"
    exit 1
fi

# ---------------------------------------------------------
# 2 — Activate the virtual environment
# ---------------------------------------------------------
echo "[startup] Activating virtual environment..."
# shellcheck disable=SC1091
source .venv/bin/activate

# ---------------------------------------------------------
# 3 — Sync dependencies using uv
# ---------------------------------------------------------
echo "[startup] Running uv sync..."
uv sync

# ---------------------------------------------------------
# 4 — Launch Flask in the background
# ---------------------------------------------------------
echo "[startup] Launching Flask in the background..."
nohup flask run --host 0.0.0.0 --port 5000 >/tmp/flask.log 2>&1 &

echo "[startup] Flask started successfully."
echo "[startup] Open in browser on port 5000."
