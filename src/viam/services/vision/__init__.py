from viam.resource.registry import Registry, ResourceRegistration
from viam.services.vision.service import VisionRPCService

from .client import Classification, Detection, VisionClient
from .vision import Vision, CaptureAllRequest, CaptureAllResult

__all__ = [
    "CaptureAllRequest",
    "CaptureAllResult",
    "Classification",
    "Detection",
    "VisionClient",
    "Vision",
]

Registry.register_subtype(ResourceRegistration(Vision, VisionRPCService, lambda name, channel: VisionClient(name, channel)))
