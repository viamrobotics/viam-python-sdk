ROOT_DIR:=$(shell dirname $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))/../../../..)

run_server:
	cd ${ROOT_DIR} && python -m examples.echo.v1.server

run_client:
	cd ${ROOT_DIR} && python -m examples.echo.v1.client
