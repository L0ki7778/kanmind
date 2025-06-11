#!/usr/bin/env bash

VENV_PATH="/e/programming/kanMind/kanmind_v2/env"

export VIRTUAL_ENV="$VENV_PATH"
export PATH="$VENV_PATH/Scripts:$PATH"
export PROMPT="(env) $PROMPT"

# Explicit alias so Git Bash uses the virtualenv Python
alias python="$VENV_PATH/Scripts/python.exe"
alias pip="$VENV_PATH/Scripts/pip.exe"

# Confirm it's working
echo "✅ Virtual environment activated!"
which python
python --version
