#!/usr/bin/env bash
set -euo pipefail

# ============================================================
#  ENVIRONMENT DIAGNOSTICS (manual staff utility)
# ------------------------------------------------------------
# This script prints:
#   - System Python version
#   - uv version
#   - venv Python version
#   - installed packages
#   - basic dependency health
#   - Flask process status
#   - port forwarding info
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
echo "[diagnostics] Dependency health (uv pip check):"
if [ -d ".venv" ]; then
    .venv/bin/uv pip check || echo "dependency issues detected"
else
    echo "no venv, skipping dependency check"
fi

echo
echo "[diagnostics] Flask process status:"
pgrep -fl flask || echo "Flask not running"

echo
echo "[diagnostics] Port forwarding (5000):"
ss -tulpn | grep 5000 || echo "Port 5000 not active"

echo "=========================================================="
