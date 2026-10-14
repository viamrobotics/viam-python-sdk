from grpclib.testing import ChannelFor

from viam.proto.common import DoCommandRequest, DoCommandResponse, GetStatusRequest, GetStatusResponse, Pose
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
    NavigationServiceStub,
    PlanToLocationRequest,
    PlanToLocationResponse,
    PlanToPointRequest,
    PlanToPointResponse,
    Position,
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
    Waypoint,
    WaypointList,
)
from viam.resource.manager import ResourceManager
from viam.services.navigation import NavigationClient, NavigationRPCService
from viam.utils import dict_to_struct, struct_to_dict

from .mocks.services import MockNavigation

DESTINATION = Position(pose=Pose(x=10.0, y=20.0, z=0.0))


class TestNavigationService:
    name = "navigation"
    navigation = MockNavigation(name="navigation")

    async def test_add_location(self):
        result = await self.navigation.add_location("home", DESTINATION)
        assert result == MockNavigation.LOCATION
        assert self.navigation.calls["add_location"] == ("home", DESTINATION)

    async def test_get_location(self):
        result = await self.navigation.get_location("home")
        assert result == MockNavigation.LOCATION

    async def test_list_locations(self):
        result = await self.navigation.list_locations()
        assert result == [MockNavigation.LOCATION]

    async def test_update_location(self):
        result = await self.navigation.update_location("home", DESTINATION, "new_home")
        assert result == MockNavigation.LOCATION
        assert self.navigation.calls["update_location"] == ("home", DESTINATION, "new_home")

    async def test_delete_location(self):
        await self.navigation.delete_location("home")
        assert self.navigation.calls["delete_location"] == ("home",)

    async def test_add_route(self):
        waypoints = [Waypoint(location="home")]
        result = await self.navigation.add_route("route1", waypoints)
        assert result == MockNavigation.ROUTE
        assert self.navigation.calls["add_route"] == ("route1", waypoints)

    async def test_get_route(self):
        result = await self.navigation.get_route("route1")
        assert result == MockNavigation.ROUTE

    async def test_list_routes(self):
        result = await self.navigation.list_routes()
        assert result == [MockNavigation.ROUTE]

    async def test_update_route(self):
        waypoints = [Waypoint(location="home")]
        result = await self.navigation.update_route("route1", "new_route", waypoints)
        assert result == MockNavigation.ROUTE
        assert self.navigation.calls["update_route"] == ("route1", "new_route", waypoints)

    async def test_delete_route(self):
        await self.navigation.delete_route("route1")
        assert self.navigation.calls["delete_route"] == ("route1",)

    async def test_add_zone(self):
        geometry = {"type": "circle", "radius_m": 1.0}
        result = await self.navigation.add_zone("zone1", "keepout", geometry, 2.0)
        assert result == MockNavigation.ZONE
        assert self.navigation.calls["add_zone"] == ("zone1", "keepout", geometry, 2.0)

    async def test_get_zone(self):
        result = await self.navigation.get_zone("zone1")
        assert result == MockNavigation.ZONE

    async def test_list_zones(self):
        result = await self.navigation.list_zones("keepout")
        assert result == [MockNavigation.ZONE]
        assert self.navigation.calls["list_zones"] == ("keepout",)

    async def test_update_zone(self):
        geometry = {"type": "circle", "radius_m": 2.0}
        result = await self.navigation.update_zone("zone1", "speed_limit", geometry, 3.0, "new_zone")
        assert result == MockNavigation.ZONE
        assert self.navigation.calls["update_zone"] == ("zone1", "speed_limit", geometry, 3.0, "new_zone")

    async def test_delete_zone(self):
        await self.navigation.delete_zone("zone1")
        assert self.navigation.calls["delete_zone"] == ("zone1",)

    async def test_navigate_to_location(self):
        result = await self.navigation.navigate_to_location("home")
        assert result == MockNavigation.STATUS

    async def test_navigate_to_point(self):
        result = await self.navigation.navigate_to_point(DESTINATION)
        assert result == MockNavigation.STATUS

    async def test_navigate_route(self):
        result = await self.navigation.navigate_route("route1", loop=True)
        assert result == MockNavigation.STATUS
        assert self.navigation.calls["navigate_route"] == ("route1", None, 0, False, True, False)

    async def test_plan_to_point(self):
        result = await self.navigation.plan_to_point(DESTINATION)
        assert result == MockNavigation.PLAN

    async def test_plan_to_location(self):
        result = await self.navigation.plan_to_location("home")
        assert result == MockNavigation.PLAN

    async def test_execute_plan(self):
        result = await self.navigation.execute_plan(MockNavigation.PLAN)
        assert result == MockNavigation.STATUS

    async def test_go_to_location(self):
        result = await self.navigation.go_to_location("home", linear_m_per_sec=1.0)
        assert result == MockNavigation.STATUS

    async def test_go_to_point(self):
        result = await self.navigation.go_to_point(DESTINATION)
        assert result == MockNavigation.STATUS

    async def test_suspend(self):
        result = await self.navigation.suspend("paused for safety")
        assert result == MockNavigation.STATUS
        assert self.navigation.calls["suspend"] == ("paused for safety",)

    async def test_resume(self):
        result = await self.navigation.resume()
        assert result == MockNavigation.STATUS

    async def test_cancel(self):
        result = await self.navigation.cancel()
        assert result == MockNavigation.STATUS

    async def test_get_position(self):
        result = await self.navigation.get_position()
        assert result == MockNavigation.POSITION

    async def test_get_navigation_status(self):
        result = await self.navigation.get_navigation_status()
        assert result == MockNavigation.STATUS

    async def test_get_properties(self):
        result = await self.navigation.get_properties()
        assert result == MockNavigation.PROPERTIES

    async def test_get_costmap(self):
        result = await self.navigation.get_costmap()
        assert result == MockNavigation.COSTMAP

    async def test_do(self):
        command = {"command": "args"}
        result = await self.navigation.do_command(command)
        assert result == {"command": command}

    async def test_get_status(self):
        status = await self.navigation.get_status()
        assert status == {}


