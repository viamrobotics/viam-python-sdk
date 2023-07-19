#!/bin/sh
cd `dirname $0`

# Create a virtual environment to run our code
VENV="venv"
PYTHON="$VENV/bin/python"

python3 -m venv $VENV
PYTHON -m pip install -r requirements.txt -U # remove -U if viam-sdk should not be upgraded whenever possible

# Be sure to use `exec` so that termination signals reach the python process,
# or handle forwarding termination signals manually
exec PYTHON -m src.main $@
