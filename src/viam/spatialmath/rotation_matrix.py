import ctypes
import weakref
from typing import List, Sequence

from . import _ffi


class RotationMatrix:
    """A 3x3 rotation matrix backed by the spatialmath FFI.

    ``elements`` is a 9-value list following Go ``rdk/spatialmath``'s row-major
    rotation-matrix convention (``elements[3*row + col]``). Construction and
    readback are both raw pass-throughs of the underlying nalgebra buffer, so
    they are mutually consistent by construction; that this raw buffer coincides
    with rdk's row-major convention is an empirical fact pinned by the golden
    parity tests (it is not a general column-major/row-major identity).
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
        s = _ffi.read_struct(self._handle, _ffi._Rotation3Struct)
        return [s.m[idx] for idx in range(9)]

    def to_quaternion(self):
        from .quaternion import Quaternion

        return Quaternion._from_handle(_ffi.lib().viam_quaternion_from_rotation_matrix(self._handle))

    def __repr__(self) -> str:
        return f"RotationMatrix({self.elements})"
