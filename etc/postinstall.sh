rm -rf src/viam/rpc/libviam.* || true
if [ "$(uname)" == "Linux" ]; then
    curl -sL -o src/viam/rpc/libviam.so https://github.com/viamrobotics/viam-rust-sdk/releases/latest/download/libviam-linux_$(uname -m).so
elif [ "$(uname)" == "Darwin" ]; then
    curl -sL -o src/viam/rpc/libviam.dylib https://github.com/viamrobotics/viam-rust-sdk/releases/latest/download/libviam-macosx_$(uname -m).dylib
fi
