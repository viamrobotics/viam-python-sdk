from viam.resource.registry import ComponentRegistration, Registry

from .camera import Camera, DistortionParameters, IntrinsicParameters, RawImage
from .client import CameraClient
from .service import CameraService

__all__ = [
    "Camera",
    "IntrinsicParameters",
    "DistortionParameters",
    "RawImage",
]

Registry.register_subtype(
    ComponentRegistration(
        Camera,
        CameraService,
        lambda name, channel: CameraClient(name, channel),
    )
)
