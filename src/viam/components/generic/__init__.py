# needs this import for Generic service description
import viam.gen.component.generic.v1.generic_pb2
from viam.resource.registry import ResourceRegistration, Registry

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
