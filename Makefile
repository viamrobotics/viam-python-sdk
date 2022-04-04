clean:
	find . -type d -name '__pycache__' | xargs rm -rf

buf:
	rm -rf viam/gen
	rm -rf tmp/*.bin
	buf generate buf.build/viamrobotics/goutils
	buf generate buf.build/viamrobotics/rdk
	buf build -o tmp/goutils.bin --as-file-descriptor-set buf.build/viamrobotics/goutils
	buf build -o tmp/rdk.bin --as-file-descriptor-set buf.build/viamrobotics/rdk
	protol -e googl* --in-place -s _grpc.py -s _pb2.py -s _pb2.pyi -o viam/gen raw tmp/goutils.bin
	protol -e googl* --in-place -s _grpc.py -s _pb2.py -s _pb2.pyi -o viam/gen raw tmp/rdk.bin
	find viam/gen -type f -name '__init__.py' -delete

better_imports:
	python3 -m etc.generate_proto_import
	@echo Add init files for specific documented protos
	touch viam/proto/__init__.py
	touch viam/proto/api/__init__.py

test:
	python3 -m pytest

documentation:
	find docs/source -type f -name '*.rst' -not -name 'index.rst' -delete
	rm -rf docs/build/*
	SPHINX_APIDOC_OPTIONS="members,show-inheritance" sphinx-apidoc -efM --templatedir ./docs/templates -o ./docs/source ./viam
	sphinx-build -b html ./docs/source ./docs/build/html

package: buf better_imports test
	@echo "TODO: Create pip-installable package"
