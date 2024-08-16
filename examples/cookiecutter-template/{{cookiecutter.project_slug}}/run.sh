#!/bin/bash
set -e

SUDO=sudo
if ! command -v $SUDO; then
	echo "no sudo on this system, proceeding as current user"
	SUDO=""
fi

UNAME=$(uname -s)

if [ "$UNAME" = "Linux" ]
then
	echo "Installing venv on Linux"
$SUDO apt-get install -qqy python3-venv
fi

python3 -m venv .venv && . .venv/bin/activate && pip3 install -r requirements.txt
exec python3 -m src $@
