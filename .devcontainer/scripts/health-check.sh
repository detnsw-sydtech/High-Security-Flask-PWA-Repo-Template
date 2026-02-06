#!/usr/bin/env bash
set -e

echo "==============================================="
echo "🔍 SE12 Environment Health Check"
echo "==============================================="

prompt_repair () {
    local message="$1"
    echo ""
    read -p "$message [y/N]: " choice
    case "$choice" in
        y|Y ) return 0 ;;
        * )   return 1 ;;
    esac
}

# ------------------------------------------------
# Python
# ------------------------------------------------
echo -n "🐍 Python version: "
python3 --version || {
    echo "❌ Python not found"
    echo "This should never happen inside the devcontainer."
    exit 1
}

# ------------------------------------------------
# uv
# ------------------------------------------------
echo -n "⚡ uv version: "
uv --version || {
    echo "❌ uv not found"
    echo "This should never happen inside the devcontainer."
    exit 1
}

# ------------------------------------------------
# Virtual environment
# ------------------------------------------------
if [ -d ".venv" ]; then
    echo "📦 Virtual environment: present"
else
    echo "❌ Virtual environment missing (.venv not found)"
    if prompt_repair "Would you like to create a new virtual environment using 'uv sync'" ; then
        uv sync
    else
        exit 1
    fi
fi

# ------------------------------------------------
# Dependency integrity
# ------------------------------------------------
echo -n "🔐 Checking lockfile integrity... "
if uv lock --check >/dev/null 2>&1; then
    echo "OK"
else
    echo "❌ Lockfile mismatch"
    if prompt_repair "Run 'uv sync' to repair dependency state" ; then
        uv sync
    else
        exit 1
    fi
fi

# ------------------------------------------------
# Flask
# ------------------------------------------------
echo -n "🔥 Flask import test: "
if uv run python3 -c "import flask" >/dev/null 2>&1; then
    echo "OK"
else
    echo "❌ Flask not installed"
    if prompt_repair "Install missing dependencies with 'uv sync'" ; then
        uv sync
    else
        exit 1
    fi
fi

# ------------------------------------------------
# MkDocs
# ------------------------------------------------
echo -n "📚 MkDocs version: "
if uv run mkdocs --version >/dev/null 2>&1; then
    uv run mkdocs --version
else
    echo "❌ MkDocs not installed"
    if prompt_repair "Install MkDocs using 'uv sync --group docs'" ; then
        uv sync --group docs
    else
        exit 1
    fi
fi

# ------------------------------------------------
# MkDocs plugins
# ------------------------------------------------
echo "🔌 Checking MkDocs plugins..."

check_plugin () {
    local plugin=$1
    if uv run python3 -c "import $plugin" >/dev/null 2>&1; then
        echo "   ✔ $plugin"
    else
        echo "   ❌ $plugin missing"
        MISSING_PLUGIN=1
    fi
}

MISSING_PLUGIN=0
check_plugin "mkdocs_autorefs"
check_plugin "mkdocs_material"
check_plugin "mkdocs_mermaid2_plugin"
check_plugin "mkdocs_material_extensions"

if [ "$MISSING_PLUGIN" -eq 1 ]; then
    if prompt_repair "Install missing MkDocs plugins using 'uv sync --group docs'" ; then
        uv sync --group docs
    else
        exit 1
    fi
fi

# ------------------------------------------------
# Final result
# ------------------------------------------------
echo "==============================================="
echo "✅ All checks passed — environment is healthy"
echo "==============================================="
