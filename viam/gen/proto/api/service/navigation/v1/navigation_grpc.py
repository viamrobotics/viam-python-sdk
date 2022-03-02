import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
from ...... import proto
from ...... import proto

class NavigationServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetMode(self, stream: 'grpclib.server.Stream[proto.api.service.navigation.v1.navigation_pb2.GetModeRequest, proto.api.service.navigation.v1.navigation_pb2.GetModeResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SetMode(self, stream: 'grpclib.server.Stream[proto.api.service.navigation.v1.navigation_pb2.SetModeRequest, proto.api.service.navigation.v1.navigation_pb2.SetModeResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetLocation(self, stream: 'grpclib.server.Stream[proto.api.service.navigation.v1.navigation_pb2.GetLocationRequest, proto.api.service.navigation.v1.navigation_pb2.GetLocationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetWaypoints(self, stream: 'grpclib.server.Stream[proto.api.service.navigation.v1.navigation_pb2.GetWaypointsRequest, proto.api.service.navigation.v1.navigation_pb2.GetWaypointsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AddWaypoint(self, stream: 'grpclib.server.Stream[proto.api.service.navigation.v1.navigation_pb2.AddWaypointRequest, proto.api.service.navigation.v1.navigation_pb2.AddWaypointResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RemoveWaypoint(self, stream: 'grpclib.server.Stream[proto.api.service.navigation.v1.navigation_pb2.RemoveWaypointRequest, proto.api.service.navigation.v1.navigation_pb2.RemoveWaypointResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.service.navigation.v1.NavigationService/GetMode': grpclib.const.Handler(self.GetMode, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.navigation.v1.navigation_pb2.GetModeRequest, proto.api.service.navigation.v1.navigation_pb2.GetModeResponse), '/proto.api.service.navigation.v1.NavigationService/SetMode': grpclib.const.Handler(self.SetMode, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.navigation.v1.navigation_pb2.SetModeRequest, proto.api.service.navigation.v1.navigation_pb2.SetModeResponse), '/proto.api.service.navigation.v1.NavigationService/GetLocation': grpclib.const.Handler(self.GetLocation, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.navigation.v1.navigation_pb2.GetLocationRequest, proto.api.service.navigation.v1.navigation_pb2.GetLocationResponse), '/proto.api.service.navigation.v1.NavigationService/GetWaypoints': grpclib.const.Handler(self.GetWaypoints, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.navigation.v1.navigation_pb2.GetWaypointsRequest, proto.api.service.navigation.v1.navigation_pb2.GetWaypointsResponse), '/proto.api.service.navigation.v1.NavigationService/AddWaypoint': grpclib.const.Handler(self.AddWaypoint, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.navigation.v1.navigation_pb2.AddWaypointRequest, proto.api.service.navigation.v1.navigation_pb2.AddWaypointResponse), '/proto.api.service.navigation.v1.NavigationService/RemoveWaypoint': grpclib.const.Handler(self.RemoveWaypoint, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.navigation.v1.navigation_pb2.RemoveWaypointRequest, proto.api.service.navigation.v1.navigation_pb2.RemoveWaypointResponse)}

class NavigationServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetMode = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.navigation.v1.NavigationService/GetMode', proto.api.service.navigation.v1.navigation_pb2.GetModeRequest, proto.api.service.navigation.v1.navigation_pb2.GetModeResponse)
        self.SetMode = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.navigation.v1.NavigationService/SetMode', proto.api.service.navigation.v1.navigation_pb2.SetModeRequest, proto.api.service.navigation.v1.navigation_pb2.SetModeResponse)
        self.GetLocation = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.navigation.v1.NavigationService/GetLocation', proto.api.service.navigation.v1.navigation_pb2.GetLocationRequest, proto.api.service.navigation.v1.navigation_pb2.GetLocationResponse)
        self.GetWaypoints = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.navigation.v1.NavigationService/GetWaypoints', proto.api.service.navigation.v1.navigation_pb2.GetWaypointsRequest, proto.api.service.navigation.v1.navigation_pb2.GetWaypointsResponse)
        self.AddWaypoint = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.navigation.v1.NavigationService/AddWaypoint', proto.api.service.navigation.v1.navigation_pb2.AddWaypointRequest, proto.api.service.navigation.v1.navigation_pb2.AddWaypointResponse)
        self.RemoveWaypoint = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.navigation.v1.NavigationService/RemoveWaypoint', proto.api.service.navigation.v1.navigation_pb2.RemoveWaypointRequest, proto.api.service.navigation.v1.navigation_pb2.RemoveWaypointResponse)