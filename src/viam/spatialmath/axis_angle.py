import weakref
from typing import NamedTuple

from . import _ffi


class Axis(NamedTuple):
    x: float
    y: float
    z: float


class AxisAngle:
    """Axis-angle (axis x/y/z, theta) backed by the spatialmath FFI."""

    __slots__ = ("_handle", "__weakref__")

    def __init__(self, x: float, y: float, z: float, theta: float):
        lib = _ffi.lib()
        self._handle = _ffi.check(lib.viam_new_axis_angle(float(x), float(y), float(z), float(theta)))
        weakref.finalize(self, lib.viam_free_axis_angles_memory, self._handle)

    @classmethod
    def _from_handle(cls, handle) -> "AxisAngle":
        obj = cls.__new__(cls)
        obj._handle = _ffi.check(handle)
        weakref.finalize(obj, _ffi.lib().viam_free_axis_angles_memory, obj._handle)
        return obj

    def _struct(self):
        return _ffi.read_struct(self._handle, _ffi._AxisAngleStruct)

    @property
    def axis(self) -> Axis:
        s = self._struct()
        x, y, z = s.axis.x, s.axis.y, s.axis.z
        if x == 0.0 and y == 0.0 and z == 0.0:
            # zero rotation: the axis is mathematically undefined; match Go rdk's canonical (0, 0, 1)
            return Axis(0.0, 0.0, 1.0)
        return Axis(x, y, z)

    @property
    def theta(self) -> float:
        return self._struct().theta

    def to_quaternion(self):
        from .quaternion import Quaternion

        s = self._struct()
        return Quaternion._from_handle(_ffi.lib().viam_quaternion_from_axis_angle(s.axis.x, s.axis.y, s.axis.z, s.theta))

    def __repr__(self) -> str:
        s = self._struct()
        return f"AxisAngle(x={s.axis.x}, y={s.axis.y}, z={s.axis.z}, theta={s.theta})"
