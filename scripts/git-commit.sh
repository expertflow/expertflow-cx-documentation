#!/usr/bin/env zsh
# Run from the repo root. Stages all tracked changes, commits via Haiku, then pushes.

set -e

cd "$(git rev-parse --show-toplevel)"

if [[ -z "$(git status --porcelain)" ]]; then
  echo "Nothing to commit."
  exit 0
fi

echo "==> Staged changes:"
git status --short

echo ""
echo "==> Asking Haiku to commit..."

claude --model haiku -p \
  "You are helping commit changes to a git repository. Do the following steps in order:
1. Run git status to see what changed.
2. Stage appropriate files with git add (skip .env, secrets, or generated lock files unless they were explicitly modified as part of a feature).
3. Check recent git log to match commit message style.
4. Create a concise, meaningful commit message and commit. End the commit message with: Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
5. Push to the current remote branch with: git push

Do not skip pre-commit hooks. Do not amend existing commits." \
  --allowedTools "Bash"

echo ""
echo "==> Done."
