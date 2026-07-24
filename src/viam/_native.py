"""Shared loader for the bundled libviam_rust_utils native library."""

import ctypes
import pathlib
import sys
from functools import lru_cache


def _lib_suffix() -> str:
    if sys.platform == "darwin":
        return "dylib"
    if "linux" in sys.platform:
        return "so"
    return "dll"


@lru_cache(maxsize=1)
def load_native_lib() -> ctypes.CDLL:
    """Locate, load, and cache the bundled libviam_rust_utils shared library.

    Raises:
        OSError: if the native library cannot be found or loaded.
    """
    suffix = _lib_suffix()
    libname = pathlib.Path(__file__).parent.absolute() / "rpc" / f"libviam_rust_utils.{suffix}"
    return ctypes.CDLL(str(libname))
