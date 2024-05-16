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

    async def get_paths(self, *, timeout: Optional[float] = None) -> List[Path]:
        request = GetPathsRequest(name=self.name)
        response: GetPathsResponse = await self.client.GetPaths(request, timeout=timeout)
        return list(response.paths)

    async def get_location(self, *, timeout: Optional[float] = None) -> GeoPoint:
        request = GetLocationRequest(name=self.name)
        response: GetLocationResponse = await self.client.GetLocation(request, timeout=timeout)
        return response.location

    async def get_obstacles(self, *, timeout: Optional[float] = None) -> List[GeoGeometry]:
        request = GetObstaclesRequest(name=self.name)
        response: GetObstaclesResponse = await self.client.GetObstacles(request, timeout=timeout)
        return list(response.obstacles)

    async def get_waypoints(self, *, timeout: Optional[float] = None) -> List[Waypoint]:
        request = GetWaypointsRequest(name=self.name)
        response: GetWaypointsResponse = await self.client.GetWaypoints(request, timeout=timeout)
        return list(response.waypoints)

    async def add_waypoint(self, point: GeoPoint, *, timeout: Optional[float] = None):
        request = AddWaypointRequest(name=self.name, location=point)
        await self.client.AddWaypoint(request, timeout=timeout)

    async def remove_waypoint(self, id: str, *, timeout: Optional[float] = None):
        request = RemoveWaypointRequest(name=self.name, id=id)
        await self.client.RemoveWaypoint(request, timeout=timeout)

    async def get_mode(self, *, timeout: Optional[float] = None) -> Mode.ValueType:
        request = GetModeRequest(name=self.name)
        response: GetModeResponse = await self.client.GetMode(request, timeout=timeout)
        return response.mode

    async def set_mode(self, mode: Mode.ValueType, *, timeout: Optional[float] = None):
        request = SetModeRequest(name=self.name, mode=mode)
        await self.client.SetMode(request, timeout=timeout)

    async def get_properties(self, *, timeout: Optional[float] = None) -> MapType.ValueType:
        request = GetPropertiesRequest(name=self.name)
        response: GetPropertiesResponse = await self.client.GetProperties(request, timeout=timeout)
        return response.map_type

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **__) -> Mapping[str, ValueTypes]:
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout)
        return struct_to_dict(response.result)
