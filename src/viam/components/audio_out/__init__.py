from viam.media.audio import AudioCodec
from viam.proto.common import AudioInfo
from viam.resource.registry import Registry, ResourceRegistration

from .audio_out import AudioOut
from .client import AudioOutClient
from .service import AudioOutRPCService

__all__ = [
    "AudioOut",
    "AudioInfo",
    "AudioCodec",
]

Registry.register_api(
    ResourceRegistration(
        AudioOut,
        AudioOutRPCService,
        lambda name, channel: AudioOutClient(name, channel),
    )
)
