from typing import List

from grpclib.client import Channel
from viam.proto.api.common import ResourceName
from viam.proto.api.service.metadata import (MetadataServiceStub,
                                             ResourcesRequest,
                                             ResourcesResponse)


class MetadataClient:

    def __init__(self, channel: Channel):
        self.client = MetadataServiceStub(channel)

    async def resources(self) -> List[ResourceName]:
        request = ResourcesRequest()
        response: ResourcesResponse = await self.client.Resources(request)
        return list(response.resources)
