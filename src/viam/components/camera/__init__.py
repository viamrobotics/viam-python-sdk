from viam.registry import ComponentRegistration, Registry

from .camera import Camera
from .client import CameraClient
from .service import CameraService

__all__ = [
    'Camera',
]

Registry.register(
    ComponentRegistration(
        Camera,
        'camera',
        CameraService,
        lambda name, channel: CameraClient(name, channel),
    )
)
