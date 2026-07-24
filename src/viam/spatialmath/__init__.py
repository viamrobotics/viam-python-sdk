"""Pythonic spatial-math types backed by the shared Rust FFI (``libviam_rust_utils``).

Results are parity-tested against Go ``rdk/spatialmath`` using golden vectors.

**Angle convention** — ALL angles in these classes are in **radians**.
Euler angles follow the Z-Y'-X'' (yaw → pitch → roll) intrinsic convention.

**Proto bridge** — the ``from_proto`` / ``to_proto`` / ``from_pose`` / ``to_pose``
class methods convert to and from the Viam protobuf API, which uses **degrees**.
Those methods handle the conversion automatically; callers should not pre-convert.

Classes
-------
- :class:`AxisAngle`       — axis-angle representation (axis x/y/z + theta in radians)
- :class:`Axis`            — ``NamedTuple(x, y, z)`` returned by :attr:`AxisAngle.axis`
- :class:`EulerAngles`     — roll, pitch, yaw in radians (Z-Y'-X'' order)
- :class:`OrientationVector` — orientation vector (ox, oy, oz + theta in radians)
- :class:`Quaternion`      — unit quaternion (w, x, y, z)
- :class:`RotationMatrix`  — 3×3 rotation matrix
- :class:`Vector3`         — 3-D Cartesian vector (x, y, z)
"""

from .axis_angle import Axis, AxisAngle
from .euler_angles import EulerAngles
from .orientation_vector import OrientationVector
from .quaternion import Quaternion
from .rotation_matrix import RotationMatrix
from .vector3 import Vector3

__all__ = ["Axis", "AxisAngle", "EulerAngles", "OrientationVector", "Quaternion", "RotationMatrix", "Vector3"]
