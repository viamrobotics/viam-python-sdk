#!/bin/sh
cd `dirname $0`

poetry run python -m src.main $@
