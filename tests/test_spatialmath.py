from viam.spatialmath import _ffi


def test_ffi_new_and_free_quaternion():
    lib = _ffi.lib()
    ptr = lib.viam_new_quaternion(1.0, 0.0, 0.0, 0.0)
    assert ptr  # non-null
    comps = _ffi.read_components(lib.viam_quaternion_get_components, ptr, 4, lib.viam_free_quaternion_components)
    assert comps == [1.0, 0.0, 0.0, 0.0]
    lib.viam_free_quaternion_memory(ptr)
