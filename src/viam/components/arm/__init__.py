import asyncio

from viam.proto.common import KinematicsFileFormat, Pose
from viam.proto.component.arm import JointPositions
from viam.proto.component.arm import Status as ArmStatus
from viam.proto.robot import Status
from viam.resource.registry import Registry, ResourceRegistration
from viam.utils import message_to_struct

from .arm import Arm
from .client import ArmClient
from .service import ArmRPCService

__all__ = [
    "Arm",
    "JointPositions",
    "KinematicsFileFormat",
    "Pose",
]


async def create_status(component: Arm) -> Status:
    (
        end_position,
        joint_positions,
        is_moving,
    ) = await asyncio.gather(
        component.get_end_position(),
        component.get_joint_positions(),
        component.is_moving(),
    )
    s = ArmStatus(
        end_position=end_position,
        joint_positions=joint_positions,
        is_moving=is_moving,
    )
    return Status(name=Arm.get_resource_name(component.name), status=message_to_struct(s))


Registry.register_subtype(ResourceRegistration(Arm, ArmRPCService, lambda name, channel: ArmClient(name, channel), create_status))
