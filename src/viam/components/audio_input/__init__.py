from viam.resource.registry import ComponentRegistration, Registry

from .audio_input import AudioInput
from .client import AudioInputClient
from .service import AudioInputService

__all__ = [
    "AudioInput",
]


Registry.register_subtype(
    ComponentRegistration(
        AudioInput,
        AudioInputService,
        lambda name, channel: AudioInputClient(name, channel),
    )
)
