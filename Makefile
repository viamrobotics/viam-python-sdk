GEN_DIR='./viam/gen'

clean:
	find . -type d -name '__pycache__' | xargs rm -rf

buf:
	find $(GEN_DIR) -not -name '__init__.py' -delete || true
	buf generate buf.build/googleapis/googleapis
	buf generate buf.build/viamrobotics/goutils
	buf generate buf.build/viamrobotics/rdk
