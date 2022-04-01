clean:
	find . -type d -name '__pycache__' | xargs rm -rf

buf:
	rm -rf viam/gen
	rm -rf tmp/*.bin
	buf generate buf.build/viamrobotics/goutils
	buf generate /Users/njooma/Developer/rdk
	buf build -o tmp/goutils.bin --as-file-descriptor-set buf.build/viamrobotics/goutils
	buf build -o tmp/rdk.bin --as-file-descriptor-set /Users/njooma/Developer/rdk
	protol -e googl* --in-place -s _grpc.py -s _pb2.py -s _pb2.pyi -o viam/gen raw tmp/goutils.bin
	protol -e googl* --in-place -s _grpc.py -s _pb2.py -s _pb2.pyi -o viam/gen raw tmp/rdk.bin
	find viam/gen -type f -name '__init__.py' -delete

better_imports:
	python3 -m etc.generate_proto_import

test:
	python3 -m pytest

documentation:
	pdoc -o ./docs ./viam

dox: buf
	sphinx-apidoc -f -o ./docsx/source ./viam
	sphinx-build -b html ./docsx/source ./docsx/build/html

package: buf better_imports test
	@echo "TODO: Create pip-installable package"
