.PHONY: clean
clean:
	find . -type d -name '__pycache__' | xargs rm -rf

.PHONY: lint
lint:
	ruff check ./src ./tests

.PHONY: format
format:
	ruff format ./src ./tests
	ruff check --extend-select I --fix ./src ./tests

.PHONY: buf
buf: clean
	rm -rf src/viam/gen
	chmod +x plugin/main.py
	uv pip install protoletariat
	uv pip install protobuf==5.29.6
	$(eval API_VERSION := $(shell grep 'API_VERSION' src/viam/version_metadata.py | awk -F '"' '{print $$2}'))
	buf generate buf.build/viamrobotics/api:${API_VERSION}
	buf generate buf.build/viamrobotics/goutils
	protol -e googl* --in-place -s _grpc.py -s _pb2.py -s _pb2.pyi -o src/viam/gen buf buf.build/viamrobotics/api
	protol -e googl* --in-place -s _grpc.py -s _pb2.py -s _pb2.pyi -o src/viam/gen buf buf.build/viamrobotics/goutils
	find src/viam/gen -type d -exec touch {}/__init__.py \;
	uv run python3 -m etc.generate_proto_import -v

.PHONY: test
test:
	coverage run -m pytest && coverage html

.PHONY: test_docs
test_docs:
	kill -9 `ps aux | grep "[d]ocs.examples._server" | awk '{print $$2}'` || true
	kill -9 `ps aux | grep "[e]xamples.server.v1.server" | awk '{print $$2}'` || true
	python3 -m docs.examples._server &
	python3 -m examples.server.v1.server 0.0.0.0 9091 quiet &
	sleep 3
	pytest --nbmake "./docs"
	kill -9 `ps aux | grep "[d]ocs.examples._server" | awk '{print $$2}'`
	kill -9 `ps aux | grep "[e]xamples.server.v1.server" | awk '{print $$2}'`

.PHONY: typecheck
typecheck:
	pyright

.PHONY: documentation
documentation:
	$(MAKE) -C docs clean html

.PHONY: install
install:
	uv sync --all-extras
	bash etc/postinstall.sh
