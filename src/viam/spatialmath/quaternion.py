import weakref
from typing import List

from . import _ffi
from .vector3 import Vector3


class Quaternion:
    """A quaternion (w, i, j, k) backed by the rust-utils spatialmath FFI."""

    __slots__ = ("_handle", "__weakref__")

    def __init__(self, w: float, i: float, j: float, k: float):
        lib = _ffi.lib()
        self._handle = _ffi.check(lib.viam_new_quaternion(float(w), float(i), float(j), float(k)))
        weakref.finalize(self, lib.viam_free_quaternion_memory, self._handle)

    @classmethod
    def _from_handle(cls, handle) -> "Quaternion":
        obj = cls.__new__(cls)
        obj._handle = _ffi.check(handle)
        weakref.finalize(obj, _ffi.lib().viam_free_quaternion_memory, obj._handle)
        return obj

    @classmethod
    def from_imaginary_vector(cls, real: float, imag: Vector3) -> "Quaternion":
        return cls._from_handle(_ffi.lib().viam_new_quaternion_from_vector(float(real), imag._handle))

    def _components(self) -> List[float]:
        lib = _ffi.lib()
        return _ffi.read_components(lib.viam_quaternion_get_components, self._handle, 4, lib.viam_free_quaternion_components)

    @property
    def w(self) -> float:
        return self._components()[0]

    @property
    def i(self) -> float:
        return self._components()[1]

    @property
    def j(self) -> float:
        return self._components()[2]

    @property
    def k(self) -> float:
        return self._components()[3]

    @property
    def imaginary_vector(self) -> Vector3:
        return Vector3._from_handle(_ffi.lib().viam_quaternion_get_imaginary_vector(self._handle))

    def __mul__(self, other: "Quaternion") -> "Quaternion":
        return Quaternion._from_handle(_ffi.lib().viam_quaternion_hamiltonian_product(self._handle, other._handle))

    def __add__(self, other: "Quaternion") -> "Quaternion":
        return Quaternion._from_handle(_ffi.lib().viam_quaternion_add(self._handle, other._handle))

    def __sub__(self, other: "Quaternion") -> "Quaternion":
        return Quaternion._from_handle(_ffi.lib().viam_quaternion_subtract(self._handle, other._handle))

    def conjugate(self) -> "Quaternion":
        return Quaternion._from_handle(_ffi.lib().viam_quaternion_get_conjugate(self._handle))

    def scaled(self, factor: float) -> "Quaternion":
        return Quaternion._from_handle(_ffi.lib().viam_quaternion_get_scaled(self._handle, float(factor)))

    def normalized(self) -> "Quaternion":
        return Quaternion._from_handle(_ffi.lib().viam_quaternion_get_normalized(self._handle))

    def normalize(self) -> None:
        """Normalize this quaternion in place."""
        _ffi.lib().viam_normalize_quaternion(self._handle)

    def rotate_vector(self, v: Vector3) -> Vector3:
        return Vector3._from_handle(_ffi.lib().viam_quaternion_rotate_vector(self._handle, v._handle))

    @classmethod
    def from_pose(cls, pose) -> "Quaternion":
        from .orientation_vector import OrientationVector

        ov = OrientationVector(pose.o_x, pose.o_y, pose.o_z, pose.theta)
        return ov.to_quaternion()

    def to_pose(self, x: float, y: float, z: float):
        from viam.proto.common import Pose

        ov = self.to_orientation_vector()
        c = ov._components()
        return Pose(x=x, y=y, z=z, o_x=c[0], o_y=c[1], o_z=c[2], theta=c[3])

    def to_orientation_vector(self):
        from .orientation_vector import OrientationVector

        return OrientationVector._from_handle(_ffi.lib().viam_orientation_vector_from_quaternion(self._handle))

    def to_euler_angles(self):
        from .euler_angles import EulerAngles

        return EulerAngles._from_handle(_ffi.lib().viam_euler_angles_from_quaternion(self._handle))

    def to_axis_angle(self):
        from .axis_angle import AxisAngle

        return AxisAngle._from_handle(_ffi.lib().viam_axis_angle_from_quaternion(self._handle))

    def to_rotation_matrix(self):
        from .rotation_matrix import RotationMatrix

        return RotationMatrix._from_handle(_ffi.lib().viam_rotation_matrix_from_quaternion(self._handle))

    def __repr__(self) -> str:
        c = self._components()
        return f"Quaternion(w={c[0]}, i={c[1]}, j={c[2]}, k={c[3]})"
