from viam.resource.registry import Registry, ResourceRegistration

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
    ResourceRegistration(
        Camera,
        CameraService,
        lambda name, channel: CameraClient(name, channel),
    )
)
