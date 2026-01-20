#!/usr/bin/env sh
set -euo pipefail

# =============================================================
# If uv is not installed yet, exit gracefully so the container can finish setup
# -------------------------------------------------------------
if ! command -v uv >/dev/null 2>&1; then
    echo "[startup] uv not installed yet — skipping startup tasks."
    exit 0
fi

# ============================================================
#  STARTUP SCRIPT (runs every time the Codespace starts)
# ------------------------------------------------------------
# Responsibilities:
#   1. Ensure a virtual environment exists (.venv)
#   2. Activate the environment safely
#   3. Run `uv sync` to install/update dependencies
#   4. Launch the Flask app in the background
#
# This script is intentionally idempotent:
#   - Safe to run on first boot
#   - Safe to run on subsequent boots
#   - Safe even if .venv is missing or stale
# ============================================================

echo "[startup] STARTUP SCRIPT RAN" > /tmp/startup.log

# ============================================================
#  SECTION 1 — Ensure virtual environment exists
# ------------------------------------------------------------
# We do NOT assume .venv already exists.
# On a fresh Codespace, it will not.
# `uv venv` is fast, safe, and reproducible.
# ============================================================

echo "[startup] Ensuring virtual environment exists..."
if [ ! -d ".venv" ]; then
    echo "[startup] Creating virtual environment with uv venv..."
    uv venv
fi


# ============================================================
#  SECTION 2 — Activate the virtual environment
# ------------------------------------------------------------
# This always succeeds because Section 1 guarantees .venv exists.
# ============================================================

echo "[startup] Activating virtual environment..."
source .venv/bin/activate


# ============================================================
#  SECTION 3 — Sync dependencies using uv
# ------------------------------------------------------------
# `uv sync` ensures:
#   - dependencies match uv.lock
#   - environment is fully reproducible
#   - no drift between Codespace boots
# ============================================================

echo "[startup] Running uv sync..."
uv sync


# ============================================================
#  SECTION 4 — Launch Flask in the background
# ------------------------------------------------------------
# nohup ensures Flask keeps running after the script exits.
# Output is logged to /tmp/flask.log for debugging.
# ============================================================

echo "[startup] Launching Flask in the background..."
nohup flask run --host 0.0.0.0 --port 5000 >/tmp/flask.log 2>&1 &

echo "[startup] Flask started successfully."
