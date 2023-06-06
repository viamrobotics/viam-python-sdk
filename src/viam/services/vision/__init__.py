from viam.resource.registry import Registry, ResourceRegistration
from viam.services.vision.service import VisionRPCService

from .client import Classification, Detection, VisionClient
from .vision import Vision

__all__ = [
    "Classification",
    "Detection",
    "VisionClient",
    "Vision",
]

Registry.register_subtype(ResourceRegistration(Vision, VisionRPCService, lambda name, channel: VisionClient(name, channel)))
