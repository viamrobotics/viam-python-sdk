from grpclib.testing import ChannelFor
import pytest

from viam.components.resource_manager import ResourceManager
from viam.components.sensor import SensorService, SensorClient
from viam.proto.api.component.sensor import (
    SensorServiceStub,
    GetReadingsRequest, GetReadingsResponse,
)
from viam.utils import primitive_to_value

from .mocks.components import MockSensor


class TestSensor:

    sensor = MockSensor(name='sensor', result=[1, 2, 3])

    @pytest.mark.asyncio
    async def test_get_readings(self):
        readings = await self.sensor.get_readings()
        assert readings == [1, 2, 3]


class TestService:

    name = 'sensor'
    readings = [1, 2, 3]
    sensor = MockSensor(name=name, result=readings)
    manager = ResourceManager([sensor])
    service = SensorService(manager)

    @pytest.mark.asyncio
    async def test_get_readings(self):
        async with ChannelFor([self.service]) as channel:
            client = SensorServiceStub(channel)
            request = GetReadingsRequest(name=self.name)
            result: GetReadingsResponse = await client.GetReadings(request)
            value_readings = []
            for reading in self.readings:
                value_readings.append(primitive_to_value(reading))
            assert list(result.readings) == value_readings


class TestClient:

    name = 'sensor'
    readings = [1, 2, 3]
    sensor = MockSensor(name=name, result=readings)
    manager = ResourceManager([sensor])
    service = SensorService(manager)

    @pytest.mark.asyncio
    async def test_get_readings(self):
        async with ChannelFor([self.service]) as channel:
            client = SensorClient(self.name, channel)
            value_readings = await client.get_readings()
            assert self.readings == value_readings
