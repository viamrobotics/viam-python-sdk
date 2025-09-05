from viam.proto.service.worldstatestore import StreamTransformChangesResponse, TransformChangeType
from viam.resource.registry import Registry, ResourceRegistration

from .client import WorldStateStoreClient
from .service import WorldStateStoreService
from .worldstatestore import WorldStateStore

__all__ = [
    "WorldStateStore",
    "WorldStateStoreClient",
    "WorldStateStoreService",
    "StreamTransformChangesResponse",
    "TransformChangeType",
]

Registry.register_api(
    ResourceRegistration(WorldStateStore, WorldStateStoreService, lambda name, channel: WorldStateStoreClient(name, channel))
)
