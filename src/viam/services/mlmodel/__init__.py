import warnings
from importlib import util

if util.find_spec("numpy") is None:
    warnings.warn(
        (
            """MLModel support in the Viam Python SDK requires the installation of an
additional dependency: numpy.  Update your package using the extra [mlmodel]
e.g. `pip install viam-sdk[mlmodel]` or the equivalent update in your dependency manager."""
        ),
    )
    raise ImportError

from viam.proto.service.mlmodel import File, LabelType, Metadata, TensorInfo
from viam.resource.registry import Registry, ResourceRegistration

from .client import MLModelClient
from .mlmodel import MLModel
from .service import MLModelRPCService

__all__ = ["File", "LabelType", "Metadata", "MLModel", "MLModelClient", "TensorInfo"]

Registry.register_subtype(
    ResourceRegistration(
        MLModel, MLModelRPCService, lambda name, channel: MLModelClient(name, channel)
    )
)
