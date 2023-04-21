from viam.proto.service.vision import Classification, Detection

from .client import VisionServiceClient, VisModelConfig, VisModelType

__all__ = [
    "Classification",
    "Detection",
    "VisionServiceClient",
    "VisModelConfig",
    "VisModelType",
]
