import ctypes
import weakref
from typing import List, Sequence

from . import _ffi


class RotationMatrix:
    """A 3x3 rotation matrix backed by the spatialmath FFI.

    ``elements`` is a 9-value list in row-major order:
    ``elements[3*row + col]`` is the entry at (row, col).
    """

    __slots__ = ("_handle", "__weakref__")

    def __init__(self, elements: Sequence[float]):
        if len(elements) != 9:
            raise ValueError("RotationMatrix requires exactly 9 elements")
        lib = _ffi.lib()
        raw = (ctypes.c_double * 9)(*[float(elements[idx]) for idx in range(9)])
        self._handle = _ffi.check(lib.viam_new_rotation_matrix(ctypes.byref(raw)))
        weakref.finalize(self, lib.viam_free_rotation_matrix_memory, self._handle)

    @classmethod
    def _from_handle(cls, handle) -> "RotationMatrix":
        obj = cls.__new__(cls)
        obj._handle = _ffi.check(handle)
        weakref.finalize(obj, _ffi.lib().viam_free_rotation_matrix_memory, obj._handle)
        return obj

    @property
    def elements(self) -> List[float]:
        lib = _ffi.lib()
        return _ffi.read_components(
            lib.viam_rotation_matrix_get_elements, self._handle, 9, lib.viam_free_rotation_matrix_elements
        )

    def to_quaternion(self):
        from .quaternion import Quaternion

        return Quaternion._from_handle(_ffi.lib().viam_quaternion_from_rotation_matrix(self._handle))

    def __repr__(self) -> str:
        return f"RotationMatrix({self.elements})"
