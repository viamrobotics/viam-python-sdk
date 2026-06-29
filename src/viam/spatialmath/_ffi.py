"""Low-level ctypes binding to the spatialmath exports of libviam_rust_utils.

Private. The public API is the wrapper classes in this package.
"""

import ctypes
from ctypes import POINTER, c_double, c_void_p
from functools import lru_cache
from typing import Callable, List

from viam._native import load_native_lib


class _EulerAnglesStruct(ctypes.Structure):
    # rust-utils: #[repr(C)] struct EulerAngles { roll, pitch, yaw: f64 }
    _fields_ = [("roll", c_double), ("pitch", c_double), ("yaw", c_double)]


class _Vec3Struct(ctypes.Structure):
    _fields_ = [("x", c_double), ("y", c_double), ("z", c_double)]


class _AxisAngleStruct(ctypes.Structure):
    # rust-utils: #[repr(C)] struct AxisAngle { axis: Vector3<f64>, theta: f64 }
    _fields_ = [("axis", _Vec3Struct), ("theta", c_double)]


class _Rotation3Struct(ctypes.Structure):
    # nalgebra Rotation3 wraps a column-major Matrix3<f64>. Validated by golden tests.
    _fields_ = [("m", c_double * 9)]


# (restype, argtypes) for every viam_-prefixed spatialmath export we use.
_SIGNATURES = {
    # vector3
    "viam_new_vector3": (c_void_p, (c_double, c_double, c_double)),
    "viam_free_vector_memory": (None, (c_void_p,)),
    "viam_vector_get_components": (POINTER(c_double), (c_void_p,)),
    "viam_free_vector_components": (None, (c_void_p,)),
    "viam_vector_set_x": (None, (c_void_p, c_double)),
    "viam_vector_set_y": (None, (c_void_p, c_double)),
    "viam_vector_set_z": (None, (c_void_p, c_double)),
    "viam_normalize_vector": (None, (c_void_p,)),
    "viam_vector_get_normalized": (c_void_p, (c_void_p,)),
    "viam_scale_vector": (None, (c_void_p, c_double)),
    "viam_vector_get_scaled": (c_void_p, (c_void_p, c_double)),
    "viam_vector_add": (c_void_p, (c_void_p, c_void_p)),
    "viam_vector_subtract": (c_void_p, (c_void_p, c_void_p)),
    "viam_vector_dot_product": (c_double, (c_void_p, c_void_p)),
    "viam_vector_cross_product": (c_void_p, (c_void_p, c_void_p)),
    # quaternion
    "viam_new_quaternion": (c_void_p, (c_double, c_double, c_double, c_double)),
    "viam_new_quaternion_from_vector": (c_void_p, (c_double, c_void_p)),
    "viam_free_quaternion_memory": (None, (c_void_p,)),
    "viam_quaternion_get_components": (POINTER(c_double), (c_void_p,)),
    "viam_free_quaternion_components": (None, (c_void_p,)),
    "viam_quaternion_set_real": (None, (c_void_p, c_double)),
    "viam_quaternion_set_i": (None, (c_void_p, c_double)),
    "viam_quaternion_set_j": (None, (c_void_p, c_double)),
    "viam_quaternion_set_k": (None, (c_void_p, c_double)),
    "viam_quaternion_set_components": (None, (c_void_p, c_double, c_double, c_double, c_double)),
    "viam_quaternion_set_imag_from_vector": (None, (c_void_p, c_void_p)),
    "viam_quaternion_get_imaginary_vector": (c_void_p, (c_void_p,)),
    "viam_normalize_quaternion": (None, (c_void_p,)),
    "viam_quaternion_get_normalized": (c_void_p, (c_void_p,)),
    "viam_quaternion_rotate_vector": (c_void_p, (c_void_p, c_void_p)),
    "viam_scale_quaternion": (None, (c_void_p, c_double)),
    "viam_quaternion_get_scaled": (c_void_p, (c_void_p, c_double)),
    "viam_quaternion_get_conjugate": (c_void_p, (c_void_p,)),
    "viam_quaternion_add": (c_void_p, (c_void_p, c_void_p)),
    "viam_quaternion_subtract": (c_void_p, (c_void_p, c_void_p)),
    "viam_quaternion_hamiltonian_product": (c_void_p, (c_void_p, c_void_p)),
    "viam_quaternion_from_euler_angles": (c_void_p, (c_double, c_double, c_double)),
    "viam_quaternion_from_axis_angle": (c_void_p, (c_double, c_double, c_double, c_double)),
    "viam_quaternion_from_axis_angle_vector": (c_void_p, (c_double, c_void_p)),
    "viam_quaternion_from_rotation_matrix": (c_void_p, (c_void_p,)),
    "viam_quaternion_from_orientation_vector": (c_void_p, (c_void_p,)),
    # orientation vector
    "viam_new_orientation_vector": (c_void_p, (c_double, c_double, c_double, c_double)),
    "viam_free_orientation_vector_memory": (None, (c_void_p,)),
    "viam_orientation_vector_get_components": (POINTER(c_double), (c_void_p,)),
    "viam_free_orientation_vector_components": (None, (c_void_p,)),
    "viam_orientation_vector_from_quaternion": (c_void_p, (c_void_p,)),
    # euler angles (no getter; read via _EulerAnglesStruct)
    "viam_new_euler_angles": (c_void_p, (c_double, c_double, c_double)),
    "viam_free_euler_angles_memory": (None, (c_void_p,)),
    "viam_euler_angles_from_quaternion": (c_void_p, (c_void_p,)),
    # axis angle (no getter; read via _AxisAngleStruct)
    "viam_new_axis_angle": (c_void_p, (c_double, c_double, c_double, c_double)),
    "viam_free_axis_angles_memory": (None, (c_void_p,)),
    "viam_axis_angle_from_quaternion": (c_void_p, (c_void_p,)),
    # rotation matrix (no getter; read via _Rotation3Struct)
    "viam_new_rotation_matrix": (c_void_p, (POINTER(c_double * 9),)),
    "viam_free_rotation_matrix_memory": (None, (c_void_p,)),
    "viam_rotation_matrix_from_quaternion": (c_void_p, (c_void_p,)),
}


@lru_cache(maxsize=1)
def lib() -> ctypes.CDLL:
    """Return the shared CDLL with all spatialmath signatures configured."""
    _lib = load_native_lib()
    for name, (restype, argtypes) in _SIGNATURES.items():
        fn = getattr(_lib, name)
        fn.restype = restype
        fn.argtypes = argtypes
    return _lib


def check(ptr):
    """Raise on a null pointer returned by the FFI."""
    if not ptr:
        raise ValueError("spatialmath FFI returned a null pointer (invalid input)")
    return ptr


def read_components(getter: Callable, handle, count: int, freer: Callable) -> List[float]:
    """Call a *_get_components getter, copy `count` doubles to Python floats, free the array."""
    arr_ptr = check(getter(handle))
    values = [arr_ptr[i] for i in range(count)]
    freer(ctypes.cast(arr_ptr, c_void_p))
    return values


def read_struct(handle, struct_type):
    """Read a repr(C) struct value off a handle pointer (for euler/axis/rotation).

    The returned struct *aliases* the handle's memory (unlike ``read_components``,
    which copies). Read out the fields you need while the handle is still alive;
    do not retain the returned struct after the handle is freed.
    """
    return ctypes.cast(handle, POINTER(struct_type)).contents
