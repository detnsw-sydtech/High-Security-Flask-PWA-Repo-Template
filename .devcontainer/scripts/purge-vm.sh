#!/usr/bin/env bash

LOG_DIR=".devcontainer/logs"
LOG_FILE="$LOG_DIR/purge-$(date +%Y-%m-%d_%H-%M-%S).log"
STAMP_FILE="$HOME/.last_vm_purge"
NOW=$(date +%s)
SEVEN_DAYS=$((7 * 24 * 60 * 60))

mkdir -p "$LOG_DIR"

DRY_RUN=false
FORCE_PURGE=false

# ---------------------------------------------------------
# Parse flags
# ---------------------------------------------------------
for arg in "$@"; do
    case $arg in
        --dry-run)
            DRY_RUN=true
            ;;
        --force)
            FORCE_PURGE=true
            ;;
    esac
done

echo "===============================================" | tee -a "$LOG_FILE"
echo "🧹 Codespaces VM Purge Script" | tee -a "$LOG_FILE"
echo "===============================================" | tee -a "$LOG_FILE"

# ---------------------------------------------------------
# Disk usage warning
# ---------------------------------------------------------
DISK_USE=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')

if (( DISK_USE > 80 )); then
    echo "⚠️ WARNING: Disk usage is at ${DISK_USE}% — purge recommended." | tee -a "$LOG_FILE"
fi

# ---------------------------------------------------------
# Timestamp check
# ---------------------------------------------------------
if [ -f "$STAMP_FILE" ]; then
    LAST=$(cat "$STAMP_FILE")
    if (( NOW - LAST < SEVEN_DAYS )) && [ "$FORCE_PURGE" = false ]; then
        echo "⏳ Purge skipped — last purge was less than 7 days ago." | tee -a "$LOG_FILE"
        echo "Use --force to override." | tee -a "$LOG_FILE"
        exit 0
    fi
fi

# ---------------------------------------------------------
# BEFORE snapshot
# ---------------------------------------------------------
echo "" | tee -a "$LOG_FILE"
echo "📊 Disk usage BEFORE purge:" | tee -a "$LOG_FILE"
df -h / | tee -a "$LOG_FILE"

echo "" | tee -a "$LOG_FILE"
echo "📁 Folder sizes BEFORE purge:" | tee -a "$LOG_FILE"
du -sh ~/.vscode-server 2>/dev/null | tee -a "$LOG_FILE"
du -sh ~/.cache/pip 2>/dev/null | tee -a "$LOG_FILE"
du -sh ~/.cache/uv 2>/dev/null | tee -a "$LOG_FILE"
du -sh ~/.npm 2>/dev/null | tee -a "$LOG_FILE"
du -sh /tmp 2>/dev/null | tee -a "$LOG_FILE"

# ---------------------------------------------------------
# DRY RUN MODE
# ---------------------------------------------------------
if [ "$DRY_RUN" = true ]; then
    echo "" | tee -a "$LOG_FILE"
    echo "🔍 DRY RUN — showing what WOULD be deleted:" | tee -a "$LOG_FILE"
    echo "~/.vscode-server/{data,extensions/*/.cache}" | tee -a "$LOG_FILE"
    echo "~/.cache/pip" | tee -a "$LOG_FILE"
    echo "~/.cache/uv" | tee -a "$LOG_FILE"
    echo "~/.npm" | tee -a "$LOG_FILE"
    echo "/tmp/*" | tee -a "$LOG_FILE"
    echo "" | tee -a "$LOG_FILE"
    echo "Dry run complete — no files deleted." | tee -a "$LOG_FILE"
    exit 0
fi

# ---------------------------------------------------------
# PERFORM PURGE
# ---------------------------------------------------------
echo "" | tee -a "$LOG_FILE"
echo "🧹 Performing purge..." | tee -a "$LOG_FILE"

rm -rf ~/.vscode-server/{data,extensions/*/.cache} 2>/dev/null
rm -rf ~/.cache/pip ~/.cache/uv ~/.npm 2>/dev/null
rm -rf /tmp/* 2>/dev/null
find /workspaces -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null

echo "$NOW" > "$STAMP_FILE"

# ---------------------------------------------------------
# AFTER snapshot
# ---------------------------------------------------------
echo "" | tee -a "$LOG_FILE"
echo "📊 Disk usage AFTER purge:" | tee -a "$LOG_FILE"
df -h / | tee -a "$LOG_FILE"

echo "" | tee -a "$LOG_FILE"
echo "📁 Folder sizes AFTER purge:" | tee -a "$LOG_FILE"
du -sh ~/.vscode-server 2>/dev/null | tee -a "$LOG_FILE"
du -sh ~/.cache/pip 2>/dev/null | tee -a "$LOG_FILE"
du -sh ~/.cache/uv 2>/dev/null | tee -a "$LOG_FILE"
du -sh ~/.npm 2>/dev/null | tee -a "$LOG_FILE"
du -sh /tmp 2>/dev/null | tee -a "$LOG_FILE"

echo "" | tee -a "$LOG_FILE"
echo "✅ VM purge complete." | tee -a "$LOG_FILE"
echo "Log saved to: $LOG_FILE"
echo "===============================================" | tee -a "$LOG_FILE"
