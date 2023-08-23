from datetime import datetime
from typing import List, Mapping, Optional

from grpclib.client import Channel

from viam.proto.common import DoCommandRequest, DoCommandResponse
from viam.proto.service.slam import (
    GetInternalStateRequest,
    GetInternalStateResponse,
    GetLatestMapInfoRequest,
    GetLatestMapInfoResponse,
    GetPointCloudMapRequest,
    GetPointCloudMapResponse,
    GetPositionRequest,
    GetPositionResponse,
    SLAMServiceStub,
)
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.utils import ValueTypes, dict_to_struct, struct_to_dict

from . import Pose
from .slam import SLAM


class SLAMClient(SLAM, ReconfigurableResourceRPCClientBase):
    """
    Connect to the SLAMService, which allows the robot to create a map of its surroundings and find its location in that map.
    """

    client: SLAMServiceStub

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = SLAMServiceStub(channel)
        super().__init__(name)

    async def get_position(self, *, timeout: Optional[float] = None) -> Pose:
        request = GetPositionRequest(name=self.name)
        response: GetPositionResponse = await self.client.GetPosition(request, timeout=timeout)
        return response.pose

    async def get_point_cloud_map(self, *, timeout: Optional[float] = None) -> List[GetPointCloudMapResponse]:
        request = GetPointCloudMapRequest(name=self.name)
        response: List[GetPointCloudMapResponse] = await self.client.GetPointCloudMap(request, timeout=timeout)
        return response

    async def get_internal_state(self, *, timeout: Optional[float] = None) -> List[GetInternalStateResponse]:
        request = GetInternalStateRequest(name=self.name)
        response: List[GetInternalStateResponse] = await self.client.GetInternalState(request, timeout=timeout)
        return response

    async def get_latest_map_info(self, *, timeout: Optional[float] = None) -> datetime:
        request = GetLatestMapInfoRequest(name=self.name)
        response: GetLatestMapInfoResponse = await self.client.GetLatestMapInfo(request, timeout=timeout)
        return response.last_map_update.ToDatetime()

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None) -> Mapping[str, ValueTypes]:
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout)
        return struct_to_dict(response.result)
