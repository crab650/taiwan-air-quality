#!/bin/bash
# Taiwan Air Quality Tracker - PythonAnywhere Git Sync Automation
# This script runs the crawler and commits/pushes changes to GitHub.

# Resolve the absolute path of the script directory
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR"

echo "=== Air Quality Tracker Git Sync Start: $(date) ==="

# 1. Execute the Python crawler to get the latest AQI data
if [ -f "aqi_crawler_pa.py" ]; then
    python aqi_crawler_pa.py
else
    echo "[!] Error: aqi_crawler_pa.py not found in $DIR"
    exit 1
fi

# 2. Initialize Git and remote if not already set up
TARGET_REMOTE="https://github.com/crab650/taiwan-air-quality.git"

if [ ! -d ".git" ]; then
    echo "[*] Git repository not detected. Initializing git..."
    git init
    git branch -M main
fi

CURRENT_REMOTE=$(git remote get-url origin 2>/dev/null)

if [ -z "$CURRENT_REMOTE" ]; then
    echo "[*] Adding remote origin: $TARGET_REMOTE"
    git remote add origin "$TARGET_REMOTE"
elif [ "$CURRENT_REMOTE" != "$TARGET_REMOTE" ]; then
    echo "[*] Updating remote origin to: $TARGET_REMOTE"
    git remote set-url origin "$TARGET_REMOTE"
fi

# 3. Check if data/ folder has changed or README.md has changed
STATUS=$(git status --porcelain data/ README.md)

if [ -n "$STATUS" ]; then
    echo "[*] Changes detected in air quality data or README. Preparing to commit..."
    
    # Stage the data and the updated README
    git add data/ README.md
    
    # Commit with local timestamp
    git commit -m "Auto-update air quality data and README: $(date +'%Y-%m-%d %H:%M:%S')"
    
    # Push to remote main branch
    echo "[*] Pushing updates to GitHub..."
    git push origin main
    
    if [ $? -eq 0 ]; then
        echo "[+] Push successful!"
    else
        echo "[!] Error: Failed to push to GitHub. (Note: Make sure your credentials or GitHub Personal Access Token is configured.)"
    fi
else
    echo "[*] No changes detected in air quality data. Skipping git push."
fi

echo "=== Air Quality Tracker Git Sync Complete: $(date) ==="
echo ""
