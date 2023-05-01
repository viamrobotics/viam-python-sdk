from viam.resource.registry import Registry, ResourceRegistration

from .camera import Camera, DistortionParameters, IntrinsicParameters, RawImage
from .client import CameraClient
from .service import CameraRPCService

__all__ = [
    "Camera",
    "IntrinsicParameters",
    "DistortionParameters",
    "RawImage",
]

Registry.register_subtype(
    ResourceRegistration(
        Camera,
        CameraRPCService,
        lambda name, channel: CameraClient(name, channel),
    )
)
