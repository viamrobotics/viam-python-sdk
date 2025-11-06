from viam.media.audio import AudioCodec
from viam.proto.common import AudioInfo
from viam.resource.registry import Registry, ResourceRegistration

from .audio_in import AudioIn
from .client import AudioInClient
from .service import AudioInRPCService

AudioResponse = AudioIn.AudioResponse

__all__ = [
    "AudioIn",
    "AudioResponse",
    "AudioInfo",
    "AudioCodec",
]

Registry.register_api(
    ResourceRegistration(
        AudioIn,
        AudioInRPCService,
        lambda name, channel: AudioInClient(name, channel),
    )
)
