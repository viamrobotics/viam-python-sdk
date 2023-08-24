import viam.gen.component.generic.v1.generic_pb2  # Need this import for Generic service descriptors to resolve
from viam.resource.registry import Registry, ResourceRegistration

from .client import GenericClient
from .generic import Generic
from .service import GenericRPCService

__all__ = [
    "Generic",
]

Registry.register_subtype(
    ResourceRegistration(
        Generic,
        GenericRPCService,
        lambda name, channel: GenericClient(name, channel),
    )
)
