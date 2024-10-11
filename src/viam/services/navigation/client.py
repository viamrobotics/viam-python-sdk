from typing import List, Mapping, Optional

from grpclib.client import Channel

from viam.proto.common import DoCommandRequest, DoCommandResponse
from viam.proto.service.navigation import (
    AddWaypointRequest,
    GetLocationRequest,
    GetLocationResponse,
    GetModeRequest,
    GetModeResponse,
    GetObstaclesRequest,
    GetObstaclesResponse,
    GetPathsRequest,
    GetPathsResponse,
    GetPropertiesRequest,
    GetPropertiesResponse,
    GetWaypointsRequest,
    GetWaypointsResponse,
    NavigationServiceStub,
    Path,
    RemoveWaypointRequest,
    SetModeRequest,
)
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.utils import ValueTypes, dict_to_struct, struct_to_dict

from . import GeoGeometry, GeoPoint, MapType, Mode, Waypoint
from .navigation import Navigation


class NavigationClient(Navigation, ReconfigurableResourceRPCClientBase):
    """
    Connect to the NavigationService, which allows the robot to navigate to specified locations.
    """

    client: NavigationServiceStub

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = NavigationServiceStub(channel)
        super().__init__(name)

    async def get_paths(self, *, timeout: Optional[float] = None, **kwargs) -> List[Path]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetPathsRequest(name=self.name)
        response: GetPathsResponse = await self.client.GetPaths(request, timeout=timeout, metadata=md)
        return list(response.paths)

    async def get_location(self, *, timeout: Optional[float] = None, **kwargs) -> GeoPoint:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetLocationRequest(name=self.name)
        response: GetLocationResponse = await self.client.GetLocation(request, timeout=timeout, metadata=md)
        return response.location

    async def get_obstacles(self, *, timeout: Optional[float] = None, **kwargs) -> List[GeoGeometry]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetObstaclesRequest(name=self.name)
        response: GetObstaclesResponse = await self.client.GetObstacles(request, timeout=timeout, metadata=md)
        return list(response.obstacles)

    async def get_waypoints(self, *, timeout: Optional[float] = None, **kwargs) -> List[Waypoint]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetWaypointsRequest(name=self.name)
        response: GetWaypointsResponse = await self.client.GetWaypoints(request, timeout=timeout, metadata=md)
        return list(response.waypoints)

    async def add_waypoint(self, point: GeoPoint, *, timeout: Optional[float] = None, **kwargs):
        md = kwargs.get("metadata", self.Metadata()).proto
        request = AddWaypointRequest(name=self.name, location=point)
        await self.client.AddWaypoint(request, timeout=timeout, metadata=md)

    async def remove_waypoint(self, id: str, *, timeout: Optional[float] = None, **kwargs):
        md = kwargs.get("metadata", self.Metadata()).proto
        request = RemoveWaypointRequest(name=self.name, id=id)
        await self.client.RemoveWaypoint(request, timeout=timeout, metadata=md)

    async def get_mode(self, *, timeout: Optional[float] = None, **kwargs) -> Mode.ValueType:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetModeRequest(name=self.name)
        response: GetModeResponse = await self.client.GetMode(request, timeout=timeout, metadata=md)
        return response.mode

    async def set_mode(self, mode: Mode.ValueType, *, timeout: Optional[float] = None, **kwargs):
        md = kwargs.get("metadata", self.Metadata()).proto
        request = SetModeRequest(name=self.name, mode=mode)
        await self.client.SetMode(request, timeout=timeout, metadata=md)

    async def get_properties(self, *, timeout: Optional[float] = None, **kwargs) -> MapType.ValueType:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetPropertiesRequest(name=self.name)
        response: GetPropertiesResponse = await self.client.GetProperties(request, timeout=timeout, metadata=md)
        return response.map_type

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout, metadata=md)
        return struct_to_dict(response.result)
