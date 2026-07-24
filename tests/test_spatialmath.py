import gc
import json
import math
import pathlib

import pytest

from viam.proto.common import Orientation, Pose
from viam.proto.common import Vector3 as ProtoVector3
from viam.spatialmath import AxisAngle, EulerAngles, OrientationVector, Quaternion, RotationMatrix, Vector3, _ffi


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


def test_orientation_vector_roundtrip_with_quaternion():
    ov = OrientationVector(0.0, 0.0, 1.0, 0.0)
    q = ov.to_quaternion()
    back = q.to_orientation_vector()
    assert (round(back.o_x, 6), round(back.o_y, 6), round(back.o_z, 6), round(back.theta, 6)) == (0.0, 0.0, 1.0, 0.0)


def test_orientation_vector_proto_bridge():
    proto = Orientation(o_x=0.0, o_y=0.0, o_z=1.0, theta=0.5)
    ov = OrientationVector.from_proto(proto)
    out = ov.to_proto()
    assert (out.o_x, out.o_y, out.o_z, round(out.theta, 6)) == (0.0, 0.0, 1.0, 0.5)


def test_euler_angles_readback():
    ea = EulerAngles(0.1, 0.2, 0.3)
    assert (round(ea.roll, 9), round(ea.pitch, 9), round(ea.yaw, 9)) == (0.1, 0.2, 0.3)


def test_quaternion_to_euler_identity():
    ea = Quaternion(1, 0, 0, 0).to_euler_angles()
    assert (round(ea.roll, 9), round(ea.pitch, 9), round(ea.yaw, 9)) == (0.0, 0.0, 0.0)


def test_axis_angle_readback():
    # Use three distinct nonzero axis components so any x/y/z field swap or
    # theta-vs-axis bleed in the nested repr(C) struct is caught.
    n = math.sqrt(1 + 4 + 9)  # ||(1, 2, 3)|| = sqrt(14)
    x, y, z = 1 / n, 2 / n, 3 / n
    aa = AxisAngle(x, y, z, 1.5707963267948966)
    assert (round(aa.axis.x, 6), round(aa.axis.y, 6), round(aa.axis.z, 6)) == (round(x, 6), round(y, 6), round(z, 6))
    assert round(aa.theta, 6) == round(1.5707963267948966, 6)


def test_quaternion_to_axis_angle_identity():
    aa = Quaternion(1, 0, 0, 0).to_axis_angle()
    assert round(aa.theta, 9) == 0.0


def test_rotation_matrix_identity_from_quaternion():
    rm = Quaternion(1, 0, 0, 0).to_rotation_matrix()
    e = rm.elements
    assert [round(x, 6) for x in e] == [1, 0, 0, 0, 1, 0, 0, 0, 1]


def test_rotation_matrix_construct_roundtrip():
    rm = RotationMatrix([1, 0, 0, 0, 1, 0, 0, 0, 1])
    q = rm.to_quaternion()
    assert (round(q.w, 6), round(q.i, 6), round(q.j, 6), round(q.k, 6)) == (1.0, 0.0, 0.0, 0.0)


def test_rotation_matrix_elements_roundtrip_asymmetric():
    # 90 deg about Z is ASYMMETRIC, so this guards construct/read mutual consistency:
    # reading an FFI-produced matrix then constructing from those elements must
    # recover the same elements exactly.
    q = Quaternion(0.7071067811865476, 0.0, 0.0, 0.7071067811865476)
    e = q.to_rotation_matrix().elements
    e2 = RotationMatrix(e).elements
    assert [round(x, 9) for x in e2] == [round(x, 9) for x in e]
    # and the matrix must actually be asymmetric (otherwise the test proves nothing)
    assert round(e[1], 6) != round(e[3], 6)


def test_rotation_matrix_construct_from_external_elements():
    # An externally-supplied asymmetric matrix (rdk row-major convention) must read
    # back unchanged, documenting the construct-from-elements contract directly.
    e = [0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0]
    assert RotationMatrix(e).elements == e


