from viam.registry import ComponentRegistration, Registry

from .base import Base, Vector3
from .client import BaseClient
from .service import BaseService

__all__ = [
    'Base',
    'BaseClient',
    'Vector3'
]

Registry.register(
    ComponentRegistration(
        Base,
        'base',
        BaseService,
        lambda name, channel: BaseClient(name, channel),
    )
)
