from viam.registry import ComponentRegistration, Registry

from .client import GripperClient
from .gripper import Gripper
from .service import GripperService

__all__ = [
    'Gripper',
]

Registry.register(
    ComponentRegistration(
        Gripper,
        'gripper',
        GripperService,
        lambda name, channel: GripperClient(name, channel),
    )
)
