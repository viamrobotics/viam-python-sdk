from viam.resource.registry import Registry, ResourceRegistration

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
