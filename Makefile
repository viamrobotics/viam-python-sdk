clean:
	find . -type d -name '__pycache__' | xargs rm -rf

buf:
	rm -rf proto
	buf generate buf.build/viamrobotics/goutils
	buf generate buf.build/viamrobotics/rdk
