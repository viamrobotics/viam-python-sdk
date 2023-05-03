from viam.proto.service.mlmodel import File, LabelType, Metadata, TensorInfo
from viam.resource.registry import Registry, ResourceRegistration

from .client import MLModelClient
from .mlmodel import MLModel
from .service import MLModelRPCService

__all__ = ["File", "LabelType", "Metadata", "MLModel", "MLModelClient", "TensorInfo"]

Registry.register_subtype(ResourceRegistration(MLModel, MLModelRPCService, lambda name, channel: MLModelClient(name, channel)))
