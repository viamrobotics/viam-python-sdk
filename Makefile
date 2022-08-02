clean:
	find . -type d -name '__pycache__' | xargs rm -rf

lint:
	poetry run flake8 --exclude=**/gen/**

format:
	poetry run black --exclude ".*/gen/.*" ./src

buf:
	rm -rf src/viam/gen
	buf generate buf.build/viamrobotics/goutils
	buf generate buf.build/viamrobotics/rdk
	protol -e googl* --in-place -s _grpc.py -s _pb2.py -s _pb2.pyi -o src/viam/gen buf buf.build/viamrobotics/goutils
	protol -e googl* --in-place -s _grpc.py -s _pb2.py -s _pb2.pyi -o src/viam/gen buf buf.build/viamrobotics/rdk
	find src/viam/gen -type d -exec touch {}/__init__.py \;

better_imports:
	python3 -m etc.generate_proto_import
	@echo Add init files for specific documented protos
	touch src/viam/proto/__init__.py
	touch src/viam/proto/api/__init__.py

test:
	poetry run coverage run -m pytest && coverage html

documentation:
	cd docs && $(MAKE) clean html

package: buf better_imports test
	@echo "TODO: Create pip-installable package"
