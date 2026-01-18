#!/usr/bin/env bash
echo "STARTUP SCRIPT RAN" > /tmp/startup.log
set -e

# ------------------------------------------------------------
# STARTUP SCRIPT (runs every time the Codespace starts)
# ------------------------------------------------------------
# This script ensures that:
#   1. The virtual environment exists
#   2. Dependencies are fully installed (uv sync)
#   3. Flask launches only AFTER the environment is stable
# ------------------------------------------------------------

echo "[startup] Waiting for virtual environment (.venv) to be ready..."
for i in $(seq 1 30); do
    if [ -d ".venv" ]; then
        break
    fi
    sleep 1
done

echo "[startup] Activating virtual environment..."
source .venv/bin/activate

echo "[startup] Running uv sync (this may update uv.lock)..."
uv sync

echo "[startup] Launching Flask in the background..."
nohup flask run --host 0.0.0.0 --port 5000 >/tmp/flask.log 2>&1 &

echo "[startup] Flask started successfully."
