clean:
	find . -type d -name '__pycache__' | xargs rm -rf

_lint:
	flake8 --exclude=**/gen/**

lint:
	poetry run make _lint

_format:
	black --exclude ".*/gen/.*" ./src

format:
	poetry run make _format

_buf: clean
	rm -rf src/viam/gen
	buf generate buf.build/viamrobotics/api
	buf generate buf.build/viamrobotics/goutils
	protol -e googl* --in-place -s _grpc.py -s _pb2.py -s _pb2.pyi -o src/viam/gen buf buf.build/viamrobotics/api
	protol -e googl* --in-place -s _grpc.py -s _pb2.py -s _pb2.pyi -o src/viam/gen buf buf.build/viamrobotics/goutils
	find src/viam/gen -type d -exec touch {}/__init__.py \;

buf:
	poetry run make _buf

_better_imports:
	python3 -m etc.generate_proto_import -v
	@echo Add init files for specific documented protos

better_imports:
	poetry run make _better_imports

_test:
	coverage run -m pytest && coverage html

test:
	poetry run make _test

_test_docs:
	pytest --nbmake "./docs"

test_docs:
	kill -9 `ps aux | grep "[e]xamples.server.v1.server" | awk '{print $$2}'` || true
	poetry run python3 -m examples.server.v1.server 0.0.0.0 9091 quiet &
	poetry run make _test_docs
	kill -9 `ps aux | grep "[e]xamples.server.v1.server" | awk '{print $$2}'`

_documentation:
	cd docs && $(MAKE) clean html

documentation:
	poetry run make _documentation

package: clean buf better_imports format test
	@echo "TODO: Create pip-installable package"

install:
	poetry install
	sh etc/postinstall.sh
