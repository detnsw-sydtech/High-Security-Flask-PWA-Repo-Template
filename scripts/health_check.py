"""
Comprehensive environment health check for Codespaces and local development.
Run with:
    uv run python scripts/health_check.py
"""

import os
import sys
import importlib
from pathlib import Path

# ---------------------------------------------------------------------
# Allowed modules for dynamic import (prevents arbitrary code execution)
# ---------------------------------------------------------------------
ALLOWED_MODULES = {
    "flask",
    "sqlalchemy",
    "faker",
    "flask_sqlalchemy",
    "src.app",
    "src.app.main",
    "src.app.extensions",
    "src.app.models",
}

def safe_import(module: str):
    """Import a module only if it is explicitly allowed."""
    if module not in ALLOWED_MODULES:
        raise ValueError(f"Module '{module}' is not allowed for import")
    return importlib.import_module(module)

# ---------------------------------------------------------------------

def check_python():
    print("🔍 Checking Python version…")
    print(f"   Python: {sys.version}")
    # Adjusted to match repo standard: Python 3.12+
    assert sys.version_info >= (3, 12), "Python 3.12+ required"
    print("   ✔ OK\n")

def check_uv():
    print("🔍 Checking uv installation…")
    uv_path = Path.home() / ".local" / "bin" / "uv"
    assert uv_path.exists(), "uv not found"
    print(f"   uv found at: {uv_path}")
    print("   ✔ OK\n")

def check_venv():
    print("🔍 Checking virtual environment…")
    assert ".venv" in sys.executable, "Not running inside .venv"
    print(f"   Using interpreter: {sys.executable}")
    print("   ✔ OK\n")

def check_imports():
    print("🔍 Checking required imports…")
    for module in ["flask", "sqlalchemy", "faker", "flask_sqlalchemy"]:
        try:
            safe_import(module)
            print(f"   ✔ {module} imported")
        except ImportError:
            raise AssertionError(f"Missing dependency: {module}")
    print()

def check_flask_app():
    print("🔍 Checking Flask app import…")
    try:
        from src.app import create_app
        app = create_app()
        assert app is not None
        print("   ✔ Flask app created successfully\n")
    except Exception as e:
        raise AssertionError(f"Flask app failed to load: {e}")

def check_env_vars():
    print("🔍 Checking environment variables…")
    required = ["FLASK_APP"]
    for var in required:
        assert var in os.environ, f"Missing environment variable: {var}"
        print(f"   ✔ {var} = {os.environ[var]}")
    print()

if __name__ == "__main__":
    print("=== STHS Environment Health Check ===\n")
    check_python()
    check_uv()
    check_venv()
    check_imports()
    check_flask_app()
    check_env_vars()
    print("🎉 All checks passed — environment is healthy!")