class TestService:
    @classmethod
    def setup_class(cls):
        cls.name = "navigation"
        cls.navigation = MockNavigation(name=cls.name)
        cls.manager = ResourceManager([cls.navigation])
        cls.service = NavigationRPCService(cls.manager)

    async def test_add_location(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            request = AddLocationRequest(name=self.name, location_name="home", position=DESTINATION, extra=dict_to_struct({"a": "b"}))
            response: AddLocationResponse = await client.AddLocation(request)
            assert response.location == self.navigation.LOCATION
            assert self.navigation.calls["add_location"] == ("home", DESTINATION)
            assert self.navigation.extra == {"a": "b"}

    async def test_get_location(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            request = GetLocationRequest(name=self.name, location_name="home")
            response: GetLocationResponse = await client.GetLocation(request)
            assert response.location == self.navigation.LOCATION

    async def test_list_locations(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            request = ListLocationsRequest(name=self.name)
            response: ListLocationsResponse = await client.ListLocations(request)
            assert list(response.locations) == [self.navigation.LOCATION]

    async def test_update_location(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            request = UpdateLocationRequest(name=self.name, location_name="home", position=DESTINATION, new_name="new_home")
            response: UpdateLocationResponse = await client.UpdateLocation(request)
            assert response.location == self.navigation.LOCATION
            assert self.navigation.calls["update_location"] == ("home", DESTINATION, "new_home")

    async def test_delete_location(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            request = DeleteLocationRequest(name=self.name, location_name="home")
            await client.DeleteLocation(request)
            assert self.navigation.calls["delete_location"] == ("home",)

    async def test_add_route(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            waypoints = [Waypoint(location="home")]
            request = AddRouteRequest(name=self.name, route_name="route1", waypoints=waypoints)
            response: AddRouteResponse = await client.AddRoute(request)
            assert response.route == self.navigation.ROUTE
            assert self.navigation.calls["add_route"] == ("route1", waypoints)

    async def test_get_route(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            request = GetRouteRequest(name=self.name, route_name="route1")
            response: GetRouteResponse = await client.GetRoute(request)
            assert response.route == self.navigation.ROUTE

    async def test_list_routes(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            request = ListRoutesRequest(name=self.name)
            response: ListRoutesResponse = await client.ListRoutes(request)
            assert list(response.routes) == [self.navigation.ROUTE]

    async def test_update_route(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            waypoints = [Waypoint(location="home")]
            request = UpdateRouteRequest(
                name=self.name, route_name="route1", new_name="new_route", waypoints=WaypointList(waypoints=waypoints)
            )
            response: UpdateRouteResponse = await client.UpdateRoute(request)
            assert response.route == self.navigation.ROUTE
            assert self.navigation.calls["update_route"] == ("route1", "new_route", waypoints)

    async def test_delete_route(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            request = DeleteRouteRequest(name=self.name, route_name="route1")
            await client.DeleteRoute(request)
            assert self.navigation.calls["delete_route"] == ("route1",)

    async def test_add_zone(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            geometry = {"type": "circle", "radius_m": 1.0}
            request = AddZoneRequest(name=self.name, zone_name="zone1", type="keepout", geometry=dict_to_struct(geometry), max_speed=2.0)
            response: AddZoneResponse = await client.AddZone(request)
            assert response.zone == self.navigation.ZONE
            assert self.navigation.calls["add_zone"] == ("zone1", "keepout", geometry, 2.0)

    async def test_get_zone(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            request = GetZoneRequest(name=self.name, zone_name="zone1")
            response: GetZoneResponse = await client.GetZone(request)
            assert response.zone == self.navigation.ZONE

    async def test_list_zones(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            request = ListZonesRequest(name=self.name, type="keepout")
            response: ListZonesResponse = await client.ListZones(request)
            assert list(response.zones) == [self.navigation.ZONE]
            assert self.navigation.calls["list_zones"] == ("keepout",)

    async def test_update_zone(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            geometry = {"type": "circle", "radius_m": 2.0}
            request = UpdateZoneRequest(
                name=self.name, zone_name="zone1", type="speed_limit", geometry=dict_to_struct(geometry), max_speed=3.0, new_name="new_zone"
            )
            response: UpdateZoneResponse = await client.UpdateZone(request)
            assert response.zone == self.navigation.ZONE
            assert self.navigation.calls["update_zone"] == ("zone1", "speed_limit", geometry, 3.0, "new_zone")

    async def test_delete_zone(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            request = DeleteZoneRequest(name=self.name, zone_name="zone1")
            await client.DeleteZone(request)
            assert self.navigation.calls["delete_zone"] == ("zone1",)

    async def test_navigate_to_location(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            request = NavigateToLocationRequest(name=self.name, location_name="home")
            response: NavigateToLocationResponse = await client.NavigateToLocation(request)
            assert response.status == self.navigation.STATUS

    async def test_navigate_to_point(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            request = NavigateToPointRequest(name=self.name, destination=DESTINATION)
            response: NavigateToPointResponse = await client.NavigateToPoint(request)
            assert response.status == self.navigation.STATUS

    async def test_navigate_route(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            request = NavigateRouteRequest(name=self.name, route_name="route1", loop=True)
            response: NavigateRouteResponse = await client.NavigateRoute(request)
            assert response.status == self.navigation.STATUS
            assert self.navigation.calls["navigate_route"] == ("route1", None, 0, False, True, False)

    async def test_plan_to_point(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            request = PlanToPointRequest(name=self.name, destination=DESTINATION)
            response: PlanToPointResponse = await client.PlanToPoint(request)
            assert response.plan == self.navigation.PLAN

    async def test_plan_to_location(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            request = PlanToLocationRequest(name=self.name, location_name="home")
            response: PlanToLocationResponse = await client.PlanToLocation(request)
            assert response.plan == self.navigation.PLAN

    async def test_execute_plan(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            request = ExecutePlanRequest(name=self.name, plan=self.navigation.PLAN)
            response: ExecutePlanResponse = await client.ExecutePlan(request)
            assert response.status == self.navigation.STATUS

    async def test_go_to_location(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            request = GoToLocationRequest(name=self.name, location_name="home")
            response: GoToLocationResponse = await client.GoToLocation(request)
            assert response.status == self.navigation.STATUS

    async def test_go_to_point(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            request = GoToPointRequest(name=self.name, destination=DESTINATION)
            response: GoToPointResponse = await client.GoToPoint(request)
            assert response.status == self.navigation.STATUS

    async def test_suspend(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            request = SuspendRequest(name=self.name, reason="paused for safety")
            response: SuspendResponse = await client.Suspend(request)
            assert response.status == self.navigation.STATUS
            assert self.navigation.calls["suspend"] == ("paused for safety",)

    async def test_resume(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            request = ResumeRequest(name=self.name)
            response: ResumeResponse = await client.Resume(request)
            assert response.status == self.navigation.STATUS

    async def test_cancel(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            request = CancelRequest(name=self.name)
            response: CancelResponse = await client.Cancel(request)
            assert response.status == self.navigation.STATUS

    async def test_get_position(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            request = GetPositionRequest(name=self.name)
            response: GetPositionResponse = await client.GetPosition(request)
            assert response.position == self.navigation.POSITION

    async def test_get_navigation_status(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            request = GetNavigationStatusRequest(name=self.name)
            response: GetNavigationStatusResponse = await client.GetNavigationStatus(request)
            assert response.status == self.navigation.STATUS

    async def test_get_properties(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            request = GetPropertiesRequest(name=self.name)
            response: GetPropertiesResponse = await client.GetProperties(request)
            assert response.properties == self.navigation.PROPERTIES

    async def test_get_costmap(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            request = GetCostmapRequest(name=self.name)
            response = await client.GetCostmap(request)
            assert response == self.navigation.COSTMAP

    async def test_do(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            command = {"command": "args"}
            request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
            response: DoCommandResponse = await client.DoCommand(request)
            result = struct_to_dict(response.result)
            assert result == {"command": command}

    async def test_get_status(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            request = GetStatusRequest(name=self.name)
            response: GetStatusResponse = await client.GetStatus(request)
            assert struct_to_dict(response.result) == {}


class TestClient:
    @classmethod
    def setup_class(cls):
        cls.name = "navigation"
        cls.navigation = MockNavigation(name=cls.name)
        cls.manager = ResourceManager([cls.navigation])
        cls.service = NavigationRPCService(cls.manager)

    async def test_add_location(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            result = await client.add_location("home", DESTINATION)
            assert result == self.navigation.LOCATION

    async def test_get_location(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            result = await client.get_location("home")
            assert result == self.navigation.LOCATION

    async def test_list_locations(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            result = await client.list_locations()
            assert result == [self.navigation.LOCATION]

    async def test_update_location(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            result = await client.update_location("home", DESTINATION, "new_home")
            assert result == self.navigation.LOCATION

    async def test_delete_location(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            await client.delete_location("home")
            assert self.navigation.calls["delete_location"] == ("home",)

    async def test_add_route(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            waypoints = [Waypoint(location="home")]
            result = await client.add_route("route1", waypoints)
            assert result == self.navigation.ROUTE

    async def test_get_route(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            result = await client.get_route("route1")
            assert result == self.navigation.ROUTE

    async def test_list_routes(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            result = await client.list_routes()
            assert result == [self.navigation.ROUTE]

    async def test_update_route(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            waypoints = [Waypoint(location="home")]
            result = await client.update_route("route1", "new_route", waypoints)
            assert result == self.navigation.ROUTE
            assert self.navigation.calls["update_route"] == ("route1", "new_route", waypoints)

    async def test_update_route_leaves_waypoints_unchanged(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            await client.update_route("route1")
            assert self.navigation.calls["update_route"] == ("route1", None, None)

    async def test_delete_route(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            await client.delete_route("route1")
            assert self.navigation.calls["delete_route"] == ("route1",)

    async def test_add_zone(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            geometry = {"type": "circle", "radius_m": 1.0}
            result = await client.add_zone("zone1", "keepout", geometry, 2.0)
            assert result == self.navigation.ZONE

    async def test_get_zone(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            result = await client.get_zone("zone1")
            assert result == self.navigation.ZONE

    async def test_list_zones(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            result = await client.list_zones("keepout")
            assert result == [self.navigation.ZONE]

    async def test_update_zone(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            geometry = {"type": "circle", "radius_m": 2.0}
            result = await client.update_zone("zone1", "speed_limit", geometry, 3.0, "new_zone")
            assert result == self.navigation.ZONE
            assert self.navigation.calls["update_zone"] == ("zone1", "speed_limit", geometry, 3.0, "new_zone")

    async def test_update_zone_leaves_fields_unchanged(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            await client.update_zone("zone1")
            assert self.navigation.calls["update_zone"] == ("zone1", None, None, None, None)

    async def test_delete_zone(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            await client.delete_zone("zone1")
            assert self.navigation.calls["delete_zone"] == ("zone1",)

    async def test_navigate_to_location(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            result = await client.navigate_to_location("home")
            assert result == self.navigation.STATUS

    async def test_navigate_to_point(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            result = await client.navigate_to_point(DESTINATION)
            assert result == self.navigation.STATUS

    async def test_navigate_route(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            result = await client.navigate_route(route_name="route1", loop=True)
            assert result == self.navigation.STATUS
            assert self.navigation.calls["navigate_route"] == ("route1", None, 0, False, True, False)

    async def test_plan_to_point(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            result = await client.plan_to_point(DESTINATION)
            assert result == self.navigation.PLAN

    async def test_plan_to_location(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            result = await client.plan_to_location("home")
            assert result == self.navigation.PLAN

    async def test_execute_plan(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            result = await client.execute_plan(self.navigation.PLAN)
            assert result == self.navigation.STATUS

    async def test_go_to_location(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            result = await client.go_to_location("home", linear_m_per_sec=1.0)
            assert result == self.navigation.STATUS

    async def test_go_to_point(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            result = await client.go_to_point(DESTINATION)
            assert result == self.navigation.STATUS

    async def test_suspend(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            result = await client.suspend("paused for safety")
            assert result == self.navigation.STATUS
            assert self.navigation.calls["suspend"] == ("paused for safety",)

    async def test_resume(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            result = await client.resume()
            assert result == self.navigation.STATUS

    async def test_cancel(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            result = await client.cancel()
            assert result == self.navigation.STATUS

    async def test_get_position(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            result = await client.get_position()
            assert result == self.navigation.POSITION

    async def test_get_navigation_status(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            result = await client.get_navigation_status()
            assert result == self.navigation.STATUS

    async def test_get_properties(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            result = await client.get_properties()
            assert result == self.navigation.PROPERTIES

    async def test_get_costmap(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            result = await client.get_costmap()
            assert result == self.navigation.COSTMAP

    async def test_do(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            command = {"command": "args"}
            response = await client.do_command(command)
            assert response == {"command": command}

    async def test_get_status(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            status = await client.get_status()
            assert status == {}
