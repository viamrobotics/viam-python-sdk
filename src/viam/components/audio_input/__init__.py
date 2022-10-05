from viam.proto.component.audioinput import AudioChunk, AudioChunkInfo
from viam.registry import ComponentRegistration, Registry

from .audio_input import AudioInput
from .client import AudioInputClient
from .service import AudioInputService

__all__ = [
    "AudioChunk",
    "AudioChunkInfo",
    "AudioInput",
]


Registry.register(
    ComponentRegistration(
        AudioInput,
        "audio_input",
        AudioInputService,
        lambda name, channel: AudioInputClient(name, channel),
    )
)
