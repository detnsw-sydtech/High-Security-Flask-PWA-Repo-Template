#!/usr/bin/env bash
set -e

# ------------------------------------------------------------
# STARTUP SCRIPT (runs every time the Codespace starts)
# ------------------------------------------------------------
# This script:
#   - activates the virtual environment
#   - launches Flask in the background
#   - logs output to /tmp/flask.log
#
# Codespaces requires backgrounded processes for auto-start.
# ------------------------------------------------------------

echo "[startup] Activating virtual environment..."
source .venv/bin/activate

echo "[startup] Launching Flask in background..."
nohup flask run --host 0.0.0.0 --port 5000 >/tmp/flask.log 2>&1 &

echo "[startup] Flask started."
