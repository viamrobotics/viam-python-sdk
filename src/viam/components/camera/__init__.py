from viam.registry import ComponentRegistration, Registry

from .camera import Camera, DistortionParameters, IntrinsicParameters, RawImage
from .client import CameraClient
from .service import CameraService

__all__ = [
    "Camera",
    "IntrinsicParameters",
    "DistortionParameters",
    "RawImage",
]

Registry.register(
    ComponentRegistration(
        Camera,
        "camera",
        CameraService,
        lambda name, channel: CameraClient(name, channel),
    )
)
