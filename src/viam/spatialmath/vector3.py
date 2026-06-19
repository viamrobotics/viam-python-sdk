import weakref
from typing import List

from . import _ffi


class Vector3:
    """A 3-vector backed by the rust-utils spatialmath FFI."""

    __slots__ = ("_handle", "__weakref__")

    def __init__(self, x: float, y: float, z: float):
        lib = _ffi.lib()
        self._handle = _ffi.check(lib.viam_new_vector3(float(x), float(y), float(z)))
        weakref.finalize(self, lib.viam_free_vector_memory, self._handle)

    @classmethod
    def _from_handle(cls, handle) -> "Vector3":
        obj = cls.__new__(cls)
        obj._handle = _ffi.check(handle)
        weakref.finalize(obj, _ffi.lib().viam_free_vector_memory, obj._handle)
        return obj

    def _components(self) -> List[float]:
        lib = _ffi.lib()
        return _ffi.read_components(lib.viam_vector_get_components, self._handle, 3, lib.viam_free_vector_components)

    @property
    def x(self) -> float:
        return self._components()[0]

    @property
    def y(self) -> float:
        return self._components()[1]

    @property
    def z(self) -> float:
        return self._components()[2]

    def dot(self, other: "Vector3") -> float:
        return _ffi.lib().viam_vector_dot_product(self._handle, other._handle)

    def cross(self, other: "Vector3") -> "Vector3":
        return Vector3._from_handle(_ffi.lib().viam_vector_cross_product(self._handle, other._handle))

    def __add__(self, other: "Vector3") -> "Vector3":
        return Vector3._from_handle(_ffi.lib().viam_vector_add(self._handle, other._handle))

    def __sub__(self, other: "Vector3") -> "Vector3":
        return Vector3._from_handle(_ffi.lib().viam_vector_subtract(self._handle, other._handle))

    def scaled(self, factor: float) -> "Vector3":
        return Vector3._from_handle(_ffi.lib().viam_vector_get_scaled(self._handle, float(factor)))

    def normalized(self) -> "Vector3":
        return Vector3._from_handle(_ffi.lib().viam_vector_get_normalized(self._handle))

    def __repr__(self) -> str:
        c = self._components()
        return f"Vector3(x={c[0]}, y={c[1]}, z={c[2]})"
