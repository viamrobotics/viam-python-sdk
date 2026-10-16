from grpclib.server import Stream

from viam.proto.common import DoCommandRequest, DoCommandResponse, GetStatusRequest, GetStatusResponse
from viam.proto.service.navigation import (
    AddLocationRequest,
    AddLocationResponse,
    AddRouteRequest,
    AddRouteResponse,
    AddZoneRequest,
    AddZoneResponse,
    CancelRequest,
    CancelResponse,
    DeleteLocationRequest,
    DeleteLocationResponse,
    DeleteRouteRequest,
    DeleteRouteResponse,
    DeleteZoneRequest,
    DeleteZoneResponse,
    ExecutePlanRequest,
    ExecutePlanResponse,
    GetCostmapRequest,
    GetCostmapResponse,
    GetLocationRequest,
    GetLocationResponse,
    GetNavigationStatusRequest,
    GetNavigationStatusResponse,
    GetPositionRequest,
    GetPositionResponse,
    GetPropertiesRequest,
    GetPropertiesResponse,
    GetRouteRequest,
    GetRouteResponse,
    GetZoneRequest,
    GetZoneResponse,
    GoToLocationRequest,
    GoToLocationResponse,
    GoToPointRequest,
    GoToPointResponse,
    ListLocationsRequest,
    ListLocationsResponse,
    ListRoutesRequest,
    ListRoutesResponse,
    ListZonesRequest,
    ListZonesResponse,
    NavigateRouteRequest,
    NavigateRouteResponse,
    NavigateToLocationRequest,
    NavigateToLocationResponse,
    NavigateToPointRequest,
    NavigateToPointResponse,
    NavigationServiceBase,
    PlanToLocationRequest,
    PlanToLocationResponse,
    PlanToPointRequest,
    PlanToPointResponse,
    ResumeRequest,
    ResumeResponse,
    SuspendRequest,
    SuspendResponse,
    UpdateLocationRequest,
    UpdateLocationResponse,
    UpdateRouteRequest,
    UpdateRouteResponse,
    UpdateZoneRequest,
    UpdateZoneResponse,
)
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.utils import dict_to_struct, struct_to_dict

from .navigation import Navigation