def test_quaternion_from_and_to_pose():
    pose = Pose(x=1, y=2, z=3, o_x=0, o_y=0, o_z=1, theta=0)
    q = Quaternion.from_pose(pose)
    out = q.to_pose(1, 2, 3)
    assert (out.x, out.y, out.z) == (1.0, 2.0, 3.0)
    # identity orientation -> o_z = 1
    assert round(out.o_z, 6) == 1.0


def test_vector3_proto_bridge():
    v = Vector3.from_proto(ProtoVector3(x=1, y=2, z=3))
    out = v.to_proto()
    assert (out.x, out.y, out.z) == (1.0, 2.0, 3.0)


def test_orientation_vector_proto_theta_is_degrees():
    # proto theta is degrees; OrientationVector is radians-native
    proto = Orientation(o_x=0.0, o_y=0.0, o_z=1.0, theta=90.0)
    ov = OrientationVector.from_proto(proto)
    assert round(ov.theta, 9) == round(math.radians(90.0), 9)  # stored internally as radians
    out = ov.to_proto()
    assert round(out.theta, 6) == 90.0  # converted back to degrees


def test_quaternion_pose_theta_is_degrees():
    pose = Pose(x=1, y=2, z=3, o_x=0, o_y=0, o_z=1, theta=90.0)
    q = Quaternion.from_pose(pose)
    out = q.to_pose(1, 2, 3)
    assert (out.x, out.y, out.z) == (1.0, 2.0, 3.0)
    assert round(out.theta, 6) == 90.0  # degrees round-trip through radians-native quaternion


_GOLDEN = json.loads((pathlib.Path(__file__).parent / "spatialmath" / "fixtures" / "golden.json").read_text())


def _close(a, b, tol=1e-9):
    return math.isclose(a, b, rel_tol=0, abs_tol=tol)


@pytest.mark.parametrize("case", _GOLDEN["quaternion_conversions"], ids=lambda c: c["name"])
def test_quaternion_conversions_match_go(case):
    q = Quaternion(*case["quat"])

    ov = q.to_orientation_vector()
    assert all(_close(g, v) for g, v in zip(case["ov"], [ov.o_x, ov.o_y, ov.o_z, ov.theta])), f"ov mismatch for {case['name']}"

    ea = q.to_euler_angles()
    assert all(_close(g, v) for g, v in zip(case["euler"], [ea.roll, ea.pitch, ea.yaw])), f"euler mismatch for {case['name']}"

    aa = q.to_axis_angle()
    assert all(_close(g, v) for g, v in zip(case["axis_angle"], [aa.axis.x, aa.axis.y, aa.axis.z, aa.theta])), (
        f"axis_angle mismatch for {case['name']}"
    )

    rm = q.to_rotation_matrix()
    assert all(_close(g, v) for g, v in zip(case["rotation_matrix"], rm.elements)), f"rotation_matrix mismatch for {case['name']}"


def test_no_crash_under_churn():
    # Many construct/convert/drop cycles must not segfault or double-free.
    for _ in range(10000):
        q = Quaternion(0.5, 0.5, 0.5, 0.5)
        _ = (q * q).to_orientation_vector()
        _ = Vector3(1, 2, 3).cross(Vector3(4, 5, 6))
    gc.collect()  # finalizers run without crashing


def test_components_freed_path_repeatable():
    # Each property access allocates + frees the component array via the FFI;
    # repeated reads must stay stable (no corruption, no leak-driven drift).
    q = Quaternion(1, 0, 0, 0)
    for _ in range(1000):
        assert q.w == 1.0


def test_all_conversions_under_churn():
    # Exercise every conversion path + repr in a tight loop so all six wrappers'
    # finalizers are stressed together.
    for _ in range(2000):
        q = Quaternion(0.5, 0.5, 0.5, 0.5)
        ov = q.to_orientation_vector()
        ea = q.to_euler_angles()
        aa = q.to_axis_angle()
        rm = q.to_rotation_matrix()
        _ = (repr(q), repr(ov), repr(ea), repr(aa), repr(rm))
        _ = ov.to_quaternion()
    gc.collect()


def test_null_pointer_raises_value_error():
    # _ffi.check must raise ValueError on a null pointer (invalid FFI input).
    with pytest.raises(ValueError):
        _ffi.check(None)
