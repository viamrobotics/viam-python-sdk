import ctypes

from viam._native import load_native_lib


def test_load_native_lib_returns_cdll():
    lib = load_native_lib()
    assert isinstance(lib, ctypes.CDLL)


def test_load_native_lib_is_cached():
    assert load_native_lib() is load_native_lib()
