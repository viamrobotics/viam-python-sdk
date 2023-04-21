from viam.resource.registry import Registry, ResourceRegistration

from .audio_input import AudioInput
from .client import AudioInputClient
from .service import AudioInputService

__all__ = [
    "AudioInput",
]


Registry.register_subtype(
    ResourceRegistration(
        AudioInput,
        AudioInputService,
        lambda name, channel: AudioInputClient(name, channel),
    )
)
