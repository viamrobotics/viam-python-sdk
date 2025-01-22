from typing import Any, List, Mapping, Optional

from grpclib.client import Channel

from viam.proto.app.robot import ComponentConfig
from viam.proto.common import DoCommandRequest, DoCommandResponse
from viam.proto.service.discovery import (
    DiscoverResourcesRequest,
    DiscoverResourcesResponse,
    DiscoveryServiceStub,
)
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.utils import ValueTypes, dict_to_struct, struct_to_dict

from .discovery import Discovery


class DiscoveryClient(Discovery, ReconfigurableResourceRPCClientBase):
    """
    Connect to the Discovery service, which allows you to discover resources on a machine.
    """

    client: DiscoveryServiceStub

    def __init__(self, name: str, channel: Channel):
        super().__init__(name)
        self.channel = channel
        self.client = DiscoveryServiceStub(channel)

    async def discover_resources(
        self,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> List[ComponentConfig]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = DiscoverResourcesRequest(
            name=self.name,
            extra=dict_to_struct(extra),
        )
        response: DiscoverResourcesResponse = await self.client.DiscoverResources(request, timeout=timeout, metadata=md)
        return list(response.discoveries)

    async def do_command(
        self,
        command: Mapping[str, ValueTypes],
        *,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Mapping[str, ValueTypes]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout, metadata=md)
        return struct_to_dict(response.result)
