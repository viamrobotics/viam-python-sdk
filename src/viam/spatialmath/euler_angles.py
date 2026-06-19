import weakref

from . import _ffi


class EulerAngles:
    """Euler angles (roll, pitch, yaw; Z-Y'-X" order) backed by the spatialmath FFI."""

    __slots__ = ("_handle", "__weakref__")

    def __init__(self, roll: float, pitch: float, yaw: float):
        lib = _ffi.lib()
        self._handle = _ffi.check(lib.viam_new_euler_angles(float(roll), float(pitch), float(yaw)))
        weakref.finalize(self, lib.viam_free_euler_angles_memory, self._handle)

    @classmethod
    def _from_handle(cls, handle) -> "EulerAngles":
        obj = cls.__new__(cls)
        obj._handle = _ffi.check(handle)
        weakref.finalize(obj, _ffi.lib().viam_free_euler_angles_memory, obj._handle)
        return obj

    def _struct(self):
        return _ffi.read_struct(self._handle, _ffi._EulerAnglesStruct)

    @property
    def roll(self) -> float:
        return self._struct().roll

    @property
    def pitch(self) -> float:
        return self._struct().pitch

    @property
    def yaw(self) -> float:
        return self._struct().yaw

    def to_quaternion(self):
        from .quaternion import Quaternion

        s = self._struct()
        return Quaternion._from_handle(_ffi.lib().viam_quaternion_from_euler_angles(s.roll, s.pitch, s.yaw))

    def __repr__(self) -> str:
        s = self._struct()
        return f"EulerAngles(roll={s.roll}, pitch={s.pitch}, yaw={s.yaw})"
