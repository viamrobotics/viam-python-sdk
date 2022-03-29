import pytest
from grpclib.testing import ChannelFor
from viam.components.gps import GPS, GPSClient
from viam.components.gps.service import GPSService
from viam.components.resource_manager import ResourceManager
from viam.proto.api.common import GeoPoint
from viam.proto.api.component.gps import (GPSServiceStub, ReadAltitudeRequest,
                                          ReadAltitudeResponse,
                                          ReadLocationRequest,
                                          ReadLocationResponse,
                                          ReadSpeedRequest, ReadSpeedResponse)

from .mocks.components import MockGPS

POINT = GPS.Point(40.664679865782624, -73.97668056188789)
ALTITUDE = 15
SPEED = 1341.12


@pytest.fixture(scope='function')
def gps() -> GPS:
    return MockGPS('gps', POINT, ALTITUDE, SPEED)


@pytest.fixture(scope='function')
def service(gps: GPS) -> GPSService:
    rm = ResourceManager([gps])
    return GPSService(rm)


class TestGPS:

    @pytest.mark.asyncio
    async def test_read_location(self, gps: GPS):
        loc = await gps.read_location()
        assert loc == POINT

    @pytest.mark.asyncio
    async def test_read_altitude(self, gps: GPS):
        alt = await gps.read_altitude()
        assert alt == ALTITUDE

    @pytest.mark.asyncio
    async def test_read_speed(self, gps: GPS):
        speed = await gps.read_speed()
        assert speed == SPEED


class TestService:

    @pytest.mark.asyncio
    async def test_read_location(self, gps: GPS, service: GPSService):
        async with ChannelFor([service]) as channel:
            client = GPSServiceStub(channel)
            request = ReadLocationRequest(name=gps.name)
            response: ReadLocationResponse = await client.ReadLocation(request)
            point: GeoPoint = response.coordinate
            assert GPS.Point(point.latitude, point.longitude) == POINT

    @pytest.mark.asyncio
    async def test_read_altitude(self, gps: GPS, service: GPSService):
        async with ChannelFor([service]) as channel:
            client = GPSServiceStub(channel)
            request = ReadAltitudeRequest(name=gps.name)
            response: ReadAltitudeResponse = await client.ReadAltitude(request)
            assert response.altitude_meters == ALTITUDE

    @pytest.mark.asyncio
    async def test_read_speed(self, gps: GPS, service: GPSService):
        async with ChannelFor([service]) as channel:
            client = GPSServiceStub(channel)
            request = ReadSpeedRequest(name=gps.name)
            response: ReadSpeedResponse = await client.ReadSpeed(request)
            assert response.speed_mm_per_sec == SPEED


class TestClient:

    @pytest.mark.asyncio
    async def test_read_location(self, gps: GPS, service: GPSService):
        async with ChannelFor([service]) as channel:
            client = GPSClient(gps.name, channel)
            loc = await client.read_location()
            assert loc == POINT

    @pytest.mark.asyncio
    async def test_read_altitude(self, gps: GPS, service: GPSService):
        async with ChannelFor([service]) as channel:
            client = GPSClient(gps.name, channel)
            alt = await client.read_altitude()
            assert alt == ALTITUDE

    @pytest.mark.asyncio
    async def test_read_speed(self, gps: GPS, service: GPSService):
        async with ChannelFor([service]) as channel:
            client = GPSClient(gps.name, channel)
            speed = await client.read_speed()
            assert speed == SPEED
