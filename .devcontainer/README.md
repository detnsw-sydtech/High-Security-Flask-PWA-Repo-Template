.devcontainer/
│
├── devcontainer.json
│   # Canonical configuration:
│   # - Python 3.12 base image
│   # - overrideCommand: false
│   # - postStartCommand runs preflight + startup
│   # - port forwarding + VS Code extensions
│
├── preflight.sh
│   # Layer 1 automation:
│   # - Validates Python version
│   # - Checks uv installation
│   # - Detects venv drift
│   # - Never mutates the environment
│   # - Safe to run synchronously on every boot
│
├── startup.sh
│   # Layer 2 automation:
│   # - Ensures .venv exists (creates if missing)
│   # - Activates venv
│   # - Runs uv sync
│   # - Launches Flask in background
│   # - Writes logs to /tmp/startup.log
│
├── scripts/
│   ├── install-uv.sh
│   │   # Optional helper:
│   │   # - Installs uv if missing
│   │   # - Used only in postCreateCommand (if ever needed)
│   │
│   ├── rebuild-venv.sh
│   │   # Optional helper:
│   │   # - rm -rf .venv && uv venv && uv sync
│   │   # - Used for drift recovery or teaching moments
│   │
│   └── diagnostics.sh
│       # Optional helper:
│       # - Prints environment diagnostics
│       # - Useful for student debugging
│
├── logs/
│   └── README.md
│       # Explains:
│       # - /tmp/startup.log (Flask + startup output)
│       # - /tmp/flask.log (Flask runtime logs)
│       # - Why logs are not stored in the repo
│
└── README.md
    # Student‑facing documentation:
    # - What the devcontainer does
    # - How automation works
    # - How to rebuild the Codespace
    # - How to interpret preflight warnings
    # - How to read startup logs
