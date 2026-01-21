#!/usr/bin/env bash

echo "🔧 Activating virtual environment..."
source .venv/bin/activate

echo "📦 Syncing dependencies with uv..."
uv sync

echo "🌱 Loading environment variables from .env (if present)..."
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

echo "🐍 Setting Flask application factory..."
export FLASK_APP=src.app:create_app

echo "🐞 Enabling Flask debug mode..."
export FLASK_ENV=development
export FLASK_DEBUG=1

echo "🚀 Starting Flask development server..."
uv run flask run --host=0.0.0.0 --port=5000
