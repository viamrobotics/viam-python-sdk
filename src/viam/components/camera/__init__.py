from viam.media.video import ViamImage
from viam.proto.component.camera import DistortionParameters, IntrinsicParameters
from viam.resource.registry import Registry, ResourceRegistration

from .camera import Camera
from .client import CameraClient
from .service import CameraRPCService

__all__ = [
    "Camera",
    "IntrinsicParameters",
    "DistortionParameters",
    "ViamImage",
]

Registry.register_subtype(
    ResourceRegistration(
        Camera,
        CameraRPCService,
        lambda name, channel: CameraClient(name, channel),
    )
)
