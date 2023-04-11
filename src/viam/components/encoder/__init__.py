from viam.proto.component.motor import Status as MotorStatus
from viam.proto.robot import Status
from viam.resource.registry import ResourceRegistration, Registry
from viam.utils import message_to_struct

from .client import EncoderClient
from .encoder import Encoder
from .service import EncoderService

__all__ = [
    "Encoder",
]


Registry.register_subtype(
    ResourceRegistration(
        Encoder,
        EncoderService,
        lambda name, channel: EncoderClient(name, channel),
    )
)
