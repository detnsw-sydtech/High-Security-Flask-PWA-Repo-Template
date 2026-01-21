#!/usr/bin/env bash

echo "🔍 Checking for virtual environment..."
if [ ! -d ".venv" ]; then
    echo "❌ No virtual environment found. Run 'uv venv' first."
    exit 1
fi

echo "🔧 Activating virtual environment..."
source .venv/bin/activate

echo "📦 Syncing dependencies with uv..."
uv sync

echo "🌱 Loading environment variables from .env (if present)..."
if [ -f .env ]; then
    set -o allexport
    source .env
    set +o allexport
    echo "✅ Environment variables loaded."
else
    echo "⚠️ No .env file found. Continuing without environment variables."
fi

echo "🐍 Setting Flask application factory..."
export FLASK_APP="src.app:create_app"

echo "🐞 Enabling Flask debug mode..."
export FLASK_ENV="development"
export FLASK_DEBUG=1

echo "🚀 Starting Flask development server..."
uv run flask run --host=0.0.0.0 --port=5000
