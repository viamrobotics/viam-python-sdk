if [ "$(uname)" == "Linux" ]; then
    cp bin/libviam-linux_$(uname -m).so src/viam/rpc/libviam.so
elif [ "$(uname)" == "Darwin" ]; then
	cp bin/libviam-macosx_$(uname -m).dylib src/viam/rpc/libviam.dylib
fi
