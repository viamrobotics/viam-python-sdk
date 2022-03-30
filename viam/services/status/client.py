from typing import List, Optional

from grpclib.client import Channel
from viam.proto.api.common import ResourceName
from viam.proto.api.service.status import (GetStatusRequest, GetStatusResponse,
                                           StatusServiceStub)


class StatusClient:

    def __init__(self, channel: Channel) -> None:
        self.client = StatusServiceStub(channel)

    async def get_status(
        self,
        components: Optional[List[ResourceName]] = None
    ):
        """
        Get the status of the robot's components. You can optionally
        provide a list of `ResourceName` for which you want statuses.

        Args:
            components (Optional[List[ResourceName]]): Optional list of
                `ResourceName` for components you want statuses.
        """
        names = components if components is not None else []
        request = GetStatusRequest(resource_names=names)
        response: GetStatusResponse = await self.client.GetStatus(request)
        return list(response.status)
