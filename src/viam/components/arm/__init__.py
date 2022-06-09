from viam.proto.api.component.arm import Status as ArmStatus
from viam.proto.api.robot import Status
from viam.registry import ComponentRegistration, Registry
from viam.utils import message_to_struct

from .arm import Arm, JointPositions, Pose, WorldState
from .client import ArmClient
from .service import ArmService

__all__ = [
    'Arm',
    'JointPositions',
    'Pose',
    'WorldState',
]


async def create_status(component: Arm) -> Status:
    s = ArmStatus(
        end_position=await component.get_end_position(),
        joint_positions=await component.get_joint_positions()
    )
    return Status(
        name=Arm.get_resource_name(component.name),
        status=message_to_struct(s)
    )

Registry.register(
    ComponentRegistration(
        Arm,
        'arm',
        ArmService,
        lambda name, channel: ArmClient(name, channel),
        create_status
    )
)
