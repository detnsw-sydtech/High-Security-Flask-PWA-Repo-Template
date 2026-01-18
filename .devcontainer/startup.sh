#!/usr/bin/env bash
echo "STARTUP SCRIPT RAN" > /tmp/startup.log
set -e

# ------------------------------------------------------------
# STARTUP SCRIPT (runs every time the Codespace starts)
# ------------------------------------------------------------
# Purpose:
#   This script prepares the development environment each time
#   the Codespace starts. It ensures that:
#     1. The virtual environment exists
#     2. All dependencies are installed (uv sync)
#     3. Flask launches automatically in the background
#
# Why this matters:
#   Codespaces does NOT keep background processes running
#   between sessions. This script guarantees that the Flask
#   development server starts reliably every time.
# ------------------------------------------------------------

echo "[startup] Waiting for virtual environment (.venv) to be ready..."
while [ ! -d ".venv" ]; do
    sleep 1
done

echo "[startup] Activating virtual environment..."
source .venv/bin/activate

echo "[startup] Ensuring dependencies are installed (uv sync)..."
uv sync

echo "[startup] Launching Flask in the background..."
nohup flask run --host 0.0.0.0 --port 5000 >/tmp/flask.log 2>&1 &

echo "[startup] Flask started successfully."
