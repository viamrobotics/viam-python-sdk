from viam.components import KinematicsReturn
from viam.proto.common import KinematicsFileFormat, Pose
from viam.proto.component.arm import JointPositions, MoveOptions
from viam.resource.registry import Registry, ResourceRegistration

from .arm import Arm
from .client import ArmClient
from .service import ArmRPCService

__all__ = [
    "Arm",
    "JointPositions",
    "KinematicsFileFormat",
    "KinematicsReturn",
    "MoveOptions",
    "Pose",
]

Registry.register_api(ResourceRegistration(Arm, ArmRPCService, lambda name, channel: ArmClient(name, channel)))
