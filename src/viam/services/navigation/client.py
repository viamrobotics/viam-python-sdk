from typing import Any, Dict, List, Mapping, Optional

from grpclib.client import Channel

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
    DeleteRouteRequest,
    DeleteZoneRequest,
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
    Location,
    NavigateRouteRequest,
    NavigateRouteResponse,
    NavigateToLocationRequest,
    NavigateToLocationResponse,
    NavigateToPointRequest,
    NavigateToPointResponse,
    NavigationServiceStub,
    Plan,
    PlanToLocationRequest,
    PlanToLocationResponse,
    PlanToPointRequest,
    PlanToPointResponse,
    Position,
    Properties,
    ResumeRequest,
    ResumeResponse,
    Route,
    Status,
    SuspendRequest,
    SuspendResponse,
    UpdateLocationRequest,
    UpdateLocationResponse,
    UpdateRouteRequest,
    UpdateRouteResponse,
    UpdateZoneRequest,
    UpdateZoneResponse,
    Waypoint,
    WaypointList,
    Zone,
)
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.utils import ValueTypes, dict_to_struct, struct_to_dict

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

    async def add_location(
        self,
        location_name: str,
        position: Optional[Position] = None,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Location:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = AddLocationRequest(name=self.name, location_name=location_name, position=position, extra=dict_to_struct(extra))
        response: AddLocationResponse = await self.client.AddLocation(request, timeout=timeout, metadata=md)
        return response.location

    async def get_location(
        self, location_name: str, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Location:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetLocationRequest(name=self.name, location_name=location_name, extra=dict_to_struct(extra))
        response: GetLocationResponse = await self.client.GetLocation(request, timeout=timeout, metadata=md)
        return response.location

    async def list_locations(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> List[Location]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = ListLocationsRequest(name=self.name, extra=dict_to_struct(extra))
        response: ListLocationsResponse = await self.client.ListLocations(request, timeout=timeout, metadata=md)
        return list(response.locations)

    async def update_location(
        self,
        location_name: str,
        position: Optional[Position] = None,
        new_name: Optional[str] = None,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Location:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = UpdateLocationRequest(
            name=self.name, location_name=location_name, position=position, new_name=new_name, extra=dict_to_struct(extra)
        )
        response: UpdateLocationResponse = await self.client.UpdateLocation(request, timeout=timeout, metadata=md)
        return response.location

    async def delete_location(
        self, location_name: str, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> None:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = DeleteLocationRequest(name=self.name, location_name=location_name, extra=dict_to_struct(extra))
        await self.client.DeleteLocation(request, timeout=timeout, metadata=md)

    async def add_route(
        self,
        route_name: str,
        waypoints: Optional[List[Waypoint]] = None,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Route:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = AddRouteRequest(name=self.name, route_name=route_name, waypoints=waypoints, extra=dict_to_struct(extra))
        response: AddRouteResponse = await self.client.AddRoute(request, timeout=timeout, metadata=md)
        return response.route

    async def get_route(
        self, route_name: str, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Route:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetRouteRequest(name=self.name, route_name=route_name, extra=dict_to_struct(extra))
        response: GetRouteResponse = await self.client.GetRoute(request, timeout=timeout, metadata=md)
        return response.route

    async def list_routes(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> List[Route]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = ListRoutesRequest(name=self.name, extra=dict_to_struct(extra))
        response: ListRoutesResponse = await self.client.ListRoutes(request, timeout=timeout, metadata=md)
        return list(response.routes)

    async def update_route(
        self,
        route_name: str,
        new_name: Optional[str] = None,
        waypoints: Optional[List[Waypoint]] = None,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Route:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = UpdateRouteRequest(
            name=self.name,
            route_name=route_name,
            new_name=new_name,
            waypoints=WaypointList(waypoints=waypoints) if waypoints is not None else None,
            extra=dict_to_struct(extra),
        )
        response: UpdateRouteResponse = await self.client.UpdateRoute(request, timeout=timeout, metadata=md)
        return response.route

    async def delete_route(
        self, route_name: str, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> None:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = DeleteRouteRequest(name=self.name, route_name=route_name, extra=dict_to_struct(extra))
        await self.client.DeleteRoute(request, timeout=timeout, metadata=md)

    async def add_zone(
        self,
        zone_name: str,
        type: str,
        geometry: Dict[str, Any],
        max_speed: Optional[float] = None,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Zone:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = AddZoneRequest(
            name=self.name,
            zone_name=zone_name,
            type=type,
            geometry=dict_to_struct(geometry),
            max_speed=max_speed,
            extra=dict_to_struct(extra),
        )
        response: AddZoneResponse = await self.client.AddZone(request, timeout=timeout, metadata=md)
        return response.zone

    async def get_zone(self, zone_name: str, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Zone:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetZoneRequest(name=self.name, zone_name=zone_name, extra=dict_to_struct(extra))
        response: GetZoneResponse = await self.client.GetZone(request, timeout=timeout, metadata=md)
        return response.zone

    async def list_zones(
        self, type: Optional[str] = None, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> List[Zone]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = ListZonesRequest(name=self.name, type=type or "", extra=dict_to_struct(extra))
        response: ListZonesResponse = await self.client.ListZones(request, timeout=timeout, metadata=md)
        return list(response.zones)

    async def update_zone(
        self,
        zone_name: str,
        type: Optional[str] = None,
        geometry: Optional[Dict[str, Any]] = None,
        max_speed: Optional[float] = None,
        new_name: Optional[str] = None,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Zone:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = UpdateZoneRequest(
            name=self.name,
            zone_name=zone_name,
            type=type,
            geometry=dict_to_struct(geometry) if geometry is not None else None,
            max_speed=max_speed,
            new_name=new_name,
            extra=dict_to_struct(extra),
        )
        response: UpdateZoneResponse = await self.client.UpdateZone(request, timeout=timeout, metadata=md)
        return response.zone

    async def delete_zone(
        self, zone_name: str, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> None:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = DeleteZoneRequest(name=self.name, zone_name=zone_name, extra=dict_to_struct(extra))
        await self.client.DeleteZone(request, timeout=timeout, metadata=md)

    async def navigate_to_location(
        self, location_name: str, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Status:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = NavigateToLocationRequest(name=self.name, location_name=location_name, extra=dict_to_struct(extra))
        response: NavigateToLocationResponse = await self.client.NavigateToLocation(request, timeout=timeout, metadata=md)
        return response.status

    async def navigate_to_point(
        self, destination: Position, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Status:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = NavigateToPointRequest(name=self.name, destination=destination, extra=dict_to_struct(extra))
        response: NavigateToPointResponse = await self.client.NavigateToPoint(request, timeout=timeout, metadata=md)
        return response.status

    async def navigate_route(
        self,
        route_name: Optional[str] = None,
        waypoints: Optional[List[Waypoint]] = None,
        start_index: int = 0,
        start_nearest: bool = False,
        loop: bool = False,
        wait: bool = False,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Status:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = NavigateRouteRequest(
            name=self.name,
            route_name=route_name or "",
            waypoints=waypoints,
            start_index=start_index,
            start_nearest=start_nearest,
            loop=loop,
            wait=wait,
            extra=dict_to_struct(extra),
        )
        response: NavigateRouteResponse = await self.client.NavigateRoute(request, timeout=timeout, metadata=md)
        return response.status

    async def plan_to_point(
        self,
        destination: Position,
        start: Optional[Position] = None,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Plan:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = PlanToPointRequest(name=self.name, destination=destination, start=start, extra=dict_to_struct(extra))
        response: PlanToPointResponse = await self.client.PlanToPoint(request, timeout=timeout, metadata=md)
        return response.plan

    async def plan_to_location(
        self,
        location_name: str,
        start: Optional[Position] = None,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Plan:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = PlanToLocationRequest(name=self.name, location_name=location_name, start=start, extra=dict_to_struct(extra))
        response: PlanToLocationResponse = await self.client.PlanToLocation(request, timeout=timeout, metadata=md)
        return response.plan

    async def execute_plan(
        self, plan: Plan, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Status:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = ExecutePlanRequest(name=self.name, plan=plan, extra=dict_to_struct(extra))
        response: ExecutePlanResponse = await self.client.ExecutePlan(request, timeout=timeout, metadata=md)
        return response.status

    async def go_to_location(
        self,
        location_name: str,
        wait: Optional[bool] = None,
        linear_m_per_sec: Optional[float] = None,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Status:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GoToLocationRequest(
            name=self.name, location_name=location_name, wait=wait, linear_m_per_sec=linear_m_per_sec, extra=dict_to_struct(extra)
        )
        response: GoToLocationResponse = await self.client.GoToLocation(request, timeout=timeout, metadata=md)
        return response.status

    async def go_to_point(
        self,
        destination: Position,
        wait: Optional[bool] = None,
        linear_m_per_sec: Optional[float] = None,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Status:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GoToPointRequest(
            name=self.name, destination=destination, wait=wait, linear_m_per_sec=linear_m_per_sec, extra=dict_to_struct(extra)
        )
        response: GoToPointResponse = await self.client.GoToPoint(request, timeout=timeout, metadata=md)
        return response.status

    async def suspend(
        self, reason: str = "", *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Status:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = SuspendRequest(name=self.name, reason=reason, extra=dict_to_struct(extra))
        response: SuspendResponse = await self.client.Suspend(request, timeout=timeout, metadata=md)
        return response.status

    async def resume(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Status:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = ResumeRequest(name=self.name, extra=dict_to_struct(extra))
        response: ResumeResponse = await self.client.Resume(request, timeout=timeout, metadata=md)
        return response.status

    async def cancel(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Status:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = CancelRequest(name=self.name, extra=dict_to_struct(extra))
        response: CancelResponse = await self.client.Cancel(request, timeout=timeout, metadata=md)
        return response.status

    async def get_position(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Position:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetPositionRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetPositionResponse = await self.client.GetPosition(request, timeout=timeout, metadata=md)
        return response.position

    async def get_navigation_status(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Status:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetNavigationStatusRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetNavigationStatusResponse = await self.client.GetNavigationStatus(request, timeout=timeout, metadata=md)
        return response.status

    async def get_properties(self, *, timeout: Optional[float] = None, **kwargs) -> Properties:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetPropertiesRequest(name=self.name)
        response: GetPropertiesResponse = await self.client.GetProperties(request, timeout=timeout, metadata=md)
        return response.properties

    async def get_costmap(
        self, layer: str = "", stride: int = 0, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> GetCostmapResponse:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetCostmapRequest(name=self.name, layer=layer, stride=stride, extra=dict_to_struct(extra))
        return await self.client.GetCostmap(request, timeout=timeout, metadata=md)

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout, metadata=md)
        return struct_to_dict(response.result)

    async def get_status(
        self,
        *,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Mapping[str, ValueTypes]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetStatusRequest(name=self.name)
        response: GetStatusResponse = await self.client.GetStatus(request, timeout=timeout, metadata=md)
        return struct_to_dict(response.result)
