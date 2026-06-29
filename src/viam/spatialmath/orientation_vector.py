import math
import weakref
from typing import List

from viam.proto.common import Orientation

from . import _ffi


class OrientationVector:
    """An orientation vector (o_x, o_y, o_z, theta) backed by the spatialmath FFI.

    ``theta`` is in RADIANS for this class. The proto bridge converts to/from the proto's degrees.
    """

    __slots__ = ("_handle", "__weakref__")

    def __init__(self, o_x: float, o_y: float, o_z: float, theta: float):
        lib = _ffi.lib()
        self._handle = _ffi.check(lib.viam_new_orientation_vector(float(o_x), float(o_y), float(o_z), float(theta)))
        weakref.finalize(self, lib.viam_free_orientation_vector_memory, self._handle)

    @classmethod
    def _from_handle(cls, handle) -> "OrientationVector":
        obj = cls.__new__(cls)
        obj._handle = _ffi.check(handle)
        weakref.finalize(obj, _ffi.lib().viam_free_orientation_vector_memory, obj._handle)
        return obj

    @classmethod
    def from_proto(cls, proto: Orientation) -> "OrientationVector":
        return cls(proto.o_x, proto.o_y, proto.o_z, math.radians(proto.theta))

    def to_proto(self) -> Orientation:
        c = self._components()
        return Orientation(o_x=c[0], o_y=c[1], o_z=c[2], theta=math.degrees(c[3]))

    def _components(self) -> List[float]:
        lib = _ffi.lib()
        return _ffi.read_components(
            lib.viam_orientation_vector_get_components, self._handle, 4, lib.viam_free_orientation_vector_components
        )

    @property
    def o_x(self) -> float:
        return self._components()[0]

    @property
    def o_y(self) -> float:
        return self._components()[1]

    @property
    def o_z(self) -> float:
        return self._components()[2]

    @property
    def theta(self) -> float:
        return self._components()[3]

    def to_quaternion(self):
        from .quaternion import Quaternion

        return Quaternion._from_handle(_ffi.lib().viam_quaternion_from_orientation_vector(self._handle))

    def __repr__(self) -> str:
        c = self._components()
        return f"OrientationVector(o_x={c[0]}, o_y={c[1]}, o_z={c[2]}, theta={c[3]})"
