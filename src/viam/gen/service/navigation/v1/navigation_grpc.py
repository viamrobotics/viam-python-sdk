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
import google.protobuf.timestamp_pb2
from .... import service

class NavigationServiceBase(abc.ABC):

    @abc.abstractmethod
    async def AddLocation(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.AddLocationRequest, service.navigation.v1.navigation_pb2.AddLocationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetLocation(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.GetLocationRequest, service.navigation.v1.navigation_pb2.GetLocationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListLocations(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.ListLocationsRequest, service.navigation.v1.navigation_pb2.ListLocationsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateLocation(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.UpdateLocationRequest, service.navigation.v1.navigation_pb2.UpdateLocationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteLocation(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.DeleteLocationRequest, service.navigation.v1.navigation_pb2.DeleteLocationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AddRoute(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.AddRouteRequest, service.navigation.v1.navigation_pb2.AddRouteResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetRoute(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.GetRouteRequest, service.navigation.v1.navigation_pb2.GetRouteResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListRoutes(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.ListRoutesRequest, service.navigation.v1.navigation_pb2.ListRoutesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateRoute(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.UpdateRouteRequest, service.navigation.v1.navigation_pb2.UpdateRouteResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteRoute(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.DeleteRouteRequest, service.navigation.v1.navigation_pb2.DeleteRouteResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AddZone(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.AddZoneRequest, service.navigation.v1.navigation_pb2.AddZoneResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetZone(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.GetZoneRequest, service.navigation.v1.navigation_pb2.GetZoneResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListZones(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.ListZonesRequest, service.navigation.v1.navigation_pb2.ListZonesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateZone(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.UpdateZoneRequest, service.navigation.v1.navigation_pb2.UpdateZoneResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteZone(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.DeleteZoneRequest, service.navigation.v1.navigation_pb2.DeleteZoneResponse]') -> None:
        pass

    @abc.abstractmethod
    async def NavigateToLocation(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.NavigateToLocationRequest, service.navigation.v1.navigation_pb2.NavigateToLocationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def NavigateToPoint(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.NavigateToPointRequest, service.navigation.v1.navigation_pb2.NavigateToPointResponse]') -> None:
        pass

    @abc.abstractmethod
    async def NavigateRoute(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.NavigateRouteRequest, service.navigation.v1.navigation_pb2.NavigateRouteResponse]') -> None:
        pass

    @abc.abstractmethod
    async def PlanToPoint(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.PlanToPointRequest, service.navigation.v1.navigation_pb2.PlanToPointResponse]') -> None:
        pass

    @abc.abstractmethod
    async def PlanToLocation(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.PlanToLocationRequest, service.navigation.v1.navigation_pb2.PlanToLocationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ExecutePlan(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.ExecutePlanRequest, service.navigation.v1.navigation_pb2.ExecutePlanResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GoToLocation(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.GoToLocationRequest, service.navigation.v1.navigation_pb2.GoToLocationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GoToPoint(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.GoToPointRequest, service.navigation.v1.navigation_pb2.GoToPointResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Suspend(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.SuspendRequest, service.navigation.v1.navigation_pb2.SuspendResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Resume(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.ResumeRequest, service.navigation.v1.navigation_pb2.ResumeResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Cancel(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.CancelRequest, service.navigation.v1.navigation_pb2.CancelResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetPosition(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.GetPositionRequest, service.navigation.v1.navigation_pb2.GetPositionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetNavigationStatus(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.GetNavigationStatusRequest, service.navigation.v1.navigation_pb2.GetNavigationStatusResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetProperties(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.GetPropertiesRequest, service.navigation.v1.navigation_pb2.GetPropertiesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetCostmap(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.GetCostmapRequest, service.navigation.v1.navigation_pb2.GetCostmapResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetStatus(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetStatusRequest, common.v1.common_pb2.GetStatusResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.service.navigation.v1.NavigationService/AddLocation': grpclib.const.Handler(self.AddLocation, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.AddLocationRequest, service.navigation.v1.navigation_pb2.AddLocationResponse), '/viam.service.navigation.v1.NavigationService/GetLocation': grpclib.const.Handler(self.GetLocation, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.GetLocationRequest, service.navigation.v1.navigation_pb2.GetLocationResponse), '/viam.service.navigation.v1.NavigationService/ListLocations': grpclib.const.Handler(self.ListLocations, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.ListLocationsRequest, service.navigation.v1.navigation_pb2.ListLocationsResponse), '/viam.service.navigation.v1.NavigationService/UpdateLocation': grpclib.const.Handler(self.UpdateLocation, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.UpdateLocationRequest, service.navigation.v1.navigation_pb2.UpdateLocationResponse), '/viam.service.navigation.v1.NavigationService/DeleteLocation': grpclib.const.Handler(self.DeleteLocation, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.DeleteLocationRequest, service.navigation.v1.navigation_pb2.DeleteLocationResponse), '/viam.service.navigation.v1.NavigationService/AddRoute': grpclib.const.Handler(self.AddRoute, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.AddRouteRequest, service.navigation.v1.navigation_pb2.AddRouteResponse), '/viam.service.navigation.v1.NavigationService/GetRoute': grpclib.const.Handler(self.GetRoute, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.GetRouteRequest, service.navigation.v1.navigation_pb2.GetRouteResponse), '/viam.service.navigation.v1.NavigationService/ListRoutes': grpclib.const.Handler(self.ListRoutes, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.ListRoutesRequest, service.navigation.v1.navigation_pb2.ListRoutesResponse), '/viam.service.navigation.v1.NavigationService/UpdateRoute': grpclib.const.Handler(self.UpdateRoute, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.UpdateRouteRequest, service.navigation.v1.navigation_pb2.UpdateRouteResponse), '/viam.service.navigation.v1.NavigationService/DeleteRoute': grpclib.const.Handler(self.DeleteRoute, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.DeleteRouteRequest, service.navigation.v1.navigation_pb2.DeleteRouteResponse), '/viam.service.navigation.v1.NavigationService/AddZone': grpclib.const.Handler(self.AddZone, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.AddZoneRequest, service.navigation.v1.navigation_pb2.AddZoneResponse), '/viam.service.navigation.v1.NavigationService/GetZone': grpclib.const.Handler(self.GetZone, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.GetZoneRequest, service.navigation.v1.navigation_pb2.GetZoneResponse), '/viam.service.navigation.v1.NavigationService/ListZones': grpclib.const.Handler(self.ListZones, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.ListZonesRequest, service.navigation.v1.navigation_pb2.ListZonesResponse), '/viam.service.navigation.v1.NavigationService/UpdateZone': grpclib.const.Handler(self.UpdateZone, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.UpdateZoneRequest, service.navigation.v1.navigation_pb2.UpdateZoneResponse), '/viam.service.navigation.v1.NavigationService/DeleteZone': grpclib.const.Handler(self.DeleteZone, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.DeleteZoneRequest, service.navigation.v1.navigation_pb2.DeleteZoneResponse), '/viam.service.navigation.v1.NavigationService/NavigateToLocation': grpclib.const.Handler(self.NavigateToLocation, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.NavigateToLocationRequest, service.navigation.v1.navigation_pb2.NavigateToLocationResponse), '/viam.service.navigation.v1.NavigationService/NavigateToPoint': grpclib.const.Handler(self.NavigateToPoint, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.NavigateToPointRequest, service.navigation.v1.navigation_pb2.NavigateToPointResponse), '/viam.service.navigation.v1.NavigationService/NavigateRoute': grpclib.const.Handler(self.NavigateRoute, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.NavigateRouteRequest, service.navigation.v1.navigation_pb2.NavigateRouteResponse), '/viam.service.navigation.v1.NavigationService/PlanToPoint': grpclib.const.Handler(self.PlanToPoint, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.PlanToPointRequest, service.navigation.v1.navigation_pb2.PlanToPointResponse), '/viam.service.navigation.v1.NavigationService/PlanToLocation': grpclib.const.Handler(self.PlanToLocation, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.PlanToLocationRequest, service.navigation.v1.navigation_pb2.PlanToLocationResponse), '/viam.service.navigation.v1.NavigationService/ExecutePlan': grpclib.const.Handler(self.ExecutePlan, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.ExecutePlanRequest, service.navigation.v1.navigation_pb2.ExecutePlanResponse), '/viam.service.navigation.v1.NavigationService/GoToLocation': grpclib.const.Handler(self.GoToLocation, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.GoToLocationRequest, service.navigation.v1.navigation_pb2.GoToLocationResponse), '/viam.service.navigation.v1.NavigationService/GoToPoint': grpclib.const.Handler(self.GoToPoint, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.GoToPointRequest, service.navigation.v1.navigation_pb2.GoToPointResponse), '/viam.service.navigation.v1.NavigationService/Suspend': grpclib.const.Handler(self.Suspend, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.SuspendRequest, service.navigation.v1.navigation_pb2.SuspendResponse), '/viam.service.navigation.v1.NavigationService/Resume': grpclib.const.Handler(self.Resume, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.ResumeRequest, service.navigation.v1.navigation_pb2.ResumeResponse), '/viam.service.navigation.v1.NavigationService/Cancel': grpclib.const.Handler(self.Cancel, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.CancelRequest, service.navigation.v1.navigation_pb2.CancelResponse), '/viam.service.navigation.v1.NavigationService/GetPosition': grpclib.const.Handler(self.GetPosition, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.GetPositionRequest, service.navigation.v1.navigation_pb2.GetPositionResponse), '/viam.service.navigation.v1.NavigationService/GetNavigationStatus': grpclib.const.Handler(self.GetNavigationStatus, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.GetNavigationStatusRequest, service.navigation.v1.navigation_pb2.GetNavigationStatusResponse), '/viam.service.navigation.v1.NavigationService/GetProperties': grpclib.const.Handler(self.GetProperties, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.GetPropertiesRequest, service.navigation.v1.navigation_pb2.GetPropertiesResponse), '/viam.service.navigation.v1.NavigationService/GetCostmap': grpclib.const.Handler(self.GetCostmap, grpclib.const.Cardinality.UNARY_UNARY, service.navigation.v1.navigation_pb2.GetCostmapRequest, service.navigation.v1.navigation_pb2.GetCostmapResponse), '/viam.service.navigation.v1.NavigationService/DoCommand': grpclib.const.Handler(self.DoCommand, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse), '/viam.service.navigation.v1.NavigationService/GetStatus': grpclib.const.Handler(self.GetStatus, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.GetStatusRequest, common.v1.common_pb2.GetStatusResponse)}

class UnimplementedNavigationServiceBase(NavigationServiceBase):

    async def AddLocation(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.AddLocationRequest, service.navigation.v1.navigation_pb2.AddLocationResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetLocation(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.GetLocationRequest, service.navigation.v1.navigation_pb2.GetLocationResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ListLocations(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.ListLocationsRequest, service.navigation.v1.navigation_pb2.ListLocationsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def UpdateLocation(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.UpdateLocationRequest, service.navigation.v1.navigation_pb2.UpdateLocationResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DeleteLocation(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.DeleteLocationRequest, service.navigation.v1.navigation_pb2.DeleteLocationResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def AddRoute(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.AddRouteRequest, service.navigation.v1.navigation_pb2.AddRouteResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetRoute(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.GetRouteRequest, service.navigation.v1.navigation_pb2.GetRouteResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ListRoutes(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.ListRoutesRequest, service.navigation.v1.navigation_pb2.ListRoutesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def UpdateRoute(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.UpdateRouteRequest, service.navigation.v1.navigation_pb2.UpdateRouteResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DeleteRoute(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.DeleteRouteRequest, service.navigation.v1.navigation_pb2.DeleteRouteResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def AddZone(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.AddZoneRequest, service.navigation.v1.navigation_pb2.AddZoneResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetZone(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.GetZoneRequest, service.navigation.v1.navigation_pb2.GetZoneResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ListZones(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.ListZonesRequest, service.navigation.v1.navigation_pb2.ListZonesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def UpdateZone(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.UpdateZoneRequest, service.navigation.v1.navigation_pb2.UpdateZoneResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DeleteZone(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.DeleteZoneRequest, service.navigation.v1.navigation_pb2.DeleteZoneResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def NavigateToLocation(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.NavigateToLocationRequest, service.navigation.v1.navigation_pb2.NavigateToLocationResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def NavigateToPoint(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.NavigateToPointRequest, service.navigation.v1.navigation_pb2.NavigateToPointResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def NavigateRoute(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.NavigateRouteRequest, service.navigation.v1.navigation_pb2.NavigateRouteResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def PlanToPoint(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.PlanToPointRequest, service.navigation.v1.navigation_pb2.PlanToPointResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def PlanToLocation(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.PlanToLocationRequest, service.navigation.v1.navigation_pb2.PlanToLocationResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ExecutePlan(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.ExecutePlanRequest, service.navigation.v1.navigation_pb2.ExecutePlanResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GoToLocation(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.GoToLocationRequest, service.navigation.v1.navigation_pb2.GoToLocationResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GoToPoint(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.GoToPointRequest, service.navigation.v1.navigation_pb2.GoToPointResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def Suspend(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.SuspendRequest, service.navigation.v1.navigation_pb2.SuspendResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def Resume(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.ResumeRequest, service.navigation.v1.navigation_pb2.ResumeResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def Cancel(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.CancelRequest, service.navigation.v1.navigation_pb2.CancelResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetPosition(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.GetPositionRequest, service.navigation.v1.navigation_pb2.GetPositionResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetNavigationStatus(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.GetNavigationStatusRequest, service.navigation.v1.navigation_pb2.GetNavigationStatusResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetProperties(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.GetPropertiesRequest, service.navigation.v1.navigation_pb2.GetPropertiesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetCostmap(self, stream: 'grpclib.server.Stream[service.navigation.v1.navigation_pb2.GetCostmapRequest, service.navigation.v1.navigation_pb2.GetCostmapResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetStatus(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetStatusRequest, common.v1.common_pb2.GetStatusResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class NavigationServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.AddLocation = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/AddLocation', service.navigation.v1.navigation_pb2.AddLocationRequest, service.navigation.v1.navigation_pb2.AddLocationResponse)
        self.GetLocation = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/GetLocation', service.navigation.v1.navigation_pb2.GetLocationRequest, service.navigation.v1.navigation_pb2.GetLocationResponse)
        self.ListLocations = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/ListLocations', service.navigation.v1.navigation_pb2.ListLocationsRequest, service.navigation.v1.navigation_pb2.ListLocationsResponse)
        self.UpdateLocation = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/UpdateLocation', service.navigation.v1.navigation_pb2.UpdateLocationRequest, service.navigation.v1.navigation_pb2.UpdateLocationResponse)
        self.DeleteLocation = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/DeleteLocation', service.navigation.v1.navigation_pb2.DeleteLocationRequest, service.navigation.v1.navigation_pb2.DeleteLocationResponse)
        self.AddRoute = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/AddRoute', service.navigation.v1.navigation_pb2.AddRouteRequest, service.navigation.v1.navigation_pb2.AddRouteResponse)
        self.GetRoute = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/GetRoute', service.navigation.v1.navigation_pb2.GetRouteRequest, service.navigation.v1.navigation_pb2.GetRouteResponse)
        self.ListRoutes = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/ListRoutes', service.navigation.v1.navigation_pb2.ListRoutesRequest, service.navigation.v1.navigation_pb2.ListRoutesResponse)
        self.UpdateRoute = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/UpdateRoute', service.navigation.v1.navigation_pb2.UpdateRouteRequest, service.navigation.v1.navigation_pb2.UpdateRouteResponse)
        self.DeleteRoute = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/DeleteRoute', service.navigation.v1.navigation_pb2.DeleteRouteRequest, service.navigation.v1.navigation_pb2.DeleteRouteResponse)
        self.AddZone = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/AddZone', service.navigation.v1.navigation_pb2.AddZoneRequest, service.navigation.v1.navigation_pb2.AddZoneResponse)
        self.GetZone = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/GetZone', service.navigation.v1.navigation_pb2.GetZoneRequest, service.navigation.v1.navigation_pb2.GetZoneResponse)
        self.ListZones = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/ListZones', service.navigation.v1.navigation_pb2.ListZonesRequest, service.navigation.v1.navigation_pb2.ListZonesResponse)
        self.UpdateZone = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/UpdateZone', service.navigation.v1.navigation_pb2.UpdateZoneRequest, service.navigation.v1.navigation_pb2.UpdateZoneResponse)
        self.DeleteZone = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/DeleteZone', service.navigation.v1.navigation_pb2.DeleteZoneRequest, service.navigation.v1.navigation_pb2.DeleteZoneResponse)
        self.NavigateToLocation = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/NavigateToLocation', service.navigation.v1.navigation_pb2.NavigateToLocationRequest, service.navigation.v1.navigation_pb2.NavigateToLocationResponse)
        self.NavigateToPoint = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/NavigateToPoint', service.navigation.v1.navigation_pb2.NavigateToPointRequest, service.navigation.v1.navigation_pb2.NavigateToPointResponse)
        self.NavigateRoute = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/NavigateRoute', service.navigation.v1.navigation_pb2.NavigateRouteRequest, service.navigation.v1.navigation_pb2.NavigateRouteResponse)
        self.PlanToPoint = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/PlanToPoint', service.navigation.v1.navigation_pb2.PlanToPointRequest, service.navigation.v1.navigation_pb2.PlanToPointResponse)
        self.PlanToLocation = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/PlanToLocation', service.navigation.v1.navigation_pb2.PlanToLocationRequest, service.navigation.v1.navigation_pb2.PlanToLocationResponse)
        self.ExecutePlan = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/ExecutePlan', service.navigation.v1.navigation_pb2.ExecutePlanRequest, service.navigation.v1.navigation_pb2.ExecutePlanResponse)
        self.GoToLocation = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/GoToLocation', service.navigation.v1.navigation_pb2.GoToLocationRequest, service.navigation.v1.navigation_pb2.GoToLocationResponse)
        self.GoToPoint = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/GoToPoint', service.navigation.v1.navigation_pb2.GoToPointRequest, service.navigation.v1.navigation_pb2.GoToPointResponse)
        self.Suspend = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/Suspend', service.navigation.v1.navigation_pb2.SuspendRequest, service.navigation.v1.navigation_pb2.SuspendResponse)
        self.Resume = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/Resume', service.navigation.v1.navigation_pb2.ResumeRequest, service.navigation.v1.navigation_pb2.ResumeResponse)
        self.Cancel = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/Cancel', service.navigation.v1.navigation_pb2.CancelRequest, service.navigation.v1.navigation_pb2.CancelResponse)
        self.GetPosition = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/GetPosition', service.navigation.v1.navigation_pb2.GetPositionRequest, service.navigation.v1.navigation_pb2.GetPositionResponse)
        self.GetNavigationStatus = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/GetNavigationStatus', service.navigation.v1.navigation_pb2.GetNavigationStatusRequest, service.navigation.v1.navigation_pb2.GetNavigationStatusResponse)
        self.GetProperties = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/GetProperties', service.navigation.v1.navigation_pb2.GetPropertiesRequest, service.navigation.v1.navigation_pb2.GetPropertiesResponse)
        self.GetCostmap = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/GetCostmap', service.navigation.v1.navigation_pb2.GetCostmapRequest, service.navigation.v1.navigation_pb2.GetCostmapResponse)
        self.DoCommand = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/DoCommand', common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)
        self.GetStatus = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.navigation.v1.NavigationService/GetStatus', common.v1.common_pb2.GetStatusRequest, common.v1.common_pb2.GetStatusResponse)