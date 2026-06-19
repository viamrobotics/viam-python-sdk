import ctypes
import weakref
from typing import List, Sequence

from . import _ffi

# nalgebra Matrix3 is column-major; this permutation transposes between the
# library's column-major storage and our row-major `elements`. It is its own
# inverse, so the same map serves both reading and constructing.
_TRANSPOSE = (0, 3, 6, 1, 4, 7, 2, 5, 8)


class RotationMatrix:
    """A 3x3 rotation matrix backed by the spatialmath FFI.

    ``elements`` is row-major (row 0, row 1, row 2), matching the Go SDK and
    standard matrix convention. The underlying nalgebra storage is column-major;
    construction and readback transpose between the two.
    """

    __slots__ = ("_handle", "__weakref__")

    def __init__(self, elements: Sequence[float]):
        if len(elements) != 9:
            raise ValueError("RotationMatrix requires exactly 9 elements")
        lib = _ffi.lib()
        # transpose row-major input -> column-major for nalgebra Matrix3::from_vec
        colmajor = (ctypes.c_double * 9)(*[float(elements[_TRANSPOSE[idx]]) for idx in range(9)])
        self._handle = _ffi.check(lib.viam_new_rotation_matrix(ctypes.byref(colmajor)))
        weakref.finalize(self, lib.viam_free_rotation_matrix_memory, self._handle)

    @classmethod
    def _from_handle(cls, handle) -> "RotationMatrix":
        obj = cls.__new__(cls)
        obj._handle = _ffi.check(handle)
        weakref.finalize(obj, _ffi.lib().viam_free_rotation_matrix_memory, obj._handle)
        return obj

    @property
    def elements(self) -> List[float]:
        s = _ffi.read_struct(self._handle, _ffi._Rotation3Struct)
        # transpose column-major storage -> row-major
        return [s.m[_TRANSPOSE[idx]] for idx in range(9)]

    def to_quaternion(self):
        from .quaternion import Quaternion

        return Quaternion._from_handle(_ffi.lib().viam_quaternion_from_rotation_matrix(self._handle))

    def __repr__(self) -> str:
        return f"RotationMatrix({self.elements})"
