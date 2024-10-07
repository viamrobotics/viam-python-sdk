from grpclib.testing import ChannelFor

from viam.proto.common import DoCommandRequest, DoCommandResponse, GeoPoint
from viam.proto.service.navigation import (
    AddWaypointRequest,
    GetLocationRequest,
    GetLocationResponse,
    GetModeRequest,
    GetModeResponse,
    GetObstaclesRequest,
    GetObstaclesResponse,
    GetPropertiesRequest,
    GetPropertiesResponse,
    GetWaypointsRequest,
    GetWaypointsResponse,
    MapType,
    Mode,
    NavigationServiceStub,
    RemoveWaypointRequest,
    SetModeRequest,
)
from viam.resource.manager import ResourceManager
from viam.services.navigation import NavigationClient, NavigationRPCService
from viam.utils import dict_to_struct, struct_to_dict

from .mocks.services import MockNavigation


class TestNavigationService:
    name = "navigation"
    navigation = MockNavigation(name="navigation")

    async def test_get_location(self):
        result = await self.navigation.get_location()
        assert result == MockNavigation.LOCATION

    async def test_get_obstacles(self):
        result = await self.navigation.get_obstacles()
        assert result == MockNavigation.OBSTACLES

    async def test_get_waypoints(self):
        result = await self.navigation.get_waypoints()
        assert result == self.navigation.WAYPOINTS

    async def test_add_waypoint(self):
        assert self.navigation.add_waypoints == []
        point = GeoPoint(latitude=100.0, longitude=200.0)
        await self.navigation.add_waypoint(point)
        assert self.navigation.add_waypoints == [point]

    async def test_remove_waypoint(self):
        assert self.navigation.remove_waypoints == []
        id = "xyz"
        await self.navigation.remove_waypoint(id)
        assert self.navigation.remove_waypoints == [id]

    async def test_get_mode(self):
        result = await self.navigation.get_mode()
        assert result == Mode.MODE_UNSPECIFIED

    async def test_set_mode(self):
        assert self.navigation.mode == Mode.MODE_UNSPECIFIED
        mode = Mode.MODE_MANUAL
        await self.navigation.set_mode(mode)
        assert self.navigation.mode == mode

    async def test_get_properties(self):
        assert self.navigation.map_type == MapType.MAP_TYPE_UNSPECIFIED
        result = await self.navigation.get_properties()
        assert self.navigation.map_type == result

    async def test_do(self):
        command = {"command": "args"}
        result = await self.navigation.do_command(command)
        assert result == {"command": command}


class TestService:
    @classmethod
    def setup_class(cls):
        cls.name = "navigation"
        cls.navigation = MockNavigation(name=cls.name)
        cls.manager = ResourceManager([cls.navigation])
        cls.service = NavigationRPCService(cls.manager)

    async def test_get_location(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            request = GetLocationRequest(name=self.name)
            response: GetLocationResponse = await client.GetLocation(request)
            result = response.location
            assert result == self.navigation.LOCATION

    async def test_get_obstacles(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            request = GetObstaclesRequest(name=self.name)
            response: GetObstaclesResponse = await client.GetObstacles(request)
            result = response.obstacles
            assert result == self.navigation.OBSTACLES

    async def test_get_waypoints(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            request = GetWaypointsRequest(name=self.name)
            response: GetWaypointsResponse = await client.GetWaypoints(request)
            result = response.waypoints
            assert result == self.navigation.WAYPOINTS

    async def test_add_waypoint(self):
        async with ChannelFor([self.service]) as channel:
            assert self.navigation.add_waypoints == []
            client = NavigationServiceStub(channel)
            point = GeoPoint(latitude=100.0, longitude=200.0)
            request = AddWaypointRequest(name=self.name, location=point)
            await client.AddWaypoint(request)
            assert self.navigation.add_waypoints == [point]

    async def test_remove_waypoint(self):
        async with ChannelFor([self.service]) as channel:
            assert self.navigation.remove_waypoints == []
            client = NavigationServiceStub(channel)
            id = "xyz"
            request = RemoveWaypointRequest(name=self.name, id=id)
            await client.RemoveWaypoint(request)
            assert self.navigation.remove_waypoints == [id]

    async def test_get_mode(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            request = GetModeRequest(name=self.name)
            response: GetModeResponse = await client.GetMode(request)
            result = response.mode
            assert result == Mode.MODE_UNSPECIFIED

    async def test_set_mode(self):
        async with ChannelFor([self.service]) as channel:
            assert self.navigation.mode == Mode.MODE_UNSPECIFIED
            client = NavigationServiceStub(channel)
            mode = Mode.MODE_MANUAL
            request = SetModeRequest(name=self.name, mode=mode)
            await client.SetMode(request)
            assert self.navigation.mode == Mode.MODE_MANUAL

    async def test_get_properties(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            request = GetPropertiesRequest(name=self.name)
            response: GetPropertiesResponse = await client.GetProperties(request)
            result = response.map_type
            assert result == MapType.MAP_TYPE_UNSPECIFIED

    async def test_do(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationServiceStub(channel)
            command = {"command": "args"}
            request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
            response: DoCommandResponse = await client.DoCommand(request)
            result = struct_to_dict(response.result)
            assert result == {"command": command}


class TestClient:
    @classmethod
    def setup_class(cls):
        cls.name = "navigation"
        cls.navigation = MockNavigation(name=cls.name)
        cls.manager = ResourceManager([cls.navigation])
        cls.service = NavigationRPCService(cls.manager)

    async def test_get_location(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            result = await client.get_location()
            assert result == self.navigation.LOCATION

    async def test_get_obstacles(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            result = await client.get_obstacles()
            assert result == self.navigation.OBSTACLES

    async def test_get_waypoints(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            result = await client.get_waypoints()
            assert result == self.navigation.WAYPOINTS

    async def test_add_waypoint(self):
        async with ChannelFor([self.service]) as channel:
            assert self.navigation.add_waypoints == []
            client = NavigationClient(self.name, channel)
            point = GeoPoint(latitude=100.0, longitude=200.0)
            await client.add_waypoint(point)
            assert self.navigation.add_waypoints == [point]

    async def test_remove_waypoint(self):
        async with ChannelFor([self.service]) as channel:
            assert self.navigation.remove_waypoints == []
            client = NavigationClient(self.name, channel)
            id = "xyz"
            await client.remove_waypoint(id)
            assert self.navigation.remove_waypoints == [id]

    async def test_get_mode(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            result = await client.get_mode()
            assert result == Mode.MODE_UNSPECIFIED

    async def test_set_mode(self):
        async with ChannelFor([self.service]) as channel:
            assert self.navigation.mode == Mode.MODE_UNSPECIFIED
            client = NavigationClient(self.name, channel)
            mode = Mode.MODE_MANUAL
            await client.set_mode(mode)
            assert self.navigation.mode == Mode.MODE_MANUAL

    async def test_get_properties(self):
        async with ChannelFor([self.service]) as channel:
            assert self.navigation.map_type == MapType.MAP_TYPE_UNSPECIFIED
            client = NavigationClient(self.name, channel)
            result = await client.get_properties()
            assert self.navigation.map_type == result

    async def test_do(self):
        async with ChannelFor([self.service]) as channel:
            client = NavigationClient(self.name, channel)
            command = {"command": "args"}
            response = await client.do_command(command)
            assert response == {"command": command}
