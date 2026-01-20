#!/usr/bin/env bash
set -euo pipefail

# ============================================================
#  ENVIRONMENT DIAGNOSTICS (manual staff utility)
# ------------------------------------------------------------
# This script prints:
#   - Python version
#   - uv version
#   - venv Python version
#   - installed packages
#   - port forwarding info
#   - Flask status
#
# Useful for debugging student environments.
# ============================================================

echo "================ ENVIRONMENT DIAGNOSTICS ================"

echo "[diagnostics] System Python:"
python3 --version || echo "python3 not found"

echo
echo "[diagnostics] uv version:"
if command -v uv >/dev/null 2>&1; then
    uv --version
else
    echo "uv not installed"
fi

echo
echo "[diagnostics] Virtual environment:"
if [ -d ".venv" ]; then
    .venv/bin/python3 --version || echo "venv python missing"
else
    echo ".venv does not exist"
fi

echo
echo "[diagnostics] Installed packages (uv pip freeze):"
if [ -d ".venv" ]; then
    .venv/bin/uv pip freeze || echo "unable to list packages"
else
    echo "no venv, skipping package list"
fi

echo
echo "[diagnostics] Flask process status:"
pgrep -fl flask || echo "Flask not running"

echo
echo "[diagnostics] Port forwarding:"
ss -tulpn | grep 5000 || echo "Port 5000 not active"

echo "=========================================================="

