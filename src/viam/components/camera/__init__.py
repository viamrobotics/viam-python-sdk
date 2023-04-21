from viam.media.video import RawImage
from viam.proto.component.camera import DistortionParameters, IntrinsicParameters
from viam.resource.registry import ResourceRegistration, Registry

from .camera import Camera
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
