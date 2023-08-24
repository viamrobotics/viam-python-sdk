from viam.resource.registry import Registry, ResourceRegistration

from .audio_input import AudioInput
from .client import AudioInputClient
from .service import AudioInputRPCService

__all__ = [
    "AudioInput",
]


Registry.register_subtype(
    ResourceRegistration(
        AudioInput,
        AudioInputRPCService,
        lambda name, channel: AudioInputClient(name, channel),
    )
)
