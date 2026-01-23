from typing import Mapping, Tuple, Union

from viam.proto.common import KinematicsFileFormat, Mesh

KinematicsReturn = Union[
    Tuple[KinematicsFileFormat.ValueType, bytes],
    Tuple[KinematicsFileFormat.ValueType, bytes, Mapping[str, Mesh]],
]

__all__ = [
    "KinematicsReturn",
]
