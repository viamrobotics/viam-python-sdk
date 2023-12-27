from grpclib.server import Stream

from viam.proto.common import DoCommandRequest, DoCommandResponse
from viam.proto.service.navigation import (
    AddWaypointRequest,
    AddWaypointResponse,
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
    NavigationServiceBase,
    RemoveWaypointRequest,
    RemoveWaypointResponse,
    SetModeRequest,
    SetModeResponse,
)
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.utils import dict_to_struct, struct_to_dict

from .navigation import Navigation


class NavigationRPCService(NavigationServiceBase, ResourceRPCServiceBase):
    """
    gRPC Service for a Navigation service
    """

    RESOURCE_TYPE = Navigation

    async def GetPaths(self, stream: Stream[GetPathsRequest, GetPathsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        navigation = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        paths = await navigation.get_paths(timeout=timeout)
        response = GetPathsResponse(paths=paths)
        await stream.send_message(response)

    async def GetLocation(self, stream: Stream[GetLocationRequest, GetLocationResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        navigation = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        location = await navigation.get_location(timeout=timeout)
        response = GetLocationResponse(location=location)
        await stream.send_message(response)

    async def GetObstacles(self, stream: Stream[GetObstaclesRequest, GetObstaclesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        navigation = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        obstacles = await navigation.get_obstacles(timeout=timeout)
        response = GetObstaclesResponse(obstacles=obstacles)
        await stream.send_message(response)

    async def GetWaypoints(self, stream: Stream[GetWaypointsRequest, GetWaypointsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        navigation = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        waypoints = await navigation.get_waypoints(timeout=timeout)
        response = GetWaypointsResponse(waypoints=waypoints)
        await stream.send_message(response)

    async def AddWaypoint(self, stream: Stream[AddWaypointRequest, AddWaypointResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        point = request.location
        navigation = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await navigation.add_waypoint(point, timeout=timeout)
        response = AddWaypointResponse()
        await stream.send_message(response)

    async def RemoveWaypoint(self, stream: Stream[RemoveWaypointRequest, RemoveWaypointResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        id = request.id
        navigation = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await navigation.remove_waypoint(id=id, timeout=timeout)
        response = RemoveWaypointResponse()
        await stream.send_message(response)

    async def GetMode(self, stream: Stream[GetModeRequest, GetModeResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        navigation = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        mode = await navigation.get_mode(timeout=timeout)
        response = GetModeResponse(mode=mode)
        await stream.send_message(response)

    async def SetMode(self, stream: Stream[SetModeRequest, SetModeResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        mode = request.mode
        navigation = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await navigation.set_mode(mode, timeout=timeout)
        response = SetModeResponse()
        await stream.send_message(response)

    async def GetProperties(self, stream: Stream[GetPropertiesRequest, GetPropertiesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        map_type = await navigation.get_properties(timeout=timeout)
        response = GetPropertiesResponse(map_type=map_type)
        await stream.send_message(response)

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await navigation.do_command(command=struct_to_dict(request.command), timeout=timeout, metadata=stream.metadata)
        response = DoCommandResponse(result=dict_to_struct(result))
        await stream.send_message(response)
