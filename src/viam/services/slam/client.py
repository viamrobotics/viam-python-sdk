from typing import Final, List, Mapping, Optional

from grpclib.client import Channel

from viam.proto.common import DoCommandRequest, DoCommandResponse, Pose
from viam.proto.service.slam import (
    GetInternalStateRequest,
    GetInternalStateResponse,
    GetPointCloudMapRequest,
    GetPointCloudMapResponse,
    GetPositionRequest,
    GetPositionResponse,
    SLAMServiceStub,
)
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, Subtype
from viam.services.service_client_base import ServiceClientBase
from viam.utils import dict_to_struct, struct_to_dict, ValueTypes


class SLAMServiceClient(ServiceClientBase, ReconfigurableResourceRPCClientBase):
    """
    Connect to the SLAMService, which allows the robot to create a map of its surroundings and find its location in that map.
    """

    SUBTYPE: Final = Subtype(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, "slam")

    def __init__(self, name: str, channel: Channel):
        super().__init__(name, channel)
        self.client = SLAMServiceStub(channel)

    async def get_position(self, name: str, *, timeout: Optional[float] = None) -> Pose:
        request = GetPositionRequest(name=name)
        response: GetPositionResponse = await self.client.GetPosition(request, timeout=timeout)
        return response.pose

    async def get_point_cloud_map(self, name: str, *, timeout: Optional[float] = None) -> List[GetPointCloudMapResponse]:
        request = GetPointCloudMapRequest(name=name)
        response: List[GetPointCloudMapResponse] = await self.client.GetPointCloudMap(request, timeout=timeout)
        return response

    async def get_internal_state(self, name: str, *, timeout: Optional[float] = None) -> List[GetInternalStateResponse]:
        request = GetInternalStateRequest(name=name)
        response: List[GetInternalStateResponse] = await self.client.GetInternalState(request, timeout=timeout)
        return response

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None) -> Mapping[str, ValueTypes]:
        """Send/receive arbitrary commands

        Args:
            command (Dict[str, ValueTypes]): The command to execute

        Returns:
            Dict[str, ValueTypes]: Result of the executed command
        """
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout)
        return struct_to_dict(response.result)
