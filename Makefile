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
