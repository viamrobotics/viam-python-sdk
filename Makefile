buf:
	find ./gen -not -name '__init__.py' -delete
	buf generate buf.build/googleapis/googleapis
	buf generate buf.build/viamrobotics/goutils
