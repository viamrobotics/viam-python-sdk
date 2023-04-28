from viam.proto.service.mlmodel import Metadata
from viam.resource.registry import Registry, ResourceRegistration

from .client import MLModelServiceClient
from .mlmodel import MLModelService
from .service import MLModelServiceRPCService

__all__ = ["Metadata", "MLModelService", "MLModelServiceClient"]

Registry.register_subtype(
    ResourceRegistration(MLModelService, MLModelServiceRPCService, lambda name, channel: MLModelServiceClient(name, channel))
)
