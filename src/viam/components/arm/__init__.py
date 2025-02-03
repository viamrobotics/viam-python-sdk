from viam.proto.common import KinematicsFileFormat, Pose
from viam.proto.component.arm import JointPositions
from viam.resource.registry import Registry, ResourceRegistration

from .arm import Arm
from .client import ArmClient
from .service import ArmRPCService

__all__ = [
    "Arm",
    "JointPositions",
    "KinematicsFileFormat",
    "Pose",
]

Registry.register_api(ResourceRegistration(Arm, ArmRPCService, lambda name, channel: ArmClient(name, channel)))
