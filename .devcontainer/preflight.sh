#!/usr/bin/env bash
set -euo pipefail

REQUIRED="3.12"

echo "🔍 Running devcontainer preflight checks..."

# ---------------------------------------------------------
# 1. Check system Python version
# ---------------------------------------------------------
if command -v python3 >/dev/null 2>&1; then
    CURRENT="$(python3 --version | awk '{print $2}' | cut -d. -f1-2)"
else
    echo "❌ ERROR: python3 not found in PATH."
    echo "This environment is not valid for the High Security Flask PWA template."
    exit 1
fi

if [ "$CURRENT" != "$REQUIRED" ]; then
    echo "❌ ERROR: System Python version mismatch."
    echo "Found:    $CURRENT"
    echo "Required: $REQUIRED"
    echo "Please rebuild the Codespace so it uses the correct Python version."
    exit 1
fi

echo "✅ System Python version OK ($CURRENT)"

# ---------------------------------------------------------
# 2. Check uv installation
# ---------------------------------------------------------
if ! command -v uv >/dev/null 2>&1; then
    echo "⚠️ WARNING: uv is not installed or not on PATH."
    echo "The postCreateCommand should have installed uv."
    echo "Try rebuilding the container or run:"
    echo "    bash .devcontainer/scripts/install-uv.sh"
else
    echo "✅ uv is installed ($(uv --version))"
fi

# ---------------------------------------------------------
# 3. Check virtual environment drift
# ---------------------------------------------------------
if [ -d ".venv" ]; then
    if [ -x ".venv/bin/python3" ]; then
        VENV_PY="$(.venv/bin/python3 --version | awk '{print $2}' | cut -d. -f1-2)"
        if [ "$VENV_PY" != "$REQUIRED" ]; then
            echo "⚠️ WARNING: Your virtual environment was created with Python $VENV_PY."
            echo "This may cause dependency or bytecode drift."
            echo "Recommended fix:"
            echo "    bash .devcontainer/scripts/rebuild-venv.sh"
        else
            echo "✅ Virtual environment Python version OK ($VENV_PY)"
        fi
    fi
else
    echo "ℹ️ No virtual environment detected yet. This is normal on first boot."
fi

# ---------------------------------------------------------
# 4. Ensure .venv exists after setup (when used in lifecycle)
# ---------------------------------------------------------
if [ ! -d ".venv" ]; then
    echo "⚠️ NOTE: .venv does not exist yet."
    echo "If this is after postCreateCommand, run:"
    echo "    bash .devcontainer/scripts/rebuild-venv.sh"
else
    echo "✅ .venv directory present."
fi

echo "✨ Preflight checks complete."
