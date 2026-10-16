from typing import Mapping, Tuple, Union

from viam.proto.common import KinematicModel, KinematicsFileFormat, Mesh

KinematicsReturn = Union[
    Tuple[KinematicsFileFormat.ValueType, bytes],
    Tuple[KinematicsFileFormat.ValueType, bytes, Mapping[str, Mesh]],
    Tuple[KinematicsFileFormat.ValueType, bytes, Mapping[str, Mesh], KinematicModel],
]

__all__ = [
    "KinematicsReturn",
]
