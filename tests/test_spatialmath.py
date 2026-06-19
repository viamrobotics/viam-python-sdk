from viam.spatialmath import Quaternion, Vector3, _ffi


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


def test_quaternion_components():
    q = Quaternion(1, 0, 0, 0)
    assert (q.w, q.i, q.j, q.k) == (1.0, 0.0, 0.0, 0.0)


def test_quaternion_hamiltonian_product_identity():
    q = Quaternion(0.5, 0.5, 0.5, 0.5)
    ident = Quaternion(1, 0, 0, 0)
    p = q * ident
    assert (round(p.w, 9), round(p.i, 9), round(p.j, 9), round(p.k, 9)) == (0.5, 0.5, 0.5, 0.5)


def test_quaternion_conjugate():
    c = Quaternion(1, 2, 3, 4).conjugate()
    assert (c.w, c.i, c.j, c.k) == (1.0, -2.0, -3.0, -4.0)


def test_quaternion_rotate_vector():
    # 180 deg about Z maps +X to -X
    q = Quaternion(0, 0, 0, 1)
    r = q.rotate_vector(Vector3(1, 0, 0))
    assert (round(r.x, 6), round(r.y, 6), round(r.z, 6)) == (-1.0, 0.0, 0.0)
