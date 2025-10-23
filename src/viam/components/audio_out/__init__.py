from viam.resource.registry import Registry, ResourceRegistration

from viam.proto.common import AudioInfo
from viam.audio_codecs import AudioCodec
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
