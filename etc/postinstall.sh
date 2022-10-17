rm -rf src/viam/rpc/libviam_rust_utils.* || true
if [ "$(uname)" == "Linux" ]; then
    curl -sL -o src/viam/rpc/libviam_rust_utils.so https://github.com/viamrobotics/rust-utils/releases/latest/download/libviam_rust_utils-linux_$(uname -m).so
elif [ "$(uname)" == "Darwin" ]; then
    curl -sL -o src/viam/rpc/libviam_rust_utils.dylib https://github.com/viamrobotics/rust-utils/releases/latest/download/libviam_rust_utils-macosx_$(uname -m).dylib
fi
