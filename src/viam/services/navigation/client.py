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
    GetWaypointsRequest,
    GetWaypointsResponse,
    NavigationServiceStub,
    RemoveWaypointRequest,
    SetModeRequest,
)
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.utils import ValueTypes, dict_to_struct, struct_to_dict

from . import GeoObstacle, GeoPoint, Mode, Waypoint
from .navigation import Navigation


class NavigationClient(Navigation, ReconfigurableResourceRPCClientBase):
    """
    Connect to the NavigationService, which allows the robot to create a map of its surroundings and find its location in that map.
    """

    client: NavigationServiceStub

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = NavigationServiceStub(channel)
        super().__init__(name)

    async def get_location(self, *, timeout: Optional[float] = None) -> GeoPoint:
        request = GetLocationRequest(name=self.name)
        response: GetLocationResponse = await self.client.GetLocation(request, timeout=timeout)
        return response.location

    async def get_obstacles(self, *, timeout: Optional[float] = None) -> List[GeoObstacle]:
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

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None) -> Mapping[str, ValueTypes]:
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout)
        return struct_to_dict(response.result)
