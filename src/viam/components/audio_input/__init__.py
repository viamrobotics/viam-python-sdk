from viam.registry import ComponentRegistration, Registry

from .audio_input import Audio, AudioInput
from .client import AudioInputClient
from .service import AudioInputService

__all__ = [
    "AudioInput",
    "Audio",
]


Registry.register(
    ComponentRegistration(
        AudioInput,
        "audio_input",
        AudioInputService,
        lambda name, channel: AudioInputClient(name, channel),
    )
)