class NavigationRPCService(NavigationServiceBase, ResourceRPCServiceBase):
    """
    gRPC Service for a Navigation service
    """

    RESOURCE_TYPE = Navigation

    async def AddLocation(self, stream: Stream[AddLocationRequest, AddLocationResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        location = await navigation.add_location(
            request.location_name,
            request.position if request.HasField("position") else None,
            extra=struct_to_dict(request.extra),
            timeout=timeout,
            metadata=stream.metadata,
        )
        await stream.send_message(AddLocationResponse(location=location))

    async def GetLocation(self, stream: Stream[GetLocationRequest, GetLocationResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        location = await navigation.get_location(
            request.location_name, extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata
        )
        await stream.send_message(GetLocationResponse(location=location))

    async def ListLocations(self, stream: Stream[ListLocationsRequest, ListLocationsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        locations = await navigation.list_locations(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        await stream.send_message(ListLocationsResponse(locations=locations))

    async def UpdateLocation(self, stream: Stream[UpdateLocationRequest, UpdateLocationResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        location = await navigation.update_location(
            request.location_name,
            request.position if request.HasField("position") else None,
            request.new_name if request.HasField("new_name") else None,
            extra=struct_to_dict(request.extra),
            timeout=timeout,
            metadata=stream.metadata,
        )
        await stream.send_message(UpdateLocationResponse(location=location))

    async def DeleteLocation(self, stream: Stream[DeleteLocationRequest, DeleteLocationResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await navigation.delete_location(
            request.location_name, extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata
        )
        await stream.send_message(DeleteLocationResponse())

    async def AddRoute(self, stream: Stream[AddRouteRequest, AddRouteResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        route = await navigation.add_route(
            request.route_name, list(request.waypoints), extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata
        )
        await stream.send_message(AddRouteResponse(route=route))

    async def GetRoute(self, stream: Stream[GetRouteRequest, GetRouteResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        route = await navigation.get_route(
            request.route_name, extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata
        )
        await stream.send_message(GetRouteResponse(route=route))

    async def ListRoutes(self, stream: Stream[ListRoutesRequest, ListRoutesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        routes = await navigation.list_routes(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        await stream.send_message(ListRoutesResponse(routes=routes))

    async def UpdateRoute(self, stream: Stream[UpdateRouteRequest, UpdateRouteResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        route = await navigation.update_route(
            request.route_name,
            request.new_name if request.HasField("new_name") else None,
            list(request.waypoints.waypoints) if request.HasField("waypoints") else None,
            extra=struct_to_dict(request.extra),
            timeout=timeout,
            metadata=stream.metadata,
        )
        await stream.send_message(UpdateRouteResponse(route=route))

    async def DeleteRoute(self, stream: Stream[DeleteRouteRequest, DeleteRouteResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await navigation.delete_route(request.route_name, extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        await stream.send_message(DeleteRouteResponse())

    async def AddZone(self, stream: Stream[AddZoneRequest, AddZoneResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        zone = await navigation.add_zone(
            request.zone_name,
            request.type,
            struct_to_dict(request.geometry),
            request.max_speed if request.HasField("max_speed") else None,
            extra=struct_to_dict(request.extra),
            timeout=timeout,
            metadata=stream.metadata,
        )
        await stream.send_message(AddZoneResponse(zone=zone))

    async def GetZone(self, stream: Stream[GetZoneRequest, GetZoneResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        zone = await navigation.get_zone(request.zone_name, extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        await stream.send_message(GetZoneResponse(zone=zone))

    async def ListZones(self, stream: Stream[ListZonesRequest, ListZonesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        zones = await navigation.list_zones(
            request.type or None, extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata
        )
        await stream.send_message(ListZonesResponse(zones=zones))

    async def UpdateZone(self, stream: Stream[UpdateZoneRequest, UpdateZoneResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        zone = await navigation.update_zone(
            request.zone_name,
            request.type if request.HasField("type") else None,
            struct_to_dict(request.geometry) if request.HasField("geometry") else None,
            request.max_speed if request.HasField("max_speed") else None,
            request.new_name if request.HasField("new_name") else None,
            extra=struct_to_dict(request.extra),
            timeout=timeout,
            metadata=stream.metadata,
        )
        await stream.send_message(UpdateZoneResponse(zone=zone))

    async def DeleteZone(self, stream: Stream[DeleteZoneRequest, DeleteZoneResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await navigation.delete_zone(request.zone_name, extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        await stream.send_message(DeleteZoneResponse())

    async def NavigateToLocation(self, stream: Stream[NavigateToLocationRequest, NavigateToLocationResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        status = await navigation.navigate_to_location(
            request.location_name, extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata
        )
        await stream.send_message(NavigateToLocationResponse(status=status))

    async def NavigateToPoint(self, stream: Stream[NavigateToPointRequest, NavigateToPointResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        status = await navigation.navigate_to_point(
            request.destination, extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata
        )
        await stream.send_message(NavigateToPointResponse(status=status))

    async def NavigateRoute(self, stream: Stream[NavigateRouteRequest, NavigateRouteResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        status = await navigation.navigate_route(
            request.route_name or None,
            list(request.waypoints) or None,
            request.start_index,
            request.start_nearest,
            request.loop,
            request.wait,
            extra=struct_to_dict(request.extra),
            timeout=timeout,
            metadata=stream.metadata,
        )
        await stream.send_message(NavigateRouteResponse(status=status))

    async def PlanToPoint(self, stream: Stream[PlanToPointRequest, PlanToPointResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        plan = await navigation.plan_to_point(
            request.destination,
            request.start if request.HasField("start") else None,
            extra=struct_to_dict(request.extra),
            timeout=timeout,
            metadata=stream.metadata,
        )
        await stream.send_message(PlanToPointResponse(plan=plan))

    async def PlanToLocation(self, stream: Stream[PlanToLocationRequest, PlanToLocationResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        plan = await navigation.plan_to_location(
            request.location_name,
            request.start if request.HasField("start") else None,
            extra=struct_to_dict(request.extra),
            timeout=timeout,
            metadata=stream.metadata,
        )
        await stream.send_message(PlanToLocationResponse(plan=plan))

    async def ExecutePlan(self, stream: Stream[ExecutePlanRequest, ExecutePlanResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        status = await navigation.execute_plan(request.plan, extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        await stream.send_message(ExecutePlanResponse(status=status))

    async def GoToLocation(self, stream: Stream[GoToLocationRequest, GoToLocationResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        status = await navigation.go_to_location(
            request.location_name,
            request.wait if request.HasField("wait") else None,
            request.linear_m_per_sec if request.HasField("linear_m_per_sec") else None,
            extra=struct_to_dict(request.extra),
            timeout=timeout,
            metadata=stream.metadata,
        )
        await stream.send_message(GoToLocationResponse(status=status))

    async def GoToPoint(self, stream: Stream[GoToPointRequest, GoToPointResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        status = await navigation.go_to_point(
            request.destination,
            request.wait if request.HasField("wait") else None,
            request.linear_m_per_sec if request.HasField("linear_m_per_sec") else None,
            extra=struct_to_dict(request.extra),
            timeout=timeout,
            metadata=stream.metadata,
        )
        await stream.send_message(GoToPointResponse(status=status))

    async def Suspend(self, stream: Stream[SuspendRequest, SuspendResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        status = await navigation.suspend(request.reason, extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        await stream.send_message(SuspendResponse(status=status))

    async def Resume(self, stream: Stream[ResumeRequest, ResumeResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        status = await navigation.resume(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        await stream.send_message(ResumeResponse(status=status))

    async def Cancel(self, stream: Stream[CancelRequest, CancelResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        status = await navigation.cancel(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        await stream.send_message(CancelResponse(status=status))

    async def GetPosition(self, stream: Stream[GetPositionRequest, GetPositionResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        position = await navigation.get_position(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        await stream.send_message(GetPositionResponse(position=position))

    async def GetNavigationStatus(self, stream: Stream[GetNavigationStatusRequest, GetNavigationStatusResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        status = await navigation.get_navigation_status(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        await stream.send_message(GetNavigationStatusResponse(status=status))

    async def GetProperties(self, stream: Stream[GetPropertiesRequest, GetPropertiesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        properties = await navigation.get_properties(timeout=timeout, metadata=stream.metadata)
        await stream.send_message(GetPropertiesResponse(properties=properties))

    async def GetCostmap(self, stream: Stream[GetCostmapRequest, GetCostmapResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        response = await navigation.get_costmap(
            request.layer, request.stride, extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata
        )
        await stream.send_message(response)

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await navigation.do_command(command=struct_to_dict(request.command), timeout=timeout, metadata=stream.metadata)
        response = DoCommandResponse(result=dict_to_struct(result))
        await stream.send_message(response)

    async def GetStatus(self, stream: Stream[GetStatusRequest, GetStatusResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await navigation.get_status(timeout=timeout, metadata=stream.metadata)
        response = GetStatusResponse(result=dict_to_struct(result))
        await stream.send_message(response)
