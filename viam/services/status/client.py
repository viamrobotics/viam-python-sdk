from typing import Dict, List, Optional

from grpclib.client import Channel
from viam.components import ComponentType
from viam.proto.api.service.status import (GetStatusRequest, GetStatusResponse,
                                           StatusServiceStub)
from viam.utils import resource_name_for_component_name_type


class StatusClient:

    def __init__(self, channel: Channel) -> None:
        self.client = StatusServiceStub(channel)

    async def get_status(
        self,
        components: Optional[Dict[str, List[ComponentType]]] = None
    ):
        """
        Get the status of the robot's components. You can optionally
        provide a mapping of the components for which you want statuses.

        Args:
            components (Optional[Dict[str, List[ComponentType]]]):
                Optional mapping of components for which you want statuses.
                Key: the name of the component
                Value: an array of `ComponentType` this component conforms to
                Example: { 'left': [ComponentType.MOTOR] }
        """
        names = components if components is not None else {}
        resource_names = []
        for name, types in names.items():
            for t in types:
                resource_names.append(
                    resource_name_for_component_name_type(name, t)
                )
        request = GetStatusRequest(resource_names=resource_names)
        response: GetStatusResponse = await self.client.GetStatus(request)
        return list(response.status)
