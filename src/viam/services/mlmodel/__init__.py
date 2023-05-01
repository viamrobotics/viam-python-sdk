from viam.proto.service.mlmodel import File, LabelType, Metadata, TensorInfo
from viam.resource.registry import Registry, ResourceRegistration

from .client import MLModelServiceClient
from .mlmodel import MLModelService
from .service import MLModelServiceRPCService

__all__ = ["File", "LabelType", "Metadata", "MLModelService", "MLModelServiceClient", "TensorInfo"]

Registry.register_subtype(
    ResourceRegistration(MLModelService, MLModelServiceRPCService, lambda name, channel: MLModelServiceClient(name, channel))
)
