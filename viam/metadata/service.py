from typing import List
from grpclib.server import Stream
from viam.components.service_base import ComponentServiceBase
from viam.proto.api.common import ResourceName
from viam.proto.api.service.metadata import (
    MetadataServiceBase,
    ResourcesRequest, ResourcesResponse
)
from viam.utils import resource_names_for_component


class MetadataService(MetadataServiceBase, ComponentServiceBase):

    def _generate_metadata(self) -> List[ResourceName]:
        md: List[ResourceName] = []

        for component in self.manager.components.values():
            md.extend(resource_names_for_component(component))

        return md

    async def Resources(
        self,
        stream: Stream[ResourcesRequest, ResourcesResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        metadata = self._generate_metadata()
        response = ResourcesResponse(resources=metadata)
        await stream.send_message(response)
