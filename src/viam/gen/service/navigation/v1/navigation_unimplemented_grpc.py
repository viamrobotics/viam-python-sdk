import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.api.annotations_pb2
import google.protobuf.struct_pb2
from .... import service
from .navigation_grpc import NavigationServiceBase as _NavigationServiceBase

class UnimplementedNavigationServiceBase(_NavigationServiceBase):

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