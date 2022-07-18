ROOT_DIR:=$(shell dirname $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))/../../../..)

run_server:
	cd ${ROOT_DIR} && poetry run python3 -m examples.server.v1.server

run_client:
	cd ${ROOT_DIR} && poetry run python3 -m examples.server.v1.client
