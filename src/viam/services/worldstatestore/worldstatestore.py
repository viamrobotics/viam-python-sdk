import abc
from typing import Any, AsyncGenerator, Final, List, Mapping, Optional

from viam.proto.common import Transform
from viam.proto.service.worldstatestore import (
    StreamTransformChangesResponse,
)
from viam.resource.types import API, RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE

from ..service_base import ServiceBase


class WorldStateStore(ServiceBase):
    """WorldStateStore is a Viam service that manages world state transforms.

    The WorldStateStore service provides functionality to store, retrieve, and stream
    changes to world state transforms, which represent the pose of objects in different
    reference frames. This functionality can be used to create custom visualizations of the world state.

    For more information, see `WorldStateStore service <https://docs.viam.com/dev/reference/apis/services/world-state-store/>`_.
    """

    API: Final = API(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, "world_state_store"
    )

    @abc.abstractmethod
    async def list_uuids(
        self,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> List[bytes]:
        """List all world state transform UUIDs.

        ::

            worldstatestore = WorldStateStoreClient.from_robot(robot=machine, name="builtin")

            uuids = await worldstatestore.list_uuids()

        Returns:
            List[bytes]: A list of transform UUIDs
        """
        ...

    @abc.abstractmethod
    async def get_transform(
        self,
        uuid: bytes,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> Transform:
        """Get a world state transform by UUID.

        ::

            worldstatestore = WorldStateStoreClient.from_robot(robot=machine, name="builtin")

            transform = await worldstatestore.get_transform(uuid=b"some-uuid")

        Args:
            uuid (bytes): The UUID of the transform to retrieve

        Returns:
            Transform: The requested transform
        """
        ...

    @abc.abstractmethod
    async def stream_transform_changes(
        self,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> AsyncGenerator[StreamTransformChangesResponse, None]:
        """Stream changes to world state transforms.

        ::

            worldstatestore = WorldStateStoreClient.from_robot(robot=machine, name="builtin")

            async for change in worldstatestore.stream_transform_changes():
                print(f"Transform {change.transform.uuid} {change.change_type}")

        Returns:
            AsyncGenerator[StreamTransformChangesResponse, None]: A stream of transform changes
        """
        ...
