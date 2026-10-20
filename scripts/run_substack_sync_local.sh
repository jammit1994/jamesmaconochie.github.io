#!/bin/bash
# Weekly Substack -> blog sync, run on James's Mac by launchd
# (~/Library/LaunchAgents/com.jamesmaconochie.substack-sync.plist).
#
# Substack blocks GitHub Actions, so the sync runs here instead: pull main,
# run scripts/substack_sync.py, then commit and push only the new posts and
# their hero images. Shows a macOS notification with the result.
#
# launchd runs this from a separate clone at ~/.local/share/substack-sync/site,
# because macOS blocks background jobs from reading OneDrive folders. The
# script works on whichever clone it lives in.
#
# Run by hand:   bash ~/.local/share/substack-sync/site/scripts/run_substack_sync_local.sh
# Log:           ~/Library/Logs/substack-sync.log

set -uo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
VENV="$HOME/.local/share/substack-sync/venv"
MANIFEST="$(mktemp -t substack-manifest)"
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"

notify() {
  osascript -e "display notification \"$1\" with title \"Substack sync\"" >/dev/null 2>&1 || true
}

fail() {
  echo "FAILED: $1"
  notify "Failed: $1. See ~/Library/Logs/substack-sync.log"
  rm -f "$MANIFEST"
  exit 1
}

echo "===== $(date '+%Y-%m-%d %H:%M:%S') ====="
cd "$REPO" || fail "repo folder not found"

# OneDrive/VS Code can leave a stale git lock behind
[ -e .git/index.lock ] && fail "git is locked (.git/index.lock exists)"

[ "$(git rev-parse --abbrev-ref HEAD)" = "main" ] || fail "repo is not on the main branch"

# One-time setup of the Python environment
if [ ! -x "$VENV/bin/python" ]; then
  echo "Creating Python environment at $VENV"
  /usr/bin/python3 -m venv "$VENV" || fail "could not create Python environment"
  "$VENV/bin/pip" install -q python-dateutil requests markdownify beautifulsoup4 \
    || fail "could not install Python packages"
fi

git pull --ff-only --autostash -q origin main || fail "git pull failed"

MANIFEST_PATH="$MANIFEST" "$VENV/bin/python" scripts/substack_sync.py \
  || fail "sync script error"

# Files the sync created: each post plus its hero image
FILES=()
while IFS= read -r f; do
  [ -n "$f" ] && FILES+=("$f")
done < <("$VENV/bin/python" -c '
import json, sys
for p in json.load(open(sys.argv[1])):
    for k in ("filepath", "image_path"):
        if p.get(k):
            print(p[k])
' "$MANIFEST")

TITLES="$("$VENV/bin/python" -c '
import json, sys
print(", ".join(p["title"] for p in json.load(open(sys.argv[1]))))
' "$MANIFEST")"
rm -f "$MANIFEST"

if [ ${#FILES[@]} -eq 0 ]; then
  echo "No new posts."
  exit 0
fi

git add -- "${FILES[@]}" || fail "git add failed"
git commit -q -m "Add Substack post(s): $TITLES

Auto-synced from Substack by scripts/run_substack_sync_local.sh." -- "${FILES[@]}" \
  || fail "git commit failed"
git push -q origin main || fail "git push failed (post is committed locally)"

echo "Published: $TITLES"
notify "New on the blog: $TITLES"
