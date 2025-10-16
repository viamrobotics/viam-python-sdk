from viam.resource.registry import Registry, ResourceRegistration

from .audio_in import AudioIn
from .client import AudioInClient
from .service import AudioInRPCService

# Export the AudioResponse type alias for external use
AudioResponse = AudioIn.AudioResponse


__all__ = [
    "AudioIn",
    "AudioResponse",
]


Registry.register_api(
    ResourceRegistration(
        AudioIn,
        AudioInRPCService,
        lambda name, channel: AudioInClient(name, channel),
    )
)
