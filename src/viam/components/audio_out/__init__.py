from viam.resource.registry import Registry, ResourceRegistration

from .audio_out import AudioOut
from .client import AudioOutClient
from .service import AudioOutRPCService

__all__ = [
    "AudioOut",
]

Registry.register_api(
    ResourceRegistration(
        AudioOut,
        AudioOutRPCService,
        lambda name, channel: AudioOutClient(name, channel),
    )
)