from viam.resource.registry import ComponentRegistration, Registry

from .client import GenericClient
from .generic import Generic
from .service import GenericService

__all__ = [
    "Generic",
]

Registry.register(
    ComponentRegistration(
        Generic,
        GenericService,
        lambda name, channel: GenericClient(name, channel),
    )
)
