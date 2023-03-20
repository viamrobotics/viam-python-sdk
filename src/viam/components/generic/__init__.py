import viam.gen.component.generic.v1.generic_pb2  # Need this import for Generic service descriptors to resolve
from viam.resource.registry import Registry, ResourceRegistration

from .client import GenericClient
from .generic import Generic
from .service import GenericService

__all__ = [
    "Generic",
]

Registry.register_subtype(
    ResourceRegistration(
        Generic,
        GenericService,
        lambda name, channel: GenericClient(name, channel),
    )
)
