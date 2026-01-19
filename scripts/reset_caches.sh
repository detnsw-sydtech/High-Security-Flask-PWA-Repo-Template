# 1. Reset Python + uv state

rm -rf .venv
uv cache clean
uv sync --frozen
uv pip check


# 2. Reset framework artefacts
# delete pycache
# clear Jinja2 template caches
# remove JS build artefacts
# remove bundler caches

find . -type d -name "__pycache__" -exec rm -rf {} +
rm -rf dist/ build/ .next/ vite/.cache
rm -rf .jinja2_cache

# 3. Reset service‑worker and PWA artefacts
# remove old service worker builds
# regenerate manifest and hashed assets
# ensure no stale SW artefacts are committed
