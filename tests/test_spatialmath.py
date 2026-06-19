from viam.spatialmath import Vector3, _ffi


def test_ffi_new_and_free_quaternion():
    lib = _ffi.lib()
    ptr = lib.viam_new_quaternion(1.0, 0.0, 0.0, 0.0)
    assert ptr  # non-null
    comps = _ffi.read_components(lib.viam_quaternion_get_components, ptr, 4, lib.viam_free_quaternion_components)
    assert comps == [1.0, 0.0, 0.0, 0.0]
    lib.viam_free_quaternion_memory(ptr)


def test_vector3_components():
    v = Vector3(1.0, 2.0, 3.0)
    assert (v.x, v.y, v.z) == (1.0, 2.0, 3.0)


def test_vector3_dot_and_cross():
    a, b = Vector3(1, 0, 0), Vector3(0, 1, 0)
    assert a.dot(b) == 0.0
    c = a.cross(b)
    assert (round(c.x), round(c.y), round(c.z)) == (0, 0, 1)


def test_vector3_normalized():
    n = Vector3(3, 0, 0).normalized()
    assert (round(n.x, 6), n.y, n.z) == (1.0, 0.0, 0.0)
