from viam.resource.registry import Registry, ResourceRegistration

from .client import EncoderClient
from .encoder import Encoder
from .service import EncoderRPCService

__all__ = [
    "Encoder",
]


Registry.register_subtype(
    ResourceRegistration(
        Encoder,
        EncoderRPCService,
        lambda name, channel: EncoderClient(name, channel),
    )
)
