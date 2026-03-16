import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.api.annotations_pb2
import google.protobuf.struct_pb2
from .... import service

class NavigationServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetMode(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.GetModeRequest, service.navigation.v1.navigation_pb2.GetModeResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SetMode(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.SetModeRequest, service.navigation.v1.navigation_pb2.SetModeResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetLocation(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.GetLocationRequest, service.navigation.v1.navigation_pb2.GetLocationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetWaypoints(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.GetWaypointsRequest, service.navigation.v1.navigation_pb2.GetWaypointsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AddWaypoint(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.AddWaypointRequest, service.navigation.v1.navigation_pb2.AddWaypointResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RemoveWaypoint(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.RemoveWaypointRequest, service.navigation.v1.navigation_pb2.RemoveWaypointResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetObstacles(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.GetObstaclesRequest, service.navigation.v1.navigation_pb2.GetObstaclesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetPaths(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.GetPathsRequest, service.navigation.v1.navigation_pb2.GetPathsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetProperties(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.GetPropertiesRequest, service.navigation.v1.navigation_pb2.GetPropertiesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.service.navigation.v1.NavigationService/GetMode': grpclib.const.Handler(self.GetMode, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.GetModeRequest, service.navigation.v1.navigation_pb2.GetModeResponse), '/viam.service.navigation.v1.NavigationService/SetMode': grpclib.const.Handler(self.SetMode, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.SetModeRequest, service.navigation.v1.navigation_pb2.SetModeResponse), '/viam.service.navigation.v1.NavigationService/GetLocation': grpclib.const.Handler(self.GetLocation, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.GetLocationRequest, service.navigation.v1.navigation_pb2.GetLocationResponse), '/viam.service.navigation.v1.NavigationService/GetWaypoints': grpclib.const.Handler(self.GetWaypoints, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.GetWaypointsRequest, service.navigation.v1.navigation_pb2.GetWaypointsResponse), '/viam.service.navigation.v1.NavigationService/AddWaypoint': grpclib.const.Handler(self.AddWaypoint, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.AddWaypointRequest, service.navigation.v1.navigation_pb2.AddWaypointResponse), '/viam.service.navigation.v1.NavigationService/RemoveWaypoint': grpclib.const.Handler(self.RemoveWaypoint, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.RemoveWaypointRequest, service.navigation.v1.navigation_pb2.RemoveWaypointResponse), '/viam.service.navigation.v1.NavigationService/GetObstacles': grpclib.const.Handler(self.GetObstacles, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.GetObstaclesRequest, service.navigation.v1.navigation_pb2.GetObstaclesResponse), '/viam.service.navigation.v1.NavigationService/GetPaths': grpclib.const.Handler(self.GetPaths, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.GetPathsRequest, service.navigation.v1.navigation_pb2.GetPathsResponse), '/viam.service.navigation.v1.NavigationService/GetProperties': grpclib.const.Handler(self.GetProperties, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.GetPropertiesRequest, service.navigation.v1.navigation_pb2.GetPropertiesResponse), '/viam.service.navigation.v1.NavigationService/DoCommand': grpclib.const.Handler(self.DoCommand, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)}

class UnimplementedNavigationServiceBase(NavigationServiceBase):

    async def GetMode(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.GetModeRequest, service.navigation.v1.navigation_pb2.GetModeResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def SetMode(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.SetModeRequest, service.navigation.v1.navigation_pb2.SetModeResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetLocation(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.GetLocationRequest, service.navigation.v1.navigation_pb2.GetLocationResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetWaypoints(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.GetWaypointsRequest, service.navigation.v1.navigation_pb2.GetWaypointsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def AddWaypoint(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.AddWaypointRequest, service.navigation.v1.navigation_pb2.AddWaypointResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def RemoveWaypoint(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.RemoveWaypointRequest, service.navigation.v1.navigation_pb2.RemoveWaypointResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetObstacles(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.GetObstaclesRequest, service.navigation.v1.navigation_pb2.GetObstaclesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetPaths(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.GetPathsRequest, service.navigation.v1.navigation_pb2.GetPathsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetProperties(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.GetPropertiesRequest, service.navigation.v1.navigation_pb2.GetPropertiesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class NavigationServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetMode = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/GetMode', service.navigation.v1.navigation_pb2.GetModeRequest, service.navigation.v1.navigation_pb2.GetModeResponse)
        self.SetMode = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/SetMode', service.navigation.v1.navigation_pb2.SetModeRequest, service.navigation.v1.navigation_pb2.SetModeResponse)
        self.GetLocation = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/GetLocation', service.navigation.v1.navigation_pb2.GetLocationRequest, service.navigation.v1.navigation_pb2.GetLocationResponse)
        self.GetWaypoints = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/GetWaypoints', service.navigation.v1.navigation_pb2.GetWaypointsRequest, service.navigation.v1.navigation_pb2.GetWaypointsResponse)
        self.AddWaypoint = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/AddWaypoint', service.navigation.v1.navigation_pb2.AddWaypointRequest, service.navigation.v1.navigation_pb2.AddWaypointResponse)
        self.RemoveWaypoint = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/RemoveWaypoint', service.navigation.v1.navigation_pb2.RemoveWaypointRequest, service.navigation.v1.navigation_pb2.RemoveWaypointResponse)
        self.GetObstacles = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/GetObstacles', service.navigation.v1.navigation_pb2.GetObstaclesRequest, service.navigation.v1.navigation_pb2.GetObstaclesResponse)
        self.GetPaths = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/GetPaths', service.navigation.v1.navigation_pb2.GetPathsRequest, service.navigation.v1.navigation_pb2.GetPathsResponse)
        self.GetProperties = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/GetProperties', service.navigation.v1.navigation_pb2.GetPropertiesRequest, service.navigation.v1.navigation_pb2.GetPropertiesResponse)
        self.DoCommand = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/DoCommand', common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)